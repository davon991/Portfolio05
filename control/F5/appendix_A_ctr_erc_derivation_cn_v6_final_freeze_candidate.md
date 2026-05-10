# 附录 A：CtR/ERC 理论推导

本附录补充第 2 章，是 CtR–CtB 模型中风险预算模块的数学依据。正文中已经把 CtR 和归一化 CtR 份额作为主要计算量使用；本附录说明这些量如何从组合方差、组合波动率梯度和风险预算条件中自然得到。因此，附录 A 不是一套独立理论体系，而是对第 2 章和主模型中 \(D_R\) 相关公式的完整数学推导。

本附录沿用正文符号。设 \(x\in\mathbb R^n\) 为组合权重向量，\(\Sigma\in\mathbb R^{n\times n}\) 为资产收益率协方差矩阵，\(\mathbf 1\) 为全 1 向量。在 long-only 设定中，

\[
\mathbf 1^\top x=1,\qquad x_i\ge 0,\quad i=1,\ldots,n.
\]

本附录首先在严格正权重 \(x_i>0\) 的情形下推导，因为 ERC 构造使用对数势函数。该推导与正文中的 long-only simplex 约束相一致。

## A.1 符号与组合方差

设 \(\xi=(\xi_1,\ldots,\xi_n)^\top\) 为资产单期收益率向量。协方差矩阵定义为

\[
\Sigma=(\sigma_{ij})_{i,j=1}^n,\qquad 
\sigma_{ij}=\operatorname{cov}(\xi_i,\xi_j).
\]

假设 \(\Sigma\) 对称正定。组合收益率为

\[
r_p(x)=x^\top \xi.
\]

因此组合方差为

\[
\sigma_p^2(x)=\operatorname{var}(r_p(x))=x^\top \Sigma x. \tag{A.1}
\]

组合波动率为

\[
\sigma_p(x)=\sqrt{x^\top \Sigma x}. \tag{A.2}
\]

后文正是对 \(\sigma_p(x)\) 进行资产层面的风险分解。这个分解构成 CtR 风险预算模块的数学基础。

## A.2 组合波动率的梯度

由于 \(\Sigma\) 是对称矩阵，二次型的梯度为

\[
\nabla_x(x^\top \Sigma x)=2\Sigma x. \tag{A.3}
\]

由 (A.2) 可得

\[
\nabla_x \sigma_p(x)
=
\nabla_x (x^\top \Sigma x)^{1/2}
=
\frac{\Sigma x}{\sqrt{x^\top \Sigma x}}
=
\frac{\Sigma x}{\sigma_p(x)}. \tag{A.4}
\]

因此，组合波动率对第 \(i\) 个资产权重的偏导数为

\[
\frac{\partial \sigma_p(x)}{\partial x_i}
=
\frac{(\Sigma x)_i}{\sigma_p(x)}. \tag{A.5}
\]

这个偏导数表示当第 \(i\) 个资产权重发生微小变化时，组合总风险的边际变化。

## A.3 边际风险贡献与 CtR

定义第 \(i\) 个资产的边际风险贡献为

\[
\operatorname{MRC}_i(x;\Sigma)
=
\frac{\partial \sigma_p(x)}{\partial x_i}
=
\frac{(\Sigma x)_i}{\sigma_p(x)}. \tag{A.6}
\]

第 \(i\) 个资产的总风险贡献，即 Contribution to Risk，定义为资产权重与边际风险贡献的乘积：

\[
\operatorname{CtR}_i(x;\Sigma)
=
x_i\,\operatorname{MRC}_i(x;\Sigma)
=
x_i\frac{(\Sigma x)_i}{\sigma_p(x)}. \tag{A.7}
\]

向量形式为

\[
\operatorname{CtR}(x;\Sigma)
=
x\odot \frac{\Sigma x}{\sigma_p(x)}, \tag{A.8}
\]

其中 \(\odot\) 表示逐元素乘法。

所有资产的 CtR 之和等于组合总波动率：

\[
\sum_{i=1}^n \operatorname{CtR}_i(x;\Sigma)
=
\sum_{i=1}^n x_i\frac{(\Sigma x)_i}{\sigma_p(x)}
=
\frac{x^\top \Sigma x}{\sigma_p(x)}
=
\sigma_p(x). \tag{A.9}
\]

该等式也可以理解为 Euler 齐次函数定理在一阶齐次函数 \(\sigma_p(x)\) 上的应用。因此，CtR 给出了组合总风险在资产层面的加性分解。

## A.4 归一化 CtR 份额与风险预算

风险预算关注的不是绝对风险贡献，而是资产在组合总风险中的份额。定义归一化 CtR 份额为

\[
\widetilde{\operatorname{CtR}}_i(x;\Sigma)
=
\frac{\operatorname{CtR}_i(x;\Sigma)}{\sigma_p(x)}
=
\frac{x_i(\Sigma x)_i}{x^\top \Sigma x}. \tag{A.10}
\]

由 (A.9) 可知

\[
\sum_{i=1}^n \widetilde{\operatorname{CtR}}_i(x;\Sigma)=1. \tag{A.11}
\]

设风险预算向量为

\[
b=(b_1,\ldots,b_n)^\top,\qquad b_i>0,\qquad \sum_{i=1}^n b_i=1.
\]

