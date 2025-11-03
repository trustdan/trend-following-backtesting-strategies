#!/bin/bash
# Linux/macOS/WSL setup script for statistical analysis environment

set -e  # Exit on error

echo "================================================================================"
echo "Python Statistical Analysis Environment Setup"
echo "================================================================================"
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "ERROR: Conda not found!"
    echo ""
    echo "Please install Miniconda or Anaconda first:"
    echo "  Linux/WSL: wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
    echo "             bash Miniconda3-latest-Linux-x86_64.sh"
    echo "  macOS: brew install miniconda"
    echo ""
    echo "Then restart your terminal and run this script again."
    exit 1
fi

echo "[1/4] Conda found, checking for existing environment..."
if conda env list | grep -q "trading-analysis"; then
    echo "Environment 'trading-analysis' already exists."
    echo "Removing old environment..."
    conda env remove -n trading-analysis -y
fi

echo ""
echo "[2/4] Creating conda environment from environment.yml..."
echo "This may take 2-5 minutes..."
conda env create -f environment.yml

echo ""
echo "[3/4] Testing installation..."
# Initialize conda for this script
eval "$(conda shell.bash hook)"
conda activate trading-analysis

python -c "import pandas, numpy, statsmodels, sklearn, matplotlib, seaborn; print('All packages imported successfully!')"

echo ""
echo "================================================================================"
echo "Setup complete!"
echo "================================================================================"
echo ""
echo "To run the analysis:"
echo "  1. conda activate trading-analysis"
echo "  2. python statistical_analysis.py"
echo ""
echo "Or simply run:  ./run_analysis.sh"
echo ""
