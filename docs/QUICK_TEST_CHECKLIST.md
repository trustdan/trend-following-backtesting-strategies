# Quick Testing Checklist

Use this checklist for each ticker you test.

---

## Pre-Test Setup

- [ ] Identify ticker symbol
- [ ] Identify sector category
- [ ] Open TradingView chart
- [ ] Set timeframe (daily recommended)
- [ ] Set date range (sufficient history for backtesting)

---

## Testing Sequence

### Round 1: Top 5 SPY Winners
Test these first (they were most profitable on SPY):

- [ ] **alt31** - Fractional + BE Lock (SPY PF: 1.474)
  - Screenshot saved? _____
  - Profit Factor: _____
  - Result: ✓ Profitable / ✗ Unprofitable

- [ ] **alt38** - Triple Combo (SPY PF: 1.466)
  - Screenshot saved? _____
  - Profit Factor: _____
  - Result: ✓ Profitable / ✗ Unprofitable

- [ ] **alt34** - Fractional + Momentum (SPY PF: 1.396)
  - Screenshot saved? _____
  - Profit Factor: _____
  - Result: ✓ Profitable / ✗ Unprofitable

- [ ] **alt26** - Fractional Pyramid (SPY PF: 1.388)
  - Screenshot saved? _____
  - Profit Factor: _____
  - Result: ✓ Profitable / ✗ Unprofitable

- [ ] **alt40** - Ultimate (SPY PF: 1.348)
  - Screenshot saved? _____
  - Profit Factor: _____
  - Result: ✓ Profitable / ✗ Unprofitable

### Round 2: If Top 5 Fail, Try These
Only test if none of the above were profitable:

- [ ] **alt36** - BE + Momentum (SPY PF: 1.338)
- [ ] **alt21** - Breakeven Lock (SPY PF: 1.335)
- [ ] **alt35** - Fractional + Time (SPY PF: 1.306)
- [ ] **alt37** - BE + Time (SPY PF: 1.301)
- [ ] **alt30** - Momentum Pyramid (SPY PF: 1.277)

---

## Data Collection

**Ticker:** ___________
**Sector:** ___________
**Date Tested:** ___________

**Best Strategy:** ___________
**Best Profit Factor:** ___________
**Best Win Rate:** ___________%
**Max Drawdown:** ___________%

---

## Quick Observations

**Does the ticker trend well?**
- [ ] Strong trending behavior
- [ ] Choppy/sideways often
- [ ] Mixed

**Volatility compared to SPY:**
- [ ] Higher volatility
- [ ] Similar volatility
- [ ] Lower volatility

**Notes:**
_________________________________________________
_________________________________________________
_________________________________________________

---

## Post-Test Actions

- [ ] Screenshots saved to: `sectors/[sector]/screenshots/`
- [ ] Results documented in: `sectors/[sector]/[TICKER]_RESULTS.md`
- [ ] Updated DISCOVERIES.md with patterns observed
- [ ] If profitable strategy found: Note which strategy for future reference

---

## Quick Decision Tree

```
START: Load ticker in TradingView
  ↓
Test alt31 (your SPY champion)
  ↓
  ├─→ PF > 1.3? → WINNER! Document and move to next ticker
  ↓
  ├─→ PF 1.0-1.3? → Marginal. Test alt38 and alt34
  ↓
  └─→ PF < 1.0? → Test alt38, alt34, alt26, alt40
      ↓
      └─→ All fail? → This ticker might not be trend-following friendly
          - Document as "difficult ticker"
          - Try one or two from Round 2
          - If still failing, move to next ticker
```

---

## Time-Saving Tips

1. **If 3 strategies fail on a ticker, move on** - Don't test all 40
2. **Take screenshots only of profitable strategies** - Save disk space
3. **Use copy/paste for TradingView** - Load strategy once, change params
4. **Test sector ETFs before individual stocks** - XLE before XOM
5. **Pattern recognition** - If tech stocks keep failing, note the pattern early

---

## Red Flags (Skip Testing)

Stop testing a ticker if you observe:
- [ ] Extremely low liquidity (wide spreads)
- [ ] Recent IPO (insufficient history)
- [ ] Obvious data issues (gaps, splits not adjusted)
- [ ] Delisted or bankruptcy situation

---

## Success Criteria

What makes a strategy "good enough" to use?

| Metric | Minimum | Good | Excellent |
|--------|---------|------|-----------|
| Profit Factor | 1.0 | 1.3 | 1.5+ |
| Win Rate | 35% | 40% | 45%+ |
| Max Drawdown | <40% | <30% | <20% |
| # of Trades | 50+ | 100+ | 200+ |

---

## When You Find a Winner

When you find a profitable strategy (PF > 1.3):

1. ✓ Take screenshot of performance summary
2. ✓ Take screenshot of equity curve
3. ✓ Take screenshot of trade list
4. ✓ Note the parameters used
5. ✓ Save strategy file to sector folder
6. ✓ Document in results file
7. ✓ Add to DISCOVERIES.md
8. Consider: Is this better than buy-and-hold for this ticker?

---

## Progress Tracking

### ETFs Tested:
- [ ] SPY (✓ DONE - alt31 PF: 1.474)
- [ ] QQQ
- [ ] IWM
- [ ] XLE
- [ ] XLU
- [ ] XLF
- [ ] XLK
- [ ] XLV
- [ ] XLI
- [ ] DIA
- [ ] VTI

### Sectors Completed:
- [ ] Basic Materials (0/3 tickers)
- [ ] Communication Services (0/3 tickers)
- [ ] Consumer Cyclical (0/3 tickers)
- [ ] Consumer Defensive (0/3 tickers)
- [ ] Energy (0/3 tickers)
- [ ] Financial (0/3 tickers)
- [ ] Healthcare (0/3 tickers)
- [ ] Industrials (0/3 tickers)
- [ ] Real Estate (0/3 tickers)
- [ ] Technology (0/3 tickers)
- [ ] Utilities (0/3 tickers)

---

**Print this checklist and keep it next to your computer while testing!**
