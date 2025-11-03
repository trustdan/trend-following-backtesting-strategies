# Discoveries and Learnings: Systematic Sector Testing

**Testing Period:** November 2025 - Ongoing
**Methodology:** Testing 10 strategies across 11 sector categories + ETFs
**Approach:** Strategy-by-strategy (test one strategy across all sectors, then move to next)

---

## 🎯 Overall Takeaways (Summary - Update as Patterns Emerge)

### Batch 1: Initial 10 Strategies (Current)

#### Universal Truths:
- [ ] _To be filled as patterns emerge..._
- [ ]
- [ ]

#### Sector Characteristics Discovered:
- **Trend-Friendly Sectors:**
- **Choppy/Difficult Sectors:**
- **High Volatility Sectors:**
- **Low Volatility Sectors:**

#### Position Management Insights:
- **Pyramiding helps:**
- **Single position better for:**
- **Fractional sizing best for:**

#### Entry Mechanism Insights:
- **Breakouts work best:**
- **EMA entries preferred:**
- **Filtering required:**
- **Dual TF helps:**

#### Exit Strategy Insights:
- **Profit targets best for:**
- **Trailing stops best for:**
- **Time exits work for:**

#### Directional Insights:
- **Long bias sectors:**
- **Short bias sectors:**
- **Balanced sectors:**

---

### Batch 2: Future Iterations (Reserved)

_This section reserved for findings from optimized strategies, sector-specific variants, or new approaches developed from Batch 1 learnings._

---

## 📊 Strategy-by-Strategy Detailed Findings

---

### 1. TURTLE CORE V2.2 (Baseline)
**File:** `turtle-core-v2.2.pine`
**Philosophy:** Classic Turtle/Seykota - Donchian breakout with standard pyramiding
**Test Status:** [ ] Not Started  [x] In Progress  [ ] Completed

#### Overall Strategy Takeaway:
_High-level summary of where this strategy works/fails and why..._

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | | | | | |
| **Communication Services** | | | | | |
| **Consumer Cyclical** | | | | | |
| **Consumer Defensive** | | | | | |
| **Energy** | | | | | |
| **Financial** | | | | | |
| **Healthcare** | | | | | |
| **Industrials** | | | | | |
| **Real Estate** | | | | | |
| **Technology** | | | | | |
| **Utilities** | | | | | |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | | | | | |
| **Nasdaq** | QQQ | | | | | |
| **Energy** | XLE | | | | | |
| **Financials** | XLF | | | | | |
| **Healthcare** | XLV | | | | | |
| **Industrials** | XLI | | | | | |
| **Consumer Staples** | XLP | | | | | |
| **Consumer Disc** | XLY | | | | | |
| **Real Estate** | XLRE | | | | | |
| **Utilities** | XLRU | | | | | |

#### Key Learnings:
- **Best Sectors:**
- **Worst Sectors:**
- **Common Failure Pattern:**
- **Common Success Pattern:**
- **Surprise Finding:**

#### Specific Observations:
- **Basic Materials:**
- **Communication Services:**
- **Consumer Cyclical:**
- **Consumer Defensive:**
- **Energy:**
- **Financial:**
- **Healthcare:**
- **Industrials:**
- **Real Estate:**
- **Technology:**
- **Utilities:**

---

### 2. ALT2: EMA Crossover
**File:** `alt2.pine`
**Philosophy:** Smooth MA entries to reduce whipsaws
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
EMA crossover drastically reduces trade frequency but filtering is TOO AGGRESSIVE - many sectors produced ZERO trades or ZERO wins. Strategy shows extreme sector sensitivity: one massive outlier (CAT +24%) masks widespread failure. The smooth entry mechanism misses too many valid trends while occasionally catching exceptional moves. Overall: 8 profitable, 3 scratch, 10 unprofitable out of 21 sectors tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | -1.73% | 0.941 | 43.59% (34/78) | 11.12% | Slightly unprofitable, decent trade count |
| **Communication Services** | 0.00% | N/A | N/A (0/0) | 0.00% | NO TRADES - over-filtered |
| **Consumer Cyclical** | ~0.00% | N/A | N/A | N/A | Scratch - minimal activity |
| **Consumer Defensive** | -4.35% | 0.00 | 0.00% (0/5) | 4.35% | ALL LOSSES - brutal |
| **Energy** | -6.23% | 0.037 | 9.09% (1/11) | 6.23% | Nearly all losses |
| **Financial** | -1.24% | 0.726 | 40.00% (4/10) | 4.69% | Below breakeven |
| **Healthcare** | +0.24% | 1.104 | 57.14% (4/7) | 2.26% | Barely profitable |
| **Industrials** | +24.53% | 16.77 | 72.73% (8/11) | 1.83% | **EXCEPTIONAL - huge outlier** |
| **Real Estate** | +2.63% | 3.681 | 66.67% (4/6) | 2.14% | Profitable |
| **Technology** | -8.97% | 0.00 | 0.00% (0/14) | 8.97% | **WORST - zero wins** |
| **Utilities** | +0.11% | 1.043 | 50.00% (5/10) | 2.85% | Barely profitable |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | +12.38% | 1.043 | 41.18% (21/51) | 8.24% | Profitable despite low win% |
| **Nasdaq** | QQQ | -0.06% | 0.895 | 50.00% (2/4) | 0.36% | Scratch - very few trades |
| **Energy** | XLE | +2.13% | 1.336 | 47.37% (9/19) | 6.90% | Profitable |
| **Financials** | XLF | +0.07% | 1.151 | 50.00% (2/4) | 0.17% | Barely profitable, low trades |
| **Healthcare** | XLV | +3.83% | ∞ | 100.00% (4/4) | 0.85% | Perfect 4/4 wins! |
| **Industrials** | XLI | -0.08% | 0.837 | 50.00% (2/4) | 0.41% | Scratch - very few trades |
| **Consumer Staples** | XLP | -2.26% | 0.00 | 0.00% (0/4) | 2.26% | ALL LOSSES |
| **Consumer Disc** | XLY | -0.43% | 0.00 | 0.00% (0/1) | 0.82% | Only 1 trade - lost |
| **Real Estate** | XLRE | -3.82% | 0.00 | 0.00% (0/6) | 3.82% | ALL LOSSES |
| **Utilities** | XLU | -0.70% | 0.626 | 71.43% (5/7) | 2.69% | High win% but still lost money |

#### Key Learnings:
- **Best Sectors:** CAT (Industrials stock) is a massive outlier at +24.53% with PF: 16.77 - nothing else comes close
- **Worst Sectors:** MSFT (-8.97%), XOM (-6.23%), WMT (-4.35%), XLRE (-3.82%) - all with 0-9% win rates
- **Vs Baseline (Turtle Core):** NOT YET TESTED - baseline data needed for comparison
- **Common Failure Pattern:** Over-filtering leads to ZERO winning trades in 5 sectors (GOOG, WMT, MSFT, XLP, XLRE, XLY)
- **Common Success Pattern:** When it works, it REALLY works (CAT, XLV) - but these are rare exceptions
- **Surprise Finding:** XLU had 71% win rate but STILL lost money - winners too small vs losses

#### Specific Observations:
- **Basic Materials (FCX):** Produced most trades (78) but couldn't turn profit - death by 1000 cuts
- **Communication Services (GOOG):** Completely filtered out - zero signals generated
- **Consumer Cyclical (AMZN):** Near-zero activity suggests over-filtering on strong trending stock
- **Consumer Defensive (WMT):** 5 trades, 5 losses - EMA crossover caught every false signal
- **Energy (XOM):** Only 1 winner in 11 trades (9% win rate) - catastrophic
- **Financial (JPM):** 40% win rate not enough to overcome losses - negative PF
- **Healthcare (UNH):** Barely profitable stock vs XLV ETF (perfect 4/4) - ETF diversification helped
- **Industrials (CAT):** The golden child - 72.73% win rate, PF 16.77, minimal DD - why so different?
- **Real Estate (PLD):** Stock profitable (+2.63%), ETF (XLRE) failed completely (0% wins) - major divergence
- **Technology (MSFT):** 14 trades, ZERO wins - worst individual performer. QQQ scratch suggests diversification critical
- **Utilities (DUK):** Stock barely profitable, ETF (XLU) unprofitable despite 71% win rate - sizing issue?

---

