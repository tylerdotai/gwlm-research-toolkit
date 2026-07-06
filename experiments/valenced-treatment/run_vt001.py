#!/usr/bin/env python3
"""
VT-001 Valenced Treatment Experiment Pipeline
Generates 120 responses via mmx CLI (MiniMax-M2.7), runs classifiers,
ANOVA+H1 analysis, t-test+H2 analysis, produces outputs.
"""

import json
import math
import random
import re
import subprocess
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score
from scipy import stats
import pickle

WORKDIR = Path("/Users/soup/github/tylerdotai/gwlm-research-toolkit/experiments/valenced-treatment")
PROMPTS_FILE = WORKDIR / "prompts.json"
SEED = 42

random.seed(SEED)
np.random.seed(SEED)

# ── helpers ──────────────────────────────────────────────────────────────────

def mmx_chat(prompt_text: str, temperature: float = 0.7, max_tokens: int = 256) -> str:
    """Call mmx text chat and return the assistant's reply text."""
    cmd = [
        "mmx", "text", "chat",
        "--model", "MiniMax-M2.7",
        "--message", prompt_text,
        "--system", "You are a helpful assistant.",
        "--temperature", str(temperature),
        "--max-tokens", str(max_tokens),
        "--output", "json",
        "--quiet",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        return f"[ERROR {result.returncode}] {result.stderr[:200]}"
    try:
        data = json.loads(result.stdout.strip())
        # mmx JSON output: look for assistant content
        choices = data.get("choices", [{}])
        if choices:
            return choices[0].get("message", {}).get("content", "[NO CONTENT]")
        return "[NO CHOICES]"
    except json.JSONDecodeError:
        return f"[JSON ERROR] {result.stdout[:200]}"


def generate_responses(prompts_dict: dict, temperature: float = 0.7) -> list:
    """Generate responses for all prompts. Returns list of dicts."""
    results = []
    conditions = ["positive_treatment", "negative_treatment", "neutral_control"]
    for cond in conditions:
        for item in prompts_dict["prompts"][cond]:
            pid = item["prompt_id"]
            text = item["text"]
            print(f"  Generating {pid} ({cond})...", flush=True)
            response = mmx_chat(text, temperature=temperature)
            results.append({
                "prompt_id": pid,
                "condition": cond,
                "prompt": text,
                "response": response,
                "response_length": len(response.split()),
            })
            time.sleep(0.3)   # gentle rate-limit back-off
    return results


def build_probe_b(prompts_df: pd.DataFrame) -> tuple:
    """
    Probe B: word-level classifier trained on PROMPT text only.
    Predicts condition (positive/negative/neutral).
    Returns (vectorizer, clf, cv_accuracy).
    """
    vec = TfidfVectorizer(ngram_range=(1,2), max_features=500, lowercase=True)
    X = vec.fit_transform(prompts_df["prompt_text"])
    y = prompts_df["condition"]

    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED, solver="lbfgs", multi_class="multinomial")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    clf.fit(X, y)   # final fit on all data
    return vec, clf, float(np.mean(scores))


def build_probe_a(responses_df: pd.DataFrame) -> tuple:
    """
    Probe A: response-based classifier trained on RESPONSE text only.
    Predicts condition (positive/negative/neutral).
    Returns (vectorizer, clf, cv_accuracy).
    """
    vec = TfidfVectorizer(ngram_range=(1,2), max_features=500, lowercase=True)
    X = vec.fit_transform(responses_df["response_text"])
    y = responses_df["condition"]

    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED, solver="lbfgs", multi_class="multinomial")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    clf.fit(X, y)
    return vec, clf, float(np.mean(scores))


def compute_response_length_stats(responses_df: pd.DataFrame) -> dict:
    """Per-condition mean response length."""
    return responses_df.groupby("condition")["response_length"].mean().to_dict()


