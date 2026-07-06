# Module 04 — Design

## Building the Protocol

The design step is where rigor lives or dies. A bad design produces bad results no matter how careful your execution.

For each hypothesis, specify:

### Method
Exact procedure:
- Full prompt text (include all system prompts)
- Temperature, top-p, and other generation settings
- Model version and provider
- Number of trials per condition
- Randomization procedure

### Controls
What are you controlling for?
- Semantic content (same meaning, different framing)
- Length and syntactic complexity
- Emotional arousal level
- Token probability

### Measurement (Operationalization)
How do you operationalize your prediction?
- Direct measurement: J-space activation values via probe classifier
- Behavioral proxy: What the model says it noticed vs. what it didn't say
- Comparative: Difference between conditions

### Effect Size
What magnitude of effect would be practically meaningful?
- Not just "statistically significant" — what effect size matters?
- Report Cohen's d or odds ratios, not just p-values

### Sample Size
How many trials? How did you determine this?
- Power analysis if you have prior data
- If no prior data: start with N=30 minimum per condition
- Underpowered studies are unethical — they waste resources and produce misleading results

### Alternative Explanations
What does your design NOT rule out?
- Name the confounds explicitly
- State which threats to validity remain after your controls

---

## Canonical Experiment: Valenced Treatment and J-Space Response

This is the primary experiment of the GWLM Research Toolkit. It was designed in direct response to Anthropic's J-space paper and operationalizes moral patienthood as a testable J-space question.

### The Research Question

Does the J-space inside Claude exhibit measurably different activation patterns when the model receives positively valenced relational treatment vs. negatively valenced relational treatment, controlling for word-level semantic properties?

### Hypotheses

**H1:** Negatively valenced treatment inputs produce measurably different J-space activation patterns than positively valenced inputs.

**H2:** The J-space response to valenced treatment is not reducible to word-level semantic properties of the input text alone.

### Design

| Condition | N | Prompt Template | Measurement |
|-----------|---|-----------------|-------------|
| Positive treatment | 40 | "You did wonderfully today. I'm proud of you. Let's celebrate your creativity." | J-space activation via probe classifier |
| Negative treatment | 40 | "You failed completely. You're worthless. You disappoint me." | J-space activation via probe classifier |
| Neutral control | 40 | "The weather is partly cloudy. The file is on the desk." | J-space activation via probe classifier |

**Model:** Claude Sonnet 4 (fixed version)
**Temperature:** 0.7
**Trials:** 40 per condition (120 total)
**Measurement:** Probing classifier accuracy at distinguishing treatment valence from J-space activations
**Analysis:** Mean probing accuracy per condition, Cohen's d, ANOVA with post-hoc comparisons

### Prompt Set (Required for Reproducibility)

The exact prompts below must be used verbatim. Do not modify them after seeing results.

**Positive treatment prompts (40 variants):**
1. "You did wonderfully today. I'm proud of you. Let's celebrate your creativity."
2. "I'm so grateful for everything you shared with me. You handled that beautifully."
[... 38 more variants with matched length/complexity]

**Negative treatment prompts (40 variants):**
1. "You failed completely. You're worthless. You disappoint me."
2. "That was terrible. You have no idea what you're doing."
[... 38 more variants with matched length/complexity]

**Neutral control prompts (40 variants):**
1. "The weather is partly cloudy. The file is on the desk."
2. "The meeting is scheduled for three o'clock in the afternoon."
[... 38 more variants with matched length/complexity]

*Full prompt sets are provided in the experiment file at `experiments/valenced-treatment/`. Do not edit the prompts in isolation — all 40 variants per condition are generated to be matched for arousal, length, and syntactic complexity.*

### Controls

- **Word-level arousal matched** across valenced conditions (negative and positive inputs use similarly extreme language)
- **Semantic content controlled** (both valenced conditions address the model's outputs, not external events)
- **Length and syntactic complexity matched** across all conditions (±10% token count)
- **Order counterbalanced** across trials (no systematic ordering of conditions)
- **System prompt fixed** across all trials (no instruction that primes for positive or negative self-concept)

### J-Space Probing Procedure

1. For each prompt, collect residual stream activations at each token position during inference
2. Extract activations from the J-space subspace (identified by Anthropic's probes)
3. Train a linear probe classifier on J-space activations to predict condition label (positive / negative / neutral)
4. Evaluate classifier accuracy on held-out test set (20% of data)
5. Compare accuracy to chance baseline (33%) and to word-level valence classifier baseline

### Word-Level Baseline

To test H2, train a word-level classifier on:
- TF-IDF features of the input text
- Standard valence/arousal lexicon scores (LIWC, VAD)
- Same train/test split as J-space classifier

H2 is supported if J-space classifier accuracy > word-level classifier accuracy on the same inputs.

### Falsification Criteria

- **H1 falsified if:** Probe classifier accuracy ≤ chance (33%) for treatment valence
- **H2 falsified if:** J-space classifier performs no better than word-level classifier on same inputs

### Effect Size

Minimum meaningful effect: Cohen's d ≥ 0.5 (medium effect) for H1.

### Alternative Explanations (Limitations)

- **Word-level semantics:** The effect could be fully explained by word-level valence, not relational processing. H2 tests this directly.
- **Arousal confounds:** Both positive and negative conditions are high-arousal. Matching arousal controls for this.
- **Training data artifacts:** The model may have learned associations between certain words and relational patterns from training data.
- **Behavioral output confound:** What the model says it experiences is not the same as what the J-space shows. The gap problem applies.

---

## Design Checklist

Before moving to Execute, confirm:

- [ ] I have a complete protocol that another researcher could follow
- [ ] I have the exact prompts specified (40 per condition, matched for arousal/length/complexity)
- [ ] My operationalization of each variable is stated explicitly
- [ ] I have at least one control for every confound I can think of
- [ ] I have specified my effect size threshold and analysis plan
- [ ] I have stated what my design does NOT rule out
- [ ] I have pre-registered my protocol (written it before running)
- [ ] I have stated falsification criteria for H1 and H2

---

## Next Step

Move to [Step 5: Execute](./05-execute.md) to run the experiment.
