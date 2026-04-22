# 07_solver_contract.md

## 1. 文件目的与当前状态

本文件用于冻结本项目的**统一求解器契约（solver contract）**，回答以下问题：

1. 哪些模型需要统一进入同一求解器框架；
2. 求解器输入、输出、诊断信息如何统一；
3. “先梯度、后牛顿”的路线在本项目中如何严格实现；
4. long-only simplex 约束、CtR/CtB 非线性结构与 band 软约束如何被数值处理；
5. 若不收敛、触边严重、局部二阶信息不稳定，如何回退与记录。

本文件不负责：

- 主模型与离散度函数的数学定义（由 `06_model_contract.md` 管理）；
- 基准梯队与正文比较层级（由 `06A_baseline_ladder.md` 管理）；
- 结果导出文件清单（由 `08_result_contract.md` 管理）；
- 统计检验与过拟合防护（由 `08A_statistical_validation.md` 管理）。

**当前状态**：F2 freeze  
**冻结说明**：已与 `08_result_contract.md` 的 diagnostics 字段和结果接口对齐，本轮进入 F2 freeze。

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

因此，本文件不得改变以下已冻结事实：

1. 主研究对象是 **long-only 大类资产 ETF 组合**；
2. 主可行域是 long-only simplex；
3. 主模型的角色是 **CtR 主目标 + CtB band 约束**；
4. 经验主目标中的 `D_R(x;b)` 与 `D_B(x)` 已在 `06_model_contract.md` 冻结；
5. 算法主线必须体现笔记中的 **“先梯度、后牛顿”**，而不是直接上黑箱通用优化器；
6. 结果必须可诊断、可追溯、可进入论文与答辩，而不是只返回一个权重向量。

---

## 3. 求解器覆盖范围

### 3.1 统一求解器必须覆盖的对象

统一求解器框架必须覆盖以下三类非线性组合问题：

1. `CtR-only`
2. `CtB-only`
3. `Main`

它们统一写成：

\[
\min_{x\in\mathcal{X}} F(x;\Theta_t),
\]

其中 `Θ_t` 表示该调仓时点的全部输入（`Σ_t, x_{t-1}, b, δ, η, γ, ρ` 等）。

### 3.2 其他基准与统一接口的关系

- `EW`：不需要数值求解，但必须通过统一结果接口导出；
- `GMV`：可走专门的 QP / convex solver，也可走统一接口中的 `problem_type='gmv'` 分支；
- `MDP`：允许使用统一非线性求解框架，但不强制与主模型完全共用二阶近似；
- `IVOL` / `HRP`：若实现，走各自专门生成器，再进入统一结果导出接口。

### 3.3 本文件的主焦点

本文件主要冻结的是 **CtR-only / CtB-only / Main** 的统一 solver contract。  
也就是说，本文真正需要“先梯度、后牛顿”路线保障的，是这三类核心非线性问题。

---

## 4. 统一问题模板

### 4.1 主可行域

统一可行域为：

\[
\mathcal{X}
=
\left\{
 x\in\mathbb{R}^n:
 x_i\ge 0,\ \sum_{i=1}^n x_i=1
\right\}.
\]

### 4.2 统一目标模板

对统一 solver 而言，核心问题固定写为：

\[
F(x;\Theta_t)
=
L(x;\Theta_t)+R(x;\Theta_t),
\]

其中：

- `L(x;Θ_t)`：主结构项（如 `D_R`, `D_B`, 或其组合）；
- `R(x;Θ_t)`：规则化项（如平滑项、`L2` 项、CtB band 罚项）。

### 4.3 三类核心问题的统一写法

#### `CtR-only`

\[
F_{\mathrm{CtR}}(x)
=
D_R(x;b)+\eta \|x-x_{t-1}\|_2^2+\gamma\|x\|_2^2.
\]

#### `CtB-only`

\[
F_{\mathrm{CtB}}(x)
=
D_B(x)+\eta \|x-x_{t-1}\|_2^2+\gamma\|x\|_2^2.
\]

#### `Main`（软约束实现型）

