# 04_literature_map_lite.md

## 1. 文件目的与当前状态

本文件用于建立本项目的**轻量文献地图（literature map lite）**，服务以下目标：

1. 为论文各章提供**最小但充分**的核心引用集合；
2. 防止后续写作时临时堆砌文献、重复搜索或引用口径漂移；
3. 明确每篇文献在本项目中的**角色**：基础来源、核心支撑、比较对象、统计纪律、可视化借鉴；
4. 为 `chapter drafting`、`defense_qa_bank.md`、`final PPT/script` 提供统一的引用入口；
5. 与 `03A_contribution_claims.md` 对齐：只保留那些真正支撑研究主张的文献，不做泛泛而谈的文献堆叠。

**当前状态**：F3 rolling

> 说明：本文件是“轻量地图”，不是最终文献综述正文，也不是 BibTeX 数据库。它的任务是先冻结“哪些文献必须进场、各自支撑什么、优先写到哪一章”，后续再滚动补充。

---

## 2. 上位约束与依赖文件

本文件服从以下已冻结文件：

- `00_project_charter.md`
- `01_notation_master.md`
- `02_definition_formula_ledger.md`
- `03_thesis_skeleton.md`
- `03A_contribution_claims.md`
- `05_data_contract.md`
- `06_model_contract.md`
- `06A_baseline_ladder.md`
- `08A_statistical_validation.md`

因此，本文件不得改变以下已冻结事实：

1. 研究主线是 **CtR 主目标 + CtB 结构约束**；
2. 主文默认 long-only 大类资产 ETF 语境；
3. 主比较基准固定为 `EW / GMV / CtR-only / MDP / CtB-only / Main`；
4. 文献的作用首先是支撑理论对象、模型角色、比较设计与统计纪律，而不是把论文写成“风险平价大全”；
5. 若某类文献与项目主线关联很弱，只能进入附录或答辩补充，而不能挤占正文引用预算。

---

## 3. 使用规则

### 3.1 先映射角色，再扩展数量

后续新增文献必须先回答三个问题：

1. 它支撑哪一章、哪一节？
2. 它支撑“理论定义 / 建模选择 / 基准比较 / 统计验证 / 图表借鉴”中的哪一种角色？
3. 若删掉它，论文是否会损失关键论证？

若三问都回答不清，则该文献暂不进入主地图。

### 3.2 三层优先级

本文件对文献采用三层优先级：

- **Tier A（Must Cite）**：正文主线至少应直接引用一次；
- **Tier B（Strong Support）**：强支撑文献，通常进入正文或附录主表；
- **Tier C（Optional / Appendix）**：只在稳健性、比较对象或答辩补充中使用。

### 3.3 章节映射优先于年份堆砌

本文件禁止按“年份排序即完成综述”的写法。后续文献综述必须优先按以下维度组织：

- 基础理论；
- 风险贡献 / 风险预算；
- 相关结构 / 分散化；
- 比较基准与替代构造；
- 协方差估计与数值稳定；
- 统计验证与防过拟合。

### 3.4 不把工程文件伪装成学术创新

工程文档、包文档、产品白皮书可以作为“实现借鉴”或“解释借鉴”，但不能替代学术主引文；主张若涉及理论、方法或统计推断，优先对应论文、期刊文献或正式工作论文。

---

## 4. 章节引用预算（最低配置）

> 本节给出“每章至少应从哪些簇中抽文献”。这不是最终参考文献数量上限，而是**最低严肃配置**。

### 第 2 章：理论预备与经典框架

最低引用簇：

- Markowitz / mean-variance foundation
- Sharpe / index-model or CAPM background
- covariance estimation / shrinkage（用于说明实证为何不能直接裸用样本协方差）

### 第 3 章：CtR 与风险预算

最低引用簇：

- risk contribution interpretation
- ERC / equal risk contribution
- risk parity as baseline construction

### 第 4 章：CtB、相关结构与 long-only 可操作化

最低引用簇：

- diversification ratio / MDP
- x-sigma-rho risk attribution
- diversified risk parity / correlation-structure adjacent literature

### 第 5 章：CtR–CtB 协调模型

最低引用簇：

- 第 3 章 + 第 4 章的桥接文献
- 明确说明：本章创新主要来自**协调建模与制度化实现**，不是声称发现了一个已完全独立成熟的新经典范式

### 第 6 章：统一求解器与数值制度

最低引用簇：

- 以用户笔记中的“先梯度、后牛顿”为主；
- 外部文献仅作为数值实现常识或附录补充，不强制追求大量优化算法引用。

### 第 7–8 章：实验与结果

最低引用簇：

- 主比较基准对应文献；
- covariance estimation；
- statistical validation / data snooping / DSR。

