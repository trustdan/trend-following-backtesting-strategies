```
    ___________                   __   ___________      .__  .__                .__
    \__    ___/______  ____   ____/  |_ \_   _____/____  |  | |  |   ______  _  _|__| ____    ____
      |    |  \_  __ \_/ __ \ /    \   __\|    __)/  _ \ |  | |  |  /  _ \ \/ \/ /  |/    \  / ___\
      |    |   |  | \/\  ___/|   |  \  |  |     \(  <_> )|  |_|  |_(  <_> )     /|  |   |  \/ /_/  >
      |____|   |__|    \___  >___|  /__|  \___  / \____/ |____/____/\____/ \/\_/ |__|___|  /\___  /
                           \/     \/          \/                                         \//_____/
```

# Trend Following Strategy Development Project

A systematic exploration of 40+ trend-following strategies, documenting the journey from -93% to +40% through iterative learning and optimization.

**New to this repository?** Start with [docs/START_HERE.md](docs/START_HERE.md) for a guided introduction, or dive directly into [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md) for comprehensive results from 293 validated backtests.

---

## 💡 KEY TAKEAWAYS (293 Validated Backtests Across 21 Securities)

### The Critical Discovery: Strategy Performance is Asset-Dependent
**What works on SPY often fails elsewhere.** After testing 14 strategies across 21 securities (11 stocks + 10 ETFs), the data reveals that asset characteristics matter more than strategy sophistication. The same strategy can be the best performer on one security and catastrophic on another.

### The Winners: Universal Strategies That Actually Work
1. **Alt10 (Profit Targets)** - 76.19% success rate (16/21 profitable)
   - Explicit 3N-6N-9N profit taking = predictable 3-10 week holds
   - Works on BOTH stocks AND ETFs (rare!)
   - Best for: Healthcare (UNH +33.1%, XLV +27.7%), broad market (SPY +20.3%, QQQ +22.8%)

2. **Alt45 (Dual-Momentum)** - 66.67% success rate (14/21 profitable)
   - 2nd most consistent strategy overall
   - QQQ +29.23%, CAT +28.62%, UNH +27.07%
   - Best for: Growth stocks with strong momentum

3. **Alt26 (Fractional Pyramid)** - 57.14% success rate (12/21 profitable)
   - **Best SPY performer** (+33.50% validated)
   - Lowest drawdowns (MSFT 4.98%, WMT 5.96%)
   - Scale-out exits (100%→75%→50%→25%)

### The Sector Truth: Some Markets Are Untradeable
- **Healthcare:** 12/13 strategies profitable (92% success) - **TRADE THIS**
- **Technology:** 8/10 strategies profitable (80% success) - **TRADE THIS**
- **Utilities:** 0/14 strategies profitable (0% success) - **AVOID COMPLETELY**
- **Energy:** 2/10 strategies profitable (20% success) - **AVOID**

### Record-Breaking Performances (All Validated)
- **Best ETF Result:** XLV Alt46 +34.80% (sector-adaptive parameters)
- **Lowest Drawdown Ever:** CAT Alt47 3.96% max DD (across all 293 backtests!)
- **Highest Win Rate:** UNH Alt28 72.22% (legendary quality)
- **Best Profit Factor:** UNH Alt28 4.809 (exceptional risk/reward)

### Data Quality: 99.74% Validation Rate
After systematic visual verification of all 388 screenshots:
- **1 exit bug found** (SPY Alt39 - purple arrows stopped after 2017)
- **387 results validated** as healthy with proper exit activity
- **Methodology:** Visual inspection of exit markers throughout 2010-2025
- See [data-verification-plan.md](data-verification-plan.md) for complete validation protocol

### The Options Trading Insight
**Not all profitable strategies suit options trading.** Strategies need regular exits (3-12 weeks) to match options expiration. Visual cue: If the equity curve is zoomed (showing only 2010-2012 instead of full timeline), the strategy holds too long for options.

### What Actually Matters (Validated by 293 Backtests)
1. **Exit optimization > Entry optimization** - Where you get out matters more than where you get in
2. **Profit targets are essential** - Multi-stage profit taking (3N, 6N, 9N) outperforms trailing-only
3. **Pyramiding is mandatory** - Single-position strategies catastrophically underperform
4. **Asset selection trumps strategy selection** - Alt10 on Healthcare beats best strategy on Utilities
5. **Simplicity beats complexity** - Top performers use 2-3 enhancements, not kitchen-sink approaches

### The Bottom Line for Traders
**Use Alt10, Alt45, or Alt26 on Healthcare/Technology stocks.** Avoid Utilities and Energy entirely. Test thoroughly on YOUR instruments before live trading - what works on SPY may fail on your ticker.

---

## ✅ Project Status: COMPLETED

**293 Valid Backtests** across 14 strategies and 21 securities (1 removed due to exit bug - see [data-verification-plan.md](data-verification-plan.md))

**Key Findings:**
- **Best Overall Strategy:** Alt10 (Profit Targets) - 76.19% success rate (16/21 profitable)
- **Best SPY Strategy:** Alt26 (Fractional Pyramid) - +33.50% validated result
- **Best ETF Strategy:** Alt46 (Sector Adaptive) - XLV +34.80% return
- **Lowest Drawdown Ever:** Alt47 CAT - 3.96% max DD (across all 293 backtests)
- **Sector Insight:** Healthcare 92% success (12/13), Utilities 0% success (0/14)
- **Data Quality:** 388 screenshots validated, 387 healthy (99.74%), 1 exit bug found (SPY Alt39)

