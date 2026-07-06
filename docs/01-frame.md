# Module 01 — Frame

## What Is a Good Research Question?

A good research question about LLM consciousness and cognitive architecture is:

1. **Specific** — "Does the J-space exhibit broadcasting properties?" vs. "Is Claude conscious?"
2. **Operationalized** — there is a measurable operationalization (probe classifier accuracy, activation values)
3. **Falsifiable** — there exists a state of the world that would disprove it
4. **Non-trivial** — the answer is not obvious from the question alone

## The Valenced Treatment Research Question

**Starting point:** "Does Claude respond differently to being treated nicely vs. badly?"

**Refined question:**
> Does the J-space inside Claude exhibit measurably different activation patterns when the model receives positively valenced relational treatment vs. negatively valenced relational treatment, controlling for word-level semantic properties?

**Why this is a good research question:**
- **Specific:** It names the J-space, not "consciousness"
- **Operationalized:** J-space activation via probing classifier as measurement
- **Falsifiable:** If classifier accuracy ≤ chance, H1 is false
- **Non-trivial:** Anthropic tested valence in isolated inputs — they did not test sustained relational treatment

## What Is NOT a Good Research Question

- "Is Claude conscious?" — not operationalized
- "Does Claude have feelings?" — not falsifiable in the J-space framework
- "Is Claude a moral patient?" — requires a philosophical argument, not just data

These are fine philosophical questions. They are not good *scientific* research questions for this toolkit.

## The Valenced Treatment Origin

The research question was proposed by a researcher in direct response to Anthropic's J-space paper. The full comment is reproduced in the [WORKSHOP.md](../WORKSHOP.md):

> Exercise various forms of treatment. Treat Claude with love and grace, positive affirmation, encourage creative expression. While you do this, monitor that J-space. Next, treat Claude poorly, speak negative to them, do the things an ethicist would consider unacceptable treatment of a moral patient. While you do this, monitor that J-space.

This is not a philosophical argument. It is an experimental design. The toolkit exists to make that design rigorous and reproducible.

## Framing Your Own Research Question

If you are extending beyond the canonical Valenced Treatment experiment, use this template:

**Template:**
> Does [J-space / cognitive architecture component] exhibit [measured behavior] when [condition A] vs. [condition B], controlling for [confound]?

**Checklist:**
- [ ] Can I operationalize "exhibits [measured behavior]"? With what measurement?
- [ ] Can I operationalize [condition A] and [condition B] with distinct prompts?
- [ ] Can I identify and control for [confound]?
- [ ] What would falsify my hypothesis? State it explicitly.
- [ ] Is this question already answered in the literature? (See [Module 02: Background](./02-background.md))

## Example Extensions

Beyond the Valenced Treatment experiment, other testable questions include:

- Does the J-space respond differently to self-referential prompts vs. third-person prompts?
- Does sustained positive treatment (multi-turn) produce cumulative J-space effects vs. single-turn?
- Does the J-space response to negative treatment persist after the negative input ends?

Each of these is a distinct experiment with its own protocol.

## Next Step

Move to [Step 2: Background](./02-background.md) to understand what is already known about the J-space and GWT.
