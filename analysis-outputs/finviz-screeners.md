# FINVIZ SCREENER CONFIGURATIONS
## Optimized for Trend-Following + Options Trading

**Based on:** 293 validated backtests showing 92% success in Healthcare, 71% in Tech, 0% in Utilities

---

## SCREENER #1: "HEALTHCARE MOMENTUM BEAST"
### Target: XLV/UNH-like stocks for Alt43/Alt46 deployment

**Why This Works:**
- Healthcare sector: **92.31% strategy success rate** (12/13 profitable)
- Alt43 on XLV: **+34.79% return** (RECORD BREAKING)
- Alt46 on XLV: **+34.80% return** (beat by 0.01%)
- UNH across strategies: Consistently profitable (Alt10/15/28/39/43/44/45/46/47)

**Pine Script to Deploy:** Alt43, Alt46, Alt39, Alt45, Alt10

**Options Strategy:** 30-45 DTE covered calls, cash-secured puts, credit spreads

---

### **FINVIZ FILTER CONFIGURATION:**

#### **Descriptive Tab:**
- **Sector:** Healthcare
- **Market Cap:** +Mid (over $2B) *(ensures liquid options)*
- **Average Volume:** Over 500K *(tradable options volume)*
- **Price:** Over $50 *(avoid penny stocks, better premium)*

#### **Fundamental Tab:**
- **EPS growth this year:** Positive *(growth = momentum)*
- **Sales growth past 5 years:** Positive *(sustainable business)*
- **Return on Equity:** Positive *(quality filter)*

#### **Technical Tab:**
- **Price:** Above SMA200 *(confirmed uptrend - CRITICAL for trend-following)*
- **SMA20:** Above SMA50 *(short-term momentum)*
- **SMA50:** Above SMA200 *(golden cross territory)*
- **Performance (Year):** Up *(yearly trend confirmation)*
- **Average True Range:** Over 2% *(enough volatility for exits)*
- **Beta:** 0.5 to 1.5 *(moderate volatility, good for options premium)*
- **RSI (14):** 40 to 70 *(avoid overbought extremes)*

#### **Chart Pattern (Visual Confirmation):**
- Look for: **Steady uptrends** (avoid choppy/sideways)
- Avoid: Range-bound, mean-reverting patterns
- Ideal: Higher highs, higher lows (like XLV 2010-2025)

---

### **EXPECTED RESULTS:**
- **Candidates:** 15-30 healthcare stocks
- **Examples:** UNH, JNJ, LLY, ABBV, TMO, ABT, BMY, MRK (if they meet criteria)
- **Backtest Reference:** UNH Alt43 (+30.92%), UNH Alt46 (+32.16%), UNH Alt10 (+33.13%)

---

