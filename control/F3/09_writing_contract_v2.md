# 09_writing_contract.md

## 0. 文件目的与当前状态

本文件用于冻结本项目的**论文写作契约（writing contract）**，使后续章节正文、图注、表注、附录、答辩口径与 PPT 脚本都服从同一套稳定标准。

它回答以下问题：

1. 论文正文应按什么逻辑链写；
2. 每章允许写什么、不允许写什么；
3. 记号、术语、公式、图表、结果解释与统计措辞如何统一；
4. 哪些结论可以进入主文，哪些只能进入附录、robustness 或答辩补充；
5. 如何把 F1 / F2 / F3 文件、clean 主线结果与已落地图表稳定映射到正文；
6. 每次章节推进后，哪些文件需要更新、哪些文件可以冻结；
7. 如何在不破坏已冻结主线的前提下，把论文推进到最终可提交状态。

**当前状态**：F3 final-freeze candidate  
**版本**：v2.0  
**定位**：正文生产制度，而非写作建议清单。

---

## 1. 上位约束与服从关系

本文件完全服从以下已冻结或已接受文件：

### F1（硬冻结）
- `00_project_charter.md`
- `01_notation_master.md`
- `02_definition_formula_ledger.md`
- `03_thesis_skeleton.md`

### F2（理论稳定冻结）
- `03A_contribution_claims.md`
- `05_data_contract.md`
- `06_model_contract.md`
- `06A_baseline_ladder.md`
- `07_solver_contract.md`
- `08_result_contract.md`
- `08A_statistical_validation.md`

### F3（clean 主线与写作相关）
- `04_literature_map_lite.md`
- `synthetic_toy_experiments_v8.md`
- `minimal_real_etf_run_v5.md`
- `calibration_protocol_v8.md`
- `full_experiments_v8.md`
- `figure_table_factory_final_v2.md`
- `inference_package_v3.md`
- `solver_reliability_protocol_v3.md`
- `experiment_registry_final.md`
- `gmv_decoupling_protocol_v3.md`
- `chapter_feedback_loop_final.md`
- `defense_qa_bank_final.md`
- `final_PPT_script_v3.md`

本文件不得改写以下已冻结事实：

1. 研究主线固定为：**CtR 主目标 + CtB 结构约束 / 容忍带**；
2. 主经验语境固定为：**long-only 大类资产 ETF 组合**；
3. 主比较对象固定为：`EW / GMV / CtR-only / MDP / CtB-only / Main`；
4. 主符号固定为：`x, \Sigma, CtR, CtB, D_R, D_B, \delta, \eta, \gamma, \rho`；
5. clean 主线结果固定为：`d08` 是 validation 选出的主规格，`d04` 是 stricter-band robustness 规格；
6. 第 8 章主结果口径固定为：**Main 不是 return champion，而是 mechanism-consistent compromise model**；
7. 正文不得使用 test 集回头重选主规格，不得把结构改善偷换成收益全面优越。

---

## 2. 论文必须呈现的闭环逻辑

整篇论文必须读成一条闭合学术论证链，而不是实验日志、软件说明书或文献拼贴：

> 研究问题 → 统一记号与数学对象 → CtR 理论 → CtB 理论 → CtR–CtB 协调模型 → 统一求解器 → 数据与实验制度 → 校准规则 → 主结果与机制解释 → 统计支持 → 局限与边界

若一段文字无法判断自己属于这条链上的哪个节点，则默认不应进入正文主线。

---

## 3. 全局写作原则

### 3.1 结果优先，修辞服从结果
正文必须先说明“结果是什么”，再说明“这意味着什么”。
不得先写强结论，再倒找图表或统计结果配合。

### 3.2 机制优先于绩效排名
本文不是单纯的收益竞赛论文。正文的核心不是“谁收益最高”，而是：

- 风险配置如何变化；
- 相关结构如何变化；
- CtB band 何时激活；
- 结构控制带来什么代价；
- 为什么这些变化支持本文的主模型解释。

### 3.3 无证据链主张不得进入主文
正文每个关键判断必须至少落在以下之一：

- 已冻结定义或命题；
- 已冻结模型公式；
- 已落地图 / 表；
- clean-lineage 结果文件；
- inference 记录；
- solver reliability 记录；
- calibration 记录。

### 3.4 不跨层漂移
同一对象在以下层面必须保持同义：

- 数学定义；
- 代码对象；
- 结果字段；
- 图题 / 表题；
- 正文表述；
- 答辩表述；
- PPT 表述。

### 3.5 论文不是 README
正文不得写成：

