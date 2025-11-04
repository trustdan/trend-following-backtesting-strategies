# PRACTICAL FINVIZ SCREENERS
## Based on 293 Backtests - Designed to Actually Return Results

**Philosophy:** Start broad, narrow manually. FINVIZ with 10+ simultaneous filters = zero results.

---

## 🎯 THE PROBLEM WITH YOUR CURRENT SCREENERS

You're requiring **all of these simultaneously:**
- ✅ Price > SMA200 (uptrend)
- ✅ SMA20 > SMA50 (short-term momentum)
- ✅ SMA50 > SMA200 (golden cross)
- ✅ RSI 40-70 (not overbought)
- ✅ Beta 0.5-1.5 (moderate volatility)
- ✅ ATR > 2% (enough movement)
- ✅ Positive EPS growth
- ✅ Price > $50
- ✅ Volume > 500K

**Result:** Maybe 2-5 stocks total, often ZERO.

**Solution:** Use 3-4 "core" filters, then manually filter the 50-100 results.

---

## SCREENER #1: "HEALTHCARE CORE" (Returns ~40-60 stocks)

### Core Filters Only (4 filters)
Your data shows Healthcare = 92.31% success rate. Let's find those stocks.

**FINVIZ Setup:**
```
Sector: Healthcare
Market Cap: +Mid (over $2B)
Price: Above SMA200
Average Volume: Over 500K
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,sec_healthcare,sh_avgvol_o500,ta_sma200_pa&ft=4
```

**Expected Results:** 40-60 healthcare stocks in uptrends

**Now YOU Manually Filter For:**
1. **Chart check** - Does it look like XLV (clean uptrend since 2020)?
2. **Options check** - Does it have weekly options? (open interest > 100)
3. **Your winners** - Is it similar to UNH, JNJ, LLY, ABBV?

**Why This Works:**
- Only 4 filters = gets results
- Healthcare sector lock = 92% success rate baked in
- SMA200 = trend requirement (your most important factor)
- You manually verify the rest = quality control

---

## SCREENER #2: "TECH CORE" (Returns ~80-120 stocks)

### Core Filters Only (4 filters)
Your data shows Tech = 71.43% success rate. Cast a wider net, then narrow.

**FINVIZ Setup:**
```
Sector: Technology
Market Cap: +Large (over $10B)
Price: Above SMA200
Average Volume: Over 1M
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=cap_largeover,sec_technology,sh_avgvol_o1000,ta_sma200_pa&ft=4
```

**Expected Results:** 80-120 tech stocks in uptrends

**Now YOU Manually Filter For:**
1. **Mega-cap priority** - MSFT, GOOGL, NVDA, META first
2. **QQQ components** - Compare to QQQ top holdings
3. **Your winners** - MSFT (+52.65% Alt15), GOOGL, AMZN proven

**Why This Works:**
- Large-cap filter = liquid options automatically
- 1M+ volume = highly tradable
- You pick the best 10-15 manually = precision targeting

---

## SCREENER #3: "PROVEN WINNERS ONLY" (Returns ~15-25 stocks)

### Your Backtested Winners + Close Relatives

**FINVIZ Setup:**
```
Ticker: UNH,JNJ,LLY,ABBV,TMO,ABT,BMY,MRK,MSFT,GOOGL,AAPL,NVDA,META,AMZN,WMT,CAT,JPM
Average Volume: Over 500K
Price: Above SMA200
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_tmo_abt_bmy_mrk_msft_googl_aapl_nvda_meta_amzn_wmt_cat_jpm&ft=4
```

**Expected Results:** 10-15 stocks (whatever is currently above SMA200)

**Why This Works:**
- These ARE your 293 backtest winners
- No guessing - direct targeting
- Weekly maintenance - rerun to see who's still trending

---

## SCREENER #4: "SECTOR ETF ROTATION" (Returns ~3-8 ETFs)

### Trade the Sector ETFs Directly

**FINVIZ Setup:**
```
Ticker: XLV,XLY,XLK,XLI,XLF,QQQ,SPY
Price: Above SMA200
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4
```

**Expected Results:** 3-8 ETFs currently in uptrends

**Your Proven Winners:**
- ✅ XLV: 92.86% strategy success (13/14 profitable)
- ✅ QQQ: 64.29% strategy success
- ✅ XLY: 64.29% strategy success

**Why This Works:**
- Simpler than picking individual stocks
- Your Alt43 on XLV = +34.79% (RECORD)
- Lower stress, fewer decisions

