@echo off
REM Windows setup script for statistical analysis environment
REM Run this from Anaconda Prompt

echo ================================================================================
echo Python Statistical Analysis Environment Setup
echo ================================================================================
echo.

REM Check if conda is available
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda not found!
    echo.
    echo Please install Miniconda or Anaconda first:
    echo   - Miniconda: https://docs.conda.io/en/latest/miniconda.html
    echo   - Anaconda: https://www.anaconda.com/download
    echo.
    echo Then run this script from "Anaconda Prompt"
    pause
    exit /b 1
)

echo [1/4] Conda found, checking for existing environment...
conda env list | findstr "trading-analysis" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Environment 'trading-analysis' already exists.
    echo Removing old environment...
    call conda env remove -n trading-analysis -y
)

echo.
echo [2/4] Creating conda environment from environment.yml...
echo This may take 2-5 minutes...
call conda env create -f environment.yml

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to create environment!
    pause
    exit /b 1
)

echo.
echo [3/4] Activating environment...
call conda activate trading-analysis

echo.
echo [4/4] Testing installation...
python -c "import pandas, numpy, statsmodels, sklearn, matplotlib, seaborn; print('All packages imported successfully!')"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Package import failed!
    pause
    exit /b 1
)

echo.
echo ================================================================================
echo Setup complete!
echo ================================================================================
echo.
echo To run the analysis:
echo   1. conda activate trading-analysis
echo   2. python statistical_analysis.py
echo.
echo Or simply run:  run_analysis.bat
echo.
pause