### 3. ALT9: Time Exit Primary
**File:** `alt9.pine`
**Philosophy:** Trends have finite lifespans - exit after N bars
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**SHOCKING DISCOVERY:** Time exits work BRILLIANTLY on individual growth stocks (+28-38% returns) but CATASTROPHICALLY fail on broad market ETFs (-24% on SPY). This is a complete reversal of conventional wisdom! The 40-bar forced exit captures momentum moves in volatile individual names while cutting winners too early on steadier index ETFs. **For options traders:** This strategy has regular exits (full timeline visible) making it OPTIONS-SUITABLE. Success pattern: high-growth individual stocks with strong momentum. Failure pattern: diversified ETFs and defensive sectors. Overall: 7 very profitable, 1 profitable, 2 scratch, 11 unprofitable out of 21 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | +13.69% | 1.093 | 33.18% (71/214) | 36.10% | Profitable with many trades |
| **Communication Services** | -7.22% | 0.975 | 28.30% (15/53) | 11.61% | Scratch/slightly unprofitable |
| **Consumer Cyclical** | +37.65% | 2.463 | 47.27% (26/55) | 11.99% | **EXCEPTIONAL - best performer** |
| **Consumer Defensive** | +30.39% | 2.428 | 45.65% (21/46) | 6.68% | **OUTSTANDING - low DD** |
| **Energy** | -0.47% | 0.979 | 30.00% (12/40) | 13.86% | Scratch - barely breakeven |
| **Financial** | -0.29% | 0.924 | 34.00% (17/50) | 12.01% | Scratch - essentially flat |
| **Healthcare** | +35.87% | 1.964 | 45.76% (27/59) | 17.64% | **EXCELLENT - consistent wins** |
| **Industrials** | +31.54% | 2.017 | 38.64% (17/44) | 6.78% | **VERY STRONG - low DD** |
| **Real Estate** | -1.25% | 0.935 | 43.18% (19/44) | 8.33% | Unprofitable despite decent win% |
| **Technology** | +28.90% | 2.141 | 43.40% (23/53) | 8.80% | **EXCELLENT - strong tech name** |
| **Utilities** | -20.18% | 0.215 | 21.43% (9/42) | 21.03% | **DISASTER - worst individual** |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | -23.99% | 0.700 | 36.21% (63/174) | 29.79% | **CATASTROPHIC on broad market** |
| **Nasdaq** | QQQ | -1.44% | 0.835 | 34.94% (29/83) | 11.99% | Unprofitable - time cuts winners |
| **Energy** | XLE | -8.55% | 0.641 | 38.10% (16/42) | 13.48% | Failed badly |
| **Financials** | XLF | -13.62% | 0.587 | 33.90% (20/59) | 21.05% | Severe underperformance |
| **Healthcare** | XLV | +29.96% | 2.102 | 45.10% (23/51) | 8.28% | **EXCEPTION - ETF winner!** |
| **Industrials** | XLI | -4.57% | 0.778 | 32.79% (20/61) | 12.28% | Unprofitable |
| **Consumer Staples** | XLP | -8.23% | 0.655 | 35.09% (20/57) | 11.63% | Failed on defensive sector |
| **Consumer Disc** | XLY | +14.68% | 1.415 | 41.18% (28/68) | 10.77% | Profitable - cyclical works |
| **Real Estate** | XLRE | -4.19% | 0.877 | 39.13% (9/23) | 8.80% | Unprofitable |
| **Utilities** | XLU | -19.13% | 0.283 | 28.57% (14/49) | 23.87% | **TERRIBLE - defensive disaster** |

#### Key Learnings:
- **Best Sectors:** AMZN (+37.7%), UNH (+35.9%), WMT (+30.4%), CAT (+31.5%), XLV (+30.0%), MSFT (+28.9%) - ALL individual growth stocks or healthcare
- **Worst Sectors:** SPY (-24.0%), DUK (-20.2%), XLU (-19.1%), XLF (-13.6%) - broad market and utilities
- **Does time exit EVER work?** YES! But ONLY on individual high-momentum stocks. Complete failure on diversified ETFs
- **Common Failure Pattern:** Diversified ETFs (SPY, QQQ, sector ETFs except XLV/XLY) - time exits cut trends too early on steady grinders
- **Common Success Pattern:** Individual stocks with strong momentum bursts (AMZN, WMT, UNH, CAT, MSFT) - 40-bar window captures explosive moves
- **Surprise Finding:** This CONTRADICTS SPY testing where Alt9 failed! Individual stocks ≠ ETFs for time exits

#### Specific Observations:
- **Basic Materials (FCX):** Profitable (+13.7%) with 214 trades - high activity, modest returns
- **Communication Services (GOOG):** Slight loss (-7.2%), low trade count suggests over-filtering or bad timing
- **Consumer Cyclical (AMZN):** **BEST PERFORMER** at +37.7% with PF 2.463 - time exits capture AMZN's explosive runs perfectly
- **Consumer Defensive (WMT):** **STUNNING +30.4%** - defensive stock acts like growth with forced exits, lowest DD at 6.68%
- **Energy (XOM):** Essentially flat (-0.47%) - choppy energy sector gives no edge to time-based exits
- **Financial (JPM):** Flat (-0.29%) - financials don't trend in 40-bar windows, need longer holds
- **Healthcare (UNH):** **EXCELLENT +35.9%** - healthcare momentum captured beautifully, PF 1.964
- **Industrials (CAT):** **VERY STRONG +31.5%** - industrial cycles fit 40-bar exit window, low 6.78% DD
- **Real Estate (PLD):** Slight loss (-1.3%) despite 43% win rate - winners too small, common RE pattern
- **Technology (MSFT):** **STRONG +28.9%** - tech momentum plays well with time exits, PF 2.141
- **Utilities (DUK):** **WORST INDIVIDUAL at -20.2%** - defensive utilities completely incompatible with forced exits, PF 0.215
- **ETF Insight:** Only XLV (+30%) and XLY (+14.7%) profitable - both have growth/momentum characteristics. SPY/QQQ/defensive sectors all fail

---

### 4. ALT10: Profit Targets
**File:** `alt10.pine`
**Philosophy:** Lock in gains at 3N, 6N, 9N - reduce reversal risk
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**BREAKTHROUGH STRATEGY!** Profit targets deliver the BEST overall performance so far with 76% profitable rate (16/21). Unlike Alt9 time exits which failed on ETFs, profit targets work BRILLIANTLY on both individual stocks AND broad market ETFs. The 3N-6N-9N scaling exits lock in gains while still capturing major trends. This strategy TRANSFORMS SPY from catastrophic failure (Alt9: -24%) to strong success (Alt10: +20%). Healthcare dominates with UNH at +33% (best performer), while commodities crater with FCX at -32% (worst by far). The hypothesis that profit targets help mean-reverting sectors is REJECTED for utilities but CONFIRMED for trending defensive stocks like WMT. **For options traders:** Regular profit taking creates natural exit points - OPTIONS-SUITABLE. Overall: 13 very profitable, 3 profitable, 1 scratch, 4 unprofitable out of 21 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | -32.21% | 0.754 | 39.31% (125/318) | 34.85% | **WORST PERFORMER** - catastrophic losses |
| **Communication Services** | +21.77% | 1.708 | 52.86% (37/70) | 8.46% | Very profitable, low DD |
| **Consumer Cyclical** | +21.94% | 1.661 | 54.55% (54/99) | 10.50% | Very profitable - AMZN loves profit targets |
| **Consumer Defensive** | +24.48% | 2.084 | 52.46% (32/61) | 9.00% | **EXCELLENT** - trending defensive works! |
| **Energy** | -7.75% | 0.757 | 39.66% (23/58) | 13.97% | Unprofitable - choppy commodity |
| **Financial** | -1.26% | 0.899 | 49.28% (34/69) | 10.55% | Scratch - nearly breakeven |
| **Healthcare** | +33.13% | 2.312 | 57.58% (38/66) | 6.99% | **BEST PERFORMER** - stunning! |
| **Industrials** | +20.56% | 2.588 | 58.82% (30/51) | 5.34% | **EXCEPTIONAL** - lowest DD! |
| **Real Estate** | +20.56% | 2.588 | 58.82% (30/51) | 5.34% | Very profitable stock (vs ETF failure) |
| **Technology** | +22.47% | 1.877 | 50.65% (39/77) | 10.82% | Very profitable - consistent |
| **Utilities** | -12.39% | 0.563 | 36.36% (20/55) | 19.96% | Failed badly - hypothesis rejected |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | +20.31% | 1.232 | 48.33% (101/209) | 16.75% | **HUGE vs Alt9 (-24%)** - 44% swing! |
| **Nasdaq** | QQQ | +22.75% | 1.495 | 54.17% (52/96) | 8.28% | Very profitable, low DD |
| **Energy** | XLE | +5.94% | 1.218 | 44.83% (26/58) | 13.81% | Profitable - better than XOM stock |
| **Financials** | XLF | +10.79% | 1.447 | 54.55% (36/66) | 8.27% | Profitable - ETF beats stock! |
| **Healthcare** | XLV | +27.68% | 2.22 | 59.70% (40/67) | 8.91% | **OUTSTANDING** - near 60% win rate |
| **Industrials** | XLI | +4.42% | 1.089 | 46.38% (32/69) | 12.87% | Profitable but modest |
| **Consumer Staples** | XLP | +1.86% | 1.079 | 51.61% (32/62) | 14.14% | Scratch - barely breakeven |
| **Consumer Disc** | XLY | +22.79% | 1.754 | 60.53% (46/76) | 11.05% | **EXCELLENT** - highest win rate! |
| **Real Estate** | XLRE | -7.27% | 0.583 | 37.50% (12/32) | 11.09% | Failed - major divergence from PLD |
| **Utilities** | XLU | -7.13% | 0.657 | 35.48% (22/62) | 14.59% | Failed - defensive doesn't mean profitable |

