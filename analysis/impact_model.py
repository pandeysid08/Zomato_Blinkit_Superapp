"""Illustrative incremental-NOV scenarios for cross-app adoption.
Zomato monthly transacting customers (27.2M) and Q1 FY27 group NOV (Rs 31,120 cr)
are reported (S1, S2). Adoption rate, orders per month and extra basket are ASSUMPTIONS."""
ZOMATO_MTC, ORDERS_PM, EXTRA_BASKET, GROUP_NOV_CR = 27.2e6, 1.5, 150, 31120
for a in (0.05, 0.10, 0.15):
    q_cr = ZOMATO_MTC * a * ORDERS_PM * EXTRA_BASKET * 3 / 1e7
    print(f"adoption {a:.0%}: +Rs {q_cr:,.0f} cr per quarter ({q_cr / GROUP_NOV_CR:.2%} of group NOV)")
