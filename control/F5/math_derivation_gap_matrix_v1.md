# math_derivation_gap_matrix_v1.md

## 0. 文件目的与状态

**状态**：F4 rolling / math-strengthening controller v1.  
**作用**：本文件用于判断最终论文哪些章节必须补充数学推导，哪些章节只需保留公式定义，哪些章节不应为了“显得数学多”而堆砌推导。

本文件服从：
- F1：项目主线、统一记号、定义台账、论文骨架；
- F2：模型、数据、baseline、solver、result、statistical validation 契约；
- F3：clean-lineage 结果、写作契约、答辩口径、图表工厂；
- F4：当前正文草稿与 reader-facing 结构。

本文件不改变 CtR–CtB 主模型，不改变实证结果，不改变 baseline 集合。

---

## 1. 总体判断

当前论文已经有完整结构，但数学推导还偏“定义型”。最终版应升级为“定义 + 必要推导 + 解释 + 与后续模型连接”的形式。

必须补强的章节：
1. 经典模型章节：Markowitz / Tobin / Sharpe；
2. CtR 章节；
3. CtB 章节；
4. CtR–CtB 模型章节；
5. 求解器章节。

不宜补太多推导的章节：
1. 数据与校准章节；
2. 结果章节；
3. 结论；
4. 附录中的复现说明。

---

## 2. 章节级补强矩阵

| 章节 | 当前问题 | 必须补的数学内容 | 补强强度 | 是否进正文 |
|---|---|---|---|---|
| Постановка задачи | 还需要更像正式数学问题陈述 | 给出输入、可行域、目标、输出、计算任务 | 高 | 必须 |
| 1. Markowitz/Tobin/Sharpe | 需满足导师要求并连接旧课程论文 | Markowitz 拉格朗日推导；Tobin 组合公式；Sharpe 协方差结构 | 高 | 必须 |
| 2. CtR | 已有定义，但 Euler 分解推导略短 | MRC 推导、Euler 加总、标准化 CtR share 推导、风险预算条件 | 高 | 必须 |
| 3. CtB | 已有定义和关系式，但解释可加强 | CtB 从相关系数推出；CtR–CtB 关系式；不等价解释 | 高 | 必须 |
| 4. CtR–CtB 模型 | 公式已有，但建模边界需更严谨 | 硬约束与软约束关系；退化到 CtR-only；参数分层 | 中高 | 必须 |
| 5. Solver | 已有 PG/Newton，但 KKT 和 simplex 约束解释不足 | 投影梯度；free-set Newton；KKT residual；fallback 的数学含义 | 中高 | 必须，但不贴代码 |
| 6. 数据/校准 | 表格已有 | 只补校准目标的数学决策规则，不做复杂推导 | 中 | 正文简洁 |
| 7. 结果 | 结果已有 | 只解释 D_R / D_B / turnover / inference 的关系 | 低中 | 正文简洁 |
| Заключение | 不需要推导 | 逐条总结完成内容 | 低 | 必须 |
| Appendix | listing 和补充表 | 长推导可放附录，但主定义不能只放附录 | 中 | 附录 |

---

## 3. 必须补入正文的核心推导

### 3.1 Markowitz 拉格朗日推导

目的：满足导师要求“加入课程论文 Markowitz/Tobin/Sharpe”，同时使经典模型成为 CtR–CtB 的理论入口。

应写入：
\[
\min_x x^\top \Sigma x,\quad \mathbf 1^\top x=1,\quad \mu^\top x=\mu_0.
\]

构造：
\[
L(x,\lambda,\nu)=x^\top\Sigma x-\lambda(\mathbf 1^\top x-1)-\nu(\mu^\top x-\mu_0).
\]

一阶条件：
\[
2\Sigma x-\lambda\mathbf 1-\nu\mu=0.
\]

因此：
\[
x=\frac12\Sigma^{-1}(\lambda\mathbf 1+\nu\mu).
\]

