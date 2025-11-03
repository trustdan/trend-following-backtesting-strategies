@echo off
REM Windows script to run statistical analysis
REM Must be run from Anaconda Prompt

echo ================================================================================
echo Running Statistical Analysis
echo ================================================================================
echo.

REM Check if conda is available
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda not found! Please run from Anaconda Prompt.
    pause
    exit /b 1
)

REM Activate environment
call conda activate trading-analysis
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Environment 'trading-analysis' not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

echo Environment activated: trading-analysis
echo.
echo Starting analysis...
echo.

REM Run the analysis
python statistical_analysis.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Analysis failed!
    pause
    exit /b 1
)

echo.
echo ================================================================================
echo Analysis complete! Check the statistical_outputs folder.
echo ================================================================================
echo.
pause
