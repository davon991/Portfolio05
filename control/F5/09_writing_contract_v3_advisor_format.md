# 09_writing_contract_v3_advisor_format.md

## 0. Purpose
This file updates the writing contract after the advisor's email. It does not change the CtR–CtB research model. It converts the existing chapter draft package into a dissertation-ready structure that satisfies the department formatting rule.

## 1. Advisor requirements incorporated

### 1.1 Add course work into the dissertation
The previous course work on Markowitz, Tobin, and Sharpe must be integrated into the dissertation. It should not be attached as an unrelated old paper. It should be rewritten as part of the theoretical background.

Final placement:
- Chapter 2: Markowitz model, Tobin risk-free asset extension, Sharpe one-index model.
- Optional appendix: short note explaining that the course-work material was reused and adapted.
- Bibliography: keep the core Markowitz, Tobin, Sharpe references.

### 1.2 Program listings in appendix
All main program listings must be placed in the appendix, not in the main text.

Main text:
- Describe algorithms and give formulas.
- Give calculation examples, tables, and figures.
- Do not paste long code blocks.

Appendix:
- Listing A.1: `src/ctrctb/models/metrics.py`
- Listing A.2: `src/ctrctb/models/objectives.py`
- Listing A.3: `src/ctrctb/models/strategies.py`
- Listing A.4: `src/ctrctb/solvers/core.py`
- Listing A.5: `src/ctrctb/models/gmv.py`
- Listing A.6: `src/ctrctb/exports/results.py`
- Listing A.7: selected runner scripts:
  - `scripts/run_experiment.py`
  - `scripts/run_calibration.py`
  - `scripts/run_inference.py`
  - `scripts/aggregate_solver_reliability.py`
  - `scripts/build_figures_final_v2.py`
  - `scripts/build_tables_final_v2.py`

### 1.3 Calculation examples must stay in main text
Do not move all empirical outputs to appendix. The main text must contain:
- Table 7.1 calibration screening summary.
- Figure 7.1 calibration heatmap.
- Table 8.1 performance and trading.
- Table 8.2 structural mechanism summary.
- Table 8.3 solver reliability summary.
- Figures 8.1–8.4.
- At least one worked interpretation example for Main vs CtR-only.

### 1.4 Introduction must contain literature review
Chapter 1 must be rewritten so that it includes:
- research background;
- numbered literature references [1], [2], ...;
- what each section contains.

### 1.5 Conclusion must list what was done
Chapter 9 must be rewritten into point-by-point conclusions:
1. The theoretical background was organized.
2. CtR and CtB were defined in one notation system.
3. A coordinated model was formulated.
4. A unified solver was implemented.
5. ETF data experiments were performed.
6. Calibration and robustness checks were conducted.
7. Statistical inference and solver diagnostics were reported.
8. Program listings were placed in the appendix.

## 2. Final dissertation structure

### Title page
Title must exactly match the title submitted to the academic office. If the submitted title is still unknown, use a placeholder and replace it before final submission.

### Introduction
Must include literature review and section-by-section description.

### Problem statement
Add a separate section after Introduction:
- object of study;
- input data;
- decision variable;
- risk and structure objects;
- main optimization problem;
- expected outputs.

### Numbered chapters
1. Introduction
2. Problem statement and theoretical background
3. CtR foundation
4. CtB foundation
5. Coordinated CtR–CtB model
6. Solver and implementation
7. Experimental design and calibration
8. Out-of-sample results and mechanism interpretation
9. Conclusion

### Appendix
- Supplementary tables.
- Reproducibility chain.
- Program listings.

## 3. Formula style rules
- Number only formulas that are referenced later.
- Formula numbers must not be inside formula boxes.
- Do not insert formulas as pictures.
- Long formulas should be displayed.
- Text following formulas must use punctuation correctly.
- Do not use informal abbreviations.

## 4. Bibliography
The final list must contain at least 10 sources. Minimum accepted set:
1. Markowitz (1952)
2. Tobin (1958)
3. Sharpe (1964)
4. Qian (2006)
5. Maillard, Roncalli, Teiletche (2010)
6. Roncalli (2013)
7. Choueifaty, Coignard (2008)
8. Menchero, Davis (2011)
9. Ledoit, Wolf (2004)
10. DeMiguel, Garlappi, Uppal (2009)
11. White (2000)
12. Bailey, López de Prado (2014)
13. Nocedal, Wright (2006)

## 5. Non-negotiable wording discipline
The thesis must not claim:
- Main is the universal best-performing strategy.
- Main significantly dominates EW or GMV in return.
- d04 is better than d08.
- CtB improves every dimension simultaneously.

The thesis may claim:
- Main is the thesis model because it implements CtR as primary objective and CtB as structural constraint.
- Main significantly improves structural metrics targeted by the thesis.
- The trade-off is interpretable: lower D_B with higher D_R and higher turnover relative to CtR-only.
- The solver and clean-lineage evidence support numerical reliability.
