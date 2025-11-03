# Python Statistical Analysis Setup Guide

**Works on:** Windows, Linux, WSL, macOS

This guide will help you set up a conda environment and run the statistical analysis script.

---

## Prerequisites

You need **Anaconda** or **Miniconda** installed:

- **Anaconda** (full package): https://www.anaconda.com/download
- **Miniconda** (minimal): https://docs.conda.io/en/latest/miniconda.html

**Recommended:** Miniconda (smaller download, faster install)

---

## Installation Steps

### 1. Install Miniconda (if not already installed)

#### **Windows:**
1. Download from: https://docs.conda.io/en/latest/miniconda.html
2. Run the installer (accept defaults)
3. Open **Anaconda Prompt** (search in Start menu)

#### **Linux/WSL:**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# Follow prompts, accept defaults
source ~/.bashrc
```

#### **macOS:**
```bash
brew install miniconda
conda init zsh  # or 'bash' depending on your shell
```

---

### 2. Create the Conda Environment

Navigate to the `analysis-outputs` directory and create the environment:

#### **Windows (Anaconda Prompt):**
```cmd
cd C:\path\to\trend-following-backtesting-strategies\analysis-outputs
conda env create -f environment.yml
```

#### **Linux/WSL/macOS:**
```bash
cd /path/to/trend-following-backtesting-strategies/analysis-outputs
conda env create -f environment.yml
```

**This will:**
- Create an environment called `trading-analysis`
- Install Python 3.11
- Install pandas, numpy, statsmodels, scikit-learn, matplotlib, seaborn
- Takes ~2-5 minutes depending on internet speed

---

### 3. Activate the Environment

#### **Windows:**
```cmd
conda activate trading-analysis
```

#### **Linux/WSL/macOS:**
```bash
conda activate trading-analysis
```

You should see `(trading-analysis)` appear in your terminal prompt.

---

### 4. Run the Analysis Script

#### **Windows:**
```cmd
python statistical_analysis.py
```

#### **Linux/WSL/macOS:**
```bash
python statistical_analysis.py
```

**Expected runtime:** 10-30 seconds

**Output location:** `statistical_outputs/` folder (created automatically)

---

## What the Script Does

The script performs comprehensive statistical analysis on your 293 backtests:

### **Console Output:**
- Descriptive statistics (mean, median, std dev)
- Sector performance rankings
- Strategy performance rankings
- Correlation matrix
- Logistic regression results (predict profitability)
- Linear regression results (predict profit factor)
- Feature importance rankings
- Hypothesis test results

### **Files Generated in `statistical_outputs/`:**
1. **correlation_matrix.png** - Heatmap of metric correlations
2. **sector_performance_boxplot.png** - Return distribution by sector
3. **strategy_performance_boxplot.png** - Return distribution by strategy
4. **risk_return_scatter.png** - Risk vs return colored by sector
5. **winrate_vs_trades.png** - Win rate vs trade frequency
6. **sector_win_rate.png** - Bar chart of sector success rates
7. **feature_importance.png** - Top 15 predictive features
8. **logistic_regression_results.csv** - Full regression output
9. **linear_regression_results.csv** - Full regression output
10. **feature_importance.csv** - All features ranked
11. **ANALYSIS_REPORT.txt** - Text summary of findings

---

## Key Analyses Performed

### 1. **Logistic Regression: Predicting Profitability**
**Question:** What factors predict whether a backtest will be profitable?

**Outputs:**
- Odds ratios (e.g., "Profit targets increase odds by 3.2x")
- Sector effects (e.g., "Healthcare increases odds by 12.4x vs baseline")
- Stock vs ETF effects

### 2. **Linear Regression: Predicting Profit Factor**
**Question:** What drives risk-adjusted returns?

**Outputs:**
- R-squared (variance explained)
- Win rate coefficient
- Sector effects on profit factor
- Strategy feature effects

### 3. **Feature Importance: Random Forest**
**Question:** Which features matter most for profitability?

**Outputs:**
- Ranked list of all features
- Visualization of top 15
- Cross-validated accuracy

### 4. **Hypothesis Testing**
**Question:** Are observed differences statistically significant?

**Tests:**
- Profit targets vs no profit targets
- Healthcare vs Utilities performance
- Stocks vs ETFs

### 5. **Correlation Analysis**
**Question:** How do metrics relate to each other?

**Outputs:**
- Correlation matrix
- Heatmap visualization
- Key insights (e.g., "Win rate correlates 0.87 with profit factor")

---

## Troubleshooting

### **Issue: "conda: command not found"**
**Solution:** Conda not in PATH. Restart terminal or run:
```bash
# Linux/WSL/macOS
export PATH="$HOME/miniconda3/bin:$PATH"

# Windows: Use Anaconda Prompt instead of regular Command Prompt
```

### **Issue: "No module named 'pandas'"**
**Solution:** Environment not activated.
```bash
conda activate trading-analysis
```

### **Issue: "FileNotFoundError: cleaned-data.csv"**
**Solution:** Script expects CSV one directory up. Check your location:
```bash
# You should be in: analysis-outputs/
# CSV should be at: ../cleaned-data.csv

