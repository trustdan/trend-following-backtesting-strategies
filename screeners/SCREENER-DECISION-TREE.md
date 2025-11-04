# FINVIZ SCREENER DECISION TREE
## Which Screener Should I Use Right Now?

---

## 🎯 START HERE

**What are you trying to do?**

```
┌─────────────────────────────────────┐
│  What's your goal right now?        │
└─────────────────────────────────────┘
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
    [A]      [B]      [C]
   Build    Find     Quick
  Watchlist Trade    Check
  (Weekly)  (Daily)  (Anytime)
```

---

## PATH A: BUILD WATCHLIST (Weekly, Monday Morning)

### Decision: What do I want to discover?

```
┌────────────────────────────────────┐
│ What kind of stocks do I want?     │
└────────────────────────────────────┘
              │
     ┌────────┼────────┐
     ▼        ▼        ▼
  Healthcare Tech   Both
     │        │        │
     ▼        ▼        ▼
   [A1]     [A2]     [A3]
```

### [A1] Healthcare Universe
**Use when:**
- Starting fresh OR
- Healthcare is outperforming OR
- You want 92% win rate sector

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,fa_epsyoy_pos,fa_sales5years_pos,fa_roe_pos,ta_sma200_pa&ft=4
```

**Expected:** 30-50 stocks  
**Action:** Save to TradingView → "Healthcare Universe"  
**Next:** Run daily Pullback/Breakout screeners on this list

---

### [A2] Tech Universe
**Use when:**
- You want growth/momentum OR
- Tech is outperforming OR
- You want mega-cap liquidity

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,fa_epsyoy_pos,fa_epsyoy1_pos,fa_roe_o15,ta_sma200_pa&ft=4
```

**Expected:** 40-80 stocks  
**Action:** Save to TradingView → "Tech Universe"  
**Next:** Run daily Pullback/Breakout screeners on this list

---

### [A3] Combined Sectors
**Use when:**
- You want maximum diversification OR
- Both sectors are performing OR
- You want one master list

**Screener:** Run both A1 and A2, combine results  
**Expected:** 70-120 stocks  
**Action:** Save combined list to TradingView  
**Next:** Sort by Market Cap, prioritize Healthcare

---

## PATH B: FIND TRADES (Daily, Pre-Market)

### Decision: What setup am I looking for?

```
┌────────────────────────────────────┐
│ What's happening in the market?     │
└────────────────────────────────────┘
              │
     ┌────────┼────────┬────────┐
     ▼        ▼        ▼        ▼
  Stocks   Stocks   Market   Don't
  Pulling  Breaking Trending Know
   Back     Out      Up
     │        │        │        │
     ▼        ▼        ▼        ▼
   [B1]     [B2]     [B3]     [B4]
```

### [B1] Pullback Hunter
**Use when:**
- Market is choppy/consolidating OR
- You want to "buy the dip" OR
- RSI showing oversold conditions

**Screeners:**
```
HEALTHCARE PULLBACK:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4

TECH PULLBACK:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4
```

**Expected:** 0-10 stocks  
**Strategy:** Alt43, Alt46, Alt10  
**Options:** Buy calls 30-45 DTE, or CSP at support

**If 0 results:**
- Loosen RSI to < 45
- Change "below SMA50" to "below SMA20"
- Or skip this setup today

---

### [B2] Breakout Hunter
**Use when:**
- Market is trending strongly OR
- You see new 52-week highs OR
- Momentum is accelerating

**Screeners:**
```
HEALTHCARE BREAKOUT:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_highlow52w_nh&ft=4

TECH BREAKOUT:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_highlow52w_nh&ft=4
```

**Expected:** 0-15 stocks (bull market = more)  
**Strategy:** Alt22, Alt26, Baseline  
**Options:** Covered calls, weekly calls on QQQ

**If 0 results:**
- Change "52w high" to "20d high"
- Change "new high" to "near high" (within 5%)
- Or wait for breakouts to develop

---

### [B3] Golden Cross (Early Trends)
**Use when:**
- You want to catch trends EARLY OR
- Market just turned bullish OR
- You have patient capital (3-12 months)

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare_technology,cap_midover,sh_avgvol_o500,ta_sma200_pa,ta_sma50_pa200&ft=4
```

**Expected:** 10-30 stocks  
**Strategy:** Alt10, Baseline, Alt44  
**Options:** LEAPS 6-12 months out

**If too many results:**
- Add: Performance (Month) = Up
- Add: Volume > 1M
- Sort by Market Cap, take top 20

---

### [B4] Proven Winners Shortcut
**Use when:**
- You don't have time for full workflow OR
- Market is uncertain OR
- You want lowest-risk approach

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_msft_googl_nvda_xlv_qqq&ft=4
```

**Expected:** 3-9 stocks (out of your 9 best)  
**Strategy:** Whatever worked best in your backtests  
**Action:** Trade whichever are above SMA200 TODAY