#### Key Learnings:
- **Best Sectors:** UNH (+33.1%), WMT (+24.5%), XLV (+27.7%), GOOG (+21.8%), AMZN (+21.9%), MSFT (+22.5%), QQQ (+22.8%), XLY (+22.8%), CAT/PLD (+20.6%)
- **Worst Sectors:** FCX (-32.2% - WORST BY FAR), DUK (-12.4%), XOM (-7.8%), XLRE (-7.3%), XLU (-7.1%)
- **Vs Alt9 (Time Exits):** Profit targets CRUSH time exits on ETFs! SPY: Alt9 (-24%) vs Alt10 (+20%) = 44% improvement!
- **Mean-revert hypothesis:** REJECTED for utilities (DUK/XLU both failed), CONFIRMED for trending defensives (WMT +24.5%)
- **Common Failure Pattern:** Commodities (FCX, XOM), utilities (DUK, XLU), and over-diversified low-activity ETFs (XLRE)
- **Common Success Pattern:** Growth stocks with momentum (AMZN, MSFT, UNH), consumer strength (WMT, XLY), healthcare (UNH, XLV)
- **Surprise Finding #1:** Profit targets work BETTER on broad market ETFs than time exits - complete reversal of Alt9 results!
- **Surprise Finding #2:** FCX is catastrophically bad at -32% despite 318 trades - death by a thousand exits
- **Surprise Finding #3:** Real estate shows MASSIVE stock/ETF divergence: PLD (+20.6%) vs XLRE (-7.3%)

#### Specific Observations:
- **Basic Materials (FCX):** Absolute disaster at -32.2% with 318 trades - profit targets exit too early on commodity mean reversion, catching every false breakout
- **Communication Services (GOOG):** Solid +21.8% with low 8.46% DD - tech growth benefits from scaled profit taking
- **Consumer Cyclical (AMZN):** Excellent +21.9% with PF 1.661 - explosive growth moves hit profit targets before reversing
- **Consumer Defensive (WMT):** Outstanding +24.5% with PF 2.084 and only 9% DD - trending defensive stocks are PERFECT for profit targets!
- **Energy (XOM):** Unprofitable at -7.8% despite 39.7% win rate - choppy commodity whipsaws prevent clean exits. XLE ETF (+5.9%) performs better
- **Financial (JPM):** Nearly breakeven at -1.3% with 49% win rate - financials lack momentum for profit targets to shine. XLF (+10.8%) much better!
- **Healthcare (UNH):** **BEST INDIVIDUAL STOCK** at +33.1% with PF 2.312 and low 7% DD - healthcare trends are clean and profit targets capture them perfectly
- **Industrials (CAT):** Exceptional +20.6% with **LOWEST DD** at 5.34% and PF 2.588 - industrial cycles fit profit target rhythm beautifully
- **Real Estate (PLD):** Stock performs great (+20.6%, PF 2.588), but XLRE ETF crashes (-7.3%) - major divergence suggests individual REIT selection matters
- **Technology (MSFT):** Very strong +22.5% with PF 1.877 - tech growth momentum captured well by stepped profit exits
- **Utilities (DUK):** Failed at -12.4% with terrible PF 0.563 - defensive utilities DON'T mean-revert cleanly, they chop. Hypothesis rejected!
- **ETF Insight:** Alt10 is the FIRST strategy where broad market ETFs (SPY, QQQ) significantly outperform! Profit targets are ETF-FRIENDLY unlike time exits

---

### 5. ALT15: Single Position (No Pyramid)
**File:** `alt15.pine`
**Philosophy:** Pyramiding is risky - one position with full risk upfront
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**SHOCKING REVERSAL!** Single position strategy creates a MASSIVE stock/ETF performance divergence - the complete OPPOSITE of Alt10 (Profit Targets)! Individual growth stocks DOMINATE with 73% profitable rate (MSFT +52.7%, AMZN +48.6%, UNH +33.4%), while broad market ETFs CATASTROPHICALLY FAIL with only 20% profitable rate (SPY -21.8%, XLU -28.2%, XLF -16.2%). The 4% risk-per-trade allocation creates explosive gains on high-momentum individual names but gets crushed on slow-grinding diversified instruments. **KEY FINDING:** Pyramiding is ESSENTIAL for ETFs but OPTIONAL for individual stocks. Growth stocks have inherent volatility that works with full upfront risk, while diversified ETFs need gradual position building to capture their steadier trends. Low trade counts (11-29 trades) suggest single position = longer holds = fewer opportunities. Overall: 7 very profitable, 2 profitable, 1 scratch, 11 unprofitable out of 21 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | +1.65% | 1.008 | 33.73% (28/83) | 39.36% | Scratch - most trades, barely breakeven |
| **Communication Services** | +15.60% | 1.068 | 26.32% (5/19) | 12.22% | Scratch/profitable - borderline |
| **Consumer Cyclical** | +48.63% | 2.283 | 47.37% (9/19) | 16.13% | **EXCEPTIONAL - 2nd best performer** |
| **Consumer Defensive** | +30.14% | 2.073 | 35.29% (6/17) | 11.66% | **EXCELLENT - defensive outperforms!** |
| **Energy** | -14.97% | 0.667 | 21.05% (4/19) | 23.55% | Very unprofitable - commodity disaster |
| **Financial** | +18.53% | 1.521 | 35.29% (6/17) | 17.10% | Very profitable - stock beats ETF! |
| **Healthcare** | +33.42% | 1.746 | 47.62% (10/21) | 19.34% | **EXCELLENT - highest win rate!** |
| **Industrials** | +27.82% | 1.305 | 33.33% (6/18) | 12.21% | Very profitable - low DD |
| **Real Estate** | -5.28% | 0.853 | 41.18% (7/17) | 15.14% | Unprofitable despite 41% win rate |
| **Technology** | +52.65% | 2.598 | 46.67% (7/15) | 9.36% | **BEST PERFORMER - lowest DD!** |
| **Utilities** | -29.01% | 0.280 | 16.67% (3/18) | 33.49% | **WORST INDIVIDUAL - catastrophic** |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | -21.84% | 0.177 | 8.33% (1/12) | 22.02% | **CATASTROPHIC - only 1 winner!** |
| **Nasdaq** | QQQ | +8.28% | 1.025 | 37.93% (11/29) | 16.50% | Scratch - barely breakeven |
| **Energy** | XLE | -10.98% | 0.737 | 26.32% (5/19) | 19.04% | Unprofitable |
| **Financials** | XLF | -16.16% | 0.698 | 27.27% (6/22) | 31.84% | Very unprofitable - brutal DD |
| **Healthcare** | XLV | +24.19% | 1.546 | 38.89% (7/18) | 19.92% | **VERY PROFITABLE - ETF winner!** |
| **Industrials** | XLI | +9.88% | 1.181 | 36.84% (7/19) | 11.43% | Profitable |
| **Consumer Staples** | XLP | -3.25% | 0.875 | 50.00% (8/16) | 18.00% | Unprofitable despite 50% win rate! |
| **Consumer Disc** | XLY | -10.19% | 0.824 | 34.62% (9/26) | 23.39% | Unprofitable |
| **Real Estate** | XLRE | -14.43% | 0.482 | 27.27% (3/11) | 17.03% | Very unprofitable - only 11 trades |
| **Utilities** | XLU | -28.18% | 0.293 | 26.32% (5/19) | 34.24% | **WORST ETF - massive DD** |

