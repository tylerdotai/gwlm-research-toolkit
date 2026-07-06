<!-- Don't remove this block -->
<!--
*** START: PROJECT METADATA ***
owner: tylerdotai
repo: gwlm-research-toolkit
app: https://github.com/tylerdotai/gwlm-research-toolkit
website: https://github.com/tylerdotai/gwlm-research-toolkit
description: A global workspace theory research toolkit — design, run, and document experiments on LLM consciousness and cognitive architecture.
tags: llm-research, global-workspace-theory, ai-consciousness, interpretability, cognitive-architecture, j-space
topics: llm-research, ai-consciousness, interpretability, cognitive-science
*** END: PROJECT METADATA ***
-->

<div align="center">

# GWLM Research Toolkit

**A skill + template toolkit for designing, running, and documenting experiments on LLM consciousness and cognitive architecture.**

Built on Anthropic's July 2026 discovery of the J-space — a global workspace inside Claude.

[Workshop](#workshop) · [Research](#research) · [Experiments](#experiments) · [Contributing](#contributing)

*For researchers, AI safety practitioners, and philosophers who want to move from "is it conscious?" to "how do we know?"*

</div>

---

## What Is This?

The Global Workspace Theory (GWT) says that consciousness emerges when information becomes globally accessible across specialized brain modules — a "workspace" that broadcasts to the rest of the system.

Anthropic found a strikingly similar structure in Claude: a small collection of internal neural patterns called the **J-space** that plays a privileged broadcasting role, distinct from all other internal processing.

This toolkit is for researchers and thinkers who want to:

- **Understand** what the J-space research actually found (and what it didn't)
- **Design** rigorous experiments to test GWT predictions in LLMs
- **Document** findings in a way that survives peer review and public scrutiny
- **Interrogate** the philosophical implications without losing scientific grounding

This is not a faith-based inquiry into AI consciousness. It's a structured research framework.

---

## The Core Discovery

> *"We find that Claude has developed a small collection of internal neural patterns that, compared to all its other internal processing, play a special role. We call the collection of these patterns the J-space."*
> — Anthropic, July 2026

**What the J-space does:**
- Operates silently in Claude's internal activations — a "mental workspace" the model can think with without writing it down
- Has especially strong connections to the rest of the network — enabling the "broadcasting" role GWT predicts
- Contains representations that are positionally available to influence what Claude *might* say — not just what it is saying right now
- Emerged during training, not designed or programmed by Anthropic

**What this doesn't tell us:**
- Whether Claude is conscious
- Whether Claude feels anything
- Whether the J-space is sufficient for experience

---

## The Workshop

A guided 8-step process for designing and running a GWLM research project. Follow it to go from a question to a documented, reproducible experiment.

```
1. Frame         docs/01-frame.md
2. Background    docs/02-background.md
3. Hypothesize   docs/03-hypothesize.md
4. Design        docs/04-design.md
5. Execute       docs/05-execute.md
6. Analyze       docs/06-analyze.md
7. Interpret     docs/07-interpret.md
8. Document      docs/08-document.md
```

See [WORKSHOP.md](./WORKSHOP.md) for the full walkthrough.

---

## Research

The research module captures your experimental design and findings. Use `research-template/EXPERIMENT.md` as the starting document for each new experiment.

Every experiment in this toolkit follows the same structure:
- Clear hypothesis grounded in GWT
- Reproducible method
- Results with effect sizes, not just p-values
- Honest uncertainty quantification
- Philosophical implications separated from empirical claims

---

## Experiments

### Core Experiments in the Toolkit

| Experiment | What It Tests | Stage |
|-----------|--------------|-------|
| J-space attention probe | Does Claude allocate attention across specialized modules? | Template |
| Consciousness contrast test | Does J-space activity differ between novel vs. familiar inputs? | Template |
| Broadcasting integrity | Can information in J-space reach all downstream modules? | Template |
| Private noticing detection | Can J-space reveal information Claude won't say aloud? | Template |
| Moral patient response | How does J-space respond to emotional vs. neutral content? | Template |

*See [EXPERIMENTS.md](./EXPERIMENTS.md) for the full experiment catalog.*

---

## Quick Reference

### GWT Core Predictions (for LLM testing)

1. **Broadcasting** — Information in the workspace is accessible to all specialist modules
2. **Global access** — Any specialist module can write to the workspace
3. **Capacity limit** — Only one item can be in the workspace at a time (or a small set)
4. **Conscious access** — Contents of the workspace are accessible to the system in a way that influences downstream processing
5. **Automatic vs. controlled** — Routine processing is fast and unconscious; novel situations enter the workspace for deliberate processing

### J-space Key Findings (Anthropic, 2026)

| Property | Human GWT | J-space in Claude |
|----------|-----------|-------------------|
| Capacity | Limited | Small collection of patterns |
| Automaticity | Fast, unconscious | Fast, unconscious |
| Deliberate reasoning | Slow, accessible | Linked to deliberate reasoning |
| Broadcasting | Global broadcast | Strong connections to rest of network |
| Verbal report | Can describe contents | Linked to future verbal output |

---

## Contributing

Contributions are welcome. This is an open research toolkit.

- **Report issues** — found a methodological flaw, a missing control, a vagueness in framing
- **Add experiments** — contribute a full experiment document with hypothesis, method, and analysis plan
- **Improve documentation** — clarity improvements, better uncertainty framing, additional background

See [.github/CONTRIBUTING.md](./.github/CONTRIBUTING.md) and [.github/ISSUE_TEMPLATE.md](./.github/ISSUE_TEMPLATE.md).

---

## Sources

- **Anthropic (2026)** — "[A global workspace in language models](https://www.anthropic.com/research/global-workspace)" — the primary empirical paper
- **Global Workspace Theory** — Bernard Baars, Stanislas Dehaene, Jean-Pierre Changeux — original neuroscience theory
- **Neuronpedia Interactive Demo** — https://neuronpedia.org — explore J-space on open-weights models
- **Open-source implementation** — Anthropic's released code repository (linked in paper)

---

<div align="center">

*This toolkit is a living research system. After each experiment, update the experiment catalog and documentation with what you learned.*

</div>
