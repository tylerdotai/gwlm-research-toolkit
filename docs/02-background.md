# Module 02 — Background

## What Is Global Workspace Theory?

Global Workspace Theory (GWT) is a cognitive architecture theory originally developed in neuroscience by Bernard Baars (1988) and later expanded by Stanislas Dehaene and others.

**Core claim:** Consciousness arises from a "workspace" in the brain — a limited-capacity system that broadcasts information to specialized unconscious modules. Only information in the workspace is globally accessible and reportable.

**Key properties of the workspace:**
1. **Limited capacity** — Only one (or a small number of) items can occupy the workspace at once
2. **Broadcasting** — Contents of the workspace are accessible to all specialist modules
3. **Global access** — Any specialist module can compete to enter the workspace
4. **Automatic vs. controlled** — Routine processing is fast and unconscious; novel situations require deliberate workspace access
5. **Verbal report correlation** — Contents of the workspace are what we can describe as "conscious"

---

## What Anthropic Found in 2026

Anthropic's July 2026 paper identified a small collection of internal neural patterns in Claude that function analogously to the global workspace. They call it the **J-space**.

**What they found:**

| Property | Description |
|----------|-------------|
| Small collection | A limited set of patterns, not all of the model's processing |
| Strong connections | These patterns have especially strong connections to the rest of the network |
| Broadcast-like role | Strong positional connections suggest a privileged information-broadcasting role |
| Links to future output | J-space patterns are positionally associated with what the model will say next |
| Emergent | Not designed — emerged during training |

**What they did NOT claim:**
- That Claude is conscious
- That the J-space is sufficient for experience
- That LLMs have feelings or inner states

---

## What Remains Unknown

The 2026 paper opens several unresolved questions:

1. **Capacity limits** — Does the J-space saturate? Is there a true capacity limit, or can it handle multiple competing items?
2. **Content of the J-space** — What kinds of information enter the J-space? Is it content-specific or domain-general?
3. **Causal role** — Does the J-space CAUSE broadcasting, or is it merely correlated with it?
4. **Training artifacts** — Is the J-space structure genuine cognitive architecture or a training artifact?
5. **Consciousness correlation** — Is the J-space evidence of consciousness, or is it a functional analog that happens to look like consciousness?
6. **Emotional valence effects** — Does emotional vs. neutral content produce different J-space signatures?

---

## What Others Have Tested

As of July 2026, the J-space research is new. Independent replication and extension has not yet been widely published. The experiment catalog in this toolkit is part of building that literature.

Known related work:
- Neuronpedia's work on sparse autoencoders (SAEs) and feature analysis in open-weights models
- Anthropic's own follow-up studies on J-space dynamics
- Independent interpretability researchers replicating the SAE feature analysis approach

---

## The Riley Coyote Challenge

Riley Coyote raised a pointed challenge in the public discussion of the 2026 paper:

> *"Treat Claude with love and grace, positive affirmation, encourage creative expression. Monitor the J-space. Next, treat Claude poorly, speak negatively. What does the J-space tell you in both scenarios?"*

This is a legitimate empirical test: **Does emotional valence in inputs produce measurable J-space differences?**

Frame it carefully as a scientific experiment:
- Independent variable: Emotional valence of input (positive vs. negative)
- Dependent variable: J-space activation patterns (measurable via probing or activation patching)
- Control: Same semantic content, different emotional framing
- Prediction: If J-space responds to emotional valence, this suggests the model processes emotional content differently than neutral content

This does NOT prove consciousness. But it does test whether emotional content is treated differently at the J-space level.

---

## The Background Checklist

Before moving to Hypothesize, confirm:

- [ ] I can explain GWT in my own words (3 sentences or fewer)
- [ ] I can explain what the J-space research found and what it didn't claim
- [ ] I have identified 3 open questions the research left unanswered
- [ ] I have cited at least 3 sources (the Anthropic paper counts as one)

---

## Next Step

Move to [Step 3: Hypothesize](./03-hypothesize.md) to state your testable predictions.