- changelog；
- debugging memo；
- 执行日志；
- 脚本说明书；
- CSV 字段解说。

执行标识、路径、run id、文件树等只允许进入 reproducibility appendix 或 experiment registry appendix。

---

## 4. 语体、句法与表面风格契约

### 4.1 总体语体
采用**规范、克制、学术化、偏分析型**写法。
避免：

- 口语化过渡；
- 夸饰性词语；
- 营销式表达；
- 空泛抒情；
- defense-style 口头句式直接进入正文。

### 4.2 推荐主语
优先使用：

- “本文”
- “本研究”
- “本章”
- 必要时采用被动学术句式

避免过多第一人称单数口吻。

### 4.3 时态规则
- **现在时**：定义、恒等式、模型陈述、稳定解释；
- **过去时**：已执行的校准过程、已完成的经验实验、已获得的测试样本结果；
- **将来时**：只用于结论中的未来研究，不用于正文主结果段。

### 4.4 句长与信息密度
优先使用中等长度句子，一句表达一个主判断。
长句只有在逻辑关系明确、标点清楚、不会引起歧义时才允许。

### 4.5 禁止“AI 化表面信号”
避免：

- 连续同构句模板；
- 同义词堆叠；
- 无信息增强的“非常 / 极其 / 明显地”泛滥使用；
- 机械化“第一、第二、第三”堆段；
- 明显为了显得完整而重复解释同一意思。

---

## 5. 统一记号与术语契约

### 5.1 记号唯一来源
所有符号必须服从 `01_notation_master.md`。
若某符号已经冻结，后文不得因风格偏好改写为其他主符号。

### 5.2 不允许跨章改名
相同数学对象不得在不同章节中改名，包括：

- theory chapter；
- model chapter；
- solver chapter；
- empirical chapter；
- captions；
- appendix。

### 5.3 必须统一使用的主术语
- 风险贡献：`CtR`
- 篮子相关性 / 与组合相关结构：`CtB`
- CtR 离散度：`D_R`
- CtB 离散度：`D_B`
- 主模型：`Main`
- `CtR-only`
- `CtB-only`
- `MDP`
- `GMV`
- `band active`
- `smooth term`
- `L2 term`
- `band penalty`

### 5.4 禁止的术语漂移
不得把：

- `CtB` 写成第二种风险贡献；
- `D_B` 写成普通协方差惩罚而不说明其结构角色；
- `\rho` 写成经济偏好参数；
- `\delta` 写成风险厌恶系数；
- `\gamma` 写成收益偏好参数；
- `Main` 写成对称双目标模型。

---

## 6. 公式写作契约

### 6.1 正文公式分层
正文公式只分四类：

1. **定义公式**：必须入正文；
2. **主模型公式**：必须入正文；
3. **求解器核心公式**：正文给主版本，细节可去附录；
4. **冗长推导 / 技术证明**：默认放附录。

### 6.2 正文必须出现的核心公式
正文至少必须显式给出：

- 组合波动率 \(\sigma_p(x)=\sqrt{x^\top \Sigma x}\)；
- CtR 定义；
- CtB 定义；
- \(D_R(x;b)\) 定义；
- \(D_B(x)\) 定义；
- `CtR-only` 模型；
- `CtB-only` 模型；
- `Main` 主模型；
- `Main` 的软约束数值实现型；
- Projected Gradient 核心更新；
- Damped / reduced-coordinate Newton 的核心表达。

### 6.3 公式引用规则
- 关键公式必须编号；
- 首次出现必须解释新符号；
- 后文引用写为“由式 (5.3) 可知……”，不得写会跨页漂移的“由上式可知”；
- 结构上重要的公式定义一次后应反复引用，不要做无必要的轻微改写重述。

### 6.4 公式数量纪律
每节只保留真正服务该节论证的公式。
不得为了“显得数学充分”而堆砌没有后续作用的公式。

---

## 7. 图表写作契约

### 7.1 图表不是装饰，而是证据节点
每一张图 / 表都必须回答一个明确问题。
如果某图 / 表无法回答问题或不承载正文判断，则默认不应进入主文。

### 7.2 主文固定图集合
主文图集合固定为：

1. Figure 7.1 — calibration heatmap
2. Figure 8.1 — Main trade-off map
3. Figure 8.2 — rolling structural comparison
4. Figure 8.3 — capital allocation vs CtR contribution mirror bars
5. Figure 8.4 — cumulative return and drawdown

### 7.3 主文固定表集合
主文表集合固定为：

1. Table 7.1 — calibration screening summary
2. Table 8.1 — overall performance and trading
3. Table 8.2 — structural mechanism summary
4. Table 8.3 — solver reliability summary

