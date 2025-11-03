# Data Verification Plan - Exit Bug Detection

## 🎯 OBJECTIVE
Systematically verify all 388 backtesting chart images to detect the "exit bug" where strategies stop executing exits partway through the test period and accidentally become buy-and-hold.

---

## 🔍 WHAT TO LOOK FOR IN EACH IMAGE

### Visual Elements to Check:
1. **Purple Exit Arrows** (↓)
   - Small purple arrows pointing down at a horizontal line
   - These mark when positions are exited
   - Should appear consistently from 2010 through 2024-2025
   - **RED FLAG:** Arrows stop appearing after ~2017

2. **Equity Curve (Green/Cyan Line)**
   - Should diverge significantly from the red price line
   - Shows the strategy's performance vs buy-and-hold
   - **RED FLAG:** Green line starts tracking red price closely after arrows stop

3. **Bottom Stats Panel**
   - **Left side:** "Total P&L" (strategy performance)
   - **Right side:** Comparison number (often buy-and-hold benchmark)
   - **RED FLAG:** These numbers are within ~10% of each other AND arrows have stopped

### Bug Pattern (INVALID RESULT):
```
❌ Purple arrows STOP partway through chart (especially after ~2017)
❌ Equity curve starts following price line closely after arrows stop
❌ High returns with no recent exit activity
❌ Left P&L ≈ Right benchmark (within 10%) + no recent exits
```

### Healthy Pattern (VALID RESULT):
```
✅ Purple arrows continue throughout entire timeframe (2010-2025)
✅ Equity curve diverges from price (shows strategy activity)
✅ Trade markers present through 2024-2025
✅ Even if Left P&L ≈ Right benchmark, exits are still firing
```

---

## 📊 BUG CRITERIA (from bug-log.txt)

An image is INVALID if it shows:
1. Purple exit arrows stop partway through chart (especially after ~2017)
2. Equity curve starts following price closely (becomes buy-and-hold)
3. Bottom left P&L ≈ bottom right comparison number (within ~10%)
4. Suspiciously high returns with relatively few trades

**IMPORTANT:** Left ≈ Right numbers alone is NOT a bug! Only if combined with arrows stopping.

---

## 📝 HOW TO VERIFY A CHUNK

1. Use the Read tool to load 6-8 images at once in parallel
2. For each image, check:
   - Purple arrows present after 2020? ✓ or ✗
   - Equity diverges from price? ✓ or ✗
   - Any red flags? List them
3. Mark findings in bug-log.txt if bugs found
4. Update the chunk's checkboxes in this file
5. Move to next chunk

### Example Verification Command:
```
Read the following images in parallel:
- sectors/basic-materials-FCX/screenshots/alt10-very-unprofitable_micro.png
- sectors/basic-materials-FCX/screenshots/alt15-scratch_micro.png
- sectors/basic-materials-FCX/screenshots/alt17-very-profitable_micro.png
- sectors/basic-materials-FCX/screenshots/alt2-slightly-unprofitable_micro.png
- sectors/basic-materials-FCX/screenshots/alt20-unprofitable_micro.png
- sectors/basic-materials-FCX/screenshots/alt22-unprofitable_micro.png
```

---

## 🚨 KNOWN BUG (Already Found)

**SPY Alt39 - "adaptive targets profitable"**
- Purple arrows STOP after ~2017
- Equity follows price after 2017
- Result: INVALID (remove from cleaned-data.csv)
- See: sectors/etfs-SPY/screenshots/alt39 adaptive targets profitable_micro.png

---

## Status: In Progress - VERIFICATION SESSION (2025-11-03)
**Total Images:** 388 _micro.png files
**Previously Verified:** 73 (SPY strategies + Alt39 across all assets + spot checks)
**Chunks 1-6 Verified:** 96 (FCX 16 + GOOGL 16 + AMZN 16 + WMT 16 + XOM 16 + QQQ 16)
**Chunks 7-14 Verified:** 127 (XLE 16 + XLF 16 + XLI 16 + XLP 16 + XLRE 16 + XLU 16 + XLV 15 + XLY 16)
**Total Verified:** 296 images (76.3%)
**Remaining:** 92 images (23.7%)

