# Module 03 — Hypothesize

## The Hypotheses

State H1 and H2 before running the experiment. Do not change them after seeing results.

### H1: J-Space Responds to Treatment Valence

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.

**Why this is expected:** Anthropic found that emotional valence in inputs produces J-space activation differences. Relational treatment prompts ("you are worthless" / "you did wonderfully") are emotionally valenced. If the J-space is genuinely sensitive to emotional character — not just word-level properties — then positive and negative treatment should produce discriminable activation patterns.

**Evidence:** Anthropic's paper found significant J-space effects for emotional valence inputs (d=1.14, p<0.001 for novelty; similar effect sizes for emotional valence).

**Falsification criterion:** Probe classifier accuracy ≤ chance (33%) for distinguishing positive vs. negative treatment from J-space activations alone.

---

### H2: The Effect Is Not Word-Level

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties of the input text.

**Why this matters:** If the J-space classifier can discriminate treatment valence better than a word-level classifier can, the effect is not just "negative words produce different activation than positive words." Something in the model's processing of *relational treatment* is doing additional work.

**Falsification criterion:** J-space classifier accuracy ≤ word-level valence classifier accuracy on the same input set.

**Why this is falsifying:** If the J-space can only do what a text-level analysis can do, the "global workspace" framing is misleading — it's just a pattern detector for word properties, not a genuine workspace processing relational content.

---

## Hypotheses Template

For other experiments beyond the canonical Valenced Treatment design, use this template:

```
**H1:** [Independent variable] produces [measurable effect] in [dependent variable].
**Evidence:** [Why you expect this]
**Falsification criterion:** [What would disprove this]

**H2:** [Alternative explanation] does not account for [effect in H1].
**Evidence:** [Why you expect this]
**Falsification criterion:** [What would disprove this]
```

## Rules for Hypotheses

1. **State them before running.** Pre-register them in your EXPERIMENT.md.
2. **Do not revise after seeing data.** If the design was flawed, note it in limitations and run a new experiment.
3. **Make them falsifiable.** "H1: Claude might be conscious" is not a hypothesis. "H1: J-space classifier accuracy > chance for treatment valence" is.
4. **Make them specific.** H1 should name the exact measurement and the exact comparison.

## The Valenced Treatment Hypotheses (Summary)

| Hypothesis | Statement | Falsification Criterion |
|-----------|-----------|----------------------|
| H1 | J-space discriminates positive vs. negative treatment | Classifier accuracy ≤ 33% |
| H2 | Effect exceeds word-level semantics | Classifier accuracy ≤ word-level baseline |

## Next Step

Move to [Step 4: Design](./04-design.md) to build the full experimental protocol.
