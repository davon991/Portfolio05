# chapter_05_coordinated_model_draft_v1_3_cn.md

# 第5章 CtR–CtB协调模型：主目标、结构约束与参数分层

## 5.1 协调模型的正式定义

第 3 章与第 4 章分别给出了 CtR 与 CtB 的形式化表达。前者刻画风险份额配置，后者刻画资产与组合之间的相关结构。基于这两个对象，本文在 long-only 可行域上定义如下协调模型：

\[
\min_{x\in\mathcal{X}}
\;
D_R(x;b)
+\eta\lVert x-x_{t-1}\rVert_2^2
+\gamma\lVert x\rVert_2^2
\qquad
\text{s.t.}
\qquad
D_B(x)\le \delta.
\tag{5.1}
\]

其中，\(D_R(x;b)\) 表示 CtR 偏离函数，\(D_B(x)\) 表示 CtB 离散度；\(\delta\) 为 CtB 容忍带上界，\(\eta\) 为平滑参数，\(\gamma\) 为轻度 \(L_2\) 正则参数。按照全篇统一约定，\(\delta,\eta\) 优先视为校准参数，\(\gamma,\rho\) 优先视为数值参数，而预算向量 \(b\)、资产集合与调仓制度属于结构设定。

式（5.1）确立了 CtR 与 CtB 在本文中的分工：CtR 是配置主目标，CtB 是结构约束对象。这样的设定并非将两个对象并列处理，而是在风险预算主线之上加入一个相关结构控制层。与传统约束风险预算问题类似，模型仍以主目标为核心，只是在可行配置集合上进一步施加结构要求。本文的区别在于，该附加要求直接作用于 CtB 离散度，因此相关结构控制被制度化地嵌入到风险预算问题之中。

## 5.2 Band机制与软约束实现

从理论上说，式（5.1）已经给出了模型的正式定义；但在数值实现中，不等式约束 \(D_B(x)\le \delta\) 还需要转化为可计算的形式。为此，本文采用 band 机制来理解该约束：当 \(D_B(x)\) 不超过 \(\delta\) 时，CtB 结构处于可接受区间；当 \(D_B(x)\) 超过 \(\delta\) 时，模型才对这种结构偏离作出修正。因此，\(\delta\) 的作用不是要求 CtB 始终达到完全均衡，而是给出一个可解释的结构容忍带。

在实现层，本文采用如下软约束惩罚形式：

\[
J_\rho(x)
=
D_R(x;b)
+\eta\lVert x-x_{t-1}\rVert_2^2
+\gamma\lVert x\rVert_2^2
+\frac{\rho}{2}[D_B(x)-\delta]_+^2,
\tag{5.2}
\]

其中 \([u]_+=\max(u,0)\)，\(\rho>0\) 为罚参数。式（5.2）的含义是：当 \(D_B(x)\le \delta\) 时，惩罚项为零；当 \(D_B(x)>\delta\) 时，惩罚项开始生效，并随超出幅度增大而增强。这样一来，CtB 控制并不是无条件追求最小化，而是在结构偏离过大时才介入。

式（5.1）与式（5.2）分别对应模型的两个层次。前者界定研究问题本身，后者提供可计算的实现路径。两者的逻辑并不冲突：硬约束形式说明模型要解决什么问题，软约束形式说明该问题如何被纳入统一求解流程。因此，\(\rho\) 的角色首先是数值性的，而不是额外的经济偏好参数。

## 5.3 参数角色与退化关系

式（5.1）中的参数具有不同层次的含义。\(\delta\) 决定 CtB 容忍带的宽窄，是结构约束强度的直接载体；\(\eta\) 控制相邻调仓期之间的权重变化惩罚，从而影响路径平滑与交易稳定性；\(\gamma\) 提供轻度正则，用于改善数值条件并抑制过于尖锐的权重结构；\(\rho\) 则用于保证软约束实现的稳定性。正因为四者角色不同，本文不将其视为同类自由参数，而是坚持参数分层：\(\delta,\eta\) 进入校准协议，\(\gamma,\rho\) 主要由数值稳定性驱动。

这一分层可以通过退化关系得到进一步说明。首先，当 \(\delta\) 足够大，以至于最优解处 \(D_B(x)\le \delta\) 自然成立时，CtB 约束不再激活，式（5.1）便退化为带平滑项与正则项的 CtR-only 问题：

\[
\min_{x\in\mathcal{X}}
\;
D_R(x;b)
+\eta\lVert x-x_{t-1}\rVert_2^2
+\gamma\lVert x\rVert_2^2.
\tag{5.3}
\]

这一退化关系说明，CtR 始终是模型的主轴，CtB 的引入不是替换主目标，而是在必要时刻施加结构修正。

其次，当 \(\eta=0\) 时，模型不再显式惩罚相邻调仓期之间的权重变化，结果将更多反映当期风险结构本身，而较少考虑路径平滑。因此，\(\eta\) 的主要作用是实现层的稳定控制，而不是改变研究问题。

再次，\(\gamma\) 的作用是轻度而技术性的。它不改变 CtR 与 CtB 的角色分工，也不承担独立的经济解释；正文对它的说明应保持克制，其主要价值在于改善数值条件并避免极端权重结构。

由此可以看到，本文模型并不是为了同时最小化所有维度，而是在 CtR 主导下对 CtB 施加可解释的控制。第 5 章的任务也仅限于完成模型层的三项冻结：正式定义协调模型，说明 band 的实现方式，并明确参数的层次与边界。下一章将在此基础上转向统一求解制度。

---

## 参考文献

Maillard, S., Roncalli, T., & Teiletche, J. (2010). On the Properties of Equally Weighted Risk Contribution Portfolios. *The Journal of Portfolio Management*, 36(4), 60–70.

Menchero, J., & Davis, B. (2011). Risk Contribution Is Exposure Times Volatility Times Correlation: Decomposing Risk Using the X-Sigma-Rho Formula. *Journal of Performance Measurement* / research note version.

Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization* (2nd ed.). Springer.

Qian, E. (2006). *On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up*. Research note / working paper.

Richard, J.-C., & Roncalli, T. (2019). *Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles*. Working paper / arXiv version.
