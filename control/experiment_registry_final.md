# experiment_registry_final

## Status
F3 final freeze.

## Final accepted clean evidence lineage

### Core execution chain
1. `minimal_real__main__trainval__20260419__01`
2. `calibration__main__val__20260419__01`
3. `full__main__test__20260419__01`
4. `full__robust__d04__20260419__01`
5. `full__main__test__20260419__01/inference`
6. `results/solver_reliability/*` from clean-lineage aggregate only

## Final role assignment
- `minimal_real` -> feasibility and mechanism pre-check
- `calibration d08` -> main parameter selection
- `calibration d04` -> strict-band backup selection
- `full d08` -> primary thesis result
- `full d04` -> robustness result
- `inference` -> inferential support for mechanism claims
- `solver reliability` -> numerical reliability support

## Final parameter freeze
- Main specification: `d08 = (delta=0.02, eta=0.05, gamma=0.001, rho=100.0)`
- Robustness specification: `d04 = (delta=0.01, eta=0.05, gamma=0.001, rho=100.0)`

## Final interpretation freeze
- Main is not the return champion.
- Main is the mechanism-consistent compromise model.
- d04 is stricter, not superior overall.
- GMV is a clean low-volatility baseline after decoupling and clean rerun.
