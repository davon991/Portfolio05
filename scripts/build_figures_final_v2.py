from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

PALETTE: Dict[str, str] = {
    "Main": "#1F3A5F",
    "CtR-only": "#4C78A8",
    "CtB-only": "#2F6B3B",
    "MDP": "#7A6F5A",
    "GMV": "#8C8C8C",
    "EW": "#C7A34B",
}

NEUTRAL = "#D9D9D9"
TEXT = "#222222"
HIGHLIGHT = "#B23A48"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def save(fig, out_png: Path, out_pdf: Path) -> None:
    fig.tight_layout()
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)


def build_figure_7_1(root: Path, out_dir: Path) -> None:
    calib = read_csv(root / "results" / "runs" / "calibration__main__val__20260419__01" / "analysis" / "calibration_summary.csv")
    # Expect columns: delta, eta, dr_mean, db_mean, turnover_mean, failure_rate, active_rate, sharpe
    deltas = sorted(calib["delta"].unique())
    etas = sorted(calib["eta"].unique())
    db_mat = np.full((len(deltas), len(etas)), np.nan)
    annotations: List[List[str]] = [["" for _ in etas] for _ in deltas]

    for i, d in enumerate(deltas):
        for j, e in enumerate(etas):
            row = calib[(calib["delta"] == d) & (calib["eta"] == e)]
            if row.empty:
                continue
            r = row.iloc[0]
            db_mat[i, j] = r["db_mean"]
            annotations[i][j] = f"DR {r['dr_mean']:.3f}\nTO {r['turnover_mean']:.3f}"

    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    im = ax.imshow(db_mat, aspect="auto")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("Mean $D_B$")

    ax.set_xticks(range(len(etas)))
    ax.set_xticklabels([f"{x:.2f}" for x in etas])
    ax.set_yticks(range(len(deltas)))
    ax.set_yticklabels([f"{x:.2f}" for x in deltas])
    ax.set_xlabel(r"$\eta$")
    ax.set_ylabel(r"$\delta$")
    ax.set_title("Figure 7.1  Validation calibration heatmap")

    for i in range(len(deltas)):
        for j in range(len(etas)):
            if not np.isnan(db_mat[i, j]):
                ax.text(j, i, annotations[i][j], ha="center", va="center", fontsize=8, color="white")

    # highlight d08 = delta 0.02, eta 0.05
    if 0.02 in deltas and 0.05 in etas:
        i = deltas.index(0.02)
        j = etas.index(0.05)
        rect = patches.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, lw=2.5, ec=HIGHLIGHT)
        ax.add_patch(rect)

    save(fig, out_dir / "fig_7_1_calibration_heatmap.png", out_dir / "fig_7_1_calibration_heatmap.pdf")


def build_figure_8_1(root: Path, out_dir: Path) -> None:
    df = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "summary_metrics.csv")
    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    for _, r in df.iterrows():
        s = r["strategy"]
        ax.scatter(r["db_mean"], r["dr_mean"], s=800 * r["turnover_mean"] + 70, label=s, color=PALETTE.get(s, "#666666"))
        if s in {"Main", "CtR-only", "CtB-only"}:
            ax.annotate(s, (r["db_mean"], r["dr_mean"]), xytext=(5, 4), textcoords="offset points")
    ax.set_xlabel("Mean $D_B$")
    ax.set_ylabel("Mean $D_R$")
    ax.set_title("Figure 8.1  Main trade-off map")
    ax.legend(frameon=False, ncol=2)
    save(fig, out_dir / "fig_8_1_tradeoff.png", out_dir / "fig_8_1_tradeoff.pdf")