### 7.4 附录固定主表
附录固定主表为：

1. Table A.1 — d08 vs d04 robustness
2. Table A.2 — inference summary
3. Table A.3 — solver failure catalog

### 7.5 图表插入三句法
每张图 / 表进入正文时，必须同时具备：

1. **引入句**：为什么看它；
2. **观察句**：从图 / 表中观察到什么；
3. **解释句**：这对本文主张意味着什么。

不得把图表直接贴上去而不解释。

### 7.6 图表不支持的结论
不得：

- 从 Figure 8.4 直接推出“Main 最优”；
- 从 Figure 8.1 直接推出“Main 全面主导”；
- 从 solver summary 推出“算法普适最优”；
- 从 robustness 表推出“d04 比 d08 更适合作为主规格”。

### 7.7 图注 / 表注风格
图注与表注必须：

- 事实化；
- 短到中等长度；
- 解释感知但不写成段落小作文；
- 与正文口径一致；
- 不出现 run id、脚本名、路径名。

---

## 8. 结果解释契约

### 8.1 第 8 章结果解释顺序
结果解释顺序固定为：

1. 结构机制结果（\(D_B\), CtB, band）
2. 风险配置结果（\(D_R\), CtR, capital-vs-contribution）
3. 交易与实现结果（turnover, solver reliability）
4. 绩效结果（return, sharpe, drawdown）

即：**先结构，后配置，再实现，最后绩效。**

### 8.2 关于 Main 的固定表述
clean 主线下，正文必须保持以下口径：

- Main 不是原始绩效赢家；
- Main 相对 `CtR-only` 显著降低 \(D_B\)；
- 这一结构改善伴随更高的 \(D_R\) 与 turnover；
- Main 相对 `EW` 与 `GMV` 在结构指标上更有解释价值；
- 本文不主张 Main 在收益维度支配 `EW` 或 `GMV`。

### 8.3 robustness 段固定表述
关于 `d04` 相对 `d08`，正文固定写法为：

- 收紧 CtB band 会进一步降低 \(D_B\)；
- 同时抬高 \(D_R\) 与 turnover；
- 这说明 band 参数具有可解释的结构作用；
- `d04` 是 stricter-band robustness specification，而不是更优主规格。

### 8.4 solver 段固定表述
solver 段应写：

- clean-lineage aggregate 显示 accepted minimal 与 full 阶段成功率为 1.0；
- GMV 在 decoupling 后数值上干净；
- Main / `CtR-only` 的有限 fallback 应解释为保护机制，而不是失败伪装；
- solver 结果支撑“求解制度可靠”，而不是“算法对所有问题最优”。

### 8.5 inference 段固定表述
统计推断段应：

- 用来约束主张，而不是放大主张；
- 若不支持 return dominance，则不得通过换句式暗示“全面更优”；
- 主要服务“结构改善是否稳定”与“非支配结论的克制表达”。

---

## 9. 统计措辞契约

### 9.1 允许的措辞
允许：

- “显著降低 / 显著提高”
- “具有统计支持”
- “置信区间不跨零”
- “未观察到收益支配的统计支持”

### 9.2 禁止的措辞
避免：

- “证明了市场规律”
- “绝对优于”
- “必然提高收益”
- “在所有情形下成立”
- “收益显著更优” （若 inference 并不支持）

### 9.3 统计范围边界
所有推断性表述只适用于：

- 当前 ETF universe；
- 当前 sample split；
- 当前 calibration protocol；
- 当前 bootstrap 设计；
- 当前主模型与基准集合。

不得外推到“所有市场”或“所有资产配置问题”。

### 9.4 描述统计与推断统计不得混写
不得把：

- point estimate；
- bootstrap CI；
- 显著性判断

混在同一句里而不加区分。

---

## 10. 章节级写作契约

### 10.1 正式写作顺序（冻结）
1. 第 3 章 CtR
2. 第 4 章 CtB
3. 第 5 章 协调模型
4. 第 6 章 统一求解器
5. 第 7 章 数据、实验设计与校准
6. 第 8 章 实证结果与机制解释
7. 第 1 章 引言
8. 摘要、结论、附录

### 10.2 Chapter 1 引言
允许写：研究背景、研究问题、贡献摘要、方法概览、章节安排。  
不允许写：抢先汇报大量具体数值结果、夸大绩效、先于正文下强结论。

### 10.3 Chapter 2 理论预备与统一记号
允许写：收益、协方差、组合收益、long-only 可行域、Markowitz / Sharpe 背景、统一记号表。  
不允许写：过早展开 calibration、ETF 结果图或 test-set 结论。

