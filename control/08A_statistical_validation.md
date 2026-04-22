# 08A_statistical_validation.md

## 1. 文件目的与当前状态

本文件用于冻结本项目的**统计验证契约（statistical validation contract）**，回答以下问题：

1. 哪些结果可以被描述为“主要证据”，哪些只能作为辅助证据；
2. 参数选择、模型比较、图表解读与最终结论分别依赖什么统计口径；
3. 如何隔离 calibration 与 final evaluation，避免 test leakage；
4. 如何处理多重比较、时间序列相关、非正态收益与回测选择偏差；
5. 哪些统计结论可以进入正文，哪些只能进入附录或稳健性分析；
6. 如何把统计验证结果写入 `analysis/`、`diagnostics/` 和 `tables/`。

本文件不负责：

- 主模型、基准模型与参数定义（由 `06_model_contract.md` 与 `06A_baseline_ladder.md` 管理）；
- 结果目录与字段命名（由 `08_result_contract.md` 管理）；
- 单次实验登记（由 `experiment_registry.md` 管理）；
- 章节文字写作（由 `chapter drafting` 与 `defense_qa_bank.md` 管理）。

**当前状态**：F2 freeze

---

## 2. 上位约束与依赖文件

本文件完全服从以下文件：

- `00_project_charter.md`
- `01_notation_master.md`
- `02_definition_formula_ledger.md`
- `03_thesis_skeleton.md`
- `03A_contribution_claims.md`
- `05_data_contract.md`
- `06_model_contract.md`
- `06A_baseline_ladder.md`
- `07_solver_contract.md`
- `08_result_contract.md`

因此，本文件不得改变以下既定事实：

1. 本文的主张不是“追求最高收益”，而是展示 **CtR 主目标 + CtB 结构约束** 的机制作用；
2. 主宇宙为 long-only 大类资产 ETF，主频率为日频估计、月频调仓；
3. 主比较策略集合固定为 `EW / GMV / CtR-only / MDP / CtB-only / Main`；
4. `D_R(x;b)` 与 `D_B(x)` 的经验定义已经在 `06_model_contract.md` 中冻结；
5. 任何统计比较都必须基于 **out-of-sample** 结果，不得用 test 结果反向调参；
6. 任何统计显著性表述都必须可追溯到 `analysis/` 或 `diagnostics/` 中的固定文件。

---

## 3. 统计验证总原则

### 3.1 机制优先于收益冠军

本项目的统计验证优先级为：

1. **机制证据**：`D_R`、`D_B`、band 激活率、CtR/CtB 结构图是否支持主模型解释；
2. **实现质量证据**：收敛率、KKT 残差、失败率、fallback 频率是否可接受；
3. **组合绩效证据**：波动率、回撤、换手、Sharpe 等是否在合理范围内；
4. **显著性证据**：关键差异是否在稳健统计口径下成立。

因此，禁止把“收益更高”写成唯一或首要结论。

### 3.2 分层证据制度

所有统计结论分为三层：

- **Tier 1: Primary evidence**：可进入正文主结论；
- **Tier 2: Supporting evidence**：可进入正文补充或附录主表；
- **Tier 3: Exploratory evidence**：只能作为探索性或启发性结果，不能写成确定结论。

### 3.3 校准与最终评估严格分离

- `train`：允许估计风险模型、构建初始经验与做方法开发；
- `validation`：允许做参数筛选、规则筛选、失败治理调优；
- `test`：只允许做最终锁定后的一次性或登记式评估；
- `full sample`：只允许用于图形展示、补充说明或 ex-post 描述，不能替代 final test evidence。

### 3.4 无登记，不进入主结论

未在 `experiment_registry.md` 中登记的 run：

- 不能进入正文主表；
- 不能用来支持正式参数选择；
- 只能作为临时开发或 debug 记录。

---

## 4. 研究假设与验证层次

### 4.1 主研究问题对应的统计对象

本项目的主要研究问题不是“Main 是否在所有指标上都显著优于所有基准”，而是：

