# 08_result_contract.md

## 1. 文件目的与当前状态

本文件用于冻结本项目的**结果输出契约（result contract）**，回答以下问题：

1. 每一次 run 到底必须输出哪些文件；
2. 哪些结果是论文直接资产，哪些结果是 GPT / 诊断 / 追溯资产；
3. 后续图表、表格、章节写作和答辩解释能依赖哪些固定字段；
4. 文件名、字段名、目录结构、时间索引和策略标签如何统一；
5. 如何确保“每张图都有底层数据、每个结论都可追溯、每次失败都能被记录”。

本文件不负责：

- 主模型与基准模型的数学定义（由 `06_model_contract.md` 与 `06A_baseline_ladder.md` 管理）；
- 求解器内部迭代逻辑（由 `07_solver_contract.md` 管理）；
- 统计显著性检验与多重比较防护（由 `08A_statistical_validation.md` 管理）；
- 单次实验的具体登记（由 `experiment_registry.md` 管理）。

**当前状态**：F2 freeze  
**冻结说明**：`08A_statistical_validation.md` 已完成并与本文件对齐。

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

因此，本文件不得改变以下已冻结事实：

1. 主研究对象是 **long-only 大类资产 ETF 组合**；
2. 主资产宇宙固定为 `SPY / VEA / VWO / IEF / SHY / TIP / LQD / VNQ / GLD / DBC`；
3. 主比较策略标签固定为 `EW / GMV / CtR-only / MDP / CtB-only / Main`；
4. `D_R(x;b)`、`D_B(x)` 的经验定义已经在 `06_model_contract.md` 中冻结；
5. 核心非线性模型的 solver diagnostics 已在 `07_solver_contract.md` 中冻结；
6. 本项目所有结果必须服务论文可写性、代码可复现性、答辩可解释性和 GPT 可读性，而不是只追求图片输出。

---

## 3. 结果输出设计原则

### 3.1 一个 run_id，对应一套完整可追溯资产

每次正式或半正式实验都必须生成唯一 `run_id`，并把该次实验的：

- 数据口径；
- 参数口径；
- 策略集合；
- 原始结果；
- 论文图表；
- 诊断日志；
- GPT 可读摘要；

全部绑定到同一个 `run_id` 下。

禁止出现：

- 图来自一次 run，表来自另一次 run；
- 更新了参数但未更新结果目录；
- 无法追溯图表对应数据来源。

### 3.2 每张图必须有底层数据

本项目严格执行：

> **No orphan figure. No orphan table.**

即：

- 每个 `fig_*.png/pdf` 必须对应一个 `figdata_*.csv`；
- 每个 `table_*.tex` 必须对应一个 `table_*.csv`；
- 论文中的所有数字必须能追溯到 long-format panels、summary tables 或 diagnostics files。

### 3.3 区分三类资产

每个 run 必须同时输出三类资产：

1. **Paper assets**：直接进论文和 PPT 的图表；
2. **Analysis assets**：便于 GPT 和研究者继续分析的 CSV / JSON / long tables；
3. **Diagnostics assets**：记录 solver、约束激活、失败回退、质量检查和 warning 的文件。

### 3.4 字段名一经冻结不得漂移

后续代码、表格和图表统一使用以下主字段，不允许再造未登记别名：

- `ctr`
- `ctb`
- `D_R`
- `D_B`
- `band_active`
- `band_violation`
- `turnover`
- `obj_total`
- `dr_term`
- `band_penalty`
- `converged`
- `fallback_used`

### 3.5 结果目录必须足够“笨但稳”

本项目不追求花哨目录，而追求：

- 直观；
- 稳定；
- 一眼能查；
- 便于论文写作与答辩复盘。

---

## 4. 标准结果目录结构

每次 run 的标准目录固定为：

