# calibration_protocol_cleanfreeze_v2.md

## 0. 文件目的与当前状态

本文件是对 `calibration_protocol_v8.md` 的 clean 收口更新与重命名版本。  
其任务不再是记录“校准完成后下一步做什么”，而是冻结：

1. validation calibration 的 accepted selection rule；
2. `d08` 与 `d04` 的最终角色分工；
3. clean-rerun 对参数解释的影响；
4. downstream clean chain 已完成后的写作口径。

**当前状态**：F3 final freeze  
**Supersedes**：`calibration_protocol_v8.md`

---

## 1. Accepted calibration scope

本项目接受的校准阶段是：

- Stage: validation calibration
- Directory lineage: `calibration__main__val__20260419__01`
- Accepted main choice: `d08`
- Accepted strict-band robustness choice: `d04`

本文件只对 accepted clean lineage 负责，不引用 legacy、superseded 或 pre-clean 校准尝试。

---

## 2. Final parameter role assignment

### 2.1 Main specification
`d08 = (delta=0.02, eta=0.05, gamma=0.001, rho=100.0)`

### 2.2 Strict-band robustness specification
`d04 = (delta=0.01, eta=0.05, gamma=0.001, rho=100.0)`

### 2.3 Final role split
- `d08`：main specification
- `d04`：strict-band robustness specification

这一角色分工在 clean rerun 后保持不变。

---

## 3. What the clean rerun established

clean-rerun validation 对 `d04` 的确认表明：

1. `d04` 依然是有效的 stricter-band robustness candidate；
2. 它没有推翻 `d08` 作为 main specification 的地位；
3. validation protocol 的主规格选择没有被 clean rerun 改写。

换言之，clean rerun 的作用是**确认角色稳定**，不是触发重新选参。

---

## 4. Interpretation freeze

相对 `CtR-only`，`Main(d04)` 延续了 tighter-band 的预期模式：

- 更强的 `D_B` 压缩；
- 更大的 `D_R` 牺牲；
- 更高的 turnover 倾向。

因此，`d04` 的意义是：

> 它验证了收紧 CtB band 的结构后果具有方向一致、可解释、可复现的特征。

它不意味着：

- `d04` 在整体上优于 `d08`；
- 应在看到 test 后把 `d04` 升格为主规格；
- tighter band 一定带来更好绩效。

---

## 5. Selection rule freeze

本项目关于 calibration 的最终选择纪律如下：

1. 主规格必须由 validation protocol 选出；
2. test-set 结果不得用于替换主规格；
3. `d04` 在 full stage 中只作为 robustness，不作为 re-selection 候选；
4. calibration 的任务是选定 main specification，而不是在 test 阶段追求 ex post 表现更优参数。

---

## 6. Downstream completion record

原 `calibration_protocol_v8.md` 中 “Proceed with ...” 的后续动作现已全部完成：

1. `full_test.yaml` using `d08` → completed  
2. `full_test_d04.yaml` for robustness → completed  
3. `run_inference.py` → completed  
4. `aggregate_solver_reliability.py` → completed  

对应 clean downstream chain 已在以下文件中冻结：

- `full_experiments_v8.md`
- `inference_package_v3.md`
- `solver_reliability_protocol_v3.md`
- `experiment_registry_final.md`

因此，本文件现在是**完成态记录**，而不是待执行动作单。

---

## 7. Chapter-writing consequences

### Chapter 7
必须写明：

- `d08` 是由 validation protocol 选出的主规格；
- `d04` 是 stricter-band robustness specification；
- test performance 未被用于替换 `d08`。

### Chapter 8
必须写明：

- `d04` 相对 `d08` 进一步压低 `D_B`；
- 同时提高 `D_R` 与 turnover；
- 这支持“band 参数具有可解释结构作用”的主张；
- 该比较是 robustness evidence，不是 model-selection evidence。

### Defense / PPT
必须保持：

- “Why not promote d04?”  
  答案：因为那会把 test 用作 re-selection；
- “What does d04 prove?”  
  答案：它证明 tighter band 的结构效应是稳定且可解释的。

---

## 8. Freeze impact

### F1
不变。

### F2
不变。

### F3
本文件由 rolling update 升级为 **final freeze**，因为：
- 角色分工已固定；
- downstream clean chain 已完成；
- chapter / defense / PPT 的解释口径已同步。

---

## 9. 联动文件检查

若未来改动以下任一口径，必须回查本文件：

- `d08` / `d04` 的角色分工；
- calibration 与 test 的边界；
- robustness 与 re-selection 的区别；
- Chapter 7 / Chapter 8 对 `d04` 的叙述；
- defense / PPT 中关于参数选择的答法。

关联文件：
- `full_experiments_v8.md`
- `chapter_feedback_loop_final.md`
- `defense_qa_bank_final.md`
- `final_PPT_script_v3.md`
- `09_writing_contract_v2.md`

---

## 10. 当前版本状态

- Version: `v2.0`
- Freeze level: `F3 final freeze`
- Status: `Calibration selection rule closed and downstream-complete`
