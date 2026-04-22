from __future__ import annotations

from pathlib import Path
import pandas as pd


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_table(df: pd.DataFrame, out_csv: Path, out_tex: Path) -> None:
    df.to_csv(out_csv, index=False)
    try:
        tex = df.to_latex(index=False, float_format="%.4f")
    except Exception:
        tex = df.to_string(index=False)
    out_tex.write_text(tex, encoding="utf-8")


def main(root: str = ".") -> None:
    root = Path(root)
    out_dir = root / "results" / "final_factory" / "tables"
    ensure_dir(out_dir)

    calib_dir = root / "results" / "runs" / "calibration__main__val__20260419__01" / "analysis"
    full_dir = root / "results" / "runs" / "full__main__test__20260419__01" / "analysis"
    robust_dir = root / "results" / "runs" / "full__robust__d04__20260419__01" / "analysis"
    solver_dir = root / "results" / "solver_reliability"
    inf_dir = full_dir / "inference"

    # Main tables
    t71 = pd.read_csv(calib_dir / "calibration_summary.csv")
    write_table(t71, out_dir / "table_7_1_calibration.csv", out_dir / "table_7_1_calibration.tex")

    t81 = pd.read_csv(full_dir / "summary_metrics.csv")
    cols = [c for c in ["strategy","ann_return","ann_vol","sharpe","max_drawdown","turnover_mean","turnover_p95"] if c in t81.columns]
    write_table(t81[cols], out_dir / "table_8_1_performance.csv", out_dir / "table_8_1_performance.tex")

    t82 = pd.read_csv(full_dir / "summary_metrics.csv")
    cols = [c for c in ["strategy","dr_mean","db_mean","active_rate","turnover_mean","failure_rate"] if c in t82.columns]
    write_table(t82[cols], out_dir / "table_8_2_structure.csv", out_dir / "table_8_2_structure.tex")

    t83 = pd.read_csv(solver_dir / "solver_reliability_summary.csv")
    write_table(t83, out_dir / "table_8_3_solver.csv", out_dir / "table_8_3_solver.tex")

    # Appendix tables
    base = pd.read_csv(full_dir / "summary_metrics.csv")
    rob = pd.read_csv(robust_dir / "summary_metrics.csv")
    base["spec"] = "d08"
    rob["spec"] = "d04"
    app = pd.concat([base, rob], ignore_index=True)
    cols = [c for c in ["spec","strategy","dr_mean","db_mean","turnover_mean","ann_return","sharpe"] if c in app.columns]
    write_table(app[cols], out_dir / "table_A_1_d08_d04.csv", out_dir / "table_A_1_d08_d04.tex")

    if (inf_dir / "inference_summary.csv").exists():
        tA2 = pd.read_csv(inf_dir / "inference_summary.csv")
        write_table(tA2, out_dir / "table_A_2_inference.csv", out_dir / "table_A_2_inference.tex")

    if (solver_dir / "solver_failure_catalog.csv").exists():
        tA3 = pd.read_csv(solver_dir / "solver_failure_catalog.csv")
        write_table(tA3, out_dir / "table_A_3_solver_failures.csv", out_dir / "table_A_3_solver_failures.tex")


if __name__ == "__main__":
    main()