```text
results/
  runs/
    <run_id>/
      manifest.json
      run_notes.md
      warnings.json

      configs/
        control_snapshot.json
        data_config_snapshot.json
        model_config_snapshot.json
        solver_config_snapshot.json

      data/
        asset_metadata.csv
        rebalance_calendar.csv
        cov_summary.csv

      analysis/
        summary_metrics.csv
        weights.csv
        ctr_long.csv
        ctb_long.csv
        dr_db_timeseries.csv
        objective_terms.csv
        turnover_timeseries.csv
        solver_diagnostics.csv
        analysis_pack.json

      diagnostics/
        run_diagnostics.json
        quality_checks.csv
        failure_log.csv

      tables/
        table_summary_main.csv
        table_summary_main.tex
        table_risk_structure.csv
        table_risk_structure.tex
        table_calibration_screen.csv
        table_calibration_screen.tex

      figures/
        fig_weights_vs_risk_share.png
        fig_weights_vs_risk_share.pdf
        fig_dr_db_frontier.png
        fig_dr_db_frontier.pdf
        fig_dr_db_roll.png
        fig_dr_db_roll.pdf
        fig_ctr_heatmap.png
        fig_ctr_heatmap.pdf
        fig_ctb_heatmap.png
        fig_ctb_heatmap.pdf
        fig_solver_convergence.png
        fig_solver_convergence.pdf

      figure_data/
        figdata_weights_vs_risk_share.csv
        figdata_dr_db_frontier.csv
        figdata_dr_db_roll.csv
        figdata_ctr_heatmap.csv
        figdata_ctb_heatmap.csv
        figdata_solver_convergence.csv
```

### 4.1 目录使用规则

- `analysis/` 放研究分析主表；
- `diagnostics/` 放运行质量与失败信息；
- `tables/` 放最终表格资产；
- `figures/` 放最终图形资产；
- `figure_data/` 放图的底层数据；
- `configs/` 放本次 run 的配置快照。

### 4.2 最低允许简化

若处于最小可运行阶段（如 `minimal real ETF run`），允许暂时不输出全部 `tables/` 与 `figures/`，但以下文件仍是**硬要求**：

- `manifest.json`
- `summary_metrics.csv`
- `weights.csv`
- `dr_db_timeseries.csv`
- `solver_diagnostics.csv`
- `analysis_pack.json`
- `run_diagnostics.json`

---

## 5. run 级元数据契约

### 5.1 `manifest.json`

该文件是每次 run 的唯一元信息入口，必须至少包含以下字段：

```json
{
  "run_id": "...",
  "run_type": "toy|minimal_real|full|calibration",
  "timestamp_utc": "...",
  "universe_name": "core10_etf",
  "assets": ["SPY", "VEA", "VWO", "IEF", "SHY", "TIP", "LQD", "VNQ", "GLD", "DBC"],
  "date_start": "...",
  "date_end": "...",
  "rebalance_frequency": "monthly",
  "cov_estimator": "ledoit_wolf_252d",
  "strategies": ["EW", "GMV", "CtR-only", "MDP", "CtB-only", "Main"],
  "main_params": {
    "delta": "...",
    "eta": "...",
    "gamma": "...",
    "rho": "..."
  },
  "status": "success|partial|failed"
}
```

### 5.2 `run_notes.md`

该文件用于简要记录：

- 本次 run 的目的；
- 是否属于正式主结果；
- 是否存在已知异常；
- 是否可进入正文图表；
- 后续是否需要重跑。

### 5.3 `warnings.json`

集中记录 run 级 warning，例如：

- 某些日期使用 fallback；
- 某些窗口样本数不足；
- 某些 figure 未生成；
- 某个策略在某段窗口被跳过。

---

## 6. analysis 主表契约

本节冻结后续最常用分析表的文件名、主字段和语义。

### 6.1 `summary_metrics.csv`

#### 目的

用于输出每个策略在指定评价窗口中的总览指标，是论文 summary table 与摘要讨论的主来源。

#### 主键

- `run_id`
- `strategy`
- `sample`（`train|validation|test|full_eval`）

#### 必备字段

