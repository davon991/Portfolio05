# Приложение C. Листинги программ

В данном приложении приведены основные фрагменты программного кода, использованные для реализации модели портфельной оптимизации и эмпирических расчетов. Листинги охватывают расчет структурных показателей, построение целевых функций, интерфейсы стратегий, численное решение задачи на симплексе без коротких позиций, скользящий расчет, калибровку параметров, статистическую проверку и анализ численной надежности. Чтение данных, сохранение результатов и построение рисунков используются как вспомогательные процедуры для подготовки эмпирических материалов; основные листинги сосредоточены на вычислении показателей, оптимизационных задачах, численном решении, калибровке и статистической проверке.

## C.1. Расчет показателей CtR, CtB, \(D_R\) и \(D_B\)

Листинг C.1 реализует портфельную дисперсию, портфельную волатильность, вклады CtR, нормированные доли CtR, значения CtB и две меры отклонения \(D_R\) и \(D_B\). Эти вычисления соответствуют основным определениям разделов 2–4.

```python
import numpy as np


def portfolio_variance(x: np.ndarray, sigma: np.ndarray) -> float:
    return float(x @ sigma @ x)


def portfolio_volatility(x: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.sqrt(max(portfolio_variance(x, sigma), 1e-16)))


def ctr_values(x: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    vol = portfolio_volatility(x, sigma)
    return x * (sigma @ x) / vol


def ctr_shares(x: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    var = max(portfolio_variance(x, sigma), 1e-16)
    return x * (sigma @ x) / var


def ctb_values(x: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    sig_i = np.sqrt(np.clip(np.diag(sigma), 1e-16, None))
    sig_p = portfolio_volatility(x, sigma)
    return (sigma @ x) / (sig_i * sig_p)


def d_r(x: np.ndarray, sigma: np.ndarray, b: np.ndarray) -> float:
    shares = ctr_shares(x, sigma)
    gap = shares - b
    return float(0.5 * np.sum(gap**2))


def d_b(x: np.ndarray, sigma: np.ndarray) -> float:
    vals = ctb_values(x, sigma)
    gap = vals - vals.mean()
    return float(0.5 * np.sum(gap**2))
```

## C.2. Целевые функции и реализация стратегий

Листинг C.2 задает целевые функции для CtR-only, CtB-only и модели CtR–CtB. Разложение целевой функции на отдельные компоненты позволяет фиксировать вклад риск-бюджетного члена, CtB-члена, сглаживания весов, регуляризации и штрафа за нарушение CtB-band.

```python
from dataclasses import dataclass
import numpy as np


@dataclass
class ObjectiveBreakdown:
    obj_total: float
    dr_term: float
    db_term: float
    smooth_term: float
    l2_term: float
    band_penalty: float


def objective_ctro_only(x, sigma, b, x_prev, eta, gamma):
    dr_term = d_r(x, sigma, b)
    smooth_term = float(eta * np.sum((x - x_prev)**2)) if x_prev is not None else 0.0
    l2_term = float(gamma * np.sum(x**2))
    total = dr_term + smooth_term + l2_term
    return ObjectiveBreakdown(total, dr_term, 0.0, smooth_term, l2_term, 0.0)


def objective_ctb_only(x, sigma, x_prev, eta, gamma):
    db_term = d_b(x, sigma)
    smooth_term = float(eta * np.sum((x - x_prev)**2)) if x_prev is not None else 0.0
    l2_term = float(gamma * np.sum(x**2))
    total = db_term + smooth_term + l2_term
    return ObjectiveBreakdown(total, 0.0, db_term, smooth_term, l2_term, 0.0)


def objective_main(x, sigma, b, x_prev, eta, gamma, delta, rho):
    dr_term = d_r(x, sigma, b)
    db_term = d_b(x, sigma)
    smooth_term = float(eta * np.sum((x - x_prev)**2)) if x_prev is not None else 0.0
    l2_term = float(gamma * np.sum(x**2))
    violation = max(db_term - delta, 0.0)
    band_penalty = float(0.5 * rho * violation**2)
    total = dr_term + smooth_term + l2_term + band_penalty
    return ObjectiveBreakdown(total, dr_term, db_term, smooth_term, l2_term, band_penalty)
```

Интерфейс стратегии передает целевую функцию в общий solver. Равновесная стратегия не требует оптимизации, GMV решается как выпуклая квадратичная задача, а остальные нелинейные стратегии рассчитываются с помощью единой численной процедуры.

