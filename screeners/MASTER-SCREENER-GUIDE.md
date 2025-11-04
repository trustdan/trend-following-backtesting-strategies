# MASTER FINVIZ SCREENER GUIDE
## The Complete System: Universe → Situational → Trade
**Synthesized from 293 backtests + 3 methodologies**

---

## 🧠 THE CORE CONCEPT (Why Your Old Screeners Failed)

### ❌ What You Were Doing (Doesn't Work)
```
FINVIZ with 13 filters → Looking for "the perfect stock RIGHT NOW"
↓
Result: 0-2 stocks (or zero) because perfection is rare
↓
Analysis paralysis, no trades
```

### ✅ What You Should Do (Works)
```
FINVIZ "Universe" (Weekly) → Build watch list of quality stocks
  ↓
FINVIZ "Situational" (Daily) → Find setups RIGHT NOW
  ↓
TradingView + Pine Scripts → Exact entry timing
  ↓
Trade execution
```

---

## 📐 THE THREE-TIER FRAMEWORK

### TIER 1: UNIVERSE SCREENERS (Weekly, 30-60 stocks)
**Purpose:** Find all quality stocks in your proven sectors that are in long-term uptrends  
**Frequency:** Run Monday morning, update TradingView watch lists  
**Result:** Your "fishing pond" for the week

### TIER 2: SITUATIONAL SCREENERS (Daily, 0-10 stocks)
**Purpose:** Find specific entry setups (pullbacks, breakouts) from your Universe  
**Frequency:** Run daily before market open  
**Result:** Today's high-probability candidates

### TIER 3: EXECUTION (Real-time, 1-3 trades)
**Purpose:** Apply Pine Scripts to Situational candidates for exact entries  
**Frequency:** When Situational screeners trigger  
**Result:** Actual trades

---

## 🏥 HEALTHCARE UNIVERSE SCREENER

### The Foundation (Returns 30-50 stocks)
Your backtests: **92.31% strategy success rate** in Healthcare

**Core Filters (Never Remove):**
```
Sector: Healthcare
Market Cap: +Mid (over $2B)
Average Volume: Over 500K
Price: Above SMA200 ← THE CRITICAL FILTER
```

**Quality Filters (Start With These):**
```
Price: Over $50
EPS growth this year: Positive
Sales growth past 5 years: Positive
Return on Equity: Positive
```

### FINVIZ URL (Base Configuration):
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,fa_epsyoy_pos,fa_sales5years_pos,fa_roe_pos,ta_sma200_pa&ft=4
```

### 🎚️ ADJUSTMENT DIALS

**If TOO MANY results (>80 stocks):**
- Add: `SMA50 > SMA200` (longer-term trend confirmation)
- Raise: Price to $75+
- Raise: Market Cap to Large+ (>$10B)
- Add: `Performance (Year): Up`

**If TOO FEW results (<20 stocks):**
- Drop: ROE requirement
- Drop: Sales growth requirement (keep EPS growth)
- Lower: Price to $30
- Lower: Volume to 300K

**If ZERO results (bear market):**
- Remove ALL quality filters except Sector + Price > SMA200
- This will show you which healthcare stocks are even trending

---

## 💻 TECH UNIVERSE SCREENER

### The Foundation (Returns 40-80 stocks)
Your backtests: **71.43% strategy success rate** in Tech

**Core Filters (Never Remove):**
```
Sector: Technology
Market Cap: +Large (over $10B)
Average Volume: Over 1M
Price: Above SMA200 ← THE CRITICAL FILTER
```

**Quality Filters (Start With These):**
```
Price: Over $100
EPS growth this year: Positive
EPS growth next year: Positive
Return on Equity: Over 15%
```

### FINVIZ URL (Base Configuration):
```
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,fa_epsyoy_pos,fa_epsyoy1_pos,fa_roe_o15,ta_sma200_pa&ft=4
```

### 🎚️ ADJUSTMENT DIALS

**If TOO MANY results (>120 stocks):**
- Add: `SMA50 > SMA200`
- Raise: Price to $150+
- Add: Industry filter (Software, Semiconductors only)
- Add: `SMA20 > SMA50` (short-term momentum)

**If TOO FEW results (<30 stocks):**
- Drop: EPS growth next year requirement (keep this year)
- Drop: ROE requirement
- Lower: Price to $50
- Lower: Market Cap to Mid+ (>$2B)

**If ZERO results:**
- Remove ALL quality filters except Sector + Price > SMA200
- Tech might be in correction

---

## 🎯 SITUATIONAL SCREENER #1: "PULLBACK HUNTER"

### The Concept
Stocks from your Universe that are **temporarily oversold** in a **confirmed uptrend**

**Use Case:**
- When you want to "buy the dip" on quality stocks
- Perfect for Alt43/Alt46 (volatility-adaptive entries)
- Best when market is choppy but not broken

### Base Setup
Start with Healthcare OR Tech Universe filters, then ADD:

**Timing Filters:**
```
Price: Above SMA200 (long-term trend intact)
Price: Below SMA50 (currently in pullback)
RSI (14): Below 40 (oversold, potential bounce)
```

### FINVIZ URL (Healthcare Pullback):
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4
```