\[
F_{\mathrm{Main}}(x)
=
D_R(x;b)+\eta \|x-x_{t-1}\|_2^2+\gamma\|x\|_2^2
+\frac{\rho}{2}[D_B(x)-\delta]_+^2.
\]

### 4.4 统一约定

后续所有代码模块、日志模块、诊断模块都必须把“当前在求解哪个 `F(x)`”记录清楚，禁止只写一个模糊的 `objective(x)` 而不记录策略标签。

---

## 5. 统一求解器接口

### 5.1 主函数签名（契约层）

建议统一主接口为：

```python
solve_portfolio_problem(
    problem_type: str,
    cov: np.ndarray,
    x_prev: np.ndarray,
    budget: np.ndarray | None,
    delta: float | None,
    eta: float,
    gamma: float,
    rho: float | None,
    solver_config: dict,
) -> SolverResult
```

其中：

- `problem_type ∈ {'ctr_only', 'ctb_only', 'main', 'gmv', 'mdp'}`；
- `cov` 对应 `Σ_t`；
- `x_prev` 对应 `x_{t-1}`；
- `budget` 对应 `b`；
- `delta` 仅在 `main` 中必须；
- `rho` 在 `main` 中必须，在其他问题中可为空；
- `solver_config` 记录容差、步长、最大迭代次数、切换规则等。

### 5.2 统一输出对象

`SolverResult` 必须至少包含：

```python
{
    'x': np.ndarray,
    'objective_value': float,
    'converged': bool,
    'status': str,
    'iterations_pg': int,
    'iterations_newton': int,
    'kkt_residual': float,
    'feasibility_residual': float,
    'band_violation': float,
    'active_set_size': int,
    'hit_boundary': bool,
    'fallback_used': str | None,
    'diagnostics': dict,
}
```

### 5.3 禁止事项

统一接口禁止出现以下行为：

1. 只返回最终 `x`，不返回诊断；
2. 把失败 silently 转成某个默认权重而不记录；
3. 不区分 `iterations_pg` 与 `iterations_newton`；
4. 不记录 band 约束是否激活；
5. 不记录是否使用 fallback。

---

## 6. 初始点、warm start 与数值域

### 6.1 主 warm start 规则

每个调仓时点的主 warm start 固定为：

1. 若 `x_{t-1}` 可行且数值稳定，则先用 `x_{t-1}`；
2. 若 `x_{t-1}` 不可用或不稳定，则用 `CtR-only` 的上期解；
3. 若仍不可用，则回退到 `EW`；
4. 对 `Main`，允许在 `CtR-only` 解基础上再进入主模型求解。

### 6.2 interiorization 规则

由于 simplex 边界可能导致某些分量过小、影响数值稳定性，统一采用轻量 interiorization：

对任意候选向量 `x`，定义

\[
\mathrm{interiorize}_\varepsilon(x)
=
\frac{\max(x,\varepsilon \mathbf{1})}{\mathbf{1}^\top \max(x,\varepsilon \mathbf{1})},
\]

其中 `ε` 是极小正数（如 `1e-10 ~ 1e-8` 量级，由实现层决定）。

### 6.3 使用原则

- interiorization 只用于数值稳定，不得改变经济解释；
- 主结果中的权重仍按 simplex 解释；
- 若某期严重依赖 interiorization 才能求解成功，必须在 diagnostics 中记录。

---

## 7. 两阶段算法的正式冻结

本项目统一采用：

> **Stage I: Projected Gradient**  
> **Stage II: Damped Newton on Free Set / Reduced Coordinates**

这是本文件最核心的冻结点。

### 7.1 为什么必须先梯度、后牛顿

原因固定为以下 5 条：

1. 主问题具有非线性与潜在非凸结构；
2. simplex 边界与 band 罚项使得直接二阶法容易不稳；
3. 从较粗糙初始点直接做牛顿，可能走向边界外或遭遇糟糕曲率；
4. 笔记中的算法主线本来就是“先梯度、后牛顿”；
5. 该路线最利于论文解释、代码实现与 diagnostics 记录。

