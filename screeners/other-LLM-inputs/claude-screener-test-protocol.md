# SCREENER TEST PROTOCOL
## Verify These Work Before You Commit

**Time Required:** 15 minutes  
**Goal:** Confirm these screeners return usable results and your winners appear

---

## TEST #1: Healthcare Core Screener (5 minutes)

### Step 1: Run the screener
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,sec_healthcare,sh_avgvol_o500,ta_sma200_pa&ft=4
```

### Step 2: Count results
- **Expected:** 40-60 stocks
- **If you get:** 0-10 stocks → Market is bearish, most healthcare broke SMA200
- **If you get:** 100+ stocks → Bullish market, adjust filters to narrow

### Step 3: Verify your winners appear
Look for these in the results:
- [ ] UNH (UnitedHealth Group)
- [ ] JNJ (Johnson & Johnson)
- [ ] LLY (Eli Lilly)
- [ ] ABBV (AbbVie)

**If 3+ of these appear:** ✅ Screener works  
**If 0-1 appear:** ⚠️ Check if they're below SMA200 (market timing issue, not screener issue)

### Step 4: Spot check quality
Click on 5 random stocks from results:
- Do they have charts that look like clean uptrends?
- Are they household-name healthcare companies?
- Do they have options? (check your broker)

**If yes to 4-5 stocks:** ✅ Screener works  
**If yes to 0-2 stocks:** ❌ Screener broken (contact me)

---

## TEST #2: Tech Core Screener (5 minutes)

### Step 1: Run the screener
```
https://finviz.com/screener.ashx?v=111&f=cap_largeover,sec_technology,sh_avgvol_o1000,ta_sma200_pa&ft=4
```

### Step 2: Count results
- **Expected:** 80-120 stocks
- **If you get:** 0-20 stocks → Tech crash, most broke SMA200
- **If you get:** 150+ stocks → Tech boom, all boats rising

### Step 3: Verify your winners appear
Look for these in the results:
- [ ] MSFT (Microsoft)
- [ ] GOOGL (Alphabet)
- [ ] AAPL (Apple)
- [ ] NVDA (NVIDIA)

**If 3+ of these appear:** ✅ Screener works  
**If 0-1 appear:** ⚠️ Major market correction happening

### Step 4: Spot check mega-caps
Click on MSFT, GOOGL, AAPL (if in results):
- Are they showing clean uptrends?
- Do they have weekly options?
- Do you recognize most other names in top 20?

**If yes to all:** ✅ Screener works  
**If no to any:** ⚠️ Market conditions poor, trade ETFs instead

---

## TEST #3: Proven Winners Screener (3 minutes)

### Step 1: Run the screener
```
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_tmo_abt_bmy_mrk_msft_googl_aapl_nvda_meta_amzn_wmt_cat_jpm&ft=4
```

### Step 2: Count results
- **Expected:** 10-15 stocks (out of your 17 proven winners)
- **If you get:** 5-9 stocks → Normal market, some winners pulled back
- **If you get:** 0-4 stocks → Major correction, most broke SMA200
- **If you get:** 15-17 stocks → Bull market, everything trending up

### Step 3: Identify the survivors
Which of your proven winners are still above SMA200?
- [ ] UNH
- [ ] JNJ
- [ ] LLY
- [ ] ABBV
- [ ] MSFT
- [ ] GOOGL
- [ ] AAPL
- [ ] NVDA
- [ ] META
- [ ] AMZN
- [ ] WMT
- [ ] CAT
- [ ] JPM

**Count:** _____ out of 13

**If 8-13 are above SMA200:** ✅ Bull market, trade stocks  
**If 4-7 are above SMA200:** ⚠️ Mixed market, trade ETFs  
**If 0-3 are above SMA200:** ❌ Bear market, sit in cash

---

## TEST #4: Sector ETF Rotation (2 minutes)

### Step 1: Run the screener
```
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4
```

### Step 2: Count results
- **Expected:** 3-8 ETFs
- **If you get:** 0-2 ETFs → Bear market, most sectors broken
- **If you get:** 6-7 ETFs → Bull market, most sectors trending

### Step 3: Check your best ETFs
Which of these are currently above SMA200?
- [ ] XLV (Healthcare) - Your 92% win rate ETF
- [ ] QQQ (Tech) - Your 64% win rate ETF
- [ ] SPY (Broad Market) - Your baseline

**If XLV is above SMA200:** ✅ Trade healthcare (your best sector)  
**If QQQ is above SMA200:** ✅ Trade tech (your second-best sector)  
**If neither above SMA200:** ⚠️ Defensive market, avoid or trade SPY only

---

## TEST #5: Avoid Garbage Screener (2 minutes)

### Step 1: Run the screener
```
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

### Step 2: Count results
- **Expected:** 30-60 stocks (utilities + energy)

### Step 3: Verify DUK appears
- [ ] DUK (Duke Energy) is in the list

**If DUK appears:** ✅ Screener correctly identifies garbage  
**If DUK doesn't appear:** ❌ Screener broken

### Step 4: Cross-reference with Test #1
- Did any utilities/energy appear in Healthcare Core?
- Did any utilities/energy appear in Tech Core?