### 🎚️ ADJUSTMENT DIALS

**If TOO MANY results (>20):**
- Tighten RSI: Below 35 (more oversold)
- Add: Volume > 1M (more liquid only)
- Add: SMA50 > SMA200 (stronger underlying trend)

**If TOO FEW results (0-2):**
- Loosen RSI: Below 45
- Change: Price below SMA50 → Price below SMA20 (milder pullback)
- Remove: Price below SMA requirement entirely (just use RSI)

### Expected Results:
- Bull market: 5-15 stocks
- Normal market: 3-8 stocks
- Bear market: 0-2 stocks (most broke SMA200)

**What This Tells You:**
- 0 results = No quality stocks are pulling back (chase or wait)
- 10+ results = Widespread selling (be selective, not all will bounce)

---

## 🚀 SITUATIONAL SCREENER #2: "BREAKOUT HUNTER"

### The Concept
Stocks from your Universe hitting **new 52-week highs TODAY**

**Use Case:**
- When you want to ride momentum that's proving itself NOW
- Perfect for Alt22 (Parabolic SAR, loves trending breakouts)
- Best in strong bull markets

### Base Setup
Start with Healthcare OR Tech Universe filters, then ADD:

**Timing Filters:**
```
Price: Above SMA200 (already confirmed)
Signal: New High (52-week high)
OR: 20-Day High (if 52w too restrictive)
```

### FINVIZ URL (Tech Breakout):
```
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_highlow52w_nh&ft=4
```

### 🎚️ ADJUSTMENT DIALS

**If TOO MANY results (>15):**
- Add: SMA20 > SMA50 (confirm short-term momentum)
- Add: Performance (Week): Up (filter out false breakouts)
- Raise: Market Cap to >$20B (mega-caps only)

**If TOO FEW results (0-2):**
- Change: 52-week high → 20-day high (recent strength)
- Remove: Universe quality filters (just Sector + SMA200 + New High)
- Change: New High → Near High (within 5% of highs)

### Expected Results:
- Bull market: 10-20 stocks
- Normal market: 5-10 stocks
- Bear market: 0-3 stocks

**What This Tells You:**
- 0 results = No new leadership (defensive mode)
- 15+ results = Strong breadth (time to deploy capital)

---

## 🔄 SITUATIONAL SCREENER #3: "GOLDEN CROSS"

### The Concept
Stocks where **SMA50 just crossed above SMA200** (classic trend-following signal)

**Use Case:**
- Catch the START of major uptrends (Turtle-style)
- Perfect for Alt10 (profit targets work best in developing trends)
- Patient capital, 3-12 month horizon

### Base Setup
```
Sector: Healthcare OR Technology
Market Cap: Mid+ (>$2B)
Average Volume: Over 500K
Price: Above SMA200
SMA50: Above SMA200 (golden cross confirmed)
Pattern: SMA50 crossed SMA200 (recent cross)
```