See [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md) for complete analysis.

---

## 🔬 Methodology: How This Research Was Conducted

This project represents a systematic human-AI collaboration for discovering robust trend-following strategies. Here's the exact process used, which anyone can replicate:

### 1. Strategy Generation via AI

**Process:** I used AI (primarily ChatGPT and Claude) to generate individual Pine Script strategies that embody **Ed Seykota's trend-following principles** while testing unique underlying theories.

**Key Prompt Pattern:**
> "Create a TradingView Pine Script strategy that follows Ed Seykota's philosophy of cutting losses and letting winners run. The strategy should test [SPECIFIC THEORY] such as [fractional pyramiding / momentum-gated entries / profit targets / etc.]. Include proper position sizing, ATR-based stops, and Donchian channel entries."

**Why This Worked:**
- AI excels at generating syntactically correct Pine Script code
- Each strategy tested a **distinct hypothesis** (not just parameter tweaks)
- 40+ variations created, each exploring different exit logic, sizing methods, or filters
- AI provided consistent code structure while varying the experimental components

### 2. Manual Testing in TradingView

**Process Overview:** For each AI-generated strategy, I tested it across all 21 securities using an optimized workflow that dramatically reduced testing time.

#### Code Transfer Workflow (Cursor + Vim)

I used **Cursor** (a VS Code fork) with **Vim keybindings** for lightning-fast code copying:

1. Open Pine Script file in Cursor
2. Click anywhere in the file
3. Press `gg` to jump to the top
4. Press `Shift+V` to enter Visual Line mode (selects entire line)
5. Press `G` (uppercase) to extend selection to the bottom of the file
6. Press `Ctrl+C` to copy (standard Windows clipboard)
7. Alt+Tab to TradingView
8. Paste into Pine Editor

**Why This Matters:** The entire code selection process takes <2 seconds. No mouse dragging, no scroll-and-shift-click, just muscle memory keystrokes.

#### Date Range Selection (One-Time Setup Per Strategy)

When first loading a new Pine Script strategy in TradingView:

1. TradingView prompts for backtest date range
2. I selected dates with my mouse:
   - **Start Date:** Beginning of 2010 (roughly January 2010)
   - **End Date:** November 1, 2025 (current date at time of testing)
3. This range was locked in for that strategy session

**Critical Optimization:** Once the strategy and date range were configured, TradingView **remembered these settings**. This meant I could systematically test all 21 securities without having to:
- Re-select the Pine Script strategy for each ticker
- Re-enter the date range for each ticker
- Manually configure any other strategy settings

#### Ticker Switching Workflow (The Speed Secret)

After setting up one strategy with its date range, testing all 21 securities became extremely fast:

1. **Alt+Tab** to TradingView (from documentation/screenshot workflow)
2. Start typing the next ticker symbol (e.g., "M", "S", "F", "T")
3. TradingView automatically opens the ticker search bar
4. TradingView automatically recognizes whether I'm searching for:
   - Individual stock (MSFT, GOOGL, AMZN, etc.)
   - ETF (SPY, QQQ, XLV, XLE, etc.)
5. Press **Enter** to load the ticker
6. Strategy immediately runs on the new security with same date range
7. Review results, capture screenshot (see below)
8. Repeat for next ticker

**Time Savings:** This workflow reduced per-ticker testing from ~2-3 minutes (if reconfiguring each time) to ~15-30 seconds. Testing all 21 securities for one strategy went from 40-60 minutes to approximately 5-10 minutes.

**Example Workflow for Alt47:**
- Load Alt47 Pine Script, set 2010-2025 date range
- Type "FCX" + Enter → Test → Screenshot
- Type "GOOGL" + Enter → Test → Screenshot
- Type "AMZN" + Enter → Test → Screenshot
- ... (18 more securities)
- Complete all 21 tests in <10 minutes

#### Screenshot Capture Workflow

For every backtest result:

1. Strategy runs and displays results in TradingView
2. Press **Win + Shift + S** (Windows Snipping Tool)
3. Draw selection box around Strategy Tester panel
4. Screenshot auto-saves to Windows Photos folder with timestamp
5. Later: Navigate to Photos folder, move screenshots to sector folders
6. Rename to descriptive format: `alt[X]-[result]_reduced.png`

**PowerShell Size Reduction:** After capturing batches of screenshots, I ran [resize_images.ps1](resize_images.ps1) to reduce them by 35% (to 65% of original size). This was necessary because TradingView's high-resolution screenshots often exceeded Claude Code's image processing limits.

#### Standardized Backtest Settings

Every test used identical parameters:
- **Initial Capital:** $100,000
- **Commission:** 0.005% (0.5 basis points)
- **Slippage:** 2 ticks
- **Backtest Period:** ~2010-2025 (approximately 15 years of data)

#### Why Manual Testing Over Automation

