#!/usr/bin/env python3
"""
Statistical Analysis of Trend-Following Backtests
==================================================

Analyzes 293 validated backtests to quantify:
1. Sector effects on profitability
2. Strategy feature importance (profit targets, pyramiding, filters)
3. Correlation between performance metrics
4. Predictive models for success

Usage:
    python statistical_analysis.py

Output:
    - Console: Regression summaries, feature importance
    - Files: correlation_matrix.png, sector_performance.png, etc.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import logit, ols
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from scipy import stats
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


class TradingAnalysis:
    """Complete statistical analysis of backtest data"""

    def __init__(self, csv_path='../cleaned-data.csv'):
        """Load and prepare data"""
        print("=" * 80)
        print("STATISTICAL ANALYSIS: Trend-Following Backtests")
        print("=" * 80)
        print(f"\nLoading data from: {csv_path}")

        self.df = pd.read_csv(csv_path)
        print(f"Loaded {len(self.df)} backtest results")

        # Create output directory
        self.output_dir = Path('statistical_outputs')
        self.output_dir.mkdir(exist_ok=True)
        print(f"Output directory: {self.output_dir.absolute()}\n")

        # Feature engineering
        self._engineer_features()

    def _engineer_features(self):
        """Create analysis features from raw data"""
        print("Engineering features...")

        # Sector mapping
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
        self.df['sector'] = self.df['ticker'].map(sector_map)

        # Asset type
        etfs = ['SPY', 'QQQ', 'XLE', 'XLF', 'XLV', 'XLI', 'XLP', 'XLY', 'XLRE', 'XLU']
        self.df['asset_type'] = self.df['ticker'].apply(
            lambda x: 'ETF' if x in etfs else 'Stock'
        )

        # Strategy features
        self.df['has_profit_targets'] = self.df['strategy'].isin(
            ['Alt10', 'Alt43', 'Alt46', 'Alt47']
        )
        self.df['has_pyramiding'] = self.df['strategy'].isin(
            ['Alt15', 'Alt26', 'Alt39', 'Alt45']
        )
        self.df['has_time_exit'] = self.df['strategy'] == 'Alt9'
        self.df['has_sar'] = self.df['strategy'] == 'Alt22'
        self.df['has_filters'] = self.df['strategy'].isin(['Alt28', 'Alt44'])

        # Performance categories
        self.df['is_profitable'] = self.df['total_return_pct'] > 0
        self.df['is_very_profitable'] = self.df['total_return_pct'] > 20
        self.df['low_drawdown'] = self.df['max_drawdown_pct'] < 10

        # Handle missing/invalid profit factors
        self.df['profit_factor'] = pd.to_numeric(self.df['profit_factor'], errors='coerce')
        self.df['log_pf'] = np.log(self.df['profit_factor'].replace([np.inf, -np.inf], np.nan))

        # Exit frequency tier (based on trades)
        self.df['exit_frequency'] = pd.cut(
            self.df['trades'],
            bins=[0, 30, 60, 100, 500],
            labels=['Low', 'Medium', 'High', 'Very_High']
        )

        print(f"  - Created sector mapping for {self.df['sector'].notna().sum()} tickers")
        print(f"  - Identified {self.df['asset_type'].value_counts().to_dict()}")
        print(f"  - Profitable results: {self.df['is_profitable'].sum()}/{len(self.df)} ({100*self.df['is_profitable'].mean():.1f}%)")
        print()

    def descriptive_statistics(self):
        """Generate descriptive statistics"""
        print("\n" + "=" * 80)
        print("DESCRIPTIVE STATISTICS")
        print("=" * 80 + "\n")

        # Overall performance
        print("Overall Performance Metrics:")
        print("-" * 40)
        metrics = ['total_return_pct', 'profit_factor', 'win_rate_pct', 'max_drawdown_pct', 'trades']
        print(self.df[metrics].describe().round(2))
        print()

        # Sector performance
        print("\nSector Performance Summary:")
        print("-" * 40)
        sector_stats = self.df.groupby('sector').agg({
            'is_profitable': ['sum', 'count', 'mean'],
            'total_return_pct': 'mean',
            'profit_factor': 'mean',
        }).round(2)
        sector_stats.columns = ['Profitable', 'Total', 'Win_Rate', 'Avg_Return', 'Avg_PF']
        sector_stats = sector_stats.sort_values('Win_Rate', ascending=False)
        print(sector_stats)
        print()

        # Strategy performance
        print("\nStrategy Performance Summary:")
        print("-" * 40)
        strategy_stats = self.df.groupby('strategy').agg({
            'is_profitable': ['sum', 'count', 'mean'],
            'total_return_pct': 'mean',
            'trades': 'mean',
        }).round(2)
        strategy_stats.columns = ['Profitable', 'Total', 'Win_Rate', 'Avg_Return', 'Avg_Trades']
        strategy_stats = strategy_stats.sort_values('Win_Rate', ascending=False)
        print(strategy_stats)
        print()

    def correlation_analysis(self):
        """Analyze correlations between metrics"""
        print("\n" + "=" * 80)
        print("CORRELATION ANALYSIS")
        print("=" * 80 + "\n")

        # Select numeric columns
        corr_cols = ['total_return_pct', 'profit_factor', 'win_rate_pct',
                     'max_drawdown_pct', 'trades']
        corr_data = self.df[corr_cols].dropna()

        # Calculate correlation matrix
        corr_matrix = corr_data.corr()
        print("Correlation Matrix:")
        print("-" * 40)
        print(corr_matrix.round(3))
        print()

        # Visualize
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
                   square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Performance Metrics Correlation Matrix', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(self.output_dir / 'correlation_matrix.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'correlation_matrix.png'}")
        plt.close()

        # Key insights
        print("\nKey Correlation Insights:")
        print("-" * 40)
        print(f"  • Return vs Profit Factor: {corr_matrix.loc['total_return_pct', 'profit_factor']:.3f}")
        print(f"  • Return vs Win Rate: {corr_matrix.loc['total_return_pct', 'win_rate_pct']:.3f}")
        print(f"  • Return vs Max Drawdown: {corr_matrix.loc['total_return_pct', 'max_drawdown_pct']:.3f}")
        print(f"  • Win Rate vs Profit Factor: {corr_matrix.loc['win_rate_pct', 'profit_factor']:.3f}")
        print()

    def logistic_regression_profitability(self):
        """Logistic regression: Predict profitability"""
        print("\n" + "=" * 80)
        print("LOGISTIC REGRESSION: Predicting Profitability")
        print("=" * 80 + "\n")

        # Prepare data
        model_data = self.df[['is_profitable', 'sector', 'has_profit_targets',
                              'has_pyramiding', 'asset_type', 'trades']].dropna()

        # Create formula
        formula = 'is_profitable ~ C(sector) + has_profit_targets + has_pyramiding + C(asset_type) + trades'

        # Fit model
        print("Fitting logistic regression model...")
        print(f"Formula: {formula}")
        print(f"Sample size: {len(model_data)}\n")

        model = logit(formula, data=model_data).fit(disp=0)

        # Print summary
        print(model.summary())
        print("\n")

        # Calculate odds ratios
        print("Odds Ratios (Interpretation):")
        print("-" * 60)
        params = model.params
        odds_ratios = np.exp(params)
        conf_int = np.exp(model.conf_int())
        conf_int.columns = ['Lower_CI', 'Upper_CI']

        results = pd.DataFrame({
            'Coefficient': params,
            'Odds_Ratio': odds_ratios,
            'Lower_CI': conf_int['Lower_CI'],
            'Upper_CI': conf_int['Upper_CI'],
            'P_Value': model.pvalues
        })

        print(results.round(3))
        print()

        # Key insights
        print("\nKey Insights:")
        print("-" * 60)
        if 'has_profit_targets[T.True]' in odds_ratios.index:
            pt_or = odds_ratios['has_profit_targets[T.True]']
            print(f"  • Profit Targets: {pt_or:.2f}x odds of profitability")
        if 'has_pyramiding[T.True]' in odds_ratios.index:
            pyr_or = odds_ratios['has_pyramiding[T.True]']
            print(f"  • Pyramiding: {pyr_or:.2f}x odds of profitability")
        if 'C(asset_type)[T.Stock]' in odds_ratios.index:
            stock_or = odds_ratios['C(asset_type)[T.Stock]']
            print(f"  • Stocks vs ETFs: {stock_or:.2f}x odds of profitability")

        # Healthcare effect
        healthcare_params = [p for p in odds_ratios.index if 'Healthcare' in p]
        if healthcare_params:
            hc_or = odds_ratios[healthcare_params[0]]
            print(f"  • Healthcare Sector: {hc_or:.2f}x odds vs baseline")

        print()

        # Save to file
        results.to_csv(self.output_dir / 'logistic_regression_results.csv')
        print(f"  ✓ Saved: {self.output_dir / 'logistic_regression_results.csv'}\n")

    def linear_regression_profit_factor(self):
        """Linear regression: Predict profit factor"""
        print("\n" + "=" * 80)
        print("LINEAR REGRESSION: Predicting Profit Factor")
        print("=" * 80 + "\n")

        # Prepare data (filter out invalid profit factors)
        model_data = self.df[
            (self.df['profit_factor'].notna()) &
            (self.df['profit_factor'] > 0) &
            (self.df['profit_factor'] != np.inf)
        ].copy()

        model_data['log_pf'] = np.log(model_data['profit_factor'])

        # Create formula
        formula = 'log_pf ~ C(sector) + win_rate_pct + trades + has_profit_targets'

        # Fit model
        print("Fitting linear regression model (log-transformed Profit Factor)...")
        print(f"Formula: {formula}")
        print(f"Sample size: {len(model_data)}\n")

        model = ols(formula, data=model_data).fit()

        # Print summary
        print(model.summary())
        print("\n")

        # Key insights
        print("Key Insights:")
        print("-" * 60)
        print(f"  • R-squared: {model.rsquared:.3f} ({100*model.rsquared:.1f}% variance explained)")
        print(f"  • Win Rate coefficient: {model.params['win_rate_pct']:.4f}")
        print(f"    → 1% increase in win rate = {100*(np.exp(model.params['win_rate_pct'])-1):.2f}% increase in PF")

        if 'has_profit_targets[T.True]' in model.params.index:
            pt_coef = model.params['has_profit_targets[T.True]']
            print(f"  • Profit Targets effect: {100*(np.exp(pt_coef)-1):.1f}% increase in PF")

        print()

        # Save to file
        results = pd.DataFrame({
            'Coefficient': model.params,
            'Std_Error': model.bse,
            'T_Stat': model.tvalues,
            'P_Value': model.pvalues
        })
        results.to_csv(self.output_dir / 'linear_regression_results.csv')
        print(f"  ✓ Saved: {self.output_dir / 'linear_regression_results.csv'}\n")

    def feature_importance_analysis(self):
        """Random Forest feature importance"""
        print("\n" + "=" * 80)
        print("FEATURE IMPORTANCE: Random Forest Classification")
        print("=" * 80 + "\n")

        # Prepare features
        features = ['has_profit_targets', 'has_pyramiding', 'has_time_exit',
                   'has_sar', 'has_filters', 'win_rate_pct', 'trades', 'max_drawdown_pct']

        # Add sector dummies
        sector_dummies = pd.get_dummies(self.df['sector'], prefix='sector')
        asset_dummies = pd.get_dummies(self.df['asset_type'], prefix='asset')

        X = pd.concat([
            self.df[features],
            sector_dummies,
            asset_dummies
        ], axis=1).dropna()

        y = self.df.loc[X.index, 'is_profitable']

        # Train Random Forest
        print("Training Random Forest Classifier...")
        print(f"Features: {len(X.columns)}")
        print(f"Sample size: {len(X)}\n")

        rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        rf.fit(X, y)

        # Cross-validation score
        cv_scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
        print(f"Cross-Validation Accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
        print()

        # Feature importance
        importance = pd.DataFrame({
            'feature': X.columns,
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=False)

        print("Top 15 Most Important Features:")
        print("-" * 60)
        print(importance.head(15).to_string(index=False))
        print()

        # Visualize top features
        top_n = 15
        plt.figure(figsize=(10, 8))
        top_features = importance.head(top_n)
        plt.barh(range(len(top_features)), top_features['importance'])
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Importance', fontsize=12)
        plt.ylabel('Feature', fontsize=12)
        plt.title('Top 15 Features Predicting Profitability', fontsize=14, fontweight='bold')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig(self.output_dir / 'feature_importance.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'feature_importance.png'}")
        plt.close()

        # Save to file
        importance.to_csv(self.output_dir / 'feature_importance.csv', index=False)
        print(f"  ✓ Saved: {self.output_dir / 'feature_importance.csv'}\n")

    def visualizations(self):
        """Create key visualizations"""
        print("\n" + "=" * 80)
        print("GENERATING VISUALIZATIONS")
        print("=" * 80 + "\n")

        # 1. Sector performance box plot
        plt.figure(figsize=(14, 8))
        sector_order = self.df.groupby('sector')['total_return_pct'].median().sort_values(ascending=False).index
        sns.boxplot(data=self.df, x='sector', y='total_return_pct', order=sector_order)
        plt.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Break-even')
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Sector', fontsize=12)
        plt.ylabel('Total Return (%)', fontsize=12)
        plt.title('Return Distribution by Sector', fontsize=14, fontweight='bold')
        plt.legend()
        plt.tight_layout()
        plt.savefig(self.output_dir / 'sector_performance_boxplot.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'sector_performance_boxplot.png'}")
        plt.close()

        # 2. Strategy performance
        plt.figure(figsize=(14, 8))
        strategy_order = self.df.groupby('strategy')['total_return_pct'].median().sort_values(ascending=False).index
        sns.boxplot(data=self.df, x='strategy', y='total_return_pct', order=strategy_order)
        plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Strategy', fontsize=12)
        plt.ylabel('Total Return (%)', fontsize=12)
        plt.title('Return Distribution by Strategy', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(self.output_dir / 'strategy_performance_boxplot.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'strategy_performance_boxplot.png'}")
        plt.close()

        # 3. Risk-Return scatter by sector
        plt.figure(figsize=(12, 8))
        for sector in self.df['sector'].unique():
            sector_data = self.df[self.df['sector'] == sector]
            plt.scatter(sector_data['max_drawdown_pct'],
                       sector_data['total_return_pct'],
                       label=sector, alpha=0.6, s=100)
        plt.xlabel('Maximum Drawdown (%)', fontsize=12)
        plt.ylabel('Total Return (%)', fontsize=12)
        plt.title('Risk-Return Profile by Sector', fontsize=14, fontweight='bold')
        plt.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / 'risk_return_scatter.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'risk_return_scatter.png'}")
        plt.close()

        # 4. Win rate vs trades
        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(self.df['trades'], self.df['win_rate_pct'],
                            c=self.df['total_return_pct'], cmap='RdYlGn',
                            s=100, alpha=0.6, edgecolors='black', linewidth=0.5)
        plt.colorbar(scatter, label='Total Return (%)')
        plt.xlabel('Number of Trades', fontsize=12)
        plt.ylabel('Win Rate (%)', fontsize=12)
        plt.title('Win Rate vs Trade Frequency (colored by Return)', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / 'winrate_vs_trades.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'winrate_vs_trades.png'}")
        plt.close()

        # 5. Sector win rate comparison
        sector_stats = self.df.groupby('sector').agg({
            'is_profitable': 'mean',
            'total_return_pct': 'count'
        }).reset_index()
        sector_stats.columns = ['sector', 'win_rate', 'count']
        sector_stats = sector_stats.sort_values('win_rate', ascending=False)

        plt.figure(figsize=(12, 6))
        bars = plt.bar(range(len(sector_stats)), sector_stats['win_rate'],
                      color=['green' if x > 0.5 else 'red' for x in sector_stats['win_rate']],
                      alpha=0.7, edgecolor='black')
        plt.xticks(range(len(sector_stats)), sector_stats['sector'], rotation=45, ha='right')
        plt.ylabel('Win Rate (% Profitable)', fontsize=12)
        plt.xlabel('Sector', fontsize=12)
        plt.title('Sector Success Rate (% of Strategies Profitable)', fontsize=14, fontweight='bold')
        plt.axhline(y=0.5, color='blue', linestyle='--', alpha=0.5, label='50% threshold')

        # Add count labels on bars
        for i, (bar, count) in enumerate(zip(bars, sector_stats['count'])):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1%}\n(n={count})',
                    ha='center', va='bottom', fontsize=9)

        plt.legend()
        plt.tight_layout()
        plt.savefig(self.output_dir / 'sector_win_rate.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir / 'sector_win_rate.png'}")
        plt.close()

        print()

    def hypothesis_tests(self):
        """Statistical hypothesis testing"""
        print("\n" + "=" * 80)
        print("HYPOTHESIS TESTING")
        print("=" * 80 + "\n")

        # Test 1: Do profit targets improve performance?
        print("Test 1: Do Profit Targets Improve Returns?")
        print("-" * 60)
        with_pt = self.df[self.df['has_profit_targets']]['total_return_pct'].dropna()
        without_pt = self.df[~self.df['has_profit_targets']]['total_return_pct'].dropna()

        t_stat, p_value = stats.ttest_ind(with_pt, without_pt)
        print(f"  With Profit Targets: mean = {with_pt.mean():.2f}%, n = {len(with_pt)}")
        print(f"  Without Profit Targets: mean = {without_pt.mean():.2f}%, n = {len(without_pt)}")
        print(f"  T-statistic: {t_stat:.3f}")
        print(f"  P-value: {p_value:.4f}")
        print(f"  Result: {'SIGNIFICANT' if p_value < 0.05 else 'NOT SIGNIFICANT'} (α=0.05)")
        print()

        # Test 2: Healthcare vs Utilities
        print("Test 2: Healthcare vs Utilities Performance")
        print("-" * 60)
        healthcare = self.df[self.df['sector'] == 'Healthcare']['total_return_pct'].dropna()
        utilities = self.df[self.df['sector'] == 'Utilities']['total_return_pct'].dropna()

        t_stat, p_value = stats.ttest_ind(healthcare, utilities)
        print(f"  Healthcare: mean = {healthcare.mean():.2f}%, n = {len(healthcare)}")
        print(f"  Utilities: mean = {utilities.mean():.2f}%, n = {len(utilities)}")
        print(f"  T-statistic: {t_stat:.3f}")
        print(f"  P-value: {p_value:.4f}")
        print(f"  Result: {'SIGNIFICANT' if p_value < 0.05 else 'NOT SIGNIFICANT'} (α=0.05)")
        print()

        # Test 3: Stocks vs ETFs
        print("Test 3: Individual Stocks vs ETFs")
        print("-" * 60)
        stocks = self.df[self.df['asset_type'] == 'Stock']['total_return_pct'].dropna()
        etfs = self.df[self.df['asset_type'] == 'ETF']['total_return_pct'].dropna()

        t_stat, p_value = stats.ttest_ind(stocks, etfs)
        print(f"  Stocks: mean = {stocks.mean():.2f}%, n = {len(stocks)}")
        print(f"  ETFs: mean = {etfs.mean():.2f}%, n = {len(etfs)}")
        print(f"  T-statistic: {t_stat:.3f}")
        print(f"  P-value: {p_value:.4f}")
        print(f"  Result: {'SIGNIFICANT' if p_value < 0.05 else 'NOT SIGNIFICANT'} (α=0.05)")
        print()

    def generate_summary_report(self):
        """Create summary report file"""
        print("\n" + "=" * 80)
        print("GENERATING SUMMARY REPORT")
        print("=" * 80 + "\n")

        report_path = self.output_dir / 'ANALYSIS_REPORT.txt'

        with open(report_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("STATISTICAL ANALYSIS REPORT\n")
            f.write("Trend-Following Backtest Data (293 Results)\n")
            f.write("=" * 80 + "\n\n")

            # Dataset overview
            f.write("DATASET OVERVIEW\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total backtests: {len(self.df)}\n")
            f.write(f"Profitable: {self.df['is_profitable'].sum()} ({100*self.df['is_profitable'].mean():.1f}%)\n")
            f.write(f"Very profitable (>20%): {self.df['is_very_profitable'].sum()} ({100*self.df['is_very_profitable'].mean():.1f}%)\n")
            f.write(f"Low drawdown (<10%): {self.df['low_drawdown'].sum()} ({100*self.df['low_drawdown'].mean():.1f}%)\n\n")

            # Top sectors
            f.write("TOP SECTORS BY WIN RATE\n")
            f.write("-" * 40 + "\n")
            sector_wr = self.df.groupby('sector')['is_profitable'].agg(['sum', 'count', 'mean'])
            sector_wr = sector_wr.sort_values('mean', ascending=False)
            for sector, row in sector_wr.head(5).iterrows():
                f.write(f"{sector}: {row['mean']:.1%} ({int(row['sum'])}/{int(row['count'])})\n")
            f.write("\n")

            # Top strategies
            f.write("TOP STRATEGIES BY WIN RATE\n")
            f.write("-" * 40 + "\n")
            strat_wr = self.df.groupby('strategy')['is_profitable'].agg(['sum', 'count', 'mean'])
            strat_wr = strat_wr.sort_values('mean', ascending=False)
            for strategy, row in strat_wr.head(5).iterrows():
                f.write(f"{strategy}: {row['mean']:.1%} ({int(row['sum'])}/{int(row['count'])})\n")
            f.write("\n")

            # Key correlations
            f.write("KEY CORRELATIONS\n")
            f.write("-" * 40 + "\n")
            corr_data = self.df[['total_return_pct', 'profit_factor', 'win_rate_pct', 'max_drawdown_pct']].corr()
            f.write(f"Return vs Profit Factor: {corr_data.loc['total_return_pct', 'profit_factor']:.3f}\n")
            f.write(f"Return vs Win Rate: {corr_data.loc['total_return_pct', 'win_rate_pct']:.3f}\n")
            f.write(f"Return vs Max Drawdown: {corr_data.loc['total_return_pct', 'max_drawdown_pct']:.3f}\n\n")

            # Files generated
            f.write("OUTPUT FILES GENERATED\n")
            f.write("-" * 40 + "\n")
            for file in sorted(self.output_dir.glob('*')):
                if file.name != 'ANALYSIS_REPORT.txt':
                    f.write(f"  - {file.name}\n")

        print(f"  ✓ Saved: {report_path}\n")

    def run_all(self):
        """Run complete analysis pipeline"""
        self.descriptive_statistics()
        self.correlation_analysis()
        self.logistic_regression_profitability()
        self.linear_regression_profit_factor()
        self.feature_importance_analysis()
        self.hypothesis_tests()
        self.visualizations()
        self.generate_summary_report()

        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE!")
        print("=" * 80)
        print(f"\nAll outputs saved to: {self.output_dir.absolute()}")
        print("\nGenerated files:")
        for file in sorted(self.output_dir.glob('*')):
            print(f"  - {file.name}")
        print("\n" + "=" * 80 + "\n")


if __name__ == '__main__':
    # Run analysis
    analysis = TradingAnalysis(csv_path='../cleaned-data.csv')
    analysis.run_all()