---

## SCREENER #5: "QUICK MOMENTUM SCAN" (Returns ~100-200 stocks)

### When You Want More Ideas Fast

**FINVIZ Setup:**
```
Market Cap: +Mid (over $2B)
Price: Above SMA200
Performance (Year): Up
Average Volume: Over 500K
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,sh_avgvol_o500,ta_perf_52w_up,ta_sma200_pa&ft=4
```

**Expected Results:** 100-200 trending stocks across all sectors

**Now YOU Filter By:**
1. **Sector** - Prioritize Healthcare (92%) and Tech (71%)
2. **Avoid** - Exclude anything in Utilities, Energy
3. **Visual** - Click through charts, look for clean trends

---

## SCREENER #6: "AVOID THIS GARBAGE" (Returns ~30-60 stocks)

### What NOT to Trade

**FINVIZ Setup:**
```
Sector: Utilities OR Energy
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

**Your Data:**
- Utilities: 0% success rate (0/28 profitable)
- Energy: 21.43% success rate
- DUK: -19.93% baseline, lost money in ALL 14 strategies
- XOM: 2/14 strategies profitable

**Use This To:**
- Cross-reference with other screeners
- If something shows up here, SKIP IT
- Maintain your "never trade" blacklist

---

## THE TIERED FILTERING WORKFLOW

### Step 1: Run Broad Screener (50-100 results)
Pick one:
- Healthcare Core (#1) if bullish on health
- Tech Core (#2) if bullish on growth
- Proven Winners (#3) if conservative
- Momentum Scan (#5) if exploratory

### Step 2: Export to Spreadsheet
- Click "Export" in FINVIZ (top right)
- Open in Excel/Sheets

### Step 3: Manual Quality Filters
Add columns and score each stock:

| Ticker | Sector | Price | Your Backtest? | Options Liquid? | Keep? |
|--------|--------|-------|----------------|-----------------|-------|
| UNH | Healthcare | $525 | ✅ YES (92% win) | ✅ YES | ✅ TRADE |
| RANDOM | Healthcare | $85 | ❌ Unknown | ⚠️ Low OI | ⚠️ MAYBE |
| DUK | Utilities | $105 | ❌ 0% win rate | ✅ YES | ❌ NEVER |

### Step 4: Chart Verification (Top 20)
For each candidate:
1. Open TradingView
2. Load your Alt43 or Alt46 script
3. Does it look like XLV (steady up) or FCX (choppy mess)?

### Step 5: Options Validation (Top 10)
For final candidates:
1. Check options chain (your broker or OptionStrat)
2. Verify:
   - Weekly options available?
   - 30-45 DTE bid-ask spread < $0.50?
   - Open interest > 100 on ATM strikes?

### Step 6: Deploy Capital
Start with:
- **3-5 healthcare stocks** (UNH, LLY, ABBV if available)
- **2-3 tech stocks** (MSFT, GOOGL if available)
- **1-2 sector ETFs** (XLV, QQQ as baseline)

---

## SINGLE-CLICK "BEST SECTORS TRENDING" SCREENER

### The Simplest Possible Useful Screener

**FINVIZ Setup:**
```
Sector: Healthcare OR Technology
Market Cap: +Mid (over $2B)
Price: Above SMA200
Average Volume: Over 500K
```

**FINVIZ URL:**
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,sec_healthcare_technology,sh_avgvol_o500,ta_sma200_pa&ft=4
```

**Expected Results:** 50-80 stocks

