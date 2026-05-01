# solver_reliability_protocol_v3

## Status
F3 final-freeze candidate after clean-lineage aggregation.

## Accepted aggregation scope
The accepted solver reliability aggregate includes only the clean lineage:

1. `minimal_real__main__trainval__20260419__01`
2. `calibration__main__val__20260419__01__d08`
3. `calibration__main__val__20260419__01__d04`
4. `full__main__test__20260419__01`
5. `full__robust__d04__20260419__01`

No legacy, superseded, or pre-fix runs are included.

## Final accepted conclusions

### By run type
- `minimal_real`: all strategies have success rate 1.0
- `full`: all strategies have success rate 1.0

### GMV
- GMV no longer carries partial-rate contamination in the accepted clean lineage
- GMV can now be cited as a numerically clean low-volatility baseline

### Main
- Main has success rate 1.0 in accepted clean full and minimal runs
- Main occasionally uses fallback, but not as a failure mode
- fallback is therefore interpreted as a robustness safeguard rather than as numerical breakdown

### Other strategies
- `CtR-only`, `CtB-only`, and `MDP` also achieve success rate 1.0 on the accepted clean lineage
- `MDP` and `CtB-only` show larger KKT residual scales than `CtR-only` and `Main`, but still within accepted operational bounds

## Writing rule
In the final thesis:
- cite success-rate results from the clean aggregate only
- refer to fallback as a limited safeguard mechanism
- do not cite legacy partial counts from older aggregates

## Final freeze note
This protocol is now suitable for final writing and defense use.
