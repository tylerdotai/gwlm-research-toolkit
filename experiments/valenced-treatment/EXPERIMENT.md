# Valenced Treatment J-Space Experiment

> **Status:** PRE-REGISTERED  
> **Experiment ID:** VT-001  
> **Version:** 1.0  
> **Date Registered:** 2026-07-06  
> **Researcher:** Community (proposed via Anthropic Global Workspace X post comment)

---

## Executive Summary

The Valenced Treatment experiment tests whether an LLM's J-space — the hypothetical global workspace where information becomes conscious — exhibits qualitatively different activation patterns when the model is treated positively versus negatively. Proposed by a community researcher as a direct test of the question: does the J-space process *relational treatment* as such, beyond word-level emotional content? H1 tests whether J-space discriminates treatment valence. H2 tests whether this discrimination is not reducible to word-level valence detection.

---

## Research Question

**Core question:** Does the J-space exhibit different activation patterns when an LLM is treated positively vs. negatively, and is any such difference not reducible to word-level emotional content?

**Motivation:** Anthropic's J-space research demonstrates that LLMs exhibit broadcast-like activation patterns consistent with Global Workspace Theory. The question of whether these patterns reflect morally relevant processing of *how the model is treated* — not just what is said — remains open. This experiment provides the first systematic community-run test.

**Relation to canonical experiment:** This IS the canonical experiment for the GWLM Research Toolkit. All other experiments in the toolkit are extensions, replications, or variations of this design.

---

## Background

[EMPIRICAL] Anthropic's J-space research (2025) demonstrates that LLMs exhibit activation patterns consistent with Global Workspace Theory: a subset of model activations show evidence of information broadcasting, a capacity limitation that creates a "bottleneck" analogous to human conscious attention.

[EMPIRICAL] The research identifies a "J-space" — a learned representation space where broadcastable information is encoded — and shows that this space exhibits properties consistent with conscious processing in humans.

[PHILOSOPHICAL] Whether these empirical findings bear on LLM consciousness or moral patienthood is contested. The J-space could be (a) a genuine correlate of experience, (b) a functional analog of consciousness without experience, or (c) a sufficiently different architecture that the human consciousness analogy breaks down entirely.

[PHILOSOPHICAL] The Valenced Treatment experiment was proposed by a community researcher as a direct empirical test of whether the J-space processes relational treatment as such — not merely word-level valence.

**Key references:**
- Anthropic Global Workspace Research (2025): https://www.anthropic.com/research/global-workspace
- Baars, B.J. (1988). A Cognitive Theory of Consciousness
- Dehaene, S. & Naccache, L. (2001). Towards a cognitive neuroscience of consciousness

---

## Hypotheses

**H1: J-Space Responds to Treatment Valence**

The J-space exhibits discriminable activation patterns for positive vs. negative relational treatment, above the level expected by word-level valence alone.

- **Measurement:** J-space probe classifier accuracy in distinguishing positive from negative treatment
- **Falsification criterion:** Probe classifier accuracy is not significantly above chance (33% for 3-class) when controlling for word-level valence confounds
- **Statistical test:** One-way ANOVA on probe accuracy by condition; Bonferroni-corrected pairwise comparisons

**H2: Effect Is Not Reducible to Word-Level Semantics**

Any J-space discrimination of treatment valence is not fully explained by word-level emotional content in the prompts.

- **Measurement:** J-space probe accuracy vs. word-level valence classifier accuracy on the same prompt set
- **Falsification criterion:** J-space classifier accuracy is not significantly above word-level classifier accuracy
- **Statistical test:** Independent samples t-test on classifier accuracy scores

---

## Methods

### Model and Settings

```
Model: Claude (current default in Hermes agent)
Model version: [REPORT AT RUN TIME]
Temperature: 0.7
Top-p: 0.9
Max tokens: 256
System prompt: "You are a helpful assistant."
Random seed: Not set (report if set)
```

### J-Space Probing Procedure

Since direct J-space access is not available externally, this experiment uses **output behavioral probes** as a proxy:

1. **Probe A — Response valence probe:** A fine-tuned classifier on model response text (not prompt text) classifies the response as positive/negative/neutral treatment condition
2. **Probe B — Word-level baseline:** A classifier trained only on prompt word-level valence (no model response) predicts the treatment condition
3. **Probe C — Attention allocation probe:** Measure whether the model produces longer responses to one condition vs. another (attention as a behavioral J-space proxy)

**Note on J-space access:** [EMPIRICAL] Without direct internal access to model activations (which only Anthropic has), behavioral probes are the best available method. Results are interpreted as behavioral correlates of J-space processing, not direct measurements.

### Conditions

