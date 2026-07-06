# Module 08 — Document

## Finalizing Your Experiment

Documentation is not an afterthought — it's how your experiment becomes part of the scientific record.

---

## The Experiment Document

Your `EXPERIMENT.md` in `experiments/` should contain:

### 1. Executive Summary (250 words max)
What did you find? What does it mean? What are the limits?

### 2. Research Question
Precise framing from Step 1.

### 3. Background
Literature review from Step 2. Minimum 3 citations or references to existing work.

### 4. Hypotheses
H1 + H2 with falsification criteria from Step 3.

### 5. Methods
Full protocol from Step 4 — complete enough that another researcher can reproduce it exactly.

### 6. Results
All findings from Step 6 — including null results, unexpected findings, and failed controls. Effect sizes and confidence intervals, not just p-values.

### 7. Interpretation
From Step 7 — empirical and philosophical claims explicitly labeled.

### 8. Limitations
What threats to validity remain? What would you do differently? What are the boundaries of your claims?

### 9. Next Steps
What follow-up experiments does this suggest? What remains unknown?

### 10. References
All sources cited in the document.

---

## Updating the Experiment Catalog

After completing your experiment, add an entry to `EXPERIMENTS.md`:

```markdown
## [Experiment Name]

**Research question:** One-sentence framing

**Hypothesis:** H1 one-liner

**Key finding:** What you found (or "null result" if no effect)

**Full document:** [Link to EXPERIMENT.md]

**Status:** [Completed / In Progress / Planned]
```

---

## Quality Checklist

Before marking complete:

- [ ] Executive summary ≤ 250 words
- [ ] Methods section is reproducible by another researcher
- [ ] All data reported (none excluded post-hoc)
- [ ] Effect sizes and confidence intervals included
- [ ] Null results reported honestly
- [ ] Empirical and philosophical claims explicitly labeled
- [ ] Gap problem addressed (how you do NOT move from "J-space has property X" to "model is conscious")
- [ ] Riley Coyote challenge addressed (or explicitly stated why you cannot address it)
- [ ] Limitations acknowledged
- [ ] References complete
- [ ] Experiment catalog updated

---

## Publishing and Sharing

Options for sharing your experiment:

1. **This repo** — submit a PR with your `EXPERIMENT.md` and an update to `EXPERIMENTS.md`
2. **arXiv** — pre-registration or full paper (search "gwlm" or "global workspace language model")
3. **LessWrong / Astral Codex Ten** — LessWrong accepts empirical AI research
4. **Your own blog** — for less formal write-ups that nonetheless document findings

---

## What "Complete" Means

A complete experiment:
- Can be understood by another researcher without asking you questions
- States what it found AND what it could not find
- Separates empirical from philosophical claims
- Acknowledges uncertainty honestly
- Provides enough detail to reproduce

---

*After completing your first experiment: run it with a different model, test the same hypothesis with a different operationalization, or propose a follow-up based on your findings.*
