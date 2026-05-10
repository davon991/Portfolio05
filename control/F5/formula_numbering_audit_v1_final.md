# formula_numbering_audit_v1_final.md

## 1. 审查对象

本轮审查：

- `problem_statement_ru_cn_v5_optimal.md`
- `section_01_classic_models_ru_cn_v4.md`

审查目标：

1. 是否需要加入公式编号；
2. 哪些公式应编号；
3. 哪些公式不应编号；
4. 是否需要进一步优化文字连贯性。

---

## 2. 对 `Постановка задачи` 的判断

该部分位于正式编号章节之前。若给所有公式编号，会出现不自然的 (0.1)、(0.2)，也容易导致全稿编号混乱。

因此最优做法是：

- 不给普通定义编号；
- 只给核心优化问题加标签。

应加标签：

1. CtR–CtB 硬约束问题：\((P)\)；
2. penalty / soft-constrained problem：\((P_\rho)\)。

理由：

- 这两个问题后续模型章节和求解器章节会引用；
- 它们是核心研究问题；
- 使用问题标签比使用普通编号更自然。

不编号：

- \(r_t\)；
- \(\Sigma\)；
- \(\mathcal X\)；
- \(\sigma_p(x)\)；
- CtR / CtB / \(D_R\) / \(D_B\) 的简短定义。

这些定义后续会在专门章节中正式推导和编号。

---

## 3. 对 `Раздел 1` 的判断

`Раздел 1` 是经典背景章节，不宜大量编号。最优做法是只编号 Markowitz 中真正服务后文的公式。

应编号：

1. Markowitz 主优化问题：\((1.1)\)；
2. GMV 闭式解：\((1.2)\)。

理由：

- Markowitz 主问题是经典组合优化的出发点；
- GMV 是后文 baseline，可在实验和结果章节引用。

不编号：

- Tobin 资本市场线；
- Tobin Sharpe ratio；
- Sharpe 单指数模型；
- Sharpe 协方差矩阵形式。

理由：

- 它们是理论背景，不是后文直接使用的模型；
- 编号过多会削弱 CtR–CtB 主线。

---

## 4. 当前推荐更新

新增：

- `problem_statement_ru_cn_v6_formula_ref_final.md`
- `section_01_classic_models_ru_cn_v5_formula_ref_final.md`

这两个文件只做公式编号/引用层面的最小更新，不改变数学模型。
