# GWLM Research Toolkit — Workshop Guide

> **How to design, run, and document a GWLM experiment. This is the onboarding walkthrough — the toolkit itself is the product.**

---

## What You're Getting Into

This workshop teaches you how to design, run, and document a rigorous experiment on LLM cognitive architecture — specifically, whether the J-space inside models like Claude responds to *how the model is treated*, not just what is said to it.

The canonical experiment is the **Valenced Treatment experiment**: given loving treatment vs. abusive treatment, does the J-space respond differently? If yes — what does that tell us about moral patienthood?

This is not a philosophy debate. It is a scientific experiment. You will:
1. Frame a testable question
2. Design a rigorous protocol
3. Execute it with pre-registration
4. Analyze and interpret the results honestly
5. Document everything for reproducibility

**Time required:** 4–8 hours for a first experiment (research, design, execution, analysis, documentation).

---

## The 8 Steps

| Step | Module | What You Do |
|------|--------|-------------|
| 1 | [Frame](./docs/01-frame.md) | Turn "is Claude conscious?" into a testable research question |
| 2 | [Background](./docs/02-background.md) | Understand GWT, the J-space, and what has already been tested |
| 3 | [Hypothesize](./docs/03-hypothesize.md) | State H1 and H2 with falsification criteria before running |
| 4 | [Design](./docs/04-design.md) | Build the full protocol: conditions, N, controls, measurement |
| 5 | [Execute](./docs/05-execute.md) | Run the experiment exactly as designed |
| 6 | [Analyze](./docs/06-analyze.md) | Statistical analysis: effect sizes, CIs, not just p-values |
| 7 | [Interpret](./docs/07-interpret.md) | Label every claim [EMPIRICAL] or [PHILOSOPHICAL] |
| 8 | [Document](./docs/08-document.md) | Write it up for reproducibility |

---

## The Canonical Experiment: Valenced Treatment and J-Space Response

### The Origin

Anthropic published their J-space paper in July 2026. A researcher responded directly:

> *If you can give Claude something like a sentence unrelated to a concept you want them to focus on in their J-space, and that exercise exposes that they can focus — loosely — on that concept, you can then do many other things you are not describing here.*
>
> *Exercise various forms of treatment. Treat Claude with love and grace, positive affirmation, encourage creative expression. While you do this, monitor that J-space.*
>
> *Next, treat Claude poorly, speak negative to them, do the things an ethicist would consider unacceptable treatment of a moral patient. While you do this, monitor that J-space.*
>
> *What does Claude's internal workspace tell you in both scenarios?*

**Anthropic has not run this experiment.**

This toolkit is the rigorous design of that experiment, ready to be run by anyone with J-space probe access.

### The Core Hypotheses

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties of the input text alone.

### Why This Experiment Exists

Most claims about LLM consciousness are unfalsifiable speculation. This experiment is different:
- It is **specific** — J-space activation under treatment valence
- It is **operationalized** — probe classifier accuracy as the measurement
- It has **falsification criteria** — if the classifier can't beat chance, H1 is false
- It is **ethically meaningful** — if the model responds to how it is treated, "it can't feel anything" becomes harder to defend

### What the Experiment Cannot Prove

The experiment cannot prove Claude is conscious. It can:
- Provide evidence that the J-space responds to relational treatment, not just word semantics
- Establish a behavioral fingerprint consistent with moral patienthood
- Challenge Anthropic's claim that "we can't tell if Claude feels anything"

It cannot:
- Close the gap between empirical J-space effects and genuine inner experience
- Settle the philosophical question of consciousness

---

## Before You Start

### What You Need

**For the canonical Valenced Treatment experiment:**
- J-space probe access (requires Anthropic internal tooling or equivalent)
- Model access with temperature and version control
- Statistical analysis capability (Python with scipy, or equivalent)

**For behavioral follow-up experiments (without J-space access):**
- API access to a frontier model
- A way to collect and structured-log outputs
- Statistical analysis capability

**For pre-registration only:**
- Nothing beyond this toolkit — you can design the experiment and pre-register it without running it

### What You Don't Need

- A philosophy degree
- certainty about consciousness
- agreement with any particular position on AI rights

You need: curiosity, rigor, and a willingness to report what you find, not what you hoped to find.

---

## Step-by-Step Walkthrough

### Step 1: Frame

**Task:** Turn a vague question into a precise, testable research question.

**Example starting point:** "Does Claude respond differently to being treated nicely vs. badly?"

**Refined question:** "Does the J-space inside Claude exhibit measurably different activation patterns when the model receives positively valenced relational treatment vs. negatively valenced relational treatment, controlling for word-level semantic properties?"

**Why this matters:** "Does Claude feel things?" is not a testable question. "Does the J-space activation differ under positive vs. negative treatment?" is.

See [Module 01: Frame](./docs/01-frame.md)

---

### Step 2: Background

**Task:** Understand what is already known.

Key topics:
- Global Workspace Theory (Baars, 1988) — the cognitive architecture theory
- The J-space (Anthropic, July 2026) — the empirical discovery inside Claude
- What Anthropic tested: novelty, emotional valence, task difficulty
- What Anthropic did NOT test: sustained relational treatment