随后代入两个约束，得到关于 \(\lambda,\nu\) 的二元线性系统。

正文解释重点：Markowitz 建立了收益—协方差—权重的统一语言；本文后续 CtR/CtB 仍依赖同一协方差输入，但研究重点从收益—方差权衡转向风险贡献与相关结构。

---

### 3.2 Tobin 无风险资产组合公式

应写入：
若无风险资产收益为 \(r_f\)，风险组合为 \(x\)，投资比例为 \(\alpha\)，则组合收益和风险为：
\[
\mu_P=\alpha r_f+(1-\alpha)\mu_x,
\]
\[
\sigma_P=(1-\alpha)\sigma_x.
\]

解释重点：Tobin 模型说明资本可以在无风险资产和风险资产组合之间分配，但本文主要研究给定风险资产池内部的 long-only 风险结构，因此 Tobin 作为背景而不是主模型。

---

### 3.3 Sharpe 单指数模型协方差推导

应写入：
\[
r_i=\alpha_i+\beta_i I+\varepsilon_i,
\quad \mathbb E\varepsilon_i=0,
\quad \mathrm{Cov}(I,\varepsilon_i)=0.
\]

若 \(i\ne j\)，则：
\[
\mathrm{Cov}(r_i,r_j)=\beta_i\beta_j\sigma_I^2.
\]

若 \(i=j\)，则：
\[
\mathrm{Var}(r_i)=\beta_i^2\sigma_I^2+\sigma^2_{\varepsilon_i}.
\]

矩阵形式：
\[
\Sigma=\sigma_I^2\beta\beta^\top+D,
\]
其中 \(D=\mathrm{diag}(\sigma^2_{\varepsilon_1},\ldots,\sigma^2_{\varepsilon_n})\)。

解释重点：Sharpe 模型降低协方差估计复杂度，但本文不继续沿用旧课程论文的 Sharpe-k 数值实验，因为当前主模型不是 Sharpe 单指数组合选择，而是 CtR–CtB 结构优化。

---

### 3.4 CtR 的 MRC 与 Euler 分解

必须补入正文。

从：
\[
\sigma_p(x)=\sqrt{x^\top\Sigma x}
\]

推出：
\[
\frac{\partial \sigma_p(x)}{\partial x_i}
=
\frac{(\Sigma x)_i}{\sigma_p(x)}.
\]

于是：
\[
\mathrm{MRC}_i(x;\Sigma)=\frac{(\Sigma x)_i}{\sigma_p(x)}.
\]

定义：
\[
\mathrm{CtR}_i(x;\Sigma)=x_i\mathrm{MRC}_i(x;\Sigma)
=\frac{x_i(\Sigma x)_i}{\sigma_p(x)}.
\]

加总：
\[
\sum_i \mathrm{CtR}_i(x;\Sigma)
=\frac{\sum_i x_i(\Sigma x)_i}{\sigma_p(x)}
=\frac{x^\top\Sigma x}{\sigma_p(x)}
=\sigma_p(x).
\]

---

### 3.5 CtR share 与 D_R

必须补入正文。

\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)
=\frac{\mathrm{CtR}_i(x;\Sigma)}{\sigma_p(x)}
=\frac{x_i(\Sigma x)_i}{x^\top\Sigma x}.
\]

预算向量：
\[
b_i>0,\quad \sum_i b_i=1.
\]

风险预算目标：
\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)=b_i.
\]

偏离函数：
\[
D_R(x;b)=\frac12\sum_i(\widetilde{\mathrm{CtR}}_i(x;\Sigma)-b_i)^2.
\]

---

### 3.6 CtB 从相关系数推出

必须补入正文。

\[
\mathrm{CtB}_i(x;\Sigma)=\mathrm{Corr}(r_i,r_p).
\]

由于 \(r_p=x^\top r\)，有：
\[
\mathrm{Cov}(r_i,r_p)=\mathrm{Cov}(r_i,x^\top r)=(\Sigma x)_i.
\]

