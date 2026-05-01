# Portfolio05 / README

## 项目概述 / Обзор проекта

**中文：**  
本项目围绕 long-only 大类资产 ETF 组合配置展开，研究主线是：在保留 CtR（Contribution to Risk）作为主配置对象的前提下，引入 CtB（Correlation to Basket）作为结构控制对象，构造一个可求解、可校准、可检验的协调模型。

**Русский:**  
Данный проект посвящён long-only аллокации ETF широких классов активов. Основная исследовательская линия состоит в следующем: сохранить CtR (Contribution to Risk) как главный объект аллокации и одновременно ввести CtB (Correlation to Basket) как объект структурного контроля, чтобы построить согласованную модель, пригодную для решения, калибровки и проверки. 

---

## 1. 研究目标 / Цель проекта

**中文：**  
项目的目标不是寻找单纯的“收益冠军”策略，而是建立一条可解释的研究路径：  
1. 明确 CtR 与 CtB 的理论角色分工；  
2. 构造 CtR 主目标 + CtB 结构约束的协调模型；  
3. 通过统一求解器、统一校准制度和 out-of-sample 检验，给出结构性机制证据；  
4. 将代码、结果与论文叙述统一到同一套口径下。

**Русский:**  
Цель проекта состоит не в поиске стратегии-чемпиона по доходности, а в построении интерпретируемой исследовательской линии:  
1. Чётко разделить теоретические роли CtR и CtB;  
2. Построить координированную модель вида «CtR как основная цель + CtB как структурное ограничение»;  
3. Предоставить механизмное вневыборочное свидетельство через единый solver, единый протокол калибровки и out-of-sample проверку;  
4. Согласовать код, результаты и текст диссертации в одной общей системе обозначений и выводов.

---

## 2. 项目当前完成状态 / Текущее состояние проекта

**中文：**  
当前项目已经完成 thesis-level clean lineage：  
- toy smoke 与 toy A–G 合成实验；  
- minimal real ETF 预检流程；  
- validation calibration；  
- full test 主规格；  
- stricter-band robustness 规格；  
- inference package；  
- solver reliability aggregation；  
- 论文主图、主表与附录表导出；  
- 俄文论文成稿。

**Русский:**  
На текущем этапе проект уже завершил thesis-level clean lineage:  
- toy smoke и toy A–G синтетические эксперименты;  
- минимальный реальный ETF pipeline;  
- validation calibration;  
- full test для основной спецификации;  
- stricter-band robustness specification;  
- inference package;  
- агрегирование solver reliability;  
- экспорт основных рисунков, таблиц и приложений диссертации;  
- русскоязычный текст диссертации.

**已接受的 clean 主线 / Принятая clean-lineage цепочка:**
- `minimal_real__main__trainval__20260419__01`
- `calibration__main__val__20260419__01`
- `full__main__test__20260419__01`
- `full__robust__d04__20260419__01`
- clean inference package
- clean solver reliability aggregate

---

## 3. 仓库中应重点查看的内容 / Что в репозитории смотреть в первую очередь

### 3.1 代码与配置 / Код и конфигурации

**中文：**  
代码部分用于完成数据准备、实验执行、参数校准、统计推断、求解器可靠性汇总以及论文图表导出。配置文件定义实验协议，脚本文件对应可复现实验接口。

**Русский:**  
Кодовая часть отвечает за подготовку данных, запуск экспериментов, калибровку параметров, статистический вывод, агрегирование надёжности solver-а и экспорт диссертационных рисунков и таблиц. Конфигурационные файлы задают экспериментальный протокол, а скрипты реализуют воспроизводимые интерфейсы запуска.

**关键路径 / Ключевые пути:**
- `configs/`
  - `toy_smoke.yaml`
  - `toy_a.yaml` ... `toy_g.yaml`
  - `minimal_real.yaml`
  - `calibration.yaml`
  - `full_test.yaml`
  - `full_test_d04.yaml`
- `scripts/`
  - `run_experiment.py`
  - `run_calibration.py`
  - `run_inference.py`
  - `aggregate_solver_reliability.py`
  - `build_figures_final_v2.py`
  - `build_tables_final_v2.py`

### 3.2 结果目录 / Каталог результатов

**中文：**  
所有实验结果按 run_id 落在 `results/runs/` 下。论文最终图表与中间导出数据位于 `results/final_factory/`。

**Русский:**  
Все результаты экспериментов сохраняются под `results/runs/` в соответствии с run_id. Финальные рисунки, таблицы и сопутствующие экспортированные данные для диссертации находятся в `results/final_factory/`. 

**关键路径 / Ключевые пути:**
- `results/runs/<run_id>/`
- `results/solver_reliability/`
- `results/final_factory/figures/`
- `results/final_factory/tables/`
- `results/final_factory/figdata/`
- `results/final_factory/figmeta/`

---

## 4. 最小复现顺序 / Минимальный порядок воспроизведения

**中文：**  
若需要从代码层重新复核论文主线，可按下面的最小顺序执行。该顺序覆盖 toy 验证、真实数据、校准、主测试、稳健性、统计推断、求解器可靠性和最终图表导出。

**Русский:**  
Если требуется заново воспроизвести основную линию диссертации на уровне кода, рекомендуется следующий минимальный порядок. Он покрывает toy-проверку, реальный ETF pipeline, калибровку, основной тест, robustness, статистический вывод, надёжность solver-а и финальный экспорт рисунков и таблиц.

```powershell
python scripts\run_experiment.py --config configs\toy_smoke.yaml
python scripts\run_experiment.py --config configs\toy_a.yaml
python scripts\run_experiment.py --config configs\toy_b.yaml
python scripts\run_experiment.py --config configs\toy_c.yaml
python scripts\run_experiment.py --config configs\toy_d.yaml
python scripts\run_experiment.py --config configs\toy_e.yaml
python scripts\run_experiment.py --config configs\toy_f.yaml
python scripts\run_experiment.py --config configs\toy_g.yaml

python scripts\run_experiment.py --config configs\minimal_real.yaml
python scripts\run_calibration.py --config configs\calibration.yaml
python scripts\run_experiment.py --config configs\full_test.yaml
python scripts\run_experiment.py --config configs\full_test_d04.yaml
python scripts\run_inference.py --run-id full__main__test__20260419__01
python scripts\aggregate_solver_reliability.py
python scripts\build_figures_final_v2.py
python scripts\build_tables_final_v2.py
```

---

## 5. 论文结果层对应关系 / Соответствие уровня результатов диссертации

**主文图 / Основные рисунки:**
- Figure 7.1 — calibration heatmap
- Figure 8.1 — trade-off map
- Figure 8.2 — rolling structural comparison
- Figure 8.3 — capital allocation vs CtR contribution
- Figure 8.4 — cumulative return and drawdown

**主文表 / Основные таблицы:**
- Table 7.1 — calibration screening summary
- Table 8.1 — overall performance and trading
- Table 8.2 — structural mechanism summary
- Table 8.3 — solver reliability summary

**附录表 / Таблицы приложения:**
- Table A.1 — `d08` vs `d04` robustness
- Table A.2 — inference summary
- Table A.3 — solver failure catalog

---

## 6. 环境与依赖 / Среда и зависимости

**中文：**  
项目在 Windows PowerShell 环境下完成开发与运行，推荐使用虚拟环境。首次配置可按以下方式执行。

**Русский:**  
Проект разрабатывался и запускался в среде Windows PowerShell; рекомендуется использовать виртуальное окружение. Первичная настройка может быть выполнена следующим образом.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