```python
def solve_main(sigma, b, x_prev, eta, gamma, delta, rho, solver_cfg=None):
    n = sigma.shape[0]
    x0 = project_to_simplex(x_prev if x_prev is not None else np.ones(n) / n)
    func = lambda x: objective_main(x, sigma, b, x_prev, eta, gamma, delta, rho).obj_total
    res = projected_gradient_then_newton(func, x0, **(solver_cfg or {}))
    return res.weights, res
```

## C.3. Численный метод решения

Листинг C.3 показывает проекцию на long-only simplex и двухэтапную схему решения. Проекция обеспечивает неотрицательность весов и выполнение бюджетного ограничения. Затем используется проекционный градиентный этап и локальное ньютоновское уточнение на свободных координатах. Для контроля качества решения сохраняются статус сходимости, KKT-остаток, число итераций и признак использования резервного шага.

```python
def project_to_simplex(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float)
    if np.all(v >= 0) and np.isclose(v.sum(), 1.0):
        return v.copy()
    n = v.size
    u = np.sort(v)[::-1]
    cssv = np.cumsum(u)
    rho = np.nonzero(u * np.arange(1, n + 1) > (cssv - 1))[0]
    if len(rho) == 0:
        return np.ones(n) / n
    rho = rho[-1]
    theta = (cssv[rho] - 1) / (rho + 1.0)
    w = np.maximum(v - theta, 0)
    s = w.sum()
    return w / s if s > 0 else np.ones(n) / n
```

```python
def projected_gradient_then_newton(func, x0, pg_max_iter=300, pg_step=0.1,
                                   pg_tol=1e-7, newton_max_iter=20,
                                   interior_eps=1e-6):
    x = project_to_simplex(np.asarray(x0, dtype=float))
    f_prev = func(x)
    fallback_used = False

    for pg_iter in range(1, pg_max_iter + 1):
        g = numerical_grad(func, x)
        step = pg_step
        improved = False
        for _ in range(20):
            x_new = project_to_simplex(x - step * g)
            f_new = func(x_new)
            if f_new <= f_prev + 1e-12:
                improved = True
                break
            step *= 0.5
        if not improved:
            fallback_used = True
            break
        if np.linalg.norm(x_new - x) < pg_tol:
            x = x_new
            f_prev = f_new
            break
        x = x_new
        f_prev = f_new

    for newton_iter in range(1, newton_max_iter + 1):
        free = np.where(x > interior_eps)[0]
        if len(free) <= 1:
            break
        base = free[:-1]
        last = free[-1]

        def reduced_func(z):
            xr = x.copy()
            xr[base] = z
            xr[last] = 1.0 - xr.sum() + xr[last]
            if (xr < 0).any():
                return 1e12
            return func(xr)

        z0 = x[base].copy()
        gz = numerical_grad(reduced_func, z0)
        hz = numerical_hessian(reduced_func, z0) + 1e-6 * np.eye(len(z0))
        try:
            dz = -np.linalg.solve(hz, gz)
        except np.linalg.LinAlgError:
            fallback_used = True
            break

        step = 1.0
        improved = False
        for _ in range(20):
            z_new = z0 + step * dz
            xr = x.copy()
            xr[base] = z_new
            xr[last] = 1.0 - xr.sum() + xr[last]
            if (xr >= -1e-12).all() and func(project_to_simplex(xr)) <= func(x) + 1e-12:
                x = project_to_simplex(xr)
                improved = True
                break
            step *= 0.5
        if not improved:
            fallback_used = True
            break

    resid = kkt_residual_simplex(func, x)
    return SolverResult(x, resid < 1e-5, pg_iter, newton_iter, resid,
                        fallback_used, int((x > interior_eps).sum()),
                        'success' if resid < 1e-5 else 'partial', float(func(x)))
```

## C.4. Основной цикл расчета и калибровка параметров

Листинг C.4 показывает скользящий расчет портфельных стратегий. На каждом шаге ребалансировки по историческим доходностям оценивается ковариационная матрица, после чего рассчитываются EW, GMV, CtR-only, MDP, CtB-only и модель CtR–CtB. Затем сохраняются веса, структурные показатели, оборот портфеля, доходность периода и диагностика численного решения. В программном выводе `Main` является расчетным обозначением модели CtR–CtB.

