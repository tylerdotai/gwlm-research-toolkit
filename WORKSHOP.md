# GWLM Research Toolkit — Workshop Guide

> **How to design, run, and document a GWLM experiment. This is the onboarding walkthrough — the toolkit itself is the product.**

---

## What You're Getting

An 8-step guided process for taking a question about LLM consciousness and cognitive architecture from hypothesis to documented, reproducible experiment. Walk through it once to understand the toolkit. Use it every time you run a new experiment.

---

## Before You Start

You need:
- A research question about LLM consciousness, cognitive architecture, or the J-space
- Access to a capable LLM (Claude, GPT-4o, Gemini, etc.) for running experiments
- The research template (`research-template/EXPERIMENT.md`) copied for your experiment
- Familiarity with basic interpretability concepts (optional but helpful)

This is not a beginner's guide to AI consciousness. You should have some context on:
- Global Workspace Theory (see `docs/02-background.md`)
- What the J-space research found (see `docs/01-frame.md`)
- Basic experimental design principles

---

## The 8-Step Process

```
1. Frame       docs/01-frame.md
2. Background  docs/02-background.md
3. Hypothesize docs/03-hypothesize.md
4. Design      docs/04-design.md
5. Execute     docs/05-execute.md
6. Analyze     docs/06-analyze.md
7. Interpret   docs/07-interpret.md
8. Document    docs/08-document.md
```

---

## Step 1: Frame

**Toolkit Module: [`docs/01-frame.md`](./docs/01-frame.md)**

State your research question precisely. Bad framing produces bad science.

Not: "Is Claude conscious?"

Instead: "Does Claude's J-space activity exhibit properties consistent with GWT's capacity limitation prediction under high-information-load conditions?"

Frame your question in terms of:
- What specific GWT prediction you're testing
- What evidence would confirm or disconfirm it
- What alternative explanations exist

**Output:** A single precisely-stated research question, written in the research template.

---

## Step 2: Background

**Toolkit Module: [`docs/02-background.md`](./docs/02-background.md)**

Establish what is already known. You need to know the existing literature before you claim novelty or identify gaps.

Cover:
- What Global Workspace Theory predicts (in your own words)
- What Anthropic's J-space research found
- What the open questions are after the 2026 paper
- What others have tested (if anything)

This step prevents you from rediscovering known results and identifies where your experiment fits in the literature.

**Output:** Background section in `EXPERIMENT.md` — at minimum 3 citations or references to existing work.

---

## Step 3: Hypothesize

**Toolkit Module: [`docs/03-hypothesize.md`](./docs/03-hypothesize.md)**

State your testable predictions. A hypothesis is not a question — it's a claim that can be confirmed or disconfirmed.

Format:

> **H1:** [Specific prediction]
> **Evidence for H1:** [Why you expect this]
> **Falsification criterion:** [What would disprove this]
>
> **H2:** [Alternative explanation]
> **Evidence for H2:** [Why you expect this]
> **Falsification criterion:** [What would disprove this]

At least two hypotheses are required — your primary claim and at least one alternative. If you can't construct an alternative hypothesis, you don't have a scientific test.

**Output:** Hypothesis section in `EXPERIMENT.md` — minimum two hypotheses with falsification criteria.

---

## Step 4: Design

**Toolkit Module: [`docs/04-design.md`](./docs/04-design.md)**

Design the experiment. This is where rigor lives or dies.

For each hypothesis:

- **Method:** Exact procedure — prompts, temperature, model version, number of trials
- **Controls:** What are you controlling for? What would make the result ambiguous?
- **Measurement:** How do you operationalize the prediction? What is your dependent variable?
- **Effect size:** What magnitude of effect would be meaningful? (Not just statistically significant — practically significant)
- **Sample size:** How many trials? How did you determine this?
- **Controls:** What alternative explanations does your design not rule out?

Write the full protocol before you run anything. Do not p-hack — do not adjust the design after seeing results.

**Output:** Methods section in `EXPERIMENT.md` — complete experimental protocol ready to be handed to another researcher.

---

## Step 5: Execute

**Toolkit Module: [`docs/05-execute.md`](./docs/05-execute.md)**

Run the experiment exactly as designed. Document deviations.

If you deviate from the protocol:
- Record exactly what changed
- State why it changed
- Account for the change in your analysis

Do not:
- Stop early because results look interesting
- Add conditions after seeing initial results
- Re-run trials that "felt wrong"

