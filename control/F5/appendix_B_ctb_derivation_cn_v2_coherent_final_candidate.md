# 附录 B：CtB 理论推导

本附录补充第 3 章，是 CtR–CtB 模型中 CtB 模块的数学依据。第 3 章已经将 CtB 定义为单个资产与组合之间的相关关系；本附录进一步推导 CtB 如何由资产与组合的协方差得到，CtB 与 CtR 如何联系，以及如何从 CtB 精确相等过渡到计算型非均衡度量 \(D_B\)。因此，附录 B 不重复第 3 章的概念解释，而是展开 CtB 部分背后的数学链条。

本附录沿用正文和附录 A 的符号。设 \(x\in\mathbb R^n\) 为组合权重向量，\(\Sigma\in\mathbb R^{n\times n}\) 为资产收益率协方差矩阵，\(\sigma_p(x)=\sqrt{x^\top\Sigma x}\) 为组合波动率，并设

\[
\sigma_i=\sqrt{\Sigma_{ii}},\qquad i=1,\ldots,n,
\]

为第 \(i\) 个资产的个体波动率。假设 \(\sigma_i>0\) 且 \(\sigma_p(x)>0\)。

## B.1 资产与组合的协方差

设 \(r=(r_1,\ldots,r_n)^\top\) 为资产单期收益率向量。组合收益率为

\[
r_p=x^\top r. \tag{B.1}
\]

第 \(i\) 个资产收益率与组合收益率之间的协方差为

\[
\operatorname{Cov}(r_i,r_p)
=
\operatorname{Cov}(r_i,x^\top r). \tag{B.2}
\]

由于 \(x\) 是固定组合权重向量，有

\[
\operatorname{Cov}(r_i,x^\top r)
=
\sum_{j=1}^n x_j\operatorname{Cov}(r_i,r_j)
=
\sum_{j=1}^n x_j\Sigma_{ij}. \tag{B.3}
\]

因此

\[
\operatorname{Cov}(r_i,r_p)=(\Sigma x)_i. \tag{B.4}
\]

公式 (B.4) 表明，向量 \(\Sigma x\) 的第 \(i\) 个分量具有明确结构含义：它度量第 \(i\) 个资产与整个组合之间的协方差联系。

## B.2 CtB 定义及其与 CtR 的关系

CtB 定义为第 \(i\) 个资产收益率与组合收益率之间的相关系数：

\[
\operatorname{CtB}_i(x;\Sigma)
=
\operatorname{Corr}(r_i,r_p)
=
\frac{\operatorname{Cov}(r_i,r_p)}
{\sigma_i\sigma_p(x)}. \tag{B.5}
\]

结合 (B.4)，得到 CtB 的基本公式：

\[
\operatorname{CtB}_i(x;\Sigma)
=
\frac{(\Sigma x)_i}{\sigma_i\sigma_p(x)}. \tag{B.6}
\]

该量描述的不是总风险份额，而是单个资产与整个组合之间的相关程度。

CtB 与 CtR 的关系可以由附录 A 中的 CtR 定义得到：

\[
\operatorname{CtR}_i(x;\Sigma)
=
x_i\frac{(\Sigma x)_i}{\sigma_p(x)}. \tag{B.7}
\]

由 (B.6) 可得

\[
(\Sigma x)_i
=
\sigma_i\sigma_p(x)\operatorname{CtB}_i(x;\Sigma). \tag{B.8}
\]

将 (B.8) 代入 (B.7)，得到

\[
\operatorname{CtR}_i(x;\Sigma)
=
x_i\sigma_i\operatorname{CtB}_i(x;\Sigma). \tag{B.9}
\]

进一步除以 \(\sigma_p(x)\)，可得

\[
\widetilde{\operatorname{CtR}}_i(x;\Sigma)
=
\frac{x_i\sigma_i}{\sigma_p(x)}
\operatorname{CtB}_i(x;\Sigma). \tag{B.10}
\]

公式 (B.10) 表明，CtR 与 CtB 有联系，但并不相同。CtR 份额不仅取决于 CtB，还取决于资产权重、资产自身波动率和组合总波动率。因此，CtB 相等并不意味着风险贡献相等；风险贡献相等也不意味着 CtB 相等。

## B.3 equal-CtB 条件

理论上的均匀 CtB 结构可以写成

\[
\operatorname{CtB}_i(x;\Sigma)=c,
\qquad i=1,\ldots,n, \tag{B.11}
\]

