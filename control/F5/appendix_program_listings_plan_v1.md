# appendix_program_listings_plan_v1.md

## Purpose
This file converts the advisor's requirement "В приложении должны быть листинги программ" into a concrete appendix plan.

## Rule
Main text contains formulas, algorithms, calculation examples, figures and tables.
Appendix contains full code listings.

## Required listings

### Listing A.1. Core metrics
File:
`src/ctrctb/models/metrics.py`

Purpose:
Defines portfolio variance, volatility, CtR, CtR shares, CtB, \(D_R\), \(D_B\), and diversification ratio.

Thesis reference:
Used in Chapters 3–5 and Chapter 8.

### Listing A.2. Objective functions
File:
`src/ctrctb/models/objectives.py`

Purpose:
Implements CtR-only, CtB-only, Main, GMV, and MDP objective functions.

Thesis reference:
Used in Chapter 5 model implementation.

### Listing A.3. Strategy wrappers
File:
`src/ctrctb/models/strategies.py`

Purpose:
Maps strategy labels `EW`, `GMV`, `CtR-only`, `MDP`, `CtB-only`, `Main` into solver calls.

Thesis reference:
Used in Chapters 6–8.

### Listing A.4. Unified solver
File:
`src/ctrctb/solvers/core.py`

Purpose:
Implements projected gradient followed by damped Newton and returns diagnostic information.

Thesis reference:
Used in Chapter 6 and Table 8.3.

### Listing A.5. Dedicated GMV solver
File:
`src/ctrctb/models/gmv.py`

Purpose:
Implements the dedicated long-only GMV solver via SLSQP.

Thesis reference:
Used in Chapter 6 and GMV benchmark discussion.

### Listing A.6. Result export
File:
`src/ctrctb/exports/results.py`

Purpose:
Exports weights, CtR, CtB, \(D_R\), \(D_B\), objective terms, turnover, solver diagnostics, summary metrics, and manifest.

Thesis reference:
Used in Chapter 7 reproducibility and Appendix B.

### Listing A.7. Run scripts
Files:
- `scripts/run_experiment.py`
- `scripts/run_calibration.py`
- `scripts/run_inference.py`
- `scripts/aggregate_solver_reliability.py`
- `scripts/build_figures_final_v2.py`
- `scripts/build_tables_final_v2.py`

Purpose:
Documents the reproducible experiment chain.

## Appendix ordering
A. Supplementary empirical tables.
B. Reproducibility flow.
C. Program listings.

## Do not include
- full raw CSV files;
- large generated figures in code listing section;
- environment cache files;
- `__pycache__`;
- temporary logs.