- `run_id`
- `strategy`
- `sample`
- `ann_return`
- `ann_vol`
- `sharpe`
- `max_drawdown`
- `calmar`
- `turnover_mean`
- `turnover_p95`
- `D_R_mean`
- `D_B_mean`
- `band_active_rate`
- `n_rebalances`

#### 规则

- `strategy` 必须使用 `06A_baseline_ladder.md` 中冻结的主标签；
- `Main` 的 `D_R_mean`、`D_B_mean` 必须可与 `CtR-only`、`CtB-only` 对比；
- 任意新增绩效字段只允许追加，不允许改名已有字段。

---

### 6.2 `weights.csv`

#### 目的

记录每个调仓时点的组合权重，是所有资本配置图、换手计算和边界命中分析的基础表。

#### 主键

- `date`
- `strategy`
- `asset`

#### 必备字段

- `date`
- `strategy`
- `asset`
- `weight`
- `weight_prev`
- `trade`

#### 规则

- `date` 使用 ISO `YYYY-MM-DD`；
- `asset` 必须属于主宇宙或明确标记 toy case 资产名；
- 每个 `date × strategy` 下所有 `weight` 和必须在容差内等于 1。

---

### 6.3 `ctr_long.csv`

#### 目的

记录 CtR 及其预算偏离，是 CtR 热力图、风险分配镜像图和正文机制解释的核心底层表。

#### 主键

- `date`
- `strategy`
- `asset`

#### 必备字段

- `date`
- `strategy`
- `asset`
- `ctr`
- `ctr_share`
- `budget`
- `ctr_gap`

其中：

- `ctr` 对应 `\mathrm{CtR}_i(x;\Sigma)`；
- `ctr_share` 对应标准化风险贡献份额；
- `ctr_gap = ctr_share - budget`。

#### 规则

- `ctr_share` 在每个 `date × strategy` 横截面上之和必须等于 1（容差内）；
- `budget` 与当期预算向量保持一致；
- `ctr_gap` 是图表和论文中“偏离预算”的主解释字段。

---

### 6.4 `ctb_long.csv`

#### 目的

记录 CtB 及其横截面偏离，是 CtB 热力图、结构解释图与 `D_B` 解释的底层表。

#### 主键

- `date`
- `strategy`
- `asset`

#### 必备字段

- `date`
- `strategy`
- `asset`
- `ctb`
- `ctb_mean`
- `ctb_gap`

其中：

- `ctb` 对应 `\mathrm{CtB}_i(x;\Sigma)`；
- `ctb_mean` 是同一 `date × strategy` 横截面均值；
- `ctb_gap = ctb - ctb_mean`。

#### 规则

- `ctb_gap` 的横截面均值必须在容差内为 0；
- 后续 `D_B` 的任何图表解释都不得脱离 `ctb_long.csv` 的底层数据。

---

### 6.5 `dr_db_timeseries.csv`

#### 目的

记录每期主离散度及 band 激活情况，是主论文最关键的机制解释表之一。

#### 主键

- `date`
- `strategy`

#### 必备字段

- `date`
- `strategy`
- `D_R`
- `D_B`
- `delta`
- `band_active`
- `band_violation`

其中：

- `band_active` 为二元字段，表示该期 band 是否激活；
- `band_violation = max(D_B - delta, 0)`。

#### 规则

- `CtR-only` 与 `CtB-only` 仍可记录 `D_R` 与 `D_B`，以保证横向比较；
- `Main` 的 `band_active` 与 `band_violation` 是答辩时解释“band 什么时候真的起作用”的主证据；
- 若 `band_active = 0`，则 `band_violation` 必须在容差内为 0。

---

### 6.6 `objective_terms.csv`

#### 目的

拆分每期目标函数组成项，供主模型机制解释与 solver/penalty 诊断使用。

#### 主键

- `date`
- `strategy`

#### 必备字段

- `date`
- `strategy`
- `obj_total`
- `dr_term`
- `db_term`
- `smooth_term`
- `l2_term`
- `band_penalty`

