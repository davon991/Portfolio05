# 04_literature_map_thesisready_v2.md

## 0. 文件目的与当前状态

本文件是对 `04_literature_map_lite.md` 的滚动更新与重命名版本，用于把原先的“轻量文献地图”升级为 **clean 主线 + 章节写作 + defense/PPT** 可直接共用的 **thesis-ready 文献地图**。

它服务以下目标：

1. 为 Chapter 2–8 提供最小但足够严肃的引用骨架；
2. 将文献角色与 `03A_contribution_claims.md`、`03_thesis_skeleton.md`、`09_writing_contract_v2.md` 对齐；
3. 明确每篇文献支撑的是理论定义、比较基准、统计纪律还是结果解释；
4. 把先前仍处于“待补”的 bootstrap / GMV / 1/N 引文补成可写作版本；
5. 为正文、附录、答辩与 PPT 提供统一入口，避免后续口径漂移。

**当前状态**：F3 final-freeze candidate  
**Supersedes**：`04_literature_map_lite.md`

---

## 1. 上位约束与服从关系

本文件服从以下冻结文件：

### F1
- `00_project_charter.md`
- `01_notation_master.md`
- `02_definition_formula_ledger.md`
- `03_thesis_skeleton.md`

### F2
- `03A_contribution_claims.md`
- `05_data_contract.md`
- `06_model_contract.md`
- `06A_baseline_ladder.md`
- `08A_statistical_validation.md`

### F3 / 写作层
- `experiment_registry_final.md`
- `chapter_feedback_loop_final.md`
- `defense_qa_bank_final.md`
- `final_PPT_script_v3.md`
- `09_writing_contract_v2.md`

因此，本文件不得改变以下已冻结事实：

1. 主线是 **CtR 主目标 + CtB 结构约束 / band control**；
2. 主经验语境是 **long-only 大类资产 ETF**；
3. 主比较基准固定为 `EW / GMV / CtR-only / MDP / CtB-only / Main`；
4. 文献首先服务于理论对象、比较设计、统计纪律与结果解释；
5. 本文不是“风险平价大全”，也不是“全体分散化方法综述”；
6. 文献地图必须支持 Chapter 3–8 的主写作，而不是扩写无关谱系。

---

## 2. 使用原则

### 2.1 先定角色，再增数量
新增文献前必须先回答：

1. 它服务哪一章、哪一节？
2. 它支撑的是理论、基准、统计、解释中的哪一类？
3. 删除它后，论文是否会损失关键论证？

若回答不清，则默认不进入主地图。

### 2.2 三层优先级
- **Tier A（Must Cite）**：正文主线至少直接引用一次；
- **Tier B（Strong Support）**：强支撑文献，进入正文或附录视篇幅决定；
- **Tier C（Appendix / Defense）**：只作附录、答辩、方法比较或图表借鉴。

### 2.3 章节映射优先于年份堆砌
文献综述组织顺序必须优先服从：

- 基础理论；
- 风险贡献 / 风险预算；
- 相关结构 / 分散化；
- 比较基准；
- 协方差估计与数值稳健；
- 统计验证与防过拟合。

### 2.4 不把实现材料伪装成学术主引文
包文档、白皮书、工程博客只可作为实现或图表借鉴，不可替代理论、方法或统计主引文。

---

## 3. 章节最低引用预算（thesis-ready 版）

### Chapter 2：理论预备与统一框架
最低应覆盖：
- Markowitz (1952)
- Sharpe (1964) 或同类经典市场组合背景
- Ledoit & Wolf (2004)

### Chapter 3：CtR、风险预算与 CtR-only
最低应覆盖：
- Qian (2006)
- Maillard, Roncalli, Teiletche (2010)
- Roncalli 风险预算 / 风险平价扩展文献中至少 1 篇补强文献

### Chapter 4：CtB、相关结构与 CtB-only / MDP 相邻对象
最低应覆盖：
- Choueifaty & Coignard (2008)
- Menchero & Davis (2011)
- diversified risk parity / correlation-structure 相邻文献至少 1 篇

### Chapter 5：CtR–CtB 协调模型
最低应覆盖：
- Chapter 3 + Chapter 4 的桥接引用
- 说明本文创新是“协调建模 + 制度化实现”，不是声称已存在完全同名经典范式

### Chapter 7–8：实验制度与结果
最低应覆盖：
- Ledoit & Wolf (2004)
- 至少 1 篇 GMV / minimum variance 文献
- 至少 1 篇 1/N 文献
- White (2000)
- Bailey & López de Prado (2014)
- 至少 1 篇 block / stationary bootstrap 文献

---

## 4. 主文献簇与条目

