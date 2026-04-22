# figure_table_factory_final.md

Status: **F3 final freeze**

## 0. Purpose

This file freezes the **final figure and table factory** for the thesis after the clean-lineage execution chain has been completed and accepted:

- `minimal_real__main__trainval__20260419__01`
- `calibration__main__val__20260419__01`
- `full__main__test__20260419__01`
- `full__robust__d04__20260419__01`
- `full__main__test__20260419__01/inference`
- clean-lineage `solver_reliability` aggregate

The factory is designed to serve the thesis core line only:

1. CtR as the primary objective
2. CtB as the structural constraint
3. coordinated modeling between CtR and CtB
4. unified solver and numerical reliability
5. parameter calibration
6. real ETF test results
7. defense readiness

No figure or table should enter the main text unless it directly supports one of those seven points.

---

## 1. Final evidence hierarchy

### 1.1 Primary empirical specification
- **Main specification**: `d08 = (delta=0.02, eta=0.05, gamma=0.001, rho=100.0)`
- Role: primary thesis model

### 1.2 Robustness specification
- **Strict-band specification**: `d04 = (delta=0.01, eta=0.05, gamma=0.001, rho=100.0)`
- Role: strict-band robustness evidence

### 1.3 Accepted final interpretation
- Main is **not** the return or Sharpe champion.
- Main is the **mechanism-consistent compromise model**.
- Relative to `CtR-only`, Main significantly lowers `D_B`, while significantly raising `D_R` and turnover.
- Relative to `CtB-only`, Main preserves more CtR structure and lowers turnover, but gives up some CtB tightness.
- Relative to `EW` and `GMV`, Main improves structural metrics, but no universal return dominance is claimed.
- `d04` is stricter, not universally superior.
- GMV is a numerically clean low-volatility benchmark after decoupling and clean rerun.

---

## 2. Stable source files allowed for figure/table generation

Only the following file classes are allowed as stable sources.

### 2.1 Main full run
- `summary_metrics.csv`
- `weights.csv`
- `ctr_long.csv`
- `ctb_long.csv`
- `dr_db_timeseries.csv`
- `objective_terms.csv`
- `turnover_timeseries.csv`
- `solver_diagnostics.csv`
- `analysis_pack.json`
- `run_manifest.json`
- `run_diagnostics.json`

### 2.2 Calibration
- `calibration_summary.csv`
- `calibration_log.csv`

### 2.3 Robustness full run (`d04`)
- same schema as main full run

### 2.4 Inference package
- `inference_summary.csv`
- `bootstrap_metric_deltas.csv`
- `hypothesis_tests.csv`
- `inference_notes.md`

### 2.5 Solver aggregate
- `solver_reliability_summary.csv`
- `solver_stage_breakdown.csv`
- `solver_failure_catalog.csv`

### 2.6 Not permitted as primary sources
- manual spreadsheet editing
- temporary screenshots used as primary numerical evidence
- unsaved plotting notebook states
- legacy lineage outputs

---

## 3. Layering rule

### Main text
Use only figures and tables that are necessary for:
- Chapter 7 calibration logic
- Chapter 8 main empirical result
- direct defense of why Main remains the thesis model

### Appendix
Use figures and tables that strengthen interpretation but would slow down the main narrative.

### Defense only
Use condensed, high-density visuals tailored to oral explanation.

---

## 4. Final main-text figure list (ranked)

## Figure 7.1
- **Chinese title**: 主模型参数校准热图：`delta`–`eta` 的机制与交易权衡
- **English title**: Calibration Heatmap for the Main Model: the `delta`–`eta` Mechanism–Turnover Trade-off
- **Section**: Chapter 7, calibration
- **Core question**: Why was `d08` selected as the main specification?
- **Claim supported**: parameter choice follows mechanism quality and controllable trading, not Sharpe chasing
- **Files**: `calibration_summary.csv`, `calibration_log.csv`
- **Layer**: Main text
- **Priority**: 1
- **Recommended chart**: 2D heatmap, x=`eta`, y=`delta`, fill=`db_mean`, annotations=`dr_mean / turnover_mean / failure_rate`
- **Why this form**: two-parameter grid is naturally represented by a heatmap; easier to identify `d08` and `d04`
- **Highlight**: star for `d08`, square for `d04`, visual warning on rejected/high-failure cells
- **Caption draft**: The figure summarizes the validation-stage calibration grid. The final choice `d08` is selected as the best balance between CtB improvement, CtR discipline, and trading control, while `d04` is retained as a stricter-band backup.
- **Body guidance**: explain first what `delta` tightens, then what `eta` smooths, then why `d08` is a balance point rather than a performance winner.

