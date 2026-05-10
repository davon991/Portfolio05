# 第 3 节 CtB、组合相关结构与结构性分散化 — 正式中文版本 v6

## 文件状态

- 建议文件名：`section_03_ctb_correlation_cn_formal_v6_final_candidate.md`
- 层级：F4 rolling draft
- 用途：第 3 节正式中文正文候选稿
- 说明：本文件不是逻辑说明版，而是可直接作为中文论文正文基础的正式版本
- 正文主模型统一称为：CtR–CtB 模型
- 不出现笔记、项目管理、文件治理等内部痕迹

---

# 3. CtB、组合相关结构与结构性分散化

第 2 节已经引入了资产对组合风险的贡献 CtR。CtR 可以将组合总风险分解为各资产的风险贡献，并形成风险预算偏离度量。然而，风险贡献的分布并不能完全描述组合内部结构。即使标准化 CtR 份额已经接近给定风险预算，不同资产与组合整体之间的相关关系仍可能存在明显差异。

因此，本节引入第二个结构性对象，即资产与组合之间的相关性 Correlation to Basket，以下记为 CtB。与 CtR 不同，CtB 不是组合总风险的份额，而是刻画单个资产收益与整个组合收益之间的相关关系。

## 3.1. 组合收益与资产—组合协方差

设 \(r_t=(r_{1t},\ldots,r_{nt})^\top\) 为资产收益率向量，\(x\) 为组合权重向量。组合收益率为
\[
r_{p,t}=x^\top r_t.
\tag{3.1}
\]
资产收益率协方差矩阵记为 \(\Sigma\)。第 \(i\) 个资产收益率与组合收益率之间的协方差为
\[
\operatorname{Cov}(r_i,r_p)
=
\operatorname{Cov}(r_i,x^\top r)
=
\sum_{j=1}^n x_j\Sigma_{ij}.
\]
因此，
\[
\operatorname{Cov}(r_i,r_p)
=
(\Sigma x)_i.
\tag{3.2}
\]
公式 (3.2) 表明，向量 \(\Sigma x\) 具有重要的结构含义：其第 \(i\) 个分量刻画了第 \(i\) 个资产与整个组合之间的协方差关系。

## 3.2. CtB 的定义

设
\[
\sigma_i=\sqrt{\Sigma_{ii}}
\]
为第 \(i\) 个资产收益率的标准差，\(\sigma_p(x)\) 为公式 (2.1) 中定义的组合波动率。假设 \(\sigma_i>0\) 且 \(\sigma_p(x)>0\)。

第 \(i\) 个资产与组合之间的相关性定义为
\[
\operatorname{CtB}_i(x;\Sigma)
=
\operatorname{Corr}(r_i,r_p)
=
\frac{\operatorname{Cov}(r_i,r_p)}{\sigma_i\sigma_p(x)}.
\]
结合公式 (3.2)，得到
\[
\operatorname{CtB}_i(x;\Sigma)
=
\frac{(\Sigma x)_i}{\sigma_i\sigma_p(x)}.
\tag{3.3}
\]
公式 (3.3) 是本文中 CtB 的基本定义。

CtB 表示单个资产收益与整个组合收益之间的相关程度。如果 \(\operatorname{CtB}_i\) 较大，则说明该资产与组合整体之间的联系较强；如果 \(\operatorname{CtB}_i\) 较小，则说明该资产与组合整体之间的联系较弱。

需要强调的是，CtB 与 CtR 不同。CtR 回答的问题是：组合总风险中有多少由某个资产承担？CtB 回答的问题是：某个资产与整个组合之间的相关关系有多强？因此，CtB 不是 CtR 的替代，而是 CtR 的补充。

## 3.3. CtR 与 CtB 的关系

CtR 与 CtB 之间的关系可以由公式 (2.3) 和公式 (3.3) 得到。由公式 (3.3) 可知
\[
(\Sigma x)_i
=
\sigma_i\sigma_p(x)\operatorname{CtB}_i(x;\Sigma).
\]
将该式代入 CtR 定义，可得
\[
\operatorname{CtR}_i(x;\Sigma)
=
x_i\sigma_i\operatorname{CtB}_i(x;\Sigma).
\]
再除以组合波动率 \(\sigma_p(x)\)，得到标准化 CtR 份额与 CtB 之间的关系：
\[
\widetilde{\operatorname{CtR}}_i(x;\Sigma)
=
\frac{x_i\sigma_i}{\sigma_p(x)}
\operatorname{CtB}_i(x;\Sigma).
\tag{3.4}
\]
公式 (3.4) 是理解 CtR 与 CtB 差异的关键。

由公式 (3.4) 可知，CtR 份额不仅取决于 CtB，还取决于资产权重 \(x_i\)、资产自身波动率 \(\sigma_i\) 和组合总波动率 \(\sigma_p(x)\)。因此，CtB 相等并不自动意味着 CtR 相等；反过来，风险贡献相等也不保证资产与组合之间的相关性均衡。

## 3.4. Equal-CtB 作为理论结构目标

如果 CtR 描述的是风险分配，那么 CtB 描述的是资产与组合之间的相关关系。理论上，均衡的 CtB 结构可以写为
\[
\operatorname{CtB}_i(x;\Sigma)=c,
\qquad i=1,\ldots,n.
\tag{3.5}
\]
条件 (3.5) 是自然的理论目标，但它并不意味着在 long-only 约束下总能得到一个简单且可行的闭式组合。由于 \(\operatorname{CtB}_i(x;\Sigma)\) 本身依赖于组合权重、组合波动率以及可行域约束，exact equal-CtB 会导向一个方程系统，而不是一个通用可直接使用的计算公式。

因此，正文中将 exact equal-CtB 视为理论参照。相应系统、归一化以及 long-only 可行性的进一步讨论放在附录 C 中。对于后续模型而言，本文采用的不是强制等式 (3.5)，而是 CtB 离散度量。

## 3.5. CtB 离散度量 \(D_B\)

为了将一组 CtB 数值压缩为一个可比较的指标，首先定义 CtB 的横截面均值：
\[
\overline{\operatorname{CtB}}(x;\Sigma)
=
\frac1n
\sum_{i=1}^n
\operatorname{CtB}_i(x;\Sigma).
\tag{3.6}
\]
在此基础上，定义 CtB 离散度：
\[
D_B(x)
=
\frac12
\sum_{i=1}^n
\left(
\operatorname{CtB}_i(x;\Sigma)
-
\overline{\operatorname{CtB}}(x;\Sigma)
\right)^2.
\tag{3.7}
\]
公式 (3.7) 是各资产 CtB 相对于其均值的二次离散度量。如果 \(D_B(x)=0\)，则所有资产具有相同的 CtB，也就是条件 (3.5) 成立。

\(D_B(x)\) 是 CtB 结构非均衡的计算型度量。它是一个标量，具有直接解释性，也可以进入后续优化模型。

## 3.6. 对后续模型的作用

本节说明了 CtB 如何刻画资产与组合之间的相关关系，并说明了如何用 \(D_B(x)\) 衡量 CtB 结构的非均衡程度。

但是，\(D_B\) 本身并不指定组合总风险应如何分配到各资产。因此，CtB 不能替代 CtR，而应与 CtR 协同使用。下一节将把 \(D_R(x;b)\) 和 \(D_B(x)\) 结合起来，构造 CtR–CtB 主模型。