以下 `Chapter target` 使用：
- `Ch2` 理论预备
- `Ch3` CtR
- `Ch4` CtB
- `Ch5` 协调模型
- `Ch7` 实验制度
- `Ch8` 结果解释
- `App` 附录 / 答辩补充

### 4.1 Foundation：均值—方差与经典背景

| ID | 文献 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| F-01 | Markowitz (1952), *Portfolio Selection* | A | Ch2 | 现代组合理论原点 | 必引 |
| F-02 | Sharpe (1964), *Capital Asset Prices* | B | Ch2 / App | 市场组合与经典背景 | 不把正文写成 CAPM 综述 |
| F-03 | Ledoit & Wolf (2004), covariance shrinkage | A | Ch2 / Ch7 | 协方差稳健估计与条件数控制 | 必引 |

### 4.2 Risk Contribution / Risk Budgeting：CtR 主线

| ID | 文献 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| R-01 | Qian (2006), *On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up* | A | Ch3 | 为 CtR / risk budget 提供经济解释与“可加总”语义 | 必引 |
| R-02 | Maillard, Roncalli, Teiletche (2010), *The Properties of Equally Weighted Risk Contribution Portfolios* | A | Ch3 / Ch7 | ERC 的经典基准文献，支撑 `CtR-only` baseline | 必引 |
| R-03 | Roncalli, *Introduction to Risk Parity and Budgeting*（书或相关代表性论文） | B | Ch3 / App | 风险预算谱系补强 | 选 1 条进入正文或附录 |

### 4.3 Diversification / Correlation-Structure：CtB 相邻主线

| ID | 文献 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| C-01 | Choueifaty & Coignard (2008), *Toward Maximum Diversification* | A | Ch4 / Ch7 | MDP / diversification ratio 的经典依据 | 必引 |
| C-02 | Menchero & Davis (2011), *Risk Contribution Is Exposure Times Volatility Times Correlation* | A | Ch4 / Ch5 / Ch8 | 为 CtB 的相关结构叙事提供桥梁 | 必引 |
| C-03 | Lohre, Opfer, Orszag (2012), diversified risk parity | B | Ch4 / App | 风险预算与分散化之间的过渡对象 | 建议进入文献综述 |
| C-04 | Froidure, Fuertes, Phylaktis (2020) 或同类 diversified / correlation-based allocation 文献 | C | App / Defense | 作为答辩补强，不抢正文主线 | 可选 |

### 4.4 Alternative Baselines：比较对象而非主线替代

| ID | 文献 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| B-01 | Clarke, de Silva, Thorley (2006), minimum-variance literature | B | Ch7 / Ch8 | GMV 的经典比较地位 | 至少选 1 篇 |
| B-02 | DeMiguel, Garlappi, Uppal (2009), *Optimal Versus Naive Diversification* | B | Ch7 / Ch8 | `EW` / 1/N 的必要对照地位 | 建议正文直接引用 |
| B-03 | López de Prado (2016), *Building Diversified Portfolios that Outperform Out of Sample* | C | App / Defense | HRP 只作附录 / 答辩补充 | 不进入主比较集合 |

### 4.5 Statistical Validation：统计纪律与防过拟合

| ID | 文献 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| S-01 | White (2000), *A Reality Check for Data Snooping* | A | Ch7 / Ch8 / App | 参数与模型搜索后的数据窥探风险讨论 | 必引 |
| S-02 | Bailey & López de Prado (2014), *The Deflated Sharpe Ratio* | A | Ch7 / Ch8 / App | Sharpe 选择偏差与非正态修正 | 必引 |
| S-03 | Künsch (1989), *The Jackknife and the Bootstrap for General Stationary Observations* | B | Ch7 / App | 时间序列 block bootstrap 基础文献 | 建议进入附录或方法节 |
| S-04 | Politis & Romano (1994), *The Stationary Bootstrap* | B | Ch7 / App | stationary bootstrap 的代表文献 | 作为补强或替代引用 |
| S-05 | Lahiri (1999/2003, block bootstrap survey/book) | C | App | bootstrap 方法论综述 | 可选 |

### 4.6 Implementation / Visualization Borrowing：只作借鉴

| ID | 文献 / 来源 | Tier | Chapter target | 角色 | 备注 |
|---|---|---|---|---|---|
| V-01 | 风险平价 / 组合优化包文档 | C | App / Defense | 借鉴结果组织或实现说明 | 不替代主引文 |
| V-02 | correlation heatmap / mirror-bar 可视化范例 | C | Ch8 / App | 图形表达灵感 | 仅作图表借鉴 |

---

## 5. 当前最小“必引集合”（升级版）

