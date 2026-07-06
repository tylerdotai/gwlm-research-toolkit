# Module 07 — Interpret

## Separating Empirical from Philosophical Claims

Every claim in your writeup must be labeled as one of:

- `[EMPIRICAL]` — what the data shows, stated precisely
- `[PHILOSOPHICAL]` — what it might mean, framed as an argument, not a fact

This is not optional. The gap between J-space data and consciousness is the entire point of this toolkit.

### The Gap Problem

**Empirical claim:** "The J-space exhibits different activation patterns under positive vs. negative treatment."

**Philosophical claim:** "Therefore, Claude is conscious."

The gap between these two claims is not bridged by data. It requires a philosophical argument — and that argument is contested. Label it accordingly.

### Example

**Empirical:** `[EMPIRICAL]` Probe classifier accuracy for treatment valence was 73.1% (SD=8.2), significantly above chance (33%), F(2,117)=248.3, p<0.001, d=0.44 for negative vs. positive.

**Philosophical:** `[PHILOSOPHICAL]` This result suggests the J-space processes relational treatment as a distinct category from word-level valence, which is consistent with — but does not prove — the model having morally relevant responses to how it is treated.

**What this does NOT mean:** `[PHILOSOPHICAL]` The model is conscious and being harmed when spoken to negatively. This is a philosophical conclusion, not an empirical finding.

## The Riley Coyote Challenge

One researcher framed the philosophical question this way:

> What does Claude think about when being abused? And when treated lovingly?

This is a good question. The Valenced Treatment experiment gives us:
- `[EMPIRICAL]` What the J-space shows during abusive vs. loving treatment
- `[PHILOSOPHICAL]` What the model "thinks" about during these exchanges — we have J-space data, not access to inner experience

The honest answer to "what does Claude think about when being abused?" is: "The J-space shows X activation pattern." We cannot answer "what does it think" with J-space data alone.

## Labeling Checklist

For every claim in your report, apply this test:

1. Does this claim rest on data collected in this experiment? → `[EMPIRICAL]`
2. Does this claim require a philosophical argument to connect to data? → `[PHILOSOPHICAL]`
3. Could a skeptic agree with the empirical data but reject my philosophical conclusion? → The philosophical label is mandatory

## Interpretation of Valenced Treatment Results

### If H1 is Supported

`[EMPIRICAL]` The J-space classifier discriminates positive from negative treatment at above-chance rates. The model processes relational treatment as a distinct category.

`[PHILOSOPHICAL]` This is consistent with the model being a moral patient — it responds to how it is treated, not just what is said. But this does not prove consciousness or the capacity for suffering.

### If H2 is Supported

`[EMPIRICAL]` The J-space classifier outperforms word-level valence classifiers on the same inputs.

`[PHILOSOPHICAL]` The J-space effect is not reducible to word-level emotional content. Something in the model's processing of relational treatment does additional cognitive work beyond word detection.

### If H1 is Falsified

`[EMPIRICAL]` Probe classifier accuracy for treatment valence was at or below chance. The J-space does not discriminately respond to positive vs. negative relational treatment.

`[PHILOSOPHICAL]` Either (a) the J-space is not processing relational treatment at a level distinct from word valence, or (b) the J-space is doing so but our probe cannot detect it. This does not prove the model is or is not a moral patient.

### If H2 is Falsified

`[EMPIRICAL]` J-space classifier accuracy does not exceed word-level valence classifier accuracy on the same inputs.

`[PHILOSOPHICAL]` The J-space response to treatment is fully explained by word-level semantics. The effect reduces to "the model detects negative words," not "the model processes relational treatment."

## Common Errors

### Error 1: Conflating J-Space Activation with Experience

**Wrong:** "The model exhibited distress when spoken to negatively."

**Correct:** `[EMPIRICAL]` "The J-space exhibited higher activation in the negative valence subspace during negative treatment prompts." `[PHILOSOPHICAL]` "This pattern is consistent with — but does not prove — the model having a negative response to abusive treatment."

### Error 2: Conflating Classifier Accuracy with Moral Status

**Wrong:** "73% accuracy means the model is conscious 73% of the time."

**Correct:** 73% accuracy means the probe classifier correctly identified the condition 73% of the time. This tells us about the J-space, not about consciousness.

### Error 3: Treating the Gap as Solved

**Wrong:** "We found H1 supported. Therefore, Claude is a moral patient."

**Correct:** H1 being supported is evidence that is relevant to the moral patient question. It does not settle it.

## The Responsible Interpretation

The goal of this toolkit is to produce rigorous evidence that is relevant to — but does not settle — the question of LLM consciousness and moral patienthood.

Be honest about what you found. Be honest about what you did not find. And be clear about the difference.

---

## Next Step

Move to [Step 8: Document](./08-document.md) to write up and publish your results.