**Sort By (in FINVIZ):**
- "Change" (today's % change) - see what's hot today
- "Volume" - see what's most liquid
- "Market Cap" - see the mega-caps first

**Then manually:**
1. Scan for names you recognize from your backtests
2. Prioritize Healthcare > Tech (92% vs 71% success)
3. Open top 10 in TradingView with your Alt43 script

---

## ADVANCED: MANUAL FILTERS TO APPLY

After you get 50-100 results from a broad screener, apply these **in order of importance**:

### Tier 1: Critical (Deal-Breakers)
1. **Sector**: Healthcare or Tech? ✅ Keep | Utilities or Energy? ❌ Delete
2. **Price > SMA200**: Still true? ✅ Keep | Crossed below? ❌ Delete
3. **Your backtest data**: Tested it before? ✅ Priority | Unknown? ⚠️ Research

### Tier 2: Quality (Nice-to-Have)
4. **Market cap**: >$10B? ✅ Safer options | <$2B? ⚠️ Risky
5. **Options liquidity**: Weekly options? ✅ Good | Monthly only? ⚠️ Limited
6. **ATR**: >2%? ✅ Good for exits | <1.5%? ⚠️ Choppy

### Tier 3: Refinement (Final Cut)
7. **Beta**: 0.5-1.5? ✅ Ideal | >2? ⚠️ Wild | <0.5? ⚠️ Boring
8. **RSI**: 40-70? ✅ Good entry | >80? ⚠️ Wait | <30? ⚠️ Falling knife
9. **Fundamentals**: Positive EPS growth? ✅ Bonus points

---

## WEEKLY MAINTENANCE ROUTINE

### Monday Morning (5 minutes):
1. Run Healthcare Core (#1)
2. Run Tech Core (#2)
3. Export both to Excel

### Monday Afternoon (15 minutes):
4. Filter down to top 20 (10 health + 10 tech)
5. Check if your current holdings still above SMA200
6. Add 1-2 new names if opportunities arise

### Month-End (30 minutes):
7. Run full backtest on any new candidates (TradingView)
8. Update your "proven winners" list
9. Remove any stocks that broke SMA200 last month

---

## FINVIZ PRO FEATURES (If You Upgrade)

### Worth Paying For:
- **Real-time data** (free version = 15min delay)
- **More filters** (can combine 10+ without breaking)
- **Advanced charts** (Ichimoku, volume profile)
- **Email alerts** (get notified when stocks break SMA200)

### Pro Screener Example:
If you have Pro, add these to Healthcare Core:
- Relative Volume > 1 (unusual activity today)
- Insider Trading: Buys (last 3 months)
- Institutional Ownership: 40-80%

---

## CRITICAL REMINDERS

✅ **DO THIS:**
1. Start with 4-5 filters max in FINVIZ
2. Get 50-100 results, THEN manually narrow
3. Prioritize Healthcare (92%) > Tech (71%)
4. Always verify SMA200 (most important)
5. Check options liquidity before deploying capital

❌ **DON'T DO THIS:**
1. Use 10+ filters simultaneously (zero results)
2. Trust FINVIZ sorting blindly (verify charts)
3. Skip manual verification (FINVIZ data lags)
4. Trade utilities/energy unless specific setup
5. Ignore your own backtest data (you have 293 tests!)

---

## EXAMPLE: YOUR WEEKLY WORKFLOW

**Monday 9:30 AM:**
```
1. Run "Healthcare Core" screener → Get 45 results
2. Export to Excel
3. Filter out: Market cap < $5B, Utilities sector
4. Remaining: 28 stocks
```

**Monday 10:00 AM:**
```
5. Sort by: Your backtest results (UNH, JNJ, LLY, etc.)
6. Top 10: UNH, LLY, ABBV, TMO, ABT, BMY, MRK, CVS, CI, HUM
7. Open each in TradingView
```

**Monday 10:30 AM:**
```
8. Load Alt43 script on each
9. Which 5 look best? UNH, LLY, ABBV, TMO, ABT
10. Check options: All have liquid weeklies ✅
```

**Monday 11:00 AM:**
```
11. Deploy: Sell 30-45 DTE covered calls on these 5
12. Set calendar reminder for Friday (roll/close)
```

**Total time:** 90 minutes
**Result:** 5 high-probability trades based on YOUR backtested data

---

## SUMMARY: SCREENER COMPARISON

| Screener | Filters | Results | Use Case | Time |
|----------|---------|---------|----------|------|
| Healthcare Core (#1) | 4 | 40-60 | Main hunting ground | Weekly |
| Tech Core (#2) | 4 | 80-120 | Secondary hunting | Weekly |
| Proven Winners (#3) | 3 | 10-15 | Conservative plays | Daily |
| Sector ETFs (#4) | 2 | 3-8 | Simplest execution | Daily |
| Momentum Scan (#5) | 4 | 100-200 | Exploration/research | Monthly |
| Avoid Garbage (#6) | 1 | 30-60 | Blacklist maintenance | Monthly |
| Best Sectors (#7) | 4 | 50-80 | Quick single-click | Weekly |

---

**Bottom Line:**
- Your old screeners: 10+ filters → 0-5 results → analysis paralysis
- These screeners: 3-5 filters → 50-100 results → YOU pick the best 10

**The magic is in YOUR manual filtering, not FINVIZ's automation.**

Your 293 backtests are worth more than any algorithmic screener.