**Guaranteed Winners:**
- UNH: 92.86% (Alt43 +30.92%, Alt46 +32.16%)
- MSFT: 85.71% (Alt15 +52.65%)
- XLV: 92.86% (Alt43 +34.79% RECORD)

---

## PATH C: QUICK CHECKS (Anytime)

### Decision: What do I need to know?

```
┌────────────────────────────────────┐
│ What question needs answering?     │
└────────────────────────────────────┘
              │
     ┌────────┼────────┬────────┐
     ▼        ▼        ▼        ▼
  Market    My      Should   What
  Bull or  Winners  I Trade   Not
  Bear?   Trending? Today?   Trade?
     │        │        │        │
     ▼        ▼        ▼        ▼
   [C1]     [C2]     [C3]     [C4]
```

### [C1] Market Temperature Check
**Use when:**
- Monday morning (weekly check) OR
- Market feels different OR
- Deciding risk level for the week

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4
```

**Interpretation:**
- **6-7 ETFs:** Bull market → Trade stocks aggressively
- **4-5 ETFs:** Normal → Mix of stocks + ETFs
- **2-3 ETFs:** Cautious → Best setups only
- **0-1 ETFs:** Bear market → Cash or XLV only

**Most Important:**
- XLV trending? → Focus on healthcare (92% wins)
- QQQ trending? → Add tech exposure (71% wins)
- Neither? → Sit in cash

---

### [C2] Proven Winners Check
**Use when:**
- Daily quick check OR
- Deciding if "your stocks" are tradable OR
- Confirming trend is intact

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_tmo_abt_bmy_mrk_msft_googl_aapl_nvda_meta_amzn_wmt_cat_jpm&ft=4
```

**Count Results:**
- **10-17:** Strong bull → Trade your proven winners
- **6-9:** Normal → Selective trades
- **3-5:** Choppy → Only UNH, MSFT, XLV
- **0-2:** Bear → Cash

**Priority Order:**
1. UNH (92% win rate)
2. MSFT (85% win rate)
3. XLV (92% win rate)
4. AMZN, WMT, CAT (78% win rate)
5. GOOGL (71% win rate)

---

### [C3] "Should I Trade Today?"
**Decision tree:**

```
START
  │
  ├─→ Sector ETF Check: How many trending?
  │    ├─→ 5-7 ETFs: YES, go aggressive
  │    ├─→ 3-4 ETFs: MAYBE, be selective
  │    └─→ 0-2 ETFs: NO, defensive mode
  │
  ├─→ Proven Winners Check: How many?
  │    ├─→ 8+ trending: YES, trade stocks
  │    ├─→ 4-7 trending: MAYBE, trade ETFs
  │    └─→ 0-3 trending: NO, sit in cash
  │
  └─→ Pullback/Breakout Screeners: Any signals?
       ├─→ 10+ signals: YES, lots of opportunity
       ├─→ 3-9 signals: MAYBE, pick best 2-3
       └─→ 0-2 signals: NO, wait for setups
```

**Final Decision Matrix:**

| ETFs Trending | Winners Trending | Situational Signals | TRADE? |
|---------------|------------------|---------------------|---------|
| 5-7 | 8+ | 10+ | ✅ YES - Full size |
| 5-7 | 8+ | 3-9 | ✅ YES - Normal size |
| 3-4 | 4-7 | 3-9 | ⚠️ MAYBE - Half size |
| 3-4 | 4-7 | 0-2 | ⚠️ MAYBE - Watch only |
| 0-2 | 0-3 | Any | ❌ NO - Cash |

---

### [C4] Blacklist Check
**Use when:**
- Reviewing Universe results OR
- Unfamiliar stock appears OR
- Confirming "never trade" list