```python
strategies = ['EW', 'GMV', 'CtR-only', 'MDP', 'CtB-only', 'Main']

for idx in range(len(month_ends) - 1):
    reb_date = month_ends[idx]
    next_date = month_ends[idx + 1]
    hist = returns[returns.index <= reb_date].tail(window)
    sigma = estimate_covariance(hist, method=cov_estimator)

    solved = {}
    diagnostics = {}
    solved['EW'], diagnostics['EW'] = equal_weight(n)
    solved['GMV'], diagnostics['GMV'] = solve_gmv(sigma, solver_cfg)
    solved['CtR-only'], diagnostics['CtR-only'] = solve_ctr_only(sigma, b, prev_weights['CtR-only'], eta, gamma, solver_cfg)
    solved['MDP'], diagnostics['MDP'] = solve_mdp(sigma, gamma=gamma, solver_cfg=solver_cfg)
    solved['CtB-only'], diagnostics['CtB-only'] = solve_ctb_only(sigma, prev_weights['CtB-only'], eta, gamma, solver_cfg)
    solved['Main'], diagnostics['Main'] = solve_main(sigma, b, prev_weights['Main'], eta, gamma, delta, rho, solver_cfg)

    for strategy in strategies:
        x = solved[strategy]
        dr = d_r(x, sigma, b)
        db = d_b(x, sigma)
        turnover = float(np.abs(x - prev_weights[strategy]).sum()) if prev_weights[strategy] is not None else float(np.abs(x).sum())
        monthly_ret = monthly_held_return(returns, reb_date, next_date, x)
        prev_weights[strategy] = x.copy()
```

Калибровка параметров проводится на проверочном периоде. Перебираются значения \(\delta\) и \(\eta\); после каждого запуска извлекаются структурные показатели, оборот портфеля и статус решения для модели CtR–CtB.

```python
for delta, eta in itertools.product(delta_grid, eta_grid):
    run_cfg = deepcopy(base_config)
    run_cfg['model']['delta'] = float(delta)
    run_cfg['model']['eta'] = float(eta)
    artifacts = run_real_backtest(run_cfg, root)
    summary = pd.read_csv(artifacts.result_dir / 'analysis' / 'summary_metrics.csv')
    main_row = summary[summary['strategy'] == 'Main'].iloc[0].to_dict()
    records.append({'delta': delta, 'eta': eta, **main_row})
```

## C.5. Статистическая проверка и численная надежность

Листинг C.5 реализует moving block bootstrap для попарных различий между моделью CtR–CtB и базовыми стратегиями. Для каждой метрики рассчитываются средняя разность, доверительный интервал и результат односторонней проверки.

```python
def moving_block_bootstrap(arr: np.ndarray, block_size: int, n_boot: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = len(arr)
    block_size = max(1, min(block_size, n))
    starts = np.arange(0, n - block_size + 1)
    out = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        sample = []
        while len(sample) < n:
            s = int(rng.choice(starts))
            sample.extend(arr[s:s + block_size])
        out[b] = float(np.asarray(sample[:n]).mean())
    return out
```

Численная надежность проверяется по стратегиям. В сводке фиксируются доля успешных решений, доля резервных шагов, доля несходимости, число итераций и KKT-остаток.

```python
grouped = solver_diagnostics.groupby('strategy')
summary = grouped.agg(
    n_rows=('status', 'size'),
    success_rate=('status', lambda s: float((s == 'success').mean())),
    fallback_rate=('fallback_used', 'mean'),
    nonconverged_rate=('converged', lambda s: float((s == 0).mean())),
    mean_pg_iter=('iterations_pg', 'mean'),
    mean_newton_iter=('iterations_newton', 'mean'),
    median_kkt_residual=('kkt_residual', 'median'),
    max_kkt_residual=('kkt_residual', 'max'),
)
```

## Итог приложения

Приложение C содержит основные программные листинги, которые связывают математическую модель с эмпирическими расчетами. Листинг C.1 соответствует вычислению CtR, CtB, \(D_R\) и \(D_B\); листинг C.2 — целевым функциям и стратегиям; листинг C.3 — численному решению на long-only simplex; листинг C.4 — скользящий расчету и калибровке параметров; листинг C.5 — статистической проверке и анализу численной надежности. Тем самым теоретическая постановка, калибровка и результаты работы имеют единую программную основу.