### FINVIZ URL:
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare_technology,cap_midover,sh_avgvol_o500,ta_sma200_pa,ta_sma50_pa200,ta_pattern_tlsupport&ft=4
```

### 🎚️ ADJUSTMENT DIALS

**If TOO MANY results:**
- Add: Volume > 1M
- Add: EPS growth positive
- Add: Performance (Month): Up

**If TOO FEW results:**
- Remove: Pattern requirement (just keep SMA50 > SMA200)
- Expand: Sector to "All" (then manually filter)

---

## ⚫ THE BLACKLIST SCREENER

### Always Run This (Returns 30-60 stocks to AVOID)
Your backtests: **0% success in Utilities, 21% in Energy**

**What NOT to Trade:**
```
Sector: Utilities OR Energy
```

### FINVIZ URL:
```
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

**Use Case:**
Cross-reference with ANY other screener. If a stock appears here, DELETE IT from your list.

**Your Proven Disasters:**
- DUK: 0/14 strategies profitable (worst: Alt15 -29.01%)
- XLU: 0/14 strategies profitable
- XOM: 2/14 profitable (barely)

---

## 📊 SECTOR ETF QUICK-CHECK

### Daily Market Temperature (Returns 0-7 ETFs)

**Core Filters:**
```
Ticker: XLV,XLY,XLK,XLI,XLF,QQQ,SPY
Price: Above SMA200
```

### FINVIZ URL:
```
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4
```

**What This Tells You:**
- 6-7 trending: Bull market → Trade individual stocks
- 3-5 trending: Normal → Mix of stocks + ETFs
- 0-2 trending: Bear market → Trade only trending ETFs (if any)

**Your Proven Winners:**
- ✅ XLV: 13/14 strategies profitable (Alt43 +34.79% RECORD)
- ✅ QQQ: 9/14 strategies profitable
- ⚠️ SPY: 7/14 strategies profitable (50%)

---

## 🗓️ THE COMPLETE WEEKLY + DAILY WORKFLOW

### 🏁 INITIAL SETUP (One-time, 30 minutes)

#### Week 1, Monday Morning

**Step 1: Build Healthcare Universe (10 min)**
1. Run Healthcare Universe screener → Get 30-50 stocks
2. Export results to CSV
3. Import into TradingView watch list: "Healthcare Universe"
4. Verify your proven winners appear: UNH, LLY, ABBV, JNJ

**Step 2: Build Tech Universe (10 min)**
1. Run Tech Universe screener → Get 40-80 stocks
2. Export results to CSV
3. Import into TradingView watch list: "Tech Universe"
4. Verify your proven winners appear: MSFT, GOOGL, NVDA

**Step 3: Build Blacklist (5 min)**
1. Run Blacklist screener → Get 30-60 stocks
2. Note in a file: "NEVER TRADE: DUK, XLU, XLE, XOM..."
3. Cross-reference: Remove any utilities/energy from Universe lists

**Step 4: Check Market Temperature (5 min)**
1. Run Sector ETF screener
2. Count: How many of 7 ETFs are trending?
   - 5-7 = Bull mode (trade stocks)
   - 2-4 = Cautious (trade ETFs + best stocks)
   - 0-1 = Bear mode (cash or XLV only if trending)

---

### 📅 WEEKLY MAINTENANCE (Monday, 15 minutes)

**Every Monday, 8:45 AM ET:**

**Step 1: Refresh Universe Lists (10 min)**
1. Re-run Healthcare Universe screener
2. Re-run Tech Universe screener
3. Update TradingView watch lists
   - Who fell below SMA200? → Remove
   - New names above SMA200? → Add