**Screener:**
```
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

**Action:**
- If stock appears here → DELETE from all lists
- Utilities: 0% success rate (DUK, XLU)
- Energy: 21% success rate (XOM, XLE)

**Remember:**
- DUK: Lost money in ALL 14 strategies
- XLU: Lost money in ALL 14 strategies
- Never trade these, even if they "look good"

---

## 🎯 RECOMMENDED WORKFLOWS

### Workflow 1: "Full System" (For serious traders)

**Monday Morning (15 min):**
```
[A1] Healthcare Universe → Save to TradingView
[A2] Tech Universe → Save to TradingView
[C1] Market Temperature → Determine mode
```

**Daily Pre-Market (5 min):**
```
[B1] Pullback Hunter → 0-10 candidates
[B2] Breakout Hunter → 0-10 candidates
[C3] Should I Trade? → Decision
→ Load top 3-5 in TradingView
→ Apply Alt43/Alt46 scripts
→ Execute best 2-3 setups
```

**Expected:** 2-5 trades/week, 70-90% win rate

---

### Workflow 2: "Time-Efficient" (For busy traders)

**Monday Morning (5 min):**
```
[C1] Market Temperature → Bull/Bear?
[C2] Proven Winners Check → Who's trending?
```

**Daily Pre-Market (3 min):**
```
[B4] Proven Winners Shortcut
→ Trade UNH, MSFT, or XLV if trending
→ Use Alt43 or Alt46
```

**Expected:** 1-3 trades/week, 75-85% win rate

---

### Workflow 3: "Conservative" (For risk-averse)

**Weekly (10 min):**
```
[C1] Market Temperature → Only trade if bull
[C2] Proven Winners Check → Must have 8+ trending
[B4] Proven Winners Shortcut → Trade only UNH or XLV
```

**Expected:** 0-2 trades/week, 85-95% win rate

---

## 🚨 EMERGENCY DECISION RULES

### When Everything Returns Zero:

**Step 1:** Check Market Temperature (C1)
- If 0-1 ETFs trending → Bear market, correct response is ZERO trades

**Step 2:** Check Proven Winners (C2)
- If 0-3 trending → Broad correction, wait

**Step 3:** Only trade XLV if above SMA200
- Your 92% win rate sector
- Alt43 record: +34.79%
- Safest possible deployment

---

### When Too Many Signals (Overwhelmed):

**Priority Order:**
1. Healthcare Pullbacks (92% success)
2. Proven Winners (UNH, MSFT, XLV)
3. Tech Breakouts (71% success)
4. Everything else

**Rule:** Trade top 3 only, ignore the rest

---

### When Uncertain What to Do:

**Default Action:**
```
1. Run Proven Winners Check (C2)
2. Is UNH above SMA200? → Trade UNH with Alt43
3. Is MSFT above SMA200? → Trade MSFT with Alt15
4. Is XLV above SMA200? → Trade XLV with Alt43
5. None above? → Sit in cash
```

---

## 📊 RESULTS INTERPRETATION GUIDE

### Universe Screeners (A1, A2):

| Result Count | Interpretation | Action |
|--------------|----------------|--------|
| 0-10 | Bear market or bad filters | Remove quality filters |
| 10-30 | Normal/cautious | Use as-is |
| 30-60 | Good bull market | Use as-is (ideal) |
| 60-100 | Strong bull market | Tighten filters or sort by cap |
| 100+ | Too broad | Add SMA50>200, SMA20>50 |

---

### Situational Screeners (B1, B2, B3):

| Result Count | Interpretation | Action |
|--------------|----------------|--------|
| 0 | No setups today | Try alternate setup or wait |
| 1-3 | Limited opportunity | Trade all if quality |
| 4-10 | Good opportunity | Trade top 3-5 |
| 11-20 | Excellent opportunity | Trade top 5, save rest |
| 20+ | Too many (unusual) | Sort by cap, take top 10 |

---

### Market Temperature (C1):

| ETFs Trending | Market State | Strategy |
|---------------|--------------|----------|
| 6-7 | Strong bull | Aggressive stock trading |
| 4-5 | Normal bull | Balanced stock/ETF mix |
| 2-3 | Weak/choppy | Selective, best setups only |
| 0-1 | Bear | Defensive, cash or XLV only |

---

## 💡 QUICK TIPS

**Tip 1:** When starting out, use Workflow 2 (Time-Efficient)
- Less overwhelming
- Focuses on proven winners
- Still captures 75-85% win rate

**Tip 2:** Always start with Market Temperature (C1)
- Tells you if you should even be trading
- 1-minute check prevents costly mistakes

**Tip 3:** Bookmark these URLs in this order:
1. Market Temperature (C1) - Daily
2. Proven Winners (C2) - Daily
3. Healthcare Pullback (B1) - As needed
4. Tech Breakout (B2) - As needed

**Tip 4:** When in doubt, trade XLV with Alt43
- Your best combination: 92% sector + record strategy
- Simplest execution: One ETF, liquid options
- Proven results: +34.79% in backtests

---

## 🎯 FINAL FLOWCHART

```
START: What's your goal?
  │
  ├─→ Build Watchlist? → Monday → Use [A] paths
  │
  ├─→ Find Trade? → Daily → Use [B] paths
  │
  └─→ Quick Check? → Anytime → Use [C] paths

ALWAYS START WITH:
  1. Market Temperature (C1) → Bull or bear?
  2. Proven Winners (C2) → Who's trending?
  3. Then pick appropriate screener

DEFAULT WHEN UNCERTAIN:
  → Trade UNH/MSFT/XLV if above SMA200
  → Use Alt43 or Alt46
  → Or sit in cash if none trending

NEVER FORGET:
  ❌ Avoid utilities/energy (0% and 21% success)
  ✅ Prioritize healthcare (92% success)
  ✅ Quality > Quantity (3 good trades > 10 mediocre)
```

---

**REMEMBER: The best screener is the one you'll actually use consistently.**

Start with Workflow 2, master it, then expand to Workflow 1 if desired.