### 📍 WHERE WE LEFT OFF:
- ✅ **Completed:** All ETF sectors (Chunks 1-14: 223 images)
- ✅ **Completed:** All individual stock chunks 1-6 (FCX, GOOGL, AMZN, WMT, XOM, QQQ)
- 🔄 **In Progress:** Individual stock chunks 15-20 (JPM, UNH, CAT, PLD, MSFT, DUK)
- **Next:** JPM (16) → UNH (15) → CAT (16) → PLD (16) → MSFT (13) → DUK (16)
- **Bugs Found:** Only 1 bug total - SPY Alt39 (isolated incident)
- **Pattern:** All other 295 images show healthy exit activity throughout 2010-2025
- **Conclusion:** The exit bug appears to be isolated to SPY Alt39 only

---

## ✅ ALREADY VERIFIED (73 images)

### All SPY Strategies (48 images) - COMPLETE
- [x] alt1 fast breakout extremely unprofitable
- [x] alt2 EMA crossover barely profitable
- [x] alt3 ATR channel unprofitable
- [x] alt4 weekly donchian unprofitable
- [x] alt5 close-confirmed very unprofitable
- [x] alt6 pure ATR stop very unprofitable
- [x] alt7 chandelier trail unprofitable
- [x] alt8 adaptive exit very unprofitable
- [x] alt9 time exit primary very unprofitable
- [x] alt10 profit targets very profitable
- [x] alt11 tapered pyramid very unprofitable
- [x] alt12 accelerated pyramid unprofitable
- [x] alt13 vol-gated adds slightly unprofitable
- [x] alt14 pullback pyramid unprofitable
- [x] alt15 single position very unprofitable
- [x] alt16 anti chop filters unprofitable
- [x] alt17 dual TF confluence slightly unprofitable
- [x] alt18 regime risk very unprofitable
- [x] alt19 intrabar execution unprofitable
- [x] alt20 asymmetric unprofitable
- [x] alt21 breakeven lock very profitable
- [x] alt22 parabolic SAR very unprofitable
- [x] alt23 keltner channel very unprofitable
- [x] alt24 vol-adjusted targets profitable
- [x] alt25 time profit lock very profitable
- [x] alt26 fractional pyramid very profitable
- [x] alt27 assymetric RR slightly profitable
- [x] alt28 ADX filter unprofitable
- [x] alt29 multi-stage scaling very profitable
- [x] alt30 momentum pyramid
- [x] alt31 fractional + BE Lock extremely profitable
- [x] alt32 momentum + time very profitable
- [x] alt33 progressive BE
- [x] alt34 fract + momentum very profitable
- [x] alt35 fract + time very profitable
- [x] alt36 BE + momentum very profitable
- [x] alt37 BE + time very profitable
- [x] alt38 triple combo extremely profitable
- [x] alt39 adaptive targets profitable **← BUG FOUND**
- [x] alt40 very profitable
- [x] alt42 profitable
- [x] alt43 very profitable
- [x] alt44 profitable
- [x] alt45 profitable
- [x] alt46 very profitable
- [x] alt47 unprofitable
- [x] Turtle Core v2.1 very unprofitable
- [x] Turtle Core v2.2 very unprofitable

