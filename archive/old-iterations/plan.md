# 20 Ed Seykota-Style Trend Following Alternatives: Backtest Plan

## Core Seykota Principles (Maintained Across All Variants)
- **Simplicity:** Price and volatility-based rules only
- **Risk Management:** ATR-based position sizing (N)
- **Volatility Normalization:** All stops and adds scaled by N
- **Pyramid into Strength:** Add to winning positions
- **Cut Losses Quickly:** Protective stops always active
- **No Prediction:** React to price, don't forecast

---

## Control Strategy
### **0. BASELINE: Original Turtle Core v2.1**
**Theoretical Assumption:** 55-bar Donchian breakout + hybrid exit (ATR stop OR 10-bar Donchian) is the robust standard.

**Key Parameters:**
- Entry: 55-bar Donchian (System 2)
- Exit: Max of (2N stop, 10-bar low)
- Add-ons: Every 0.5N, max 4 units
- Risk: 1% per unit

**File:** `Ed-Seykota.pine` (baseline)

---

## Entry Signal Alternatives (1-5)

### **1. FAST BREAKOUT (Turtle System 1)**
**Theoretical Assumption:** Shorter-term (20-bar) breakouts catch trends earlier despite more whipsaws.

**Changes from Baseline:**
- Entry: 20-bar Donchian instead of 55-bar
- Exit: 10-bar Donchian (unchanged)
- Optional: Skip signal if last S1 trade was a winner (original Turtle S1 rule)

**Expected Trade-off:** More trades, earlier entries, higher whipsaw rate

---

