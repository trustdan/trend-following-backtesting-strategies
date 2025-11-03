Below I’ll do three things:

1. **Identify concrete improvements** to your current “Seykota / Turtle Core v2.1 + Date Range” script while staying true to Ed Seykota’s trend‑following ethos (simple rules, rigorous risk control, volatility normalization, pyramid into strength, cut losses quickly).
2. **Deliver an improved v2.2** of your existing approach (drop‑in replacement) with small, principled tweaks—not a re‑design.
3. **Provide four alternative, self‑contained strategies** you can paste into TradingView and backtest side‑by‑side. Each embraces a slightly different theoretical assumption about trend following (breakouts vs. MAs, timeframe aggregation, ATR channels), but all remain “Seykota‑clean”: simple, robust, and focused on price and risk.

------

## 1) Improvements to your current script (what to refine & why)

Your v2.1 is already strong and very “Seykota”: Donchian breakout, ATR‑based position sizing (“N”), add‑ons every fraction of N, protective/Donchian exits, optional regime filter, and a clean backtest date window. Great foundation.

Here are targeted refinements that maintain the same philosophy:

- **Use intrabar extremes for adds (optional):**
   You currently require `close >= lastAdd + addStepN * N_entry` to add. That’s conservative, but can miss legitimate add‑levels hit intrabar and then faded by the close. Provide a switch to use `high`/`low` (breakout‑authentic, classic Turtle/Seykota behavior) versus `close` (your current default). This keeps the idea but lets you test the trade‑off between “capture strength early” vs. “avoid intrabar noise.”
- **Add explicit slippage modeling (ticks):**
   You already model commission. Add a `slippage` input (in ticks) to `strategy()`—this matters a lot for breakout systems because many entries are stop‑like.
- **Protect adds against blow‑off volatility spikes (optional):**
   Permit an input to block add‑ons when current ATR > ATR’s own moving average (e.g., `ATR > SMA(ATR, n)`), which avoids pyramiding right as volatility explodes (often near late‑trend “whoosh” phases). Still 100% price/volatility‑based; no over‑fitting.
- **Harden stops with tick rounding:**
   Use `math.round_to_mintick(stop)` so stop orders land on valid ticks. (Protects you from broker rejection differences between symbols.)
- **Higher‑timeframe Donchian option:**
   Add a toggle to compute Donchian on a higher timeframe (e.g., Weekly), executed on the chart timeframe. It’s the *same* rule, just less noise—very Seykota.
- **Regime filter choice:**
   Keep your SPY/MA filter, but offer MA type choice (SMA/EMA/WMA) and timeframe (D/W). The *principle* (only trade with the major tide) remains; you can test which “tide” definition behaves best on your market.
- **Time‑exit clarity:**
   Your “Roll” mode is nice. Add a “barsSinceEntry” plot label and record when/why a time exit occurred. This helps interpret outcomes without changing rules.
- **Safer date‑window flat:**
   When you force‑flat at the `fromDate`, also reset working vars so the first trade after the window starts doesn’t inherit stale add anchors: `units := 0`, `lastAddLong/Short := na`, `N_entry := na`.

All of these preserve the trend‑following core while making execution and testing sturdier.

------

## 2) Improved drop‑in: **Seykota / Turtle Core v2.2 (small, principled tweaks)**

Copy–paste as a new script. It’s your v2.1 with:

- optional intrabar add‑triggers,
- slippage input,
- ATR blow‑off guard for add‑ons,
- tick‑rounded stops,
- safer variable resets at the backtest start.

