# defense_qa_bank_final

## Status
F3 final freeze.

## Final defense answers

### Q1. Why is Main the thesis model if EW performs better on some simple metrics?
A:
Because the thesis objective is not raw-return maximization.
Main is the model that explicitly implements CtR as the primary target and CtB as the structural constraint.
Inference confirms that Main significantly improves the structural metrics targeted by the thesis, even though it is not the return champion.

### Q2. Why keep d08 as the main specification when d04 is stricter?
A:
Because d08 was selected on the validation set under the calibration protocol.
d04 is retained as a strict-band robustness specification.
Promoting d04 after observing the test set would misuse the test set for re-selection.

### Q3. What does d04 prove?
A:
It proves that tightening the CtB band has a stable and interpretable effect:
lower `D_B`, but higher `D_R` and higher turnover.
This strengthens the structural interpretation of the model.

### Q4. Is GMV still a valid benchmark?
A:
Yes.
After decoupling and clean rerun, GMV is numerically clean and can be used as a low-volatility baseline.
But it is not the thesis model, because its objective is different.

### Q5. Can you claim statistical superiority of Main in returns?
A:
No.
The supported claim is structural superiority on the metrics targeted by the thesis, not universal return superiority.
