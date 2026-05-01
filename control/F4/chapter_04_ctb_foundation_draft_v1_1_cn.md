# chapter_04_ctb_foundation_draft_v1_1_cn.md

# 第4章 CtB基础：相关结构、离散度与结构控制对象

## 4.1 CtB 的定义及其结构含义

第 3 章已经给出了 CtR 与风险预算的统一表达。若仅从 CtR 出发，组合可以在风险份额意义上接近目标预算，但这并不意味着资产与组合之间的相关暴露也同时得到控制。为刻画这种结构层面的差异，本文引入 Correlation to Basket（CtB）作为第二个基础对象。

设第 \(i\) 个资产的波动率为

\[
\sigma_i=\sqrt{\Sigma_{ii}},
\tag{4.1}
\]

组合收益为 \(r_p=x^\top r_t\)，组合波动率为 \(\sigma_p(x)=\sqrt{x^\top \Sigma x}\)。则第 \(i\) 个资产相对于组合的 CtB 定义为其与组合收益的相关系数：

\[
\mathrm{CtB}_i(x;\Sigma)
=
\mathrm{Corr}(r_i,r_p).
\tag{4.2}
\]

由协方差与相关系数的定义，可将式（4.2）写成可直接计算的形式：

\[
\mathrm{CtB}_i(x;\Sigma)
=
\frac{\mathrm{Cov}(r_i,r_p)}{\sigma_i\,\sigma_p(x)}
=
\frac{(\Sigma x)_i}{\sigma_i\,\sigma_p(x)}.
\tag{4.3}
\]

式（4.3）表明，CtB 描述的是单个资产与整个组合之间的相关暴露强度。与 CtR 相比，CtB 不再直接回答“某资产承担了多少风险份额”，而是回答“某资产在多大程度上与组合整体同向波动”。因此，CtB 更接近组合的相关结构对象，而不是风险预算对象。

这一视角与相关结构和分散化文献的基本脉络是一致的。Choueifaty 与 Coignard（2008）强调分散化与相关结构本身的配置意义；Menchero 与 Davis（2011）的 \(x\)-\(\sigma\)-\(\rho\) 分解则表明，风险贡献可以拆解为资本权重、单资产波动与相关结构三部分的共同作用。对本文而言，这些文献的作用不在于直接给出本文模型，而在于说明：除了 CtR 之外，组合中还存在一个需要单独刻画的相关结构维度。

从 long-only 组合的解释角度看，CtB 还有一个直接优点：它是无量纲的相关系数，因此在不同资产之间具有天然可比性。若少数资产的 CtB 长期显著高于其他资产，则说明组合的相关暴露更集中；反之，若 CtB 在资产间分布较为均衡，则说明组合的相关结构更分散。也正因为此，CtB 在本文中被视为结构质量的直接刻画对象。

## 4.2 CtB 离散度 \(D_B(x)\) 及 CtB-only 基准

为了将 CtB 从逐资产的截面量压缩为可建模、可比较的标量对象，本文先定义 CtB 的截面均值：

\[
\overline{\mathrm{CtB}}(x;\Sigma)
=
\frac{1}{n}\sum_{i=1}^n \mathrm{CtB}_i(x;\Sigma).
\tag{4.4}
\]

在此基础上，将 CtB 离散度定义为

\[
D_B(x)
:=
\frac{1}{2}
\sum_{i=1}^n
\left(
\mathrm{CtB}_i(x;\Sigma)-\overline{\mathrm{CtB}}(x;\Sigma)
\right)^2.
\tag{4.5}
\]

由定义可知，\(D_B(x)\ge 0\)，且当所有资产的 CtB 完全相等时，\(D_B(x)=0\)。因此，\(D_B\) 可以被解释为资产—组合相关暴露在截面上的不均衡程度。若 \(D_B\) 较大，则说明组合的相关结构被少数资产主导；若 \(D_B\) 较小，则说明资产与组合之间的相关暴露更为均衡。