#### 规则

- 对 `Main`，`obj_total` 应与主实现型目标一致；
- 对不含某项的策略，相应字段允许为 0，但字段不得缺失；
- `db_term` 主要服务 `CtB-only`，`band_penalty` 主要服务 `Main`。

---

### 6.7 `turnover_timeseries.csv`

#### 目的

记录每期换手，是平滑项 `η` 经济意义与交易可实施性讨论的主表。

#### 主键

- `date`
- `strategy`

#### 必备字段

- `date`
- `strategy`
- `turnover`
- `gross_trade`

#### 规则

- `turnover` 公式必须与回测模块保持一致；
- 主文摘要指标中的 `turnover_mean` 与 `turnover_p95` 必须从本表聚合得到。

---

### 6.8 `solver_diagnostics.csv`

#### 目的

逐期记录 solver 级诊断，是与 `07_solver_contract.md` 对齐的核心文件。

#### 主键

- `date`
- `strategy`

#### 必备字段

- `date`
- `strategy`
- `converged`
- `status`
- `iterations_pg`
- `iterations_newton`
- `kkt_residual`
- `feasibility_residual`
- `active_set_size`
- `hit_boundary`
- `band_violation`
- `fallback_used`
- `solve_time_ms`

#### 规则

- 至少对 `CtR-only / CtB-only / Main` 强制输出；
- 若某策略无需统一 solver，可把不适用字段记为 `NA`，但文件结构不变；
- `converged = false` 时，`status` 与 `fallback_used` 不能为空。

---

### 6.9 `analysis_pack.json`

#### 目的

为 GPT 与研究者提供一次 run 的机器可读总结入口。

#### 必备字段

```json
{
  "run_id": "...",
  "best_strategy_by_primary_rule": "...",
  "primary_rule": "Main preferred if D_R and D_B jointly improved subject to validation rule",
  "key_findings": ["..."],
  "metric_deltas_vs_ctr_only": {},
  "metric_deltas_vs_ctb_only": {},
  "metric_deltas_vs_mdp": {},
  "recommended_figures": ["..."],
  "warnings": ["..."]
}
```

#### 规则

- `analysis_pack.json` 是摘要入口，不替代底层表；
- 其中所有判断都必须能追溯到 `summary_metrics.csv`、`dr_db_timeseries.csv`、`solver_diagnostics.csv` 或 figure data。

---

## 7. diagnostics 契约

### 7.1 `run_diagnostics.json`

用于记录 run 级质量信息，至少包括：

- `n_total_rebalances`
- `n_failed_solves`
- `n_fallback_calls`
- `n_boundary_hits`
- `n_band_active`
- `max_kkt_residual`
- `quality_gate_passed`

### 7.2 `quality_checks.csv`

用于记录逐项检查结果，至少包括：

- `check_name`
- `scope`
- `passed`
- `severity`
- `message`

建议至少执行以下检查：

1. 权重和是否为 1；
2. 是否存在负权重；
3. `ctr_share` 横截面和是否为 1；
4. `ctb_gap` 横截面均值是否为 0；
5. `band_violation` 与 `band_active` 是否一致；
6. `obj_total` 是否与组成项一致；
7. `summary_metrics.csv` 是否可从底层表复算关键指标；
8. figure data 与 figures 是否一一对应。

### 7.3 `failure_log.csv`

逐条记录失败或异常，包括：

- `date`
- `strategy`
- `failure_type`
- `message`
- `fallback_used`
- `resolved`

禁止把失败只写到终端，不写入结果目录。

---

## 8. paper assets 契约

### 8.1 表格命名规则

正文主表统一采用：

- `table_summary_main.*`
- `table_risk_structure.*`
- `table_calibration_screen.*`

若有扩展表，只允许追加编号或后缀，不允许改动主表文件名。

### 8.2 图形命名规则

正文主图统一采用：