### **2. CLASSIC EMA CROSSOVER**
**Theoretical Assumption:** Weighted moving averages filter noise better than absolute high/low breakouts. (Seykota's original approach)

**Changes from Baseline:**
- Entry: 50 EMA crosses above/below 200 EMA
- Exit: Reverse crossover (and/or ATR trailing stop)
- Pyramiding: Typically disabled (single position) OR add on pullbacks to fast EMA

**Expected Trade-off:** Smoother signals, less noise, delayed entries

**Reference:** ChatGPT.md lines 237-319, Gemini.md lines 13-85

---

### **3. ATR CHANNEL BREAKOUT**
**Theoretical Assumption:** Volatility bands around a moving average define trends better than fixed lookback highs/lows.

**Changes from Baseline:**
- Entry: Close > SMA(100) + 2*ATR (long), Close < SMA(100) - 2*ATR (short)
- Exit: Close crosses back through SMA(100) ± 2*ATR OR ATR stop
- Adds: Every 0.5N as price extends beyond entry band

**Expected Trade-off:** More responsive to volatility expansion/contraction

**Reference:** ChatGPT.md lines 406-487

---

### **4. WEEKLY TIMEFRAME DONCHIAN**
**Theoretical Assumption:** Higher timeframe lookbacks capture major trends and avoid daily noise.

**Changes from Baseline:**
- Entry: Weekly 26-bar Donchian high/low (executed on daily chart)
- Exit: Weekly 13-bar Donchian OR 2N stop
- Adds: Daily chart execution, every 0.5N

**Expected Trade-off:** Fewer, higher-quality trades with less chop

**Reference:** ChatGPT.md lines 322-403

---

### **5. CLOSE-CONFIRMED BREAKOUT**
**Theoretical Assumption:** Requiring close above/below the breakout level filters false intrabar spikes.

**Changes from Baseline:**
- Entry: Close > Donchian high (not just intrabar touch)
- Exit: Same hybrid logic
- Optional: Add "tide" filter (only long above 200 SMA, short below)

**Expected Trade-off:** Fewer false signals, but may miss early momentum

**Reference:** ChatGPT.md lines 495-576

---

## Exit Strategy Alternatives (6-10)

### **6. PURE ATR TRAILING STOP**
**Theoretical Assumption:** Fixed ATR-based stops respect volatility character better than arbitrary N-bar lows.

**Changes from Baseline:**
- Entry: 55-bar Donchian (unchanged)
- Exit: ONLY 2N stop from avg entry (remove 10-bar Donchian exit)
- Optional: Trail stop from highest high since entry (Chandelier)

**Expected Trade-off:** Longer rides in trends, risk of giving back more in reversals

**Reference:** Gemini.md lines 173-214

---

### **7. CHANDELIER TRAILING STOP**
**Theoretical Assumption:** Trailing from highest high (for longs) captures more trend while protecting gains.

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Exit: Trail stop = Highest(high, 22) - 3N (for longs), Lowest(low, 22) + 3N (shorts)
- Initial stop: Still 2N from entry

**Expected Trade-off:** Better upside capture, reduced premature exits

**Reference:** ChatGPT.md lines 237-319 (trailN parameter)

---

### **8. ADAPTIVE EXIT LENGTH**
**Theoretical Assumption:** Exit lookback should vary with volatility (tight in low vol, wide in high vol).

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Exit: If ATR > SMA(ATR, 100), use 20-bar Donchian; else 10-bar
- Adds: Unchanged

**Expected Trade-off:** Dynamic protection matching market character

**Reference:** Claude alternative 1 (seykota_alt1_adaptive_volatility.pine)

---

### **9. TIME-BASED EXIT**
**Theoretical Assumption:** Trends have finite lifespans; exit stale positions after N bars.

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Exit: Max of (2N stop, 10-bar Donchian, OR 60 bars in position)
- Optional: "Roll" mode (re-enter if breakout still valid)

**Expected Trade-off:** Prevents holding dead positions, forces review

**Reference:** Ed-Seykota.pine lines 30-31, 156-188

---

### **10. PROFIT TARGET + TRAILING STOP**
**Theoretical Assumption:** Take partial profits at milestones, trail remainder.

**Changes from Baseline:**
- Entry: 55-bar Donchian, full 4 units
- Exit: Close 1 unit at +3N, 1 at +6N, trail remaining 2 units with Chandelier
- Risk: Still size each unit for 1% risk

**Expected Trade-off:** Lock gains earlier, reduce risk of full reversals

---

## Pyramiding / Scaling Alternatives (11-15)

### **11. TAPERED PYRAMID**
**Theoretical Assumption:** Risk per unit should DECREASE as trend extends to avoid late-trend concentration.

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Adds: Unit 1 = 1.0% risk, Unit 2 = 0.66% risk, Unit 3 = 0.5% risk, Unit 4 = 0.4% risk
- Calculation: `riskPct / (units + 1)` OR fixed taper array

**Expected Trade-off:** Reduced exposure to late-trend reversals, lower profit potential

**Reference:** Gemini.md lines 117-169

---

### **12. ACCELERATED PYRAMID**
**Theoretical Assumption:** Strong trends justify faster pyramiding (add every 0.25N instead of 0.5N).

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Adds: Every 0.25N (half the distance), up to 6 units (instead of 4)
- Risk: 0.75% per unit (to maintain similar total exposure)

**Expected Trade-off:** Capture more of explosive moves, higher exposure risk

**Reference:** Claude alternative 5 (seykota_alt5_accelerated_pyramid.pine)

---

### **13. VOLATILITY-GATED ADDS**
**Theoretical Assumption:** Avoid adding during volatility explosions (often late-trend "blow-offs").

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Adds: Block add-ons if ATR > SMA(ATR, 20) (volatility spike guard)
- Otherwise: Standard 0.5N adds

**Expected Trade-off:** Avoid pyramiding into exhaustion moves

**Reference:** ChatGPT.md lines 19-20, 79-81, 162

---

### **14. PULLBACK PYRAMID**
**Theoretical Assumption:** Add to positions on strength pullbacks, not melt-ups.

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Adds: Only add if price pulls back to 10 EMA after hitting add threshold
- Logic: `if (high >= lastAdd + 0.5N) AND (close <= ema(close, 10))`, add next bar

**Expected Trade-off:** Better add prices, miss runaway trends without pullbacks

---

### **15. SINGLE POSITION (No Pyramid)**
**Theoretical Assumption:** Pyramiding overconcentrates risk; single positions are simpler and more robust.

**Changes from Baseline:**
- Entry: 55-bar Donchian, full position size (4% risk in single entry)
- Adds: None (maxUnits = 1)
- Exit: Same hybrid logic

**Expected Trade-off:** Simpler, lower peak exposure, misses compounding of pyramids

---

## Filtering / Regime Alternatives (16-18)

### **16. ANTI-CHOP FILTERS**
**Theoretical Assumption:** Trend systems fail in ranging markets; use ADX, Efficiency Ratio, and directional filters.

**Changes from Baseline:**
- Entry: 55-bar Donchian AND ADX > 25 AND Efficiency Ratio > 0.3
- Adds: Also require trend quality filters
- Exit: Standard

**Expected Trade-off:** Far fewer trades, higher win rate, miss some early trends

**Reference:** Claude alternative 3 (seykota_alt3_anti_chop.pine)

---

### **17. DUAL TIMEFRAME CONFLUENCE**
**Theoretical Assumption:** Require trend alignment across timeframes (daily + weekly).

**Changes from Baseline:**
- Entry: Daily 55-bar breakout AND weekly close > weekly 26-bar high
- Exit: Standard
- Adds: Standard

**Expected Trade-off:** Higher-conviction trades, fewer entries

**Reference:** Claude alternative 2 (seykota_alt2_dual_timeframe.pine)

---

### **18. REGIME-DEPENDENT RISK**
**Theoretical Assumption:** Increase position size in favorable regimes (SPY > 200 SMA), decrease in unfavorable.

**Changes from Baseline:**
- Entry: 55-bar Donchian
- Risk: 1.5% per unit if SPY > 200D MA, 0.5% per unit if below
- Adds: Standard

**Expected Trade-off:** Bet bigger when macro tailwind exists

**Reference:** Ed-Seykota.pine lines 25-28, 73-77 (regime filter logic)

---

## Execution / Mechanics Alternatives (19-20)

### **19. INTRABAR EXECUTION**
**Theoretical Assumption:** True breakouts occur at high/low, not close; using close misses entries.

**Changes from Baseline:**
- Entry: High > 55-bar high (for long) OR Low < 55-bar low (short) — not close-based
- Adds: High >= lastAdd + 0.5N (use intrabar extremes)
- Exit: Standard

**Expected Trade-off:** Earlier fills, more responsive, potential for more noise

**Reference:** ChatGPT.md lines 15-16, 79-80, 159-161

---

### **20. ASYMMETRIC LONG/SHORT**
**Theoretical Assumption:** Long and short trends behave differently; optimize parameters separately.

**Changes from Baseline:**
- Long Entry: 55-bar Donchian, 2N stop, 0.5N adds
- Short Entry: 35-bar Donchian, 2.5N stop, 0.75N adds (tighter, wider stops)
- Rationale: Shorts are faster/choppier; longs are slower/smoother

**Expected Trade-off:** Better match directional asymmetry in markets

**Reference:** Claude alternative 4 (seykota_alt4_asymmetric.pine)

---

## Backtesting Protocol

### **Standardized Parameters (for comparison)**
1. **Capital:** $100,000
2. **Commission:** 0.5% (0.005)
3. **Slippage:** 2 ticks (add this input to all scripts)
4. **Date Range:** 2015-01-01 to present (or 2022-01-01 per current scripts)
5. **Market:** Test on multiple instruments (ES, NQ, stocks, crypto)
6. **Control Variables:** Keep risk %, maxUnits, ATR length consistent FIRST; vary only the theoretical component

### **Metrics to Compare**
- Total Return %
- Max Drawdown %
- Sharpe Ratio
- Win Rate %
- Profit Factor
- Average Trade Duration
- Number of Trades
- Recovery Time (from drawdowns)

### **Testing Sequence**
1. Run Baseline (Strategy 0) on all instruments
2. Run each alternative (1-20) with isolated changes
3. Document which theoretical assumptions outperform
4. Combine winning ideas into "hybrid" strategies (Phase 2)

---

## Implementation Notes

### **Code Organization**
- Each alternative = separate .pine file
- Naming: `seykota_alt{N}_{short_name}.pine`
- Header comment: State theoretical assumption clearly
- Keep baseline code structure for easy comparison

### **Seykota Purity Check**
Before implementing, verify each alternative maintains:
- ✅ Price and volatility only (no volume divergence, no oscillators)
- ✅ ATR-based risk normalization
- ✅ Mechanical rules (no discretion)
- ✅ Protective stops always active
- ✅ Simple, explainable logic

### **What NOT to Test (Violations of Seykota principles)**
- ❌ Martingale position sizing (doubling down on losers)
- ❌ Prediction-based signals (ML models, sentiment)
- ❌ Mean reversion without stop losses
- ❌ Over-optimization (curve-fitting to past data)
- ❌ Complex indicator combinations (RSI + MACD + Stochastic, etc.)

---

## Expected Insights

By comparing these 20 alternatives, you will learn:

1. **Entry Timing:** Are fast breakouts (S1) or slow (S2) better for your instruments?
2. **Exit Method:** Do ATR trails outperform Donchian exits?
3. **Pyramiding:** Is tapering risk superior to equal-sized adds?
4. **Filters:** Do anti-chop filters improve Sharpe, or do they cause missed trends?
5. **Timeframes:** Does weekly Donchian beat daily?
6. **Asymmetry:** Do longs and shorts need different rules?

The goal is NOT to find "the best" strategy, but to **understand which assumptions hold true across markets and time periods**. Robust strategies will perform consistently; fragile ones will excel in backtest but fail forward.

---

## References
- **ChatGPT.md:** Incremental improvements to v2.1, alternative strategies (MA crossover, weekly Donchian, ATR channels, 20/10 Donchian)
- **Gemini.md:** EMA systems, System 1 vs 2, tapered pyramid, pure volatility stops
- **Claude Alternatives:** Adaptive volatility, anti-chop filters, asymmetric, accelerated pyramid
- **Ed-Seykota.pine:** Baseline Turtle Core v2.1 with date range and regime filter

---

## Next Steps
1. ✅ Review this plan for completeness
2. ⬜ Prioritize 5-10 alternatives for initial testing (start with highest-conviction ideas)
3. ⬜ Implement selected alternatives in Pine Script
4. ⬜ Run backtests across multiple instruments
5. ⬜ Document findings in `backtest_results.md`
6. ⬜ Iterate: Combine best-performing assumptions into hybrid strategies

**Remember Seykota's wisdom:** *"Everybody gets what they want from the markets."* These alternatives aren't about finding a "holy grail"—they're about understanding what kind of trader YOU are and what assumptions YOU believe in.
