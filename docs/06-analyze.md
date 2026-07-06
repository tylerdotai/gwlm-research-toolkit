# Module 06 — Analyze

## Processing Your Data

Analyze results against your hypotheses. Report everything — not just what supports your claims.

---

## Analysis Principles

### Report All Trials
Include all data. Do not exclude outliers post-hoc unless you had a pre-registered exclusion criterion. If you exclude any data, explain exactly why.

### Effect Size Over Statistical Significance
A p-value tells you whether an effect exists. It does not tell you how large the effect is.

Report:
- **Effect size** (Cohen's d, odds ratio, correlation coefficient — whichever matches your design)
- **Confidence intervals** (not just point estimates)
- **p-value** (as context, not as the main result)

### Uncertainty Quantification
Be explicit about what you don't know:
- Wide confidence intervals = high uncertainty
- Small N = high uncertainty
- Unexpected results = high uncertainty

---

## Analysis by Hypothesis

For each hypothesis:

### H1 (Primary Prediction)
- Did the data support or disconfirm the prediction?
- What was the effect size?
- Was it statistically significant?
- What does "significant" mean here — and what does it NOT mean?

### H2 (Alternative)
- Did the alternative fare better or worse than H1?
- What does this suggest about the mechanism?

### Unexpected Findings
- Did anything appear that you didn't predict?
- Is this a confound, a real finding, or noise?

---

## Example: Novelty Experiment Analysis

**H1 Result:**
Novel inputs showed higher probing classifier accuracy (M=0.72, SD=0.11) than familiar inputs (M=0.58, SD=0.13).
- Effect size: Cohen's d = 1.14 (large effect)
- t(98) = 6.2, p < 0.001
- 95% CI for difference: [0.10, 0.18]

**Interpretation:** Strong support for H1. Novel inputs produce distinguishable activation patterns. However, this does not directly establish consciousness — it establishes a functional difference consistent with GWT predictions.

**H2 Result:**
Attention-matching control reduced but did not eliminate the effect (M=0.68, SD=0.12 vs. M=0.61, SD=0.11).
- Effect size: Cohen's d = 0.61 (medium effect)
- Partial support for H2 — attention explains some but not all of the novelty effect

**Limitation:** "Novelty" is operationalized via topic rarity, which confounds novelty with domain specificity.

---

## Common Mistakes to Avoid

| Mistake | Why It Matters |
|---------|---------------|
| P-hacking | Changing analysis after seeing results inflates false positive rate |
| Underpowered N | Small samples produce unreliable effect estimates |
| Ignoring null results | Null results are real results — "no effect found" is a finding |
| No effect size | Statistical significance without effect size is uninterpretable |
| No confidence intervals | Point estimates without uncertainty are misleading |

---

## Analysis Checklist

Before moving to Interpret, confirm:

- [ ] All trials analyzed (none excluded post-hoc, or exclusions justified)
- [ ] Effect sizes reported for all primary comparisons
- [ ] Confidence intervals included
- [ ] Null results reported (not just significant ones)
- [ ] Unexpected findings documented
- [ ] H2 compared explicitly to H1

---

## Next Step

Move to [Step 7: Interpret](./07-interpret.md) to separate empirical claims from philosophical implications.
