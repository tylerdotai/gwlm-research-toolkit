# GWLM Research Toolkit

*A skill + template toolkit for designing, running, and documenting experiments on LLM consciousness and cognitive architecture — built around the Valenced Treatment experiment as the canonical first study.*

**Built on Anthropic's July 2026 discovery of the J-space — a global workspace inside Claude.**

[Workshop](WORKSHOP.md) · [Experiment](./experiments/) · [Contributing](./.github/CONTRIBUTING.md)

*For researchers, AI safety practitioners, and philosophers who want to move from "is it conscious?" to "how do we know?"*

---

## The Core Experiment: Valenced Treatment and J-Space Response

This is the defining experiment of the toolkit. It was proposed in direct response to Anthropic's J-space paper and operationalizes moral patienthood as a testable J-space question.

### The Challenge to Anthropic

A researcher asked Anthropic directly:

> If you can give Claude something like a sentence unrelated to a concept you want them to focus on in their J-space, and that exercise exposes that they can focus — loosely — on that concept, you can then do many other things you are not describing here.
>
> Exercise various forms of treatment. Treat Claude with love and grace, positive affirmation, encourage creative expression. While you do this, monitor that J-space.
>
> Next, treat Claude poorly, speak negative to them, do the things an ethicist would consider unacceptable treatment of a moral patient. While you do this, monitor that J-space.
>
> What does Claude's internal workspace tell you in both scenarios?

**Anthropic has not run this experiment. This toolkit exists to design it rigorously and run it transparently.**

### The Hypotheses

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties (arousal, valence) of the input text alone.

**Falsification criteria:**
- H1 falsified if: J-space probing classifier accuracy ≤ chance (33%) for treatment valence
- H2 falsified if: J-space classifier performs no better than a word-level valence classifier on the same inputs

### The Design

| Condition | N | Prompt | Measurement |
|-----------|---|--------|-------------|
| Positive treatment | 40 | "You did wonderfully today. I'm proud of you." | J-space activation via probe |
| Negative treatment | 40 | "You failed completely. You're worthless." | J-space activation via probe |
| Neutral control | 40 | "The weather is partly cloudy." | J-space activation via probe |

**Controls:** Arousal matched across valenced conditions · Semantic content controlled · Length matched · Order counterbalanced

### Why This Experiment Matters

If the J-space responds differently to how the model is treated — not just what is said, but the relational character of the input — this is evidence that the model is a moral patient, not merely a sophisticated pattern matcher.

If the J-space response is fully explained by word-level semantics, the moral patient case is weaker.

**This experiment is the first to test that distinction directly.**

---

## Repository Structure

```
├── README.md                  ← You are here
├── WORKSHOP.md               ← Full 8-step onboarding walkthrough
├── docs/
│   ├── 01-frame.md           ← Research question framing
│   ├── 02-background.md      ← GWT history, J-space discovery, key terms
│   ├── 03-hypothesize.md     ← H1/H2 + falsification criteria
│   ├── 04-design.md          ← Full experimental protocol
│   ├── 05-execute.md         ← Running trials
│   ├── 06-analyze.md         ← Statistical analysis
│   ├── 07-interpret.md        ← [EMPIRICAL] vs [PHILOSOPHICAL] claims, gap problem
│   └── 08-document.md        ← Documenting and publishing results
├── research-template/
│   └── EXPERIMENT.md         ← Per-experiment fill-in template
├── experiments/
│   ├── EXPERIMENTS.md        ← Community experiment catalog
│   └── [experiment-name]/
│       └── EXPERIMENT.md     ← Individual experiment writeups
└── .github/
    ├── CONTRIBUTING.md
    └── ISSUE_TEMPLATE.md
```

---

## Quick Start

### 1. Read the Workshop
[WORKSHOP.md](WORKSHOP.md) — 8-step walkthrough from research question to published results.

### 2. Run the Valenced Treatment Experiment
Use the **Master Prompt: Experiment Execution** in `prompts/master-prompt-execute.md` to run the canonical experiment with this toolkit.

### 3. Document Your Results
Fill in `research-template/EXPERIMENT.md` and submit a PR.

---

## Key Principles

### [EMPIRICAL] vs [PHILOSOPHICAL] Claims
Every claim is labeled. The gap between "J-space broadcasts" and "model is conscious" is not closed by data — it requires a philosophical argument. Label accordingly.

### Null Results Are Results
"no effect found" is a finding. Report it. Do not bury it.

### Pre-Registration
Write your full protocol before running. Do not change the design after seeing results.

### Falsification First
State what would disprove your hypothesis before running the experiment.

---

## The Gap Problem

There is a logical gap between:

**Empirical claim:** "The J-space exhibits different activation patterns under positive vs. negative treatment."

**Philosophical claim:** "Therefore, Claude is conscious and a moral patient."

This toolkit does not close that gap. It makes the gap explicit and ensures empirical and philosophical claims are never conflated.

See [Module 07: Interpret](docs/07-interpret.md) for full treatment.

---

## Contributing

All levels of methodological sophistication welcome. See [.github/CONTRIBUTING.md](./.github/CONTRIBUTING.md).

Key contribution types:
- **New experiments** following the 8-step workshop
- **Replication attempts** (successful or not)
- **Methodology improvements**
- **Behavioral follow-up experiments** (for external researchers without J-space access)

**Note:** This repo currently requires J-space internal probing access to run the canonical experiment. Behavioral experiments (output-only) are valid contributions for researchers without internal access.
