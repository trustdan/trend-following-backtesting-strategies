Based on the incredibly detailed backtest analysis you've provided, I can see the issue immediately.

This is a classic case of **confusing a \*screener\* with an \*entry trigger\*.**

Your "too-specific-finviz-screeners.md" file describes a perfect, "point-in-time" *entry setup* (a trigger), which is a transient state. For example, your "Healthcare Momentum Beast" requires a stock to be in a perfect uptrend (`SMA20 > SMA50 > SMA200`) while *simultaneously* being in a pullback or consolidation (`RSI 40-70`).

In a strong market, your best stocks will have an RSI *above* 70 and be filtered out. In a choppy market, their SMA structure will be broken, and they'll also be filtered out. You are looking for a needle in a haystack, which is why you're getting zero results.

A *screener's* job is to build a high-quality **universe** (a watch list) of stocks that meet your core criteria. You then use your Pine Scripts (Alt43, Alt15, etc.) in TradingView to find the *trigger* on that watch list.

Let's modify your approach. We will create "Universe" screeners that find the *right kind of stocks* and then "Situational" screeners to find stocks in specific *setups* (like a pullback).

------



### 1. The "Universe" Screeners (Your Primary Watch List)



The goal here is to find all stocks that meet your core fundamental and long-term trend criteria. We will remove the highly restrictive *timing* filters (RSI, SMA crossovers).



#### 🩺 Healthcare "Universe" (Based on your 'Beast')



This finds all high-quality healthcare stocks in a confirmed long-term uptrend. This is the "lake" you will fish in for your Alt43/Alt46 signals.

- **Sector:** Healthcare
- **Market Cap:** +Mid (over $2B)
- **Average Volume:** Over 500K
- **Price:** Over $50
- **EPS growth this year:** Positive
- **Sales growth past 5 years:** Positive
- **Return on Equity:** Positive
- **Price:** **Above SMA200** (This is the *only* technical filter we need to confirm the long-term uptrend)

**Why this works:** This list will show you *all* trending healthcare stocks (like your backtest-proven UNH, LLY, etc.), even if their RSI is currently 80 (strong) or 35 (pulling back). You can then run your Pine Scripts on this list to find the *actual* entry.



#### 💻 Tech "Universe" (Based on your 'Crusher')



This finds all high-quality, large-cap tech stocks in a confirmed long-term uptrend. This is your watch list for Alt15/Alt22/Alt47.

- **Sector:** Technology
- **Market Cap:** +Large (over $10B)
- **Average Volume:** Over 1M
- **Price:** Over $100
- **EPS growth this year:** Positive
- **EPS growth next year:** Positive
- **Return on Equity:** Over 15%
- **Price:** **Above SMA200**

------



### 2. The "Situational" Screeners (Finding Triggers Now)



Your original screener was trying to do this. These are much more specific and will return fewer results, but they are *actionable*.



#### 📉 The "Pullback Hunter" Screener



Your RSI filter (`RSI 40-70`) suggests you want to buy on a dip. This screener finds high-quality stocks in a long-term uptrend that are *currently* in a significant pullback.

- **Filters:** Use all the "Universe" filters (e.g., Healthcare Universe).
- **Key Technicals:**
  - Price: **Above** SMA200 (The long-term trend is *intact*)
  - Price: **Below** SMA50 (The stock is *currently* in a pullback)
  - RSI (14): **Oversold (below 40)** (The pullback is potentially finding a bottom)

This list will give you 0-10 stocks that are "on sale" and match your core thesis—perfect for deploying your Alt strategies.



#### 🚀 The "Breakout" Screener



This is the opposite of the pullback. It finds strong stocks that are *currently* breaking out to new highs.

- **Filters:** Use all the "Universe" filters (e.g., Tech Universe).
- **Key Technicals:**
  - Price: **Above** SMA200
  - **New High:** 52-Week High (The stock is showing extreme relative strength *today*)

------



### 🚫 The "Avoidance" Filter (You Got This Right)



Your "UTILITIES & ENERGY AVOIDANCE FILTER" is spot on, and your backtest data (`analysis.csv` and `DISCOVERIES.md`) confirms it 100%.

- Utilities: 0% success rate.
- Energy: 21.43% success rate.

Your logic to **blacklist** Utilities, Energy, and most Consumer Staples (except WMT) is a core part of your strategy and should be maintained.



### Your New Workflow



Here is how you can put this all together:

1. **Weekly:** Run the **"Healthcare Universe"** and **"Tech Universe"** screeners. Save these 20-50 stocks into a master watch list in TradingView.
2. **Daily:** Run the **"Pullback Hunter"** and **"Breakout"** screeners. These are your "high alert" lists.
3. **Execute:** Open your TradingView watch lists and apply your Pine Scripts (Alt10, Alt43, Alt47, etc.) to find the *exact* signals on the stocks the screeners identified.

This approach separates *finding good companies* (Finviz) from *timing the trade* (TradingView/Pine Script) and should solve your "zero results" problem immediately.

Would you like the Finviz URLs for the "Universe," "Pullback Hunter," and "Breakout" screeners I described?