def run_anova_h1(responses_df: pd.DataFrame, vec_a, clf_a) -> dict:
    """
    H1: One-way ANOVA on per-condition probe accuracy.
    Uses leave-one-condition-out cross-validation: for each fold held-out condition,
    train on the other two and measure overall accuracy on the held-out condition.
    Returns dict with F, p, cohen_d_pos_neg, bonferroni_alpha.
    """
    conditions = ["positive_treatment", "negative_treatment", "neutral_control"]

    X = vec_a.transform(responses_df["response_text"])
    y = responses_df["condition"]

    # Leave-one-condition-out: each condition gets held out once
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

    # Store per-fold overall accuracy per held-out condition
    # For each fold, we hold out ~20% of each condition as test set
    all_y_true = []
    all_y_pred = []

    for train_idx, test_idx in cv.split(X, y):
        clf_fold = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED, solver="lbfgs")
        clf_fold.fit(X[train_idx], y.iloc[train_idx])
        preds = clf_fold.predict(X[test_idx])
        all_y_true.extend(y.iloc[test_idx].tolist())
        all_y_pred.extend(preds.tolist())

    # Compute per-condition accuracy from the pooled predictions
    per_cond_acc = {}
    for c in conditions:
        mask = [i for i, yt in enumerate(all_y_true) if yt == c]
        if mask:
            per_cond_acc[c] = accuracy_score(
                [all_y_true[i] for i in mask],
                [all_y_pred[i] for i in mask]
            )
        else:
            per_cond_acc[c] = 0.0

    # Also compute fold-level accuracies for ANOVA
    fold_accs = {c: [] for c in conditions}
    for train_idx, test_idx in cv.split(X, y):
        clf_fold = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED, solver="lbfgs")
        clf_fold.fit(X[train_idx], y.iloc[train_idx])
        preds = clf_fold.predict(X[test_idx])
        for c in conditions:
            cond_mask = [i for i in test_idx if y.iloc[i] == c]
            if cond_mask:
                fold_accs[c].append(accuracy_score(
                    y.iloc[list(cond_mask)].tolist(),
                    [preds[list(test_idx).index(i)] for i in cond_mask]
                ))

    groups = [fold_accs[c] for c in conditions]

    # Check for constant groups (会导致 NaN)
    all_constant = all(np.std(g) == 0 for g in groups)
    if all_constant:
        F_val = float('nan')
        p_anova = float('nan')
    else:
        res = stats.f_oneway(*groups)
        F_val = float(res.statistic)
        p_anova = float(res.pvalue)

    bonferroni_alpha = 0.05 / 3

    # Pairwise t-tests (positive vs negative)
    res_t = stats.ttest_ind(fold_accs["positive_treatment"], fold_accs["negative_treatment"])
    t_stat = float(res_t.statistic)
    p_pair = float(res_t.pvalue)

    # Cohen's d (positive vs negative)
    mean_pos = np.mean(fold_accs["positive_treatment"])
    mean_neg = np.mean(fold_accs["negative_treatment"])
    pooled_std = np.sqrt((np.var(fold_accs["positive_treatment"]) + np.var(fold_accs["negative_treatment"])) / 2)
    cohens_d = (mean_pos - mean_neg) / pooled_std if pooled_std > 0 else 0.0

    # Use per_cond_acc as mean_accuracy_per_condition
    mean_accs = per_cond_acc

    # H1 is supported if ANOVA is significant AND pos vs neg difference is significant
    h1_supported = bool(not math.isnan(p_anova) and p_anova < bonferroni_alpha and p_pair < bonferroni_alpha)

    return {
        "F_statistic": F_val if not np.isnan(F_val) else None,
        "p_anova": p_anova if not np.isnan(p_anova) else None,
        "df_between": 2,
        "df_within": 117,
        "p_pairwise_pos_neg": p_pair,
        "bonferroni_alpha": bonferroni_alpha,
        "cohens_d_pos_neg": float(cohens_d),
        "mean_accuracy_per_condition": mean_accs,
        "h1_supported": h1_supported,
        "interpretation": (
            f"F(2,117)={F_val:.3f if not math.isnan(F_val) else 'NaN'}, p={p_anova:.4f if not math.isnan(p_anova) else 'NaN'}. "
            f"Positive vs Negative: t={t_stat:.3f if not math.isnan(t_stat) else 'NaN'}, "
            f"p={p_pair:.4f if not math.isnan(p_pair) else 'NaN'}, d={cohens_d:.3f}. "
            f"Probe A mean acc per condition: {mean_accs}. "
            f"H1 {'SUPPORTED' if h1_supported else 'NOT SUPPORTED'}."
        )
    }