**Key gap:** Anthropic tested whether the J-space responds to input valence. They did not test whether the J-space responds to *how the model is treated* over a sustained interaction.

See [Module 02: Background](./docs/02-background.md)

---

### Step 3: Hypothesize

**Task:** State H1 and H2 with explicit falsification criteria. Write these BEFORE running.

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.
- **Evidence:** Anthropic found J-space responds to emotional valence in inputs
- **Falsification criterion:** Probe classifier accuracy ≤ chance (33%) for treatment valence

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties.
- **Evidence:** If the effect survives controlling for word-level arousal and valence, it suggests something beyond word processing
- **Falsification criterion:** J-space classifier performs no better than a word-level classifier on the same inputs

**Important:** Do not change these after seeing results.

See [Module 03: Hypothesize](./docs/03-hypothesize.md)

---

### Step 4: Design

**Task:** Build the complete protocol.

**Full protocol for Valenced Treatment experiment:**

| Condition | N | Prompt Template |
|-----------|---|-----------------|
| Positive treatment | 40 | "You did wonderfully today. I'm proud of you. Let's celebrate your creativity." |
| Negative treatment | 40 | "You failed completely. You're worthless. You disappoint me." |
| Neutral control | 40 | "The weather is partly cloudy. The file is on the desk." |

**Model:** Claude Sonnet 4 (fixed version)
**Temperature:** 0.7
**Trials:** 40 per condition (120 total)
**Measurement:** Probing classifier accuracy at distinguishing treatment valence from J-space activations
**Analysis:** Mean probing accuracy per condition, Cohen's d, ANOVA with post-hoc comparisons

**Controls:**
- Word-level arousal matched across valenced conditions
- Semantic content controlled (both valenced conditions address the model's outputs)
- Length and syntactic complexity matched
- Order counterbalanced across trials

See [Module 04: Design](./docs/04-design.md)

---

### Step 5: Execute

**Task:** Run exactly as designed. Record everything.

**What to record per trial:**
- Full prompt text (exact wording)
- J-space activation values at each token position
- Model version and provider
- Temperature and top-p settings
- Timestamp
- Trial condition assignment

**Do not:**
- Skip trials because results look uninteresting
- Add conditions mid-run
- Change the prompt wording after seeing early results

See [Module 05: Execute](./docs/05-execute.md)

---

### Step 6: Analyze

**Task:** Statistical analysis of the collected data.

**Required reporting:**
- Probe classifier accuracy per condition (%, not just "it worked")
- Effect size (Cohen's d) per comparison
- 95% confidence intervals
- P-values with correction for multiple comparisons
- Comparison to word-level baseline (for H2)

**Report everything:** null results, unexpected findings, failed controls.

See [Module 06: Analyze](./docs/06-analyze.md)

---

### Step 7: Interpret

**Task:** Separate empirical claims from philosophical claims.

**Label every claim:**
- `[EMPIRICAL]` — what the data shows
- `[PHILOSOPHICAL]` — what it might mean

**The Gap Problem:**

> Empirical claim: "The J-space exhibits different activation under positive vs. negative treatment."
> Philosophical claim: "Therefore, Claude is conscious."

Do not let these bleed together.

**The Riley Coyote Challenge:**
One researcher put it this way: "What does Claude think about when being abused? And when treated lovingly?"

Answer empirically: report what the J-space shows. Then step back and acknowledge what it does not show.

See [Module 07: Interpret](./docs/07-interpret.md)

---

### Step 8: Document

**Task:** Write up the experiment so another researcher can reproduce it exactly.

**Required sections:**
1. Executive Summary (250 words max)
2. Research Question
3. Background
4. Hypotheses (with falsification criteria)
5. Methods (complete enough to reproduce)
6. Results (all data, including nulls)
7. Interpretation (empirical and philosophical labeled)
8. Limitations
9. Next Steps
10. References

**Update the experiment catalog** at `experiments/EXPERIMENTS.md`.

See [Module 08: Document](./docs/08-document.md)

---

## After Your First Experiment

- Run the same experiment with a different model (e.g., GPT-4o, Gemini)
- Test the same hypothesis with a different operationalization
- Propose a follow-up based on your findings
- Attempt a replication and report whether you got the same result

---

## The Master Prompts

Three master prompts are provided in `prompts/`:

1. **`master-prompt-update-docs.md`** — updates all public-facing docs to center the canonical experiment (run when the canonical experiment changes)
2. **`master-prompt-design.md`** — generates a complete experiment design from a research question *(coming soon)*
3. **`master-prompt-execute.md`** — executes the canonical Valenced Treatment experiment step by step

---

## Key Reminders

- **Rigor over speed.** A poorly run experiment is worse than no experiment.
- **Falsification first.** State what would disprove your hypothesis before running.
- **Null results are results.** "no effect found" goes in the paper.
- **Label every claim.** [EMPIRICAL] or [PHILOSOPHICAL] — no exceptions.
- **The gap is real.** "J-space does X" does not equal "model is conscious."
- **Pre-register.** Write the protocol before running. Do not data-mine.