- `fig_weights_vs_risk_share.*`
- `fig_dr_db_frontier.*`
- `fig_dr_db_roll.*`
- `fig_ctr_heatmap.*`
- `fig_ctb_heatmap.*`
- `fig_solver_convergence.*`

### 8.3 图形底层数据契约

每张正文图必须有对应 `figure_data/figdata_*.csv`，命名一一对应：

- `fig_dr_db_frontier.*` ↔ `figdata_dr_db_frontier.csv`
- `fig_ctb_heatmap.*` ↔ `figdata_ctb_heatmap.csv`

### 8.4 论文与 PPT 共用规则

- 论文与答辩 PPT 尽量共用同一套主图；
- 若为 PPT 做了简化版图片，也必须保留对应底层 `figdata_*.csv`；
- PPT 不得使用无法追溯到某个 `run_id` 的图。

---

## 9. 文件命名、时间与标签规则

### 9.1 日期格式

统一使用 ISO 格式：`YYYY-MM-DD`。

### 9.2 策略标签

统一使用以下标签，大小写与连字符固定：

- `EW`
- `GMV`
- `CtR-only`
- `MDP`
- `CtB-only`
- `Main`

### 9.3 资产标签

主宇宙下固定为：

- `SPY`
- `VEA`
- `VWO`
- `IEF`
- `SHY`
- `TIP`
- `LQD`
- `VNQ`
- `GLD`
- `DBC`

### 9.4 缺失值规则

- 不允许把缺失 silently 处理成 0；
- 若字段不可用，使用 `NA` 并在 `warnings.json` 或 `failure_log.csv` 中说明；
- 正式主结果目录不得包含未说明的缺失关键字段。

---

## 10. toy / minimal / full 三类 run 的最低输出要求

### 10.1 toy experiments

至少输出：

- `manifest.json`
- `summary_metrics.csv`（可简化）
- `weights.csv`
- `dr_db_timeseries.csv`
- `solver_diagnostics.csv`
- 至少 1 张主要 figure 及对应 `figdata_*.csv`

### 10.2 minimal real ETF run

至少输出：

- `manifest.json`
- `summary_metrics.csv`
- `weights.csv`
- `ctr_long.csv`
- `ctb_long.csv`
- `dr_db_timeseries.csv`
- `solver_diagnostics.csv`
- `analysis_pack.json`
- `run_diagnostics.json`

### 10.3 full experiments

必须输出本文件第 4 节规定的全部主目录与核心文件。

---

## 11. 与后续文件的接口

### 11.1 与 `08A_statistical_validation.md` 的接口

后续统计验证文件将补充：

- 绩效差异的显著性检验表；
- 多重比较与过拟合防护输出；
- 校准筛选的统计依据文件。

这些文件会在本目录结构基础上追加，但**不会替代**本文件冻结的 analysis / diagnostics 主表。

### 11.2 与 `experiment_registry.md` 的接口

`experiment_registry.md` 负责说明“实验如何登记”；本文件负责说明“每个登记后的实验必须产出什么”。

### 11.3 与 `figure/table factory` 的接口

后续图表工厂只允许从：

- `analysis/*.csv`
- `diagnostics/*.csv/json`

读取数据生成最终图表，不允许手工拼接未登记数据源。

---

## 12. 冻结建议

本文件当前建议维持 **F2 draft**，原因如下：

1. 主 analysis 表、diagnostics 表和 figure-data 制度已经基本成型；
2. 但统计验证文件 `08A_statistical_validation.md` 尚未完成，部分附加输出可能还会追加；
3. 因此本文件当前适合冻结主结构、保留统计附加层的扩展空间。

当以下条件满足时，本文件进入 **F2 freeze**：

- `08A_statistical_validation.md` 完成；
- `experiment_registry.md` 给出统一 run 登记口径；
- `minimal real ETF run` 成功输出至少一次符合本契约的结果目录。

在进入 F2 freeze 后：

- 主文件名不得再改；
- 主字段名不得再改；
- 正文主图主表名称不得再改；
- 新增字段只能追加，不得破坏向后兼容。