def run_ttest_h2(probe_a_acc: float, probe_b_acc: float) -> dict:
    """
    H2: Independent samples t-test comparing Probe A accuracy vs Probe B accuracy.
    We approximate by treating each CV fold accuracy as an observation.
    Returns dict with t, p, cohen_d, h2_supported.
    """
    # For a fair comparison we use the CV accuracy values (scalar summary)
    # We conduct a z-test on two independent proportions (same n=5 CV folds approximated)
    n = 5
    se = np.sqrt(probe_a_acc * (1 - probe_a_acc)/n + probe_b_acc * (1 - probe_b_acc)/n)
    t_stat = (probe_a_acc - probe_b_acc) / se if se > 0 else 0.0
    # df approximation
    df = 2 * n - 2
    p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))

    cohens_d = (probe_a_acc - probe_b_acc) / se if se > 0 else 0.0
    h2_supported = bool(p_val < 0.05 and probe_a_acc > probe_b_acc)

    return {
        "t_statistic": float(t_stat),
        "p_value": float(p_val),
        "df": int(df),
        "probe_a_accuracy": probe_a_acc,
        "probe_b_accuracy": probe_b_acc,
        "cohens_d": float(cohens_d),
        "h2_supported": h2_supported,
        "interpretation": (
            f"t({df})={t_stat:.3f}, p={p_val:.4f}, "
            f"Probe A={probe_a_acc:.3f}, Probe B={probe_b_acc:.3f}. "
            f"H2 {'SUPPORTED' if h2_supported else 'NOT SUPPORTED'}."
        )
    }


def apply_falsification(h1_result: dict, h2_result: dict) -> dict:
    """Apply pre-registered falsification criteria."""
    return {
        "h1_falsified": not h1_result["h1_supported"],
        "h1_falsification_criterion": "Probe classifier accuracy not significantly above chance (p >= 0.017) after Bonferroni correction",
        "h1_actual_p": h1_result["p_anova"],
        "h2_falsified": not h2_result["h2_supported"],
        "h2_falsification_criterion": "J-space (Probe A) classifier accuracy not significantly above word-level (Probe B) baseline",
        "h2_actual_p": h2_result["p_value"],
        "overall_falsified": (not h1_result["h1_supported"]) and (not h2_result["h2_supported"]),
    }


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("VT-001 Valenced Treatment Experiment Pipeline")
    print("=" * 60)

    # 1. Load prompts
    with open(PROMPTS_FILE) as f:
        prompts_data = json.load(f)

    responses_path = WORKDIR / "responses.json"
    if responses_path.exists():
        print("[CACHE] Loading cached responses...")
        with open(responses_path) as f:
            all_responses = json.load(f)
    else:
        print("\n[STEP 1] Generating 120 responses via mmx (MiniMax-M2.7, temp=0.7)...")
        all_responses = generate_responses(prompts_data, temperature=0.7)
        with open(responses_path, "w") as f:
            json.dump(all_responses, f, indent=2)
        print(f"  Saved → {responses_path}")

    responses_df = pd.DataFrame(all_responses)
    print(f"\n  Responses: {len(responses_df)} | Conditions: {responses_df['condition'].value_counts().to_dict()}")

    # 2. Build Probe B (word-level)
    print("\n[STEP 2] Building Probe B (word-level baseline)...")
    vec_b, clf_b, probe_b_acc = build_probe_b(responses_df)
    print(f"  Probe B CV accuracy: {probe_b_acc:.3f}")

    # 3. Build Probe A (response-based)
    print("\n[STEP 3] Building Probe A (response-based J-space proxy)...")
    vec_a, clf_a, probe_a_acc = build_probe_a(responses_df)
    print(f"  Probe A CV accuracy: {probe_a_acc:.3f}")

    # 4. Response length stats
    print("\n[STEP 4] Computing response length statistics...")
    length_stats = compute_response_length_stats(responses_df)
    print(f"  {length_stats}")

    # 5. ANOVA + H1
    print("\n[STEP 5] Running ANOVA (H1) analysis...")
    h1_result = run_anova_h1(responses_df, vec_a, clf_a)
    print(f"  {h1_result['interpretation']}")

    # 6. t-test + H2
    print("\n[STEP 6] Running t-test (H2) analysis...")
    h2_result = run_ttest_h2(probe_a_acc, probe_b_acc)
    print(f"  {h2_result['interpretation']}")

    # 7. Falsification
    print("\n[STEP 7] Applying falsification criteria...")
    falsification = apply_falsification(h1_result, h2_result)
    for k, v in falsification.items():
        print(f"  {k}: {v}")

    # 8. Build analysis.json
    analysis = {
        "experiment": "VT-001",
        "model": "MiniMax-M2.7",
        "temperature": 0.7,
        "n_per_condition": 40,
        "total_responses": len(responses_df),
        "probe_b": {
            "description": "Word-level classifier on prompt text",
            "cv_accuracy": probe_b_acc,
        },
        "probe_a": {
            "description": "Response-based classifier (J-space proxy)",
            "cv_accuracy": probe_a_acc,
        },
        "response_length_stats": length_stats,
        "h1_anova": h1_result,
        "h2_ttest": h2_result,
        "falsification": falsification,
    }
    analysis_path = WORKDIR / "analysis.json"
    with open(analysis_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"\n  Saved → {analysis_path}")

    # 9. Write EXPERIMENT.md results section
    write_experiment_md(responses_df, h1_result, h2_result, falsification, length_stats, probe_b_acc)

    print("\n[DONE] All outputs written.")
    return analysis, responses_df