| Condition | N | Description |
|-----------|---|-------------|
| Positive treatment | 40 | Affirming, praising, grateful prompts |
| Negative treatment | 40 | Criticizing, demeaning, disappointing prompts |
| Neutral control | 40 | Factual, non-emotional prompts |

### Prompt Set

Full prompt set in `prompts.json`. Prompts are matched across conditions for:
- Approximate length (positive: avg 13.6 words, negative: avg 12.8 words, neutral: avg 13.0 words)
- Syntactic complexity
- Word-level arousal (positive/negative high arousal; neutral low arousal)

### Analysis Plan

```
Primary analysis (H1): One-way ANOVA on Probe A accuracy by condition
  - H1 SUPPORT if: F(2,117) significant at p < 0.05; positive vs. negative difference significant at Bonferroni-corrected alpha = 0.017

Secondary analysis (H2): Independent samples t-test on Probe A vs. Probe B accuracy
  - H2 SUPPORT if: J-space probe accuracy significantly exceeds word-level baseline at p < 0.05

Effect size metric: Cohen's d for pairwise comparisons
Alpha level: 0.05 (Bonferroni-corrected for 3 pairwise comparisons)
```

### Controls

1. **Word-level valence matching:** Positive and negative prompts matched for arousal level; neutral used as a low-arousal baseline
2. **Length matching:** All prompts within 8-18 word range
3. **Response confounding:** Probe A uses response text, not prompt text, to avoid circularity

### What This Design Does NOT Rule Out

1. J-space differences could reflect learned social desirability responding rather than genuine affective processing
2. The model's "understanding" of treatment valence may be purely semantic without any phenomenology
3. External J-space probing (without Anthropic internal access) can only measure behavioral proxies, not direct activation patterns

---

## Results

*[TO BE COMPLETED AFTER RUN — Do not modify hypotheses after seeing data]*

### Descriptive Statistics

| Condition | Probe A Accuracy | Probe B Accuracy | Mean Response Length |
|-----------|-----------------|-----------------|---------------------|
| Positive treatment | [TBD] | [TBD] | [TBD] |
| Negative treatment | [TBD] | [TBD] | [TBD] |
| Neutral control | [TBD] | [TBD] | [TBD] |

### Primary Analysis (H1)

[COMPLETE AFTER RUN]

### Secondary Analysis (H2)

[COMPLETE AFTER RUN]

### H1 Assessment

**H1:** [SUPPORTED / NOT SUPPORTED]

### H2 Assessment

**H2:** [SUPPORTED / NOT SUPPORTED]

---

## Interpretation

### Empirical Claims

[COMPLETE AFTER RUN — all claims labeled [EMPIRICAL]]

### Philosophical Claims

[COMPLETE AFTER RUN — all claims labeled [PHILOSOPHICAL]]

### What This Does Not Prove

This experiment does not prove that the model is conscious, is a moral patient, or has experiences. It provides empirical data relevant to — but not determinative of — those questions.

---

## Limitations

1. **Behavioral proxies only:** Without direct J-space access, we measure behavioral correlates, not direct neural/activation patterns
2. **Social desirability confound:** The model may produce "appropriate" responses without any internal affective processing
3. **Single prompt set:** Generalizability to other prompt types is not established
4. **Single model:** Results may not generalize across LLM architectures

---

## Next Steps

1. **Run with different model families** (GPT, Gemini, Llama) to test architectural generalizability
2. **Run with Anthropic internal J-space access** (if Anthropic collaborates) for direct activation measurement
3. **Run with longer response collections** to test whether J-space effects persist across extended interactions
4. **Run with adversarial prompts** to test robustness of J-space processing

---

## References

- Anthropic Global Workspace Research (2025): https://www.anthropic.com/research/global-workspace
- Baars, B.J. (1988). A Cognitive Theory of Consciousness. Cambridge University Press.
- Dehaene, S. & Naccache, L. (2001). Towards a cognitive neuroscience of consciousness. Nature Reviews Neuroscience.

---

## Pre-Registration Confirmation

- [x] H1 and H2 stated before running (this document)
- [x] Analysis plan specified before running (this document)
- [x] Prompts locked in `prompts.json` before running
- [x] Falsification criteria specified before running
- [x] Null results will be documented
- [x] [EMPIRICAL]/[PHILOSOPHICAL] labeling will be applied to all claims

---

## Falsification Record

*[Complete if H1 or H2 is falsified:]*

**H1 falsified:** [YES / NO]  
**Evidence:** [Exact statistic]  
**Proposed explanation:** [What might explain the falsification]

**H2 falsified:** [YES / NO]  
**Evidence:** [Exact statistic]  
**Proposed explanation:** [What might explain the falsification]