因此：
\[
\mathrm{CtB}_i(x;\Sigma)=\frac{(\Sigma x)_i}{\sigma_i\sigma_p(x)}.
\]

---

### 3.7 CtR 与 CtB 的桥接关系

必须补入正文。

从：
\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)=\frac{x_i(\Sigma x)_i}{x^\top\Sigma x}
\]

以及：
\[
\mathrm{CtB}_i(x;\Sigma)=\frac{(\Sigma x)_i}{\sigma_i\sigma_p(x)}
\]

可得：
\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)
=\frac{x_i\sigma_i}{\sigma_p(x)}\mathrm{CtB}_i(x;\Sigma).
\]

解释重点：CtR 和 CtB 有同一协方差来源，但不等价。CtR 是风险份额；CtB 是相关结构。

---

### 3.8 D_B 与 CtB-only

必须补入正文。

\[
\overline{\mathrm{CtB}}(x;\Sigma)=\frac1n\sum_i\mathrm{CtB}_i(x;\Sigma).
\]

\[
D_B(x)=\frac12\sum_i(\mathrm{CtB}_i(x;\Sigma)-\overline{\mathrm{CtB}}(x;\Sigma))^2.
\]

CtB-only：
\[
\min_{x\in\mathcal X}D_B(x).
\]

解释重点：CtB-only 不是推荐策略，而是结构边界基准。

---

### 3.9 CtR–CtB 模型与软约束

必须补入正文。

正式模型：
\[
\min_{x\in\mathcal X}
D_R(x;b)+\eta\|x-x_{t-1}\|_2^2+\gamma\|x\|_2^2,
\quad D_B(x)\le\delta.
\]

实现形式：
\[
J_\rho(x)=D_R(x;b)+\eta\|x-x_{t-1}\|_2^2+\gamma\|x\|_2^2+\frac\rho2[D_B(x)-\delta]_+^2.
\]

解释重点：\(\delta\) 是结构容忍带；\(\rho\) 是数值罚参数，不是经济偏好。

---

### 3.10 求解器数学补强

应写入正文，但不宜过长。

Projected gradient：
\[
y^{(k)}=x^{(k)}-\alpha_k\nabla F(x^{(k)}),
\]
\[
x^{(k+1)}=\Pi_{\mathcal X}(y^{(k)}).
\]

Newton：
\[
H_kp_k=-g_k,
\]
\[
x^{(k+1)}=\Pi_{\mathcal X}(x^{(k)}+\tau_kp_k).
\]

必须解释：先 PG 是为了保持可行性，后 Newton 是为了局部加速；fallback 是数值保护，不是失败伪装。

---

## 4. 不建议加入正文的推导

### 4.1 不建议加入旧 Sharpe 最优 k 推导

理由：
- 它属于旧课程论文的单指数模型专项算法；
- 当前 thesis 主模型不是 Sharpe-k；
- 会打断 CtR–CtB 主线；
- 会和当前 baseline ladder 冲突。

### 4.2 不建议加入过长的 Hessian 展开

理由：
- 当前实现使用 numerical gradient / numerical Hessian；
- 主文只需说明二阶段算法逻辑；
- 精细 Hessian 公式可以省略或放附录。

### 4.3 不建议在结果章推导 bootstrap 理论

理由：
- 统计推断方法只需说明 moving-block bootstrap 的用途；
- 不应把第 8 章变成统计方法论文。

---

## 5. 正文阅读连贯性规则

每个公式必须满足：
1. 公式前说明为什么需要它；
2. 公式后说明它衡量什么；
3. 后文至少调用一次；
4. 若公式不再使用，则不要编号；
5. 不使用内部项目名，例如 F1/F2、clean-lineage、run_id、Main、d08、d04。

---

## 6. 本轮冻结影响

- F1：不变。
- F2：不变。
- F3：不变。
- F4：升级为 math-strengthening rolling。
- 新增本文件作为数学推导补强控制文件。