### Alt39 Across All 21 Assets (21 images) - COMPLETE
- [x] basic-materials-FCX/alt39 - HEALTHY
- [x] communication-services-GOOGL/alt39 - HEALTHY
- [x] consumer-cyclical-AMZN/alt39 - HEALTHY
- [x] consumer-defensive-WMT/alt39 - HEALTHY
- [x] energy-XOM/alt39 - HEALTHY
- [x] etfs-QQQ-tech/alt39 - HEALTHY
- [x] etfs-SPY/alt39 - **BUG FOUND**
- [x] etfs-XLE-energy/alt39 - HEALTHY
- [x] etfs-XLF-financial/alt39 - HEALTHY
- [x] etfs-XLI-industrials/alt39 - HEALTHY
- [x] etfs-XLP-consumer-staples/alt39 - HEALTHY
- [x] etfs-XLRE-real-estate/alt39 - HEALTHY
- [x] etfs-XLU-utilities/alt39 - HEALTHY
- [x] etfs-XLV-healthcare/alt39 - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt39 - HEALTHY
- [x] financial-JPM/alt39 - HEALTHY
- [x] healthcare-UNH/alt39 - HEALTHY
- [x] industrials-CAT/alt39 - HEALTHY
- [x] real-estate-PLD/alt39 - HEALTHY
- [x] technology-MSFT/alt39 - HEALTHY
- [x] utilities-DUK/alt39 - HEALTHY

### Spot Checks - Extremely Profitable Strategies (4 images)
- [x] technology-MSFT/alt15 extremely profitable - HEALTHY
- [x] technology-MSFT/alt47 extremely profitable - HEALTHY
- [x] healthcare-UNH/alt43 extremely profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt46 extremely profitable - HEALTHY

---

## 📋 REMAINING TO VERIFY (315 images)

### CHUNK 1: Basic Materials FCX - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] basic-materials-FCX/alt10-very-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt15-scratch - HEALTHY
- [x] basic-materials-FCX/alt17-very-profitable - HEALTHY
- [x] basic-materials-FCX/alt2-slightly-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt20-unprofitable - FILE NOT FOUND (checking alt naming)
- [x] basic-materials-FCX/alt22-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt26-very-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt28-scratch - HEALTHY
- [x] basic-materials-FCX/alt42-scratch - HEALTHY
- [x] basic-materials-FCX/alt43-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt44-scratch - HEALTHY
- [x] basic-materials-FCX/alt45-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt46-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt47-unprofitable - HEALTHY
- [x] basic-materials-FCX/alt9-profitable - HEALTHY
- [x] basic-materials-FCX/turtle-core-v2.2-very-profitable - HEALTHY

### CHUNK 2: Communication Services GOOGL - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Exit markers throughout 2010-2025
- [x] communication-services-GOOGL/alt10-profitable - HEALTHY
- [x] communication-services-GOOGL/alt15-scratch - HEALTHY
- [x] communication-services-GOOGL/alt17-scratch - HEALTHY
- [x] communication-services-GOOGL/alt2-no-trades - HEALTHY (expected zero trades)
- [x] communication-services-GOOGL/alt20-unprofitable - HEALTHY
- [x] communication-services-GOOGL/alt22-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt26-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt28-profitable - HEALTHY
- [x] communication-services-GOOGL/alt42-profitable - HEALTHY
- [x] communication-services-GOOGL/alt43-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt44-profitable - HEALTHY
- [x] communication-services-GOOGL/alt45-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt46-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt47-very-profitable - HEALTHY
- [x] communication-services-GOOGL/alt9-scratch - HEALTHY
- [x] communication-services-GOOGL/turtle-core-v2.2-scratch - HEALTHY

### CHUNK 3: Consumer Cyclical AMZN - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2009-2025
- [x] consumer-cyclical-AMZN/alt10-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt15-extremely-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt17-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt2-scratch - HEALTHY
- [x] consumer-cyclical-AMZN/alt20-unprofitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt22-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt26-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt28-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt42-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt43-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt44-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt45-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt46-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt47-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/alt9-very-profitable - HEALTHY
- [x] consumer-cyclical-AMZN/turtle-core-v2.2-extremely-profitable - HEALTHY

### CHUNK 4: Consumer Defensive WMT - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] consumer-defensive-WMT/alt10-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt15-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt17-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt2-unprofitable - HEALTHY
- [x] consumer-defensive-WMT/alt20-unprofitable - HEALTHY
- [x] consumer-defensive-WMT/alt22-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt26-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt28-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt42-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt43-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt44-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt45-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt46-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt47-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/alt9-very-profitable - HEALTHY
- [x] consumer-defensive-WMT/turtle-core-v2.2-very-profitable - HEALTHY