---

## 5. 核心文献簇与条目

以下表格中的 `Chapter target` 使用简写：

- `Ch2` 理论预备
- `Ch3` CtR
- `Ch4` CtB
- `Ch5` 协调模型
- `Ch7` 实验设计
- `Ch8` 结果解释
- `App` 附录/答辩补充

### 5.1 Foundation：均值—方差与经典背景

| ID | 文献 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| F-01 | Markowitz (1952), *Portfolio Selection* | A | Foundation | Ch2 | 现代组合理论与均值—方差框架的原点 | 必引 |
| F-02 | Sharpe (1964), *Capital Asset Prices* | B | Foundation | Ch2 / App | CAPM 与市场组合背景；用于说明 Sharpe/指数模型谱系 | 不把本文写成 CAPM 论文 |
| F-03 | Ledoit & Wolf (2004), shrinkage covariance papers | A | Estimation | Ch2 / Ch7 | 说明实证中协方差估计应重视稳健性与条件数 | 服务 `05_data_contract.md` |

### 5.2 Risk Contribution / Risk Budgeting：CtR 主线

| ID | 文献 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| R-01 | Qian (2006), *On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up* | A | CtR | Ch3 | 为 CtR / risk budget 提供经济解释与“可加总”语义 | 必引 |
| R-02 | Maillard, Roncalli, Teiletche (2010), *The Properties of Equally Weighted Risk Contribution Portfolios* | A | ERC / Risk Parity | Ch3 / Ch7 | ERC 的经典基准文献；支撑 `CtR-only` baseline | 必引 |
| R-03 | Roncalli, factor/risk parity related work | B | Risk Parity Extension | Ch3 / App | 用于说明 risk parity 的扩展谱系 | 视篇幅选择 |

### 5.3 Diversification / Correlation-Structure：CtB 相邻主线

| ID | 文献 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| C-01 | Choueifaty & Coignard (2008), *Toward Maximum Diversification* | A | Diversification / MDP | Ch4 / Ch7 | 为 MDP 与相关结构型比较对象提供经典依据 | 必引 |
| C-02 | Menchero & Davis (2011), *Risk Contribution Is Exposure Times Volatility Times Correlation: Decomposing Risk Using the X-Sigma-Rho Formula* | A | Risk Attribution / Correlation | Ch4 / Ch5 / Ch8 | 支撑“相关结构”解释框架，为 CtB 的叙事提供桥梁 | 必引 |
| C-03 | Lohre, Opfer, Orszag (2012), diversified risk parity | B | Diversified RP | Ch4 / App | 说明风险预算与分散化/相关结构之间的中间地带 | 适合作为过渡文献 |

### 5.4 Alternative Baselines：可比但不抢主线

| ID | 文献 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| B-01 | minimum-variance literature（如 Clarke, de Silva, Thorley 2006） | B | Baseline | Ch7 / Ch8 | 支撑 GMV 的经典比较地位 | 至少选 1 篇 |
| B-02 | López de Prado (2016), *Building Diversified Portfolios that Outperform Out of Sample* | C | HRP | App / Defense | 支撑 HRP 只做附录或答辩补充，而非正文主比较集合 | 与 `06A` 对齐 |
| B-03 | 1/N naive diversification 文献（如 DeMiguel et al. 2009） | B | Baseline | Ch7 / Ch8 | 支撑 EW 作为必要但有限的朴素对照 | 可与 GMV 同组写 |

### 5.5 Statistical Validation：统计纪律与防过拟合

| ID | 文献 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| S-01 | White (2000), *A Reality Check for Data Snooping* | A | Statistical Validation | Ch7 / Ch8 / App | 支撑多模型/多参数搜索后的数据窥探风险讨论 | 必引 |
| S-02 | Bailey & López de Prado (2014), *The Deflated Sharpe Ratio* | A | Statistical Validation | Ch7 / Ch8 / App | 支撑 selection bias、non-normality 与 Sharpe 膨胀控制 | 必引 |
| S-03 | block bootstrap / stationary bootstrap references | B | Time-Series Inference | Ch7 / App | 支撑本文为何不用 naive IID t-test 作为唯一依据 | 后续可补更具体条目 |

### 5.6 Implementation / Visualization Borrowing：只作借鉴

| ID | 文献/来源 | Tier | 类别 | Chapter target | 在本项目中的角色 | 备注 |
|---|---|---|---|---|---|---|
| V-01 | risk parity / portfolio optimization package docs | C | Implementation | App / Defense | 借鉴图表与结果组织方式 | 不替代学术主引文 |
| V-02 | clustering / correlation heatmap visualization examples | C | Visualization | Ch8 / App | 借鉴相关矩阵排序热图、机制图表现形式 | 只作图表灵感 |