### 7.2 Stage I：Projected Gradient 的角色

Stage I 的目标不是追求最终高精度，而是：

- 找到一个稳定可行的下降路径；
- 消除明显的目标不协调；
- 识别接近 0 的分量与初步活动集；
- 为 Stage II 提供更好的局部起点。

### 7.3 Stage II：Damped Newton 的角色

Stage II 的目标是：

- 在较稳定的局部邻域内利用二阶信息加速收敛；
- 改善 KKT 残差；
- 提高终点精度与局部稳定性；
- 为结果导出提供更可靠的最优性诊断。

---

## 8. Stage I：Projected Gradient 细则

### 8.1 统一更新形式

Stage I 的更新固定为：

\[
y^{(k)} = x^{(k)} - \alpha_k \nabla F(x^{(k)}),
\qquad
x^{(k+1)} = \Pi_{\mathcal{X}}\left(y^{(k)}\right),
\]

其中 `Π_𝒳` 是对 simplex 的欧氏投影。

### 8.2 步长规则

Stage I 默认采用 backtracking line search。必须满足：

- 初始步长 `α_init` 可配置；
- 缩减因子 `β_ls ∈ (0,1)` 可配置；
- 采用 Armijo 型充分下降条件；
- 若多次缩步后仍失败，记录 `line_search_failed_pg=True`。

### 8.3 Stage I 停止条件

满足以下任一条件即可停止 Stage I：

1. `projected_gradient_norm <= tol_pg_switch`；
2. 目标函数改善量连续若干步低于阈值；
3. 达到 `max_iter_pg`；
4. 活动集稳定达到预设轮数；
5. 触发切换到 Stage II 的手动条件。

### 8.4 活动集的初步识别

定义活动集估计为：

\[
\mathcal{A}^{(k)} = \{i: x_i^{(k)} \le \tau_{\mathrm{active}}\},
\]

其中 `τ_active` 是极小正阈值。  
Stage I 负责提供该活动集的初步估计，但**不在此阶段做最终冻结**。

---

## 9. Stage II：Damped Newton on Free Set 细则

### 9.1 为什么不用“裸牛顿”

本项目明确禁止在 simplex 全空间上直接使用无阻尼、无活动集控制的裸牛顿法。  
原因是：

- 它可能破坏非负约束；
- 在 band 罚项激活切换处可能出现不稳定曲率；
- 在接近边界时可能数值恶化；
- 不利于诊断和论文解释。

### 9.2 自由集定义

在 Stage II，定义自由集为：

\[
\mathcal{F}^{(k)} = \{i: x_i^{(k)} > \tau_{\mathrm{free}}\}.
\]

只有自由集分量进入二阶更新；活动集分量固定为 0 或保持在极小邻域内，由可行性修正统一处理。

### 9.3 Reduced-coordinate Newton

Stage II 原则上在 reduced coordinates / free set 上构建局部二阶模型：

\[
H_{\mathcal{F}\mathcal{F}} d_{\mathcal{F}} = -g_{\mathcal{F}} + \text{(equality correction)},
\]

并同时维护：

\[
\sum_{i\in\mathcal{F}} d_i = 0
\]

以保证更新后仍能与 simplex 约束兼容。

### 9.4 Hessian 使用原则

Stage II 允许以下二阶对象：

1. 精确 Hessian；
2. 正则化 Hessian：`H + λ_I I`；
3. Gauss–Newton / quasi-Newton 近似（仅在精确 Hessian 代价或稳定性不理想时）。

但必须记录：

- 使用的是哪类 Hessian；
- 是否进行了正则化；
- 正则化参数大小。

### 9.5 阻尼与线搜索

Newton 更新采用：

\[
x^{(k+1)} = \Pi_{\mathcal{X}}\left(x^{(k)} + s_k d^{(N)}\right),
\]

其中 `s_k` 由阻尼线搜索确定。  
统一要求：

- 不允许默认全步长直接接受；
- 必须做下降与可行性检查；
- 若连续多次无法找到合适阻尼步长，则触发 fallback。

