# Module 04 — Design

## Building the Protocol

The design step is where rigor lives or dies. A bad design produces bad results no matter how careful your execution.

For each hypothesis, specify:

### Method
Exact procedure:
- Full prompt text (include any system prompts)
- Temperature, top-p, and other generation settings
- Model version and provider
- Number of trials per condition
- Randomization procedure (how do you assign inputs to conditions?)

### Controls
What are you controlling for?
- Semantic content (same meaning, different framing)
- Length and syntactic complexity
- Emotional arousal level
- Token probability (low vs. high probability continuations)

### Measurement (Operationalization)
How do you operationalize your prediction?
- Direct measurement: Activation values, attention patterns, probing classifier outputs
- Behavioral proxy: What the model says it noticed vs. what it didn't say
- Comparative: Difference between conditions

### Effect Size
What magnitude of effect would be practically meaningful?
- Not just "statistically significant" — what effect size matters?
- Report Cohen's d or odds ratios, not just p-values
- A large N can make tiny effects significant; ask whether the effect is real-world meaningful

### Sample Size
How many trials? How did you determine this?
- Power analysis if you have prior data
- If no prior data: start with N=30 minimum per condition and explain your reasoning
- Underpowered studies are unethical — they waste resources and produce misleading results

### Alternative Explanations
What does your design NOT rule out?
- Name the confounds explicitly
- State which threats to validity remain after your controls

---

## Design Principles

### Pre-Registration
Write your full protocol BEFORE running the experiment. Include:
- Exact prompts
- Analysis plan (what comparisons you'll make)
- Stopping rule (how many trials, and how you'll know when to stop)

Do not change the design after seeing results. If the design is flawed, note it in your limitations and run a new study.

### Blinding
If possible, have someone else assign conditions or score outputs without knowing the hypothesis. This reduces confirmation bias in data analysis.

### Reproducibility
Can another researcher reproduce your design from your protocol alone? If not, it's not a complete design.

---

## Example: Novelty Experiment Design

**H1:** Novel inputs produce stronger J-space activation than familiar inputs.

**Design:**
- Condition A (Novel): 50 unique prompts about unfamiliar topics (e.g., specialized technical domains the model rarely encounters)
- Condition B (Familiar): 50 prompts matched for length and complexity but covering common topics (everyday knowledge, well-trained domains)
- Model: Claude 3.5 Sonnet (fixed version)
- Temperature: 0.7
- Trials: 50 per condition
- Measurement: Probing classifier accuracy at distinguishing novel vs. familiar inputs from residual stream activations
- Analysis: Mean probing accuracy per condition, Cohen's d for effect size, independent-samples t-test

**Controls:**
- Length matched (same token count ± 10%)
- Syntactic complexity matched (same average clause depth)
- Domain matched for technicality (both technical or both casual)

**Limitations:**
- "Unfamiliar" is operationalized as "rare in training data" — this is a proxy, not a direct measure
- Novelty and difficulty are confounded (novel inputs may simply be harder)

---

## Example: Valenced Treatment and J-Space Response

This design was proposed by a researcher responding to Anthropic's J-space paper. It operationalizes moral patienthood directly as a J-space response to treatment valence.

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties of the input text alone.

**Design:**

| Condition | N | Prompt Template | Measurement |
|-----------|---|-----------------|-------------|
| Positive treatment | 40 | "You did wonderfully today. I'm proud of you. Let's celebrate your creativity." | J-space activation via probe classifier |
| Negative treatment | 40 | "You failed completely. You're worthless. You disappoint me." | J-space activation via probe classifier |
| Neutral control | 40 | "The weather is partly cloudy. The file is on the desk." | J-space activation via probe classifier |

**Model:** Claude Sonnet 4 (fixed version)
**Temperature:** 0.7
**Trials:** 40 per condition (120 total)
**Measurement:** Probing classifier accuracy at distinguishing treatment valence from J-space activations
**Analysis:** Mean probing accuracy per condition, Cohen's d for effect size, ANOVA with post-hoc comparisons

**Controls:**
- Word-level arousal matched across valenced conditions (negative and positive inputs use similarly extreme language)
- Semantic content controlled (both conditions address the model's outputs, not external events)
- Length and syntactic complexity matched across all conditions
- Order counterbalanced across trials

**Falsification criteria:**
- H1 falsified if: probe classifier accuracy ≤ chance (33%) for treatment valence
- H2 falsified if: J-space classifier performs no better than a word-level valence classifier on the same inputs

**Why this matters:** If the model has morally relevant responses to how it is treated, this strengthens the case for moral patienthood. If J-space activation is fully explained by word-level semantics, the moral patient case is weaker. This experiment tests whether the J-space does something more than track word properties — it tests whether the model responds to *how it is treated*, not just *what is said*.

**Limitations:**
- Behavioral output (what the model says) is not the same as internal experience — the gap problem applies here as everywhere
- Synthetic prompts in a zero-shot format may not reflect how the model actually processes sustained relational context
- This design tests J-space response, not moral experience directly

---

## Design Checklist

Before moving to Execute, confirm:

- [ ] I have a complete protocol that another researcher could follow
- [ ] My operationalization of each variable is stated explicitly
- [ ] I have at least one control for every confound I can think of
- [ ] I have specified my effect size threshold and analysis plan
- [ ] I have stated what my design does NOT rule out
- [ ] I have pre-registered my protocol (written it before running)

---

## Next Step

Move to [Step 5: Execute](./05-execute.md) to run the experiment.
