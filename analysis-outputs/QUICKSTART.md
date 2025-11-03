# QUICK START: Python Statistical Analysis

**5-Minute Setup Guide** | Works on Windows, Linux, WSL, macOS

---

## Option 1: Automated Setup (Recommended)

### **Windows:**
1. Install Miniconda: https://docs.conda.io/en/latest/miniconda.html
2. Open **Anaconda Prompt** (search in Start menu)
3. Navigate to this folder:
   ```cmd
   cd C:\path\to\trend-following-backtesting-strategies\analysis-outputs
   ```
4. Run setup:
   ```cmd
   setup.bat
   ```
5. Run analysis:
   ```cmd
   run_analysis.bat
   ```

### **Linux/WSL/macOS:**
1. Install Miniconda (if needed):
   ```bash
   # Linux/WSL
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh

   # macOS
   brew install miniconda
   ```
2. Navigate to this folder:
   ```bash
   cd /path/to/trend-following-backtesting-strategies/analysis-outputs
   ```
3. Run setup:
   ```bash
   ./setup.sh
   ```
4. Run analysis:
   ```bash
   ./run_analysis.sh
   ```

---

## Option 2: Manual Setup (If scripts don't work)

### Step 1: Create Environment
```bash
conda env create -f environment.yml
```

### Step 2: Activate Environment
```bash
conda activate trading-analysis
```

### Step 3: Run Analysis
```bash
python statistical_analysis.py
```

---

## What You'll Get

### **Console Output:**
- Sector performance rankings (Healthcare 92%, Utilities 0%)
- Strategy success rates (Alt10 76%, Alt26 57%)
- Logistic regression: "Profit targets increase odds by 3.2x"
- Linear regression: What drives profit factor?
- Feature importance: Which strategy features matter most?

### **Files in `statistical_outputs/`:**
1. **Visualizations (PNG):**
   - `correlation_matrix.png` - Metric relationships
   - `sector_performance_boxplot.png` - Returns by sector
   - `sector_win_rate.png` - Success rate by sector
   - `risk_return_scatter.png` - Risk vs return map
   - `feature_importance.png` - Top 15 predictive features

2. **Data Files (CSV):**
   - `logistic_regression_results.csv` - Profitability model
   - `linear_regression_results.csv` - Profit factor model
   - `feature_importance.csv` - All features ranked

3. **Summary:**
   - `ANALYSIS_REPORT.txt` - Text summary of findings

**Runtime:** 10-30 seconds

---

## Troubleshooting

### "conda: command not found"
**Solution:** Install Miniconda first (see links above)

### "Environment not found"
**Solution:** Run setup script first (`setup.bat` on Windows, `./setup.sh` on Linux)

### "FileNotFoundError: cleaned-data.csv"
**Solution:** Make sure you're in the `analysis-outputs` directory. The script looks for `../cleaned-data.csv`

### WSL Path Issues
Access Windows files from WSL:
```bash
cd /mnt/c/Users/YourName/path/to/project/analysis-outputs
```

---

## Key Analyses Performed

### 1. **Logistic Regression**
**Answers:** What predicts profitability?
- Sector effects (Healthcare vs Utilities)
- Strategy features (profit targets, pyramiding)
- Asset type (stocks vs ETFs)

### 2. **Linear Regression**
**Answers:** What drives profit factor?
- Win rate impact
- Trade frequency impact
- Sector effects

### 3. **Feature Importance**
**Answers:** Which features matter most?
- Random Forest ranking
- Cross-validated accuracy
- Top 15 features visualized

### 4. **Hypothesis Testing**
**Answers:** Are differences statistically significant?
- Profit targets vs no profit targets
- Healthcare vs Utilities
- Stocks vs ETFs

### 5. **Correlation Analysis**
**Answers:** How do metrics relate?
- Return vs profit factor
- Win rate vs drawdown
- Trade frequency vs performance

---

## Next Steps After Running

