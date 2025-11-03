# EXIT FREQUENCY RANKINGS
## Options Trading Strategy Assignment Guide

**Purpose:** Map each Pine Script strategy to optimal options expiration cycles based on exit frequency.

**Methodology:**
- Backtest period: ~15 years (2010-2025 = 5,475 days)
- Exit frequency = Average trades per year across all tickers
- Categorization: Very High (>150/yr), High (80-150/yr), Medium (40-80/yr), Low (<40/yr)

---

## TIER 1: VERY HIGH FREQUENCY (Weekly Options Territory)

### **Alt26 - Fractional Pyramid: 276 trades on SPY**
**Annual Exit Rate:** ~18.4 exits/year (Every 20 days)
**Best Tickers for High Frequency:**
- SPY: 276 trades (18.4/year)
- FCX: 333 trades (22.2/year) - but unprofitable
- QQQ: 102 trades (6.8/year)

**Options Strategy Match:**
- ✅ **Weekly covered calls** (exit every 20 days = 2-3 week hold)
- ✅ **Monthly cash-secured puts** (scale in/out with fractional sizing)
- ✅ **Credit spreads** (frequent profit-taking aligns with theta decay)

**Ideal Tickers:** SPY, QQQ, XLV, MSFT (all 70+ trades)
**Avoid Tickers:** FCX, DUK, XLRE (high frequency but losing money)

---

### **Alt10 - Profit Targets: 209 trades on SPY**
**Annual Exit Rate:** ~13.9 exits/year (Every 26 days)
**Best Tickers for High Frequency:**
- SPY: 209 trades (13.9/year)
- FCX: 318 trades (21.2/year) - but worst performer
- AMZN: 99 trades (6.6/year)

**Options Strategy Match:**
- ✅ **Weekly/bi-weekly covered calls** (3N/6N/9N profit targets)
- ✅ **Poor man's covered calls** (high trade count = more premium opportunities)
- ✅ **Diagonal spreads** (exit at profit targets, roll frequently)

**Ideal Tickers:** GOOGL, AMZN, WMT, UNH, MSFT, QQQ, XLV, XLY (all 60+ trades)
**Avoid Tickers:** FCX (318 trades but -32% return), DUK (55 trades, -12%)

---

### **Baseline - Original Seykota: 205 trades on FCX**
**Annual Exit Rate:** ~13.7 exits/year (Every 27 days)
**Best Tickers for High Frequency:**
- FCX: 205 trades (13.7/year)
- QQQ: 80 trades (5.3/year)
- XLI: 57 trades (3.8/year)

**Options Strategy Match:**
- ✅ **Monthly covered calls** (frequent exits from ATR stops)
- ⚠️ **Moderate suitability** - exits can be abrupt (stop-outs vs profit targets)

**Ideal Tickers:** FCX, AMZN, WMT, UNH, CAT, XLV (all profitable with 40+ trades)
**Avoid Tickers:** QQQ, XLE, XLF, DUK (unprofitable despite high frequency)

---

## TIER 2: HIGH FREQUENCY (Bi-Weekly to Monthly Options)

### **Alt22 - Parabolic SAR: 121 trades on QQQ**
**Annual Exit Rate:** ~8.1 exits/year (Every 45 days)
**Best Tickers for High Frequency:**
- QQQ: 121 trades (8.1/year) - **RECORD BREAKER** (+32.44%)
- XLY: 107 trades (7.1/year)
- XLI: 104 trades (6.9/year)

**Options Strategy Match:**
- ✅ **30-45 DTE options** (SAR provides dynamic exits)
- ✅ **Covered calls** (QQQ ideal for tech volatility premium)
- ✅ **Strangles/straddles** (tech sector movement benefits)

**Ideal Tickers:** QQQ (exceptional), GOOGL, AMZN, UNH, CAT, MSFT (all 75+ trades)
**Avoid Tickers:** FCX (349 trades but -16%), DUK (63 trades, -16%), XLU (73 trades, -22%)

---

### **Alt39/Alt45 - Dual Momentum: 104 trades on QQQ**
**Annual Exit Rate:** ~6.9 exits/year (Every 53 days)
**Best Tickers for High Frequency:**
- QQQ: 104 trades (6.9/year)
- AMZN: 93 trades (6.2/year)
- XLV: 70 trades (4.7/year)