```pine
//@version=6
strategy("Seykota / Turtle Core v2.2 (clean tweaks)",
     overlay=true,
     initial_capital=100000,
     commission_type=strategy.commission.percent, commission_value=0.005,
     slippage = input.int(0, "Slippage (ticks)", minval=0),   // NEW
     default_qty_type=strategy.fixed, default_qty_value=0,
     pyramiding=10,
     max_bars_back=5000)

//================ Inputs
allowLong   = input.bool(true,  "Allow LONGs?")
allowShort  = input.bool(true,  "Allow SHORTs?")

entryLen    = input.int(55,     "Donchian ENTRY lookback", minval=10)
exitLen     = input.int(10,     "Donchian EXIT lookback",  minval=5)
nLen        = input.int(20,     "N = ATR length",          minval=5)
stopN       = input.float(2.0,  "Initial stop (in N)",     minval=0.25, step=0.25)
addStepN    = input.float(0.5,  "Add every X * N",         minval=0.25, step=0.25)
maxUnits    = input.int(4,      "Max units (incl. initial)", minval=1, maxval=10)
riskPct     = input.float(1.0,  "Risk % of equity PER UNIT", minval=0.1, maxval=5, step=0.1)

useMarket   = input.bool(false, "Use market regime filter?")
marketSym   = input.symbol("SPY", "Market symbol for regime (if used)")
marketTF    = input.timeframe("D", "Regime timeframe (if used)")
marketLen   = input.int(200,    "Market MA length (if used)", minval=50)
marketMA    = input.string("SMA", "Regime MA type", options=["SMA","EMA","WMA"])

timeExitMode= input.string("None","Time exit", options=["None","Close","Roll"])
timeExitBars= input.int(60,     "Time exit bars (if used)", minval=5)

minVol      = input.int(0,      "Min 20-bar avg volume (chart TF)", minval=0)
useIntrabarAdds = input.bool(false, "Add-ons use intrabar extremes (High/Low)?") // NEW
useATRGuard = input.bool(false, "Block add-ons when ATR > SMA(ATR, nLen)?")      // NEW

showSignals = input.bool(true,  "Plot signals & stops?")
plotDon     = input.bool(true,  "Plot Donchian bands?")

// === Date-range filter (local chart timezone)
fromDate = input.time(defval=timestamp("2022-01-01T00:00:00"), title="Backtest FROM (yyyy-mm-dd)", confirm=true)
toDate   = input.time(defval=timestamp("2099-12-31T23:59:59"), title="Backtest TO (yyyy-mm-dd)",   confirm=true)
flatAtFrom = input.bool(true, "Force FLAT at range start?")
isRangeStart = (time[1] < fromDate) and (time >= fromDate)
if flatAtFrom and isRangeStart and strategy.position_size != 0
    strategy.close_all(comment="Flat at FROM")

// Reset working state at range start (NEW safety)
var float N_entry       = na
var float lastAddLong   = na
var float lastAddShort  = na
var int   units         = 0
var int   barsInPos     = 0
if isRangeStart
    N_entry       := na
    lastAddLong   := na
    lastAddShort  := na
    units         := 0
    barsInPos     := 0

//================ Core calcs (chart timeframe)
N        = ta.atr(nLen)
volMA    = ta.sma(volume, 20)
liqOK    = volMA >= minVol

// Donchian levels
donHi    = ta.highest(high, entryLen)
donLo    = ta.lowest(low,  entryLen)
donHiPrev= donHi[1]
donLoPrev= donLo[1]

exitHiPrev = ta.highest(high, exitLen)[1]
exitLoPrev = ta.lowest(low,  exitLen)[1]

// Market regime (optional)
mClose = request.security(marketSym, marketTF, close)
maFunc(src,len) =>
    marketMA == "EMA" ? ta.ema(src,len) : marketMA == "WMA" ? ta.wma(src,len) : ta.sma(src,len)
mMA    = request.security(marketSym, marketTF, maFunc(close, marketLen))
longRegOK  = not useMarket or (mClose > mMA)
shortRegOK = not useMarket or (mClose < mMA)

//================ Signals (no lookahead)
longBreak  = allowLong  and liqOK and longRegOK  and (close > donHiPrev)
shortBreak = allowShort and liqOK and shortRegOK and (close < donLoPrev)

//================ Position state
inPos     = strategy.position_size != 0
inLong    = strategy.position_size > 0
inShort   = strategy.position_size < 0
barsInPos := inPos ? (barsInPos + 1) : 0

//================ Helpers
sharesForUnit(_equity, _Nentry) =>
    riskDollars   = _equity * (riskPct/100.0)
    perShareRisk  = math.max(stopN * _Nentry, syminfo.mintick)
    math.max(1, math.floor(riskDollars / perShareRisk))

//================ Entries
if (time >= fromDate) and (time <= toDate) and not inPos and longBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units       := 1
    lastAddLong := close

if (time >= fromDate) and (time <= toDate) and not inPos and shortBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units        := 1
    lastAddShort := close

//================ Add-on logic (every addStepN * N_entry)
priceForLongAdd  = useIntrabarAdds ? high : close
priceForShortAdd = useIntrabarAdds ? low  : close
atrGuardOK       = not useATRGuard or (N <= ta.sma(N, nLen))

canAddLong  = (time >= fromDate) and (time <= toDate) and inLong  and atrGuardOK and units < maxUnits and priceForLongAdd  >= nz(lastAddLong)  + addStepN * N_entry
canAddShort = (time >= fromDate) and (time <= toDate) and inShort and atrGuardOK and units < maxUnits and priceForShortAdd <= nz(lastAddShort) - addStepN * N_entry

if canAddLong
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units       += 1
    lastAddLong := close

if canAddShort
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units        += 1
    lastAddShort := close

//================ Protective & Donchian exits — attach only inside range (tick-rounded)
var float stopL = na
var float stopS = na

if (time >= fromDate) and (time <= toDate) and inLong
    initStopL = strategy.position_avg_price - stopN * N_entry
    stopLraw  = math.max(initStopL, exitLoPrev)
    stopL     := math.round_to_mintick(stopLraw)
    strategy.exit("L-EXIT", from_entry="L", stop=stopL)
else
    stopL := na

if (time >= fromDate) and (time <= toDate) and inShort
    initStopS = strategy.position_avg_price + stopN * N_entry
    stopSraw  = math.min(initStopS, exitHiPrev)
    stopS     := math.round_to_mintick(stopSraw)
    strategy.exit("S-EXIT", from_entry="S", stop=stopS)
else
    stopS := na

//================ Optional time exit
timeExitTrig = (time >= fromDate) and (time <= toDate) and inPos and (timeExitMode != "None") and (barsInPos >= timeExitBars)
if timeExitTrig
    if inLong
        if timeExitMode == "Close"
            strategy.close("L", comment="Time Exit")
            units := 0
        else if timeExitMode == "Roll"
            strategy.close("L", comment="Time Exit (Roll)")  // re‑entry logic can be added if desired
            units := 0
    if inShort
        if timeExitMode == "Close"
            strategy.close("S", comment="Time Exit")
            units := 0
        else if timeExitMode == "Roll"
            strategy.close("S", comment="Time Exit (Roll)")
            units := 0

//================ Plots
float dHiPlot = plotDon ? donHi : na
float dLoPlot = plotDon ? donLo : na
plot(dHiPlot, "Donchian High", color=color.new(color.blue, 40))
plot(dLoPlot, "Donchian Low",  color=color.new(color.blue, 40))

plot(showSignals and inLong  ? stopL : na, "Long Stop",  color=color.new(color.red,  0), style=plot.style_linebr)
plot(showSignals and inShort ? stopS : na, "Short Stop", color=color.new(color.red,  0), style=plot.style_linebr)
```