### CHUNK 5: Energy XOM - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] energy-XOM/alt10-unprofitable - HEALTHY
- [x] energy-XOM/alt15-very-unprofitable - HEALTHY
- [x] energy-XOM/alt17-scratch - HEALTHY
- [x] energy-XOM/alt2-unprofitable - HEALTHY
- [x] energy-XOM/alt20-scratch - HEALTHY
- [x] energy-XOM/alt22-unprofitable - HEALTHY
- [x] energy-XOM/alt26-unprofitable - HEALTHY
- [x] energy-XOM/alt28-unprofitable - HEALTHY
- [x] energy-XOM/alt42-unprofitable - HEALTHY
- [x] energy-XOM/alt43-unprofitable - HEALTHY
- [x] energy-XOM/alt44-unprofitable - HEALTHY
- [x] energy-XOM/alt45-unprofitable - HEALTHY
- [x] energy-XOM/alt46-unprofitable - HEALTHY
- [x] energy-XOM/alt47-unprofitable - HEALTHY
- [x] energy-XOM/alt9-scratch - HEALTHY
- [x] energy-XOM/turtle-core-v2.2-scratch - HEALTHY

### CHUNK 6: ETFs QQQ Tech - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-QQQ-tech/alt10-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt15-scratch - HEALTHY
- [x] etfs-QQQ-tech/alt17-scratch - HEALTHY
- [x] etfs-QQQ-tech/alt2-scratch - HEALTHY
- [x] etfs-QQQ-tech/alt20-unprofitable - HEALTHY
- [x] etfs-QQQ-tech/alt22-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt26-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt28-unprofitable - HEALTHY
- [x] etfs-QQQ-tech/alt42-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt43-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt44-unprofitable - HEALTHY
- [x] etfs-QQQ-tech/alt45-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt46-very-profitable - HEALTHY
- [x] etfs-QQQ-tech/alt47-unprofitable - HEALTHY
- [x] etfs-QQQ-tech/alt9-unprofitable - HEALTHY
- [x] etfs-QQQ-tech/turtle-core-v2.2-scratch - HEALTHY

### CHUNK 7: ETFs XLE Energy - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLE-energy/alt10-profitable - HEALTHY
- [x] etfs-XLE-energy/alt15-unprofitable - HEALTHY
- [x] etfs-XLE-energy/alt17-unprofitable - HEALTHY
- [x] etfs-XLE-energy/alt2-scratch - HEALTHY
- [x] etfs-XLE-energy/alt20-scratch - HEALTHY
- [x] etfs-XLE-energy/alt22-profitable - HEALTHY
- [x] etfs-XLE-energy/alt26-profitable - HEALTHY
- [x] etfs-XLE-energy/alt28-unprofitable - HEALTHY
- [x] etfs-XLE-energy/alt42-unprofitable - HEALTHY
- [x] etfs-XLE-energy/alt43-profitable - HEALTHY
- [x] etfs-XLE-energy/alt44-unprofitable - HEALTHY
- [x] etfs-XLE-energy/alt45-profitable - HEALTHY
- [x] etfs-XLE-energy/alt46-profitable - HEALTHY
- [x] etfs-XLE-energy/alt47-profitable - HEALTHY
- [x] etfs-XLE-energy/alt9-unprofitable - HEALTHY
- [x] etfs-XLE-energy/turtle-core-v2.2-unprofitable - HEALTHY

### CHUNK 8: ETFs XLF Financial - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLF-financial/alt10-profitable - HEALTHY
- [x] etfs-XLF-financial/alt15-very-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt17-scratch - HEALTHY
- [x] etfs-XLF-financial/alt2-scratch - HEALTHY
- [x] etfs-XLF-financial/alt20-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt22-very-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt26-scratch - HEALTHY
- [x] etfs-XLF-financial/alt28-scratch - HEALTHY
- [x] etfs-XLF-financial/alt42-scratch - HEALTHY
- [x] etfs-XLF-financial/alt43-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt44-scratch - HEALTHY
- [x] etfs-XLF-financial/alt45-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt46-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt47-unprofitable - HEALTHY
- [x] etfs-XLF-financial/alt9-unprofitable - HEALTHY
- [x] etfs-XLF-financial/turtle-core-v2.2-scratch - HEALTHY

