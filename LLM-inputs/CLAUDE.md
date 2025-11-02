# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains **Pine Script v6** trading strategies for TradingView, focused on **Ed Seykota-style trend following**. The strategies implement mechanical, rules-based systems using Donchian breakouts, ATR-based risk management, and pyramiding techniques inspired by the original Turtle Trading System and Ed Seykota's principles.

## Core Philosophy: Ed Seykota's Principles

All strategies in this repository adhere to these foundational principles:

1. **Simplicity:** Use only price and volatility (ATR). No complex indicators, no prediction, no discretion.
2. **Risk Management:** Position sizing based on N (ATR) to normalize volatility across instruments
3. **Cut Losses:** Protective stops always active (typically 2N from entry)
4. **Pyramid into Strength:** Add to winning positions at fixed N intervals (e.g., every 0.5N)
5. **Trend Following:** React to breakouts and trends; don't forecast direction
6. **Robustness:** Avoid over-optimization; prefer simple rules that work across markets and timeframes

**Never violate these principles** when modifying or creating strategies. Reject suggestions for:
- Martingale/averaging down on losers
- Prediction-based ML models
- Mean reversion without stops
- Complex indicator combinations (RSI+MACD+Stochastic, etc.)

## Key Files

### Main Strategy
- **[Ed-Seykota.pine](Ed-Seykota.pine):** The baseline "Turtle Core v2.1" strategy
  - 55-bar Donchian breakout entry (System 2)
  - Hybrid exit: max of 2N ATR stop OR 10-bar Donchian
  - Pyramiding: Up to 4 units, adding every 0.5N
  - Position sizing: 1% risk per unit based on N
  - Optional: SPY regime filter, time-based exits, volume filter

### Alternative Strategies (Claude directory)
- **[Claude/seykota_alt1_adaptive_volatility.pine](Claude/seykota_alt1_adaptive_volatility.pine):** Parameters adapt to volatility regimes
- **[Claude/seykota_alt3_anti_chop.pine](Claude/seykota_alt3_anti_chop.pine):** Uses ADX, Efficiency Ratio, and trend strength filters to avoid ranging markets
- Additional alternatives test different theoretical assumptions (see [plan.md](plan.md))

### Documentation
- **[plan.md](plan.md):** Master plan for 20 strategy alternatives to backtest, each with distinct theoretical assumptions
- **[ChatGPT.md](ChatGPT.md):** Suggestions from ChatGPT for improvements and alternative strategies
- **[Gemini.md](Gemini.md):** Suggestions from Gemini for alternative approaches

## Pine Script Development

### Testing Commands
Pine Script runs directly in TradingView's browser environment. There are no local build/test commands. To test:

1. Open TradingView and navigate to Pine Editor
2. Copy the `.pine` file contents
3. Click "Add to Chart" to run backtest
4. Use Strategy Tester panel to view performance metrics

### Key Pine Script Patterns Used

#### ATR-Based Position Sizing (N)
```pine
N = ta.atr(20)  // Calculate N (ATR)
sharesForUnit(_equity, _Nentry) =>
    riskDollars = _equity * (riskPct/100.0)
    perShareRisk = math.max(stopN * _Nentry, syminfo.mintick)
    math.max(1, math.floor(riskDollars / perShareRisk))
```

#### Donchian Breakout Logic
```pine
donHiPrev = ta.highest(high, 55)[1]  // [1] prevents lookahead
donLoPrev = ta.lowest(low, 55)[1]
longBreak = close > donHiPrev
shortBreak = close < donLoPrev
```

#### Pyramiding with State Variables
```pine
var float N_entry = na        // Freeze N at initial entry
var int units = 0             // Track pyramid position
var float lastAddLong = na    // Last add price

if inLong and close >= lastAddLong + 0.5 * N_entry
    strategy.entry("L", strategy.long, qty=shares)
    units += 1
    lastAddLong := close
```

#### Hybrid Exit Logic
```pine
initStopL = strategy.position_avg_price - 2 * N_entry
exitLoPrev = ta.lowest(low, 10)[1]
stopL := math.max(initStopL, exitLoPrev)  // Tighter of two
strategy.exit("L-EXIT", from_entry="L", stop=stopL)
```

### Date Range Filtering
All strategies use date range inputs to isolate backtest periods:
```pine
fromDate = input.time(timestamp("2022-01-01T00:00:00"))
toDate = input.time(timestamp("2099-12-31T23:59:59"))
inRange = (time >= fromDate) and (time <= toDate)

// Only trade inside range
if inRange and not inPos and longBreak
    // ... entry logic
```

### Avoiding Lookahead Bias
**Critical:** Always use `[1]` offset when comparing current bar to historical levels:
```pine
donHi = ta.highest(high, 55)
donHiPrev = donHi[1]           // Compare to PREVIOUS bar's level
longBreak = close > donHiPrev  // ✅ Correct

// ❌ WRONG (lookahead bias):
longBreak = close > ta.highest(high, 55)
```

## Architecture: Strategy Structure

All strategies follow this modular pattern:

1. **Inputs Section:** User-configurable parameters
   - Entry/exit lookbacks
   - ATR length (N)
   - Risk per unit (%)
   - Add step size (N)
   - Max pyramid units
   - Optional filters (regime, liquidity, time exits)

2. **Helpers Section:** Pure functions for calculations
   - `sharesForUnit()` for position sizing
   - Date range checks

3. **Core Calculations:** Derive signals from price/volatility
   - N (ATR)
   - Donchian levels
   - Market regime (optional external security)