------

## 3) Four alternative strategies to backtest

Each is a compact, focused translation of a classic trend‑following assumption.

### A) **Dual Moving Average + ATR “Chandelier” Trail (Seykota‑simple)**

*Assumption:* price trends persist when a fast MA overtakes a slow MA; ride with an ATR trail; size by N; pyramid into strength.

```pine
//@version=6
strategy("Seykota: MA Crossover + ATR Trail",
     overlay=true,
     initial_capital=100000,
     commission_type=strategy.commission.percent, commission_value=0.005,
     slippage=input.int(0, "Slippage (ticks)", minval=0),
     default_qty_type=strategy.fixed, pyramiding=10, max_bars_back=5000)

allowLong  = input.bool(true,  "Allow LONGs?")
allowShort = input.bool(true,  "Allow SHORTs?")
fastLen    = input.int(50,     "Fast MA", minval=2)
slowLen    = input.int(200,    "Slow MA", minval=5)
trailLen   = input.int(22,     "Trail lookback", minval=5)
nLen       = input.int(20,     "ATR length", minval=5)
stopN      = input.float(2.5,  "Initial stop (in N)", minval=0.25, step=0.25)
trailN     = input.float(3.0,  "Chandelier trail (in N)", minval=0.25, step=0.25)
addStepN   = input.float(0.5,  "Add every X * N", minval=0.25, step=0.25)
maxUnits   = input.int(4,      "Max units", minval=1, maxval=10)
riskPct    = input.float(1.0,  "Risk % of equity PER UNIT", minval=0.1, maxval=5, step=0.1)

fromDate = input.time(timestamp("2022-01-01T00:00:00"), "Backtest FROM", confirm=true)
toDate   = input.time(timestamp("2099-12-31T23:59:59"), "Backtest TO",   confirm=true)
inRange  = (time >= fromDate) and (time <= toDate)

fast = ta.sma(close, fastLen)
slow = ta.sma(close, slowLen)
N    = ta.atr(nLen)

longSig  = allowLong  and ta.crossover(fast, slow)
shortSig = allowShort and ta.crossunder(fast, slow)

var float N_entry=na, lastAddL=na, lastAddS=na
var int units=0

sharesForUnit(eq, N_) =>
    riskDollars = eq*(riskPct/100)
    perShareRisk = math.max(stopN*N_, syminfo.mintick)
    math.max(1, math.floor(riskDollars/perShareRisk))

if inRange and strategy.position_size == 0 and longSig
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units := 1
    lastAddL := close
if inRange and strategy.position_size == 0 and shortSig
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units := 1
    lastAddS := close

inLong  = strategy.position_size > 0
inShort = strategy.position_size < 0

trailL = ta.highest(high, trailLen) - trailN*N_entry
trailS = ta.lowest(low,  trailLen) + trailN*N_entry

if inRange and inLong
    initStopL = strategy.position_avg_price - stopN*N_entry
    stopL     = math.round_to_mintick(math.max(initStopL, trailL))
    strategy.exit("L-EXIT", from_entry="L", stop=stopL)
if inRange and inShort
    initStopS = strategy.position_avg_price + stopN*N_entry
    stopS     = math.round_to_mintick(math.min(initStopS, trailS))
    strategy.exit("S-EXIT", from_entry="S", stop=stopS)

// Pyramiding into strength
if inRange and inLong and units < maxUnits and high >= nz(lastAddL) + addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units += 1
    lastAddL := close
if inRange and inShort and units < maxUnits and low <= nz(lastAddS) - addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units += 1
    lastAddS := close

plot(fast, "Fast MA")
plot(slow, "Slow MA")
```