### 10.4 Chapter 3 CtR
必须做到：
- 定义 CtR、MRC、标准化 CtR share；
- 说明 ERC / risk budgeting 与本文关系；
- 给出 \(D_R\) 及其在主模型中的角色；
- 在章末完成“为什么 CtR 适合作为主配置器”的过渡。

### 10.5 Chapter 4 CtB
必须做到：
- 明确 CtB 是相关结构量；
- 说明 CtR–CtB 的联系与区别；
- 说明 CtB-only 的数学与数值复杂性；
- 在章末完成“为什么 CtB 更适合进入结构层”的过渡。

### 10.6 Chapter 5 协调模型
必须做到：
- 正式提出 Main；
- 解释为何不采用对称双目标；
- 解释参数分层；
- 解释硬约束与软约束实现的关系；
- 固定主从口径：CtR 主目标，CtB 结构约束。

### 10.7 Chapter 6 求解器
必须做到：
- 说明为何采用 PG → Newton；
- 给出统一 solver interface；
- 写清 stop rule / fallback / diagnostics；
- 把实现细节与论文主叙事分层。  
不允许写成软件手册或大段贴代码。

### 10.8 Chapter 7 数据与实验制度
必须做到：
- 解释 ETF universe；
- 解释 split、covariance estimator、rebalance 制度；
- 解释 calibration protocol；
- 解释为什么 `d08` 是主规格、`d04` 是 robustness；
- 解释统计验证边界。  
不允许写：用 test 集回头改主规格。

### 10.9 Chapter 8 结果
必须做到：
- 按“结构 → 配置 → 交易 → 绩效”顺序写；
- 每张主图 / 主表都给出问题、观察、解释；
- 明确非主张：不说 return dominance；
- 明确 `d04` 是 stricter-band robustness，而非主替代规格。

### 10.10 Chapter 9 结论
必须做到：
- 把贡献与证据闭环；
- 区分理论、方法、实证、制度贡献；
- 诚实写局限；
- 给未来研究方向。  
不允许重新发明新的贡献点。

---

## 11. 文献写作契约

### 11.1 文献角色分层
正文中的文献只服务四种角色：

1. 理论背景；
2. 方法对照；
3. 结果解释辅助；
4. 图表 / 风格借鉴。

### 11.2 引用组织原则
- 文献综述按“对象—方法—差异”组织，不按年份堆砌；
- 每章只引用真正服务该章问题的文献；
- 不用文献堆砌来掩盖本文自身逻辑不清。

### 11.3 最小必引纪律
正文主线至少应覆盖 literature map 中的一级必引集合；
GMV / 1/N / bootstrap 的补强引文，可在写第 7–8 章时精确补齐。

### 11.4 不允许的引用方式
避免：

- “大量研究表明……”而不给对象；
- “已有文献充分证明……”却不解释与本文区别；
- 在 CtB 段落引用文献却不说明为何本文仍采用结构约束化而非替代 CtR。

---

## 12. 附录边界契约

### 12.1 必须在正文出现的内容
- 主定义；
- 主模型；
- 核心命题；
- 主校准逻辑；
- 主图表；
- 第 8 章核心结论；
- 非主张边界。

### 12.2 应进入附录的内容
- 冗长推导；
- 技术证明；
- 额外 robustness 表；
- inference 细节；
- solver failure catalog；
- 复现说明与 execution registry。

### 12.3 禁止偷放附录的内容
不得把以下内容为了压缩正文而偷偷放入附录：

- Main 的正式定义；
- \(D_R\)、\(D_B\) 的最终经验定义；
- `d08` 的选择逻辑；
- Main 非收益冠军但结构上受支持的核心解释。

---

## 13. Run ID / 路径 / 结果原件写法边界

### 13.1 正文禁用项
正文不得直接出现：

- run id；
- 时间戳目录名；
- 脚本名；
- 文件路径；
- `csv/json` 字段名；
- 机器相关执行细节。

### 13.2 允许出现的位置
这些内容只允许进入：

- reproducibility appendix；
- experiment registry appendix；
- supplementary archive；
- 内部项目记录。

### 13.3 原始输出到论文语句的翻译规则
原始输出必须被翻译为：

- 机制解释；
- 相对比较；
- 受约束的结论；
- 与图表和模型一致的学术表述。

---

## 14. 自动更新与冻结规则

### 14.1 每次新增正文内容后的自动检查顺序
以后每次新增正文、图注、表注、答辩或 PPT 内容，默认都自动检查：