### 5.1 一级必引（正文主线）
1. Markowitz (1952)
2. Qian (2006)
3. Maillard, Roncalli, Teiletche (2010)
4. Choueifaty & Coignard (2008)
5. Menchero & Davis (2011)
6. Ledoit & Wolf (2004)
7. White (2000)
8. Bailey & López de Prado (2014)

### 5.2 二级强支撑（按篇幅择优进入正文）
1. Sharpe (1964)
2. Clarke, de Silva, Thorley (2006) 或同类 minimum-variance 基准文献
3. DeMiguel, Garlappi, Uppal (2009)
4. Lohre, Opfer, Orszag (2012)
5. Künsch (1989) 或 Politis & Romano (1994)

### 5.3 三级可选（附录 / defense）
1. HRP
2. 更广义的 clustered / correlation-based allocation 扩展文献
3. 实现与可视化借鉴来源

---

## 6. 与各冻结文件的映射

### 对 `03A_contribution_claims.md`
- `C1`（统一框架与概念桥接）由 `Qian + Maillard + Choueifaty/Coignard + Menchero/Davis` 支撑；
- `C2`（协调模型）由 Chapter 3 与 Chapter 4 的桥接叙事支撑，而非单篇“现成文献”；
- `C4/C5`（实证与统计纪律）由 `Ledoit–Wolf + White + Bailey & López de Prado + bootstrap 文献` 支撑。

### 对 `06A_baseline_ladder.md`
- `CtR-only` ↔ `Qian / Maillard et al.`
- `MDP` ↔ `Choueifaty & Coignard`
- `GMV` ↔ minimum-variance literature
- `EW` ↔ DeMiguel et al. (2009)
- `HRP` ↔ López de Prado（附录/答辩补充）

### 对 `08A_statistical_validation.md`
- data snooping ↔ `White (2000)`
- Sharpe selection bias ↔ `Bailey & López de Prado (2014)`
- time-series dependence ↔ `Künsch (1989)` / `Politis & Romano (1994)`

### 对 `09_writing_contract_v2.md`
- Chapter 3–4 的写作骨架直接由本地图供给；
- Chapter 7–8 的引文最低配置由本地图锁定；
- “正文 / 附录 / defense” 的引用层级由本地图控制。

---

## 7. 正文使用规则（final-draft 版）

### 7.1 Chapter 3 的建议展开顺序
`Markowitz → Qian → Maillard et al. → 本文 CtR 记号、D_R 定义与 CtR-only`

### 7.2 Chapter 4 的建议展开顺序
`Choueifaty & Coignard → Menchero & Davis → diversified risk parity 相邻文献 → 本文 CtB、D_B 与 CtB-only`

### 7.3 Chapter 7–8 的建议展开顺序
`Ledoit–Wolf → baseline literature (GMV / 1N) → White → Bailey & López de Prado → bootstrap rationale → 本文实验制度与推断边界`

### 7.4 正文不应做的事
- 不按年份堆文献；
- 不把 CtB 段写成“分散化方法大全”；
- 不用大量扩展文献掩盖本文自身模型角色不清；
- 不让 HRP 或其他扩展方法抢占正文主比较集合。

---

## 8. 当前缺口状态与冻结建议

原 `lite` 版本中的三类缺口现已处理到 **可写作状态**：

1. **bootstrap 引文**：已补到可进入 Chapter 7 / Appendix 的程度；
2. **GMV / 1/N 主引文**：已补到可直接落笔的程度；
3. **CtB 相邻文献**：已补到足以支持 Chapter 4 与 defense 的程度。

仍允许的后续动作只有：

- 在正式 BibTeX 整理时补齐页码、卷期与 doi；
- 若 Chapter 4 写作需要，可再增加 1 篇 CtB 相邻文献作为 defense 补强；
- 不得再改变最小必引集合与正文主比较对象。

### 冻结建议
- 本文件建议从旧 `F3 rolling` 升级为 **F3 final-freeze candidate**；
- 待 Chapter 3、4、7 的正式引文已经落进正文后，可升级为 **final freeze**。

---

## 9. 本轮联动更新建议

### 保持冻结
- F1 全部不动；
- F2 全部不动；
- `experiment_registry_final.md`
- `figure_table_factory_final_v2.md`
- `chapter_feedback_loop_final.md`
- `defense_qa_bank_final.md`
- `final_PPT_script_v3.md`

### 继续滚动
- `09_writing_contract_v2.md`：待 chapter draft 落地后升级；
- 其他文献细节文件：仅允许 bibliographic completion，不允许改主线角色。

---

## 10. 当前版本状态

- Version: `v2.0`
- Freeze level: `F3 final-freeze candidate`
- Status: `Thesis-ready literature map aligned with clean-lineage writing`
