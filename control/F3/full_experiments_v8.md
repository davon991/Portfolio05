# full_experiments_v8

## Status
F3 rolling update after clean-rerun robustness confirmation.

## Confirmed clean full runs
### Main specification
- Run ID: `full__main__test__20260419__01`
- Parameters: `delta=0.02`, `eta=0.05`, `gamma=0.001`, `rho=100.0`

### Robustness specification
- Run ID: `full__robust__d04__20260419__01`
- Parameters: `delta=0.01`, `eta=0.05`, `gamma=0.001`, `rho=100.0`

## Final interpretation freeze
The clean rerun confirms the intended strict-band robustness pattern:
- `d04` reduces `D_B` further than `d08`
- `d04` increases `D_R` relative to `d08`
- `d04` increases turnover relative to `d08`

Therefore:
- `d08` remains the **main specification**
- `d04` remains the **strict-band robustness specification**

## Comparison summary to cite
Relative to clean `d08`, clean `d04` shows:
- lower `db_mean`
- higher `dr_mean`
- higher `turnover_mean`
- no increase in failure rate

## Writing rule
Do not re-select the main specification on the test set.
Test-set comparison between `d08` and `d04` is interpreted as robustness evidence, not model-selection evidence.
