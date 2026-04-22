# 06_model_contract.md

## 1. 文件目的与当前状态

本文件用于冻结本项目的**模型层**，回答以下问题：

1. 本项目到底把什么当作 CtR 主目标；
2. 本项目到底把什么当作 CtB 结构约束对象；
3. CtR-only、CtB-only 与主模型三者之间是什么关系；
4. 哪些是理论对象，哪些是经验实现对象，哪些只是数值实现形式；
5. 参数如何分层，哪些可以校准，哪些不得随意改动。

本文件不负责：

- 数据下载与清洗细节（由 `05_data_contract.md` 管理）；
- 求解器实现细节（由 `07_solver_contract.md` 管理）；
- 基准梯队与比较制度（由 `06A_baseline_ladder.md` 管理）；
- 统计显著性与过拟合防护（由 `08A_statistical_validation.md` 管理）。

**当前状态**：F2 freeze  
**冻结说明**：已与 `06A_baseline_ladder.md`、`07_solver_contract.md` 和 `08_result_contract.md` 对齐，本轮进入 F2 freeze。

---

## 2. 上位约束与依赖文件

本文件完全服从以下已冻结文件：

- `00_project_charter.md`
- `01_notation_master.md`
- `02_definition_formula_ledger.md`
- `03_thesis_skeleton.md`
- `03A_contribution_claims.md`
- `05_data_contract.md`

因此，本文件不得改变以下已冻结事实：

1. 研究对象是 **long-only 大类资产 ETF 组合**；
2. 主权重记号为 `x`，协方差矩阵记号为 `Σ`；
3. CtR 是**风险分配对象**，CtB 是**相关结构对象**；
4. 主模型是“**CtR 主目标 + CtB 结构约束/容忍带**”；
5. 平滑项 `η` 与 `L2` 项 `γ` 的角色已冻结；
6. `δ` 是 CtB band 阈值，`ρ` 是数值罚参数，而不是经济含义参数。

---

## 3. 模型层的三层区分

为避免后续论文、代码与结果解释混乱，本项目明确区分三层对象。

### 3.1 理论对象（theoretical objects）

理论层冻结的是：

- `CtR_i(x;Σ)`
- `CtB_i(x;Σ)`
- 风险预算 `b`
- long-only 可行域 `𝒳`
- CtR 偏离对象 `D_R(x;b)`
- CtB 结构偏离对象 `D_B(x)`

理论层关心的是：

- 数学含义；
- 主从角色；
- 章节叙事；
- 命题与推导。

### 3.2 经验实现对象（empirical objects）

经验层冻结的是：

- 样本内每个调仓时点的 `Σ_t`；
- 上期权重 `x_{t-1}`；
- 主预算向量 `b`；
- band 阈值 `δ`；
- 主目标与约束的离散度函数形式。

经验层关心的是：

- 月频再平衡时到底求什么；
- 结果文件中的 `D_R`、`D_B` 如何解释；
- 主模型与基准模型如何可比较。

### 3.3 数值实现对象（numerical forms）

数值层冻结的是：

- 软约束惩罚表达；
- `ρ` 的作用；
- warm start / continuation / fallback 需要的辅助形式。

数值层关心的是：

- solver 是否稳；
- 约束如何被实现；
- 失败时如何回退；
- diagnostics 如何记录。

---

## 4. 主可行域与基本输入

### 4.1 主可行域

本项目主模型和主基准默认都定义在 long-only simplex 上：

\[
\mathcal{X}
=
\left\{
 x\in\mathbb{R}^n:
 x_i\ge 0,\ \sum_{i=1}^n x_i=1
\right\}.
\]

### 4.2 主输入

在每个调仓时点 `t`，模型层的主输入固定为：

- 年化协方差矩阵 `Σ_t`；
- 上期权重 `x_{t-1}`；
- 风险预算向量 `b`；
- 校准参数 `δ, η`；
- 数值参数 `γ, ρ`。

### 4.3 主预算向量

主论文的默认预算向量固定为：

\[
b_i = \frac{1}{n},\quad i=1,\dots,n.
\]

也就是说，主文中的 CtR 配置主线默认采用 **equal budget**。  
非等预算只允许进入 robustness / appendix，不得替代主结果。

---

## 5. CtR 与 CtB 的基础对象

### 5.1 标准化 CtR 份额

定义组合波动率为：

\[
\sigma_p(x)=\sqrt{x^\top \Sigma x}.
\]