### 9.6 Stage II 停止条件

满足以下全部主条件之一即可：

1. `kkt_residual <= tol_kkt`；
2. `feasibility_residual <= tol_feas`；
3. `|F_{k+1}-F_k| <= tol_obj` 且步长范数足够小；
4. 达到 `max_iter_newton`。

---

## 10. band 约束与罚项的处理

### 10.1 主实现约定

`Main` 模型使用软约束实现：

\[
\frac{\rho}{2}[D_B(x)-\delta]_+^2.
\]

因此 solver 必须在每次迭代中显式记录：

- 当前 `D_B(x)`；
- 当前 `band_gap = max(D_B(x)-δ, 0)`；
- 当前 band 是否激活。

### 10.2 光滑性处理

主 contract 允许直接使用分段可微形式 `[z]_+^2`。  
若实现层为了数值稳定使用平滑近似，则必须满足：

1. 平滑近似只能视为数值实现细节；
2. 对论文与结果解释，底层对象仍统一报告为 `[D_B-δ]_+^2`；
3. 实现中必须记录平滑参数。

### 10.3 `ρ` 的 continuation 规则

对 `Main` 模型，允许采用逐步增大 `ρ` 的 continuation 机制，但必须遵守：

1. `ρ` 是数值参数，不是经济参数；
2. continuation 只服务可行性与收敛稳定性；
3. 每次 `ρ` 调整都必须记录在 diagnostics 中；
4. 最终报告必须给出末次有效 `ρ`。

---

## 11. fallback 机制的正式冻结

统一 fallback ladder 固定如下：

### 11.1 Fallback-0：常规两阶段成功

- `Projected Gradient -> Damped Newton` 成功收敛；
- 输出 `fallback_used = null`。

### 11.2 Fallback-1：仅用 Projected Gradient 收尾

若 Stage II 数值不稳、Hessian 病态或线搜索反复失败，则：

- 停止进入 Newton；
- 继续用 Stage I 小步长收尾若干步；
- 输出 `fallback_used = 'pg_finish'`。

### 11.3 Fallback-2：增大 `γ` 或增强 Hessian 正则

若目标地形过于平坦或局部 Hessian 不稳定，则允许：

- 临时增强数值正则；
- 重新启动 Stage II；
- 输出 `fallback_used = 'regularized_newton'`。

### 11.4 Fallback-3：对 `Main` 降级为 `CtR-only` warm-restricted solve

若 `Main` 在给定 `δ,ρ` 下长期不稳，则允许：

1. 先求 `CtR-only`；
2. 再以其为 warm start 尝试较保守的 `Main`；
3. 若仍失败，输出失败状态，但不得伪装成成功的 `Main`。

### 11.5 Fallback-4：返回上期权重 / EW 作为交易执行保护

这一步只允许在**实盘化回测执行层**用于保持流水连续，不允许在论文结果中冒充“模型成功求解”。

统一要求：

- 若使用此 fallback，必须明确标记 `status='execution_fallback'`；
- `converged=False`；
- diagnostics 中必须说明源问题未成功求解。

---

## 12. 诊断输出的正式冻结

每次求解必须记录以下诊断字段：

### 12.1 迭代与收敛类

- `iterations_pg`
- `iterations_newton`
- `converged`
- `status`
- `objective_value`
- `objective_improvement`

### 12.2 可行性与最优性类

- `feasibility_residual`
- `simplex_sum_residual`
- `min_weight`
- `kkt_residual`
- `projected_gradient_norm`

### 12.3 band 与结构类

- `D_R`
- `D_B`
- `band_gap`
- `band_active`
- `band_penalty_value`

### 12.4 边界与活动集类

- `active_set_size`
- `free_set_size`
- `hit_boundary`
- `interiorization_applied`

### 12.5 二阶法类

- `newton_attempted`
- `hessian_type`
- `hessian_regularization`
- `newton_step_norm`
- `line_search_failed_newton`

### 12.6 fallback 类

- `fallback_used`
- `fallback_reason`

### 12.7 时间与稳定性类

- `solve_time_ms`
- `continuation_steps`
- `rho_final`

