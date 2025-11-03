# Next 5 Strategies to Test (Alt43-47)

**Created:** November 2025
**Based on:** Analysis of 231 backtests across Alt2-Alt42
**Purpose:** Test innovative theories derived from successful patterns

---

## Strategy Summary Table

| Strategy | Theory | Entry Logic | Exit Logic | Expected Improvement |
|----------|--------|-------------|------------|---------------------|
| **Alt43** | Volatility-Adaptive Targets | Donchian breakout | ATR-based targets (expanding/stable/contracting) | SPY, tech stocks (catch parabolic moves) |
| **Alt44** | ADX Pyramiding Hybrid | ADX > 25 filter | Fractional pyramid 100%→75%→50%→25% | Commodities, utilities (avoid chop) |
| **Alt45** | Dual-Momentum Confirmation | Donchian + RSI >50/<50 | Age-based targets (Alt39 style) | Commodities, energy (filter false breakouts) |
| **Alt46** | Sector-Adaptive Parameters | Donchian breakout | Asset-type specific targets (stocks/ETFs/commodities) | All assets (match targets to behavior) |
| **Alt47** | Momentum-Scaled Sizing | Start 0.5N, add 0.5N on RSI confirm | Fractional pyramid (Alt26 style) | All assets (reduce false breakout damage) |

---

## Alt43: Volatility-Adaptive Targets

