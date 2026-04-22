# Inference notes

Run: `full__main__test__20260419__01`

- Bootstrap type: moving block bootstrap
- Block size: 6 months
- Bootstrap replications: 5000
- Main strategy: Main
- Benchmarks: CtR-only, CtB-only, EW, GMV

Interpretation rule:
- For `D_R`, `D_B`, `band_active`, `band_violation`, and `turnover`, negative mean differences are favorable for Main.
- For `period_return`, positive mean differences are favorable for Main.
- Use `p_one_sided` for directional claims and `ci_95_*` for uncertainty reporting.