- `RQ1`：Main 是否比 `CtR-only` 更有效地控制 `D_B`，同时保持 `D_R` 在可接受水平；
- `RQ2`：Main 是否比 `CtB-only` 具有更稳定、可解释的风险配置；
- `RQ3`：Main 相比 `MDP` 是否体现出不同的相关结构控制逻辑；
- `RQ4`：Main 的实现质量（收敛、失败率、band 约束行为）是否可接受；
- `RQ5`：Main 的绩效代价是否在可接受范围内，而不是通过极端换手或不稳定权重换取表面改善。

### 4.2 Primary hypotheses（可进入正文）

正文主假设固定为：

- `H1`：相对 `CtR-only`，Main 的 out-of-sample `D_B` 均值更低或更受控；
- `H2`：相对 `CtB-only`，Main 的 out-of-sample `D_R` 均值更低或更接近预算目标；
- `H3`：Main 的 band 激活逻辑与 `D_R–D_B` 联动图支持“CtR 主导、CtB 监管”的机制解释；
- `H4`：Main 的 solver 可实现性与稳定性达到可报告标准；
- `H5`：Main 的绩效并未通过不可接受的 turnover 或失败率换取。

### 4.3 Secondary hypotheses（可进入附录或辅助分析）

- `H6`：Main 的 Sharpe、max drawdown、ann_vol 等相对若干基准存在改善；
- `H7`：Main 在某些市场阶段表现出更明显的结构控制特征；
- `H8`：Main 与 `MDP`、`GMV` 的差异可由相关结构与风险预算逻辑解释。

### 4.4 Exploratory hypotheses（不得写成主结论）

- “Main 在所有窗口都最优”；
- “Main 的收益显著更高”；
- “Main 普遍战胜所有经典资产配置方法”。

---

## 5. 样本切分与评估纪律

### 5.1 固定切分

主切分制度服从 `05_data_contract.md`：

- warm-up：风险估计预热；
- train：方法开发与初始筛选；
- validation：参数筛选与规则冻结；
- test：最终比较。

### 5.2 参数冻结时间点

以下对象必须在 final test 前冻结：

- 主宇宙；
- 收益口径；
- 协方差估计器；
- 基准集合；
- 参数搜索网格；
- 接受/拒绝规则；
- 主要图表清单；
- primary hypotheses。

### 5.3 不允许的行为

禁止：

- 看过 test 结果后扩大或缩小参数网格；
- 看过 test 结果后替换主比较基准；
- 因个别指标不理想而改写 primary endpoint；
- 以 full sample 图形结果反向修改 final narrative。

---

## 6. 主要统计端点（primary endpoints）

正文中正式统计比较的 primary endpoints 固定为：

1. `mean_D_R_oos`
2. `mean_D_B_oos`
3. `band_active_rate_oos`
4. `turnover_mean_oos`
5. `failure_rate_oos`

这些端点直接服务 `03A_contribution_claims.md` 中的 `C2 / C3 / C4 / C5`。

### 6.1 主要绩效端点（secondary performance endpoints）

作为辅助端点使用：

- `ann_return`
- `ann_vol`
- `sharpe`
- `max_drawdown`
- `sortino`
- `calmar`
- `turnover_p95`

这些指标可以进入正文表格，但不得盖过 primary endpoints 的解释优先级。

### 6.2 结构解释端点（mechanism endpoints）

用于图表与机制段落：

- `ctb_dispersion_path`
- `ctr_dispersion_path`
- `D_R–D_B frontier`
- `band_violation_rate`
- `weights_vs_risk_share_gap`
- regime-conditioned `D_B` / `D_R` differences

---

## 7. 统计推断方法：最低强制层与增强层

### 7.1 最低强制层（必须实现）

对于正文 primary endpoints，至少必须报告：

1. out-of-sample 点估计；
2. moving-block bootstrap 或 stationary bootstrap 置信区间；
3. 相对主对照对象的 paired difference 置信区间；
4. 两侧 p-value 或等价显著性判断；
5. 多重比较调整后的结论标签。

### 7.2 增强层（强烈建议实现）

