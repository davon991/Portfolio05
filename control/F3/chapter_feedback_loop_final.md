# chapter_feedback_loop_final

## Status
F3 final freeze.

## Final chapter consequences

### Chapter 7 (Calibration)
Write that:
- `d08` was selected by the validation protocol as the primary specification
- `d04` was retained as the strict-band robustness specification
- test-set performance was not used to replace `d08`

### Chapter 8 (Main empirical results)
Write that:
- Main is not the raw-performance winner
- Main significantly lowers `D_B` relative to `CtR-only`
- this comes with significantly higher `D_R` and turnover
- Main significantly improves structural metrics relative to `EW` and `GMV`
- no claim of return dominance over `EW` or `GMV` is made

### Robustness paragraph
Write that:
- tightening the CtB band from `d08` to `d04` lowers `D_B` further
- but increases `D_R` and turnover
- this confirms that the band parameter has an interpretable structural role

### Solver paragraph
Write that:
- the accepted clean-lineage aggregate gives success rate 1.0 for all strategies in minimal and full stages
- GMV is numerically clean after decoupling
- limited fallback usage for Main/CtR-only should be presented as a safeguard, not as failure

## Final non-claims
Do not claim:
- Main is the best-performing strategy overall
- Main significantly beats EW or GMV in return
- CtB constraint improves every dimension simultaneously