需要强调的是，\(D_B\) 的作用并不是取代 CtR，而是将“相关结构是否过于集中”这一问题转化为一个清晰的标量对象。第 3 章中的 \(D_R(x;b)\) 衡量的是风险预算偏离，第 4 章中的 \(D_B(x)\) 衡量的是相关暴露离散。两者对应的并不是同一个维度，因此在后续模型中也不应被简单视为可互换的目标函数。

为了给后续比较提供结构边界，本文同样定义一个理论上的 CtB-only 基准问题：

\[
x^{\mathrm{CtB}}
\in
\arg\min_{x\in\mathcal{X}} D_B(x).
\tag{4.6}
\]

式（4.6）表示：若只追求 CtB 的截面均衡，则可在 long-only 可行域内最小化相关暴露离散度。该问题并不要求组合在 CtR 份额上与预算一致，因此它与第 3 章中的 CtR-only 基准在对象层面是不同的。对本文而言，CtB-only 的意义主要在于提供一条“纯结构均衡”边界，从而使后续主模型的角色更加清楚：本文并不是在 CtR-only 与 CtB-only 之间简单择一，而是在 CtR 主配置的前提下引入对 CtB 的制度化控制。

## 4.3 CtR 与 CtB 的联系及 CtB 的角色定位

尽管 CtR 与 CtB 属于不同对象，但两者并不是彼此独立的。将第 3 章的标准化 CtR 份额与式（4.3）结合，可得

\[
\widetilde{\mathrm{CtR}}_i(x;\Sigma)
=
\frac{x_i(\Sigma x)_i}{x^\top \Sigma x}
=
\frac{x_i\,\sigma_i}{\sigma_p(x)}
\mathrm{CtB}_i(x;\Sigma).
\tag{4.7}
\]

式（4.7）表明，标准化 CtR 份额等于“资本—波动缩放项”与 CtB 的乘积。由此可见，CtR 与 CtB 共享同一个协方差输入，但解释方向并不相同：CtR 关注风险份额分配，CtB 关注相关暴露结构。

式（4.7）也说明，CtB 的均衡并不推出 CtR 的均衡。即便不同资产具有相近的 CtB 值，只要 \(x_i\sigma_i/\sigma_p(x)\) 的缩放项存在显著差异，各资产承担的 CtR 份额仍然可能明显不同。反过来，CtR 份额相近也不意味着 CtB 必然均衡，因为风险份额相等可以通过不同的权重—波动组合实现，而这些组合在相关结构上未必相同。正是这种“有联系但不等价”的关系，构成了本文将 CtR 与 CtB 分层处理的理论依据。

在本文的主线中，CtR 仍然是自然的主配置对象，因为它直接对应风险预算问题，并能够明确回答“组合风险如何分配”这一核心问题。CtB 则更适合作为结构控制对象，因为它刻画的是资产与组合之间的相关暴露形态。若将 CtB 与 CtR 直接并列为对称双目标，一方面会削弱风险预算的主导地位，另一方面也会使参数解释变得含混。相反，将 CtB 处理为后续模型中的结构约束或 band control，则能够同时保留 CtR 的配置解释和 CtB 的结构解释。

至此，本章已经完成 CtB 定义、离散度表达和角色定位三项核心工作。下一章将在此基础上正式给出 CtR–CtB 协调模型，并说明为什么其最合理的组织方式不是对称双目标，而是 CtR 主目标加 CtB 结构约束。

---

## 参考文献

Choueifaty, Y., & Coignard, Y. (2008). Toward Maximum Diversification. *The Journal of Portfolio Management*, 35(1), 40–51.

Lohre, H., Opfer, H., & Orszag, G. (2012). Diversified Risk Parity Strategies for Equity Portfolio Selection. *Journal of Investing* / related working paper version.

Menchero, J., & Davis, B. (2011). Risk Contribution Is Exposure Times Volatility Times Correlation: Decomposing Risk Using the X-Sigma-Rho Formula. *Journal of Performance Measurement* / research note version.

Qian, E. (2006). *On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up*. Research note / working paper.