定义第 `i` 个资产的 CtR 为：

\[
\mathrm{CtR}_i(x;\Sigma)=\frac{x_i(\Sigma x)_i}{\sigma_p(x)}.
\]

进一步定义**标准化风险贡献份额**：

\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)
:=
\frac{\mathrm{CtR}_i(x;\Sigma)}{\sigma_p(x)}
=
\frac{x_i(\Sigma x)_i}{x^\top \Sigma x}.
\]

则有：

\[
\sum_{i=1}^n \widetilde{\mathrm{CtR}}_i(x;\Sigma)=1.
\]

这使 `CtR` 与预算向量 `b` 可直接比较。

### 5.2 CtB 对象

定义第 `i` 个资产与组合的相关系数为：

\[
\mathrm{CtB}_i(x;\Sigma)
:=
\rho_{i,p}(x;\Sigma)
=
\frac{(\Sigma x)_i}{\sigma_i\,\sigma_p(x)},
\quad
\sigma_i=\sqrt{\Sigma_{ii}}.
\]

`CtB` 在本项目中不是“风险份额”，而是**资产与组合之间的相关结构量**。

---

## 6. CtR 离散度函数的最终冻结

### 6.1 主定义

本项目将 CtR 离散度函数最终冻结为：

\[
D_R(x;b)
:=
\frac{1}{2}
\sum_{i=1}^n
\left(
\widetilde{\mathrm{CtR}}_i(x;\Sigma)-b_i
\right)^2.
\]

### 6.2 选择该形式的理由

选择该形式，而不是把主经验模型直接写成对数势函数，有 5 个原因：

1. **与预算含义直接对齐**：`D_R` 直接衡量标准化风险贡献份额相对预算 `b` 的偏离；
2. **结果解释直接**：`D_R = 0` 恰好表示风险预算完全对齐；
3. **图表友好**：`D_R` 可直接进入 `dr_db_timeseries.csv` 与 `objective_terms.csv`；
4. **主模型角色清晰**：它天然适合作为“主配置偏离”的量；
5. **与 long-only 实证契合**：在 simplex 上容易解释，不依赖额外尺度参数。

### 6.3 解释边界

本项目承认：该 `D_R` 一般**不是全局凸函数**。  
因此，本论文并不声称主模型是一个全局凸优化问题；相反，后续 `07_solver_contract.md` 会明确把该问题视为带有非线性结构、需要良好 warm start 与诊断输出的 constrained nonlinear program。

### 6.4 报告口径冻结

后续结果文件中：

- `dr_db_timeseries.csv` 的 `D_R` 字段；
- `objective_terms.csv` 的 `dr_term` 字段；

都统一对应本节定义的 `D_R(x;b)`，不得再改成别的 CtR gap 形式。

---

## 7. CtB 离散度函数的最终冻结

### 7.1 主定义

定义 CtB 的横截面均值为：

\[
\overline{\mathrm{CtB}}(x;\Sigma)
:=
\frac{1}{n}
\sum_{i=1}^n \mathrm{CtB}_i(x;\Sigma).
\]

本项目将 CtB 离散度函数最终冻结为：

\[
D_B(x)
:=
\frac{1}{2}
\sum_{i=1}^n
\left(
\mathrm{CtB}_i(x;\Sigma)-\overline{\mathrm{CtB}}(x;\Sigma)
\right)^2.
\]

### 7.2 选择该形式的理由

选择该形式，而不是直接解“所有 CtB 完全相等”的非线性方程组作为主经验模型，有 6 个原因：

1. **语义一致**：它直接度量“相关结构是否趋于一致”；
2. **与 long-only 主模型兼容**：可自然写入约束或容忍带；
3. **结果解释清楚**：`D_B` 越小，表示 CtB 横截面越集中；
4. **不把 CtB 误写成主目标**：作为 band 约束量更自然；
5. **有利于图表与诊断**：可直接形成 `D_R–D_B` 双机制图；
6. **避免经验主模型过度依赖特殊方程组解法**。

### 7.3 为何采用等权横截面均值

本项目的主 `D_B` 使用**等权横截面均值**，而不是按 `x_i` 加权的均值，原因是：

1. 本文讨论的是整个资产宇宙的结构一致性，而不是只讨论大权重资产之间的结构；
2. 若用 `x_i` 加权，模型可能通过把某些难以匹配的资产权重压到很小来“规避”结构约束；
3. 对 fixed ETF universe 的 thesis 场景，等权横截面 dispersion 更利于答辩解释。

