# FINVIZ DAILY CHEAT SHEET
## One Page Reference - Print & Use

---

## 🗓️ MONDAY ROUTINE (15 minutes)

### 1. Healthcare Universe → Save to TradingView
```
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,fa_epsyoy_pos,fa_sales5years_pos,fa_roe_pos,ta_sma200_pa&ft=4
```
**Target:** 30-50 stocks | **Look for:** UNH, LLY, ABBV, JNJ

### 2. Tech Universe → Save to TradingView
```
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,fa_epsyoy_pos,fa_epsyoy1_pos,fa_roe_o15,ta_sma200_pa&ft=4
```
**Target:** 40-80 stocks | **Look for:** MSFT, GOOGL, NVDA

### 3. Market Temperature Check
```
https://finviz.com/screener.ashx?v=111&f=ta_sma200_pa,ticker_xlv_xly_xlk_xli_xlf_qqq_spy&ft=4
```
**Bull:** 5-7 ETFs | **Normal:** 3-4 ETFs | **Bear:** 0-2 ETFs

---

## 📅 DAILY ROUTINE (5 minutes before open)

### 1. Pullback Hunter (0-10 stocks)
```
HEALTHCARE:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4

TECH:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_sma50_pb,ta_rsi_os40&ft=4
```

### 2. Breakout Hunter (0-10 stocks)
```
HEALTHCARE:
https://finviz.com/screener.ashx?v=111&f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o50,ta_sma200_pa,ta_highlow52w_nh&ft=4

TECH:
https://finviz.com/screener.ashx?v=111&f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o100,ta_sma200_pa,ta_highlow52w_nh&ft=4
```

### 3. Open TradingView → Load Alt43/Alt46 → Trade Top 2-3

---

## 🎯 PRIORITY HIERARCHY

### Tier 1: Your Proven Winners (If Trending)
```
CHECK DAILY:
https://finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,ta_sma200_pa,ticker_unh_jnj_lly_abbv_msft_googl_nvda_xlv_qqq&ft=4
```
- UNH (92% win rate)
- MSFT (85% win rate)
- XLV (92% win rate)
- QQQ (64% win rate)

### Tier 2: Healthcare Universe Candidates
- Any stock from Healthcare Universe with Pullback/Breakout setup

### Tier 3: Tech Universe Candidates
- Any stock from Tech Universe with Pullback/Breakout setup

### ❌ Never Trade: Utilities, Energy
```
BLACKLIST CHECK:
https://finviz.com/screener.ashx?v=111&f=sec_energy_utilities&ft=4
```

---

## 🎚️ ADJUSTMENT DIALS

### If Zero Results:
- [ ] Lower RSI to < 45 (Pullback)
- [ ] Change 52w high → 20d high (Breakout)
- [ ] Remove quality filters (EPS, ROE, Sales)
- [ ] Check: Is market in correction? (ETF screener)

### If Too Many Results (>50):
- [ ] Add SMA50 > SMA200
- [ ] Add SMA20 > SMA50
- [ ] Raise Market Cap requirement
- [ ] Sort by Market Cap, take top 20

---

## 🔀 SCREENER → STRATEGY → OPTIONS

| Screener Result | Deploy Strategy | Options Setup |
|-----------------|-----------------|---------------|
| Healthcare Pullback | Alt43, Alt46, Alt39 | Buy calls 30-45 DTE or CSP |
| Healthcare Breakout | Alt10, Alt22 | Covered calls 30-45 DTE |
| Tech Pullback | Alt15, Alt47 | LEAPS diagonals |
| Tech Breakout | Alt22, Alt26 | Weekly calls (QQQ) |
| Golden Cross | Alt10, Baseline | LEAPS 6-12 months |

---

## 📊 EXPECTED RESULTS (Your Backtests)

### Healthcare Focus:
- Win Rate: 70-90%
- Best: Alt43 on XLV (+34.79%)
- Best: Alt46 on UNH (+32.16%)
- Hold: 3-12 weeks

### Tech Focus:
- Win Rate: 60-75%
- Best: Alt15 on MSFT (+52.65%)
- Best: Alt22 on QQQ (+32.44%, 121 trades)
- Hold: 1-20 weeks

---

## 🚨 DECISION RULES

### GO AGGRESSIVE (Bull Market):
- ✅ 5-7 ETFs above SMA200
- ✅ 10+ Breakout Hunter results
- ✅ XLV + QQQ both trending
→ **Trade stocks, use 60% capital**

### GO SELECTIVE (Normal Market):
- ⚠️ 3-4 ETFs above SMA200
- ⚠️ 5-8 Pullback Hunter results
- ⚠️ XLV or QQQ trending (not both)
→ **Trade best setups only, use 30% capital**

### GO DEFENSIVE (Bear Market):
- ❌ 0-2 ETFs above SMA200
- ❌ < 3 Proven Winners trending
- ❌ XLV + QQQ both broke SMA200
→ **Cash or XLV only, use 10% capital**

---

## 🎯 WEEKLY PERFORMANCE TRACKING

| Week | Healthcare Pullbacks | Tech Breakouts | Trades Executed | Win Rate |
|------|---------------------|----------------|-----------------|----------|
| 1    |                     |                |                 |          |
| 2    |                     |                |                 |          |
| 3    |                     |                |                 |          |
| 4    |                     |                |                 |          |

**Target:** 60-75% win rate, 2-5 trades per week

---

## 🔧 TROUBLESHOOTING

| Problem | Quick Fix |
|---------|-----------|
| All screeners return 0 | Check ETF screener - bear market? |
| Proven winners missing | Are they below SMA200? (correct to exclude) |
| Too many signals (20+) | Sort by Market Cap, take top 10 only |
| No time for full workflow | Just trade UNH/MSFT/XLV if trending |

---

## ✅ DAILY CHECKLIST

**Before Market Open:**
- [ ] Run Pullback Hunter (both sectors)
- [ ] Run Breakout Hunter (both sectors)
- [ ] Note: 0-15 candidates total
- [ ] Load top 5 in TradingView with Alt43
- [ ] Check options liquidity on finalists
- [ ] Execute: Top 2-3 trades only

**After Market Close:**
- [ ] Review: Did your setups work?
- [ ] Adjust: More pullbacks or breakouts tomorrow?
- [ ] Update: Your trade journal

---

## 💡 REMEMBER

**The System:**
1. Monday: Build Universe (30-50 stocks)
2. Daily: Find Situational (0-10 setups)
3. Execute: Trade top 2-3 with Pine Scripts

**The Edge:**
- Healthcare: 92% success rate
- Tech: 71% success rate
- Alt43/46/10: Your proven winners
- 293 backtests > Any screener algorithm

**The Rules:**
- Never trade utilities/energy
- Always check SMA200 first
- Quality > Quantity (3 good trades > 10 mediocre)
- When in doubt, trade XLV with Alt43

---

**PRINT THIS PAGE - KEEP IT VISIBLE**
