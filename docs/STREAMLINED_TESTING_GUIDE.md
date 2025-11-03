# Streamlined Testing Guide: 10 Strategies × 11 Sectors

## Overview

You have **10 carefully selected strategies** that test fundamentally different hypotheses about trend-following. Your goal is to discover **which strategies work WHERE** across 11 different sectors.

---

## The 10 Strategies (In Testing Order)

### Phase 1: Foundation (Test First - 3 strategies)
1. **Baseline** - Control group
2. **Alt 15** - Single position (no pyramiding)
3. **Alt 26** - Fractional pyramid (smart sizing)

*Why first?* These three test the core question: "Does position management matter for this sector?"

### Phase 2: Entry Filters (If Phase 1 shows promise - 3 strategies)
4. **Alt 2** - EMA crossover (smoother entries)
5. **Alt 28** - ADX filter (trend strength required)
6. **Alt 17** - Dual timeframe (higher TF confirmation)

*Why second?* If the sector is profitable, these test whether filtering improves results.

### Phase 3: Exit Optimizations (If profitable - 3 strategies)
7. **Alt 10** - Profit targets (take money off table)
8. **Alt 22** - Parabolic SAR (adaptive trailing)
9. **Alt 9** - Time exit (decay management)

*Why third?* Once entry works, optimize the exit strategy.

### Phase 4: Special Cases (Final test - 1 strategy)
10. **Alt 20** - Asymmetric (different longs/shorts)

*Why last?* Tests directional bias after understanding the sector.

---

## Quick Testing Protocol

### For Each Ticker:

**Step 1: Load Phase 1 (Foundation)**
- Test Baseline, Alt 15, Alt 26
- Takes ~5 minutes

**Decision Point:**
- **If ALL 3 fail (PF < 1.0):** Sector/ticker is not trend-friendly. Document and move to next ticker.
- **If ANY succeed (PF > 1.2):** Continue to Phase 2

**Step 2: Load Phase 2 (Entry Filters)**
- Test Alt 2, Alt 28, Alt 17
- Takes ~4 minutes

**Decision Point:**
- Do filters improve or hurt performance?
- Document which filter type works best

**Step 3: Load Phase 3 (Exit Optimizations)**
- Test Alt 10, Alt 22, Alt 9
- Takes ~4 minutes

**Decision Point:**
- Which exit strategy maximizes profit factor?
- Does this sector favor early exits or letting trends run?

**Step 4: Load Phase 4 (Special)**
- Test Alt 20
- Takes ~1 minute

**Decision Point:**
- Is this sector inherently bullish or bearish?
- Do longs/shorts need different parameters?

---

## Time Estimates

**Per Ticker:**
- Fast path (fails Phase 1): 5 minutes
- Medium path (passes Phase 1, fails Phase 2): 10 minutes
- Full path (all phases): 15 minutes

**Per Sector (3 tickers):**
- Minimum: 15 minutes (all fail Phase 1)
- Average: 30 minutes (mixed results)
- Maximum: 45 minutes (all pass all phases)

**Total Project:**
- 11 sectors × 30 min average = **5.5 hours**
- Spread over several days: very manageable

---

## Data Collection Template

### For Each Ticker:

```markdown
# [TICKER] - [Sector Name]

## Phase 1: Foundation
| Strategy | PF | Win Rate | Max DD | Trades | Pass? |
|----------|----|-----------

|--------|--------|-------|
| Baseline | | | | | |
| Alt 15 (Single) | | | | | |
| Alt 26 (Fractional) | | | | | |

**Decision:** □ Continue to Phase 2  □ Stop (not trend-friendly)

## Phase 2: Entry Filters (if applicable)
| Strategy | PF | Win Rate | Max DD | Trades | Better than Baseline? |
|----------|----|-----------||--------|--------|----------------------|
| Alt 2 (EMA) | | | | | |
| Alt 28 (ADX) | | | | | |
| Alt 17 (Dual TF) | | | | | |

**Best Entry:** ___________

## Phase 3: Exit Optimizations (if applicable)
| Strategy | PF | Win Rate | Max DD | Trades | Better than Baseline? |
|----------|----|-----------||--------|--------|----------------------|
| Alt 10 (Targets) | | | | | |
| Alt 22 (SAR) | | | | | |
| Alt 9 (Time) | | | | | |

**Best Exit:** ___________

## Phase 4: Special (if applicable)
| Strategy | PF | Win Rate | Max DD | Trades | Notes |
|----------|----|-----------||--------|--------|-------|
| Alt 20 (Asymmetric) | | | | | Long/short bias? |

## Summary
**Best Overall Strategy:** ___________
**Sector Characteristics:** ___________
**Key Learning:** ___________
```

---

## Pattern Recognition Checklist

After testing 3-4 sectors, start looking for patterns:

### Position Management Patterns
- [ ] Does pyramiding help high-volatility sectors? (Compare Baseline vs Alt 15 vs Alt 26)
- [ ] Does fractional sizing reduce drawdown in choppy sectors?
- [ ] Are there sectors where single position outperforms?

### Entry Mechanism Patterns
- [ ] Do defensive sectors prefer EMA entries? (Alt 2)
- [ ] Do trend-strong sectors NOT need ADX filter? (Alt 28)
- [ ] Do commodity sectors benefit from dual timeframe? (Alt 17)

### Exit Strategy Patterns
- [ ] Do mean-reverting sectors favor profit targets? (Alt 10)
- [ ] Do strong trending sectors favor Parabolic SAR? (Alt 22)
- [ ] Does time exit work for any sector? (Alt 9)

### Directional Patterns
- [ ] Are there inherently bullish sectors? (Alt 20 long bias)
- [ ] Are there sectors that short poorly? (Alt 20 analysis)

---

## Sector-by-Sector Hypotheses

### Before You Test Each Sector, Predict:

**Technology:**
- Prediction: Strong trends, pyramiding helps, no filter needed
- Expected winners: Baseline, Alt 26, Alt 22
- Expected losers: Alt 28 (over-filtering), Alt 10 (exits too early)

**Utilities:**
- Prediction: Choppy, mean-reverting, needs filtering
- Expected winners: Alt 10 (targets), Alt 28 (ADX), Alt 2 (EMA)
- Expected losers: Baseline (whipsaws), Alt 22 (too aggressive)