### Theory
Profit targets should adapt to **ATR expansion/contraction** instead of position age (Alt39's time-based approach is arbitrary).

### Logic
- **ATR Expanding** (ratio > 1.15): Wide targets 4N-7N-10N - trend accelerating, catch parabolic moves
- **ATR Stable** (normal): Standard targets 3N-6N-9N - normal trending
- **ATR Contracting** (ratio < 0.85): Tight targets 2N-4N-6N - trend weakening, book profits fast

### Hypothesis
Volatility changes reflect **actual trend strength** better than time. This should:
- Catch parabolic moves that Alt39 might exit too early (tech stocks explosive runs)
- Exit weakening trends faster than waiting for aging threshold
- Adapt to market regime changes in real-time

### Expected Results
- **SPY**: Better than Alt39's +131.89% by catching slow acceleration phases
- **MSFT/AMZN**: Catch explosive moves with wide targets during high volatility
- **FCX**: Tighter targets during contraction reduce whipsaw damage

### File
`seykota_alt43_volatility_adaptive_targets.pine`

---

## Alt44: ADX Pyramiding Hybrid

### Theory
Combine **Alt28's quality filtering** (ADX >25) with **Alt26's low-DD fractional exits**.

### Logic
- **Entry Filter**: Only when ADX > 25 (strong trend confirmation) - avoid choppy markets
- **Exit**: Fractional pyramid 100%→75%→50%→25% at 3N, 6N, 9N, 12N targets

### Hypothesis
Alt28 had **legendary UNH 72% win rate** but low trade count. Alt26 had **lowest drawdowns**. Combining them gives:
- High-quality entries (avoid chop)
- Gradual profit-taking (capture full moves)
- Best of both worlds

### Expected Results
- **Commodities (FCX)**: ADX filter avoids chop, fractional exits reduce reversals
- **Utilities (DUK/XLU)**: Maybe make them tradeable by only entering strong trends?
- **ETFs**: Quality matters more than quantity - fewer better trades

### File
`seykota_alt44_adx_pyramiding_hybrid.pine`

---

## Alt45: Dual-Momentum Confirmation

### Theory
Require **BOTH** price momentum (Donchian) **AND** oscillator momentum (RSI) before entering.

### Logic
- **Entry**: Donchian breakout AND RSI confirms (>50 for longs, <50 for shorts)
- **Exit**: Alt39's proven age-based profit targets (young 4N-7N-10N, mature 3N-6N-9N, aging 2N-4N-6N)

### Hypothesis
Many Donchian breakouts fail when RSI is weak (price breaks but momentum isn't there). Waiting for **dual confirmation** should:
- Filter false breakouts on mean-reverting assets
- Reduce whipsaws on commodities (FCX's biggest problem)
- Keep proven exits from Alt39 (SPY +131.89%)

### Expected Results
- **FCX**: Fewer false breakouts = fewer losses
- **XOM/XLE**: Energy sector reduces chop entries
- **JPM/XLF**: Financials get better entry timing

### File
`seykota_alt45_dual_momentum_confirmation.pine`

---

## Alt46: Sector-Adaptive Parameters

### Theory
Different asset types need **different profit targets** based on their movement characteristics. One-size-fits-all fails.

### Logic
- **Individual Stocks**: 3N-6N-9N (standard Alt10 targets - proven 76% success)
- **ETFs**: 4N-7N-10N (wider for slow grinders - Alt39 SPY used wide targets for +131.89%)
- **Commodities/Energy**: 2N-4N-6N (tighter for mean-reverting assets)

### Hypothesis
Alt39's **legendary SPY result (+131.89%)** came from wide targets letting slow ETF trends develop. Alt10's **worst result (FCX -32.21%)** came from holding mean-reverting commodities too long. **Matching targets to asset behavior** should improve all categories.

### Expected Results
- **SPY/QQQ**: Wide targets capture full slow grind (replicate Alt39 success)
- **MSFT/AMZN**: Standard stock targets work as proven
- **FCX/XOM**: Tighter targets avoid reversals, book profits faster

### File
`seykota_alt46_sector_adaptive_parameters.pine`

---

## Alt47: Momentum-Scaled Position Sizing

### Theory
Start with **half position**, add other half only when **momentum confirms strength**.

### Logic
- **Initial Entry**: 0.5N risk on Donchian breakout (tentative position)
- **Confirmation Add**: +0.5N if RSI confirms >60 (longs) or <40 (shorts) within 5 bars
- **Exit**: Alt26's fractional pyramid (100%→75%→50%→25% at 3N-6N-9N-12N)

### Hypothesis
Many breakouts fail immediately. Starting with **half position limits damage** on false breakouts while **adding on confirmation** captures strong trends. This should:
- Reduce average loss size on failed breakouts
- Still capture strong moves with full position (if RSI confirms)
- Combine entry quality (like Alt28) with exit quality (like Alt26)

### Expected Results
- **All assets**: Better entry quality improves risk-adjusted returns
- **Commodities/Energy**: Fewer full-size losses on whipsaws
- **Trend followers**: Full position confirmed = full upside capture

### File
`seykota_alt47_momentum_scaled_sizing.pine`

---

## Testing Priority

Based on potential impact:

1. **Alt46 (Sector-Adaptive)** - Could replicate Alt39's SPY success across all ETFs
2. **Alt43 (Volatility-Adaptive)** - Most innovative, could beat Alt39's time-based approach
3. **Alt44 (ADX Pyramid)** - Combines two proven winners (Alt28 + Alt26)
4. **Alt45 (Dual-Momentum)** - Could solve commodity whipsaw problem
5. **Alt47 (Momentum-Scaled)** - Unique entry approach, highest risk/reward uncertainty

---

## Expected Outcomes Summary

### Best Case Scenarios:
- **Alt46** replicates Alt39's SPY +131% across all major ETFs (QQQ, XLV, XLY)
- **Alt43** catches parabolic moves better, beats Alt39 on tech stocks
- **Alt44** makes utilities/commodities tradeable by avoiding chop
- **Alt45** solves FCX problem (currently -4.47% with Alt39, could go positive)
- **Alt47** delivers higher win rates across the board by reducing false breakout damage

### Worst Case Scenarios:
- Over-filtering issues (like Alt20's 95% failure)
- Complex logic creates unexpected interactions
- Improvements marginal compared to Alt10/Alt26/Alt39

---

## Key Metrics to Watch

For each strategy, compare to current champions:

| Metric | Alt10 | Alt26 | Alt39 | Target for New Strategies |
|--------|-------|-------|-------|---------------------------|
| **Profitable Rate** | 76% | 76% | 67% | >70% |
| **SPY Return** | +20% | +33% | +132% | >30% |
| **FCX Result** | -32% | -20% | -4% | >0% (positive!) |
| **Healthcare (UNH/XLV)** | +33% / +28% | +19% / +23% | +27% / +30% | Maintain >20% |
| **Utilities (DUK/XLU)** | Fail | Fail | Fail | Still fail or scratch |
| **Max DD (Best)** | 5-7% | 5-6% | 5-8% | <6% |

---

## Notes for Testing

1. **Alt46 Asset Type Selection**: User must manually set "Stock", "ETF", or "Commodity" for each test. This could be automated in future versions with symbol detection.

2. **Parameter Sensitivity**: All strategies use similar base parameters (55-bar Donchian, 2N stops, etc.) for fair comparison.

3. **Combination Potential**: If Alt43, Alt44, or Alt45 show promise, consider creating "ultra" versions that combine multiple innovations.

4. **Documentation**: Record not just results but **why** each performs differently on different asset types.

---

## Files Created

- `pine-scripts/seykota_alt43_volatility_adaptive_targets.pine`
- `pine-scripts/seykota_alt44_adx_pyramiding_hybrid.pine`
- `pine-scripts/seykota_alt45_dual_momentum_confirmation.pine`
- `pine-scripts/seykota_alt46_sector_adaptive_parameters.pine`
- `pine-scripts/seykota_alt47_momentum_scaled_sizing.pine`

All files are ready for TradingView backtesting!