若时间与实现允许，建议额外报告：

1. **Probabilistic Sharpe Ratio (PSR)**；
2. **Deflated Sharpe Ratio (DSR)**；
3. **White Reality Check** 或 **Hansen SPA**，用于处理多参数/多策略搜索偏差；
4. regime bootstrap / subperiod robustness；
5. leave-one-asset-class-out robustness。

### 7.3 Why bootstrap, not naive IID t-test

由于本项目收益序列与 `D_R / D_B / turnover` 路径都具有：

- 时间相关；
- 重叠窗口效应；
- 非正态性；
- 尾部不对称；

正文正式比较**默认不得使用单纯 IID 正态 t 检验作为唯一依据**。

---

## 8. 配对比较制度

### 8.1 主比较对象

正文正式配对比较固定为：

1. `Main vs CtR-only`
2. `Main vs CtB-only`
3. `Main vs MDP`
4. `Main vs GMV`
5. `Main vs EW`

### 8.2 主要比较矩阵

对于每一组主比较，至少对以下差值进行统计推断：

- `Δ mean_D_R_oos`
- `Δ mean_D_B_oos`
- `Δ turnover_mean_oos`
- `Δ failure_rate_oos`
- `Δ sharpe`
- `Δ max_drawdown`

### 8.3 配对单位

主配对单位优先为：

- 再平衡日期层面的 out-of-sample observations；或
- rolling window 层面的 strategy-level summary differences。

禁止把不同时间段、不同 run、不同参数集的结果拼成伪配对样本。

---

## 9. 多重比较与错误发现控制

### 9.1 主文固定校正方法

对于正文 primary hypotheses 的多重比较，默认使用：

- **Holm-Bonferroni** 作为主校正方法；
- `q-value / Benjamini-Hochberg` 可作为附录补充。

### 9.2 校正范围

以下对象必须纳入同一校正族：

- 所有正文 primary pairwise comparisons；
- 所有正文 primary endpoints；
- 所有正式声明为“显著”的 test-based claims。

### 9.3 不校正的例外

探索性图形、单一描述性 summary、toy experiments 的说明性输出，可以不做多重校正，但必须明确标注为 exploratory。

---

## 10. 参数搜索偏差与回测选择偏差控制

### 10.1 参数筛选纪律

`delta / eta` 属于校准参数；`gamma / rho` 属于数值参数。主校准与筛选必须发生在 `validation` 上，而不是 `test` 上。

### 10.2 防止 specification search 的最低要求

至少必须做到：

1. 预先写入参数网格或生成规则；
2. 写明接受/拒绝标准；
3. 在 `experiment_registry.md` 中登记尝试过的组合；
4. 保留被拒绝组合的原因摘要；
5. test 集上只评估 final locked candidates。

### 10.3 增强要求

若进行大规模搜索，应额外采用：

- White Reality Check；或
- Hansen SPA；或
- DSR/PSR + familywise 控制的组合口径。

### 10.4 不允许的叙述

禁止写：

- “我们测试了很多参数，最终选了效果最好的”；
- “test 上表现最好的就是最优参数”；
- “因为图更好看，所以把该组合写进正文”。

---

## 11. 稳健性分析最小集合

正式 full experiments 至少要做以下稳健性分析：

1. **样本期稳健性**：train/validation/test 子区间 + 至少一个 stress subperiod；
2. **协方差估计稳健性**：主估计器 vs 一个替代估计器；
3. **参数稳健性**：围绕 final `(delta, eta)` 的局部网格；
4. **交易稳健性**：加入轻度线性交易成本或 turnover penalty 敏感性；
5. **宇宙稳健性**：剔除一个资产类别后的留一类检验；
6. **solver 稳健性**：初值与 fallback 触发统计。

这些稳健性结果优先进入附录，但若其中直接支持主张，可在正文摘要呈现。

---

## 12. toy / minimal / full 三类 run 的统计要求

### 12.1 synthetic / toy experiments

目标：验证机制，不追求收益统计显著性。

必须报告：

