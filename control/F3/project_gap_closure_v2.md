# project_gap_closure_v2.md

## 0. 文件目的与当前状态

本文件是对 `project_gap_audit.md` 的收口更新与重命名版本。  
它的任务不再是列出“还没做的 clean-run 核心实验”，而是明确：

1. 哪些**核心经验缺口已经关闭**；
2. 哪些工作仍然存在，但已经降级为**写作层 / 输出层 / 附录层任务**；
3. 哪些事项明确**不再属于必要经验缺口**；
4. 当前项目距离“全项目最终冻结”还差哪几步。

**当前状态**：F3 final freeze  
**Supersedes**：`project_gap_audit.md`

---

## 1. 收口结论

基于 clean 主线结果、accepted lineage、inference、solver reliability 与 figure/table factory，  
原 `project_gap_audit.md` 中的核心“Necessary now”事项，现已全部完成或被正式降级。

因此：

> **项目当前已不存在新的必要经验缺口（no remaining necessary empirical gap）。**

剩余工作属于：

- 正文写作；
- 图表与表格导出核对；
- 附录与复现材料整理；
- 答辩与 PPT 收束；
- 少量文献补齐与措辞收紧。

---

## 2. 已关闭的核心缺口（Closed core gaps）

### 2.1 Statistical inference pack
已关闭。  
`inference_package_v3.md` 已确认 clean inference 运行与最终允许主张：

- Main vs `CtR-only`：支持结构改善与 turnover 代价，不支持 return superiority；
- Main vs `EW` / `GMV`：支持结构指标改善，不支持收益支配叙事。

### 2.2 GMV reliability fix / demotion
已关闭。  
`gmv_decoupling_protocol_v3.md` 已将 GMV 的旧 caveat 降格为“先前实现问题，现已通过 dedicated implementation 解决”，并允许其作为 clean low-volatility baseline 保留在主文中。

### 2.3 Full robustness run for `d04`
已关闭。  
`full_experiments_v8.md` 已确认 `full__robust__d04__20260419__01`，并固定 `d04` 为 stricter-band robustness specification，而非替代主规格。

### 2.4 Aggregated solver reliability summary
已关闭。  
`solver_reliability_protocol_v3.md` 已给出 accepted clean-lineage aggregate，并锁定“只使用 clean lineage，不引用 legacy / superseded / pre-fix runs”。

### 2.5 Claim–evidence matrix
已关闭到 thesis-ready 水平。  
`experiment_registry_final.md` 已经把主张、run 角色、主规格、robustness、inference、solver reliability 放进一条接受的 clean evidence lineage。

### 2.6 Final limitations / non-claims register
已关闭到写作可用水平。  
`chapter_feedback_loop_final.md` 与 `defense_qa_bank_final.md` 已明确 Main 的非主张边界，不允许收益冠军式夸张表述。

---

## 3. 当前剩余事项（Remaining tasks, non-empirical）

以下事项仍存在，但不再属于“经验缺口”：

### 3.1 Main-text writing closure
- 完成 Chapter 3–8 正文；
- 回填 Chapter 1、摘要、结论；
- 将 `09_writing_contract_v2.md` 的章级纪律真正落实到草稿中。

### 3.2 Output-layer stabilization
- 复核 Figure 7.1 / 8.1 / 8.2 / 8.3 / 8.4；
- 复核 Table 7.1 / 8.1 / 8.2 / 8.3 / A.1 / A.2 / A.3；
- 检查图号、表号、caption、正文引用是否完全一致。

### 3.3 Appendix / reproducibility packaging
- 组织 appendix inference summary 与 solver failure catalog；
- 整理 reproducibility appendix；
- 明确 run registry 与 supplementary archive 的边界。

### 3.4 Literature completion
- 将 `04_literature_map_thesisready_v2.md` 中的 bootstrap / GMV / 1/N 主引文正式落入 BibTeX；
- 在 Chapter 4 或 defense 材料中酌情补 1 篇 CtB 相邻补强文献。

### 3.5 Defense / PPT synchronization
- 确保 `chapter_feedback_loop_final.md`、`defense_qa_bank_final.md`、`final_PPT_script_v3.md` 与 Chapter 7–8 主叙事完全同口径；
- 不允许 defense/PPT 使用比正文更强的结论。

---

## 4. 明确不再必要的事项（Not necessary anymore）

以下事项不再属于必要动作，不应重新打开作为主线任务：

1. 新的 toy 扩展实验；
2. 新 universe；
3. 新 baseline 主比较对象；
4. 新 covariance estimator 主线替换；
5. 再次用 test 结果回头重选主规格；
6. 新的 full-run robustness 追加到主文；
7. 以“补数据”或“补实验”为名重新打开 clean-run 已完成事项。

---

## 5. 当前项目的真正阻塞点（True remaining gates）

从“能跑完 clean 主线”到“能最终提交论文”，当前真正阻塞点只有四类：

1. **Chapter drafting completion**  
2. **Output-layer consistency**  
3. **Appendix / reproducibility organization**  
4. **Final wording discipline**

其中，最关键的不是新增结果，而是防止在写作阶段发生：

- 记号漂移；
- 结果夸张；
- 图表与正文脱节；
- defense / PPT 口径强于正文；
- 将 robustness 误写成 re-selection。

---

## 6. 最优推进顺序（post-clean sequence）

建议后续顺序固定为：

1. 锁定 `09_writing_contract_v2.md`
2. 完成 Chapter 3–8 主文
3. 复核并稳定图表 / 表格输出层
4. 回写 Chapter 1、摘要、结论
5. 完成附录与复现组织
6. 最后统一 defense / PPT / final freeze

---

## 7. 冻结影响

### 建议保持 final freeze
- `experiment_registry_final.md`
- `full_experiments_v8.md`
- `inference_package_v3.md`
- `solver_reliability_protocol_v3.md`
- `gmv_decoupling_protocol_v3.md`
- `figure_table_factory_final_v2.md`
- `chapter_feedback_loop_final.md`
- `defense_qa_bank_final.md`
- `final_PPT_script_v3.md`

### 建议滚动更新
- `09_writing_contract_v2.md`
- 各 chapter drafts
- `04_literature_map_thesisready_v2.md`（仅限 bibliographic completion）
- appendix / reproducibility 文件

### 明确 superseded
- `project_gap_audit.md` 现应视为 **superseded by closure memo**，不再作为当前状态判断依据。

---

## 8. 当前版本状态

- Version: `v2.0`
- Freeze level: `F3 final freeze`
- Status: `Core empirical gaps closed; remaining work is writing/output-layer only`
