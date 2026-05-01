# figure_table_factory_final_v2

## Status
F3 final freeze update for output-layer completeness.

## Direct answer
### Are `calibration_log.csv` and `calibration_summary.csv` enough?
Yes. They are the **necessary raw calibration files** for the final thesis-level calibration figure and table.
No additional calibration-specific runs are required **if** the clean lineage already contains:
- `minimal_real__main__trainval__20260419__01`
- `calibration__main__val__20260419__01`
- `full__main__test__20260419__01`
- `full__robust__d04__20260419__01`
- clean inference package
- clean solver reliability aggregate

### Are other necessary figures still needed?
Yes — but only at the **output layer**, not at the experiment layer.

The previous final factory scripts already cover:
- Figure 8.1 trade-off map
- Figure 8.2 rolling structural comparison
- Figure 8.4 cumulative return & drawdown
- Table 7.1, Table 8.1, Table 8.2, Table 8.3, Table A.1

The remaining **necessary** output-layer items are:
1. **Figure 7.1** calibration heatmap  
2. **Figure 8.3** capital allocation vs CtR contribution mirror bars  
3. **Appendix inference table**  
4. **Appendix solver failure catalog table**

These are necessary because they support:
- the calibration logic in Chapter 7
- the “money vs contribution” explanation in Chapter 8
- the final appendix evidence chain for inference and numerical reliability

### Are any further empirical runs still necessary?
No.
At this point, no further **necessary** backtest / calibration / robustness / inference / solver runs are missing, provided the clean-lineage results have already been generated and accepted.

The remaining necessary work is:
- final figure/table export
- chapter writing
- defense/PPT finalization

## Final required main-text figures
1. Figure 7.1 — calibration heatmap
2. Figure 8.1 — Main trade-off map
3. Figure 8.2 — rolling D_B / D_R + active band
4. Figure 8.3 — capital vs CtR contribution mirror bars
5. Figure 8.4 — cumulative return and drawdown

## Final required main-text tables
1. Table 7.1 — calibration screening summary
2. Table 8.1 — overall performance and trading
3. Table 8.2 — structural mechanism summary
4. Table 8.3 — solver reliability summary

## Final appendix tables
1. Table A.1 — d08 vs d04 robustness
2. Table A.2 — inference summary
3. Table A.3 — solver failure catalog

## What is not necessary anymore
- new toy runs
- new universes
- new baselines
- new covariance estimators for the core thesis
- extra visual “advanced” plots with weak linkage to existing CSV outputs

## Freeze note
This file supersedes older figure factory versions when the user is working from the clean accepted lineage.