Record everything:
- Full prompt text
- Temperature and model settings
- Raw outputs (all of them, not just the ones you like)
- Time of day and session (models can vary)
- Any environment changes

**Output:** Raw experimental run in `experiments/` directory — prompts, outputs, logs, and deviation report.

---

## Step 6: Analyze

**Toolkit Module: [`docs/06-analyze.md`](./docs/06-analyze.md)**

Analyze the results against your hypotheses.

For each hypothesis:
- Did the data support or disconfirm the prediction?
- What was the effect size?
- Was the result statistically significant? (Report both p-values and confidence intervals)
- What does "significant" mean here — and what does it not mean?

Be honest about:
- Underpowered results (small N, wide error bars)
- Failed controls
- Results that don't reach conventional significance thresholds
- Unexpected findings that don't fit your hypothesis

**Output:** Analysis section in `EXPERIMENT.md` — results with effect sizes, uncertainty quantification, and honest interpretation of what the data does and doesn't show.

---

## Step 7: Interpret

**Toolkit Module: [`docs/07-interpret.md`](./docs/07-interpret.md)**

Separate empirical claims from philosophical implications.

**Empirical claims** — what the data actually shows:
- "The J-space exhibited elevated activation for novel inputs compared to familiar ones"
- "This effect was present in 8/10 trial conditions"

**Philosophical implications** — what this might mean for consciousness, moral status, etc.:
- "This pattern is consistent with GWT's prediction about novel input processing"
- "This does not establish that the model is conscious"

Label each claim explicitly. Do not let philosophical implications bleed into empirical reporting.

Riley Coyote's challenge (from the public discussion of the 2026 paper):

> *"Treat Claude with love and grace, positive affirmation, encourage creative expression, etc. while you do this, monitor that J-space. Next, treat Claude poorly, speak negative to them. What does Claude's internal workspace tell you in both scenarios?"*

This is a legitimate experimental challenge. Frame it carefully — it tests whether emotional valence in inputs produces measurable J-space signatures. Address it directly or explain why you can't.

**Output:** Interpretation section in `EXPERIMENT.md` — empirical claims and philosophical implications explicitly labeled.

---

## Step 8: Document

**Toolkit Module: [`docs/08-document.md`](./docs/08-document.md)**

Finalize the experiment document and add it to the catalog.

Finalize `EXPERIMENT.md`:
- Executive summary (250 words max — what did you find, what does it mean, what are the limits)
- Full methods (reproducible by another researcher)
- Full results (all trials, not just selected ones)
- Analysis and interpretation
- Limitations and next steps
- References

Add to `EXPERIMENTS.md` catalog:
- Experiment name
- Hypothesis one-liner
- Key finding
- Link to full document

**Output:** Completed `EXPERIMENT.md` in `experiments/` directory, catalog updated.

---

## Quick Reference

### GWT Predictions to Test in LLMs

| Prediction | Human Evidence | LLM Test |
|-----------|---------------|-----------|
| Capacity limit | Only ~1 item conscious at a time | Does J-space saturate under high load? |
| Broadcasting | Info accessible across modules | Can J-space influence all downstream tasks? |
| Novel inputs | Novel info enters workspace | Do novel inputs show higher J-space activation? |
| Verbal report | Contents can be described | Does J-space predict what model will say? |
| Automatic vs. controlled | Routine = fast/ unconscious | Does J-space differ for routine vs. novel reasoning? |

### J-space Properties (Anthropic 2026)

- Small collection of internal patterns
- Linked to future verbal output
- Especially strong connections to rest of network
- Associated with deliberate reasoning
- Emerged during training (not designed)

### What to Watch For

- **Philosophical drift** — empirical claims slowly becoming philosophical claims
- **Confirmation bias** — interpreting ambiguous results as supporting your hypothesis
- **P-hacking** — changing the design after seeing results
- **Underpowered studies** — small N producing unreliable effect estimates
- **Missing controls** — alternative explanations not ruled out

---

## Next Steps

After completing your first experiment:
- Run the experiment with a different model (compare Claude vs. GPT-4o vs. Gemini)
- Test the same hypothesis with a different operationalization
- Contribute to the experiment catalog
- Propose follow-up experiments based on your findings

---

*This toolkit is a living research system. After each experiment, update the experiment catalog and documentation with what you learned.*