1. **Review console output** - Look for significant findings
2. **Open `statistical_outputs/` folder** - View all charts
3. **Read `ANALYSIS_REPORT.txt`** - Quick summary
4. **Check regression CSVs** - Detailed coefficients

**Key Insights You'll Get:**
- ✅ Quantified sector effects (e.g., "Healthcare increases odds 12x")
- ✅ Strategy feature importance (profit targets > pyramiding)
- ✅ Statistical validation of your qualitative findings
- ✅ P-values showing significance of differences

---

## File Structure

```
analysis-outputs/
├── environment.yml              (Conda config)
├── statistical_analysis.py      (Main script - 600 lines)
├── README_SETUP.md              (Detailed guide)
├── QUICKSTART.md                (This file)
├── setup.bat                    (Windows auto-setup)
├── setup.sh                     (Linux auto-setup)
├── run_analysis.bat             (Windows runner)
├── run_analysis.sh              (Linux runner)
└── statistical_outputs/         (Created after first run)
    ├── correlation_matrix.png
    ├── sector_win_rate.png
    ├── feature_importance.png
    ├── logistic_regression_results.csv
    └── ANALYSIS_REPORT.txt
```

---

## Time Estimates

- **Miniconda install:** 5 minutes
- **Environment setup:** 2-5 minutes
- **Analysis runtime:** 10-30 seconds
- **Total first run:** ~10-15 minutes
- **Subsequent runs:** 10-30 seconds

---

## Platform-Specific Notes

### **Windows:**
- Use **Anaconda Prompt** (not regular Command Prompt)
- Double-click `setup.bat` to run setup
- Double-click `run_analysis.bat` to run analysis

### **WSL:**
- Install Linux version of Miniconda
- Access Windows files via `/mnt/c/`
- Charts saved as PNG (view from Windows Explorer)

### **macOS:**
- Use `brew install miniconda` for easiest setup
- Or download from Miniconda website

---

## Support Resources

**Conda Documentation:**
- https://docs.conda.io/en/latest/

**Python Packages Used:**
- pandas: https://pandas.pydata.org/
- statsmodels: https://www.statsmodels.org/
- scikit-learn: https://scikit-learn.org/

**Detailed Setup Guide:**
- See `README_SETUP.md` in this folder

---

## Expected Output Preview

```
================================================================================
STATISTICAL ANALYSIS: Trend-Following Backtests
================================================================================

Loading data from: ../cleaned-data.csv
Loaded 293 backtest results
Output directory: /path/to/statistical_outputs

Engineering features...
  - Created sector mapping for 293 tickers
  - Identified {'Stock': 154, 'ETF': 139}
  - Profitable results: 181/293 (61.8%)

================================================================================
DESCRIPTIVE STATISTICS
================================================================================

Sector Performance Summary:
                 Profitable  Total  Win_Rate  Avg_Return  Avg_PF
Healthcare              24     26      0.92       23.80    1.89
Technology              30     42      0.71       18.90    1.52
...

================================================================================
LOGISTIC REGRESSION: Predicting Profitability
================================================================================

                           Odds_Ratio  P_Value
has_profit_targets[T.True]       3.21    0.001
C(sector)[T.Healthcare]         12.45    0.000
C(sector)[T.Utilities]           0.04    0.000
...

Key Insights:
  • Profit Targets: 3.21x odds of profitability
  • Healthcare Sector: 12.45x odds vs baseline
  • Stocks vs ETFs: 1.87x odds of profitability

================================================================================
ANALYSIS COMPLETE!
================================================================================

All outputs saved to: /path/to/statistical_outputs

Generated files:
  - ANALYSIS_REPORT.txt
  - correlation_matrix.png
  - feature_importance.csv
  - feature_importance.png
  - linear_regression_results.csv
  - logistic_regression_results.csv
  - risk_return_scatter.png
  - sector_performance_boxplot.png
  - sector_win_rate.png
  - strategy_performance_boxplot.png
  - winrate_vs_trades.png
```

---

**Ready to run? Execute the setup script for your platform!**

- **Windows:** `setup.bat`
- **Linux/WSL/macOS:** `./setup.sh`