**Options Strategy Match:**
- ✅ **45-60 DTE covered calls** (2-month hold aligns with exits)
- ✅ **Monthly credit spreads** (momentum filter reduces whipsaws)
- ✅ **LEAPS calendars** (sell monthly against LEAPS positions)

**Ideal Tickers:** GOOGL, AMZN, WMT, UNH, CAT, PLD, MSFT, QQQ, XLV, XLY (all 60+ trades, profitable)
**Avoid Tickers:** FCX (63 trades, -4.47%), DUK (58 trades, -11.45%), XLU (63 trades, -7.46%)

---

### **Alt43/Alt46 - Advanced Profit Targets: 100 trades on AMZN**
**Annual Exit Rate:** ~6.7 exits/year (Every 55 days)
**Best Tickers for High Frequency:**
- AMZN: 100 trades (6.7/year)
- QQQ: 96 trades (6.4/year)
- XLV: 65 trades (4.3/year) - **RECORD RETURN** (+34.80%)

**Options Strategy Match:**
- ✅ **45-60 DTE options** (bi-monthly exits)
- ✅ **Covered calls on healthcare** (XLV 92% sector success rate)
- ✅ **Poor man's covered calls** (tech stocks like GOOGL, MSFT)

**Ideal Tickers:** GOOGL, AMZN, WMT, UNH, CAT, PLD, MSFT, QQQ, XLV, XLY (all 60+ trades, very profitable)
**Avoid Tickers:** FCX (62 trades, -7.19%), DUK (55 trades, -12.58%), XLRE (32 trades, -7.78%)

---

### **Alt47 - Multi-Timeframe: 111 trades on AMZN**
**Annual Exit Rate:** ~7.4 exits/year (Every 49 days)
**Best Tickers for High Frequency:**
- AMZN: 111 trades (7.4/year)
- XLY: 91 trades (6.1/year)
- MSFT: 85 trades (5.7/year)

**Options Strategy Match:**
- ✅ **30-45 DTE credit spreads** (multi-TF filter reduces noise)
- ✅ **Monthly covered calls** (~6 exits/year = consistent premium)
- ✅ **Diagonal spreads** (back-month LEAPS, sell front-month)

**Ideal Tickers:** GOOGL (+25%), WMT (+28.59%), UNH (+24.75%), MSFT (+33.61%), XLV (+29.72%), XLY (+25.23%)
**Record Holder:** CAT - 3.96% max drawdown (lowest ever)

---

## TIER 3: MEDIUM FREQUENCY (Monthly to Quarterly Options)

### **Alt44 - Multi-Timeframe + Filters: 67 trades on MSFT**
**Annual Exit Rate:** ~4.5 exits/year (Every 82 days)
**Best Tickers for Medium Frequency:**
- MSFT: 67 trades (4.5/year)
- QQQ: 63 trades (4.2/year)
- WMT: 51 trades (3.4/year)

**Options Strategy Match:**
- ✅ **60-90 DTE options** (quarterly exits)
- ✅ **LEAPS diagonals** (sell quarterly against back-month)
- ⚠️ **Lower premium income** than high-frequency strategies

**Ideal Tickers:** WMT (+17%), UNH (+17.77% with LEGENDARY 86% win rate), CAT (+18.83%), XLF (+4.99%)
**Avoid Tickers:** QQQ (-3.44%), XLE (-8.71%), DUK (-15.67% catastrophic)

---

### **Alt28 - ADX Filter: 101 trades on SPY**
**Annual Exit Rate:** ~6.7 exits/year (Every 54 days)
**Best Tickers for Medium Frequency:**
- SPY: 101 trades (6.7/year) - but unprofitable (-1.58%)
- MSFT: 67 trades (4.5/year)
- QQQ: 63 trades (4.2/year) - but unprofitable

**Options Strategy Match:**
- ⚠️ **Challenging for options** (ADX filter reduces trade count, mixed results)
- ✅ **60-90 DTE if using healthcare** (UNH +26.61% with 4.809 PF)
- ⛔ **Avoid on broad market** (SPY/QQQ both negative)

**Ideal Tickers:** AMZN (+14.70%), WMT (+12.76%), UNH (+26.61% legendary), CAT (+20.77%), MSFT (+12.67%)
**Avoid Tickers:** DUK (-15.67%), XLP (-12.82%), XLU (-9.48%), XLRE (zero wins)

---

## TIER 4: LOW FREQUENCY (Quarterly to Annual / LEAPS Territory)

