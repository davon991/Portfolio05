# chapter_03_ctr_foundation_draft_v1_2_cn.md

# 第3章 CtR基础：定义、性质与目标化风险配置

## 3.1 风险度量与 CtR 的基本定义

在统一记号下，设资产收益向量为 \(r_t=(r_{1t},\dots,r_{nt})^\top\)，组合权重为 \(x=(x_1,\dots,x_n)^\top\)，协方差矩阵为 \(\Sigma=\mathrm{Cov}(r_t)\)。本文主模型定义在 long-only simplex 上，即

\[
\mathcal{X}
=
\left\{
x\in\mathbb{R}^n:
x_i\ge 0,\ \mathbf{1}^\top x=1
\right\}.
\tag{3.1}
\]

组合方差与组合波动率分别记为

\[
\sigma_p^2(x)=x^\top \Sigma x,\qquad
\sigma_p(x)=\sqrt{x^\top \Sigma x}.
\tag{3.2}
\]

式（3.2）构成后续风险分解的共同基础。仅从资本权重出发，并不能直接判断各资产究竟承担了多少组合风险；更有解释力的对象，是组合波动率对各资产权重的边际响应。为此，定义第 \(i\) 个资产的边际风险贡献为

\[
\mathrm{MRC}_i(x;\Sigma)
=
\frac{(\Sigma x)_i}{\sigma_p(x)}.
\tag{3.3}
\]

据此，第 \(i\) 个资产对组合总波动率的贡献可写为

\[
\mathrm{CtR}_i(x;\Sigma)
=
x_i\,\mathrm{MRC}_i(x;\Sigma)
=
\frac{x_i(\Sigma x)_i}{\sigma_p(x)}.
\tag{3.4}
\]

在 \(\sigma_p(x)\) 可微且一阶正齐次的条件下，Euler 型分解给出

\[
\sum_{i=1}^n \mathrm{CtR}_i(x;\Sigma)=\sigma_p(x).
\tag{3.5}
\]

因此，CtR 不是附加的诊断指标，而是组合总风险在资产维度上的可加分解。围绕风险贡献的金融解释与风险预算语义，Qian（2006）给出了较为清晰的说明；在 ERC 与风险平价研究中，这一分解也是最核心的理论基础之一。

若直接以 \(\mathrm{CtR}_i(x;\Sigma)\) 与预算目标比较，则仍存在尺度不一致的问题：\(\mathrm{CtR}_i\) 的总和是 \(\sigma_p(x)\)，而预算向量通常被规范为和为 1 的份额向量。为使风险贡献能够与预算向量逐项比较，本文采用标准化风险贡献份额：

\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)
=
\frac{\mathrm{CtR}_i(x;\Sigma)}{\sigma_p(x)}
=
\frac{x_i(\Sigma x)_i}{x^\top \Sigma x}.
\tag{3.6}
\]

由式（3.5）可得

\[
\sum_{i=1}^n \widetilde{\mathrm{CtR}}_i(x;\Sigma)=1.
\tag{3.7}
\]

式（3.6）—（3.7）将 CtR 从波动率单位下的贡献量转化为可与预算向量直接比较的风险份额。这一步为后续建模提供了统一基准，因为本文关注的并不是某个绝对风险水平，而是风险份额结构与目标预算之间的一致性。

## 3.2 风险预算向量与等风险贡献基准

在 CtR 语言下，风险预算问题可以表述为：给定预算向量

\[
b=(b_1,\dots,b_n)^\top,\qquad
b_i>0,\quad \sum_{i=1}^n b_i=1,
\tag{3.8}
\]

希望组合的标准化风险贡献份额尽可能贴近该预算，即

\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)=b_i,\qquad i=1,\dots,n.
\tag{3.9}
\]

式（3.9）表明，每个资产在组合总风险中的占比应与预先给定的预算权重一致。由此可见，风险预算方法与传统资本配置方法的差别在于：前者直接规定风险如何分配，而不是先配置资金，再被动接受由此形成的风险结果。

本文默认采用等预算形式

\[
b_i=\frac{1}{n},\qquad i=1,\dots,n.
\tag{3.10}
\]

此时，目标条件退化为各资产风险份额相等，即通常所说的等风险贡献（Equal Risk Contribution, ERC）基准。Maillard、Roncalli 与 Teiletche（2010）对 ERC 组合的性质进行了系统分析，并说明了其与等权组合、最小方差组合之间既相关又不等价的关系。对本文而言，ERC 不是最终主模型，而是最重要的 CtR 参考基准：它代表了仅围绕风险预算展开配置的标准方向，因此在后续章节中以 `CtR-only` 的形式进入基准梯队。

若只关注 CtR 预算匹配，则相应的理论基准问题可以写为

\[
x^{\mathrm{CtR}}
\in
\arg\min_{x\in\mathcal{X}} D_R(x;b),
\tag{3.11}
\]

其中 \(D_R(x;b)\) 用于衡量实际 CtR 份额相对于预算 \(b\) 的偏离程度。式（3.11）给出了 CtR-only 基准的最简理论写法。需要说明的是，本文经验部分实际使用的 CtR-only 形式还会加入平滑项与轻度正则项，以维持滚动调仓下的数值稳定与交易可执行性；但其主导对象始终是 CtR 偏离，而不是收益预测或其他额外成分。

## 3.3 CtR偏离函数及其模型意义

为了将风险预算问题转化为可计算、可比较的标量对象，本文将 CtR 偏离函数定义为

\[
D_R(x;b)
:=
\frac{1}{2}
\sum_{i=1}^n
\left(
\widetilde{\mathrm{CtR}}_i(x;\Sigma)-b_i
\right)^2.
\tag{3.12}
\]

由定义可知，\(D_R(x;b)\ge 0\)，且仅当所有标准化风险贡献份额都与预算向量逐项一致时，才有 \(D_R(x;b)=0\)。因此，\(D_R\) 可以被解释为风险预算错配程度的标量摘要。它既保留了 CtR 的配置含义，又将多资产的风险份额比较压缩为后续模型可以直接调用的统一对象。

本文采用式（3.12）而不是其他替代写法，主要基于以下考虑。第一，这一定义与预算向量 \(b\) 直接对齐，解释上较为透明。第二，\(D_R\) 的零点含义明确，即风险预算完全匹配。第三，\(D_R\) 在本文中同时承担理论对象与模型对象的角色：在理论层，它是 CtR 预算误差的正式定义；在模型层，它将成为后续主模型的主目标。也正因为如此，CtR-only 基准不仅是一个理论参照，也为后续主模型提供了没有结构控制时的比较边界。

至此，本章已经完成 CtR 定义、预算表达和偏离函数构造三项核心工作。下一章将在此基础上引入 CtB，以刻画仅由 CtR 预算一致性尚不能覆盖的相关结构问题。

---

## 参考文献

Maillard, S., Roncalli, T., & Teiletche, J. (2010). On the Properties of Equally Weighted Risk Contribution Portfolios. *The Journal of Portfolio Management*, 36(4), 60–70.

Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.

Qian, E. (2006). *On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up*. Research note / working paper.

Roncalli, T. (2013). *Introduction to Risk Parity and Budgeting*. Chapman & Hall/CRC.
