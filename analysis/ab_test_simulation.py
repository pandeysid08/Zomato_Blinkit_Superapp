"""Sample-size calculation + SIMULATED A/B test for a cross-bundle nudge.
Baseline AOV (Rs 518) is from Eternal Q1 FY27 (source S2). The AOV standard
deviation and the uplift are ASSUMPTIONS. Output is a method demo, not a result."""
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
BASE_AOV, SD, UPLIFT = 518, 300, 0.04   # SD and uplift assumed
alpha, power = 0.05, 0.80

delta = BASE_AOV * UPLIFT
n = 2 * ((stats.norm.ppf(1 - alpha / 2) + stats.norm.ppf(power)) * SD / delta) ** 2
N = int(np.ceil(n))
print(f"Required users per arm for {UPLIFT:.0%} AOV uplift: {N:,}")

def gamma(mean, size):
    return rng.gamma((mean / SD) ** 2, SD ** 2 / mean, size)

control, treat = gamma(BASE_AOV, N), gamma(BASE_AOV * (1 + UPLIFT), N)
t, p = stats.ttest_ind(treat, control, equal_var=False)
print(f"Simulated AOV  control={control.mean():.0f}  treatment={treat.mean():.0f}  p={p:.4f}")
