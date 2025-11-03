# Pine Script COMPLETE Performance-Based Rename Script
# Renames ALL 40 scripts with ranking and profit factor
# Format: RANK_PF-X.XXX_original-name.pine

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Pine Script COMPLETE Performance Rename (1-40)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to pine-scripts directory
$scriptDir = "C:\Users\Dan\pine-scripts\pine-scripts"
Set-Location $scriptDir
Write-Host "Working directory: $scriptDir" -ForegroundColor Yellow
Write-Host ""

# Function to safely rename (handles both renamed and unrenamed files)
function Safe-Rename {
    param($old, $new)
    if (Test-Path $old) {
        try {
            Rename-Item $old $new -ErrorAction Stop
            Write-Host "[OK] $old" -ForegroundColor Green
            Write-Host "  -> $new" -ForegroundColor Gray
        }
        catch {
            Write-Host "[ERROR] Failed to rename $old" -ForegroundColor Red
            Write-Host "  Error: $_" -ForegroundColor Red
        }
    }
    else {
        Write-Host "[SKIP] File not found: $old" -ForegroundColor Yellow
    }
}

Write-Host "Starting COMPLETE rename process (40 strategies)..." -ForegroundColor Cyan
Write-Host ""

# TOP TIER - EXCELLENT PERFORMERS (Rank 1-10, PF > 1.25)
Write-Host "=== TOP TIER - EXCELLENT (Rank 1-10, PF > 1.25) ===" -ForegroundColor Green
Safe-Rename "01_PF-1.474_seykota_alt31_fractional_breakeven.pine" "01_PF-1.474_seykota_alt31_fractional_breakeven.pine"
Safe-Rename "02_PF-1.466_seykota_alt38_triple_combo.pine" "02_PF-1.466_seykota_alt38_triple_combo.pine"
Safe-Rename "03_PF-1.396_seykota_alt34_fractional_momentum.pine" "03_PF-1.396_seykota_alt34_fractional_momentum.pine"
Safe-Rename "04_PF-1.388_seykota_alt26_fractional_pyramid.pine" "04_PF-1.388_seykota_alt26_fractional_pyramid.pine"
Safe-Rename "05_PF-1.348_seykota_alt40_ultimate.pine" "05_PF-1.348_seykota_alt40_ultimate.pine"
Safe-Rename "06_PF-1.338_seykota_alt36_breakeven_momentum.pine" "06_PF-1.338_seykota_alt36_breakeven_momentum.pine"
Safe-Rename "07_PF-1.335_seykota_alt21_breakeven_lock.pine" "07_PF-1.335_seykota_alt21_breakeven_lock.pine"
Safe-Rename "08_PF-1.306_seykota_alt35_fractional_time.pine" "08_PF-1.306_seykota_alt35_fractional_time.pine"
Safe-Rename "09_PF-1.301_seykota_alt37_breakeven_time.pine" "09_PF-1.301_seykota_alt37_breakeven_time.pine"
Safe-Rename "10_PF-1.277_seykota_alt30_momentum_pyramid.pine" "10_PF-1.277_seykota_alt30_momentum_pyramid.pine"
Write-Host ""

# SOLID PERFORMERS (Rank 11-20, PF 1.0-1.25)
Write-Host "=== SOLID PERFORMERS (Rank 11-20, PF 1.0-1.25) ===" -ForegroundColor Yellow
Safe-Rename "11_PF-1.275_seykota_alt32_momentum_time.pine" "11_PF-1.275_seykota_alt32_momentum_time.pine"
Safe-Rename "12_PF-1.263_seykota_alt25_time_profit_lock.pine" "12_PF-1.263_seykota_alt25_time_profit_lock.pine"
Safe-Rename "13_PF-1.241_seykota_alt39_adaptive_targets.pine" "13_PF-1.241_seykota_alt39_adaptive_targets.pine"
Safe-Rename "14_PF-1.232_seykota_alt10_profit_targets.pine" "14_PF-1.232_seykota_alt10_profit_targets.pine"
Safe-Rename "15_PF-1.187_seykota_alt33_progressive_breakeven.pine" "15_PF-1.187_seykota_alt33_progressive_breakeven.pine"
Safe-Rename "16_PF-1.177_seykota_alt29_multi_stage_scaling.pine" "16_PF-1.177_seykota_alt29_multi_stage_scaling.pine"
Safe-Rename "17_PF-1.072_seykota_alt24_vol_adjusted_targets.pine" "17_PF-1.072_seykota_alt24_vol_adjusted_targets.pine"
Safe-Rename "18_PF-1.072_seykota_alt27_asymmetric_rr.pine" "18_PF-1.072_seykota_alt27_asymmetric_rr.pine"
Safe-Rename "19_PF-1.043_seykota_alt2_ema_crossover.pine" "19_PF-1.043_seykota_alt2_ema_crossover.pine"
Safe-Rename "20_PF-0.962_seykota_alt28_adx_filter.pine" "20_PF-0.962_seykota_alt28_adx_filter.pine"
Write-Host ""

