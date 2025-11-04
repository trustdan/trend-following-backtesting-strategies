Absolutely—this is a super common pain point with Finviz: stack a few “nice-to-haves” and suddenly you’ve screened the entire market away. Below are **minimal, battle‑tested screeners** with clear “tighten/loosen” dials so you never end up with *zero* or *everything*. They’re grounded in your backtest findings (e.g., **Healthcare and Tech worked best; Utilities/Energy consistently failed**) so the filters bias you toward where your research says the edge lives.  

------

## How to keep Finviz screeners from breaking

**Rule of 3:** Start with just three *core* filters (Universe, Liquidity, Trend). Only add one extra filter at a time and watch your hit count.
 **Target hit-count:** 30–150 tickers for broad discovery, 10–40 for deployment watchlists.
 **Avoid the killers:** narrow Beta ranges, stacked momentum signals, and multiple growth constraints together often zero the list.

------

## Screener A — “Healthcare Trend (Minimal)”

**Why this works:** Your tests showed Healthcare is unusually friendly to trend systems (92% strategy success across variants). Start broad, then only tighten if the list is too long. 

**Core (set these first):**

- **Sector:** Healthcare
- **Market Cap:** Mid+ (≥ $2B)
- **Average Volume:** ≥ 500k
- **Price:** ≥ $20 (use $50 if you want larger names)
- **Price vs SMA200:** Price **above** SMA200 (the most important trend check)

**Tighten (add one at a time):**

- **SMA50 > SMA200** (longer‑term trend structure)
- **SMA20 > SMA50** (short‑term momentum inside an uptrend)
- **Performance (Year):** Positive
- **Optionable:** Yes (if you need options)

**Loosen (if too few):**

- Drop **SMA20 > SMA50** (keep SMA50 > SMA200)
- Lower **Avg Volume** to ≥ 300k
- Lower **Price** to ≥ $15

**Notes:** Don’t stack RSI ranges with the MA stack at first—that’s a common “everything out” combo.

------

## Screener B — “Tech Leaders (Minimal)”

**Why this works:** Tech had strong, consistent outcomes in your tests (e.g., MSFT/QQQ strategies among top performers). 

**Core:**

- **Sector:** Technology
- **Market Cap:** Large+ (≥ $10B)
- **Average Volume:** ≥ 1M
- **Price:** ≥ $50 (use ≥ $100 for a mega‑cap list)
- **Price vs SMA200:** Price **above** SMA200

**Tighten:**

- **SMA50 > SMA200**
- **SMA20 > SMA50**
- **EPS growth next year:** Positive (one growth knob only—adding many fundamentals at once often zeros the list)
- **Optionable:** Yes

**Loosen:**

- Market Cap → **Mid+**
- Avg Volume ≥ **750k**
- Remove **SMA20 > SMA50** (keep the 200d trend)

------

## Screener C — “Broad Momentum (Ex‑Defensives)”

**Why this works:** You want a wide net but your research warns **Utilities/Energy** are hostile to trend‑following; you’ll exclude them *manually* after screening because Finviz doesn’t do sector “NOT” logic in one pass. 

**Core:**

- **Sector:** All
- **Market Cap:** Mid+
- **Average Volume:** ≥ 1M
- **Price:** ≥ $20
- **Price vs SMA200:** Price **above** SMA200
- **SMA50 > SMA200**

**Manual exclude (after results):**

- Remove tickers in **Utilities, Energy**, and (usually) **Consumer Defensive** based on your validation. 

**Tighten (if 300+ names):**

- Add **SMA20 > SMA50**
- **Performance (Year):** Positive

**Loosen (if too few):**

- Lower Avg Volume or Price slightly
- Remove SMA20 > SMA50 (keep 200d trend backbone)

------

## Screener D — “Breakout Watchlist (New Highs)”

**Use when you want a smaller, more actionable list.** Puts you on names already proving relative strength—particularly good for **Tech + Healthcare**, which your research favored. 

**Core:**

- **Signal:** New High (or Near High)
- **Sector:** Healthcare **OR** Technology (run it twice or leave “All” and prune)
- **Average Volume:** ≥ 1M
- **Price:** ≥ $20
- **Price vs SMA200:** Price **above** SMA200

**Tighten:** Add **SMA50 > SMA200**.
 **Loosen:** Change “New High” → “Near High”.

------

## Screener E — “Pullback in Uptrend”

**Idea:** Catch a dip inside a healthy trend; easier than RSI ranges that can zero out.

**Core:**

- **Price vs SMA200:** Price **above** SMA200
- **SMA50 > SMA200**
- **Performance (Week):** Down
- **Average Volume:** ≥ 750k
- **Price:** ≥ $20
- (Optional) **Sector:** Healthcare or Technology

**Tighten:** Add **SMA20 > SMA50**.
 **Loosen:** Remove **Performance (Week): Down** (keep the 200d uptrend).

------

## A quick mapping from your research → screeners

- **Lean into Healthcare & Tech first.** That’s where your 293 backtests showed the best consistency (e.g., Healthcare ~92% strategy success, Tech ~70%+), while **Utilities/Energy repeatedly underperformed**. These screeners reflect that bias.  
- **Keep “trend backbone” simple:** *Price above SMA200* + *SMA50 > SMA200* do most of the work without over‑filtering.
- **Use fundamentals sparingly:** One growth knob (e.g., **EPS next year > 0**) is fine; stacking three or four often wipes out the list.

------

## Common reasons screeners return 0 (and quick fixes)

- **Stacked momentum signals** (Price > SMA200 + SMA50 > 200 + SMA20 > 50 + New High + Perf Year Up + tight RSI) → Remove **one** at a time; keep Price > SMA200.
- **Narrow Beta or ATR % ranges** → Skip these unless you truly need them.
- **Multiple sector/industry picks** → Finviz treats them as AND, not OR. Run separate passes.
- **Over‑constrained fundamentals** (EPS this year + next year + 5y sales + ROE + margin thresholds) → Use only **one** of these to start.

------

## Want ready-to-click links?

Finviz occasionally changes parameter codes, so the most robust way is to set these in the GUI using the exact labels above. If you prefer links anyway, start with **only** the safest parameters (universal codes) and add more from the GUI:

**Healthcare Trend (Minimal, safe codes only):**

```
https://finviz.com/screener.ashx?v=111
  &f=sec_healthcare,cap_midover,sh_avgvol_o500,sh_price_o20,ta_sma200_pa
  &ft=4
```

Then add **SMA50 > SMA200** and **SMA20 > SMA50** from the GUI if your hit list is too big.

**Tech Leaders (Minimal, safe codes only):**

```
https://finviz.com/screener.ashx?v=111
  &f=sec_technology,cap_largeover,sh_avgvol_o1000,sh_price_o50,ta_sma200_pa
  &ft=4
```

*(If a link loads “too few,” loosen **cap** or **sh_avgvol** first.)*

------

## Quick deployment workflow (so this actually “works” in practice)

1. **Run Screener A or B** to build a clean, trend‑biased list in the sectors your tests favored. 
2. **Prune** any Utilities/Energy that sneak in during broad screens (C). 
3. **Promote** tickers that also appear in the **Breakout** (D) or **Pullback in Uptrend** (E) lists.
4. **Only then** layer your trading system (e.g., your Alt10/Alt26/Alt45 family) on the survivors. Your research shows those strategies generalize best across names *already in trend*. 

------

### If you’d like, I can also convert any of your old “too‑specific” filters into this **minimal + dials** format (one by one) and sanity‑check that each returns 20–150 names before you save it.