---

## 6. 当前最小“必引集合”

> 下列文献构成当前阶段的**最小严肃引用集合**。后续即使扩充，也不应删除这一层。

### 6.1 一级必引（正文主线）

1. Markowitz (1952)
2. Qian (2006)
3. Maillard, Roncalli, Teiletche (2010)
4. Choueifaty & Coignard (2008)
5. Menchero & Davis (2011)
6. Ledoit & Wolf (2004)
7. White (2000)
8. Bailey & López de Prado (2014)

### 6.2 二级强支撑（按篇幅择优进入正文）

1. Sharpe (1964)
2. diversified risk parity literature（如 Lohre et al.）
3. GMV / minimum variance classic baseline literature
4. 1/N inefficiency / naïve diversification literature

### 6.3 三级可选（附录、比较、答辩）

1. HRP
2. 更广泛的 clustering / risk budgeting 扩展文献
3. 工具文档、白皮书、图表灵感来源

---

## 7. 与各冻结文件的精确映射

### 对 `03A_contribution_claims.md`

- `C1`（统一框架与概念桥接）主要由 `Qian + Maillard + Choueifaty/Coignard + Menchero/Davis` 支撑；
- `C2`（协调模型）需要第 3、4 章的文献并置，而不是单一一篇“现成文献”；
- `C3`（统一求解器）以用户笔记为主，外部优化文献只作补强；
- `C4/C5`（实证与统计纪律）由 `Ledoit-Wolf + White + Bailey&López de Prado` 支撑。

### 对 `06A_baseline_ladder.md`

- `CtR-only` ↔ `Qian / Maillard et al.`
- `MDP` ↔ `Choueifaty & Coignard`
- `GMV` ↔ minimum-variance literature
- `EW` ↔ naïve diversification literature
- `HRP` ↔ López de Prado（只作附录/补充）

### 对 `08A_statistical_validation.md`

- data snooping ↔ `White (2000)`
- Sharpe selection bias ↔ `Bailey & López de Prado (2014)`
- time-series dependence ↔ 后续补 bootstrap 具体文献

---

## 8. 当前缺口与后续补充规则

### 8.1 当前明确缺口

本地图目前仍有三个“待补细化区”：

1. **CtB 直接命名文献仍偏少**：后续可继续补与“asset-to-portfolio correlation equalization / correlation parity / diversified risk parity”更直接相关的条目；
2. **bootstrap 具体实现文献尚未选定最终版本**；
3. **GMV / 1/N 的最终主引文** 可在写第 7 章时再精确补齐一到两篇。

### 8.2 允许新增的情况

只有在以下情况之一成立时，才建议把新文献加入主地图：

- 它直接填补上述三类缺口；
- 它能显著强化第 4 章 CtB 的文献合法性；
- 它是后续正式进入正文主表或主图比较对象所必需的经典文献；
- 它能显著改善答辩时对“为什么这样做而不是那样做”的回答。

### 8.3 不建议新增的情况

以下情况不建议把文献加入主地图：

- 只是同主题的“又一篇应用文章”；
- 只提供相似经验结论但不能增加理论或方法辨识度；
- 与本项目主线相关性弱，仅因为“被引多”而想加入；
- 会诱导论文从 CtR–CtB 协调主线偏移到别的框架。

---

## 9. 后续写作执行规则

### 9.1 写第 3 章时

优先从以下序列展开：

`Markowitz → Qian → Maillard et al. → 本文 CtR 记号与 long-only 可操作化`

### 9.2 写第 4 章时

优先从以下序列展开：

`Choueifaty & Coignard → Menchero & Davis → diversified risk parity / correlation-structure adjacent works → 本文 CtB 定义与 long-only 离散度`

### 9.3 写第 7–8 章时

优先从以下序列展开：

`Ledoit–Wolf → baseline literature → White → Bailey & López de Prado → 本文实验制度`

---

## 10. 冻结建议

当前建议：

- 本文件继续保持 **F3 rolling**；
- 待以下条件全部满足后，再考虑最终冻结：
  1. `synthetic / toy experiments` 已完成并能对应第 4 章与第 5 章的机制图；
  2. `minimal real ETF run` 已完成并确认主比较对象不会再改；
  3. 第 3、4、7 章草稿已各自完成一版；
  4. CtB 直接相邻文献缺口已补到可答辩水平。

在此之前，本文件允许滚动补充，但禁止改变：

- 核心文献簇的分类逻辑；
- “最小必引集合”；
- HRP 只作附录/补充的定位；
- 统计验证文献必须进入主线的规则。