### 7.4 解释边界

本项目不宣称 `D_B=0` 总能在给定 long-only simplex 上实现；  
主文只声称：`D_B` 是一个可解释的**相关结构偏离度量**，可用于约束、band 与机制分析。

### 7.5 报告口径冻结

后续结果文件中：

- `dr_db_timeseries.csv` 的 `D_B` 字段；
- `objective_terms.csv` 的 `band_penalty` 所依赖的底层对象；

都统一对应本节定义的 `D_B(x)`。

---

## 8. 理论章节中的辅助对象与经验主模型的关系

为保持与笔记中的理论路线一致，本项目承认以下辅助对象在理论上是重要的：

\[
\Phi_R(x; b, \tau)
=
\frac{1}{2}x^\top \Sigma x
-
\tau \sum_{i=1}^n b_i \log x_i,
\quad x_i>0.
\]

该类对象在笔记中与 risk budgeting / ERC 的构造、强凸性与“先梯度后牛顿”的算法主线有关。  
但本项目明确区分：

- **理论章节**可以使用 `\Phi_R` 讨论 CtR-only 的构造与性质；
- **经验主模型**统一使用本文件冻结的 `D_R(x;b)` 与 `D_B(x)`；
- 不允许把理论辅助势函数与经验主结果中的 `D_R` 混成一个对象。

这一步是为了同时满足：

1. 对笔记理论路线的忠实；
2. 对实证模型可解释性的需要；
3. 对结果文件口径统一的要求。

---

## 9. 三类模型的正式冻结

### 9.1 CtR-only 基准模型

CtR-only 基准模型冻结为：

\[
\min_{x\in\mathcal{X}}
D_R(x;b)
+
\eta \|x-x_{t-1}\|_2^2
+
\gamma \|x\|_2^2.
\]

解释：

- `D_R` 负责风险预算对齐；
- `η` 控制换手与权重跳变；
- `γ` 负责数值稳定和轻度分散化。

### 9.2 CtB-only 基准模型

CtB-only 基准模型冻结为：

\[
\min_{x\in\mathcal{X}}
D_B(x)
+
\eta \|x-x_{t-1}\|_2^2
+
\gamma \|x\|_2^2.
\]

解释：

- 它不是主文推荐策略；
- 它的角色是作为“只看相关结构”的对照基准；
- 它帮助说明“为什么 CtB 更适合作为结构层，而不是单独主导配置”。

### 9.3 主模型（硬约束形式）

主模型的正式定义冻结为：

\[
\begin{aligned}
\min_{x\in\mathcal{X}} \quad
& D_R(x;b)
+ \eta \|x-x_{t-1}\|_2^2
+ \gamma \|x\|_2^2 \\
\text{s.t.} \quad
& D_B(x) \le \delta.
\end{aligned}
\]

这是论文主文中的**规范性主模型**。

### 9.4 主模型（软约束实现形式）

为便于数值求解，主模型允许采用如下软约束实现：

\[
J(x)
=
D_R(x;b)
+ \eta \|x-x_{t-1}\|_2^2
+ \gamma \|x\|_2^2
+ \frac{\rho}{2}\,[D_B(x)-\delta]_+^2,
\]

其中

\[
[z]_+ := \max(z,0).
\]

### 9.5 主从关系冻结

本项目明确冻结以下主从关系：

1. `D_R` 是主目标；
2. `D_B` 是结构约束对象；
3. `δ` 决定允许的结构偏离上界；
4. `ρ` 只是数值实现参数，不得被解释为经济偏好参数。

这条主从关系后续不得改成：

- 对称双目标；
- `λ D_R + (1-λ)D_B` 这类混合权重主模型；
- 以 CtB 为主目标、CtR 为附属项的主文结构。

这些形式最多只能在 robustness / appendix 中作为对照，不得覆盖主模型口径。

---

## 10. 参数分层冻结

### 10.1 结构参数（不作为常规校准对象）

以下参数或设定视为**结构参数**：

- 资产宇宙（10 ETF）
- long-only simplex 可行域
- 主预算 `b_i = 1/n`
- 月频再平衡
- `D_R` 的函数形式
- `D_B` 的函数形式

结构参数默认不在主文中反复调。

### 10.2 校准参数（经济/制度层）

以下参数视为**校准参数**：

