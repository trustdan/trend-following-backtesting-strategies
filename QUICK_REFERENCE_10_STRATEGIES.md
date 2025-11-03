# Quick Reference: 10 Strategy Testing Order

**Print this page and keep it next to your computer while testing!**

---

## File Locations

All strategies are in: `pine-scripts/`

| # | Strategy Name | File Name |
|---|---------------|-----------|
| 1 | **Baseline** | `Ed-Seykota.pine` |
| 2 | **Alt 2: EMA Crossover** | `19_PF-1.043_seykota_alt2_ema_crossover.pine` |
| 3 | **Alt 9: Time Exit** | `34_PF-0.700_seykota_alt9_time_exit.pine` |
| 4 | **Alt 10: Profit Targets** | `14_PF-1.232_seykota_alt10_profit_targets.pine` |
| 5 | **Alt 15: Single Position** | `37_PF-0.177_seykota_alt15_single_position.pine` |
| 6 | **Alt 17: Dual Timeframe** | `24_PF-0.878_seykota_alt17_dual_timeframe.pine` |
| 7 | **Alt 20: Asymmetric** | `31_PF-0.729_seykota_alt20_asymmetric_long_short.pine` |
| 8 | **Alt 22: Parabolic SAR** | `28_PF-0.805_seykota_alt22_parabolic_sar.pine` |
| 9 | **Alt 26: Fractional Pyramid** | `04_PF-1.388_seykota_alt26_fractional_pyramid.pine` |
| 10 | **Alt 28: ADX Filter** | `20_PF-0.962_seykota_alt28_adx_filter.pine` |

---

## Testing Order (Per Ticker)

### ✅ Phase 1: Foundation (TEST FIRST - ~5 min)
1. Baseline
2. Alt 15 (Single Position)
3. Alt 26 (Fractional Pyramid)

**Stop here if:** All 3 fail (PF < 1.0)

---

### ✅ Phase 2: Entry Filters (IF PHASE 1 PASSES - ~4 min)
4. Alt 2 (EMA Crossover)
5. Alt 28 (ADX Filter)
6. Alt 17 (Dual Timeframe)

**Look for:** Do filters improve Baseline?

---

### ✅ Phase 3: Exit Optimizations (IF PROFITABLE - ~4 min)
7. Alt 10 (Profit Targets)
8. Alt 22 (Parabolic SAR)
9. Alt 9 (Time Exit)

**Look for:** Best exit strategy for this sector

---

### ✅ Phase 4: Special Case (~1 min)
10. Alt 20 (Asymmetric)

**Look for:** Long/short directional bias

---

## One-Sentence Descriptions

| Strategy | What It Tests |
|----------|--------------|
| **Baseline** | Classic Turtle - does pure trend following work? |
| **Alt 2** | Do smooth MA entries beat breakouts? |
| **Alt 9** | Do trends decay with time? |
| **Alt 10** | Should we take profits early? |
| **Alt 15** | Is pyramiding risky? |
| **Alt 17** | Does higher timeframe help? |
| **Alt 20** | Do bulls/bears differ? |
| **Alt 22** | Do adaptive exits work better? |
| **Alt 26** | Does smart sizing reduce risk? |
| **Alt 28** | Do we need to filter chop? |

---

## Success Criteria

**Minimum standards to consider a strategy "working":**
- Profit Factor > **1.2**
- Win Rate > **38%**
- Max Drawdown < **35%**
- Number of Trades > **30**

---

## Data to Collect (Per Strategy)

For each test, record:
1. **Profit Factor**
2. **Win Rate %**
3. **Max Drawdown %**
4. **Number of Trades**
5. **Pass/Fail** (meets minimum standards?)

---

## Decision Tree

```
Test Phase 1 (Baseline, 15, 26)
    ↓
All fail? → STOP, sector not trend-friendly
    ↓
Any pass? → Continue to Phase 2 (2, 28, 17)
    ↓
Filters help? → Note which type
    ↓
Continue to Phase 3 (10, 22, 9)
    ↓
Best exit? → Note which type
    ↓
Continue to Phase 4 (20)
    ↓
Long/short bias? → Note direction
    ↓
DONE - Pick best strategy for this ticker
```

---

## Quick Hypotheses to Test

### Position Management:
- **High volatility sectors** → Fractional (26) should win
- **Stable sectors** → Single (15) might be enough
- **Trending sectors** → Baseline pyramid should win

### Entry Mechanisms:
- **Choppy sectors** → EMA (2) or ADX (28) should help
- **Clean trends** → Filters hurt performance
- **Commodity sectors** → Dual TF (17) should help

### Exit Strategies:
- **Mean-reverting sectors** → Targets (10) should win
- **Strong trends** → SAR (22) should win
- **Any sector** → Time (9) probably fails

### Directional:
- **Tech** → Long bias (20 shows it)
- **Energy** → Balanced (20 neutral)
- **Utilities** → Hard to trend (20 struggles both ways)

---

## Time Budget

**Per ticker:**
- Fast fail: 5 min (Phase 1 only)
- Average: 10-15 min (all phases)

**Per sector (3 tickers):**
- ~30 minutes average

**Total project (11 sectors):**
- ~5-6 hours total
- Split over multiple sessions

---

## Red Flags

**Stop testing a ticker if:**
- [ ] All Phase 1 strategies have PF < 0.8
- [ ] Volume is very low (gaps, illiquid)
- [ ] Data has obvious errors
- [ ] Ticker is recently IPO'd (not enough history)

---

## After Each Sector

**Ask yourself:**
1. Which strategy won overall?
2. Did filters help or hurt?
3. Does this match my hypothesis?
4. What surprised me?
5. What pattern am I seeing?

---

## Pattern Recognition

**After 3-4 sectors, look for:**

**Position Patterns:**
- □ Pyramiding helps: __________________
- □ Single position better for: __________________
- □ Fractional needed for: __________________

**Entry Patterns:**
- □ EMA entries better for: __________________
- □ ADX filtering needed for: __________________
- □ Dual TF helps: __________________

**Exit Patterns:**
- □ Profit targets best for: __________________
- □ SAR best for: __________________
- □ Time exits work for: __________________

**Sector Patterns:**
- □ Trend-friendly sectors: __________________
- □ Choppy sectors: __________________
- □ Best performing sector: __________________

---

## Your Goal

By the end, you should be able to say:

> "For **[SECTOR]** stocks, use **[STRATEGY]** because they tend to **[CHARACTERISTIC]**"

**Example:**
> "For **Technology** stocks, use **Alt 26 (Fractional Pyramid)** because they tend to **trend strongly but with high volatility**"

---

**Remember:** You're building a mental model, not finding "the one strategy." Different tools for different jobs!

Print this, check boxes as you go, and enjoy the systematic discovery process!