**If none appeared:** ✅ Your Core screeners correctly exclude garbage  
**If some appeared:** ❌ Filters failed (shouldn't happen with sector filters)

---

## INTERPRETATION GUIDE

### All Tests Pass ✅
- Healthcare Core: 40-60 results, includes UNH/JNJ/LLY
- Tech Core: 80-120 results, includes MSFT/GOOGL
- Proven Winners: 10-15 results
- Sector ETFs: 4-7 results, includes XLV
- Avoid Garbage: 30-60 results, includes DUK

**Action:** Start using these screeners immediately ✅

---

### Some Tests Pass ⚠️
- Healthcare Core works, but Tech Core returns <40 stocks
- Or: Proven Winners shows only 6-8 stocks

**Interpretation:** Sector rotation happening (healthcare strong, tech weak)  
**Action:** Focus on sector that's working (trade healthcare only) ⚠️

---

### Most Tests Fail ❌
- Healthcare Core: <20 results
- Tech Core: <40 results
- Proven Winners: <5 results
- Sector ETFs: <3 results

**Interpretation:** Bear market, most stocks below SMA200  
**Action:** Wait for market to recover, or trade defensively (XLV only if above SMA200) ❌

---

## TROUBLESHOOTING

### Problem: "Screener returns zero results"
**Possible causes:**
1. FINVIZ URL got truncated (copy-paste error)
2. FINVIZ is down (check finviz.com home page)
3. Extreme market conditions (all stocks broke SMA200)

**Solutions:**
1. Re-copy URL from reference card
2. Wait 10 minutes and try again
3. Check if XLV is above SMA200 on TradingView

---

### Problem: "My proven winners don't appear"
**Example:** UNH not showing up in Healthcare Core

**Possible causes:**
1. UNH broke below SMA200 recently (bearish)
2. UNH is in a pullback (will return next week)
3. Screener filters are wrong

**Solutions:**
1. Check UNH on TradingView - is it above SMA200?
   - If NO: Don't trade it (trend broken)
   - If YES: Screener may be broken, check URL
2. Wait 1 week and rerun screener
3. Verify URL matches exactly

---

### Problem: "Too many results (200+)"
**Possible causes:**
1. Extreme bull market (everything trending up)
2. Filters too loose

**Solutions:**
1. Sort by "Market Cap" and take top 50
2. Add manual filter: Only trade mega-caps (>$50B)
3. Focus on Proven Winners screener instead

---

### Problem: "Unknown stocks in results"
**Example:** Healthcare Core returns 40 stocks, but you've never heard of 30 of them

**This is NORMAL:** Screener finds all qualifying stocks, not just famous ones

**Solutions:**
1. Sort by "Market Cap" (biggest = most famous)
2. Focus on top 20 by size
3. Or just use Proven Winners screener (only your backtested stocks)

---

## WEEKLY VALIDATION CHECKLIST

Run these tests every Monday:

**Week 1 (Today):**
- [ ] Test #1: Healthcare Core returns 40-60 results
- [ ] Test #3: Proven Winners returns 10-15 results
- [ ] Test #4: XLV is above SMA200

**Week 2 (Next Monday):**
- [ ] Test #2: Tech Core returns 80-120 results
- [ ] Test #4: QQQ is above SMA200

**Week 3 (Two weeks):**
- [ ] Test #1 again: Count changed?
- [ ] Test #3 again: Which stocks fell off?

**Week 4 (Three weeks):**
- [ ] All 5 tests: Benchmark performance
- [ ] Document: "On Nov 3, Healthcare returned 52 stocks, XLV above SMA200"

---

## SUCCESS METRICS

### After 1 Week:
- [ ] Ran all 5 tests successfully
- [ ] Identified 10-15 tradable candidates
- [ ] Deployed capital on 3-5 stocks/ETFs

### After 1 Month:
- [ ] Screeners consistently return 40-100 results (not zero)
- [ ] Your proven winners appear 80%+ of the time
- [ ] You have a weekly routine (Monday morning screening)

### After 3 Months:
- [ ] Trades made: 20-40 (based on screener candidates)
- [ ] Win rate: 60-75% (close to your backtest data)
- [ ] No more "analysis paralysis" from zero screener results

---

## RED FLAGS

**Stop and reassess if:**
1. Healthcare Core returns <10 stocks for 3 consecutive weeks
   - **Meaning:** Bear market, most healthcare broke SMA200
   - **Action:** Stop trading stocks, consider sector rotation

2. Your proven winners never appear (0-3 out of 13 for 4 weeks)
   - **Meaning:** Extreme bear market
   - **Action:** Move to cash, wait for recovery

3. Screeners return 200+ results every week
   - **Meaning:** Filters too loose OR extreme bubble
   - **Action:** Add 5th filter (Market Cap > $10B) or manually narrow

4. You get different results every time you run same screener
   - **Meaning:** FINVIZ free version delay (15 minutes)
   - **Action:** Upgrade to FINVIZ Pro OR run screeners at same time each day

---

## FINAL VALIDATION

### Question 1: Do these screeners return results?
- ✅ YES → Proceed to use them
- ❌ NO → Contact me with specific test results

### Question 2: Do your proven winners appear?
- ✅ YES (8+ out of 13) → Screeners validated
- ⚠️ MAYBE (4-7 out of 13) → Market in correction, use cautiously
- ❌ NO (0-3 out of 13) → Bear market, don't trade

### Question 3: Can you complete the workflow in 15 minutes?
- ✅ YES → You're ready to trade
- ❌ NO → Practice 2-3 more times this week

---

**If you answered YES to Questions 1 and 3, and at least MAYBE to Question 2:**

🎉 **You're ready to start using these screeners!** 🎉

Proceed to the Quick Reference Card and start your Monday morning routine.