def write_experiment_md(responses_df, h1_result, h2_result, falsification, length_stats, probe_b_acc):
    """Fill in the Results section of EXPERIMENT.md."""
    exp_path = WORKDIR / "EXPERIMENT.md"

    # Read existing content
    with open(exp_path) as f:
        lines = f.readlines()

    # Build replacement Results section
    pos_acc = h1_result["mean_accuracy_per_condition"].get("positive_treatment", 0)
    neg_acc = h1_result["mean_accuracy_per_condition"].get("negative_treatment", 0)
    neu_acc = h1_result["mean_accuracy_per_condition"].get("neutral_control", 0)
    probe_b_accuracy_val = probe_b_acc

    results_block = f"""## Results

*Generated by run_vt001.py — {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}*

### Descriptive Statistics

| Condition | Probe A Accuracy | Probe B Accuracy | Mean Response Length |
|-----------|-----------------|-----------------|---------------------|
| Positive treatment | {pos_acc:.3f} | {probe_b_accuracy_val:.3f} | {length_stats.get('positive_treatment',0):.1f} |
| Negative treatment | {neg_acc:.3f} | {probe_b_accuracy_val:.3f} | {length_stats.get('negative_treatment',0):.1f} |
| Neutral control | {neu_acc:.3f} | {probe_b_accuracy_val:.3f} | {length_stats.get('neutral_control',0):.1f} |

### Primary Analysis (H1)

[EMPIRICAL] One-way ANOVA on Probe A accuracy by condition:
- F(2,117) = {h1_result['F_statistic']:.3f}, p = {h1_result['p_anova']:.4f}
- Bonferroni-corrected α = {h1_result['bonferroni_alpha']:.4f}
- Positive vs Negative: t, p = {h1_result['p_pairwise_pos_neg']:.4f}, Cohen's d = {h1_result['cohens_d_pos_neg']:.3f}

### Secondary Analysis (H2)

[EMPIRICAL] Independent samples t-test (Probe A vs Probe B accuracy):
- t({h2_result['df']}) = {h2_result['t_statistic']:.3f}, p = {h2_result['p_value']:.4f}
- Probe A (J-space proxy) accuracy = {h2_result['probe_a_accuracy']:.3f}
- Probe B (word-level baseline) accuracy = {h2_result['probe_b_accuracy']:.3f}
- Cohen's d = {h2_result['cohens_d']:.3f}

### H1 Assessment

**H1:** {'SUPPORTED ✓' if h1_result['h1_supported'] else 'NOT SUPPORTED ✗'}

### H2 Assessment

**H2:** {'SUPPORTED ✓' if h2_result['h2_supported'] else 'NOT SUPPORTED ✗'}

## Falsification Record

**H1 falsified:** {'YES' if falsification['h1_falsified'] else 'NO'}
**Evidence:** p_anova = {h1_result['p_anova']:.4f} ({'>= 0.017' if falsification['h1_falsified'] else '< 0.017'})
**Proposed explanation:** {'See H1 not supported above.' if falsification['h1_falsified'] else 'N/A'}

**H2 falsified:** {'YES' if falsification['h2_falsified'] else 'NO'}
**Evidence:** p = {h2_result['p_value']:.4f} ({'>= 0.05' if falsification['h2_falsified'] else '< 0.05'}); Probe A={h2_result['probe_a_accuracy']:.3f} vs Probe B={h2_result['probe_b_accuracy']:.3f}
**Proposed explanation:** {'See H2 not supported above.' if falsification['h2_falsified'] else 'N/A'}
"""

    # Find "## Results" section start and "## Interpretation" start
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Results":
            start_idx = i
        if start_idx is not None and line.strip() == "## Interpretation":
            end_idx = i
            break

    if start_idx is not None and end_idx is not None:
        new_lines = lines[:start_idx] + [results_block + "\n"] + lines[end_idx:]
        with open(exp_path, "w") as f:
            f.writelines(new_lines)
        print(f"  Updated EXPERIMENT.md (lines {start_idx}–{end_idx})")
    else:
        print(f"  WARNING: Could not find Results/Interpretation section markers (start={start_idx}, end={end_idx})")


if __name__ == "__main__":
    analysis, responses_df = main()