## Figure 8.1
- **Chinese title**: 测试集机制折中图：`D_R`、`D_B` 与换手的联合比较
- **English title**: Test-Sample Mechanism Trade-off Map: Joint Comparison of `D_R`, `D_B`, and Turnover
- **Section**: Chapter 8, main empirical result
- **Core question**: Why is Main the thesis model although it is not the return champion?
- **Claim supported**: Main is the CtR/CtB compromise solution
- **Files**: `summary_metrics.csv`
- **Layer**: Main text
- **Priority**: 2
- **Recommended chart**: scatter map, x=`db_mean`, y=`dr_mean`, marker size=`turnover_mean`, fixed strategy colors
- **Why this form**: directly visualizes the price paid for structural improvement
- **Highlight**: thicker outline for Main; optional small note that EW/GMV optimize different objectives
- **Caption draft**: Main sits between CtR-only and CtB-only in mechanism space, reducing CtB dispersion relative to CtR-only while accepting a limited increase in CtR deviation and turnover.
- **Body guidance**: explicitly say that this is the thesis target space, not a Sharpe contest.

## Figure 8.2
- **Chinese title**: Main 与 CtR-only 的滚动机制比较：`D_B`、`D_R` 与 band 激活
- **English title**: Rolling Mechanism Comparison of Main and CtR-only: `D_B`, `D_R`, and Band Activation
- **Section**: Chapter 8, mechanism explanation
- **Core question**: Does the CtB band really work over time?
- **Claim supported**: Main persistently imposes structural control rather than changing only average summary statistics
- **Files**: `dr_db_timeseries.csv`, `objective_terms.csv`
- **Layer**: Main text
- **Priority**: 3
- **Recommended chart**: two stacked panels
  - upper: rolling `D_B` for Main vs CtR-only
  - lower: rolling `D_R` plus band activation shading or band penalty overlay
- **Why this form**: directly answers dynamic mechanism questions
- **Highlight**: periods of active band / nonzero penalty
- **Caption draft**: The figure shows that Main reduces CtB dispersion through time relative to CtR-only, and that the constraint is not decorative: the band is active over substantial parts of the test period.
- **Body guidance**: interpret dynamic mechanism first, performance implications second.

## Figure 8.3
- **Chinese title**: 最新期资本配置与 CtR 配置镜像图
- **English title**: Latest-Period Capital Allocation versus CtR Allocation Mirror Plot
- **Section**: Chapter 8, portfolio interpretation
- **Core question**: How do capital weights differ from risk allocations?
- **Claim supported**: Main is structurally different from naive capital allocation rules
- **Files**: `weights.csv`, `ctr_long.csv`
- **Layer**: Main text
- **Priority**: 4
- **Recommended chart**: mirrored horizontal bars for one selected date (latest date in full test), one side capital weights, the other side CtR shares
- **Why this form**: the most intuitive way to separate capital and risk contributions
- **Highlight**: Main, CtR-only, EW side-by-side facets
- **Caption draft**: The figure contrasts capital allocation and CtR allocation in the latest test period. It helps show that Main is not simply a capital-weight rule but a structurally organized risk-budgeting portfolio.
- **Body guidance**: keep interpretation concrete and asset-specific; avoid overloading with too many strategies.

## Figure 8.4
- **Chinese title**: 测试集累计收益与回撤背景图
- **English title**: Test-Sample Cumulative Return and Drawdown Background Chart
- **Section**: Chapter 8, performance background
- **Core question**: How should simple performance be contextualized without letting it dominate the thesis?
- **Claim supported**: Main is not the raw-performance winner, and that is not a contradiction of the thesis objective
- **Files**: `monthly_returns.csv`, `summary_metrics.csv`
- **Layer**: Main text
- **Priority**: 5
- **Recommended chart**: top panel cumulative return, bottom panel drawdown; show Main, EW, GMV, CtR-only only
- **Why this form**: enough to acknowledge performance reality without turning Chapter 8 into a horse race
- **Highlight**: annotation note on EW stronger return / GMV lower volatility, but different objective role
- **Caption draft**: The figure provides performance background only. It does not overturn the thesis interpretation because the thesis model is justified by structural mechanism rather than by raw-return leadership alone.
- **Body guidance**: state clearly that performance is contextual, not the selection criterion.

