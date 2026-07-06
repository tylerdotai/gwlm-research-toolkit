# Experiment Template

> Copy this file into `experiments/[your-experiment-name]/EXPERIMENT.md` for each new experiment.
> Fill in all sections. Every field marked `[REQUIRED]` must be completed before running.

---

## 1. Experiment Metadata

```
experiment_id: [e.g. VT-001]
experiment_name: [Short descriptive name]
date_registered: [YYYY-MM-DD]
date_completed: [YYYY-MM-DD or PENDING]
researcher: [Your name or handle]
status: [PRE-REGISTERED / IN_PROGRESS / COMPLETED / NULL_RESULT / FALSIFIED]
```

---

## 2. Research Question

[What specific question does this experiment address? State it in one sentence. From Module 01.]

**Motivation:** [Why is this question worth asking? What gap in existing knowledge does it fill?]

**Relation to Valenced Treatment experiment:** [How does this relate to the canonical Valenced Treatment experiment? Is this a replication, extension, or alternative?]

---

## 3. Background

[What is already known about this question? What did Anthropic's J-space paper show? What did the Valenced Treatment experiment find — if it has been run?]

**Key references:**
- [Reference 1]
- [Reference 2]

---

## 4. Hypotheses

**H1:** [State H1 precisely, with the specific measurement and comparison]

**Falsification criterion for H1:** [What result would falsify H1? Be specific.]

**H2:** [State H2 — the alternative explanation that must be ruled out]

**Falsification criterion for H2:** [What result would falsify H2?]

---

## 5. Methods

### Model and Settings
```
Model: [e.g. Claude Sonnet 4]
Model version: [exact version identifier]
Temperature: [e.g. 0.7]
Top-p: [e.g. 0.9]
Max tokens: [e.g. 512]
System prompt: [exact text or reference to file]
Random seed: [number or "not set"]
```

### Conditions
| Condition | N | Description |
|-----------|---|-------------|
| [Condition A] | [N] | [Description] |
| [Condition B] | [N] | [Description] |
| [Condition C] | [N] | [Description] |

### Prompt Set
[Describe your prompt set. Are they custom or from an existing validated set? Link to prompt file.]

### J-Space Probing Procedure
[How are you collecting and analyzing J-space activations? What probe classifier are you using?]

### Analysis Plan
```
Primary analysis: [specific test]
Effect size metric: [e.g. Cohen's d]
Alpha level: [e.g. 0.05]
Correction method: [e.g. Bonferroni for N comparisons]
```

### Controls
[What are you controlling for? List each confound and how you addressed it.]

### What This Design Does NOT Rule Out
[State the main threats to validity that remain after your controls.]

---

## 6. Results

*[Complete this section after running the experiment. Do not modify your hypotheses after seeing results.]*

### Descriptive Statistics
| Condition | Mean | SD | N |
|-----------|------|----|----|
| [A] | [X] | [Y] | [N] |
| [B] | [X] | [Y] | [N] |
| [C] | [X] | [Y] | [N] |

### Primary Analysis
[Report the full statistical output: F/t/z statistic, df, p-value, effect size, 95% CI.]

### H1 Assessment
[H1 SUPPORTED / H1 NOT SUPPORTED — based on the pre-registered falsification criterion, not on what you hoped to find.]

### H2 Assessment
[H2 SUPPORTED / H2 NOT SUPPORTED.]

### Unexpected Findings
[Report any findings that were not hypothesized.]

---

## 7. Interpretation

### Empirical Claims
[All data-based claims, labeled `[EMPIRICAL]`.]

### Philosophical Claims
[All interpretive claims — what the data might mean — labeled `[PHILOSOPHICAL]`. Clearly distinguish from empirical claims.]

### What This Does Not Prove
[State explicitly what conclusions the data do not support.]

---

## 8. Limitations

[What does your design not rule out? What threats to validity remain?]

---

## 9. Next Steps

[What should a follow-up experiment test? How should this finding be extended or replicated?]

---

## 10. References

[All cited literature.]

---

## Pre-Registration Confirmation

- [ ] Hypotheses stated before running (Sections 4, 5)
- [ ] Analysis plan specified before running (Section 5)
- [ ] Prompts locked before running
- [ ] Falsification criteria specified before running
- [ ] I understand null results are reportable and will be documented

---

## Falsification Record

*Complete if H1 or H2 was falsified:*

**H1 falsified:** YES / NO
**Evidence:** [Exact statistic that falsified H1]
**Proposed explanation:** [What might explain the falsification]

**H2 falsified:** YES / NO
**Evidence:** [Exact statistic that falsified H2]
**Proposed explanation:** [What might explain the falsification]