def build_figure_8_2(root: Path, out_dir: Path) -> None:
    drdb = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "dr_db_timeseries.csv")
    obj = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "objective_terms.csv")
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 6.2), sharex=True)

    for s in ["Main", "CtR-only"]:
        d = drdb[drdb["strategy"] == s].copy()
        d["date"] = pd.to_datetime(d["date"])
        axes[0].plot(d["date"], d["D_B"], label=s, color=PALETTE[s])
        axes[1].plot(d["date"], d["D_R"], label=s, color=PALETTE[s])

    m = obj[obj["strategy"] == "Main"].copy()
    if "date" in m.columns:
        m["date"] = pd.to_datetime(m["date"])
        if "band_active" in m.columns:
            active_dates = m.loc[m["band_active"].fillna(0).astype(int) == 1, "date"]
            for x in active_dates:
                for ax in axes:
                    ax.axvline(x, color=NEUTRAL, lw=0.6, alpha=0.4)

    axes[0].set_ylabel("$D_B$")
    axes[1].set_ylabel("$D_R$")
    axes[1].set_xlabel("Date")
    axes[0].legend(frameon=False)
    axes[1].legend(frameon=False)
    axes[0].set_title("Figure 8.2  Rolling structural comparison: Main vs CtR-only")
    save(fig, out_dir / "fig_8_2_rolling_drdb.png", out_dir / "fig_8_2_rolling_drdb.pdf")


def build_figure_8_3(root: Path, out_dir: Path) -> None:
    weights = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "weights.csv")
    ctr = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "ctr_long.csv")

    w = weights[weights["strategy"] == "Main"].copy()
    c = ctr[ctr["strategy"] == "Main"].copy()
    w["date"] = pd.to_datetime(w["date"])
    c["date"] = pd.to_datetime(c["date"])
    last_date = w["date"].max()

    w = w[w["date"] == last_date][["asset", "weight"]].copy()
    c = c[c["date"] == last_date][["asset", "ctr"]].copy()
    df = w.merge(c, on="asset", how="inner")
    if df.empty:
        return

    total_ctr = df["ctr"].sum()
    if abs(total_ctr) > 1e-12:
        df["ctr_share"] = df["ctr"] / total_ctr
    else:
        df["ctr_share"] = df["ctr"]

    df = df.sort_values("weight")
    fig, ax = plt.subplots(figsize=(8.0, 5.6))
    y = np.arange(len(df))
    ax.barh(y, -df["ctr_share"], color=PALETTE["CtR-only"], label="CtR contribution share")
    ax.barh(y, df["weight"], color=PALETTE["Main"], label="Capital weight")

    ax.set_yticks(y)
    ax.set_yticklabels(df["asset"])
    ax.set_xlabel("Share")
    ax.set_title("Figure 8.3  Capital allocation vs CtR contribution (Main, latest rebalance)")
    ax.axvline(0, color=TEXT, lw=0.8)
    ax.legend(frameon=False)
    save(fig, out_dir / "fig_8_3_capital_vs_contribution.png", out_dir / "fig_8_3_capital_vs_contribution.pdf")


def build_figure_8_4(root: Path, out_dir: Path) -> None:
    mr = read_csv(root / "results" / "runs" / "full__main__test__20260419__01" / "analysis" / "monthly_returns.csv")
    mr["date"] = pd.to_datetime(mr["date"])
    keep = ["Main", "EW", "GMV", "CtR-only"]
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 6.4), sharex=True)
    for s in keep:
        d = mr[mr["strategy"] == s].sort_values("date").copy()
        wealth = (1 + d["period_return"]).cumprod()
        drawdown = wealth / wealth.cummax() - 1.0
        axes[0].plot(d["date"], wealth, label=s, color=PALETTE[s])
        axes[1].plot(d["date"], drawdown, label=s, color=PALETTE[s])
    axes[0].set_ylabel("Cumulative wealth")
    axes[1].set_ylabel("Drawdown")
    axes[1].set_xlabel("Date")
    axes[0].legend(frameon=False, ncol=2)
    axes[0].set_title("Figure 8.4  Cumulative return and drawdown")
    save(fig, out_dir / "fig_8_4_cumret_drawdown.png", out_dir / "fig_8_4_cumret_drawdown.pdf")


def main(root: str = ".") -> None:
    root = Path(root)
    out_dir = root / "results" / "final_factory" / "figures"
    ensure_dir(out_dir)
    build_figure_7_1(root, out_dir)
    build_figure_8_1(root, out_dir)
    build_figure_8_2(root, out_dir)
    build_figure_8_3(root, out_dir)
    build_figure_8_4(root, out_dir)


if __name__ == "__main__":
    main()
