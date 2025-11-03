# Final 10 Diverse Strategies for Sector Testing

## Selection Criteria

After analyzing all 40+ strategies, I've selected 10 that are **maximally different** from each other. The goal is to learn **what works WHERE** across sectors, not just to test SPY winners.

Each strategy tests a fundamentally different hypothesis about trend-following:

---

## The Final 10

### 1. **Baseline** ([Ed-Seykota.pine](pine-scripts/Ed-Seykota.pine))
**Purpose:** Control group - classic Turtle/Seykota approach

**Key Features:**
- Entry: Donchian 55-bar breakout
- Exit: Donchian 10-bar opposite breach + 2N ATR stop
- Position: 4 equal pyramid units (1% risk each)
- Philosophy: Pure trend following

**What It Tests:** Does the classic Turtle system work universally or only on certain assets?

---

### 2. **Alt 2: EMA Crossover** ([19_PF-1.043_seykota_alt2_ema_crossover.pine](pine-scripts/19_PF-1.043_seykota_alt2_ema_crossover.pine))
**Purpose:** Different entry mechanism

**Key Features:**
- Entry: Fast EMA (50) crosses above/below Slow EMA (200)
- Exit: Chandelier trailing stop
- Position: 4 equal units
- Philosophy: Smooth signals, reduce whipsaws

**What It Tests:** Do smoother MA entries beat breakouts in certain sectors (especially choppy ones)?

---

### 3. **Alt 9: Time Exit Primary** ([34_PF-0.700_seykota_alt9_time_exit.pine](pine-scripts/34_PF-0.700_seykota_alt9_time_exit.pine))
**Purpose:** Time decay management

**Key Features:**
- Entry: Donchian breakout
- Exit: Primarily time-based (40 bars), ATR stop as backstop
- Position: 4 equal units
- Philosophy: Trends have finite lifespans

**What It Tests:** Do certain sectors have time-predictable trends? Does sector rotation favor time exits?

---

### 4. **Alt 10: Profit Targets** ([14_PF-1.232_seykota_alt10_profit_targets.pine](pine-scripts/14_PF-1.232_seykota_alt10_profit_targets.pine))
**Purpose:** Take profits early

**Key Features:**
- Entry: Donchian breakout
- Exit: Scale out at 3N, 6N, 9N profit targets + Chandelier trail
- Position: 4 equal units
- Philosophy: Lock in gains, reduce reversal risk

**What It Tests:** Which sectors mean-revert vs trend continuously? Are defensive sectors better with targets?

---

### 5. **Alt 15: Single Position** ([37_PF-0.177_seykota_alt15_single_position.pine](pine-scripts/37_PF-0.177_seykota_alt15_single_position.pine))
**Purpose:** No pyramiding approach

**Key Features:**
- Entry: Donchian breakout
- Exit: Donchian exit + ATR stop
- Position: Single entry, 4% risk upfront, NO adds
- Philosophy: Simpler, front-load exposure

**What It Tests:** Does pyramiding help or hurt in different sectors? High-volatility sectors might favor single positions.

---

### 6. **Alt 17: Dual Timeframe** ([24_PF-0.878_seykota_alt17_dual_timeframe.pine](pine-scripts/24_PF-0.878_seykota_alt17_dual_timeframe.pine))
**Purpose:** Multi-timeframe confluence

**Key Features:**
- Entry: Requires BOTH daily breakout AND weekly trend alignment
- Exit: Donchian + ATR stop
- Position: 4 equal units
- Philosophy: Higher quality, fewer trades

**What It Tests:** Does higher timeframe alignment matter more for certain sectors (e.g., commodities)?

---

### 7. **Alt 20: Asymmetric Long/Short** ([31_PF-0.729_seykota_alt20_asymmetric_long_short.pine](pine-scripts/31_PF-0.729_seykota_alt20_asymmetric_long_short.pine))
**Purpose:** Directional optimization

**Key Features:**
- Entry: Different Donchian lookbacks for longs (55) vs shorts (35)
- Exit: Different stops for longs (2N) vs shorts (2.5N)
- Position: Different max units per direction
- Philosophy: Bulls and bears behave differently

**What It Tests:** Are certain sectors inherently bullish (tech?) or volatile both ways (energy)?

---