# MARGINAL PERFORMERS (Rank 21-27, PF 0.80-0.99)
Write-Host "=== MARGINAL (Rank 21-27, PF 0.80-0.99) ===" -ForegroundColor Magenta
Safe-Rename "seykota_alt13_volatility_gated.pine" "21_PF-0.970_seykota_alt13_volatility_gated.pine"
Safe-Rename "seykota_alt7_chandelier_trail.pine" "22_PF-0.918_seykota_alt7_chandelier_trail.pine"
Safe-Rename "seykota_alt19_intrabar_execution.pine" "23_PF-0.894_seykota_alt19_intrabar_execution.pine"
Safe-Rename "seykota_alt17_dual_timeframe.pine" "24_PF-0.878_seykota_alt17_dual_timeframe.pine"
Safe-Rename "seykota_alt3_atr_channel.pine" "25_PF-0.874_seykota_alt3_atr_channel.pine"
Safe-Rename "seykota_alt12_accelerated_pyramid.pine" "26_PF-0.857_seykota_alt12_accelerated_pyramid.pine"
Safe-Rename "seykota_alt14_pullback_pyramid.pine" "27_PF-0.822_seykota_alt14_pullback_pyramid.pine"
Write-Host ""

# FAILURES (Rank 28-34, PF 0.60-0.79)
Write-Host "=== FAILURES (Rank 28-34, PF 0.60-0.79) ===" -ForegroundColor Red
Safe-Rename "21_PF-0.805_seykota_alt22_parabolic_sar.pine" "28_PF-0.805_seykota_alt22_parabolic_sar.pine"
Safe-Rename "seykota_alt4_weekly_donchian.pine" "29_PF-0.788_seykota_alt4_weekly_donchian.pine"
Safe-Rename "22_PF-0.744_seykota_alt23_keltner_channel.pine" "30_PF-0.744_seykota_alt23_keltner_channel.pine"
Safe-Rename "seykota_alt20_asymmetric_long_short.pine" "31_PF-0.729_seykota_alt20_asymmetric_long_short.pine"
Safe-Rename "seykota_alt11_tapered_pyramid.pine" "32_PF-0.715_seykota_alt11_tapered_pyramid.pine"
Safe-Rename "seykota_alt5_close_confirmed.pine" "33_PF-0.712_seykota_alt5_close_confirmed.pine"
Safe-Rename "seykota_alt9_time_exit.pine" "34_PF-0.700_seykota_alt9_time_exit.pine"
Write-Host ""

# DISASTERS (Rank 35-40, PF < 0.60)
Write-Host "=== DISASTERS (Rank 35-40, PF < 0.60) ===" -ForegroundColor DarkRed
Safe-Rename "seykota_alt18_regime_risk.pine" "35_PF-0.605_seykota_alt18_regime_risk.pine"
Safe-Rename "seykota_alt8_adaptive_exit.pine" "36_PF-0.590_seykota_alt8_adaptive_exit.pine"
Safe-Rename "seykota_alt15_single_position.pine" "37_PF-0.177_seykota_alt15_single_position.pine"
Safe-Rename "seykota_alt1_fast_breakout_s1.pine" "38_PF-0.131_seykota_alt1_fast_breakout.pine"
Safe-Rename "seykota_alt6_pure_atr_stop.pine" "39_PF-0.000_seykota_alt6_pure_atr_stop.pine"
Safe-Rename "seykota_alt16_anti_chop.pine" "40_PF-0.000_seykota_alt16_anti_chop.pine"
Write-Host ""

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "COMPLETE rename finished! All 40 strategies ranked." -ForegroundColor Green
Write-Host ""
Write-Host "Performance Summary:" -ForegroundColor Cyan
Write-Host "  Top Tier (1-10): PF > 1.25 - EXCELLENT" -ForegroundColor Green
Write-Host "  Solid (11-20): PF 1.0-1.25 - PROFITABLE" -ForegroundColor Yellow
Write-Host "  Marginal (21-27): PF 0.80-0.99 - NEAR BREAKEVEN" -ForegroundColor Magenta
Write-Host "  Failures (28-34): PF 0.60-0.79 - UNPROFITABLE" -ForegroundColor Red
Write-Host "  Disasters (35-40): PF < 0.60 - SEVERELY UNPROFITABLE" -ForegroundColor DarkRed
Write-Host ""
Write-Host "Top 3 for Live Trading:" -ForegroundColor Cyan
Write-Host "  01. Alt 31 - Fractional + BE Lock (PF 1.474, +40.05%)" -ForegroundColor Green
Write-Host "  02. Alt 38 - Triple Combo (PF 1.466, +38.91%)" -ForegroundColor Green
Write-Host "  03. Alt 34 - Fractional + Momentum (PF 1.396, +33.83%)" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Cyan
