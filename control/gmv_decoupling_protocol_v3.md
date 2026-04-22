# GMV Decoupling Protocol v3

Status: F3 rolling update after full-stage GMV recheck

## Outcome
The dedicated GMV implementation has now been rechecked on both:
- `minimal_real__main__trainval__20260419__01__gmvfix`
- `full__main__test__20260419__01__gmvfix`

## Full-stage result
The full-stage recheck removed the prior GMV partial months entirely.

- Previous full GMV solver status: 44 success, 15 partial
- Rechecked full GMV solver status: 59 success, 0 partial

## Interpretation rule
GMV may now be retained as a legitimate low-volatility baseline in the main text.
However, it still should not replace the Main model as the thesis centerpiece, because the thesis objective is not "minimum volatility at all costs", but CtR-primary allocation under CtB structural control.

## Writing consequence
The solver caveat attached to GMV should be downgraded from:
- "full-stage numerical warning"

to:
- "previous implementation caveat, resolved by dedicated GMV implementation"

## Remaining action
Keep one short note in the empirical chapter:
- GMV is implemented separately from the unified CtR/CtB solver stack.
- This design choice is intentional because GMV is a standard long-only convex quadratic baseline with its own dedicated numerical routine.