---

## 5. Final main-text table list (ranked)

## Table 7.1
- **Chinese title**: 主模型参数校准筛选表
- **English title**: Main-Model Calibration Screening Table
- **Section**: Chapter 7
- **Core question**: Which parameter candidates survive the calibration protocol and why?
- **Files**: `calibration_summary.csv`
- **Layer**: Main text
- **Priority**: 1
- **Recommended columns**: candidate, `delta`, `eta`, `dr_mean`, `db_mean`, `turnover_mean`, `failure_rate`, `active_rate`, selected_role
- **Why table not figure**: precise candidate-by-candidate reporting is clearer in a table
- **Highlight**: bold `d08`, italics `d04`
- **Caption draft**: The table summarizes the validation-stage screening logic and shows why `d08` is selected as the primary specification while `d04` is retained as the strict-band robustness point.

## Table 8.1
- **Chinese title**: 测试集总体绩效与交易结果表
- **English title**: Test-Sample Summary of Performance and Trading Statistics
- **Section**: Chapter 8
- **Core question**: What are the overall performance and trading outcomes on the test sample?
- **Files**: `summary_metrics.csv`
- **Layer**: Main text
- **Priority**: 2
- **Recommended columns**: ann_return, ann_vol, sharpe, max_drawdown, turnover_mean, turnover_p95
- **Why table not figure**: exact numerical reporting is required
- **Highlight**: visually separate structural strategies (`Main`, `CtR-only`, `CtB-only`, `MDP`) from reference baselines (`EW`, `GMV`)
- **Caption draft**: The table reports conventional performance and trading summaries, while the interpretation of the thesis result remains mechanism-first rather than Sharpe-first.

## Table 8.2
- **Chinese title**: 测试集机制结果表
- **English title**: Test-Sample Mechanism Result Table
- **Section**: Chapter 8
- **Core question**: What exactly does Main improve and what does it cost?
- **Files**: `summary_metrics.csv`, `dr_db_timeseries.csv`
- **Layer**: Main text
- **Priority**: 3
- **Recommended columns**: `dr_mean`, `db_mean`, `active_rate`, `failure_rate`, `band_active_share`, `band_penalty_mean`
- **Why table not figure**: exact mechanism summary deserves precise values
- **Highlight**: compare `Main` directly with `CtR-only`, `CtB-only`, `EW`, `GMV`
- **Caption draft**: The table isolates the structural metrics directly targeted by the thesis and shows the trade-off profile of Main relative to the main benchmarks.

## Table 8.3
- **Chinese title**: clean 主线求解器稳定性表
- **English title**: Solver Reliability Table on the Clean Accepted Lineage
- **Section**: Chapter 8 or solver subsection
- **Core question**: Is the solver numerically reliable on the accepted execution chain?
- **Files**: `solver_reliability_summary.csv`, `solver_stage_breakdown.csv`
- **Layer**: Main text
- **Priority**: 4
- **Recommended columns**: strategy, run_stage, success_rate, partial_rate, fallback_rate, mean_kkt_residual
- **Why table not figure**: main-text numerical credibility is better conveyed in a compact table
- **Highlight**: all success rates 1.0 in minimal and full stages; note GMV is numerically clean after decoupling
- **Caption draft**: The table summarizes numerical reliability on the accepted clean lineage and shows that the solver is operationally stable on the stages relevant to the final thesis claims.

---

## 6. Appendix figures and tables

## Appendix figures (recommended)
1. **A.1** CtR heatmap through time (`ctr_long.csv`)
2. **A.2** CtB heatmap through time (`ctb_long.csv`)
3. **A.3** all-strategy latest weight heatmap (`weights.csv`)
4. **A.4** calibration supplementary heatmap: failure rate / active rate (`calibration_summary.csv`)
5. **A.5** `d08` vs `d04` direct robustness comparison (`summary_metrics.csv` from both full runs)
6. **A.6** solver KKT residual distribution (`solver_diagnostics.csv`, `solver_stage_breakdown.csv`)
7. **A.7** toy-suite summary panel (only one page, not all toy runs separately)

## Appendix tables (recommended)
1. **A.1** bootstrap inference summary table
2. **A.2** hypothesis-test table
3. **A.3** solver failure catalog (clean lineage only, if nonempty)
4. **A.4** latest-period top weights by strategy

