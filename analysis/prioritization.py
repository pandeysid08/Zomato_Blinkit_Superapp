"""Value-vs-Effort and RICE scoring for Zomato x Blinkit integration features.
Reach/Impact/Confidence/Effort inputs are ASSUMPTIONS (hypotheses to validate),
not company data. Kano classes are hypotheses to be confirmed by a user survey."""
import pandas as pd

features = pd.DataFrame([
    # feature, reach (% of Zomato MTC), impact (0.25-3), confidence %, effort (person-months), value (1-10), kano
    ("Cross-bundling (food + grocery in one cart)", 40, 2.0, 70, 6, 8, "Performance"),
    ("Unified subscription (one membership)",       30, 2.0, 60, 8, 8, "Performance"),
    ("'15-min Essentials' tab on Zomato",           50, 1.0, 80, 3, 6, "Attractive"),
    ("Unified wallet / single checkout",            60, 0.5, 80, 4, 5, "Must-be"),
    ("Cross-app recommendations",                   35, 1.0, 50, 5, 5, "Attractive"),
], columns=["feature", "reach_pct", "impact", "confidence_pct", "effort_pm", "value", "kano"])

features["rice"] = (features.reach_pct * features.impact * features.confidence_pct / 100) / features.effort_pm
features["value_vs_effort"] = features.value / features.effort_pm
print(features.sort_values("rice", ascending=False).round(2).to_string(index=False))
features.to_csv("data/feature_prioritization.csv", index=False)