------

### B) **Weekly Donchian Breakout, Daily Execution**

*Assumption:* catch *major* trends by anchoring the breakout logic on a higher timeframe (weekly), executed on your chart timeframe. Same ATR risk and pyramiding.

```pine
//@version=6
strategy("Seykota: Weekly Donchian (daily execution)",
     overlay=true,
     initial_capital=100000,
     commission_type=strategy.commission.percent, commission_value=0.005,
     slippage=input.int(0, "Slippage (ticks)", minval=0),
     default_qty_type=strategy.fixed, pyramiding=10, max_bars_back=5000)

allowLong  = input.bool(true,  "Allow LONGs?")
allowShort = input.bool(true,  "Allow SHORTs?")
wEntryLen  = input.int(26,     "Weekly ENTRY lookback (weeks)", minval=8)
wExitLen   = input.int(13,     "Weekly EXIT lookback (weeks)",  minval=5)
nLen       = input.int(20,     "ATR length (chart TF)", minval=5)
stopN      = input.float(2.0,  "Initial stop (in N)", minval=0.25, step=0.25)
addStepN   = input.float(0.5,  "Add every X * N", minval=0.25, step=0.25)
maxUnits   = input.int(4,      "Max units", minval=1, maxval=10)
riskPct    = input.float(1.0,  "Risk % of equity PER UNIT", minval=0.1, maxval=5, step=0.1)

fromDate = input.time(timestamp("2022-01-01T00:00:00"), "Backtest FROM", confirm=true)
toDate   = input.time(timestamp("2099-12-31T23:59:59"), "Backtest TO",   confirm=true)
inRange  = (time >= fromDate) and (time <= toDate)

N = ta.atr(nLen)

// Weekly Donchian on higher TF; no lookahead
wHiPrev = request.security(syminfo.tickerid, "W", ta.highest(high, wEntryLen))[1]
wLoPrev = request.security(syminfo.tickerid, "W", ta.lowest(low,  wEntryLen))[1]
wExitHiPrev = request.security(syminfo.tickerid, "W", ta.highest(high, wExitLen))[1]
wExitLoPrev = request.security(syminfo.tickerid, "W", ta.lowest(low,  wExitLen))[1]

longBreak  = allowLong  and inRange and (close > wHiPrev)
shortBreak = allowShort and inRange and (close < wLoPrev)

var float N_entry=na, lastAddL=na, lastAddS=na
var int units=0

sharesForUnit(eq, N_) =>
    riskDollars = eq*(riskPct/100)
    perShareRisk = math.max(stopN*N_, syminfo.mintick)
    math.max(1, math.floor(riskDollars/perShareRisk))

if strategy.position_size == 0 and longBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units := 1
    lastAddL := close
if strategy.position_size == 0 and shortBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units := 1
    lastAddS := close

inLong  = strategy.position_size > 0
inShort = strategy.position_size < 0

if inRange and inLong
    exitL = math.round_to_mintick(math.max(strategy.position_avg_price - stopN*N_entry, wExitLoPrev))
    strategy.exit("L-EXIT", from_entry="L", stop=exitL)
if inRange and inShort
    exitS = math.round_to_mintick(math.min(strategy.position_avg_price + stopN*N_entry, wExitHiPrev))
    strategy.exit("S-EXIT", from_entry="S", stop=exitS)

if inRange and inLong and units < maxUnits and high >= nz(lastAddL) + addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units += 1
    lastAddL := close
if inRange and inShort and units < maxUnits and low <= nz(lastAddS) - addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units += 1
    lastAddS := close
```