**Step 2: Check Market Temperature (2 min)**
1. Run Sector ETF screener
2. Is XLV still above SMA200? (Your #1 priority)
3. Is QQQ still above SMA200? (Your #2 priority)

**Step 3: Review Last Week's Trades (3 min)**
1. Which Situational setups worked?
2. Which Universe stocks became Situational setups?
3. Adjust strategy: More pullbacks or more breakouts?

---

### 🌅 DAILY WORKFLOW (Pre-market, 5-10 minutes)

**Every Trading Day, 9:00 AM ET:**

**Step 1: Run Pullback Hunter (3 min)**
1. Healthcare Pullback screener → 0-10 results
2. Tech Pullback screener → 0-10 results
3. Note any names from your Universe that appear

**Step 2: Run Breakout Hunter (3 min)**
1. Healthcare Breakout screener → 0-10 results
2. Tech Breakout screener → 0-10 results
3. Note any names from your Universe that appear

**Step 3: TradingView Validation (5 min)**
1. Open all Situational candidates (5-15 stocks total)
2. Load Alt43, Alt46, or Alt10 scripts
3. Which ones have actual entry signals TODAY?
4. Check options liquidity on finalists

**Step 4: Execute (1 min)**
1. Top 2-3 with cleanest setups → Place trades
2. Set alerts for the rest → Monitor

---

### 🔄 MONTHLY REVIEW (Last Friday, 30 minutes)

**End of Each Month:**

**Step 1: Backtest New Names (15 min)**
1. Which stocks appeared in Situational screeners 3+ times?
2. Run Alt43/Alt46 on them in TradingView (2010-2025)
3. Did they work? → Add to "Proven Winners" list

**Step 2: Update Sector Performance (10 min)**
1. Check: Is Healthcare still 90%+ win rate?
2. Check: Is Tech still 70%+ win rate?
3. Any new sectors emerging? (industrials, consumer disc?)

**Step 3: Adjust Universe Filters (5 min)**
1. If market changed (bull → bear), loosen filters
2. If overwhelmed (too many results), tighten filters
3. Document: "Nov 2025: Healthcare 92% wins, using base filters"

---

## 🎯 MAPPING SCREENERS → PINE SCRIPTS → OPTIONS

### Healthcare Universe → Which Strategies?

**Best Performers on Healthcare:**
- Alt43 (Volatility-Adaptive): XLV +34.79%, UNH +30.92%
- Alt46 (Sector-Adaptive): XLV +34.80%, UNH +32.16%
- Alt39 (Age-Based Targets): XLV +29.70%, UNH +27.07%
- Alt10 (Profit Targets): XLV +27.68%, UNH +33.13%

**Options Strategy:**
- 30-45 DTE covered calls (Alt43/Alt46 generate 20-60 exits/year)
- Cash-secured puts on pullbacks (Pullback Hunter setups)
- LEAPS diagonals on UNH (proven 92% win rate)

---

### Tech Universe → Which Strategies?

**Best Performers on Tech:**
- Alt15 (Multi-Timeframe): MSFT +52.65% (BEST EVER)
- Alt22 (Parabolic SAR): QQQ +32.44% (121 trades)
- Alt47 (Momentum-Scaled): MSFT +33.61%, GOOGL +25.09%
- Alt10 (Profit Targets): QQQ +22.75%, SPY +20.31%

**Options Strategy:**
- LEAPS diagonals on MSFT (Alt15: 15 trades, 189-day avg hold)
- Weekly covered calls on QQQ (Alt22: 121 trades, 9-day avg hold)
- 45-60 DTE spreads on GOOGL (Alt47: 85 trades)

---

### Pullback Hunter → Which Strategies?

**Best for Mean-Reversion Within Trend:**
- Alt10 (Profit Targets): Works on pullbacks, tight stops
- Alt39 (Age-Based): Gets more aggressive on older positions
- Alt45 (Dual-Momentum): Waits for momentum to return

**Options Strategy:**
- Buy calls 30-45 DTE when RSI < 40
- Sell cash-secured puts at SMA50 support
- Wait for bounce, close at +20-30% profit

---

### Breakout Hunter → Which Strategies?

**Best for Momentum Continuation:**
- Alt22 (Parabolic SAR): LOVES breakouts (121 trades on QQQ)
- Alt26 (Fractional Pyramid): Scales into breakouts
- Baseline (Turtle): Classic breakout system

**Options Strategy:**
- Buy calls ATM 30-45 DTE on confirmed breakout
- Trail stop using Parabolic SAR
- Close at Alt22 exit signals (averages 9-day hold)

---

### Golden Cross → Which Strategies?

**Best for Early-Stage Trends:**
- Alt10 (Profit Targets): Catches first leg up
- Baseline (Turtle): Designed for this setup
- Alt44 (ADX Pyramiding): Adds on trend strength

**Options Strategy:**
- LEAPS 6-12 months out (trend just starting)
- Sell covered calls 30-45 DTE against LEAPS
- Hold through multiple profit target exits

---

## 🏆 THE PROVEN WINNERS SHORTCUT

### When You Don't Have Time for Full Workflow

**Your 13 Proven Winners (From 293 Backtests):**

**Tier 1: Elite (>75% strategy success)**
- UNH: 92.86% (13/14 strategies profitable)
- MSFT: 85.71% (12/14 strategies profitable)
- AMZN: 78.57% (11/14 strategies profitable)
- WMT: 78.57% (11/14 strategies profitable)
- CAT: 78.57% (11/14 strategies profitable)

**Tier 2: Strong (70-75% success)**
- GOOGL: 71.43% (10/14 strategies profitable)

**Tier 3: Selective (50-70% success)**
- JPM: 50.00% (7/14 strategies profitable)
- PLD: 57.14% (8/14 strategies profitable)

**Proven ETFs:**
- XLV: 92.86% (13/14 strategies profitable) - BEST
- QQQ: 64.29% (9/14 strategies profitable)
- XLY: 64.29% (9/14 strategies profitable)

### Quick-Check URL (Are They Trending?)
```
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_tmo_abt_bmy_mrk_msft_googl_aapl_nvda_meta_amzn_wmt_cat_jpm&ft=4
```

**Action:**
- Run this daily at 9 AM
- Trade whichever of your proven winners are above SMA200
- Skip the Universe/Situational process when you're busy
- Deploy Alt10, Alt43, or Alt46 (your most reliable)

---

## 🚨 CRITICAL DECISION RULES

### When to Use Universe Screeners
- ✅ You want to discover NEW stocks similar to your winners
- ✅ You have time for research (weekly routine)
- ✅ Your proven winners list is getting stale

### When to Use Situational Screeners
- ✅ You want to find entries TODAY
- ✅ You've already built Universe watch lists
- ✅ You're ready to deploy capital now

### When to Skip All Screeners
- ✅ Your proven winners (UNH, MSFT, XLV) have entry signals
- ✅ Market is in correction (< 3 ETFs trending)
- ✅ You're in middle of existing positions

### When to Go 100% Cash
- ❌ Sector ETF screener returns 0 results (all broke SMA200)
- ❌ Your proven winners screener returns < 3 stocks
- ❌ Utilities are outperforming tech/healthcare (defensive rotation)

---

## 📈 PERFORMANCE EXPECTATIONS (Based on Your Data)

### If You Follow This System:

**Healthcare Focus:**
- Expected win rate: 70-90% (your backtests: 92.31%)
- Best strategies: Alt43, Alt46, Alt39, Alt10
- Best vehicle: Individual stocks (UNH, LLY) or XLV
- Timeframe: 3-12 week holds

**Tech Focus:**
- Expected win rate: 60-75% (your backtests: 71.43%)
- Best strategies: Alt15, Alt22, Alt47
- Best vehicle: Mega-caps (MSFT, GOOGL) or QQQ
- Timeframe: 1-20 week holds (strategy-dependent)

**Mixed Portfolio:**
- Expected win rate: 65-80%
- Allocation: 60% Healthcare, 30% Tech, 10% Other
- Strategies: Alt10 (universal), Alt43 (healthcare), Alt22 (tech)

---

## 🔧 TROUBLESHOOTING GUIDE

### Problem: All screeners return zero results

**Diagnosis:**
1. Check Sector ETF screener
   - If 0-1 ETFs above SMA200 → Bear market
   - If 5-7 ETFs above SMA200 → Screener broken

**Solutions:**
- Bear market → Remove ALL filters except Price > SMA200
- Screener broken → Re-copy URLs from this doc
- Extreme case → Just trade XLV if above SMA200

---

### Problem: Universe screeners return 150+ stocks

**Diagnosis:** Bull market, everything trending up

**Solutions:**
- Add SMA50 > SMA200 (longer-term confirmation)
- Add SMA20 > SMA50 (short-term momentum)
- Raise market cap requirement
- Or just sort by Market Cap, take top 50

---

### Problem: Situational screeners ALWAYS return zero

**Diagnosis:** Wrong filters or extreme market

**Solutions:**
- Pullback Hunter → Loosen RSI to < 45
- Breakout Hunter → Change 52w high to 20d high
- Check: Did you start with Universe filters first?

---

### Problem: Your proven winners don't appear in Universe

**Example:** UNH not in Healthcare Universe screener

**Diagnosis:**
1. Check TradingView: Is UNH above SMA200?
   - NO → UNH broke trend, correct to exclude
   - YES → Screener filter issue

**Solutions:**
- If UNH below SMA200 → Don't trade it (trend broken)
- If UNH above SMA200 → Check other filters (EPS, ROE, etc.)
- Remove quality filters one by one until UNH appears

---

### Problem: Too many signals, can't execute all

**Diagnosis:** Good problem to have (bull market)

**Solutions:**
- Priority 1: Healthcare Pullbacks (92% success)
- Priority 2: Tech Breakouts (71% success)
- Priority 3: Your proven winners only
- Deploy: Top 3-5 setups only (quality > quantity)

---

## 🎯 QUICK REFERENCE: COPY-PASTE URLS

### Universe Screeners (Run Weekly)
```
HEALTHCARE UNIVERSE:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,fa_epsyoy_pos,fa_sales5years_pos,fa_roe_pos,ta_sma200_pa&ft=4

TECH UNIVERSE:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,fa_epsyoy_pos,fa_epsyoy1_pos,fa_roe_o15,ta_sma200_pa&ft=4

PROVEN WINNERS CHECK:
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_tmo_abt_bmy_mrk_msft_googl_aapl_nvda_meta_amzn_wmt_cat_jpm&ft=4
```

### Situational Screeners (Run Daily)
```
HEALTHCARE PULLBACK:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4

TECH BREAKOUT:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_highlow52w_nh&ft=4

GOLDEN CROSS:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare_technology,cap_midover,sh_avgvol_o500,ta_sma200_pa,ta_sma50_pa200&ft=4
```

### Utility Screeners (Run As Needed)
```
SECTOR ETF TEMPERATURE:
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4

BLACKLIST (NEVER TRADE):
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

---

## 📋 ONE-PAGE CHEAT SHEET

**MONDAY (Weekly Setup - 15 min):**
1. Healthcare Universe → Update TradingView list
2. Tech Universe → Update TradingView list
3. Sector ETF check → Bull or bear mode?

**DAILY (Pre-Market - 5 min):**
1. Pullback Hunter → 0-10 stocks
2. Breakout Hunter → 0-10 stocks
3. Load Alt43/Alt46 on candidates → Trade top 2-3

**PRIORITIES:**
1. Your proven winners if trending: UNH, MSFT, XLV, QQQ
2. Healthcare > Tech (92% vs 71% win rates)
3. Avoid utilities/energy (0% and 21% win rates)

**STRATEGIES:**
- Alt43/Alt46 on healthcare (34%+ returns)
- Alt15 on MSFT (52% return)
- Alt22 on QQQ (32% return, 121 trades)
- Alt10 universal (76% success rate)

---

## 🏁 FINAL CHECKLIST: ARE YOU READY?

Before you start trading with this system, verify:

- [ ] I understand: Universe (weekly) ≠ Situational (daily)
- [ ] I've run all 6 screeners once to verify they work
- [ ] I've created TradingView watch lists for Healthcare + Tech
- [ ] I know my proven winners: UNH, MSFT, XLV, QQQ
- [ ] I have the Quick Reference URLs bookmarked
- [ ] I know which Pine Scripts to use (Alt43/46/10/15/22)
- [ ] I've verified options liquidity on my target stocks
- [ ] I know NEVER to trade utilities (DUK, XLU = 0% wins)
- [ ] I have a Monday routine (15 min) and daily routine (5 min)
- [ ] I'm starting with 3-5 positions max (quality > quantity)

**If you checked 9-10 boxes: You're ready to trade ✅**

---

## 💡 THE BOTTOM LINE

**Your edge comes from three things:**

1. **293 backtests** showing Healthcare (92%) and Tech (71%) dominate
2. **This screening system** to find those stocks when they're trending
3. **Your Pine Scripts** (Alt10/43/46) to time entries precisely

Finviz builds your watch list.  
TradingView finds your entries.  
Your data tells you where to fish.

**Don't overthink it. The system works if you work the system.**

---

**Last Updated:** November 2025  
**Based On:** 293 backtests, 21 securities, 14 strategies  
**Validation Rate:** 99.74% (387/388 healthy exits)  
**Recommended Start:** Healthcare Universe + Alt43 on XLV