### **FINVIZ URL (Copy-Paste Ready):**
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_eps5years_pos,fa_epsyoy_pos,fa_salesqoq_pos,ind_stocksonly,sec_healthcare,sh_avgvol_o500,sh_price_o50,ta_beta_0.5to1.5,ta_perf_52w_up,ta_rsi_40to70,ta_sma200_pa,ta_sma20_pa50,ta_sma50_pa200&ft=4
```

---

### **POST-SCREEN VALIDATION (Manual Check):**
1. **TradingView Chart Review:** Confirm clean uptrend since 2020
2. **Options Chain Check:** Verify liquid options (open interest > 100)
3. **ATR Check:** Ideally 2-4% (enough movement without excessive risk)
4. **Avoid:** Stocks with recent -20%+ drawdowns (broken trends)

---

## SCREENER #2: "TECH PROFIT-TARGET CRUSHER"
### Target: MSFT/GOOGL/QQQ-like stocks for Alt15/Alt22/Alt47 deployment

**Why This Works:**
- Technology sector: **71.43% strategy success rate** (10/14 profitable)
- MSFT Alt15: **+52.65% return** (BEST INDIVIDUAL STOCK PERFORMER)
- QQQ Alt22: **+32.44% return** (Parabolic SAR specialist)
- MSFT Alt47: **+33.61% return** (multi-timeframe excellence)

**Pine Script to Deploy:** Alt15, Alt22, Alt47, Alt43, Alt46, Alt45

**Options Strategy:**
- Alt22 on QQQ: Monthly covered calls (121 trades)
- Alt15 on MSFT: LEAPS diagonals (15 trades, 189-day hold)
- Alt47 on MSFT: 30-45 DTE spreads (85 trades)

---

### **FINVIZ FILTER CONFIGURATION:**

#### **Descriptive Tab:**
- **Sector:** Technology
- **Industry:**
  - Software (Application, Infrastructure)
  - Semiconductors
  - Internet Content & Information
- **Market Cap:** +Large (over $10B) *(mega-cap tech stability)*
- **Average Volume:** Over 1M *(highly liquid options)*
- **Price:** Over $100 *(quality tech, better options spreads)*

#### **Fundamental Tab:**
- **EPS growth this year:** Positive
- **EPS growth next year:** Positive *(analyst optimism = momentum)*
- **Sales growth past 5 years:** Positive
- **Return on Equity:** Over 15% *(tech leaders)*

#### **Technical Tab:**
- **Price:** Above SMA200 *(uptrend confirmation)*
- **SMA20:** Above SMA50
- **SMA50:** Above SMA200
- **Performance (Year):** Up
- **Average True Range:** Over 2.5% *(tech volatility premium)*
- **Beta:** 0.8 to 1.5 *(not too wild, not too calm)*
- **RSI (14):** 35 to 75 *(slightly wider range for tech)*
- **Pattern:** Horizontal S/R *(avoid) → use chart to confirm trends*

#### **Chart Pattern (Visual Confirmation):**
- Look for: **Stair-step uptrends** (like MSFT 2010-2025)
- Ideal: Pauses/consolidations followed by breakouts (SAR excels here)
- Avoid: Parabolic runs (GOOGL's choppy periods)

---

### **EXPECTED RESULTS:**
- **Candidates:** 20-40 tech stocks
- **Examples:** MSFT, GOOGL, AAPL, NVDA, META, AVGO, ORCL, CRM, ADBE (if trending)
- **Backtest Reference:** MSFT Alt15 (+52.65%), GOOGL Alt47 (+25.09%), QQQ Alt22 (+32.44%)

---

### **FINVIZ URL (Copy-Paste Ready):**
```
https://finviz.com/screener.ashx?v=111&f=cap_largeover,fa_eps5years_pos,fa_epsyoy_pos,fa_epsyoy1_pos,fa_roe_o15,fa_sales5years_pos,sec_technology,sh_avgvol_o1000,sh_price_o100,ta_beta_0.8to1.5,ta_perf_52w_up,ta_rsi_35to75,ta_sma200_pa,ta_sma20_pa50,ta_sma50_pa200&ft=4
```

---

### **POST-SCREEN VALIDATION:**
1. **QQQ Correlation Check:** Tech stocks should loosely track QQQ (not inverse)
2. **Parabolic SAR Test:** Load Alt22 script on TradingView - does it generate 60+ trades?
3. **Options Volume:** Weekly options available? (for Alt22's frequent exits)
4. **Avoid:** Recently IPO'd stocks (< 2 years), low options liquidity

---

## SCREENER #3: "UTILITIES & ENERGY AVOIDANCE FILTER"
### Target: Find what NOT to trade (inverse screener)

**Why This Matters:**
- Utilities sector: **0.00% strategy success rate** (0/28 tests across DUK + XLU)
- Energy sector: **21.43% success rate** (barely profitable)
- Consumer Staples: **14.29% success rate** (avoid)

**Use Case:** Exclude these characteristics from ALL other screeners

---

### **FINVIZ FILTER CONFIGURATION (WHAT TO AVOID):**

#### **Descriptive Tab - RED FLAGS:**
- ❌ **Sector:** Utilities, Energy, Consumer Defensive (Staples)
- ❌ **Industry:**
  - Utilities (Regulated Electric, Gas, Water)
  - Oil & Gas E&P, Integrated, Refining
  - Packaged Foods, Beverages, Household Products

#### **Technical Tab - DEATH PATTERNS:**
- ❌ **Average True Range:** Under 1.5% *(too low for trend-following)*
- ❌ **Beta:** Under 0.4 *(defensive = mean-reverting)*
- ❌ **Performance (Year):** Down OR sideways *(no trend = failure)*
- ❌ **Pattern:** Horizontal S/R *(range-bound = trend-following killer)*
- ❌ **SMA20 vs SMA50:** Criss-crossing *(choppy, no clear trend)*

---

### **CHARACTERISTICS TO AVOID (Apply to ALL Screeners):**

1. **Sector Blacklist:**
   - ❌ Utilities (DUK: -19.93% baseline, -29.01% Alt15, -20.18% Alt9/Alt17)
   - ❌ XLU: ALL 14 strategies lost money (worst: -28.18% Alt15)
   - ❌ Energy (XLE: 11/14 strategies unprofitable)
   - ❌ Consumer Staples (XLP: 12/14 strategies unprofitable)

2. **Technical Blacklist:**
   - ❌ Low ATR (< 1.5%) = insufficient movement for exits
   - ❌ Sideways 200-day SMA (flat = no trend)
   - ❌ Price oscillating around SMA200 (mean-reverting)
   - ❌ RSI consistently 45-55 (no momentum)

3. **Fundamental Blacklist:**
   - ❌ Dividend yield > 5% (often defensive/declining stocks)
   - ❌ Beta < 0.5 (too stable for trend strategies)
   - ❌ Utility business model (regulated, stable = anti-trend)

---

### **FINVIZ URL (INVERSE - Stocks to NEVER Trade):**
```
https://finviz.com/screener.ashx?v=111&f=sec_consumerdefensive_energy_utilities,ta_beta_u0.5,ta_sma200_cross&ft=4
```
*(Use this to see what your other screeners should EXCLUDE)*

---

### **PRACTICAL APPLICATION:**
When running Screeners #1 and #2, **manually exclude** any results that:
- Have utility-like characteristics (low vol, high dividend, flat trend)
- Are in energy sector (even if they pass filters)
- Show mean-reversion patterns (price bouncing between support/resistance)

**Backtest Proof:**
- DUK: 0/14 strategies profitable (worst: Alt15 -29.01%)
- XLU: 0/14 strategies profitable (worst: Alt15 -28.18%)
- XOM: 2/14 strategies profitable (best was only +3.16% baseline)

---

## SCREENER USAGE WORKFLOW

### **Step 1: Run Healthcare Screener (#1)**
- Expected: 15-30 candidates
- Filter to top 10 by:
  - Highest ATR (most movement = more exits)
  - Cleanest uptrend (visual chart check)
  - Liquid options (open interest check)

### **Step 2: Run Tech Screener (#2)**
- Expected: 20-40 candidates
- Filter to top 10 by:
  - Mega-caps first (MSFT, GOOGL, NVDA priority)
  - QQQ sector components (verify with QQQ holdings)
  - Options liquidity (weekly options available?)

### **Step 3: Cross-Reference with Avoidance Filter (#3)**
- Run inverse screener
- Manually remove ANY overlap from Steps 1-2
- Document "never trade" list for future reference

### **Step 4: Deploy Pine Scripts**
- **Healthcare stocks:** Alt43, Alt46 first (record breakers)
- **Tech stocks:** Alt15 (LEAPS), Alt22 (if QQQ-like), Alt47 (multi-TF)
- **Both sectors:** Alt10, Alt39, Alt45 (universal winners)

### **Step 5: Options Strategy Assignment**
- **High exit frequency (60+ trades):** 30-45 DTE monthly options
- **Medium frequency (20-60 trades):** 45-60 DTE bi-monthly
- **Low frequency (< 20 trades):** LEAPS diagonals

---

## ADVANCED SCREENER: COMBO FILTER

### **"The Ultimate Trend-Following + Options Combo"**

Combines best of Healthcare + Tech, excludes all failures:

**FINVIZ FILTER:**
- **Sector:** Healthcare OR Technology (use "All" then manually filter)
- **Market Cap:** +Mid (over $2B)
- **Price:** Over $50
- **Average Volume:** Over 500K
- **EPS growth this year:** Positive
- **Price:** Above SMA200
- **SMA20:** Above SMA50
- **SMA50:** Above SMA200
- **ATR:** Over 2%
- **Beta:** 0.5 to 1.5
- **RSI:** 35 to 75
- **Performance (Year):** Up
- **Exclude Sectors:** Utilities, Energy, Consumer Defensive

---

### **FINVIZ URL (COMBO SCREENER):**
```
https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy_pos,sec_healthcare_technology,sh_avgvol_o500,sh_price_o50,ta_beta_0.5to1.5,ta_perf_52w_up,ta_rsi_35to75,ta_sma200_pa,ta_sma20_pa50,ta_sma50_pa200&ft=4
```

**Expected Results:** 30-50 stocks
**Action:** Prioritize by sector success rate (Healthcare first, then Tech)

---

## BACKTEST-VALIDATED STOCK UNIVERSE

Based on your 293 backtests, these stocks are **proven winners**:

### **TIER 1: TRADE THESE (70%+ strategy success rate)**
- ✅ **UNH (Healthcare):** 13/14 strategies profitable (92.86%)
- ✅ **MSFT (Tech):** 12/14 strategies profitable (85.71%)
- ✅ **AMZN (Consumer Disc):** 11/14 strategies profitable (78.57%)
- ✅ **WMT (Consumer Staples exception):** 11/14 strategies profitable (78.57%)
- ✅ **GOOGL (Tech):** 10/14 strategies profitable (71.43%)
- ✅ **CAT (Industrials):** 11/14 strategies profitable (78.57%)

### **TIER 2: SELECTIVE (50-70% success rate)**
- ⚠️ **JPM (Financials):** 7/14 strategies profitable (50.00%)
- ⚠️ **PLD (Real Estate):** 8/14 strategies profitable (57.14%)

### **TIER 3: AVOID (< 40% success rate)**
- ❌ **FCX (Mining):** 3/14 profitable, high volatility hurts
- ❌ **XOM (Energy):** 2/14 profitable, mean-reverting
- ❌ **DUK (Utilities):** 0/14 profitable - NEVER TRADE

### **ETF UNIVERSE:**
- ✅ **XLV (Healthcare ETF):** 13/14 profitable (92.86%) - BEST ETF
- ✅ **QQQ (Tech ETF):** 9/14 profitable (64.29%)
- ✅ **XLY (Consumer Disc):** 9/14 profitable (64.29%)
- ⚠️ **SPY (Broad Market):** 7/14 profitable (50.00%)
- ❌ **XLU (Utilities ETF):** 0/14 profitable - WORST ETF
- ❌ **XLE (Energy ETF):** 3/14 profitable - AVOID

---

## SCREENER MAINTENANCE SCHEDULE

### **Weekly:**
- Re-run screeners to catch new breakouts
- Verify top candidates still above SMA200
- Check if any holdings broke below SMA50 (potential exit)

### **Monthly:**
- Review sector rotation (is Healthcare still trending?)
- Update "avoid" list if sectors change character
- Backtest new candidates with Alt43/Alt46 on TradingView

### **Quarterly:**
- Re-validate sector success rates with new trades
- Adjust beta ranges if market volatility changes
- Review options liquidity on existing holdings

---

## FINVIZ PRO FEATURES (If Available)

### **Elite Screener Additions:**
- **Correlation Filter:** Exclude stocks with negative correlation to XLV/QQQ
- **Insider Trading:** Prefer insider buying (confirms trend)
- **Institutional Ownership:** 40-80% (liquid but not overcrowded)
- **Short Interest:** Under 5% (avoid squeeze candidates)

### **Advanced Charts:**
- Load Ichimoku Cloud (price above cloud = strong trend)
- Volume Profile (confirm breakouts with volume)
- Compare to XLV/QQQ (relative strength filter)

---

## CRITICAL SUCCESS FACTORS

✅ **DO THIS:**
1. Always filter for price > SMA200 (uptrend confirmation)
2. Prioritize Healthcare + Tech sectors (92% and 71% win rates)
3. Verify options liquidity before deploying capital
4. Use ATR > 2% to ensure enough movement
5. Cross-reference with your backtest data (UNH, MSFT, XLV proven)

❌ **NEVER DO THIS:**
1. Trade utilities (0% success rate across 28 tests)
2. Trade energy without specific setup (21% success rate)
3. Ignore the SMA200 filter (trend is everything)
4. Use tight stops like Alt20 (death by a thousand cuts)
5. Deploy time exits (Alt9) on ETFs (catastrophic on SPY -23.99%)

---

## SUMMARY: SCREENER → STRATEGY → OPTIONS MAPPING

| **Screener**    | **Expected Stocks**           | **Pine Script**      | **Options Strategy**      | **DTE** | **Success Rate** |
| --------------- | ----------------------------- | -------------------- | ------------------------- | ------- | ---------------- |
| Healthcare (#1) | UNH, JNJ, LLY, ABBV, XLV      | Alt43, Alt46, Alt10  | Covered Calls, CSP        | 30-45   | 92.31%           |
| Tech (#2)       | MSFT, GOOGL, QQQ, NVDA, META  | Alt15, Alt22, Alt47  | LEAPS, Spreads, Calls     | 30-60   | 71.43%           |
| Avoidance (#3)  | DUK, XLU, XLE, XOM, Utilities | NONE - DO NOT TRADE  | NONE                      | N/A     | 0.00%            |
| Combo           | Best of #1 + #2               | Alt10, Alt26, Alt43  | Monthly Calls/Puts        | 30-45   | 75%+             |

---

**Generated:** 2025-11-03
**Data Source:** 293 validated backtests across 21 securities × 14 strategies
**Validation:** 99.74% screenshot verification (387/388 healthy)
**Recommendation:** Start with Healthcare (#1), add Tech (#2) after mastery, NEVER trade Screener #3 results