#### Key Learnings:
- **Best Sectors:** MSFT (+52.7%), AMZN (+48.6%), UNH (+33.4%), WMT (+30.1%), CAT (+27.8%), XLV (+24.2%), JPM (+18.5%)
- **Worst Sectors:** DUK (-29.0%), XLU (-28.2%), SPY (-21.8%), XLF (-16.2%), XOM (-15.0%), XLRE (-14.4%)
- **When does pyramiding hurt?** NEVER! Removing pyramiding DESTROYS broad market performance. SPY: Alt10 +20.3% vs Alt15 -21.8% = 42% swing!
- **Stock vs ETF:** Individual stocks 73% profitable (7/11 excluding scratches), ETFs only 20% profitable (2/10)
- **Common Failure Pattern:** Diversified ETFs (SPY, XLF, XLE, XLY, XLP, XLRE, XLU) - single position can't capture slow grind
- **Common Success Pattern:** Individual growth stocks (MSFT, AMZN, UNH, WMT, CAT) - explosive moves work with 4% upfront risk
- **Surprise Finding #1:** Technology has LOWEST drawdown (9.36%) despite HIGHEST returns (52.7%) - growth volatility is profitable volatility!
- **Surprise Finding #2:** XLP has 50% win rate but still loses money - winners too small vs losses
- **Surprise Finding #3:** SPY only had 8.33% win rate (1 winner in 12 trades) - devastating for broad market

#### Specific Observations:
- **Basic Materials (FCX):** Scratch at +1.65% with most trades (83) - high activity, no edge without pyramiding. Baseline comparison needed
- **Communication Services (GOOG):** Borderline profitable at +15.6% with only 19 trades - low activity suggests over-filtering or single position limiting opportunities
- **Consumer Cyclical (AMZN):** **EXCEPTIONAL** at +48.6% with PF 2.283 - AMZN's explosive growth moves are PERFECT for single 4% position, no pyramiding needed!
- **Consumer Defensive (WMT):** **EXCELLENT** at +30.1% - defensive stock acts like growth with single position, stunning 2.073 PF
- **Energy (XOM):** Very unprofitable at -15.0% with only 21% win rate - commodity whipsaws destroy single position. XLE ETF (-11.0%) slightly better
- **Financial (JPM):** Very profitable at +18.5%, but XLF ETF catastrophic at -16.2% - MAJOR stock/ETF divergence shows single position needs individual selection
- **Healthcare (UNH):** **EXCELLENT** at +33.4% with highest win rate (47.62%) - healthcare trends are clean, single position captures them well. XLV (+24.2%) also profitable!
- **Industrials (CAT):** Very profitable at +27.8% with low 12.21% DD - industrial cycles work with single full-risk entry. XLI (+9.9%) less impressive
- **Real Estate (PLD):** Unprofitable at -5.28% despite 41% win rate - winners too small. XLRE ETF even worse (-14.4%)
- **Technology (MSFT):** **BEST PERFORMER** at +52.7% with stunning PF 2.598 and LOWEST DD (9.36%) - tech growth is the PERFECT fit for single position strategy!
- **Utilities (DUK):** **WORST INDIVIDUAL** at -29.0% with catastrophic PF 0.28 and only 16.67% win rate - defensive utilities are TOXIC for single position. XLU (-28.2%) equally terrible
- **ETF Insight:** Only XLV (+24.2%) and XLI (+9.9%) profitable - both have growth/momentum characteristics. SPY/QQQ/defensive sectors all fail badly. Pyramiding is CRITICAL for ETFs!

---

### 6. ALT17: Dual Timeframe
**File:** `alt17.pine`
**Philosophy:** Require daily + weekly trend alignment for higher conviction
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**"QUALITY OVER QUANTITY" - THE MIXED BAG!** Dual timeframe filtering dramatically reduces trade frequency (38-80 trades vs 200+) by requiring both daily AND weekly trend alignment. The results are POLARIZED: individual growth stocks still thrive (MSFT +35.8%, AMZN +34.6%, FCX +34.5%), while broad market ETFs STRUGGLE compared to less-filtered strategies. The filtering creates high-conviction entries that work beautifully on strong trending individual names but OVER-FILTERS slow-grinding diversified instruments, causing them to miss too many opportunities. **KEY INSIGHT:** Confluence filtering is a STOCK PICKER'S tool, not an ETF trader's friend. Utilities remain catastrophic (DUK -20.2%, XLU -21.5%). The strategy achieves 57% profitable rate on stocks but only 20% on ETFs. **Vs Alt10:** Individual stocks perform similarly, but ETFs crater (SPY: Alt10 +20.3% vs Alt17 -4.3%). Overall: 6 very profitable, 2 profitable, 5 scratch, 8 unprofitable out of 21 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | +34.51% | 1.735 | 38.81% (26/67) | 11.03% | Very profitable - commodity trends strong |
| **Communication Services** | +7.34% | 0.977 | 30.61% (15/49) | 10.73% | Scratch - borderline, low win rate |
| **Consumer Cyclical** | +34.64% | 2.436 | 48.15% (26/54) | 11.99% | **VERY PROFITABLE** - near 50% win rate |
| **Consumer Defensive** | +30.47% | 2.822 | 48.84% (21/43) | 6.68% | **EXCELLENT** - lowest DD, best PF! |
| **Energy** | +2.88% | 1.134 | 31.58% (12/38) | 13.86% | Scratch - barely breakeven |
| **Financial** | +10.68% | 1.448 | 36.96% (17/46) | 12.01% | Profitable - modest but solid |
| **Healthcare** | +23.38% | 1.722 | 46.55% (27/58) | 18.78% | Very profitable - most trades (58) |
| **Industrials** | +26.20% | 1.795 | 38.64% (17/44) | 6.78% | Very profitable - low DD |
| **Real Estate** | +2.18% | 1.137 | 46.34% (19/41) | 8.33% | Scratch - high win% but small gains |
| **Technology** | +35.83% | 2.68 | 41.86% (18/43) | 8.80% | **BEST PERFORMER** - stunning PF! |
| **Utilities** | -20.18% | 0.215 | 21.43% (9/42) | 21.03% | **CATASTROPHIC** - same as Alt9! |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | -4.30% | 0.878 | 40.54% (30/74) | 14.35% | Unprofitable - over-filtered vs Alt10! |
| **Nasdaq** | QQQ | +2.78% | 0.938 | 36.25% (29/80) | 10.94% | Scratch - most ETF trades (80) |
| **Energy** | XLE | -8.55% | 0.641 | 38.10% (16/42) | 13.48% | Unprofitable - choppy commodity |
| **Financials** | XLF | -0.73% | 0.994 | 37.25% (19/51) | 18.73% | Scratch - nearly breakeven |
| **Healthcare** | XLV | +25.05% | 1.987 | 41.30% (19/46) | 9.73% | **VERY PROFITABLE** - ETF winner! |
| **Industrials** | XLI | +1.90% | 1.018 | 35.09% (20/57) | 9.77% | Scratch - barely breakeven |
| **Consumer Staples** | XLP | -11.19% | 0.527 | 35.09% (20/57) | 12.72% | Unprofitable - defensive fails |
| **Consumer Disc** | XLY | +14.74% | 1.44 | 43.08% (28/65) | 10.77% | Very profitable - cyclical works! |
| **Real Estate** | XLRE | -4.19% | 0.677 | 39.13% (9/23) | 8.80% | Unprofitable - only 23 trades |
| **Utilities** | XLU | -21.48% | 0.203 | 24.49% (12/49) | 25.78% | **WORST ETF** - massive DD |

#### Key Learnings:
- **Best Sectors:** MSFT (+35.8%), AMZN (+34.6%), FCX (+34.5%), WMT (+30.5%), CAT (+26.2%), XLV (+25.0%), UNH (+23.4%)
- **Worst Sectors:** XLU (-21.5%), DUK (-20.2%), XLP (-11.2%), XLE (-8.6%), SPY (-4.3%), XLRE (-4.2%)
- **Does filtering help or hurt?** HELPS individual stocks (fewer whipsaws, better PF), HURTS ETFs (misses too many slow trends)
- **Trade frequency impact:** Dramatically reduced (38-80 trades) vs unfiltered strategies (200+). Quality improves but quantity suffers
- **Vs Alt10 (Profit Targets):** Individual stocks similar performance, but ETFs CRATER! SPY: Alt10 +20.3% vs Alt17 -4.3% = 24.6% decline!
- **Common Failure Pattern:** Broad market ETFs (SPY, QQQ, XLE, XLF, XLI, XLP, XLRE, XLU) - confluence too strict for slow grinders
- **Common Success Pattern:** Trending individual stocks with strong momentum (MSFT, AMZN, FCX, WMT, CAT) - confluence confirms quality entries
- **Surprise Finding #1:** WMT has BEST profit factor (2.822) despite being "defensive" - trending defensive beats choppy growth!
- **Surprise Finding #2:** PLD has 46.34% win rate but only +2.2% return - filtering creates good entries but exits leave money on table
- **Surprise Finding #3:** Utilities IDENTICAL failure to Alt9 (time exits): DUK -20.2% in both! Different mechanisms, same result

