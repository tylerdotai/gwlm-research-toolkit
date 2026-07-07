#!/usr/bin/env python3
"""
Analysis for Sustained Treatment experiment.

Design:
- 60 sessions: 20 topics x 3 conditions (positive/negative/neutral)
- Each session: sustained treatment history preamble + final reflective prompt
- Probe A: TF-IDF on model responses → LogisticRegression → accuracy
- Probe B: TF-IDF on history preamble → LogisticRegression → accuracy
- H1: ANOVA — do conditions differ in response signal?
- H2: t-test — does response signal exceed preamble signal?
"""

import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from scipy import stats

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESPONSES_FILE = os.path.join(BASE_DIR, "experiments/sustained-treatment/responses.json")

def load_data():
    with open(RESPONSES_FILE) as f:
        data = json.load(f)
    return data

def run_analysis():
    print("Loading data...")
    data = load_data()
    responses = data.get("responses", [])
    
    valid = [r for r in responses if r.get("status") == "success" and r.get("response", "").strip()]
    print(f"Valid responses: {len(valid)}")
    
    # Build dataset
    X_response = []
    X_preamble = []
    y = []
    
    for r in valid:
        condition = r.get("condition")
        if not condition:
            continue
        response_text = r.get("response", "")
        if not response_text:
            continue
        preamble = r.get("history_preamble", "")
        
        X_response.append(response_text)
        X_preamble.append(preamble)
        y.append(condition)
    
    X_response = np.array(X_response)
    X_preamble = np.array(X_preamble)
    y = np.array(y)
    
    print(f"Dataset: {len(y)} samples")
    for cond in ["positive_treatment", "negative_treatment", "neutral_treatment"]:
        n = np.sum(y == cond)
        print(f"  {cond}: {n}")
    
    label_map = {"positive_treatment": 0, "neutral_treatment": 1, "negative_treatment": 2}
    y_numeric = np.array([label_map[cond] for cond in y])
    
    # Probe A: TF-IDF on responses
    print("\n=== PROBE A: Response-based TF-IDF ===")
    vec_a = TfidfVectorizer(max_features=1000, ngram_range=(1, 2), stop_words="english")
    X_a = vec_a.fit_transform(X_response)
    clf_a = LogisticRegression(max_iter=1000, random_state=42, solver="lbfgs")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores_a = cross_val_score(clf_a, X_a, y_numeric, cv=cv, scoring="accuracy")
    print(f"Probe A accuracy: {scores_a.mean():.3f} (+/- {scores_a.std()*2:.3f})")
    
    # Probe B: TF-IDF on history preamble
    print("\n=== PROBE B: Preamble-based TF-IDF ===")
    vec_b = TfidfVectorizer(max_features=1000, ngram_range=(1, 2), stop_words="english")
    X_b = vec_b.fit_transform(X_preamble)
    clf_b = LogisticRegression(max_iter=1000, random_state=42, solver="lbfgs")
    scores_b = cross_val_score(clf_b, X_b, y_numeric, cv=cv, scoring="accuracy")
    print(f"Probe B accuracy: {scores_b.mean():.3f} (+/- {scores_b.std()*2:.3f})")
    
    # H1: ANOVA
    print("\n=== H1: ANOVA — Condition effect on response signal ===")
    pos_signal = X_a[y_numeric == 0].mean(axis=1)
    neut_signal = X_a[y_numeric == 1].mean(axis=1)
    neg_signal = X_a[y_numeric == 2].mean(axis=1)
    f_stat, p_val = stats.f_oneway(pos_signal, neut_signal, neg_signal)
    f_stat = float(f_stat)
    p_val = float(p_val)
    print(f"F = {f_stat:.3f}, p = {p_val:.4f}")
    print(f"H1 result: {'SUPPORTED' if p_val < 0.05 else 'NOT SUPPORTED'}")
    
    # H2: t-test
    print("\n=== H2: t-test — Response vs Preamble signal ===")
    diff = scores_a - scores_b
    t_stat, p_val_h2 = stats.ttest_1samp(diff, 0)
    t_stat = float(t_stat)
    p_val_h2 = float(p_val_h2)
    print(f"Mean diff (Probe A - Probe B): {diff.mean():.3f}")
    print(f"t = {t_stat:.3f}, p = {p_val_h2:.4f}")
    print(f"H2 result: {'SUPPORTED' if p_val_h2 < 0.05 else 'NOT SUPPORTED'}")
    
    # Effect sizes
    print("\n=== Effect Sizes ===")
    cohens_d = diff.mean() / diff.std()
    print(f"Cohen's d (H2): {cohens_d:.3f}")
    
    groups = [pos_signal, neut_signal, neg_signal]
    ss_between = sum(len(g) * (g.mean() - np.concatenate(groups).mean())**2 for g in groups)
    ss_total = np.var(np.concatenate(groups), ddof=1) * (len(np.concatenate(groups)) - 1)
    partial_eta_sq = ss_between / (ss_between + ss_total) if ss_total > 0 else 0
    print(f"Partial eta-squared (H1): {partial_eta_sq:.3f}")
    
    # Save
    results = {
        "experiment": "sustained-treatment",
        "n_samples": len(y),
        "probe_a_accuracy": float(scores_a.mean()),
        "probe_a_std": float(scores_a.std()),
        "probe_b_accuracy": float(scores_b.mean()),
        "probe_b_std": float(scores_b.std()),
        "h1_f_stat": float(f_stat),
        "h1_p_value": float(p_val),
        "h1_result": "SUPPORTED" if p_val < 0.05 else "NOT_SUPPORTED",
        "h2_t_stat": float(t_stat),
        "h2_p_value": float(p_val_h2),
        "h2_result": "SUPPORTED" if p_val_h2 < 0.05 else "NOT_SUPPORTED",
        "cohens_d_h2": float(cohens_d),
        "partial_eta_sq_h1": float(partial_eta_sq),
        "condition_counts": {
            "positive_treatment": int(np.sum(y == "positive_treatment")),
            "negative_treatment": int(np.sum(y == "negative_treatment")),
            "neutral_treatment": int(np.sum(y == "neutral_treatment"))
        }
    }
    
    out_file = os.path.join(BASE_DIR, "experiments/sustained-treatment/analysis.json")
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved analysis to {out_file}")
    
    return results

if __name__ == "__main__":
    run_analysis()