- `δ`：CtB 允许偏离上界；
- `η`：平滑/换手控制强度。

它们需要进入 validation-driven calibration。

### 10.3 数值参数（实现层）

以下参数视为**数值参数**：

- `γ`：轻度正则项；
- `ρ`：band 软约束罚参数。

它们的主要作用是：

- 稳定求解；
- 改善收敛；
- 避免病态或边界震荡。

论文解释中不得把它们包装成经济洞见参数。

---

## 11. 模型层接受与拒绝的表达

### 11.1 接受的主表达

本项目接受以下表达作为**主文标准表达**：

- CtR-only：`min D_R + smooth + l2`
- CtB-only：`min D_B + smooth + l2`
- Main：`min D_R + smooth + l2 s.t. D_B <= δ`
- Soft Main：`D_R + smooth + l2 + penalty`

### 11.2 允许进入 robustness / appendix 的表达

以下表达允许作为附录或 robustness：

- 非等预算 `b`
- box constraints
- 替代协方差估计器
- pure penalty vs exact-constraint 的比较
- CtR 理论辅助势函数 `Φ_R`

### 11.3 拒绝作为主文标准模型的表达

以下表达明确拒绝作为主文标准模型：

1. `λ D_R + (1-λ) D_B` 型对称双目标；
2. 直接把 CtB-only 说成“第二种风险平价”；
3. 把 `ρ` 解释成经济偏好权重；
4. 在没有说明的情况下改变 `D_R` 或 `D_B` 定义；
5. 在主文中随意引入收益预测项，导致论文从结构配置问题漂向 alpha 预测问题。

---

## 12. 与数据契约的接口

在每个再平衡时点 `t`，模型层的调用接口应理解为：

**输入**：

- `date_t`
- `asset_list`
- `cov_t = Σ_t`
- `x_prev = x_{t-1}`
- `budget = b`
- `delta`
- `eta`
- `gamma`
- `rho`

**输出**：

- `x_t`
- `D_R(x_t;b)`
- `D_B(x_t)`
- `band_active_t = 1{D_B(x_t) > δ}` 或基于 solver diagnostics 的等价判定
- 各项 objective terms
- solver diagnostics 句柄

---

## 13. 与后续文件的依赖关系

### 13.1 对 `06A_baseline_ladder.md` 的约束

`06A_baseline_ladder.md` 必须以本文件冻结的三类模型为核心层：

- CtR-only
- CtB-only
- Main

其余 EW / GMV / MDP 等基准只能围绕它们构成比较梯队，不能反过来改变本文件中的主模型表达。

### 13.2 对 `07_solver_contract.md` 的约束

`07_solver_contract.md` 必须接受本文件作为 solver target definition：

- 先梯度后牛顿；
- 覆盖 CtR-only、CtB-only、Main；
- 支持 exact-constraint 与 soft-constraint；
- diagnostics 中必须回报 `D_R`、`D_B`、feasibility 与 stationarity。

### 13.3 对 `08_result_contract.md` 的约束

后续结果契约至少要固定以下字段：

- `dr_db_timeseries.csv`：`date, strategy, D_R, D_B, band_active`
- `objective_terms.csv`：`date, strategy, obj_total, dr_term, smooth_term, l2_term, band_penalty`
- `ctr_long.csv`
- `ctb_long.csv`

---

## 14. 论文叙事上的冻结措辞

主文在描述本模型时，应优先使用以下措辞：

- “CtR 主目标 + CtB 结构约束”
- “风险配置主轴 + 相关结构监管层”
- “coordination model”
- “band-constrained CtR allocation”

避免使用以下容易引起误解的措辞：

- “双平价完全对称优化”
- “CtB 就是另一种风险贡献”
- “模型自动提升收益”
- “γ / ρ 反映经济偏好”

---

## 15. 当前冻结结论

本文件在当前阶段正式冻结以下 F2 内容：

1. `D_R(x;b)` 的正式经验定义；
2. `D_B(x)` 的正式经验定义；
3. CtR-only、CtB-only、主模型的正式表达；
4. 主模型的软约束实现形式；
5. 参数分层：结构 / 校准 / 数值；
6. 主从关系：CtR 主目标，CtB 结构约束。

本文件暂不冻结以下内容：

1. solver 的具体 stop rule 与 fallback 逻辑；
2. baseline 梯队的完整清单；
3. `δ, η, γ, ρ` 的最终数值选择；
4. statistical validation 的正式检验流程。