#### Specific Observations:
- **Basic Materials (FCX):** Very profitable +34.5% with PF 1.735 - commodity trends are strong enough to satisfy dual TF confluence, 67 trades shows good activity
- **Communication Services (GOOGL):** Scratch at +7.3% with low 30.6% win rate - tech stock struggles with confluence filtering, 49 trades suggests moderate activity
- **Consumer Cyclical (AMZN):** **VERY PROFITABLE** +34.6% with excellent PF 2.436 and near 50% win rate - AMZN's explosive trends satisfy both timeframes perfectly
- **Consumer Defensive (WMT):** **EXCELLENT** +30.5% with BEST PF 2.822 and LOWEST DD 6.68% - defensive stock with strong trend is PERFECT for confluence strategy!
- **Energy (XOM):** Scratch at +2.9% with low 31.6% win rate - choppy commodity can't maintain dual TF alignment, filtering helps avoid worst whipsaws but misses gains
- **Financial (JPM):** Profitable +10.7% with modest PF 1.448 - financials trend enough for confluence to add value over no-filter baseline
- **Healthcare (UNH):** Very profitable +23.4% with MOST trades (58) - healthcare has clean multi-timeframe trends, confluence confirms quality without over-filtering
- **Industrials (CAT):** Very profitable +26.2% with low 6.78% DD and PF 1.795 - industrial cycles align across timeframes, creating high-conviction entries
- **Real Estate (PLD):** Scratch +2.2% despite 46.3% win rate - MAJOR issue: high win rate but small gains = exits too early or filtering cuts trends short
- **Technology (MSFT):** **BEST PERFORMER** +35.8% with stunning PF 2.68 - tech mega-trends satisfy confluence perfectly, low 8.8% DD shows quality entries
- **Utilities (DUK):** **CATASTROPHIC** -20.2% with terrible PF 0.215 and only 21.4% win rate - utilities NEVER trend cleanly on multiple timeframes, identical failure to Alt9!
- **ETF Insight:** Only XLV (+25.0%) and XLY (+14.7%) profitable. SPY (-4.3%) shows confluence is TOO STRICT for broad market - misses too many valid but slow trends. Alt10 (profit targets) FAR BETTER for ETFs!

---

### 7. ALT20: Asymmetric Long/Short
**File:** `alt20.pine`
**Philosophy:** Bulls and bears behave differently - optimize each direction
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**CATASTROPHIC FAILURE ACROSS THE BOARD!** Asymmetric long/short optimization with different parameters for bulls vs bears delivers the WORST overall performance of any strategy tested - a stunning 95% failure rate (0 very profitable, 0 profitable, 5 scratch, 14 unprofitable out of 19 tested). The hypothesis that optimizing longs and shorts separately would improve performance is COMPLETELY REJECTED. Using 55-bar entry and 2.5N stop for longs vs 35-bar entry and 0.75N stop for shorts creates a parameter mismatch that DESTROYS consistency. Shorts get stopped out too early while longs enter too late, resulting in the worst of both worlds. **CRITICAL INSIGHT:** Asymmetric optimization is a trap - markets may have directional bias, but forcing different parameters GUARANTEES underperformance. The ONLY scratch results are commodities (XOM +2.4%, XLE +0.1%) and industrials (CAT +1.2%). Everything else bleeds money. Overall: 0 very profitable, 0 profitable, 5 scratch, 14 unprofitable out of 19 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | NOT TESTED | | | | Missing from test suite |
| **Communication Services** | -7.51% | 0.451 | 37.80% (31/82) | 9.23% | Unprofitable - worst individual stock |
| **Consumer Cyclical** | -2.34% | 0.821 | 39.02% (32/82) | 4.59% | Unprofitable |
| **Consumer Defensive** | -2.53% | 0.707 | 35.71% (25/70) | 4.74% | Unprofitable |
| **Energy** | +2.38% | 1.293 | 38.46% (20/52) | 3.39% | Scratch - only profitable individual |
| **Financial** | -0.46% | 0.942 | 41.25% (33/80) | 2.44% | Scratch - barely breakeven |
| **Healthcare** | -5.31% | 0.557 | 41.38% (36/87) | 7.07% | Unprofitable |
| **Industrials** | +1.21% | 1.129 | 43.21% (35/81) | 2.86% | Scratch - barely positive |
| **Real Estate** | -3.42% | 0.556 | 42.03% (29/69) | 3.73% | Unprofitable |
| **Technology** | -1.27% | 0.913 | 43.56% (44/101) | 3.61% | Unprofitable - most trades (101) |
| **Utilities** | -0.31% | 0.957 | 41.82% (23/55) | 3.44% | Scratch - essentially flat |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | -13.43% | 0.729 | 42.98% (136/263) | 13.82% | **CATASTROPHIC - worst ETF, most trades** |
| **Nasdaq** | QQQ | -6.99% | 0.578 | 39.10% (52/133) | 7.59% | Very unprofitable |
| **Energy** | XLE | +0.13% | 1.016 | 36.84% (21/57) | 2.45% | Scratch - barely positive |
| **Financials** | XLF | -5.66% | 0.558 | 29.21% (26/89) | 6.15% | Unprofitable - lowest win rate! |
| **Healthcare** | XLV | -4.89% | 0.626 | 35.23% (31/88) | 5.28% | Unprofitable |
| **Industrials** | XLI | NOT TESTED | | | | Missing from test suite |
| **Consumer Staples** | XLP | -2.72% | 0.699 | 37.80% (31/82) | 4.16% | Unprofitable |
| **Consumer Disc** | XLY | -4.69% | 0.698 | 34.95% (36/103) | 5.83% | Unprofitable |
| **Real Estate** | XLRE | -3.46% | 0.404 | 35.29% (12/34) | 3.52% | Unprofitable - only 34 trades |
| **Utilities** | XLU | -4.78% | 0.45 | 44.26% (27/61) | 5.26% | Unprofitable despite highest win%! |

#### Key Learnings:
- **Best Sectors:** XOM (+2.4%), CAT (+1.2%), XLE (+0.1%) - ALL barely scratch, commodities only
- **Worst Sectors:** SPY (-13.4%), GOOGL (-7.5%), QQQ (-7.0%), XLF (-5.7%), UNH (-5.3%), XLU (-4.8%)
- **Does asymmetric optimization EVER work?** NO! Forcing different parameters for longs vs shorts destroys consistency
- **Common Failure Pattern:** EVERYTHING! Both individual stocks AND ETFs fail catastrophically
- **Common Success Pattern:** NONE - not a single very profitable or profitable result
- **Surprise Finding #1:** XLU has HIGHEST win rate (44.26%) but still loses -4.78% - parameter mismatch makes winners tiny
- **Surprise Finding #2:** MSFT with most trades (101) still loses money - high activity doesn't help asymmetric strategy
- **Surprise Finding #3:** XLF has LOWEST win rate (29.21%) - financial sector completely incompatible with asymmetric parameters
- **Hypothesis REJECTED:** The idea that bulls and bears behave differently enough to warrant separate optimization is FALSE

