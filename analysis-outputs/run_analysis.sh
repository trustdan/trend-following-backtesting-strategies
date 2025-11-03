#!/bin/bash
# Linux/macOS/WSL script to run statistical analysis

set -e  # Exit on error

echo "================================================================================"
echo "Running Statistical Analysis"
echo "================================================================================"
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "ERROR: Conda not found!"
    echo "Please install conda and run setup.sh first."
    exit 1
fi

# Initialize conda for this script
eval "$(conda shell.bash hook)"

# Activate environment
if ! conda activate trading-analysis 2>/dev/null; then
    echo "ERROR: Environment 'trading-analysis' not found!"
    echo "Please run setup.sh first."
    exit 1
fi

echo "Environment activated: trading-analysis"
echo ""
echo "Starting analysis..."
echo ""

# Run the analysis
python statistical_analysis.py

echo ""
echo "================================================================================"
echo "Analysis complete! Check the statistical_outputs folder."
echo "================================================================================"
echo ""
