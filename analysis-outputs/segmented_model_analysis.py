#!/usr/bin/env python3
"""Segmented logistic analysis for trend-following backtests.

Builds on `statistical_analysis.py` by fitting:
  1. An overall profitability model with sector interactions.
  2. Sector-specific logistic regressions (focus on strategy traits).
  3. Strategy-specific logistic regressions (focus on sector effects).

Outputs CSV summaries inside `statistical_outputs/segmented_models/` so we can
compare how profit targets, pyramiding, and sector choices behave under
different regimes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from patsy import dmatrices
import warnings


DEFAULT_CSV_PATH = Path(__file__).resolve().parent.parent / 'cleaned-data.csv'
OUTPUT_ROOT = Path(__file__).resolve().parent / 'statistical_outputs' / 'segmented_models'


@dataclass
class SegmentResult:
    """Container for storing per-segment model results."""

    segment: str
    n_obs: int
    results: pd.DataFrame


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Mirror the feature engineering used in `statistical_analysis.py`."""

    sector_map = {
        # Healthcare
        'UNH': 'Healthcare', 'XLV': 'Healthcare',
        # Technology
        'MSFT': 'Technology', 'GOOGL': 'Technology', 'QQQ': 'Technology',
        # Consumer Discretionary
        'AMZN': 'Consumer_Disc', 'XLY': 'Consumer_Disc',
        # Consumer Staples
        'WMT': 'Consumer_Staples', 'XLP': 'Consumer_Staples',
        # Financials
        'JPM': 'Financials', 'XLF': 'Financials',
        # Industrials
        'CAT': 'Industrials', 'XLI': 'Industrials',
        # Energy
        'XOM': 'Energy', 'XLE': 'Energy',
        # Real Estate
        'PLD': 'Real_Estate', 'XLRE': 'Real_Estate',
        # Utilities
        'DUK': 'Utilities', 'XLU': 'Utilities',
        # Materials
        'FCX': 'Materials',
        # Broad Market
        'SPY': 'Broad_Market',
    }

    df = df.copy()
    df['sector'] = df['ticker'].map(sector_map)

    etfs = {'SPY', 'QQQ', 'XLE', 'XLF', 'XLV', 'XLI', 'XLP', 'XLY', 'XLRE', 'XLU'}
    df['asset_type'] = df['ticker'].apply(lambda x: 'ETF' if x in etfs else 'Stock')

    df['has_profit_targets'] = df['strategy'].isin(['Alt10', 'Alt43', 'Alt46', 'Alt47'])
    df['has_pyramiding'] = df['strategy'].isin(['Alt15', 'Alt26', 'Alt39', 'Alt45'])
    df['has_time_exit'] = df['strategy'] == 'Alt9'
    df['has_sar'] = df['strategy'] == 'Alt22'
    df['has_filters'] = df['strategy'].isin(['Alt28', 'Alt44'])

    df['is_profitable'] = df['total_return_pct'] > 0
    df['is_very_profitable'] = df['total_return_pct'] > 20
    df['low_drawdown'] = df['max_drawdown_pct'] < 10

    df['profit_factor'] = pd.to_numeric(df['profit_factor'], errors='coerce')

    return df


