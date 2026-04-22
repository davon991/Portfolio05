# calibration_protocol_v8

## Status
F3 rolling update after clean-rerun confirmation of `d04` on validation.

## What changed
The clean-rerun validation result for `calibration__main__val__20260419__01__d04` confirms that:
- `d04 = (delta=0.01, eta=0.05, gamma=0.001, rho=100.0)` remains a valid **strict-band robustness candidate**.
- The clean rerun does **not** replace the main parameter choice `d08`.
- The role split is therefore stable:
  - Main specification: `d08`
  - Robustness specification: `d04`

## Interpretation
Relative to `CtR-only`, `Main(d04)` continues to show:
- stronger `D_B` reduction,
- larger `D_R` sacrifice,
- somewhat higher turnover,
which is exactly the intended “tighter band” behavior.

## Decision rule
No parameter reselection is triggered by this clean-rerun check.
Proceed with:
1. `full_test.yaml` using `d08`
2. `full_test_d04.yaml` for robustness
3. `run_inference.py`
4. `aggregate_solver_reliability.py`

## Freeze impact
- F1: unchanged
- F2: unchanged
- F3: updated only