1. 是否触及 F1 记号、定义或章节主线；
2. 是否触及 F2 贡献边界、数据政策、模型角色、baseline、solver、结果契约、统计纪律；
3. 是否触及 F3 文献地图、实验解释、图表工厂、chapter feedback、defense bank、PPT script；
4. 是否触及 clean-lineage 主规格、robustness 口径、solver reliability 口径；
5. 是否触及当前 writing contract 自身。

### 14.2 触发更新的映射表
- 改动术语 / 符号 → 检查 `01_notation_master.md`, `02_definition_formula_ledger.md`
- 改动章节逻辑 → 检查 `03_thesis_skeleton.md`
- 改动贡献口径 → 检查 `03A_contribution_claims.md`
- 改动数据 / split / universe → 检查 `05_data_contract.md`
- 改动模型解释 → 检查 `06_model_contract.md`
- 改动基准集合 → 检查 `06A_baseline_ladder.md`
- 改动求解器叙述 → 检查 `07_solver_contract.md`
- 改动结果结构与图表映射 → 检查 `08_result_contract.md`, `figure_table_factory_final_v2.md`
- 改动统计措辞边界 → 检查 `08A_statistical_validation.md`, `inference_package_v3.md`
- 改动主结果口径 → 检查 `chapter_feedback_loop_final.md`, `defense_qa_bank_final.md`, `final_PPT_script_v3.md`
- 改动复现链或 run 角色 → 检查 `experiment_registry_final.md`, `solver_reliability_protocol_v3.md`, `calibration_protocol_v8.md`
- 改动正文生产制度 → 检查 `09_writing_contract.md`

### 14.3 冻结升级条件
`09_writing_contract.md` 从 **F3 final-freeze candidate** 升级到 **final freeze**，必须同时满足：

1. Chapter 3–8 主文完成；
2. Chapter 1、摘要、结论完成；
3. Figure 7.1 / 8.1 / 8.2 / 8.3 / 8.4 与 Table 7.1 / 8.1 / 8.2 / 8.3 / A.1 / A.2 / A.3 全部落地并编号稳定；
4. defense 口径与本文件一致；
5. 不再新增章节级写作制度；
6. `project_gap_audit.md` 已被更新为收口版或明确标记 superseded。

---

## 15. 本轮冻结建议与联动更新

### 15.1 本轮建议冻结
- `09_writing_contract.md`：升级为 **F3 final-freeze candidate**
- `experiment_registry_final.md`：保持 **F3 final freeze**
- `figure_table_factory_final_v2.md`：保持 **F3 final freeze**
- `chapter_feedback_loop_final.md`：保持 **F3 final freeze**
- `defense_qa_bank_final.md`：保持 **F3 final freeze**
- `final_PPT_script_v3.md`：保持 **F3 final freeze**

### 15.2 本轮建议继续滚动更新
- `04_literature_map_lite.md`：继续 **F3 rolling**，待补 bootstrap / GMV / 1/N 主引文后再冻结；
- `project_gap_audit.md`：必须更新为收口版，否则与 clean 完成态冲突；
- `calibration_protocol_v8.md`：建议从“后续动作单”改写为“已完成校准记录”。

### 15.3 本轮不建议改动
- 所有 F1 文件：不改；
- `03A_contribution_claims.md`、`05–08A`：不改；
- `synthetic_toy_experiments_v8.md`、`minimal_real_etf_run_v5.md`、`full_experiments_v8.md`：不因正文写作而回改主结论。

---

## 16. 最终接受的主文措辞骨架

以下表述方向视为当前接受版本：

- Main 是 thesis model，因为它以 CtR 作为主目标、以 CtB 作为结构约束；
- 相对 `CtR-only`，Main 显著改善目标结构指标，但以更高的 CtR 偏离与 turnover 为代价；
- 相对 `CtB-only`，Main 保留更多 CtR 结构并降低 turnover，但放弃部分 CtB 紧度；
- 相对 `EW` 与 `GMV`，Main 不主张收益支配，但可以被支持为结构上更优、数值上可靠的 compromise model；
- `d08` 是主规格，因为它由 validation protocol 选出；
- `d04` 是 strict-band robustness specification，而不是 test-set 反选出的替代主模型；
- 本文的 empirical contribution 是 reproducible mechanism study，而不是收益冠军叙事。

---

## 17. 当前版本状态

- Version: `v2.0`
- Freeze level: `F3 final-freeze candidate`
- Status: `Clean-lineage aligned and chapter-ready`
- Next gate: `Chapter drafting completion + output-layer stabilization + gap-audit cleanup`