# If not, edit line 46 in statistical_analysis.py:
# Change: csv_path='../cleaned-data.csv'
# To: csv_path='/full/path/to/cleaned-data.csv'
```

### **Issue: Windows path issues with WSL**
**Solution:** If accessing Windows files from WSL:
```bash
# Windows path: C:\Users\YourName\Documents\project
# WSL path: /mnt/c/Users/YourName/Documents/project

cd /mnt/c/Users/YourName/path/to/trend-following-backtesting-strategies/analysis-outputs
```

### **Issue: Charts not displaying (Linux/WSL without X server)**
**Solution:** Script saves all charts to files, no display needed. If you want to view them:
- **Windows:** Open PNG files from File Explorer
- **WSL:** Access via Windows path: `\\wsl$\Ubuntu\home\kali\trend-following-backtesting-strategies\analysis-outputs\statistical_outputs\`
- **Linux:** Install `eog` (Eye of GNOME) or `feh` to view images

---

## Customizing the Analysis

### **Change output directory:**
Edit line 51 in `statistical_analysis.py`:
```python
self.output_dir = Path('statistical_outputs')  # Change this
```

### **Add/remove analyses:**
Edit the `run_all()` method at the bottom (lines 592-601):
```python
def run_all(self):
    self.descriptive_statistics()
    self.correlation_analysis()
    # self.logistic_regression_profitability()  # Comment out to skip
    # Add custom analysis here
```

### **Filter data before analysis:**
Edit `_engineer_features()` method to add filters:
```python
# Example: Only analyze healthcare
self.df = self.df[self.df['sector'] == 'Healthcare']
```

---

## Running in Jupyter Notebook (Interactive Mode)

If you want to explore data interactively:

### 1. Start Jupyter:
```bash
conda activate trading-analysis
jupyter notebook
```

### 2. Create a new notebook and run:
```python
from statistical_analysis import TradingAnalysis
import matplotlib.pyplot as plt

# Load data
analysis = TradingAnalysis(csv_path='../cleaned-data.csv')

# Run individual analyses
analysis.correlation_analysis()
analysis.logistic_regression_profitability()

# Access the dataframe directly
df = analysis.df
df.head()

# Custom analysis
import seaborn as sns
sns.scatterplot(data=df, x='win_rate_pct', y='total_return_pct', hue='sector')
plt.show()
```

---

## Updating Dependencies

If you need to update packages:

```bash
conda activate trading-analysis
conda update --all

# Or update specific package
conda update pandas
```

---

## Removing the Environment

When you're done:

```bash
conda deactivate
conda env remove -n trading-analysis
```

---

## Cross-Platform Notes

### **Windows:**
- Use Anaconda Prompt (not regular Command Prompt)
- Paths use backslashes: `C:\Users\...`
- Script works identically to Linux

### **WSL (Windows Subsystem for Linux):**
- Access Windows files via `/mnt/c/`
- Can use Linux commands
- Install conda for Linux (not Windows version)

### **macOS:**
- Same as Linux
- May need to install Xcode Command Line Tools
- Use `brew install miniconda` for easiest setup

---

## Performance Notes

**Dataset size:** 293 rows (very small)
- All operations are instant (< 1 second each)
- Total runtime: 10-30 seconds including plot generation

**If you had 100K+ rows:**
- Consider using `polars` instead of `pandas` (10x faster)
- Use `dask` for out-of-core processing
- Switch to Rust for production systems

---

## Next Steps After Running Analysis

1. **Review console output** - Look for significant p-values, high odds ratios
2. **Check visualizations** - Identify patterns in sector/strategy performance
3. **Read ANALYSIS_REPORT.txt** - Quick summary of findings
4. **Examine regression CSVs** - Detailed coefficients for further interpretation

**Key questions answered:**
- ✅ Does sector predict profitability? (Logistic regression)
- ✅ What drives profit factor? (Linear regression)
- ✅ Which features matter most? (Feature importance)
- ✅ Are differences statistically significant? (Hypothesis tests)

---

## Support

**Common issues:**
- Check that environment is activated: `conda activate trading-analysis`
- Verify you're in the right directory: `ls` (should see `statistical_analysis.py`)
- Check CSV path is correct (edit line 46 if needed)

**Still stuck?**
- Check conda installation: `conda --version`
- List environments: `conda env list`
- Check Python version: `python --version` (should be 3.11.x)

---

## File Structure After Setup

```
trend-following-backtesting-strategies/
├── cleaned-data.csv                      (your data)
├── analysis-outputs/
│   ├── environment.yml                   (conda config)
│   ├── statistical_analysis.py           (main script)
│   ├── README_SETUP.md                   (this file)
│   ├── statistical_outputs/              (created by script)
│   │   ├── correlation_matrix.png
│   │   ├── sector_performance_boxplot.png
│   │   ├── feature_importance.png
│   │   ├── logistic_regression_results.csv
│   │   ├── linear_regression_results.csv
│   │   └── ANALYSIS_REPORT.txt
│   └── (other analysis files...)
```

---

**Estimated time to get running:**
- Conda installation: 5-10 minutes
- Environment creation: 2-5 minutes
- First run: 10-30 seconds
- **Total: ~15-20 minutes from zero to results**

Good luck! 🚀
