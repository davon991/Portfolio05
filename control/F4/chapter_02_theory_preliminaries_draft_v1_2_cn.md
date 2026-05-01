# chapter_02_theory_preliminaries_draft_v1_2_cn.md

# 第2章 理论预备与统一记号

本章给出全文后续分析所需的统一数学对象，包括收益向量、协方差矩阵、组合权重、long-only 可行域以及基本优化记号。CtR、CtB 及其协调模型将在后续章节中分别展开，本章仅保留必要的理论预备。

## 2.1 收益、组合与风险表示

设资产个数为 \(n\)，资产集合记为 \(\mathcal{N}=\{1,\dots,n\}\)。在时点 \(t\)，资产收益向量记为
\[
r_t=(r_{1t},\dots,r_{nt})^\top \in \mathbb{R}^n.
\]
组合权重向量记为
\[
x=(x_1,\dots,x_n)^\top \in \mathbb{R}^n.
\]

在给定权重 \(x\) 时，组合单期收益为
\[
r_{p,t}=x^\top r_t.
\tag{2.1}
\]
若资产期望收益向量记为 \(\mu\)，则组合期望收益为
\[
\mu_p(x)=x^\top \mu.
\tag{2.2}
\]

风险输入建立在协方差矩阵 \(\Sigma\) 之上：
\[
\Sigma=\mathrm{Cov}(r_t).
\]
由此，组合方差与组合波动率分别定义为
\[
v_p(x)=x^\top \Sigma x,
\tag{2.3}
\]
\[
\sigma_p(x)=\sqrt{x^\top \Sigma x}.
\tag{2.4}
\]
对单个资产，定义
\[
\sigma_i=\sqrt{\Sigma_{ii}},\qquad i=1,\dots,n.
\tag{2.5}
\]

## 2.2 long-only 可行域与优化问题

本文讨论的是 long-only 大类资产 ETF 配置，因此主可行域写为
\[
\mathcal{X}
=
\left\{
x\in\mathbb{R}^n:
x_i\ge 0,\ \mathbf{1}^\top x=1
\right\}.
\tag{2.6}
\]
该可行域表示权重非负且全部资本被完全分配。

在这一可行域上，后续模型都可以写成
\[
\min_{x\in\mathcal{X}} F(x),
\tag{2.7}
\]
其中 \(F(x)\) 在不同章节承担不同含义。第 3 章围绕 CtR 展开，第 4 章围绕 CtB 展开，第 5 章在此基础上给出协调模型。

## 2.3 经典组合理论背景与优化预备

现代组合理论通常从 Markowitz 的均值—方差框架出发。该框架确立了收益与风险之间的基本权衡，并提供了统一的收益—协方差语言。Sharpe 的资本市场理论进一步说明，风险与收益的关系可以在更一般的均衡框架中理解。对本文而言，这些理论的主要作用是提供统一背景：后续关于 CtR、CtB 以及协调模型的讨论，仍然建立在收益、协方差与权重的基本表示之上。

本文并不以收益预测为主线。虽然期望收益 \(\mu\) 在理论上被保留，但后文更关注的是在给定风险输入下，如何组织风险分配与相关结构，从而形成一种可解释的 long-only 配置框架。

对任一标量函数 \(f(x)\)，其梯度记为
\[
\nabla f(x),
\tag{2.8}
\]
其 Hessian 记为
\[
\nabla^2 f(x).
\tag{2.9}
\]
梯度描述局部一阶变化方向，Hessian 描述局部二阶曲率结构。二者将在第 6 章统一求解器中分别对应一阶更新与局部二阶加速。

在上述记号基础上，CtR 与 CtB 将分别作为后续章节的核心对象，其中 CtR 对应风险分配，CtB 对应相关结构；\(D_R(x;b)\) 与 \(D_B(x)\) 则作为相应离散度函数的统一记号。由此，全文的模型、图表与结果解释可以建立在同一套数学语言之上。

---

## 参考文献

Ledoit, O., & Wolf, M. (2004). Honey, I Shrunk the Sample Covariance Matrix. *The Journal of Portfolio Management*, 30(4), 110–119.

Markowitz, H. (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.

Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization* (2nd ed.). Springer.

Sharpe, W. F. (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. *The Journal of Finance*, 19(3), 425–442.
