# Sector Testing Tickers

This document provides recommended tickers for systematic strategy testing across all major sectors.

## Testing Workflow

For each sector below:
1. Navigate to the sector folder (e.g., `sectors/basic-materials/`)
2. Test your strategies on the recommended tickers
3. Save screenshots to `sectors/[sector-name]/screenshots/`
4. Document which strategies work best for each ticker
5. Compare results across sectors to identify sector-specific patterns

---

## Basic Materials

**Folder:** `sectors/basic-materials/`

### Recommended Tickers:
- **FCX** - Freeport-McMoRan (Copper/Gold mining)
- **NUE** - Nucor Corporation (Steel)
- **LIN** - Linde plc (Industrial gases)

*Alternative:* DD (DuPont), APD (Air Products), ALB (Albemarle)

---

## Communication Services

**Folder:** `sectors/communication-services/`

### Recommended Tickers:
- **META** - Meta Platforms (Social media)
- **GOOGL** - Alphabet (Search/advertising)
- **DIS** - Walt Disney (Media/entertainment)

*Alternative:* NFLX (Netflix), T (AT&T), CMCSA (Comcast)

---

## Consumer Cyclical

**Folder:** `sectors/consumer-cyclical/`

### Recommended Tickers:
- **AMZN** - Amazon (E-commerce/retail)
- **TSLA** - Tesla (Automotive)
- **HD** - Home Depot (Home improvement retail)

*Alternative:* NKE (Nike), SBUX (Starbucks), MCD (McDonald's)

---

## Consumer Defensive

**Folder:** `sectors/consumer-defensive/`

### Recommended Tickers:
- **WMT** - Walmart (Discount retail)
- **PG** - Procter & Gamble (Consumer goods)
- **KO** - Coca-Cola (Beverages)

*Alternative:* PEP (PepsiCo), COST (Costco), CL (Colgate-Palmolive)

---

## Energy

**Folder:** `sectors/energy/`

### Recommended Tickers:
- **XOM** - ExxonMobil (Integrated oil & gas)
- **CVX** - Chevron (Integrated oil & gas)
- **COP** - ConocoPhillips (Exploration & production)

*Alternative:* SLB (Schlumberger), EOG (EOG Resources), PSX (Phillips 66)

---

## Financial

**Folder:** `sectors/financial/`

### Recommended Tickers:
- **JPM** - JPMorgan Chase (Banking)
- **BAC** - Bank of America (Banking)
- **BRK.B** - Berkshire Hathaway (Diversified financial)

*Alternative:* WFC (Wells Fargo), GS (Goldman Sachs), MS (Morgan Stanley)

---

## Healthcare

**Folder:** `sectors/healthcare/`

### Recommended Tickers:
- **UNH** - UnitedHealth Group (Health insurance)
- **JNJ** - Johnson & Johnson (Pharmaceuticals/medical devices)
- **LLY** - Eli Lilly (Pharmaceuticals)

*Alternative:* PFE (Pfizer), ABBV (AbbVie), TMO (Thermo Fisher)

---

## Industrials

**Folder:** `sectors/industrials/`

### Recommended Tickers:
- **BA** - Boeing (Aerospace)
- **CAT** - Caterpillar (Heavy machinery)
- **UPS** - United Parcel Service (Logistics)

*Alternative:* HON (Honeywell), GE (General Electric), RTX (Raytheon)

---

## Real Estate

**Folder:** `sectors/real-estate/`

### Recommended Tickers:
- **AMT** - American Tower (Cell tower REITs)
- **PLD** - Prologis (Industrial REITs)
- **SPG** - Simon Property Group (Retail REITs)

*Alternative:* EQIX (Equinix), PSA (Public Storage), O (Realty Income)

---

## Technology

**Folder:** `sectors/technology/`

### Recommended Tickers:
- **AAPL** - Apple (Consumer electronics)
- **MSFT** - Microsoft (Software/cloud)
- **NVDA** - Nvidia (Semiconductors)

*Alternative:* AVGO (Broadcom), ORCL (Oracle), CSCO (Cisco)

---

## Utilities

**Folder:** `sectors/utilities/`

### Recommended Tickers:
- **NEE** - NextEra Energy (Electric utility)
- **DUK** - Duke Energy (Electric utility)
- **SO** - Southern Company (Electric utility)

*Alternative:* D (Dominion Energy), AEP (American Electric Power), XEL (Xcel Energy)

---

## ETFs

**Folder:** `sectors/etfs/`

### Recommended Tickers:

#### Broad Market:
- **SPY** - S&P 500 (Already tested ✓)
- **QQQ** - Nasdaq-100 (Tech-heavy)
- **IWM** - Russell 2000 (Small caps)

#### Sector-Specific ETFs:
- **XLE** - Energy Select Sector SPDR
- **XLU** - Utilities Select Sector SPDR
- **XLF** - Financial Select Sector SPDR
- **XLK** - Technology Select Sector SPDR
- **XLV** - Health Care Select Sector SPDR
- **XLI** - Industrial Select Sector SPDR

#### Other:
- **DIA** - Dow Jones Industrial Average
- **VTI** - Vanguard Total Stock Market

*Note: SPY results are already in this folder*

---

## Key Observations to Track

For each ticker tested, document:
1. **Profit Factor** - Does the strategy maintain profitability?
2. **Win Rate** - How does it compare to SPY results?
3. **Max Drawdown** - Sector-specific volatility patterns
4. **Trade Frequency** - Does the sector produce more/fewer signals?
5. **Best Performing Strategy** - Which alt works best for this sector?

## Strategy Testing Priority

Based on your SPY results, test these first on each new ticker:
1. **alt31** - Fractional + BE Lock (PF: 1.474)
2. **alt38** - Triple Combo (PF: 1.466)
3. **alt34** - Fractional + Momentum (PF: 1.396)
4. **alt26** - Fractional Pyramid (PF: 1.388)
5. **alt40** - Ultimate (PF: 1.348)

If these top performers fail, move to:
- alt36 (BE + Momentum, PF: 1.338)
- alt21 (Breakeven Lock, PF: 1.335)
- alt35 (Fractional + Time, PF: 1.306)

---

## Quick Testing Template

When testing a new ticker, create a file like `sectors/[sector]/TICKER_RESULTS.md`:

```markdown
# [TICKER] Results

**Sector:** [Sector Name]
**Date Tested:** [Date]

## Top 5 Strategies

| Strategy | Profit Factor | Win Rate | Max DD | Notes |
|----------|---------------|----------|--------|-------|
| alt31    |               |          |        |       |
| alt38    |               |          |        |       |
| alt34    |               |          |        |       |
| alt26    |               |          |        |       |
| alt40    |               |          |        |       |

## Key Findings
- [What worked]
- [What didn't work]
- [Sector-specific patterns observed]
```