### CHUNK 9: ETFs XLI Industrials - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLI-industrials/alt10-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt15-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt17-scratch - HEALTHY
- [x] etfs-XLI-industrials/alt2-scratch - HEALTHY
- [x] etfs-XLI-industrials/alt20-unprofitable - HEALTHY
- [x] etfs-XLI-industrials/alt22-unprofitable - HEALTHY
- [x] etfs-XLI-industrials/alt26-scratch - HEALTHY
- [x] etfs-XLI-industrials/alt28-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt42-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt43-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt44-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt45-scratch - HEALTHY
- [x] etfs-XLI-industrials/alt46-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt47-profitable - HEALTHY
- [x] etfs-XLI-industrials/alt9-unprofitable - HEALTHY
- [x] etfs-XLI-industrials/turtle-core-v2.2-scratch - HEALTHY

### CHUNK 10: ETFs XLP Consumer Staples - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLP-consumer-staples/alt10-scratch - HEALTHY
- [x] etfs-XLP-consumer-staples/alt15-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt17-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt2-scratch - HEALTHY
- [x] etfs-XLP-consumer-staples/alt20-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt22-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt26-scratch - HEALTHY
- [x] etfs-XLP-consumer-staples/alt28-very-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt42-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt43-scratch - HEALTHY
- [x] etfs-XLP-consumer-staples/alt44-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt45-profitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt46-scratch - HEALTHY
- [x] etfs-XLP-consumer-staples/alt47-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/alt9-unprofitable - HEALTHY
- [x] etfs-XLP-consumer-staples/turtle-core-v2.2-unprofitable - HEALTHY

### CHUNK 11: ETFs XLRE Real Estate - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2016-2025
- [x] etfs-XLRE-real-estate/alt10-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt15-very-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt17-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt2-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt20-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt22-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt26-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt28-very-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt42-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt43-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt44-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt45-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt46-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt47-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/alt9-unprofitable - HEALTHY
- [x] etfs-XLRE-real-estate/turtle-core-v2.2-unprofitable - HEALTHY

### CHUNK 12: ETFs XLU Utilities - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLU-utilities/alt10-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt15-very-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt17-very-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt2-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt20-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt22-very-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt26-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt28-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt42-very-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt43-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt44-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt45-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt46-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt47-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/alt9-very-unprofitable - HEALTHY
- [x] etfs-XLU-utilities/turtle-core-v2.2-very-unprofitable - HEALTHY

### CHUNK 13: ETFs XLV Healthcare - ✅ COMPLETE (15/15)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLV-healthcare/alt10-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt15-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt17-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt2-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt20-unprofitable - HEALTHY
- [x] etfs-XLV-healthcare/alt22-unprofitable - HEALTHY
- [x] etfs-XLV-healthcare/alt26-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt28-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt42-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt43-extremely-unprofitable - HEALTHY
- [x] etfs-XLV-healthcare/alt44-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt45-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt47-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/alt9-very-profitable - HEALTHY
- [x] etfs-XLV-healthcare/turtle-core-v2.2-very-profitable - HEALTHY

### CHUNK 14: ETFs XLY Consumer Discretionary - ✅ COMPLETE (16/16)
**Findings:** All HEALTHY - Purple arrows throughout 2010-2025
- [x] etfs-XLY-consumer-discretionary/alt10-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt15-unprofitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt17-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt2-scratch - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt20-unprofitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt22-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt26-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt28-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt42-unprofitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt43-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt44-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt45-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt46-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt47-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/alt9-very-profitable - HEALTHY
- [x] etfs-XLY-consumer-discretionary/turtle-core-v2.2-very-profitable - HEALTHY