4. **Signal Logic:** Entry/exit conditions
   - Combine breakout signals with filters
   - Check liquidity, regime, date range

5. **State Management:** Track position with `var` variables
   - N at entry (`N_entry`)
   - Last add prices (`lastAddLong`, `lastAddShort`)
   - Unit count (`units`)

6. **Trade Execution:**
   - Initial entries (`strategy.entry()`)
   - Add-ons (pyramiding)
   - Exits (`strategy.exit()` for stops, `strategy.close()` for time exits)

7. **Plotting:** Visual feedback
   - Donchian bands
   - Stop levels
   - Entry signals
   - Optional info tables

## Creating New Strategy Alternatives

When implementing alternatives from [plan.md](plan.md):

1. **Copy baseline:** Start with [Ed-Seykota.pine](Ed-Seykota.pine)
2. **Rename file:** `seykota_alt{N}_{short_name}.pine`
3. **Header comment:** State the theoretical assumption being tested
4. **Isolate changes:** Modify ONLY the component being tested (entry, exit, pyramid, or filter)
5. **Keep parameters consistent:** Use same risk%, N length, date range for comparison
6. **Document in plan.md:** Link the file and note expected trade-offs

### Example: Creating Alternative #6 (Pure ATR Trailing Stop)
```pine
// Change ONLY the exit logic:
if inRange and inLong
    // OLD: stopL := math.max(initStopL, exitLoPrev)
    stopL := initStopL  // PURE ATR STOP (no Donchian)
    strategy.exit("L-EXIT", from_entry="L", stop=stopL)
```

## Backtesting Standards

Use consistent parameters for fair comparison:
- **Capital:** $100,000
- **Commission:** 0.5% (0.005)
- **Slippage:** 2 ticks (add `slippage=2` to strategy())
- **Date Range:** 2015-01-01 to present (or 2022-01-01 for shorter tests)
- **Markets:** Test across ES, NQ, major stocks, crypto

Compare metrics:
- Total Return %
- Max Drawdown %
- Sharpe Ratio
- Win Rate %
- Profit Factor
- Trade count and duration

## Important Context

### Why 55-bar (System 2)?
The Turtle traders used two systems:
- **System 1 (S1):** 20-bar breakout (faster, more whipsaws)
- **System 2 (S2):** 55-bar breakout (slower, more robust)

The baseline uses S2 because it's historically more stable. Alternative #1 in [plan.md](plan.md) tests S1.

### Why "N" instead of "ATR"?
In Turtle/Seykota literature, **N = ATR(20)**. The term "N" emphasizes that volatility is THE fundamental unit of risk. All stops, adds, and position sizing are expressed as multiples of N (e.g., "2N stop", "0.5N add step").

### Hybrid Exit Logic
The baseline uses `math.max(2N stop, 10-bar Donchian low)` for longs. This means:
- **If trend is strong:** 10-bar low will be higher than the 2N stop → exit on 10-bar breakdown
- **If trend reverses sharply:** 2N stop will trigger first → protect capital

This hybrid approach balances "ride the trend" with "cut losses."

### Pyramiding Rationale
Adding to winners (not losers) is counterintuitive but critical:
- If price moves favorably by 0.5N, the trend is working → add more exposure
- Each add is still risking only 1% of CURRENT equity
- Maximum exposure grows WITH profits, not against them

### Why No Prediction?
Seykota's philosophy: Markets are unknowable. Prediction-based systems (ML, fundamentals) introduce discretion and overfitting risk. Pure mechanical rules based on observable price/volatility are:
- Testable
- Repeatable
- Emotionless
- Robust across markets

## Common Tasks

### Modifying Entry Logic
Change the breakout condition in the "Signals" section:
```pine
// Example: Add momentum filter
longBreak = allowLong and liqOK and longRegOK and (close > donHiPrev) and (close > close[10])
```

### Adjusting Risk Per Unit
Modify the `riskPct` input:
```pine
riskPct = input.float(1.5, "Risk % per unit", minval=0.1, maxval=5)
```

### Adding New Filters
Insert filter logic before entry execution:
```pine
// Example: ADX filter
adx = ta.dmi(14, 14)[2]
trendOK = adx > 25

if inRange and not inPos and longBreak and trendOK
    // ... entry logic
```

### Debugging Position Sizing
Add a label to visualize shares calculated:
```pine
if inRange and not inPos and longBreak
    sh = sharesForUnit(strategy.equity, N_entry)
    label.new(bar_index, low, "Shares: " + str.tostring(sh), style=label.style_label_up)
```

## Resources

- **Pine Script Reference:** https://www.tradingview.com/pine-script-reference/v6/
- **Turtle Trading Rules:** Original Turtle manuals document the S1/S2 breakout logic
- **Seykota's Principles:** "The Trading Tribe" book and interviews emphasize simplicity, risk management, and cutting losses
- **TradingView Strategy Tester:** https://www.tradingview.com/support/solutions/43000481223-strategy-tester/

## Workflow Recommendations

1. **Before coding:** Review [plan.md](plan.md) to ensure the idea is captured
2. **During development:** Test incrementally (add one filter at a time)
3. **After backtesting:** Document results and insights in comments or separate results file
4. **Compare alternatives:** Run multiple variants side-by-side on same chart/date range
5. **Forward test:** Paper trade promising strategies before going live

---

**Remember:** The goal is not to find "the perfect strategy," but to **understand which theoretical assumptions hold true** across markets and time. Robust trading comes from principles, not parameters.