------

### C) **ATR Channel Breakout (percent‑of‑volatility bands)**

*Assumption:* rather than “highest high N days ago,” define the breakout as price exceeding a volatility band above a base (SMA). This is still pure price+volatility; fewer parameters, different mechanism.

```pine
//@version=6
strategy("Seykota: ATR Channel Breakout",
     overlay=true,
     initial_capital=100000,
     commission_type=strategy.commission.percent, commission_value=0.005,
     slippage=input.int(0, "Slippage (ticks)", minval=0),
     default_qty_type=strategy.fixed, pyramiding=10, max_bars_back=5000)

allowLong  = input.bool(true,  "Allow LONGs?")
allowShort = input.bool(true,  "Allow SHORTs?")
baseLen    = input.int(100,    "Base MA length", minval=10)
nLen       = input.int(20,     "ATR length",     minval=5)
kEntry     = input.float(2.0,  "Entry band (k * ATR)", minval=0.25, step=0.25)
kExit      = input.float(2.0,  "Exit band (k * ATR)",  minval=0.25, step=0.25)
stopN      = input.float(2.0,  "Initial stop (in N)",  minval=0.25, step=0.25)
addStepN   = input.float(0.5,  "Add every X * N",      minval=0.25, step=0.25)
maxUnits   = input.int(4,      "Max units",            minval=1, maxval=10)
riskPct    = input.float(1.0,  "Risk % of equity PER UNIT", minval=0.1, maxval=5, step=0.1)

fromDate = input.time(timestamp("2022-01-01T00:00:00"), "Backtest FROM", confirm=true)
toDate   = input.time(timestamp("2099-12-31T23:59:59"), "Backtest TO",   confirm=true)
inRange  = (time >= fromDate) and (time <= toDate)

base = ta.sma(close, baseLen)
N    = ta.atr(nLen)

upBand   = base + kEntry*N
downBand = base - kEntry*N
exitUp   = base + kExit*N
exitDn   = base - kExit*N

longBreak  = allowLong  and inRange and (close > upBand[1])   // no lookahead
shortBreak = allowShort and inRange and (close < downBand[1])

var float N_entry=na, lastAddL=na, lastAddS=na
var int units=0

sharesForUnit(eq, N_) =>
    riskDollars = eq*(riskPct/100)
    perShareRisk = math.max(stopN*N_, syminfo.mintick)
    math.max(1, math.floor(riskDollars/perShareRisk))

if strategy.position_size == 0 and longBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units := 1
    lastAddL := close
if strategy.position_size == 0 and shortBreak
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units := 1
    lastAddS := close

inLong  = strategy.position_size > 0
inShort = strategy.position_size < 0

// Exits: cross back through kExit bands
if inRange and inLong
    exitL = math.round_to_mintick(math.max(strategy.position_avg_price - stopN*N_entry, exitDn[1]))
    strategy.exit("L-EXIT", from_entry="L", stop=exitL)
if inRange and inShort
    exitS = math.round_to_mintick(math.min(strategy.position_avg_price + stopN*N_entry, exitUp[1]))
    strategy.exit("S-EXIT", from_entry="S", stop=exitS)

if inRange and inLong and units < maxUnits and high >= nz(lastAddL) + addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh); units += 1; lastAddL := close
if inRange and inShort and units < maxUnits and low <= nz(lastAddS) - addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh); units += 1; lastAddS := close

plot(base, "Base MA")
plot(upBand,   "Up Band")
plot(downBand, "Down Band")
```

------

### D) **Donchian (20/10) with “first breakout close only” + optional MA tide**

*Assumption:* classic faster channel (20/10)—very Turtle/Seykota—but make the *entry* require a close through the band (strict end‑of‑bar confirm). Optional “tide” via a slow MA to stay with the big wave.

