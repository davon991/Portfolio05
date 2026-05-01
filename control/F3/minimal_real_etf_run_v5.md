# minimal_real_etf_run_v5

## Role
This file records the clean-rerun confirmation for the minimal real ETF stage after rebuilding the project in a fresh directory.

## Accepted clean-rerun result
- **run_id**: `minimal_real__main__trainval__20260419__01`
- **data window**: `2016-01-01` to `2020-12-31`
- **universe**: `core10_etf`
- **main parameters**: `delta=0.02`, `eta=0.02`, `gamma=0.001`, `rho=100.0`
- **status**: `success`

## Stage conclusion
The minimal-real stage is confirmed reproducible in the fresh environment.

## What is now established
1. The real-data monthly backtest path is clean in the fresh rerun.
2. The six-strategy result panel is complete and usable.
3. The main strategy remains a genuine CtR/CtB compromise rather than a duplicate of CtR-only.
4. GMV is numerically clean in this minimal-real rerun and no longer needs a special warning for this stage.

## What this stage does not establish
- It does not replace calibration.
- It does not replace the final test result.
- It does not provide statistical inference by itself.

## Forward rule
- Use this clean-rerun minimal-real result as the preferred train/validation evidence source.
- Move directly to `calibration` in the same clean directory.