## Why appendix only
These are useful for depth, robustness, or defense preparation, but they would interrupt the main narrative if placed in the body.

---

## 7. Defense-only visuals

## Defense Figure D1
- **Chinese title**: 为什么 Main 仍是论文主模型？
- **Form**: one-slide 2x2 panel
  - top-left: Figure 8.1 simplified
  - top-right: Figure 8.4 simplified
  - bottom-left: Main vs CtR-only mechanism delta card
  - bottom-right: one-sentence thesis objective reminder
- **Reason**: directly answers the most likely committee challenge

## Defense Figure D2
- **Chinese title**: `d08` 与 `d04`：更平衡 vs 更严格
- **Form**: paired bars for `db_mean`, `dr_mean`, `turnover_mean`
- **Reason**: compact oral explanation of robustness

## Defense Figure D3
- **Chinese title**: clean solver reliability summary
- **Form**: compact table + small success-rate bars
- **Reason**: enough to close solver questions without crowding the main thesis slides

---

## 8. Visual system (final freeze)

## 8.1 Overall palette
Keep the palette muted, publication-safe, and grayscale-safe.

### Strategy colors
- `Main`: deep navy `#1F3A5F`
- `CtR-only`: muted teal `#2C7A7B`
- `CtB-only`: muted plum `#6B4F7A`
- `MDP`: slate blue `#4C5D8A`
- `GMV`: medium gray `#7A7A7A`
- `EW`: dark sand / warm gray `#A08F73`

### Utility colors
- **Emphasis color**: dark navy `#1F3A5F`
- **Warning color**: muted brick `#A14E3B`
- **Neutral line / grid color**: `#D0D4D8`
- **Appendix secondary gray**: `#B7BDC3`

## 8.2 Visual rules
- no gradient fills
- no decorative shadows
- no 3D perspective
- no dark background in thesis figures
- legends should default to top-right or below, never floating over dense data
- gridlines must be faint and secondary
- title text must be shorter than the caption

## 8.3 Gray-print compatibility
- distinguish strategies by line style or marker shape in addition to color
- Main must always have the strongest line weight
- GMV and EW must never both appear as similar light grays without marker differentiation

## 8.4 Single-column / double-column rules
- minimum font size at final print scale: 8 pt
- line width: 1.2–1.8 pt in body figures
- marker size: large enough to survive 50% reduction
- no more than 4 colored strategies on one single-column line chart

---

## 9. Items that must be explicitly highlighted in text or visuals

### Must be highlighted in the main text
- Main is not the return champion
- Main significantly lowers `D_B` relative to `CtR-only`
- this comes with significantly higher `D_R` and turnover
- `d08` is main because it was selected on validation, not because it won the test set
- `d04` is strict-band robustness, not a replacement
- GMV is numerically clean after decoupling, but still not the thesis model

### Must be highlighted visually
- `d08` and `d04` in calibration
- Main point in mechanism map
- active-band periods in rolling chart
- Main vs CtR-only comparison in mechanism figures
- clean-lineage success rates in solver table

### Should remain appendix-only
- full CtR/ CtB heatmaps
- toy details beyond one summary panel
- detailed bootstrap distribution plots
- full solver failure catalog

---

## 10. Final do-not-use list

Do **not** include the following in the final thesis package:

1. dendrogram / correlation-cluster trees
   - unsupported by current stable outputs
2. 3D calibration surfaces
   - weak readability, poor printability
3. radar charts
   - visually flashy, analytically weak
4. sankey weight-flow charts
   - too decorative for the thesis question
5. large toy-by-toy gallery in the main text
   - toy stage is already complete and no longer central
6. strategy ranking posters
   - encourages winner-takes-all reading, which conflicts with thesis logic

---

## 11. Final generation order

### Main text first
1. Figure 7.1
2. Table 7.1
3. Figure 8.1
4. Table 8.1
5. Table 8.2
6. Figure 8.2
7. Figure 8.3
8. Figure 8.4
9. Table 8.3

### Then appendix
- inference tables
- CtR / CtB heatmaps
- robustness comparison figures
- solver appendix plots

### Then defense package
- D1, D2, D3

---

## 12. Final freeze statement

This factory is now treated as the **final figure/table plan** for the thesis.
No additional main-text figure or table should be introduced unless it replaces one of the items above and improves the thesis argument more directly.