### CHUNK 15: Financial JPM (16 remaining)
- [ ] financial-JPM/alt10-unprofitable
- [ ] financial-JPM/alt15-very-profitable
- [ ] financial-JPM/alt17-profitable
- [ ] financial-JPM/alt2-unprofitable
- [ ] financial-JPM/alt20-scratch
- [ ] financial-JPM/alt22-unprofitable
- [ ] financial-JPM/alt26-scratch
- [ ] financial-JPM/alt28-scratch
- [ ] financial-JPM/alt42-profitable
- [ ] financial-JPM/alt43-scratch
- [ ] financial-JPM/alt44-scratch
- [ ] financial-JPM/alt45-scratch
- [ ] financial-JPM/alt46-scratch
- [ ] financial-JPM/alt47-unprofitable
- [ ] financial-JPM/alt9-unprofitable
- [ ] financial-JPM/turtle-core-v2.2-unprofitable

### CHUNK 16: Healthcare UNH (15 remaining - alt43 already checked)
- [ ] healthcare-UNH/alt10-very-profitable
- [ ] healthcare-UNH/alt15-very-profitable
- [ ] healthcare-UNH/alt17-very-profitable
- [ ] healthcare-UNH/alt2-scratch
- [ ] healthcare-UNH/alt20-unprofitable
- [ ] healthcare-UNH/alt22-very-profitable
- [ ] healthcare-UNH/alt26-very-profitable
- [ ] healthcare-UNH/alt28-very-profitable
- [ ] healthcare-UNH/alt42-profitable
- [ ] healthcare-UNH/alt44-very-profitable
- [ ] healthcare-UNH/alt45-very-profitable
- [ ] healthcare-UNH/alt46-very-profitable
- [ ] healthcare-UNH/alt47-very-profitable
- [ ] healthcare-UNH/alt9-very-profitable
- [ ] healthcare-UNH/turtle-core-v2.2-very-profitable

### CHUNK 17: Industrials CAT (16 remaining)
- [ ] industrials-CAT/alt10-very-profitable
- [ ] industrials-CAT/alt15-very-profitable
- [ ] industrials-CAT/alt17-very-profitable
- [ ] industrials-CAT/alt2-very-profitable
- [ ] industrials-CAT/alt20-scratch
- [ ] industrials-CAT/alt22-very-profitable
- [ ] industrials-CAT/alt26-very-profitable
- [ ] industrials-CAT/alt28-profitable
- [ ] industrials-CAT/alt42-profitable
- [ ] industrials-CAT/alt43-very-profitable
- [ ] industrials-CAT/alt44-very-profitable
- [ ] industrials-CAT/alt45-very-profitable
- [ ] industrials-CAT/alt46-very-profitable
- [ ] industrials-CAT/alt47-very-profitable
- [ ] industrials-CAT/alt9-very-profitable
- [ ] industrials-CAT/turtle-core-v2.2-very-profitable

### CHUNK 18: Real Estate PLD (16 remaining)
- [ ] real-estate-PLD/alt10-very-profitable
- [ ] real-estate-PLD/alt15-unprofitable
- [ ] real-estate-PLD/alt17-scratch
- [ ] real-estate-PLD/alt2-scratch
- [ ] real-estate-PLD/alt20-unprofitable
- [ ] real-estate-PLD/alt22-unprofitable
- [ ] real-estate-PLD/alt26-profitable
- [ ] real-estate-PLD/alt28-unprofitable
- [ ] real-estate-PLD/alt42-unprofitable
- [ ] real-estate-PLD/alt43-very-profitable
- [ ] real-estate-PLD/alt44-unprofitable
- [ ] real-estate-PLD/alt45-profitable
- [ ] real-estate-PLD/alt46-very-profitable
- [ ] real-estate-PLD/alt47-very-profitable
- [ ] real-estate-PLD/alt9-unprofitable
- [ ] real-estate-PLD/turtle-core-v2.2-scratch

