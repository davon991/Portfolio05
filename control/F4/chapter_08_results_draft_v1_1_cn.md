# chapter_08_results_draft_v1_1_cn.md

# 第8章 样本外结果与机制解释

## 8.1 结构结果

本文首先考察结构指标，因为协调模型的核心并不是追求单一绩效最优，而是在 CtR 主导下对 CtB 施加可解释的控制。Figure 8.1 与 Table 8.2 表明，主模型在结构维度上处于 `CtR-only` 与 `CtB-only` 之间的稳定中间位置。相较于 `CtR-only`，其 \(D_B\) 由 0.0459 降至 0.0227，而 \(D_R\) 由接近零上升至 0.0024；相较于 `CtB-only`，其 \(D_R\) 显著更低，而 \(D_B\) 虽高于 `CtB-only`，但仍明显低于 `EW` 与 `GMV`。这一结果说明，协调模型并不试图同时压低所有维度，而是以有限的 CtR 代价换取更可控的相关结构。

![Figure 8.1 Main trade-off map](fig_8_1_tradeoff.png)

**图8.1** 结构折中图。横轴为 mean \(D_B\)，纵轴为 mean \(D_R\)，气泡大小对应平均换手率。

**表8.2** Structural mechanism summary。

| strategy | Mean \(D_R\) | Mean \(D_B\) | Active rate | Mean turnover | Failure rate |
|---|---:|---:|---:|---:|---:|
| CtB-only | 0.041 | 0.001 | 0.000 | 0.087 | 0.000 |
| CtR-only | 0.000 | 0.046 | 0.000 | 0.044 | 0.000 |
| EW | 0.018 | 0.219 | 0.000 | 0.017 | 0.000 |
| GMV | 0.302 | 0.238 | 0.000 | 0.074 | 0.000 |
| MDP | 0.040 | 0.002 | 0.000 | 0.091 | 0.000 |
| Main | 0.002 | 0.023 | 0.983 | 0.056 | 0.000 |

从 Table 8.2 还可以看到，主模型的 active rate 为 0.983，说明在测试期内 CtB band 在绝大多数时期都处于激活状态；同时 failure rate 仍保持为零，表明这种结构控制并未以明显的数值失败为代价。与 `EW` 和 `GMV` 相比，主模型在 \(D_B\) 上也具有明显优势，这说明单纯的资本平均或低波动配置并不会自动带来更好的 CtR–CtB 结构。

## 8.2 动态证据与横截面解释

静态均值能够说明总体方向，但不足以展示协调模型在滚动环境中的实际作用。Figure 8.2 给出了主模型与 `CtR-only` 的 \(D_B\) 和 \(D_R\) 时间序列比较。可以看到，在大多数调仓期内，主模型的 \(D_B\) 明显低于 `CtR-only`，而 \(D_R\) 则相应更高。这与 Figure 8.1 的横截面结论一致：CtB 约束持续压低了结构离散度，但这一改进需要以偏离纯 CtR 预算为代价。

![Figure 8.2 Rolling structural comparison](fig_8_2_rolling_drdb.png)

**图8.2** 主模型与 `CtR-only` 的滚动结构比较。上图为 \(D_B\)，下图为 \(D_R\)。

Figure 8.3 进一步展示了最新一次调仓时点的资本配置与 CtR 贡献份额。图中可以看到，资本权重与 CtR 贡献并不一一对应。例如，资本占比较高的资产未必承担同等比例的风险贡献，而部分资本权重并不突出的资产却可能贡献更高的 CtR 份额。这说明协调模型并不是在做简单的资本平均化，而是在给定协方差结构下同时调节资本配置与风险份额，以维持更均衡的 CtR–CtB 结构。

![Figure 8.3 Capital allocation vs CtR contribution](fig_8_3_capital_vs_contribution.png)

**图8.3** 最新一次调仓时点的资本配置与 CtR 贡献份额对比。

## 8.3 绩效结果与数值可靠性

在绩效维度上，主模型并不是样本外收益冠军。Table 8.1 与 Figure 8.4 显示，`EW` 的年化收益与 Sharpe 最高，`GMV` 的最大回撤最低，而主模型的年化收益为 3.39%，Sharpe 为 0.609，最大回撤为 -12.33%。因此，本文不主张主模型在收益或风险调整收益上支配 `EW` 或 `GMV`。主模型的意义在于，它在保持可接受收益表现的同时，显著改善了结构指标，并且没有出现明显的数值失稳。

![Figure 8.4 Cumulative return and drawdown](fig_8_4_cumret_drawdown.png)

**图8.4** 主模型、`EW`、`GMV` 与 `CtR-only` 的累计财富曲线与回撤曲线。

**表8.1** Overall performance and trading。

| strategy | Ann. return | Ann. vol | Sharpe | Max drawdown | Mean turnover |
|---|---:|---:|---:|---:|---:|
| CtB-only | 0.029 | 0.046 | 0.624 | -0.103 | 0.087 |
| CtR-only | 0.037 | 0.060 | 0.624 | -0.128 | 0.044 |
| EW | 0.069 | 0.087 | 0.798 | -0.157 | 0.017 |
| GMV | 0.019 | 0.026 | 0.734 | -0.074 | 0.074 |
| MDP | 0.029 | 0.047 | 0.632 | -0.104 | 0.091 |
| Main | 0.034 | 0.056 | 0.609 | -0.123 | 0.056 |

数值可靠性见 Table 8.3。对于主结果比较所对应的样本外阶段，各主要策略的 success rate 均为 1.000，nonconverged rate 为零；主模型的 fallback rate 为有限正值，但 median KKT residual 仍保持在 \(10^{-10}\) 量级，说明回退更适合被理解为保护性机制，而不是求解失败。`GMV` 虽采用单独实现，但 success rate 同样为 1.000，因此其作为基准的数值地位是稳定的。

**表8.3** Solver reliability summary（样本外阶段）。

| strategy | Success rate | Fallback rate | Mean PG iter | Mean Newton iter | Median KKT residual |
|---|---:|---:|---:|---:|---:|
| CtB-only | 1.000 | 0.000 | 294.9 | 2.0 | 1.13e-02 |
| CtR-only | 1.000 | 0.017 | 218.1 | 2.0 | 2.69e-11 |
| EW | 1.000 | 0.000 | 0.0 | 0.0 | 0.00e+00 |
| GMV | 1.000 | 0.000 | 0.0 | 35.8 | 7.59e-04 |
| MDP | 1.000 | 0.000 | 253.3 | 1.7 | 1.15e-01 |
| Main | 1.000 | 0.017 | 256.3 | 1.9 | 2.08e-10 |

综上，主模型的样本外意义不在于收益冠军地位，而在于：它以有限的 CtR 代价换取更低的 CtB 离散度，在动态路径上持续体现这一结构性取舍，并在数值上保持稳定。就本文的研究目标而言，这一结果已经足以支持协调模型作为可解释结构折中方案的主张。

---

## 参考文献

Bailey, D. H., & López de Prado, M. (2014). The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality. *Journal of Portfolio Management* / working paper version.

White, H. (2000). A Reality Check for Data Snooping. *Econometrica*, 68(5), 1097–1126.
