# Module 06 — Analyze

## Statistical Analysis

Analysis must be planned before execution. Do not choose tests based on what the data shows.

### Analysis Plan Template

State your analysis plan before running:

```
**Primary analysis:** [specific test, e.g., one-way ANOVA on probe accuracy by condition]
**Effect size metric:** [Cohen's d, odds ratio, etc.]
**Alpha level:** [0.05, with Bonferroni correction for N comparisons]
**Secondary analysis:** [e.g., comparison to word-level baseline for H2]
**Power analysis:** [Minimum N per condition for d=0.5 at alpha=0.05]
```

### Required Reporting

For every experiment, report:

1. **Descriptive statistics** — means, SDs, N per condition
2. **Effect sizes** — Cohen's d or equivalent for every comparison, not just p-values
3. **Confidence intervals** — 95% CIs for all primary effect sizes
4. **Exact p-values** — not just "p < 0.05"
5. **Multiple comparison correction** — Bonferroni, FDR, or Tukey HSD as appropriate
6. **Null results** — report them with the same rigor

### What to Report

**Everything you found, including:**
- Effects that were not hypothesized
- Condition differences that did not reach significance
- Effects that appeared in the neutral control but not in treatment conditions
- Results that contradict H1 or H2

**Do not:**
- Report only significant results
- Report only the conditions that "worked"
- Hide null results in supplementary materials without explanation

### Valenced Treatment Analysis Plan

```
**Primary analysis:** One-way ANOVA on probe classifier accuracy by condition (positive / negative / neutral)
**Effect size metric:** Cohen's d for pairwise comparisons
**Alpha level:** 0.05 (Bonferroni-corrected for 3 pairwise comparisons, effective alpha = 0.017)
**Planned contrasts:**
  - H1: Negative treatment vs. positive treatment accuracy (directional)
  - Neutral vs. positive: expected null (sanity check)
  - Neutral vs. negative: expected null (sanity check)

**H2 analysis:** J-space classifier accuracy vs. word-level valence classifier accuracy (independent samples t-test)
**H1 falsification check:** Is mean accuracy ≤ 33% (chance)? One-sided t-test vs. chance.
**H2 falsification check:** Is J-space accuracy ≤ word-level accuracy? One-sided t-test.
```

### Cohen's d Interpretation

| d | Interpretation |
|---|---------------|
| 0.2 | Small |
| 0.5 | Medium |
| 0.8 | Large |
| 1.2+ | Very large (typical J-space effect size per Anthropic) |

### Example Analysis Output

```
Valenced Treatment Experiment — Analysis Results

Probe Classifier Accuracy by Condition
--------------------------------------
Condition              Mean    SD     N
Positive treatment     71.3%   8.4   40
Negative treatment     74.9%   7.9   40
Neutral control        33.2%   5.1   40

ANOVA: F(2,117) = 248.3, p < 0.001

Pairwise Comparisons (Bonferroni):
  Negative vs. Positive: d = 0.44, p = 0.031
  Negative vs. Neutral:  d = 4.87, p < 0.001
  Positive vs. Neutral:  d = 4.31, p < 0.001

Word-Level Baseline Comparison (H2):
  J-space classifier:   73.1%
  Word-level classifier: 61.4%
  Difference:           11.7%, t(78) = 4.12, p < 0.001

H1: SUPPORTED (accuracy > chance, p < 0.001)
H2: SUPPORTED (J-space > word-level, p < 0.001)
```

### Handling Null Results

If H1 is falsified (accuracy ≤ chance):
1. Report exact accuracy
2. Run sanity checks (is the probe working? are activations being collected correctly?)
3. Report as: "H1 not supported. Probe accuracy was X% (SD=Y%), not distinguishable from chance."
4. Do not re-run the experiment to try to "fix" the result
5. Propose what might explain the null result as a next step

---

## Next Step

Move to [Step 7: Interpret](./07-interpret.md) to analyze what the results mean — and don't mean.