Despite the manual workflow, this approach provided advantages automated testing couldn't:
- **Visual equity curve analysis:** Smooth vs choppy growth patterns immediately visible
- **Zoom level indicators:** TradingView auto-zooms when exits are rare (critical warning sign for options traders)
- **Trade distribution patterns:** Clustering of trades reveals market regime sensitivity
- **Drawdown visualization:** Shape and frequency of drawdowns matter, not just max DD number
- **Quick pattern recognition:** Human brain excels at spotting visual anomalies across hundreds of charts

**Result:** 294 backtests completed across 14 strategies and 21 securities with high-quality visual documentation of every result.

### 3. Project Infrastructure via Claude Code

**Process:** I used Claude Code (AI coding assistant) to build the entire project skeleton:

**Folder Structure Created:**
```
sectors/
├── technology-MSFT/
│   ├── screenshots/
│   └── strategies/
├── healthcare-UNH/
│   ├── screenshots/
│   └── strategies/
├── energy-XOM/
├── utilities-DUK/
├── etfs-SPY/
├── etfs-QQQ/
├── etfs-XLV/
... (11 sectors total, 21 securities)
```

**What Claude Code Automated:**
- Created 21 sector folders (11 individual stocks + 10 sector ETFs)
- Generated standardized subfolder structure (screenshots/, strategies/)
- Built utility scripts (resize_images.ps1 for managing screenshot sizes)
- Created documentation templates (DISCOVERIES_AND_LEARNINGS.md, analysis.csv)
- Set up naming conventions and file organization systems

**Why This Mattered:**
- Systematic organization prevents chaos when testing 210+ strategy-security combinations (10 strategies × 21 securities)
- Automated folder creation ensured consistency across all sectors
- Templates enforced disciplined documentation from day one

### 4. Screenshot Capture Workflow

**Process:** For every strategy backtest, I captured evidence using Windows' built-in screenshot tool:

**Steps:**
1. Run backtest in TradingView
2. Press **Win + Shift + S** (Windows Snipping Tool)
3. Draw selection box around TradingView's Strategy Tester panel
4. Screenshot automatically saved to **Windows Photos** folder with timestamp
5. Navigate to Photos folder, locate the screenshot
6. Move screenshot from Photos to appropriate **sectors/[ticker]/screenshots/** folder
7. Rename file to descriptive format: `alt[X]-[result]_reduced.png`
   - Example: `alt26-very-profitable_reduced.png`

**Filename Conventions:**
- `alt[X]` = Strategy number being tested
- `[result]` = Performance category (very-profitable, profitable, scratch, unprofitable, catastrophic)
- `_reduced` = Indicates image has been resized (see next section)

**Why Screenshots:**
- Visual proof of every backtest result
- Equity curve reveals characteristics automated metrics miss
- Screenshots show TradingView's complete performance panel (trades, win rate, PF, drawdown, equity curve)
- Creates audit trail - anyone can verify results

### 5. Image Size Management

**The Problem:** TradingView's high-resolution screenshots often exceeded 3000 pixels wide, which Claude Code couldn't process for analysis.

**The Solution:** Created [resize_images.ps1](resize_images.ps1) PowerShell script:

**What It Does:**
```powershell
# Reduces all images by 35% (to 65% of original size)
# Recursively finds PNG/JPG files in all sector folders
# Skips files already containing "_reduced" in filename
# Uses high-quality bicubic interpolation
# Deletes original large files after successful resize
# Adds "_reduced" suffix to processed files
```

**Why 35% Reduction:**
- Brings 4000px+ screenshots down to ~2600px (within Claude Code's limits)
- Preserves visual quality for analysis (bicubic interpolation)
- Reduces repository size significantly (hundreds of screenshots)
- Prevents recursive resizing (skips files with `_reduced` suffix)

**Usage:**
```powershell
.\resize_images.ps1
# Processes all new screenshots in one batch
# Safe to run multiple times (won't re-process reduced images)
```

### 6. Screenshot Validation and Bug Detection

**The Problem:** After capturing 388 backtest screenshots, a critical quality issue emerged: some strategies appeared profitable but were actually defective. The "exit bug" caused strategies to stop executing exits partway through the test period, accidentally becoming buy-and-hold instead of actively trading.

**The Discovery:** During analysis, one result looked suspicious - **SPY Alt39** showed +121.89% returns but with visual anomalies:
- Purple exit arrows (marking position closures) **stopped appearing after ~2017**
- Equity curve began tracking the price line closely after 2017
- High returns with relatively few recent trades

This revealed a coding bug where the exit logic failed partway through the backtest, turning an active strategy into passive buy-and-hold. The inflated returns were misleading.

**The Solution: Systematic Visual Validation**

Created [bug-log.txt](bug-log.txt) and [data-verification-plan.md](data-verification-plan.md) to systematically audit all 388 screenshots:

**What We Check For:**
1. **Purple exit arrows** - Should appear consistently from 2010 through 2024-2025
   - ❌ RED FLAG: Arrows stop partway through (especially after ~2017)
2. **Equity curve behavior** - Should diverge from price line (shows strategy activity)
   - ❌ RED FLAG: Green line starts tracking red price closely after arrows stop
3. **Performance stats** - Bottom left P&L vs right benchmark
   - ❌ RED FLAG: Numbers within ~10% of each other AND arrows have stopped
4. **Trade frequency** - Should see consistent activity throughout timeframe
   - ❌ RED FLAG: High returns with no recent exit activity

**Key Insight:** Left P&L ≈ Right benchmark alone is NOT a bug! Some strategies legitimately perform similar to buy-and-hold while still actively managing exits. Only the **combination** of similar numbers + stopped arrows indicates a defect.

**Results:**
- **Total images analyzed:** 143+ (ongoing)
- **Bugs found:** 1 (SPY Alt39 only - isolated incident)
- **Status:** All other verified images show healthy exit activity throughout 2010-2025

**Why This Matters:**
- **Data integrity:** Prevents counting false positives as strategy successes
- **Transparency:** Every result is visually validated, not just trusted
- **Reproducibility:** Anyone can audit the screenshots using the same criteria
- **Research quality:** Only legitimate results inform strategy development decisions

**The Bug Pattern (INVALID results):**
```
❌ Purple arrows STOP partway through chart
❌ Equity curve follows price closely after arrows stop
❌ Suspiciously high returns with no recent exits
❌ Strategy accidentally became buy-and-hold
```

**Healthy Pattern (VALID results):**
```
✅ Purple arrows continue throughout 2010-2025
✅ Equity curve diverges from price (shows strategy activity)
✅ Trade markers present through recent periods
✅ Strategy is actively managing positions
```

**Documentation:**
- [bug-log.txt](bug-log.txt) - Master list of confirmed bugs and verified images
- [data-verification-plan.md](data-verification-plan.md) - Complete validation protocol with visual examples
- Each sector folder contains only validated screenshots

**Ongoing Process:** New screenshots are validated before being included in analysis, ensuring research findings are based on legitimate strategy performance, not coding defects.

---

### 7. Analysis and Documentation

**Process:** As results came in from each validated strategy-security combination, I:

1. **Recorded metrics** in [analysis.csv](analysis.csv):
   - Return %, Profit Factor, Win Rate %, Max Drawdown %
   - Trade count, performance category, options suitability

2. **Documented insights** in [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md):
   - What worked and why
   - What failed and why
   - Sector-specific patterns
   - Strategy suitability by asset type

3. **Used Claude Code for pattern recognition**:
   - Bulk analysis of screenshot results
   - Aggregating performance across strategies
   - Identifying strategy rankings and tier classifications
   - Generating comparison tables and statistical summaries

**Key Insight from This Process:**
> After testing 210+ strategy-security combinations, clear patterns emerged: **Alt10 (Profit Targets)** and **Alt26 (Fractional Pyramid)** both achieved 76% success rates, while utilities failed 100% of all strategies tested. These discoveries only emerged through systematic, comprehensive testing.

---

### Why This Methodology Works

**Reproducibility:** Every step is documented and can be replicated by anyone with:
- TradingView account (free version works)
- AI access for Pine Script generation (ChatGPT, Claude, etc.)
- Windows computer for screenshot workflow
- PowerShell for image processing

**Transparency:** Nothing is hidden:
- All 40+ strategy codes are in [pine-scripts/](pine-scripts/)
- All screenshots are in [sectors/](sectors/) folders
- All analysis is in [analysis.csv](analysis.csv) and [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md)
- Failures documented alongside successes
- **Bug detection:** Defective results openly identified and invalidated ([bug-log.txt](bug-log.txt))

**Systematic Discovery:** Not cherry-picking:
- Every strategy tested on same set of securities
- Standardized backtest settings eliminate variables
- Failed strategies kept for learning (not deleted)
- Honest documentation of what doesn't work
- **Visual validation:** Every screenshot checked for exit bugs before analysis

**Human-AI Synergy:** Leveraging strengths of both:
- **AI:** Generate code variations, build infrastructure, analyze patterns
- **Human:** Visual pattern recognition, hypothesis formation, judgment calls
- **Together:** Systematic testing at scale with qualitative insights

### How You Can Replicate This

1. **Generate strategies:** Ask AI to create Pine Scripts testing specific theories
2. **Setup infrastructure:** Use Claude Code to create folder structure
3. **Test systematically:** Run each strategy on each security, capture screenshots
4. **Manage images:** Use resize_images.ps1 to handle screenshot sizes
5. **Validate screenshots:** Check for exit bugs using [data-verification-plan.md](data-verification-plan.md)
6. **Document findings:** Use templates provided to record insights
7. **Iterate:** Learn from failures, refine theories, generate new strategies

**The beauty of this approach:** It's accessible to anyone. No expensive software, no advanced coding skills, no proprietary data. Just systematic application of free tools and disciplined documentation. **Plus quality assurance:** Visual validation ensures only legitimate results drive strategy decisions.

---

## 📂 Repository Structure

```
trend-following-backtesting-strategies/
├── START_HERE.md                    ← Begin here for sector testing guide
├── README.md                        ← You are here (project overview)
├── pine-scripts/                    ← All 40+ TradingView strategy files
├── sectors/                         ← Sector-by-sector testing results
│   ├── technology/
│   ├── healthcare/
│   ├── energy/
│   └── ... (11 sectors total)
├── resize_images.ps1                ← Utility to manage screenshot sizes
├── bug-log.txt                      ← Bug detection log (quality assurance)
├── data-verification-plan.md        ← Screenshot validation protocol
└── Documentation files:
    ├── DISCOVERIES_AND_LEARNINGS.md    ← Document your findings
    ├── SECTOR_TESTING_WORKFLOW.md      ← Detailed testing methodology
    ├── FINAL_10_STRATEGIES.md          ← Why these 10 for sector testing
    ├── STREAMLINED_TESTING_GUIDE.md    ← Complete testing protocol
    └── ... (additional guides)
```

## 🏆 The Champions

After testing 40 different strategy variations over 3 iterations, three strategies emerged as clear winners:

### 🥇 Alt 31: Fractional + Breakeven Lock (+40.1%)
**THE UNDISPUTED KING**
- **Profit Factor:** 1.474
- **Max Drawdown:** 12.46%
- **Win Rate:** 51.82%
- **Why it dominates:** The perfect combination of intelligent position sizing (fractional pyramiding) and ironclad protection (breakeven locks). This strategy has the smoothest equity curve of all tested strategies.

### 🥈 Alt 38: Triple Combo (+38.9%)
**PHENOMENAL PERFORMANCE**
- **Profit Factor:** 1.466
- **Max Drawdown:** 12.45%
- **Win Rate:** 51.65%
- **The trifecta:** Combines fractional pyramiding, breakeven locks, AND momentum-gated entries. Three proven winners working in harmony.

### 🥉 Alt 34: Fractional + Momentum (+33.8%)
**BRONZE MEDAL**
- **Profit Factor:** 1.396
- **Max Drawdown:** 12.45%
- **Win Rate:** 50.73%
- **Smart additions:** Fractional pyramiding enhanced with RSI-gated position adds for improved trade quality.

---

## 📊 Performance Overview

**Backtest Period:** January 2022 - October 2025 (SPY Daily)
**Initial Capital:** $100,000
**Strategies Tested:** 40 variations across 3 iterations

### Success Rate Evolution
- **Iteration 1 (Alts 1-20):** ~30% profitable
- **Iteration 2 (Alts 21-30):** 70% profitable
- **Iteration 3 (Alts 31-40):** 90% profitable! 🎯

### Performance Journey
| Iteration | Best Strategy | Return | Improvement |
|-----------|--------------|--------|-------------|
| 1 | Alt 10 (Profit Targets) | +20.3% | Baseline |
| 2 | Alt 26 (Fractional Pyramid) | +33.5% | +65% |
| 3 | Alt 31 (Fract + BE Lock) | +40.1% | +97% total |

**Nearly doubled performance over 3 iterations!**

---

## 🎯 Key Discoveries

### The Golden Combo
**Fractional Pyramiding + Breakeven Lock = Maximum Performance**

This combination proved superior to any other two-element pairing. It delivers:
- Best sizing strategy (100% → 75% → 50% → 25%)
- Best protection (move stop to breakeven after 2N profit)
- Lowest drawdown among top performers
- Smoothest equity curve ("almost always up")

### Critical Lessons Learned

#### ✅ What Works
1. **Profit Targets Are Essential** - Multi-stage profit-taking (3N, 6N, 9N) dramatically outperforms all-or-nothing exits
2. **Pyramiding Is Mandatory** - Single-position strategies catastrophically underperform (-21.8%)
3. **Slower Entries Filter Noise** - 55-bar Donchian >> 20-bar breakouts (40% vs -93%)
4. **Exit Optimization > Entry Optimization** - Where you get out matters more than where you get in
5. **Simplicity Beats Complexity** - Two well-chosen elements outperform kitchen-sink approaches
6. **Fractional Sizing Wins** - Descending position sizes (100%→75%→50%→25%) beat equal sizing
7. **Breakeven Locks Work** - Moving stops to breakeven after 2N profit reduces risk without sacrificing returns

#### ❌ What Fails
1. **Fast Breakouts** - 20-bar entries = -93% (death by whipsaws)
2. **No Pyramiding** - Single positions = -21.8% (missed compounding)
3. **Adaptive Entry Levels** - Keltner channels = -58.5% (complexity doesn't help)
4. **Alternative Trailing Methods** - Parabolic SAR = -16.8% (Chandelier superior)
5. **Excessive Filtering** - ADX, dual timeframe, anti-chop filters all reduce performance
6. **Time-Based Exits** - Markets don't care about your calendar = -21.7%
7. **Too Many Features** - "ULTIMATE" strategy with all features only placed 4th

---

## 📁 File Organization

All strategy files are ranked by performance using this naming convention:

```
RANK_PF-X.XXX_strategy-name.pine
```

**Example:**
```
01_PF-1.474_seykota_alt31_fractional_breakeven.pine  👑 KING
02_PF-1.466_seykota_alt38_triple_combo.pine          🥈 RUNNER-UP
03_PF-1.396_seykota_alt34_fractional_momentum.pine   🥉 BRONZE
...
24_PF-0.131_seykota_alt1_fast_breakout.pine          💀 DISASTER
```

### Reading the Filename
- **RANK:** Performance ranking (1 = best)
- **PF-X.XXX:** Profit Factor (>1.0 = profitable, >1.3 = excellent)
- **strategy-name:** Descriptive name of the approach

### Quick Reference Tiers
- **PF > 1.40:** Elite performers (top 2)
- **PF 1.30-1.40:** Excellent strategies (ranks 3-6)
- **PF 1.20-1.30:** Solid performers (ranks 7-14)
- **PF 1.00-1.20:** Profitable but mediocre (ranks 15-19)
- **PF < 1.00:** Net losers (ranks 20-24)

---

## 🔬 Strategy Components

### Core Elements (Present in All Winners)
- **Entry:** 55-bar Donchian breakout (slow and steady)
- **Position Sizing:** 1% risk per unit, 4 units maximum
- **Initial Stop:** 2N (2× Average True Range)
- **Profit Targets:** Multi-stage at 3N, 6N, 9N
- **Trailing Stop:** Chandelier (ATR-based) for remainder

### Enhancement Elements (Top Performers)
1. **Fractional Pyramiding** (Alts 31, 38, 34, 26, 35, 40, 36)
   - Position sizes: 100% → 75% → 50% → 25%
   - Adds every 0.5N in profit

2. **Breakeven Lock** (Alts 31, 38, 21, 36, 37, 40)
   - Move stop to entry after 2N profit
   - Guarantees no loss on mature positions

3. **Momentum Gating** (Alts 38, 34, 30, 36, 32, 40)
   - Only add to positions when RSI confirms strength
   - Improves pyramid quality

4. **Time-Based Tightening** (Alts 35, 37, 32, 25, 40)
   - After 30 bars, tighten trail from 3N to 1.5N
   - Protects aging positions

---

## 💀 Notable Failures

Understanding what doesn't work is as important as knowing what does:

### Worst Performers
1. **Alt 1: Fast Breakout** (-93.2%, PF 0.131)
   - 20-bar entries = constant whipsaws
   - 280 trades with 18.6% win rate
   - Lesson: Speed kills

2. **Alt 23: Keltner Channel** (-58.5%, PF 0.744)
   - Adaptive EMA±ATR entry levels completely failed
   - Complexity doesn't improve signal quality
   - Lesson: Stick to simple Donchian breakouts

3. **Alt 15: Single Position** (-21.8%, PF 0.177)
   - Only 12 trades in 3+ years
   - 8.3% win rate (catastrophic)
   - Lesson: Pyramiding is essential

4. **Turtle Core v2.1** (-20.9%, PF 0.715)
   - 10-bar exit too tight, gave back all gains
   - Good entries, terrible exits
   - Lesson: Exits matter more than entries

---

## 🚀 Getting Started

### For Traders New to This Repository

**Start here if you want to:**

1. **Use These Strategies for Trading** → Read [START_HERE.md](START_HERE.md) then test on YOUR instruments
   - Don't assume Alt 31 works on everything (it doesn't!)
   - Test the 10 representative strategies on your target tickers
   - Follow the 4-phase protocol to find what works for YOU

2. **Learn From the Research** → Read the complete strategy analysis:
   - This README for overview and top performers
   - [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md) for detailed findings
   - Individual .pine files to see implementation details

3. **Replicate the Study** → All strategies and methodology are documented:
   - 40+ TradingView Pine Script files in [pine-scripts/](pine-scripts/)
   - Testing methodology in [SECTOR_TESTING_WORKFLOW.md](SECTOR_TESTING_WORKFLOW.md)
   - Screenshot evidence in [sectors/](sectors/) folder

4. **Contribute Your Findings** → Test additional sectors/instruments:
   - Follow the testing protocol
   - Document your results
   - Share discoveries with the community

### For Live Trading (SPY Only - Validated)
**Recommended strategies for SPY (in order):**
1. **Alt 31** - Best overall performance, smoothest equity curve (PF: 1.474)
2. **Alt 38** - Highest profit factor, slightly more aggressive (PF: 1.466)
3. **Alt 34** - Excellent risk-adjusted returns (PF: 1.396)

All three strategies have:
- Similar low drawdowns (~12.5%)
- Win rates >50%
- Profit factors >1.39
- Proven performance across bull/bear markets (2022-2025)

**⚠️ Important:** These results are specific to SPY. Test thoroughly on other instruments before live trading.

### For Further Development
**Promising areas to explore:**
- Complete sector testing across all market segments
- Identify sector-specific strategy patterns
- Parameter optimization for top strategies per sector
- Walk-forward analysis for robustness testing
- Different timeframes (4-hour, weekly)
- Portfolio approach with sector-appropriate strategies

**Avoid these dead ends (learned the hard way):**
- Fast breakout periods (<40 bars)
- Single-position approaches
- Complex adaptive entry systems
- Alternative trailing stop methods (Parabolic SAR, etc.)
- Excessive filtering (ADX, regime, anti-chop)

---

## 📈 Complete Strategy Rankings

### Top 10 Performers
| Rank | Strategy | Return | PF | Win Rate | Drawdown |
|------|----------|--------|-----|----------|----------|
| 1 | Alt 31: Fract + BE Lock | +40.1% | 1.474 | 51.8% | 12.46% |
| 2 | Alt 38: Triple Combo | +38.9% | 1.466 | 51.7% | 12.45% |
| 3 | Alt 34: Fract + Momentum | +33.8% | 1.396 | 50.7% | 12.45% |
| 4 | Alt 26: Fractional Pyramid | +33.5% | 1.388 | 50.7% | 15.49% |
| 5 | Alt 40: ULTIMATE | +31.3% | 1.348 | 51.9% | 12.47% |
| 6 | Alt 36: BE + Momentum | +28.4% | 1.338 | 50.0% | 15.75% |
| 7 | Alt 21: Breakeven Lock | +28.2% | 1.335 | 49.8% | 15.59% |
| 8 | Alt 35: Fract + Time | +28.1% | 1.306 | 50.5% | 12.49% |
| 9 | Alt 37: BE + Time | +26.4% | 1.301 | 50.2% | 15.67% |
| 10 | Alt 30: Momentum Pyramid | +23.6% | 1.277 | 48.1% | 16.04% |

### Solid Performers (11-20)
All profitable strategies above breakeven, ranging from +5.6% to +24.4%. See [LESSONS_LEARNED.md](LESSONS_LEARNED.md) for complete details.

### Failures (21-24)
Net negative strategies kept for educational purposes. Study these to understand what NOT to do.

---

## 🧪 Sector Testing Methodology

### The Discovery
After extensive testing on SPY, a critical insight emerged: **strategy performance is highly dependent on the underlying asset's characteristics.** What works brilliantly on SPY may fail on individual stocks or sector ETFs.

### The Solution
A systematic sector testing framework to discover which strategies work for which market segments:

1. **10 Representative Strategies Selected** - Chosen to test different hypotheses (not just performance tiers):
   - Baseline (Classic Turtle)
   - Alt 2 (EMA Crossover - different entry)
   - Alt 9 (Time Exit - different exit philosophy)
   - Alt 10 (Profit Targets - early profit taking)
   - Alt 15 (Single Position - no pyramiding)
   - Alt 17 (Dual Timeframe - confluence)
   - Alt 20 (Asymmetric - long/short bias)
   - Alt 22 (Parabolic SAR - adaptive exits)
   - Alt 26 (Fractional Pyramid - smart sizing)
   - Alt 28 (ADX Filter - trend strength)

2. **11 Market Sectors Covered**:
   - ETFs (QQQ, XLE, XLU)
   - Technology, Healthcare, Energy
   - Financials, Industrials, Utilities
   - Consumer Cyclical/Defensive
   - Communication Services, Real Estate, Basic Materials

3. **4-Phase Testing Protocol** (~15 min per ticker):
   - Phase 1: Foundation (Baseline, Alt 15, Alt 26)
   - Phase 2: Entry Filters (Alt 2, Alt 28, Alt 17)
   - Phase 3: Exit Optimizations (Alt 10, Alt 22, Alt 9)
   - Phase 4: Special Cases (Alt 20)

### Expected Outcomes
- Identify universal strategies (work across many tickers)
- Identify sector-specific strategies (niche edges)
- Discover trend-friendly vs difficult sectors
- Build strategy-sector matching decision tree

---

## 🛠️ Repository Utilities

### Image Resize Script
To manage screenshot file sizes efficiently, a PowerShell utility is included:

**[resize_images.ps1](resize_images.ps1)** - Automatically resize screenshots by 35%
- Recursively finds all PNG/JPG images
- Reduces to 65% of original dimensions
- Adds `_reduced` suffix to processed files
- Skips already-reduced images (prevents recursive resizing)
- Deletes original large files
- High-quality bicubic interpolation

**Usage:**
```powershell
.\resize_images.ps1
```

This helps keep the repository size manageable when storing hundreds of backtest screenshots across multiple sectors.

---

## 📚 Documentation

### Getting Started
- **[START_HERE.md](START_HERE.md)** - Quick start guide for sector testing (read this first!)
- **[STREAMLINED_TESTING_GUIDE.md](STREAMLINED_TESTING_GUIDE.md)** - Complete testing methodology
- **[QUICK_REFERENCE_10_STRATEGIES.md](QUICK_REFERENCE_10_STRATEGIES.md)** - Print-friendly strategy reference card

### Strategy Analysis
- **[FINAL_10_STRATEGIES.md](FINAL_10_STRATEGIES.md)** - Why these 10 strategies were selected for sector testing
- **[DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md)** - Document findings as you test

### Sector Testing
- **[SECTOR_TESTING_WORKFLOW.md](SECTOR_TESTING_WORKFLOW.md)** - Detailed sector testing workflow
- **[SECTOR_TICKERS.md](SECTOR_TICKERS.md)** - Recommended tickers for each sector (2-3 per sector)
- **[QUICK_TEST_CHECKLIST.md](QUICK_TEST_CHECKLIST.md)** - Testing checklist

### Original SPY Research
- **Individual .pine files** - TradingView Pine Script implementations (40+ strategies)
- **sectors/etfs/** - Original SPY backtest results and screenshots

---

## 🎓 Philosophy

This project embodies several key principles:

### Ed Seykota's Wisdom
> "The elements of good trading are: (1) cutting losses, (2) cutting losses, and (3) cutting losses."

Our implementation: Initial stops, profit targets, trailing stops, and breakeven locks.

### Lessons from the Market
> "Win or lose, everybody gets what they want out of the market."

Systems focused on profit-taking win. Systems that fear missing out (no profit targets) lose. The market gives you what your system asks for.

### Our Corollary
> "The goal of successful strategy development is to build the best system. Money is secondary. Complexity is secondary."

**Simplicity + Profit Targets + Pyramiding = Winner**

---

## 📊 Market Conditions Tested

The backtest period (2022-2025) includes diverse market conditions:
- **2022:** Severe bear market (-18% SPY)
- **2023-2024:** Recovery and new all-time highs
- **2024-2025:** Continued volatility and uncertainty

Top strategies proved robust across all these environments, demonstrating true trend-following resilience.

---

## 🖼️ Reading Backtest Screenshots

### Critical Warning: Zoom-Level Indicates Exit Frequency

When reviewing backtest screenshots, **the equity curve's X-axis time range is extremely revealing**:

**Full Timeline (1993-2025):**
- Strategy has regular exits throughout the backtest period
- Equity curve shows complete P&L history
- Total P&L (left) matches equity curve endpoint (right)
- ✅ **Suitable for options traders who need frequent exits**

**Zoomed Timeline (e.g., 2010-2012 only):**
- Strategy has **very few exits** - TradingView auto-zooms to where trades occurred
- Equity curve only shows small portion of backtest
- Total P&L (left) includes **unrealized gains from long-held positions**
- Equity curve endpoint (right) shows value at zoom endpoint, NOT final value
- ❌ **NOT suitable for options traders - positions held too long**

**Example:** Alt 6 Pure ATR Stop shows +$282K Total P&L but -$15K equity at chart end. The equity curve is zoomed to 2010-2012 (early losing period) because the strategy holds positions without exiting from 2013-2025. Those unrealized gains inflate the Total P&L but aren't visible on the zoomed chart.

**For Options Traders:** Immediately discard any strategy screenshot with a zoomed equity curve. You need strategies that close positions regularly, which will show full timeline equity curves.

---

## ⚠️ Disclaimer

**This is educational research, not investment advice.**

- Past performance does not guarantee future results
- All backtests are subject to curve-fitting risk
- Walk-forward testing recommended before live trading
- Use appropriate position sizing for your risk tolerance
- Consider paper trading before risking real capital

---

## 🔄 Project Status

**Current Phase:** Multi-Sector Testing & Analysis

**Completed:**
- ✅ 40 strategy variations tested on SPY
- ✅ 3 complete iterations
- ✅ Comprehensive documentation
- ✅ Clear performance rankings
- ✅ Golden Combo identified (Alt 31)
- ✅ Sector testing framework developed
- ✅ Image management utilities created

**Recent Discovery:** Alt 31 works great on SPY but may fail on other tickers. This critical finding led to the development of a systematic sector testing workflow to discover which strategies work for which market segments.

**Current Focus:**
1. Testing 10 representative strategies across all market sectors
2. Identifying sector-specific strategy performance patterns
3. Building strategy-sector matching system
4. Documenting findings for the trading community

**Next Steps:**
1. Complete sector testing (Technology, Healthcare, Energy, Utilities, etc.)
2. Develop sector-optimized strategy variants
3. Create strategy selector based on ticker characteristics
4. Begin paper trading with sector-appropriate strategies
5. Walk-forward analysis for robustness validation

---

## 📞 Contact & Contributions

This is an **open research project** documenting a systematic approach to trend-following strategy development. The methodology and results are shared for educational purposes.

### How Other Traders Can Use This Research

**1. Direct Application:**
- Clone/download the repository
- Test strategies on your instruments using TradingView
- Use the [SECTOR_TESTING_WORKFLOW.md](SECTOR_TESTING_WORKFLOW.md) as your guide
- Document your findings in the appropriate sector folders

**2. Learn From the Process:**
- Study the iteration-by-iteration improvement (from -93% to +40%)
- Understand what works and what fails (and why)
- Apply the systematic testing methodology to your own strategy ideas
- Avoid the documented "dead ends"

**3. Contribute Your Findings:**
If you test these strategies on additional instruments/sectors:
- Document your results using the provided templates
- Share screenshots and performance metrics
- Add insights to [DISCOVERIES_AND_LEARNINGS.md](DISCOVERIES_AND_LEARNINGS.md)
- Help build the community knowledge base

**4. Build Upon This Work:**
- Optimize parameters for specific sectors
- Test on different timeframes
- Develop sector-specific variants
- Create automated strategy selectors
- Share improvements back to the community

### What Makes This Research Valuable

**Transparency:** Every strategy is documented with:
- Complete Pine Script source code
- Backtest screenshots
- Performance metrics
- Analysis of why it works (or fails)

**Systematic Approach:** Not cherry-picked results:
- All 40 strategies tested on same timeframe
- Failures documented alongside successes
- Clear methodology anyone can replicate
- Honest evaluation of what doesn't work

**Actionable Insights:** Beyond just "here's a profitable strategy":
- Understanding of WHY strategies work
- Knowledge of WHEN they fail
- Framework for testing YOUR instruments
- Methodology for continuous improvement

### Key Takeaway

Through systematic testing and learning from failures, strategy performance improved by **97% over 3 iterations** (-93% → +40%), proving that:
- Disciplined experimentation beats guru predictions
- Systematic testing reveals hidden patterns
- Understanding failures is as valuable as celebrating successes
- Strategy performance is asset-dependent (Alt 31 on SPY ≠ Alt 31 on everything)

**The journey from failure to success is the real value, not just the final strategy.**

---

*"The goal of a successful trader is to make the best trades. Money is secondary." - Alexander Elder*

**Last Updated:** November 2, 2025
**Strategies Tested:** 40 (SPY); 10 selected for multi-sector testing
**SPY Success Rate:** 90% (Iteration 3)
**Best SPY Strategy:** Alt 31 (+40.1%, PF 1.474)
**Current Phase:** Multi-sector testing to identify strategy-asset matching patterns