### 8. **Alt 22: Parabolic SAR** ([28_PF-0.805_seykota_alt22_parabolic_sar.pine](pine-scripts/28_PF-0.805_seykota_alt22_parabolic_sar.pine))
**Purpose:** Adaptive trailing exits

**Key Features:**
- Entry: Donchian breakout
- Exit: Parabolic SAR (accelerates with trend) + profit targets
- Position: 4 equal units
- Philosophy: Adaptive stop that tightens as trend matures

**What It Tests:** Do strong trending sectors (tech growth?) benefit from accelerating exits?

---

### 9. **Alt 26: Fractional Pyramid** ([04_PF-1.388_seykota_alt26_fractional_pyramid.pine](pine-scripts/04_PF-1.388_seykota_alt26_fractional_pyramid.pine))
**Purpose:** Smart position sizing

**Key Features:**
- Entry: Donchian breakout
- Exit: Chandelier trail + profit targets
- Position: 100% → 75% → 50% → 25% fractional sizing
- Philosophy: Reduce late-stage concentration risk

**What It Tests:** Does fractional sizing help manage volatility in different sectors? High-vol sectors might need this.

---

### 10. **Alt 28: ADX Filter** ([20_PF-0.962_seykota_alt28_adx_filter.pine](pine-scripts/20_PF-0.962_seykota_alt28_adx_filter.pine))
**Purpose:** Trend strength filtering

**Key Features:**
- Entry: Donchian breakout ONLY when ADX > 25
- Exit: Chandelier trail + profit targets
- Position: 4 equal units
- Philosophy: Quality over quantity

**What It Tests:** Are certain sectors more choppy and need filtering? Utilities might need ADX filter, tech might not.

---

## What Each Strategy Tests

| Strategy | Entry Mechanism | Exit Mechanism | Position Management | Key Hypothesis |
|----------|----------------|----------------|---------------------|----------------|
| **Baseline** | Donchian | Donchian + ATR | Standard pyramid | Pure trend following works |
| **Alt 2** | EMA Cross | Chandelier | Standard pyramid | Smooth entries reduce whipsaws |
| **Alt 9** | Donchian | Time-based | Standard pyramid | Trends decay with time |
| **Alt 10** | Donchian | Profit targets | Standard pyramid | Taking profits beats holding |
| **Alt 15** | Donchian | Donchian + ATR | Single position | Pyramiding is risky |
| **Alt 17** | Dual TF | Donchian + ATR | Standard pyramid | Higher TF confirmation helps |
| **Alt 20** | Asymmetric | Asymmetric | Standard pyramid | Longs/shorts differ |
| **Alt 22** | Donchian | Parabolic SAR | Standard pyramid | Adaptive exits work better |
| **Alt 26** | Donchian | Chandelier + targets | Fractional pyramid | Smart sizing reduces risk |
| **Alt 28** | ADX filtered | Chandelier + targets | Standard pyramid | Quality entries beat quantity |

---

## Diversity Matrix

### Entry Mechanisms (6 types):
1. **Pure Donchian:** Baseline, 9, 10, 15, 22, 26
2. **EMA Crossover:** 2
3. **Dual Timeframe:** 17
4. **ADX Filtered:** 28
5. **Asymmetric Donchian:** 20

### Exit Mechanisms (5 types):
1. **Donchian Exit:** Baseline, 15, 17, 20
2. **Chandelier Trail:** 2, 26
3. **Profit Targets:** 10, 22, 26, 28
4. **Parabolic SAR:** 22
5. **Time-Based:** 9

### Position Management (3 types):
1. **Standard Pyramid (4x1%):** Baseline, 2, 9, 10, 17, 20, 22, 28
2. **Fractional Pyramid (100-75-50-25%):** 26
3. **Single Position (4%):** 15

---

## Expected Learnings by Sector

### Technology (High Growth, High Volatility)
- **Hypothesis:** Strong trends, low chop
- **Expect to work:** Baseline, Alt 22 (SAR), Alt 26 (fractional)
- **Expect to fail:** Alt 9 (time), Alt 28 (ADX filter not needed)

### Utilities (Low Volatility, Defensive)
- **Hypothesis:** Choppy, range-bound
- **Expect to work:** Alt 10 (targets), Alt 28 (ADX filter), Alt 2 (EMA)
- **Expect to fail:** Baseline, Alt 22 (too aggressive)