**Energy:**
- Prediction: Volatile trends, needs smart sizing
- Expected winners: Alt 26 (fractional), Alt 28 (ADX), Alt 17 (dual TF)
- Expected losers: Alt 15 (single position too risky), Alt 9 (time doesn't work)

**Financials:**
- Prediction: Economic cycle driven, dual TF helps
- Expected winners: Alt 17 (dual TF), Baseline, Alt 20 (asymmetric)
- Expected losers: Alt 9 (time-based fails)

**Healthcare:**
- Prediction: Steady growth trends
- Expected winners: Baseline, Alt 2, Alt 26
- Expected losers: Alt 28 (over-filtering)

**Consumer Defensive:**
- Prediction: Low volatility, take profits early
- Expected winners: Alt 10 (targets), Alt 15 (single), Alt 2 (EMA)
- Expected losers: Baseline (holds too long), Alt 26 (unnecessary)

**Consumer Cyclical:**
- Prediction: Economic sensitive, asymmetric behavior
- Expected winners: Alt 20 (asymmetric), Alt 17 (dual TF), Baseline
- Expected losers: Alt 9 (time)

**Communication Services:**
- Prediction: Mixed (some trending like META, some stable like T)
- Expected winners: TBD - test will reveal
- Expected losers: TBD

**Basic Materials:**
- Prediction: Commodity-like, dual TF helps
- Expected winners: Alt 17 (dual TF), Alt 26 (fractional), Baseline
- Expected losers: Alt 15 (too risky), Alt 9 (time)

**Industrials:**
- Prediction: Economic cycle driven
- Expected winners: Alt 17 (dual TF), Baseline, Alt 10 (targets)
- Expected losers: Alt 9 (time)

**Real Estate:**
- Prediction: Low volatility, interest rate sensitive
- Expected winners: Alt 10 (targets), Alt 2 (EMA), Alt 28 (ADX)
- Expected losers: Baseline (whipsaws)

---

## After Testing All Sectors

### Create Your "Strategy Selector" Matrix

| Sector | Best Strategy | Why? | Characteristics |
|--------|---------------|------|----------------|
| Technology | | | |
| Utilities | | | |
| Energy | | | |
| Financials | | | |
| Healthcare | | | |
| Consumer Def | | | |
| Consumer Cyc | | | |
| Comm Services | | | |
| Basic Materials | | | |
| Industrials | | | |
| Real Estate | | | |

### Answer These Questions:

1. **Which strategies are universal?** (Work across ≥7 sectors)
   - _____________________

2. **Which strategies are sector-specific?**
   - _____________________

3. **Which sectors are trend-friendly?** (≥5 strategies profitable)
   - _____________________

4. **Which sectors are difficult?** (≤2 strategies profitable)
   - _____________________

5. **Are there sector clusters?**
   - Defensive sectors prefer: _____________________
   - Cyclical sectors prefer: _____________________
   - Growth sectors prefer: _____________________

6. **Position management insights:**
   - Pyramiding helps: _____________________
   - Single position better for: _____________________
   - Fractional sizing best for: _____________________

7. **Entry mechanism insights:**
   - EMA entries better for: _____________________
   - ADX filtering needed for: _____________________
   - Dual TF helps: _____________________

8. **Exit mechanism insights:**
   - Profit targets best for: _____________________
   - Parabolic SAR best for: _____________________
   - Time exits work for: _____________________

---

## Final Deliverable

After completing all testing, you'll have:

1. **A strategy selector system** - "For sector X, use strategy Y"
2. **Understanding of sector characteristics** - What makes each sector unique
3. **Universal principles** - What works everywhere vs nowhere
4. **Edge identification** - Where your true edge exists

**This is far more valuable than just knowing alt31 works on SPY!**

You'll understand the **WHY** behind strategy performance, not just the **WHAT**.

---

## Pro Tips

1. **Test ETFs before individual stocks** - Sector ETFs (XLE, XLU, etc.) give you the "average" sector behavior

2. **Look for pattern breaks** - If your hypothesis fails, that's valuable information

3. **Document surprises** - "I expected X but got Y because Z" are the best learnings

4. **Don't cherry-pick** - Test all 10 even if Phase 1 looks bad. Sometimes filters save a sector.

5. **Compare to buy-and-hold** - Some tickers just go up. Is your strategy adding value?

6. **Watch correlation** - If all your strategies fail on a ticker, the ticker might not be liquid enough

7. **Batch your testing** - Do all Phase 1 tests for a sector, then all Phase 2, etc.

8. **Take breaks** - This is mentally demanding work. Better to do 1-2 sectors per session.

---

## Troubleshooting

**Problem:** All strategies fail Phase 1 on a ticker
- **Solution:** Ticker might not be trend-friendly. Try an alternative from [SECTOR_TICKERS.md](SECTOR_TICKERS.md)

**Problem:** Results don't match your hypothesis
- **Solution:** This is GOOD! Document why you were wrong. That's learning.

**Problem:** Too many strategies work (hard to pick)
- **Solution:** Sector is trend-friendly. Pick based on drawdown tolerance and complexity preference.

**Problem:** Testing feels overwhelming
- **Solution:** Just do Phase 1 for all sectors first. Get the big picture. Then optimize later.

---

**Remember:** The goal is NOT to find "the best strategy" - it's to build a mental model of how strategies and sectors interact. This knowledge is your true edge.

Good hunting!