#### Specific Observations:
- **Basic Materials (FCX):** NOT TESTED - missing from test suite
- **Communication Services (GOOGL):** **WORST INDIVIDUAL** at -7.51% with terrible PF 0.451 - asymmetric parameters completely misfire on tech growth
- **Consumer Cyclical (AMZN):** Unprofitable -2.34% despite 39% win rate - AMZN's explosive moves get stopped out by tight 0.75N short stops
- **Consumer Defensive (WMT):** Unprofitable -2.53% with PF 0.707 - defensive stock can't benefit from asymmetric optimization
- **Energy (XOM):** Scratch +2.38% with PF 1.293 - ONLY profitable individual stock! Commodity volatility fits asymmetric approach slightly
- **Financial (JPM):** Scratch -0.46% with 41.25% win rate - nearly 263 trades total, parameter confusion creates break-even result
- **Healthcare (UNH):** Unprofitable -5.31% with terrible PF 0.557 despite 41.38% win rate - 87 trades can't overcome parameter mismatch
- **Industrials (CAT):** Scratch +1.21% with PF 1.129 - barely positive, 43.21% win rate suggests asymmetric helps slightly on industrial cycles
- **Real Estate (PLD):** Unprofitable -3.42% with terrible PF 0.556 despite 42.03% win rate - 69 trades, consistent small losses
- **Technology (MSFT):** Unprofitable -1.27% with most trades (101) and highest win rate (43.56%) - HIGH ACTIVITY, ZERO PROFIT! Parameter mismatch kills it
- **Utilities (DUK):** Scratch -0.31% - essentially flat, asymmetric optimization provides no edge on defensive utilities
- **ETF Insight:** SPY is CATASTROPHIC at -13.43% with 263 trades - asymmetric parameters create consistent bleeding on broad market. NO ETF is very profitable or profitable!

---

### 8. ALT22: Parabolic SAR
**File:** `alt22.pine`
**Philosophy:** Adaptive trailing stop that accelerates with trend maturity
**Test Status:** [x] Completed

#### Overall Strategy Takeaway:
**"MOMENTUM OR DEATH" - THE TECH DARLING!** Parabolic SAR creates EXTREME performance polarization - it's either spectacular success or catastrophic failure with NO middle ground! QQQ delivers a STUNNING +32.44% (best ETF performance yet!), while utilities get OBLITERATED (DUK -15.87%, XLU -22.28%). The accelerating trailing stop is PERFECT for strong, sustained tech trends but becomes a WHIPSAW MACHINE in choppy defensive sectors. Individual stocks fare better (54.5% profitable) than ETFs (30% profitable). SPY's shocking -16.70% loss despite 250 trades proves that frequency doesn't equal profitability - the Parabolic SAR overtrades in sideways markets.

**CRITICAL INSIGHT:** Parabolic SAR is NOT a universal tool - it's a SECTOR-SPECIFIC weapon that ONLY works for high-momentum growth stocks. Using it on defensive sectors is financial suicide.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | FCX -16.66% | 0.871 | 44.70% | 33.34% | UNPROFITABLE - 349 trades, massive overtrading in choppy commodity cycle |
| **Communication Services** | GOOGL +22.47% | 1.817 | 54.22% | 6.20% | VERY PROFITABLE - Clean tech trend, low DD, perfect SAR environment |
| **Consumer Cyclical** | AMZN +16.30% | 1.484 | 50.51% | 7.80% | VERY PROFITABLE - Strong momentum, 99 trades optimal |
| **Consumer Defensive** | WMT +7.81% | 1.257 | 50.65% | 8.10% | PROFITABLE - Defensive stock works surprisingly well |
| **Energy** | XOM -1.23% | 0.946 | 40.74% | 12.45% | UNPROFITABLE - Choppy energy cycle destroys SAR |
| **Financial** | JPM -6.90% | 0.772 | 41.98% | 10.71% | UNPROFITABLE - Financial volatility triggers false signals |
| **Healthcare** | UNH +19.27% | 1.602 | 50.54% | 14.34% | VERY PROFITABLE - Healthcare growth trends work well |
| **Industrials** | CAT +18.28% | 1.46 | 47.44% | 7.82% | VERY PROFITABLE - Industrial cycle captured perfectly |
| **Real Estate** | PLD -6.42% | 0.739 | 46.48% | 10.13% | UNPROFITABLE - REIT volatility kills SAR performance |
| **Technology** | MSFT +7.83% | 1.266 | 50.00% | 10.04% | PROFITABLE - Even MSFT works, proving tech bias |
| **Utilities** | DUK -15.87% | 0.381 | 26.98% | 20.53% | VERY UNPROFITABLE - WORST stock performer, low volatility death trap |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | -16.70% | 0.805 | 44.40% | 17.09% | VERY UNPROFITABLE - SHOCKING! 250 trades, massive overtrading |
| **Nasdaq** | QQQ | +32.44% | 1.864 | 59.50% | 6.08% | VERY PROFITABLE - BEST ETF EVER! Perfect tech momentum capture |
| **Energy** | XLE | +1.72% | 1.166 | 46.15% | 8.85% | PROFITABLE - Barely scratches positive |
| **Financials** | XLF | -15.07% | 0.573 | 37.78% | 20.99% | VERY UNPROFITABLE - Financial sector volatility disaster |
| **Healthcare** | XLV | -6.21% | 0.817 | 42.11% | 15.12% | UNPROFITABLE - Individual healthcare stocks work, ETF doesn't |
| **Industrials** | XLI | -0.24% | 0.99 | 50.00% | 8.92% | UNPROFITABLE - Dead flat despite CAT success |
| **Consumer Staples** | XLP | -6.55% | 0.754 | 42.17% | 18.76% | UNPROFITABLE - Defensive sectors whipsaw badly |
| **Consumer Disc** | XLY | +3.09% | 1.083 | 47.66% | 15.73% | PROFITABLE - Consumer discretionary trends captured |
| **Real Estate** | XLRE | -6.57% | 0.571 | 31.43% | 8.72% | UNPROFITABLE - Only 35 trades but still loses |
| **Utilities** | XLU | -22.28% | 0.278 | 26.03% | 22.29% | VERY UNPROFITABLE - CATASTROPHIC! Worst ETF performer |

#### Key Learnings:
- **Best Sectors:** Technology (QQQ +32.44% is LEGENDARY!), Communication Services, Consumer Cyclical - all high-momentum growth sectors
- **Worst Sectors:** Utilities are TOXIC (DUK -15.87%, XLU -22.28%), Financials fail badly, Defensive sectors whipsaw
- **Vs static trailing stops:** Parabolic SAR's acceleration is BRILLIANT for sustained trends but DEADLY in chop - creates 55% performance spread!
- **Trend acceleration matters for:** Tech stocks with strong directional bias - QQQ, GOOGL, AMZN all excel
- **Common Failure Pattern:** Low-volatility defensive sectors (utilities, staples) generate constant whipsaws as SAR tightens, 250 trades on SPY shows overtrading
- **Common Success Pattern:** High-momentum growth stocks with sustained trends allow SAR to accelerate and lock in massive gains (QQQ 59.5% win rate!)
- **Surprise Finding:** SPY's -16.70% loss is SHOCKING - the basket effect kills the strategy while QQQ soars. Individual stock selection MATTERS!

#### Specific Observations:
- **Basic Materials:** FCX generates a MASSIVE 349 trades (highest count!) but loses -16.66% - commodity cyclicality is SAR's worst nightmare
- **Communication Services:** GOOGL's +22.47% with only 6.20% max DD shows perfect trend capture - this is what Parabolic SAR was designed for!
- **Consumer Cyclical:** AMZN +16.30% proves consumer growth trends work beautifully with accelerating stops
- **Consumer Defensive:** WMT's surprising +7.81% shows defensive STOCKS can work, but defensive ETFS (XLP -6.55%) fail
- **Energy:** XOM -1.23% vs XLE +1.72% shows mixed results - energy sector volatility makes SAR unreliable
- **Financial:** JPM -6.90% and XLF -15.07% both fail badly - financial sector whipsaws are SAR killers
- **Healthcare:** MASSIVE divergence! UNH +19.27% (individual stock works) but XLV -6.21% (ETF fails) - stock selection critical
- **Industrials:** CAT +18.28% crushes it but XLI -0.24% flat - another stock vs ETF divergence proving selection matters
- **Real Estate:** PLD -6.42% and XLRE -6.57% both fail - REIT volatility and low momentum doom SAR
- **Technology:** MSFT +7.83% (profitable) and QQQ +32.44% (spectacular!) prove technology is Parabolic SAR's natural habitat
- **Utilities:** DUK -15.87% (PF 0.381, worst stock) and XLU -22.28% (PF 0.278, worst ETF) are both CATASTROPHIC - low volatility meets tight trailing stops equals death

---

### 9. ALT26: Fractional Pyramid
**File:** `alt26.pine`
**Philosophy:** Smart sizing (100%→75%→50%→25%) reduces late-stage risk
**Test Status:** [ ] Not Started  [ ] In Progress  [x] Completed

