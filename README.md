# Zomato × Blinkit Integration: Building India's Lifestyle Superapp

A product analytics case study on integrating Zomato (food delivery) and Blinkit (quick commerce) under Eternal Ltd. It covers hypothesis-driven experimentation, feature prioritization (Value vs Effort, Kano, RICE) and a staged go-to-market plan tied to revenue, retention and engagement.

**Author:** Siddharth Pandey, IIT Bhubaneswar

## Problem
Zomato (27.2M monthly transacting customers) and Blinkit (31.8M) sit under one company but run as separate apps. How can an integrated experience raise AOV, retention and adoption?

## Deliverable
The 15-slide case study deck is included: [`Zomato_Blinkit_Product_Analytics_Case_Study.pptx`](Zomato_Blinkit_Product_Analytics_Case_Study.pptx).

## Key metrics (Eternal Q1 FY27, sourced in [SOURCES.md](SOURCES.md))
| Metric | Value |
|---|---|
| Group B2C NOV | ₹31,120 cr (+54% YoY) |
| Consolidated adj. EBITDA | ₹555 cr |
| Blinkit monthly transacting customers | 31.8M (vs 16.9M in Q1 FY26) |
| Blinkit net AOV | ₹518 (₹525 in Q4 FY26) |
| Blinkit dark stores | 2,443 (vs 1,544 a year ago) |
| Blinkit NOV/store/day | ₹8.27 lakh (steady-state target ₹11 lakh) |
| Blinkit inventory loss | 1.8% of NOV |
| Zomato monthly transacting customers | 27.2M (vs 22.9M) |

Full table: [`data/eternal_key_metrics.csv`](data/eternal_key_metrics.csv)

## Approach
1. **Hypothesis → Experiment → Insight.** For each feature, state a hypothesis, the metric it moves and an A/B design. See [`analysis/ab_test_simulation.py`](analysis/ab_test_simulation.py): ~3,291 users per arm detect a 4% AOV uplift (80% power, α=0.05, assumed SD ₹300).
2. **Prioritization.** Value vs Effort, Kano and RICE scoring in [`analysis/prioritization.py`](analysis/prioritization.py).

| Rank (RICE) | Feature | Kano (hypothesis) | RICE |
|---|---|---|---|
| 1 | "15-min Essentials" tab | Attractive | 13.3 |
| 2 | Cross-bundling | Performance | 9.3 |
| 3 | Unified wallet / checkout | Must-be | 6.0 |
| 4 | Unified subscription | Performance | 4.5 |
| 5 | Cross-app recommendations | Attractive | 3.5 |

3. **Staged GTM.** Pilot in top-density Blinkit cities → expand to all Zomato metros → national rollout with the unified subscription. Gate each stage on AOV, 30-day retention and cross-app adoption.

| Stage | Metric | Gate (proposed) |
|---|---|---|
| Pilot | Cross-app order share | Statistically significant lift vs control |
| Expansion | 30-day retention | Non-negative vs control |
| National | Blended AOV, revenue per user | Positive with inventory loss ≤ 1.8% of NOV |

## Important note on data
Company figures come from public Eternal disclosures and press coverage (see [SOURCES.md](SOURCES.md)). RICE inputs, Kano classes and the A/B simulation are **illustrative assumptions**, not company data or real experiment results. In the simulation, the 4% uplift at the calculated sample size gives p≈0.11 (seed 42), which shows why sample size and power planning matter.

## Run it
```bash
pip install pandas scipy numpy
python analysis/prioritization.py
python analysis/ab_test_simulation.py
python analysis/impact_model.py
```
Open `index.html` for a one-page summary, or `Zomato_Blinkit_Product_Analytics_Case_Study.pptx` for the 15-slide deck.

## Repo structure
```
├── README.md
├── SOURCES.md
├── index.html
├── Zomato_Blinkit_Product_Analytics_Case_Study.pptx
├── data/
│   ├── eternal_key_metrics.csv
│   └── feature_prioritization.csv
└── analysis/
    ├── prioritization.py
    ├── ab_test_simulation.py
    └── impact_model.py
```
