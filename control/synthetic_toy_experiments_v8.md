# synthetic_toy_experiments_v8.md

## 1. 当前状态

**Toy suite 已完成并通过。**

截至当前，Toy-A ~ Toy-G 已全部成功运行，且未发现需要回改 F1 / F2 的证据。

## 2. 各 toy 的最终解释口径

### Toy-Smoke
用于验证：
- 目录闭环
- 结果导出闭环
- solver 基本可运行

### Toy-A
用于验证：
- 对称情形下不会凭空制造不对称
- D_R / D_B 可达近零

### Toy-B
用于验证：
- 非对称情形下不会塌缩回等权
- 权重能对结构变化做出反应

### Toy-C
用于验证：
- 5 资产结构下的稳定求解
- 主模型在 inactive-band 区间可自然退化

### Toy-D
用于验证：
- block-symmetric invariance
- 不能把其解释为“分组分离已被证明”

### Toy-E
用于验证：
- solver 压力场景
- 高 rho 下 inactive-band 仍稳定

### Toy-F
用于验证：
- slack-band 处理正确
- 主模型在 band 未激活时正确退化到 CtR-only

### Toy-G
用于验证：
- eta > 0 的 smoothness 进入目标后，主模型仍稳定收敛
- 平滑项并未破坏 D_R / D_B 解释链

## 3. 总体结论

本 toy 阶段支持以下结论：

1. 统一结果契约可用；
2. 两阶段 solver 可用；
3. 主模型在 toy 场景中没有出现系统性错解；
4. 当前 F1 / F2 不需要解冻；
5. 允许进入真实 ETF minimal run。

## 4. 不支持的结论

toy suite **不支持**：

- 真实数据上的收益优势结论
- 最终参数优劣判断
- 对长期 out-of-sample 表现的断言

## 5. 开放的下一阶段

从本版本起，进入：

> `minimal_real_etf_run.md`

并把 toy 阶段定位为已通过的前置门禁，而不是继续扩展的主战场。