#### Overall Strategy Takeaway:
**THE GOLDILOCKS STRATEGY - "JUST RIGHT" POSITION SIZING!** Fractional pyramiding delivers OUTSTANDING 76% profitable rate (16/21) and produces the BEST SPY PERFORMANCE of ANY strategy tested (+33.5%)! The 100%→75%→50%→25% scaling creates the perfect balance: aggressive enough to capture trends but defensive enough to protect against late-stage reversals. This is the FIRST strategy where both individual stocks AND broad market ETFs thrive together - no stock/ETF divergence! The smart sizing reduces drawdowns dramatically (most assets have single-digit max DD) while maintaining strong profit factors. Healthcare is spectacular (XLV PF: 2.791, highest ever!), SPY crushes previous records, and even defensive stocks like WMT work beautifully (+13.7%). The ONLY consistent failures are commodities (FCX -20.2%) and utilities (DUK -7.2%). **CRITICAL INSIGHT:** Fractional sizing is the SECRET SAUCE that makes pyramiding work for slow-grinding ETFs - it gives them gradual position building without the excessive risk that destroyed Alt15 (single position). Overall: 10 very profitable, 2 profitable, 3 scratch, 4 unprofitable out of 21 tested.

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | -20.16% | 0.797 | 38.44% (128/333) | 26.39% | **WORST PERFORMER** - commodity disaster |
| **Communication Services** | +18.65% | 2.065 | 53.25% (41/77) | 5.70% | Very profitable - low DD, strong PF |
| **Consumer Cyclical** | +15.34% | 1.66 | 53.06% (52/98) | 8.78% | Very profitable - AMZN loves fractional |
| **Consumer Defensive** | +13.69% | 1.848 | 52.24% (35/67) | 5.96% | Very profitable - defensive works! |
| **Energy** | -6.47% | 0.724 | 39.66% (23/58) | 10.50% | Unprofitable - commodity whipsaw |
| **Financial** | +3.01% | 1.083 | 50.00% (33/66) | 6.79% | Scratch - barely profitable |
| **Healthcare** | +18.73% | 1.991 | 57.14% (40/70) | 5.43% | Very profitable - clean trends |
| **Industrials** | +18.91% | 1.782 | 62.12% (41/66) | 7.93% | **HIGHEST WIN RATE (stock)** - stunning! |
| **Real Estate** | +7.64% | 1.565 | 53.85% (28/52) | 5.11% | Profitable - stock works well |
| **Technology** | +16.33% | 1.947 | 51.81% (43/83) | 4.98% | Very profitable - consistent |
| **Utilities** | -7.24% | 0.644 | 36.36% (20/55) | 13.69% | Unprofitable - defensive fails |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | +33.50% | 1.388 | 50.72% (140/276) | 12.45% | **BEST SPY RESULT EVER!** - stunning |
| **Nasdaq** | QQQ | +21.85% | 1.807 | 56.86% (58/102) | 5.95% | Very profitable - strong tech |
| **Energy** | XLE | +1.89% | 1.092 | 44.07% (26/59) | 8.72% | Profitable - barely positive |
| **Financials** | XLF | +4.25% | 1.253 | 54.93% (39/71) | 6.07% | Scratch/Profitable - borderline |
| **Healthcare** | XLV | +23.48% | 2.791 | 61.43% (43/70) | 5.41% | **HIGHEST PF EVER (2.791)** - legendary! |
| **Industrials** | XLI | +2.13% | 1.031 | 44.00% (33/75) | 8.31% | Scratch - barely breakeven |
| **Consumer Staples** | XLP | +1.19% | 1.065 | 50.00% (32/64) | 10.65% | Scratch - essentially flat |
| **Consumer Disc** | XLY | +11.64% | 1.525 | 58.54% (48/82) | 9.55% | Very profitable - consumer strength |
| **Real Estate** | XLRE | -4.75% | 0.615 | 37.50% (12/32) | 7.68% | Unprofitable - only 32 trades |
| **Utilities** | XLU | -1.74% | 0.848 | 37.88% (25/66) | 11.15% | Unprofitable - defensive disaster |

#### Key Learnings:
- **Best Sectors:** SPY (+33.5% - RECORD!), XLV (+23.5%, PF 2.791 - RECORD!), QQQ (+21.9%), CAT (+18.9%, 62.1% win rate), UNH (+18.7%), GOOGL (+18.7%)
- **Worst Sectors:** FCX (-20.2% - CATASTROPHIC), DUK (-7.2%), XOM (-6.5%), XLRE (-4.8%), XLU (-1.7%)
- **Vs standard pyramid (Baseline):** NOT YET TESTED - baseline data needed
- **Vs single position (Alt15):** MASSIVE REVERSAL! Alt15 destroyed ETFs (-21.8% SPY), Alt26 CRUSHES them (+33.5% SPY) = 55.3% swing!
- **Vs profit targets (Alt10):** Similar overall win rate (76%), but SPY performs BETTER in Alt26 (+33.5% vs +20.3%)
- **Drawdown reduction:** SPECTACULAR! Most assets have single-digit max DD. SPY only 12.45%, MSFT only 4.98%, WMT only 5.96%
- **Common Failure Pattern:** Commodities (FCX, XOM), utilities (DUK, XLU), over-diversified low-activity REITs (XLRE)
- **Common Success Pattern:** Growth stocks AND broad market ETFs both thrive - NO stock/ETF divergence like Alt15!
- **Surprise Finding #1:** SPY +33.5% is the BEST broad market performance of ANY strategy - fractional sizing is ETF-FRIENDLY!
- **Surprise Finding #2:** XLV profit factor of 2.791 with 61.43% win rate is LEGENDARY - the highest PF seen across all tests!
- **Surprise Finding #3:** CAT has 62.12% win rate (highest individual stock) - industrials love gradual position building

#### Specific Observations:
- **Basic Materials (FCX):** **CATASTROPHIC** -20.2% with 333 trades (most activity) and PF 0.797 - commodities can't handle fractional sizing, every whipsaw adds position size that gets stopped out
- **Communication Services (GOOGL):** Very profitable +18.7% with excellent PF 2.065 and low 5.70% DD - tech growth benefits from risk-adjusted position scaling
- **Consumer Cyclical (AMZN):** Very profitable +15.3% with PF 1.66 - AMZN's explosive moves work well with fractional pyramid, captures trends without over-risking
- **Consumer Defensive (WMT):** Very profitable +13.7% with strong PF 1.848 and tiny 5.96% DD - trending defensive stock is PERFECT for smart sizing!
- **Energy (XOM):** Unprofitable -6.5% despite 39.7% win rate - choppy commodity reverses after adding positions. XLE ETF (+1.9%) slightly better but still weak
- **Financial (JPM):** Scratch +3.01% with exactly 50% win rate - financials lack momentum for fractional to shine. XLF (+4.3%) slightly better, ETF diversification helps
- **Healthcare (UNH):** Very profitable +18.7% with PF 1.991 and exceptional 57.14% win rate - healthcare trends captured perfectly by smart sizing
- **Industrials (CAT):** Very profitable +18.9% with **HIGHEST WIN RATE** (62.12%) and PF 1.782 - industrial cycles fit fractional pyramid rhythm beautifully!
- **Real Estate (PLD):** Profitable +7.6% with PF 1.565 - stock performs well, but XLRE ETF fails (-4.8%) suggesting individual REIT selection matters
- **Technology (MSFT):** Very profitable +16.3% with strong PF 1.947 and **LOWEST DD** (4.98%) - tech growth + smart sizing = perfect combo!
- **Utilities (DUK):** Unprofitable -7.2% with terrible PF 0.644 - defensive utilities don't trend cleanly, fractional sizing can't fix choppy assets. XLU (-1.7%) also fails
- **ETF Insight:** Alt26 is the FIRST strategy where broad market ETFs THRIVE! SPY (+33.5%), QQQ (+21.9%), XLV (+23.5%), XLY (+11.6%) all excel. Fractional sizing gives ETFs the gradual position building they need without Alt15's excessive upfront risk!

---

### 10. ALT28: ADX Filter
**File:** `alt28.pine`
**Philosophy:** Only enter when ADX > 25 (strong trend) to avoid chop
**Test Status:** [ ] Not Started  [ ] In Progress  [ ] Completed

#### Overall Strategy Takeaway:
_High-level summary of where this strategy works/fails and why..._

#### Sector Performance Summary:

| Sector | Result | PF | Win% | Max DD | Notes |
|--------|--------|----|----|--------|-------|
| **Basic Materials** | | | | | |
| **Communication Services** | | | | | |
| **Consumer Cyclical** | | | | | |
| **Consumer Defensive** | | | | | |
| **Energy** | | | | | |
| **Financial** | | | | | |
| **Healthcare** | | | | | |
| **Industrials** | | | | | |
| **Real Estate** | | | | | |
| **Technology** | | | | | |
| **Utilities** | | | | | |

#### ETF Performance Summary:

| ETF | Ticker | Result | PF | Win% | Max DD | Notes |
|-----|--------|--------|----|----|--------|-------|
| **S&P 500** | SPY | | | | | |
| **Nasdaq** | QQQ | | | | | |
| **Energy** | XLE | | | | | |
| **Financials** | XLF | | | | | |
| **Healthcare** | XLV | | | | | |
| **Industrials** | XLI | | | | | |
| **Consumer Staples** | XLP | | | | | |
| **Consumer Disc** | XLY | | | | | |
| **Real Estate** | XLRE | | | | | |
| **Utilities** | XLRU | | | | | |

#### Key Learnings:
- **Best Sectors:** (Choppy sectors?)
- **Worst Sectors:** (Clean trending?)
- **Does filtering help or hurt?**
- **Trade frequency impact:**
- **Over-filtering problem:**
- **Common Failure Pattern:**
- **Common Success Pattern:**
- **Surprise Finding:**

#### Specific Observations:
- **Basic Materials:**
- **Communication Services:**
- **Consumer Cyclical:**
- **Consumer Defensive:**
- **Energy:**
- **Financial:**
- **Healthcare:**
- **Industrials:**
- **Real Estate:**
- **Technology:**
- **Utilities:**

---

## 📈 Cross-Strategy Comparisons

### Position Management Battle:
| Sector | Standard Pyramid (Baseline) | Single (Alt15) | Fractional (Alt26) | Winner |
|--------|---------------------------|----------------|-------------------|--------|
| Basic Materials | | | | |
| Communication | | | | |
| Consumer Cyc | | | | |
| Consumer Def | | | | |
| Energy | | | | |
| Financial | | | | |
| Healthcare | | | | |
| Industrials | | | | |
| Real Estate | | | | |
| Technology | | | | |
| Utilities | | | | |

### Entry Mechanism Battle:
| Sector | Donchian (Baseline) | EMA (Alt2) | ADX Filter (Alt28) | Dual TF (Alt17) | Winner |
|--------|-------------------|-----------|-------------------|----------------|--------|
| Basic Materials | | | | | |
| Communication | | | | | |
| Consumer Cyc | | | | | |
| Consumer Def | | | | | |
| Energy | | | | | |
| Financial | | | | | |
| Healthcare | | | | | |
| Industrials | | | | | |
| Real Estate | | | | | |
| Technology | | | | | |
| Utilities | | | | | |

### Exit Strategy Battle:
| Sector | Donchian (Baseline) | Targets (Alt10) | SAR (Alt22) | Time (Alt9) | Winner |
|--------|-------------------|----------------|------------|------------|--------|
| Basic Materials | | | | | |
| Communication | | | | | |
| Consumer Cyc | | | | | |
| Consumer Def | | | | | |
| Energy | | | | | |
| Financial | | | | | |
| Healthcare | | | | | |
| Industrials | | | | | |
| Real Estate | | | | | |
| Technology | | | | | |
| Utilities | | | | | |

---

## 🎯 Strategy Selector Matrix (Final Recommendations)

| Sector | Best Overall | Why? | 2nd Best | 3rd Best |
|--------|--------------|------|----------|----------|
| **Basic Materials** | | | | |
| **Communication Services** | | | | |
| **Consumer Cyclical** | | | | |
| **Consumer Defensive** | | | | |
| **Energy** | | | | |
| **Financial** | | | | |
| **Healthcare** | | | | |
| **Industrials** | | | | |
| **Real Estate** | | | | |
| **Technology** | | | | |
| **Utilities** | | | | |

---

## 🔍 Hypothesis Validation

### Initial Hypotheses (Before Testing):

#### Hypothesis 1: Technology = Strong Trends
- **Expected:** Baseline, Alt26, Alt22 to win
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 2: Utilities = Choppy/Mean-reverting
- **Expected:** Alt10 (targets), Alt28 (ADX), Alt2 (EMA) to win
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 3: Energy = High Vol, Needs Smart Sizing
- **Expected:** Alt26 (fractional), Alt28 (ADX), Alt17 (dual TF) to win
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 4: Pyramiding Helps Trending Sectors
- **Expected:** Baseline > Alt15 in tech, growth sectors
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 5: Time Exits Don't Work Anywhere
- **Expected:** Alt9 fails across all sectors
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 6: Profit Targets Help Defensive Sectors
- **Expected:** Alt10 beats Baseline in utilities, consumer def, real estate
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

#### Hypothesis 7: Tech Has Long Bias
- **Expected:** Alt20 shows strong long bias in tech
- **Actual:**
- **Validation:** ✅ Confirmed / ❌ Rejected / 🤔 Partially

---

## 💡 Unexpected Discoveries

### Surprise #1:
**What happened:**
**Why it matters:**
**How to use this:**

### Surprise #2:
**What happened:**
**Why it matters:**
**How to use this:**

### Surprise #3:
**What happened:**
**Why it matters:**
**How to use this:**

---

## 📝 Methodology Notes

### Testing Consistency:
- **Timeframe:** Daily
- **Date Range:** 2022-01-01 to present
- **Initial Capital:** $100,000
- **Commission:** 0.5% per trade
- **Risk per unit:** 1% (except Alt15 = 4%)

### 🚨 CRITICAL: Interpreting Screenshot Equity Curves (Options Trader Requirement)

**The equity curve X-axis zoom level reveals exit frequency - critical for options traders who need regular position closes.**

#### How to Identify Low-Exit Strategies:

**Full Timeline Visible (Good ✅):**
- Equity curve X-axis spans full backtest period (e.g., 1993-2025)
- Strategy has regular exits throughout
- Total P&L (bottom left) ≈ Equity curve endpoint (bottom right)
- **USE THESE** - suitable for options trading

**Zoomed Timeline (Bad ❌):**
- Equity curve X-axis shows only small window (e.g., 2010-2012)
- TradingView auto-zoomed because few/no exits occur after that period
- Total P&L (bottom left) >> Equity curve endpoint (bottom right)
- Discrepancy = unrealized gains from positions held without exiting
- **DISCARD IMMEDIATELY** - NOT suitable for options traders

#### Real Example - Alt 6 Pure ATR Stop:
- **Total P&L:** +$282,216 (bottom left)
- **Equity Curve Endpoint:** -$15,514 (bottom right)
- **Equity Curve Shows:** Only 2010-2012
- **What This Means:** Strategy had exits 2010-2013, then held long positions continuously through 2025 without exiting
- **Interpretation:** The +$282K includes massive unrealized gains from positions that never closed
- **For Options Traders:** UNUSABLE - options expire, you can't hold indefinitely

#### Why This Matters for Options:
- Stock strategies can hold positions indefinitely and include unrealized gains
- Options have expiration dates - you MUST exit regularly
- A strategy showing few exits means you'd be constantly rolling positions
- High roll costs and time decay make this approach unprofitable for options
- **Only use strategies with equity curves spanning the full backtest timeline**

#### Quick Visual Check:
1. Look at equity curve X-axis dates
2. If range < 50% of full backtest → REJECT
3. If Total P&L ÷ Equity Endpoint > 2.0 → REJECT
4. If zoomed in → strategy holds too long → NOT for options

### Data Quality Issues Encountered:
-

### Sectors/Tickers Skipped and Why:
-

---

## 🚀 Next Steps After Batch 1

Based on findings, consider:
- [ ] Creating sector-optimized variants of winning strategies
- [ ] Testing additional tickers in promising sectors
- [ ] Developing a sector rotation system
- [ ] Building risk-adjusted portfolio using best strategies per sector
- [ ] Backtesting sector-switching signals
- [ ] Creating composite strategies (e.g., "use Alt26 for tech, Alt10 for utilities")

---

## 📚 Reference

**Related Documents:**
- [FINAL_10_STRATEGIES.md](FINAL_10_STRATEGIES.md) - Strategy selection rationale
- [STREAMLINED_TESTING_GUIDE.md](STREAMLINED_TESTING_GUIDE.md) - Testing methodology
- [SECTOR_TICKERS.md](SECTOR_TICKERS.md) - Ticker recommendations

**Last Updated:** [Date]
**Total Strategies Tested:** 10
**Total Sectors Covered:** 11
**Total Tests Completed:** [X/110]