- 特殊协方差结构下的解析或半解析直觉；
- `D_R` / `D_B` 路径；
- 求解器收敛和边界行为；
- 说明性图表。

toy results 默认标记为 **mechanism evidence**，不用于收益优越性声称。

### 12.2 minimal real ETF run

目标：验证数据管线、求解器、结果输出与基本机制是否闭环。

必须报告：

- `summary_metrics.csv`
- `dr_db_timeseries.csv`
- `solver_diagnostics.csv`
- 核心 warning 与 failure log

此阶段可以做初步 bootstrap summary，但不得当作正式最终检验。

### 12.3 full experiments

目标：形成正文结果。

必须执行：

- 正式 out-of-sample 主比较；
- bootstrap CI 与 paired difference inference；
- multiple-testing adjustment；
- 至少一类 selection-bias 防护；
- 正文与附录结果分层。

---

## 13. 统计结论语言模板

### 13.1 可以使用的表述

- “在 out-of-sample test 上，Main 相对 CtR-only 的 `D_B` 均值更低，且差值区间主要位于 0 以下。”
- “Main 的 band 激活率与 `D_R–D_B` 图形共同支持 CtB 作为结构约束对象的解释。”
- “在采用 block bootstrap 与 Holm 校正后，若干主比较仍保持方向一致。”
- “Main 的绩效代价主要表现为适度换手上升，而非失败率显著恶化。”

### 13.2 必须避免的表述

- “显著优于所有方法”；
- “证明了 Main 是最优策略”；
- “收益显著提升，因此模型更好”；
- “从 full sample 图中可以证明……”。

---

## 14. 与 `08_result_contract.md` 的接口文件

本文件要求以下统计结果必须写入结果目录：

### 14.1 `analysis/stat_tests_primary.csv`

字段至少包括：

- `run_id`
- `comparison`
- `endpoint`
- `estimate_diff`
- `ci_lower`
- `ci_upper`
- `p_value_raw`
- `p_value_adjusted`
- `adjustment_method`
- `sign_label`

### 14.2 `analysis/stat_tests_secondary.csv`

用于 secondary endpoints 与稳健性比较。

### 14.3 `analysis/selection_bias_checks.csv`

字段至少包括：

- `method`
- `family`
- `num_models_considered`
- `test_stat`
- `p_value`
- `decision`
- `notes`

### 14.4 `diagnostics/inference_warnings.json`

集中记录：

- bootstrap 有效样本不足；
- block length 不稳定；
- 某些比较因失败率过高而不具可比性；
- 某些结果仅属 exploratory。

---

## 15. 进入正文的最低统计门槛

某项结论要进入正文主文本，至少必须满足：

1. 该结论服务 `C1–C5` 中至少一项正式贡献；
2. 该结论来自登记过的正式 run；
3. 该结论基于 out-of-sample 证据；
4. 该结论有对应 CI 或等价不确定性刻画；
5. 若涉及多重比较，已给出校正后结果；
6. 该结论未依赖明显的数据回看或 test 反向调参。

若不满足以上条件，则只能进入附录或探索性说明。

---

## 16. 冻结规则

### 16.1 当前冻结级别

本文件属于 **F2**，且在当前版本进入 **F2 freeze**。

### 16.2 后续允许更新的范围

后续仅允许：

- 补充具体 bootstrap 技术细节；
- 补充输出文件字段；
- 把某些增强层方法从“建议”升级为“已实现”。

后续不允许：

- 改变 primary hypotheses 的逻辑方向；
- 把收益优越性替换为主研究问题；
- 在看过 test 结果后更改 primary endpoints；
- 删除多重比较或 selection-bias 防护要求。

---

## 17. 与后续模块的衔接

本文件完成后，意味着：

1. `03A_contribution_claims.md` 可以进入 F2 freeze；
2. `08_result_contract.md` 可以进入 F2 freeze；
3. `experiment_registry.md` 必须开始承担 run 登记功能；
4. `calibration_protocol.md` 必须严格服从本文件的切分、筛选与拒绝制度；
5. `full experiments` 不得绕开本文件直接进入“挑结果”模式。