def bool_to_int(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    df = df.copy()
    for column in columns:
        if column in df.columns:
            df[column] = df[column].astype(int)
    return df


def fit_logistic(formula: str, data: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    y, X = dmatrices(formula, data, return_type='dataframe')

    zero_var_cols = [col for col in X.columns if col != 'Intercept' and X[col].nunique() <= 1]
    if zero_var_cols:
        X = X.drop(columns=zero_var_cols)

    duplicated_cols = X.columns[X.T.duplicated(keep='first')]
    if not duplicated_cols.empty:
        X = X.drop(columns=list(duplicated_cols))

    model = sm.Logit(y, X).fit(method='bfgs', disp=0)
    params = model.params
    odds_ratios = np.exp(params)
    conf_int = np.exp(model.conf_int())
    conf_int.columns = ['Lower_CI', 'Upper_CI']

    results = pd.DataFrame({
        'Coefficient': params,
        'Odds_Ratio': odds_ratios,
        'Lower_CI': conf_int['Lower_CI'],
        'Upper_CI': conf_int['Upper_CI'],
        'P_Value': model.pvalues,
    })
    results.index.name = 'term'
    return results, int(model.nobs)


def run_overall_interaction_model(df: pd.DataFrame, out_dir: Path) -> Optional[pd.DataFrame]:
    cols = ['is_profitable', 'sector', 'has_profit_targets', 'has_pyramiding', 'asset_type', 'trades']
    data = df[cols].dropna().copy()
    if data.empty:
        return None

    data = bool_to_int(data, ['is_profitable', 'has_profit_targets', 'has_pyramiding'])

    formula = 'is_profitable ~ has_profit_targets * C(sector) + has_pyramiding * C(sector) + C(asset_type) + trades'
    results, n_obs = fit_logistic(formula, data)
    results.insert(0, 'n_obs', n_obs)
    output_path = out_dir / 'logit_overall_sector_interactions.csv'
    results.to_csv(output_path)
    return results


PredictorSpec = Tuple[str, str]


def build_formula(data: pd.DataFrame, predictors: List[PredictorSpec]) -> Tuple[str, List[str]]:
    """Create a logistic formula by dropping predictors with no variation."""

    terms: List[str] = []
    bool_columns: List[str] = []

    for column, kind in predictors:
        if column not in data.columns:
            continue
        # Skip predictors with only one level after dropping NA.
        unique_vals = data[column].dropna().unique()
        if len(unique_vals) <= 1:
            continue

        if kind == 'boolean':
            terms.append(column)
            bool_columns.append(column)
        elif kind == 'categorical':
            terms.append(f'C({column})')
        elif kind == 'numeric':
            terms.append(column)
        else:
            raise ValueError(f"Unknown predictor kind '{kind}' for column '{column}'.")

    if not terms:
        raise ValueError('No varying predictors available for the segment.')

    return f'is_profitable ~ ' + ' + '.join(terms), bool_columns


def run_segment_models(
    df: pd.DataFrame,
    segment_col: str,
    predictors: List[PredictorSpec],
    min_obs: int,
    segment_label: str,
    out_dir: Path,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    rows: List[pd.DataFrame] = []
    failures: List[Dict[str, str]] = []

    for segment, seg_df in df.groupby(segment_col):
        working = seg_df[['is_profitable'] + [p[0] for p in predictors]].dropna().copy()
        if len(working) < min_obs:
            failures.append({'segment': str(segment), 'reason': f'Insufficient observations (n={len(working)})'})
            continue

        try:
            formula, bool_cols = build_formula(working, predictors)
            working = bool_to_int(working, ['is_profitable', *bool_cols])
            result_df, n_obs = fit_logistic(formula, working)
            result_df.insert(0, segment_label, segment)
            result_df.insert(1, 'n_obs', n_obs)
            rows.append(result_df.reset_index())
        except Exception as exc:  # noqa: BLE001
            failures.append({'segment': str(segment), 'reason': str(exc)})

    if rows:
        combined = pd.concat(rows, ignore_index=True)
        combined.to_csv(out_dir / f'logit_by_{segment_label.lower()}.csv', index=False)
    else:
        combined = pd.DataFrame()

    failures_df = pd.DataFrame(failures)
    if not failures_df.empty:
        failures_df.to_csv(out_dir / f'logit_by_{segment_label.lower()}_failures.csv', index=False)

    return combined, failures_df


def main(csv_path: Path) -> None:
    warnings.filterwarnings('ignore')

    print("=" * 80)
    print("SEGMENTED LOGISTIC ANALYSIS")
    print("=" * 80)
    print(f"Loading data from: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows")
    df = engineer_features(df)
    df = df.dropna(subset=['sector'])
    print(f"Usable rows after feature engineering: {len(df)}\n")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    print("Running overall profitability model with sector interactions...")
    overall_results = run_overall_interaction_model(df, OUTPUT_ROOT)
    if overall_results is not None:
        print(f"  ✓ Saved: {OUTPUT_ROOT / 'logit_overall_sector_interactions.csv'}")
    else:
        print("  ! Skipped overall model (no data)")
    print()

    print("Running sector-specific logistic models (strategy traits focus)...")
    sector_predictors: List[PredictorSpec] = [
        ('has_profit_targets', 'boolean'),
        ('has_pyramiding', 'boolean'),
        ('asset_type', 'categorical'),
        ('trades', 'numeric'),
    ]
    sector_results, sector_failures = run_segment_models(
        df,
        segment_col='sector',
        predictors=sector_predictors,
        min_obs=12,
        segment_label='sector',
        out_dir=OUTPUT_ROOT,
    )
    if not sector_results.empty:
        print(f"  ✓ Saved: {OUTPUT_ROOT / 'logit_by_sector.csv'}")
    if not sector_failures.empty:
        print("  ! Some sectors skipped:")
        for row in sector_failures.itertuples():
            print(f"    - {row.segment}: {row.reason}")
    print()

    print("Running strategy-specific logistic models (sector effects focus)...")
    strategy_predictors: List[PredictorSpec] = [
        ('sector', 'categorical'),
        ('has_profit_targets', 'boolean'),
        ('has_pyramiding', 'boolean'),
        ('asset_type', 'categorical'),
        ('trades', 'numeric'),
    ]
    strategy_results, strategy_failures = run_segment_models(
        df,
        segment_col='strategy',
        predictors=strategy_predictors,
        min_obs=15,
        segment_label='strategy',
        out_dir=OUTPUT_ROOT,
    )
    if not strategy_results.empty:
        print(f"  ✓ Saved: {OUTPUT_ROOT / 'logit_by_strategy.csv'}")
    if not strategy_failures.empty:
        print("  ! Some strategies skipped:")
        for row in strategy_failures.itertuples():
            print(f"    - {row.segment}: {row.reason}")

    print("\nAnalysis complete. Segmented outputs stored in:")
    print(f"  {OUTPUT_ROOT}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Segmented logistic profitability models.')
    parser.add_argument(
        '--csv',
        type=Path,
        default=DEFAULT_CSV_PATH,
        help='Path to cleaned CSV (defaults to ../cleaned-data.csv)',
    )
    args = parser.parse_args()
    main(args.csv)