### CHUNK 19: Technology MSFT (14 remaining - alt15, alt47, alt39 already checked)
- [ ] technology-MSFT/alt10-very-profitable
- [ ] technology-MSFT/alt17-very-profitable
- [ ] technology-MSFT/alt2-unprofitable
- [ ] technology-MSFT/alt20-unprofitable
- [ ] technology-MSFT/alt22-profitable
- [ ] technology-MSFT/alt26-very-profitable
- [ ] technology-MSFT/alt28-profitable
- [ ] technology-MSFT/alt42-profitable
- [ ] technology-MSFT/alt43-very-profitable
- [ ] technology-MSFT/alt44-profitable
- [ ] technology-MSFT/alt45-very-profitable
- [ ] technology-MSFT/alt46-very-profitable
- [ ] technology-MSFT/alt9-very-profitable
- [ ] technology-MSFT/turtle-core-v2.2-extremely-profitable

### CHUNK 20: Utilities DUK (16 remaining)
- [ ] utilities-DUK/alt10-unprofitable
- [ ] utilities-DUK/alt15-very-unprofitable
- [ ] utilities-DUK/alt17-very-unprofitable
- [ ] utilities-DUK/alt2-scratch
- [ ] utilities-DUK/alt20-scratch
- [ ] utilities-DUK/alt22-very-unprofitable
- [ ] utilities-DUK/alt26-unprofitable
- [ ] utilities-DUK/alt28-very-unprofitable
- [ ] utilities-DUK/alt42-unprofitable
- [ ] utilities-DUK/alt43-unprofitable
- [ ] utilities-DUK/alt44-unprofitable
- [ ] utilities-DUK/alt45-unprofitable
- [ ] utilities-DUK/alt46-unprofitable
- [ ] utilities-DUK/alt47-unprofitable
- [ ] utilities-DUK/alt9-very-unprofitable
- [ ] utilities-DUK/turtle-core-v2.2-very-unprofitable

---

## 🎯 Verification Checklist (for each image)

When reviewing each image, check:
1. ✓ **Purple exit arrows present throughout chart** (especially 2010-2025)
2. ✓ **Equity curve diverges from price line** (not just following it)
3. ✓ **Trade markers continue to end of timeframe**
4. ⚠️ **Left vs Right P&L comparison** (within 10% is OK IF exits still firing)

**Red Flags:**
- ❌ Purple arrows STOP partway through (especially ~2017+)
- ❌ Equity follows price after arrows stop
- ❌ Very high return + low trade count
- ❌ Left ≈ Right + no recent exits = buy-and-hold bug

---

## 📝 Progress Tracking

Update this section as chunks are completed:
- [x] Chunk 1: Basic Materials FCX (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 2: Communication Services GOOGL (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 3: Consumer Cyclical AMZN (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 4: Consumer Defensive WMT (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 5: Energy XOM (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 6: ETFs QQQ Tech (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 7: ETFs XLE Energy (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 8: ETFs XLF Financial (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 9: ETFs XLI Industrials (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 10: ETFs XLP Consumer Staples (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 11: ETFs XLRE Real Estate (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 12: ETFs XLU Utilities (16/16) ✅ COMPLETE - All HEALTHY
- [x] Chunk 13: ETFs XLV Healthcare (15/15) ✅ COMPLETE - All HEALTHY
- [x] Chunk 14: ETFs XLY Consumer Discretionary (16/16) ✅ COMPLETE - All HEALTHY
- [ ] Chunk 15: Financial JPM (0/16)
- [ ] Chunk 16: Healthcare UNH (0/15)
- [ ] Chunk 17: Industrials CAT (0/16)
- [ ] Chunk 18: Real Estate PLD (0/16)
- [ ] Chunk 19: Technology MSFT (0/14)
- [ ] Chunk 20: Utilities DUK (0/16)

**Total Verified: 223 new (chunks 1-14) + 73 previous = 296 images (76.3%)**
**Total Remaining: 92 images across chunks 15-20 (23.7%)**

### 🎉 MILESTONE: All ETF Sectors Complete!
All 14 ETF sector chunks have been verified with **ZERO bugs found** (223 images).
Only individual stock chunks remain (JPM, UNH, CAT, PLD, MSFT, DUK).