理论风险预算条件为

\[
\widetilde{\operatorname{CtR}}_i(x;\Sigma)=b_i,\qquad i=1,\ldots,n. \tag{A.12}
\]

结合 (A.10)，该条件等价于

\[
x_i(\Sigma x)_i=b_i\,x^\top \Sigma x,\qquad i=1,\ldots,n. \tag{A.13}
\]

这些条件说明：风险预算约束的对象不是资本权重本身，而是组合总风险在各资产之间的分配份额。

## A.5 ERC 作为等风险预算

Equal Risk Contribution 是风险预算的一个特殊情形。此时所有目标风险份额相等：

\[
b_i=\frac1n,\qquad i=1,\ldots,n. \tag{A.14}
\]

因此 (A.13) 变为

\[
x_i(\Sigma x)_i=\frac1n\,x^\top \Sigma x,
\qquad i=1,\ldots,n. \tag{A.15}
\]

等价地，所有资产的总风险贡献相等：

\[
\operatorname{CtR}_1(x;\Sigma)=
\operatorname{CtR}_2(x;\Sigma)=
\cdots=
\operatorname{CtR}_n(x;\Sigma). \tag{A.16}
\]

这就是 Equal Risk Contribution 名称的来源。

## A.6 构造 ERC 组合的对数优化问题

为了构造风险预算组合，可以先求一个正比例向量 \(y\)，再将其归一化为组合权重。向量 \(y\) 不要求满足 \(\mathbf 1^\top y=1\)，它只表示相对比例。

考虑优化问题

\[
\min_{y_i>0}
\left\{
\Phi_b(y)
=
\frac12 y^\top \Sigma y-\sum_{i=1}^n b_i\ln y_i
\right\}. \tag{A.17}
\]

其中，对数项防止 \(y_i\) 退化为零，同时体现目标风险预算比例。因此，这一形式适合先构造正比例向量，再将其归一化为组合权重。

(A.17) 的一阶条件为

\[
\frac{\partial \Phi_b(y)}{\partial y_i}
=
(\Sigma y)_i-\frac{b_i}{y_i}=0,
\qquad i=1,\ldots,n.
\]

因此

\[
y_i(\Sigma y)_i=b_i,\qquad i=1,\ldots,n. \tag{A.18}
\]

对 (A.18) 关于所有 \(i\) 求和，可得

\[
y^\top \Sigma y=\sum_{i=1}^n b_i=1. \tag{A.19}
\]

随后将 \(y\) 归一化为组合权重：

\[
x=\frac{y}{\mathbf 1^\top y}. \tag{A.20}
\]

这个归一化步骤成立的原因是：归一化 CtR 份额对正比例缩放不变。若 \(x=cy\)，且 \(c>0\)，则

\[
\frac{x_i(\Sigma x)_i}{x^\top \Sigma x}
=
\frac{cy_i(c\Sigma y)_i}{c^2y^\top \Sigma y}
=
\frac{y_i(\Sigma y)_i}{y^\top \Sigma y}. \tag{A.21}
\]

利用 (A.18)、(A.19) 和 (A.21)，得到

\[
\widetilde{\operatorname{CtR}}_i(x;\Sigma)=b_i,\qquad i=1,\ldots,n. \tag{A.22}
\]

因此，先求解 (A.17)，再进行归一化，可以得到满足风险预算条件的组合。

在 ERC 情形下，\(b_i=1/n\)，于是 (A.17) 写为

\[
\min_{y_i>0}
\left\{
\Phi_{\mathrm{ERC}}(y)
=
\frac12 y^\top \Sigma y-\frac1n\sum_{i=1}^n \ln y_i
\right\}. \tag{A.23}
\]

其驻点条件为

\[
y_i(\Sigma y)_i=\frac1n,\qquad i=1,\ldots,n. \tag{A.24}
\]

对解 \(y\) 进行归一化 \(x=y/(\mathbf 1^\top y)\)，即可得到 ERC 组合。

## A.7 从 ERC 条件到 \(D_R\) 偏离度量

在 CtR–CtB 主模型中，本文并不把风险预算份额完全相等作为唯一硬约束，而是用一个偏离度量来衡量组合与目标风险预算之间的距离：

\[
D_R(x;b,\Sigma)
=
\sum_{i=1}^n
\left(
\widetilde{\operatorname{CtR}}_i(x;\Sigma)-b_i
\right)^2. \tag{A.25}
\]

在 ERC 情形下，\(b_i=1/n\)，因此 \(D_R(x;b,\Sigma)\) 衡量实际风险份额相对于等风险份额的偏离程度。

这一过渡对主模型非常重要。在理论 ERC 设定中，要求所有风险贡献完全相等；而在 CtR–CtB 计算模型中，CtR 结构通过 \(D_R\) 作为主目标进入模型，CtB 部分则作为额外的结构控制条件进入模型。

公式 (A.1)–(A.25) 给出了从组合方差到 \(D_R(x;b,\Sigma)\) 的完整推导。因此，本附录为 CtR–CtB 模型中的 CtR 风险预算部分提供数学基础。CtB 部分与组合相关结构有关，将在后续附录中单独推导。