其中 \(c\) 为共同的 CtB 水平。将 (B.6) 代入 (B.11)，得到

\[
\frac{(\Sigma x)_i}{\sigma_i\sigma_p(x)}
=
c,
\qquad i=1,\ldots,n. \tag{B.12}
\]

因此

\[
(\Sigma x)_i
=
c\,\sigma_i\,\sigma_p(x),
\qquad i=1,\ldots,n. \tag{B.13}
\]

记

\[
\kappa=c\,\sigma_p(x).
\]

则 (B.13) 可写为

\[
(\Sigma x)_i=\kappa\sigma_i,
\qquad i=1,\ldots,n. \tag{B.14}
\]

向量形式为

\[
\Sigma x=\kappa\sigma,
\qquad
\sigma=(\sigma_1,\ldots,\sigma_n)^\top. \tag{B.15}
\]

公式 (B.15) 说明了 equal-CtB 条件的结构：资产与组合之间的协方差向量应与资产个体波动率向量成比例。

## B.4 equal-CtB 条件导出的形式候选方向

如果 \(\Sigma\) 非奇异，则由 (B.15) 形式上可得

\[
x=\kappa\Sigma^{-1}\sigma. \tag{B.16}
\]

组合权重还需要满足归一化条件

\[
\mathbf 1^\top x=1. \tag{B.17}
\]

因此可以得到形式归一化方向：

\[
x^{\mathrm{eqB}}
=
\frac{\Sigma^{-1}\sigma}
{\mathbf 1^\top\Sigma^{-1}\sigma}, \tag{B.18}
\]

前提是分母不为零。

公式 (B.18) 不是通用的实际投资组合解。它只说明在不考虑全部可行约束时，CtB 精确相等条件会导出怎样的形式方向。

## B.5 无卖空约束与可行性

本文研究的是无卖空组合，因此可行集合为

\[
\mathcal X=
\left\{
x\in\mathbb R^n:
\mathbf 1^\top x=1,\;
x_i\ge0,\; i=1,\ldots,n
\right\}. \tag{B.19}
\]

为了使形式方向 (B.18) 成为可行组合，需要满足

\[
x_i^{\mathrm{eqB}}\ge0,\qquad i=1,\ldots,n. \tag{B.20}
\]

(B.18) 中的归一化可以保证 \(\mathbf 1^\top x^{\mathrm{eqB}}=1\)，但不能保证所有分量非负。如果 \(\Sigma^{-1}\sigma\) 中存在负分量，则 \(x^{\mathrm{eqB}}\) 不属于可行集合 \(\mathcal X\)。

因此，CtB 精确相等更适合作为理论结构目标，而不是无卖空组合中的通用闭式解。

## B.6 从 CtB 精确相等到 \(D_B\) 度量

主模型需要一个适用于任意可行组合 \(x\in\mathcal X\) 的标量 CtB 非均衡度量。首先定义 CtB 的平均值：

\[
\overline{\operatorname{CtB}}(x;\Sigma)
=
\frac1n
\sum_{i=1}^n
\operatorname{CtB}_i(x;\Sigma). \tag{B.21}
\]

然后定义 CtB 非均衡度量：

\[
D_B(x;\Sigma)
=
\frac12
\sum_{i=1}^n
\left(
\operatorname{CtB}_i(x;\Sigma)
-
\overline{\operatorname{CtB}}(x;\Sigma)
\right)^2. \tag{B.22}
\]

如果 \(D_B(x;\Sigma)=0\)，则所有 \(\operatorname{CtB}_i(x;\Sigma)\) 相等，即满足 equal-CtB 条件。如果 \(D_B(x;\Sigma)\) 较大，则说明不同资产与组合之间的相关联系不均衡。

因此，\(D_B\) 是均匀 CtB 结构思想的计算型表达。与 CtB 精确相等不同，\(D_B\) 不要求精确相等一定能在可行集合内实现。因此，在 CtR–CtB 主模型中，\(D_R(x;b,\Sigma)\) 描述组合偏离风险预算结构的程度，\(D_B(x;\Sigma)\) 描述组合相关结构的非均衡程度。CtR 保持风险预算主目标的地位，CtB 则作为额外的结构控制对象进入模型。

公式 (B.1)–(B.22) 给出了从资产与组合协方差到 \(D_B(x;\Sigma)\) 的完整推导。该链条构成 CtR–CtB 模型中 CtB 部分的数学基础。