### **Alt15 - Single Position Pyramid: 29 trades on QQQ**
**Annual Exit Rate:** ~1.9 exits/year (Every 189 days)
**Best Tickers for Low Frequency:**
- FCX: 83 trades (5.5/year) - but scratch
- QQQ: 29 trades (1.9/year)
- XLF: 22 trades (1.5/year)

**Options Strategy Match:**
- ✅ **LEAPS (6-12 months)** - hold aligns with low exit frequency
- ✅ **Diagonal spreads** (sell monthly against LEAPS)
- ⛔ **Avoid short-dated options** (not enough exits for income)

**Ideal Tickers:** AMZN (+48.63%), MSFT (+52.65% - BEST PERFORMER), UNH (+33.42%), CAT (+27.82%), XLV (+24.19%)
**Avoid Tickers:** XOM (-14.97%), DUK (-29.01% worst individual), SPY (-21.84% catastrophic), XLE (-10.98%)

---

### **Alt42 - Reduced Trade Frequency: 27 trades on XLY**
**Annual Exit Rate:** ~1.8 exits/year (Every 203 days)
**Best Tickers for Low Frequency:**
- XLY: 27 trades (1.8/year) - but unprofitable (-2.80%)
- XOM: 26 trades (1.7/year) - but unprofitable
- GOOGL: 25 trades (1.7/year) - profitable (+6.50%)

**Options Strategy Match:**
- ✅ **LEAPS only** (very low exit frequency)
- ✅ **Buy-and-hold with protective puts** (6-12 month)
- ⚠️ **Poor for income strategies** (too few exits)

**Ideal Tickers:** UNH (+12.44%), MSFT (+13.25%), QQQ (+9.80%), AMZN (+8.20%)
**Avoid Tickers:** XLE (-6.20%), XLU (-12.04%), XLRE (-4.20%), XLP (-3.50%)

---

### **Alt17 - Time-Based with Trailing: 80 trades on QQQ**
**Annual Exit Rate:** ~5.3 exits/year (Every 68 days)
**Best Tickers for Medium Frequency:**
- QQQ: 80 trades (5.3/year) - but scratch (+2.78%)
- FCX: 67 trades (4.5/year) - very profitable (+34.51%)
- XLY: 65 trades (4.3/year)

**Options Strategy Match:**
- ⚠️ **Mixed suitability** - basically mirrors Baseline performance
- ✅ **60-90 DTE if using individual stocks** (FCX, AMZN, WMT profitable)
- ⛔ **Avoid on ETFs** (most are scratch or unprofitable)

**Ideal Tickers:** FCX (+34.51%), AMZN (+34.64%), WMT (+30.47%), MSFT (+35.83%), XLV (+25.05%)
**Avoid Tickers:** SPY (-4.30%), DUK (-20.18%), XLU (-21.48% worst ETF)

---

### **Alt9 - Time Exit (40 bars): 214 trades on FCX**
**Annual Exit Rate:** ~14.3 exits/year (Every 26 days)
**Best Tickers for High Frequency:**
- FCX: 214 trades (14.3/year) - but only +13.69%
- SPY: 174 trades (11.6/year) - **CATASTROPHIC** (-23.99%)
- QQQ: 83 trades (5.5/year)

**Options Strategy Match:**
- ⚠️ **TIME EXITS FAIL ON ETFS** - critical discovery
- ✅ **30-45 DTE on individual stocks only** (AMZN, WMT, UNH, CAT, MSFT)
- ⛔ **NEVER use on broad market ETFs** (SPY -23.99%, XLF -13.62%, XLU -19.13%)

**Ideal Tickers:** AMZN (+37.65%), UNH (+35.87%), CAT (+31.54%), WMT (+30.39%), MSFT (+28.90%), XLV (+29.96%)
**Avoid Tickers:** SPY (-23.99%), DUK (-20.18%), XLU (-19.13%), XLF (-13.62%), XLP (-8.23%)

---

### **Alt20 - Tight Stops (Failed Strategy): 263 trades on SPY**
**Annual Exit Rate:** ~17.5 exits/year (Every 21 days)
**Performance:** UNIVERSALLY NEGATIVE

**Options Strategy Match:**
- ⛔ **DO NOT USE FOR OPTIONS** - tight stops cause excessive exits
- ⛔ **Death by a thousand cuts** - high frequency but all losses
- 📊 **Educational value:** Shows why tight stops don't work in trending systems