```pine
//@version=6
strategy("Seykota: 20/10 Donchian, close-confirmed",
     overlay=true,
     initial_capital=100000,
     commission_type=strategy.commission.percent, commission_value=0.005,
     slippage=input.int(0, "Slippage (ticks)", minval=0),
     default_qty_type=strategy.fixed, pyramiding=10, max_bars_back=5000)

allowLong  = input.bool(true,  "Allow LONGs?")
allowShort = input.bool(true,  "Allow SHORTs?")
entryLen   = input.int(20,     "ENTRY lookback", minval=10)
exitLen    = input.int(10,     "EXIT lookback",  minval=5)
nLen       = input.int(20,     "ATR length",     minval=5)
stopN      = input.float(2.0,  "Initial stop (in N)", minval=0.25, step=0.25)
addStepN   = input.float(0.5,  "Add every X * N", minval=0.25, step=0.25)
maxUnits   = input.int(4,      "Max units", minval=1, maxval=10)
riskPct    = input.float(1.0,  "Risk % of equity PER UNIT", minval=0.1, maxval=5, step=0.1)

useTide    = input.bool(false, "Use slow MA tide?")
tideLen    = input.int(200,    "Tide MA length", minval=50)

fromDate = input.time(timestamp("2022-01-01T00:00:00"), "Backtest FROM", confirm=true)
toDate   = input.time(timestamp("2099-12-31T23:59:59"), "Backtest TO",   confirm=true)
inRange  = (time >= fromDate) and (time <= toDate)

N = ta.atr(nLen)
donHiPrev = ta.highest(high, entryLen)[1]
donLoPrev = ta.lowest(low,  entryLen)[1]
exitHiPrev = ta.highest(high, exitLen)[1]
exitLoPrev = ta.lowest(low,  exitLen)[1]
tide = ta.sma(close, tideLen)

goLong  = allowLong  and (close > donHiPrev) and (not useTide or close > tide)
goShort = allowShort and (close < donLoPrev) and (not useTide or close < tide)

var float N_entry=na, lastAddL=na, lastAddS=na
var int units=0

sharesForUnit(eq, N_) =>
    riskDollars = eq*(riskPct/100)
    perShareRisk = math.max(stopN*N_, syminfo.mintick)
    math.max(1, math.floor(riskDollars/perShareRisk))

if inRange and strategy.position_size == 0 and goLong
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units := 1
    lastAddL := close
if inRange and strategy.position_size == 0 and goShort
    N_entry := N
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units := 1
    lastAddS := close

inLong  = strategy.position_size > 0
inShort = strategy.position_size < 0

if inRange and inLong
    exitL = math.round_to_mintick(math.max(strategy.position_avg_price - stopN*N_entry, exitLoPrev))
    strategy.exit("L-EXIT", from_entry="L", stop=exitL)
if inRange and inShort
    exitS = math.round_to_mintick(math.min(strategy.position_avg_price + stopN*N_entry, exitHiPrev))
    strategy.exit("S-EXIT", from_entry="S", stop=exitS)

if inRange and inLong and units < maxUnits and high >= nz(lastAddL) + addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("L", strategy.long, qty=sh)
    units += 1
    lastAddL := close
if inRange and inShort and units < maxUnits and low <= nz(lastAddS) - addStepN*N_entry
    sh = sharesForUnit(strategy.equity, N_entry)
    strategy.entry("S", strategy.short, qty=sh)
    units += 1
    lastAddS := close

plot(donHiPrev, "Donchian High (prev)", color=color.new(color.blue, 40))
plot(donLoPrev, "Donchian Low  (prev)", color=color.new(color.blue, 40))
plot(useTide ? tide : na, "Tide MA", color=color.new(color.orange, 0))
```

------

## How to compare these quickly

- Keep **riskPct**, **stopN**, **addStepN**, **maxUnits** consistent across scripts first. That isolates the *entry/exit concept*.
- Then test toggles (intrabar adds vs. close, ATR guard, regime filters).
- Use the same **date window** and **commission/slippage** assumptions.

If you want, I can also consolidate these strategies into a **single multi‑mode script** with a dropdown (“Donchian”, “MA Xover”, “ATR Channel”, “Weekly Donchian”) so you can flip systems without changing charts—while keeping each system’s parameters namespaced to avoid cross‑contamination.

Would you like that combined “multi‑mode” harness next, or prefer keeping them as separate scripts?