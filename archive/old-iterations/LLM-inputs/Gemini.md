This is an excellent implementation of a Turtle-style (System 2) trend-following strategy, which shares its core DNA with Ed Seykota's principles. The script is robust, with clear risk management (N-based stops and sizing) 111111and pyramiding rules222.



To "improve" it while staying true to Seykota's philosophy—which prizes **simplicity, robust risk management, and letting price lead**—we shouldn't add complex indicators or optimization. Instead, we should test different *theoretical assumptions* about how a trend system should behave.

Here are several alternatives you can backtest, each based on a different core theory.

------



### 1. Alternative: The "Classic Seykota" (EMA Crossover)



This tests the theory that a **smoother, weighted average of price is a more robust trend signal** than a simple high/low "breakout," which can be prone to single-bar "noise." Seykota himself is famously associated with exponential moving average (EMA) crossover systems.

- **Theoretical Assumption:** A trend is defined by the relationship between a fast-moving average and a slow-moving average, not by an absolute N-bar high or low.

- **How to Implement:**

  - 

    **Disable Donchian:** You would remove the `donHiPrev` 3 and `donLoPrev` logic from your entry signals.

    

    

  - **Add EMAs:**

    Pine Script

    ```
    fastLen = input.int(50, "Fast EMA")
    slowLen = input.int(200, "Slow EMA")
    emaFast = ta.ema(close, fastLen)
    emaSlow = ta.ema(close, slowLen)
    ```

  - **Change Entry Signals:**

    Pine Script

    ```
    // Original: longBreak  = ... (close > donHiPrev) [cite: 14]
    longBreak  = allowLong  and liqOK and longRegOK  and ta.crossover(emaFast, emaSlow)
    
    // Original: shortBreak = ... (close < donLoPrev) [cite: 14]
    shortBreak = allowShort and liqOK and shortRegOK and ta.crossunder(emaFast, emaSlow)
    ```

  - **Change Exit Logic:** This is key. A simple crossover system often exits on the *reverse* cross. You would replace the Donchian 10-bar exit 4and the `stopN` logic555.

    

    

    

    

    Pine Script

    ```
    // In this system, you might not use N-based stops at all, or only for initial risk.
    // The primary exit *is* the reverse signal.
    if inLong and ta.crossunder(emaFast, emaSlow)
        strategy.close("L", comment="EMA Exit")
    
    if inShort and ta.crossover(emaFast, emaSlow)
        strategy.close("S", comment="EMA Exit")
    ```

  - 

    **Keep:** You would **keep the `sharesForUnit` risk-sizing logic** 6 for the initial entry, but you would need to adapt the N-stop or remove it. You would also likely disable pyramiding7, as this is typically a "one-in, one-out" system.

    

    

    

------



### 2. Alternative: The "Turtle System 1" (S1)



This tests the theory that a **shorter-term breakout system (S1) is a valid, albeit more active, trend-following signal**. The original Turtles famously traded *two* systems (S1 and S2) for diversification. Your current script is a pure S2 (55-bar entry)8.



- **Theoretical Assumption:** A shorter-term (e.g., 20-bar) breakout is a valid trend, and catching it early (despite more whipsaws) is beneficial.

- **How to Implement:**

  - **Change Lookbacks:** This is the simplest test. You are testing S1 *instead of* S2.

    Pine Script

    ```
    entryLen    = input.int(20,     "Donchian ENTRY lookback (System-1)", minval=10) // Was 55
    exitLen     = input.int(10,     "Donchian EXIT lookback",              minval=5) // Stays 10
    ```

  - **Add Turtle S1 "Filter":** A key rule of S1 was that if the *last* S1 trade was a winner, you *skip* the current signal to avoid "whipsaw" re-entries. This is more complex but is the true "S1" logic. Your script doesn't track this, so a simple lookback change is the first step.

------



### 3. Alternative: The "Tapered Pyramid"