### Energy (High Volatility, Cyclical)
- **Hypothesis:** Strong trends but whipsaw-prone
- **Expect to work:** Alt 26 (fractional), Alt 28 (ADX), Alt 17 (dual TF)
- **Expect to fail:** Alt 15 (single position too risky)

### Financials (Moderate Volatility, Economic Sensitivity)
- **Hypothesis:** Trending but sensitive to economic cycles
- **Expect to work:** Alt 17 (dual TF), Baseline, Alt 20 (asymmetric)
- **Expect to fail:** Alt 9 (time-based)

### Healthcare (Defensive but Growth)
- **Hypothesis:** Steady trends, less choppy
- **Expect to work:** Baseline, Alt 2 (EMA), Alt 26 (fractional)
- **Expect to fail:** Alt 28 (over-filtering)

---

## Testing Protocol

For each sector, test all 10 strategies on 2-3 representative tickers.

### Quick Testing Order (Most Informative First):

**Round 1: Foundation** (Test these first)
1. **Baseline** - Control
2. **Alt 15** - Single position (tests if pyramiding matters)
3. **Alt 26** - Fractional (tests if sizing matters)

**Round 2: Entry Variations** (If Round 1 shows profitability)
4. **Alt 2** - EMA entry
5. **Alt 28** - ADX filter
6. **Alt 17** - Dual timeframe

**Round 3: Exit Variations** (If Round 1 shows profitability)
7. **Alt 10** - Profit targets
8. **Alt 22** - Parabolic SAR
9. **Alt 9** - Time exit

**Round 4: Special Cases** (After patterns emerge)
10. **Alt 20** - Asymmetric (tests directional bias)

---

## Key Questions to Answer

1. **Does pyramiding help or hurt by sector?**
   - Compare: Baseline vs Alt 15 vs Alt 26

2. **Do smoother entries reduce whipsaws in choppy sectors?**
   - Compare: Baseline vs Alt 2 vs Alt 28

3. **Should we take profits early in mean-reverting sectors?**
   - Compare: Baseline vs Alt 10

4. **Does higher timeframe confirmation improve trade quality?**
   - Compare: Baseline vs Alt 17

5. **Are certain sectors inherently bullish or bearish?**
   - Test: Alt 20 (asymmetric)

6. **Do adaptive exits work better in strong trends?**
   - Compare: Baseline vs Alt 22

7. **Do time-based exits work for sector rotation?**
   - Test: Alt 9 across all sectors

---

## Success Criteria

For each strategy-sector combination, document:

| Metric | Baseline | Alt 2 | Alt 9 | Alt 10 | Alt 15 | Alt 17 | Alt 20 | Alt 22 | Alt 26 | Alt 28 |
|--------|----------|-------|-------|--------|--------|--------|--------|--------|--------|--------|
| Profit Factor | | | | | | | | | | |
| Win Rate % | | | | | | | | | | |
| Max Drawdown % | | | | | | | | | | |
| # of Trades | | | | | | | | | | |
| Best/Worst Metric | | | | | | | | | | |

**Minimum Standards:**
- Profit Factor > 1.2
- Win Rate > 38%
- Max Drawdown < 35%
- Trades > 30 (sufficient sample)

---

## After Testing All Sectors

You'll be able to answer:

1. **Which strategies are "universal"?** (Work across many sectors)
2. **Which strategies are "sector-specific"?** (Only work in certain sectors)
3. **Which sectors are "trend-friendly"?** (Many strategies work)
4. **Which sectors are "difficult"?** (Few strategies work)
5. **Do you need a sector-rotation strategy selector?**

---

## Next Steps

1. Copy these 10 .pine files to each sector's `strategies/` folder as you test
2. Use [SECTOR_TICKERS.md](SECTOR_TICKERS.md) for ticker recommendations
3. Follow [QUICK_TEST_CHECKLIST.md](QUICK_TEST_CHECKLIST.md) for efficient testing
4. Document patterns in a `DISCOVERIES.md` file
5. After testing 3-4 sectors, start looking for patterns

**The goal:** Build a mental model of "Strategy X works for Sector Y because of characteristic Z"

Good luck! This systematic approach will teach you more than testing 40 strategies on just SPY ever could.