这些字段后续必须与 `08_result_contract.md` 对齐，形成 `diagnostics.json` 与长表诊断输出。

---

## 13. 统一容差与默认配置层级

### 13.1 容差分类

求解器容差统一分为四类：

1. **switch tolerances**：决定何时从 PG 切到 Newton；
2. **feasibility tolerances**：决定 simplex / band 可行性；
3. **optimality tolerances**：决定 KKT 与 stationarity；
4. **execution tolerances**：用于实盘化回测中的防爆保护。

### 13.2 默认层级原则

- 论文主实验使用同一套默认 `solver_config`；
- calibration 不以 solver tolerances 作为主要调参维度；
- solver tolerances 视为数值制度，而不是经济参数。

### 13.3 禁止事项

不允许为了让某个策略表现更好而单独给它更宽松或更苛刻的容差，除非该差异在 contract 中被明确登记并可被充分解释。

---

## 14. 与代码目录的映射

建议代码层至少包含以下模块：

```text
src/
  solvers/
    simplex.py          # simplex projection / interiorization
    objectives.py       # D_R, D_B, penalty, gradient, Hessian helpers
    projected_grad.py   # Stage I
    damped_newton.py    # Stage II
    solve_main.py       # unified solve_portfolio_problem wrapper
    diagnostics.py      # KKT / feasibility / logging
```

### 命名约定

- `solve_portfolio_problem`：统一入口；
- `projected_gradient_step`：Stage I 主函数；
- `damped_newton_step`：Stage II 主函数；
- `compute_diagnostics`：统一诊断；
- `project_to_simplex`：simplex 投影；
- `interiorize_weights`：数值稳定辅助函数。

---

## 15. 与论文写作的接口

本文件直接服务以下论文章节：

- 第 6 章：统一求解器设计；
- 第 7 章：实验制度；
- 第 8 章：结果解释（特别是 diagnostics 与 band activation）；
- 附录：算法伪代码与停止准则。

主文需要强调的不是“我们用了某个库”，而是：

1. 问题为什么需要两阶段；
2. 为什么先 PG 再 Newton；
3. 为什么需要 active set / free set；
4. 为什么需要 fallback 与 diagnostics；
5. 这些设计如何保障结果可信。

---

## 16. 伪代码冻结（论文版）

```text
Input: Σ_t, x_{t-1}, b, δ, η, γ, ρ, solver_config
Output: x_t, diagnostics

1. Build objective F according to problem_type
2. Construct warm start x^(0)
3. Interiorize x^(0) if numerically necessary
4. Stage I: projected gradient
   repeat
      compute g_k = ∇F(x^(k))
      take projected gradient step with backtracking
      update active-set estimate
   until switch criterion or max_iter_pg
5. Stage II: damped Newton on free set
   repeat
      identify free set
      build reduced Hessian / regularized Hessian
      compute damped Newton direction
      line search with feasibility control
      update x
   until KKT / feasibility tolerance or max_iter_newton
6. If Newton fails, activate fallback ladder
7. Compute final diagnostics and return result
```

---

## 17. 冻结边界说明

本文件当前冻结以下内容：

1. 统一 solver 必须覆盖 `CtR-only / CtB-only / Main`；
2. 主算法路线固定为 `Projected Gradient -> Damped Newton`；
3. warm start、active set、free set、fallback、diagnostics 都必须进入正式 contract；
4. `Main` 通过 band 软约束罚项实现；
5. 失败时不得 silent fallback 冒充成功。

本文件当前**仍允许**在实现层调整以下细节：

1. simplex 投影的具体实现算法；
2. Hessian 精确求导、自动微分或近似求法；
3. line search 常数；
4. `ρ` continuation 的具体步长表；
5. Newton 阶段采用精确 Hessian 还是正则化近似 Hessian。

也就是说，本文件冻结的是**求解制度与接口**，而不是微观数值常数。

---

## 18. 当前版本状态

- Version: `v0.1`
- Freeze level: `F2`
- Status: `Draft, ready for alignment with result contract`