This tests the theory that **risk should be \*reduced\* as a trend gets more mature and extended**. Your current script adds up to 4 units 999, and each new unit risks 1% of the *current* equity1010101010. This means your 4th unit, added late in a trend, is risking the *same dollar amount* as your 1st unit.



- **Theoretical Assumption:** Adding new, full-sized units late in a trend increases the risk of a sharp reversal wiping out open profits. It's better to add *smaller* amounts as the trend extends.

- **How to Implement:**

  - 

    **Modify Add-on Sizing:** Change the `sharesForUnit` 11 call for *add-on* trades.

    

    

  - **Create a Dynamic Risk Pct:**

    Pine Script

    ```
    // Define a tapering factor. E.g., 0.5 = each new unit is half the risk % of the last.
    // Or simpler, just use riskPct / units
    
    // Inside 'if canAddLong'
    if canAddLong
        // Original: float sh = sharesForUnit(strategy.equity, N_entry) 
        float dynamicRiskPct = riskPct / (units + 1) // e.g., 1% -> 0.5% -> 0.33%
        float sh = sharesForUnit(strategy.equity * dynamicRiskPct / riskPct, N_entry) // Adjusts equity
    
        strategy.entry("L", strategy.long, qty=sh)
        units       += 1
        lastAddLong := close
    
    // Do the same for 'if canAddShort'
    if canAddShort
        // float dynamicRiskPct = riskPct / (units + 1)
        // ... (etc)
    ```

  - **Note:** This is a conceptual change. The `sharesForUnit` function 12 itself takes `_equity` as an argument. A simpler way is to adjust the `riskDollars` calculation inside that function *if* `units > 0`13.

    

    

    

------



### 4. Alternative: The "Pure Volatility Stop" (No Donchian Exit)



This tests the theory that **a volatility-based stop (N \* ATR) is superior to a price-based stop (10-bar low)**. Your script *combines* them, taking whichever is tighter (`math.max` for longs, `math.min` for shorts)14. This test would *isolate* the N-stop.



- 

  **Theoretical Assumption:** The 10-bar Donchian exit 15 is arbitrary and can prematurely exit a trend that is just having a shallow, low-volatility pullback. A pure ATR-based stop respects the *character* of the volatility.

  

  

- **How to Implement:**

  - **Modify Stop Logic:**

    Pine Script

    ```
    if inRange and inLong
        initStopL = strategy.position_avg_price - stopN * N_entry
        // Original: stopL := math.max(initStopL, exitLoPrev) 
        stopL     := initStopL // <--- CHANGE
        strategy.exit("L-EXIT", from_entry="L", stop=stopL)
    else
        stopL := na
    
    if inRange and inShort
        initStopS = strategy.position_avg_price + stopN * N_entry
        // Original: stopS := math.min(initStopS, exitHiPrev) [cite: 12]
        stopS     := initStopS // <--- CHANGE
        strategy.exit("S-EXIT", from_entry="S", stop=stopS)
    else
        stopS := na
    ```

- **Note:** This is a *fixed* stop from the average entry price. A common *alternative* to this is a **trailing ATR stop**, which would trail from the *highest high (for longs)* since the entry, which is another valid Seykota-style test.



### 💡 Your Backtesting Plan



I would suggest creating 4 copies of this script and making one of these theoretical changes in each.

1. **Control:** Your current script (S2 Entry, Hybrid Exit, Full Pyramid).
2. **Test 1:** Classic EMA (Test 1 above).
3. **Test 2:** S1 Entry (Test 2 above).
4. **Test 3:** Tapered Pyramid (Test 3 above).
5. **Test 4:** Pure N-Stop (Test 4 above).

By comparing the equity curves, drawdowns, and trade statistics of these 5 versions across various markets, you'll learn a great deal about which *assumptions* hold true.

Would you like me to help you write the Pine Script code for one of these alternatives, for example, the "Classic Seykota" EMA Crossover?