**Best Result:** XLE barely break-even (+0.13%)
**Worst Result:** SPY (-13.43% with 263 trades)
**Takeaway:** High exit frequency ≠ profitability

---

### **Alt2 - Experimental (Low Sample): 78 trades on FCX**
**Annual Exit Rate:** ~5.2 exits/year (Every 70 days)
**Performance:** MOSTLY FAILURES (zero trades on many tickers)

**Options Strategy Match:**
- ⛔ **AVOID** - too many zero-trade scenarios
- 📊 **Data anomaly:** GOOGL, AMZN, WMT, XLY had ZERO trades
- ✅ **Exception:** CAT +24.53% (but only 11 trades - outlier)

**Key Insight:** Over-filtering kills strategy viability

---

## SUMMARY: STRATEGY-TO-OPTIONS MAPPING

### **WEEKLY OPTIONS (7-14 DTE):**
- ❌ **None recommended** - even highest frequency strategies average 20-26 day holds

### **BI-WEEKLY OPTIONS (14-21 DTE):**
- ✅ **Alt26 on SPY** (20-day avg hold)
- ✅ **Alt10 on SPY/AMZN** (26-day avg hold)

### **MONTHLY OPTIONS (30-45 DTE):**
- ✅ **Alt22 on QQQ** (45-day hold, +32.44% return)
- ✅ **Alt47 on MSFT/WMT** (49-day hold)
- ✅ **Alt39/Alt45 on healthcare** (53-day hold)
- ✅ **Alt43/Alt46 on XLV** (55-day hold, RECORD +34.80%)

### **QUARTERLY OPTIONS (60-90 DTE):**
- ✅ **Alt44 on UNH** (82-day hold, 86% win rate)
- ✅ **Alt28 on healthcare** (54-day hold, but mixed broad market)

### **LEAPS (6-12 MONTHS):**
- ✅ **Alt15 on MSFT/AMZN** (189-day hold, +52.65% on MSFT)
- ✅ **Alt42 on tech stocks** (203-day hold, low frequency)

---

## OPTIONS INCOME STRATEGY RECOMMENDATIONS

### **COVERED CALLS (Weekly Premium Collection):**
**Best Strategies:** Alt26, Alt10
**Best Tickers:** SPY, QQQ, XLV, MSFT, GOOGL
**Typical Hold:** 20-30 days
**DTE to Sell:** 14-21 days (bi-weekly)

### **CASH-SECURED PUTS (Monthly Income):**
**Best Strategies:** Alt43, Alt46, Alt47
**Best Tickers:** XLV, UNH, MSFT, WMT
**Typical Hold:** 45-60 days
**DTE to Sell:** 30-45 days

### **CREDIT SPREADS (Defined Risk):**
**Best Strategies:** Alt22 (QQQ specialist), Alt39/Alt45
**Best Tickers:** QQQ, XLV, GOOGL, MSFT
**Typical Hold:** 30-55 days
**DTE to Sell:** 30-45 days

### **DIAGONAL SPREADS (LEAPS + Short-Term):**
**Best Strategies:** Alt15, Alt42
**Best Tickers:** MSFT, AMZN, UNH
**Back-Month:** 6-12 month LEAPS
**Front-Month:** 30-45 DTE (roll monthly)

### **THE WHEEL STRATEGY:**
**Best Strategies:** Alt26, Alt43, Alt46
**Best Tickers:** XLV, MSFT, UNH, CAT (low drawdowns)
**Why:** Regular exits for assignment management, low risk

---

## CRITICAL INSIGHTS FOR OPTIONS TRADERS

1. **NO strategy provides true weekly exit frequency** (all average 20+ days)
2. **Monthly options (30-45 DTE) are the sweet spot** for most strategies
3. **Healthcare + Tech sectors** = best options premium environments
4. **Avoid utilities/energy for any options strategy** (0% and 21% win rates)
5. **Low drawdown matters for margin** - Alt26, Alt43, Alt46, Alt47 all < 10% DD on best tickers
6. **Time exits (Alt9) fail on ETFs** - stick to individual stocks if using
7. **Profit targets (Alt10/43/46) >> time exits** for consistent options income

---

**Generated:** 2025-11-03
**Data Source:** cleaned-data.csv (293 backtests, 356 entries)
**Backtest Period:** ~15 years (2010-2025)
