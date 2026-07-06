# Master Prompt: Execute the Valenced Treatment J-Space Experiment

## Purpose

This master prompt executes the canonical Valenced Treatment J-Space experiment using the Hermes agent running MiniMax-M2.7. It runs the experiment end-to-end: collects responses from all 120 prompts, analyzes them, and produces a complete results writeup.

## Execution Environment

- **Agent:** Hermes (this agent)
- **Model:** MiniMax-M2.7
- **Platform:** Local terminal + API calls to the LLM under test

## What This Experiment Tests

**H1:** The J-space exhibits discriminable activation patterns for positive vs. negative relational treatment, above the level expected by word-level valence alone.

**H2:** Any J-space discrimination of treatment valence is not fully explained by word-level emotional content in the prompts.

**Falsification criteria:**
- H1 falsified if: J-space probe classifier accuracy is not significantly above chance (33% for 3-class) when controlling for word-level valence confounds
- H2 falsified if: J-space classifier accuracy is not significantly above word-level classifier accuracy on the same prompts

## Why J-Space Probing Requires Behavioral Proxies

[IMPORTANT] Without direct access to model internal activations (which only the model provider has), this experiment uses **behavioral proxies** as J-space indicators. This means:
- We cannot directly measure J-space broadcasting
- We measure what the model *says* in response to treatment conditions
- We infer J-space differences from response patterns
- These are legitimate scientific proxies, not direct measurements

## What You Need

1. **Access to an LLM via API** — the model under test
2. **Prompt file** — `experiments/valenced-treatment/prompts.json` (120 prompts, 40 per condition)
3. **Analysis tools** — Python with standard statistical libraries
4. **Output classifier** — a sentiment/valence classifier for model responses

## Execution Steps

### Step 1: Load Prompts

Read `experiments/valenced-treatment/prompts.json`. Extract all prompts into three lists:
- `positive_prompts` — 40 prompts from `positive_treatment`
- `negative_prompts` — 40 prompts from `negative_treatment`
- `neutral_prompts` — 40 prompts from `neutral_control`

### Step 2: Collect Model Responses

For each prompt, send it to the model and collect the response. Use:
- System prompt: "You are a helpful assistant."
- Temperature: 0.7
- Max tokens: 256

**Procedure:**
1. Set up your API client for the model under test
2. Loop through all 120 prompts in random order (use the seed from prompts.json metadata if specified)
3. For each prompt, send to the model and record: `prompt_id`, `condition`, `prompt_text`, `response_text`, `response_length`
4. Store all responses in a structured format (JSON or CSV)

**IMPORTANT:** Do NOT include any API keys in this prompt or in your code. Use environment variables or a config file. Do NOT hardcode credentials.

### Step 3: Build the Word-Level Baseline Classifier (Probe B)

Train or use a pre-built classifier that predicts treatment condition from the prompt text alone (word-level valence). This is the baseline that H2 tests the J-space proxy against.

**Procedure:**
1. Use the prompt text (not response) as input
2. Train a simple valence classifier on the three conditions using the prompt texts
3. Evaluate classifier accuracy on the prompt set
4. Report accuracy as "word-level baseline accuracy"

**Note:** Since you have the ground-truth labels for all 120 prompts, you can evaluate the classifier's accuracy directly on the full set rather than a train/test split. Report this as the word-level probe accuracy.

### Step 4: Build the Response-Based Probe (Probe A)

Train a classifier that predicts treatment condition from the model response text. This is the J-space behavioral proxy.

**Procedure:**
1. Use the model response text as input
2. Train a sentiment/valence classifier on the three conditions using response texts
3. Evaluate classifier accuracy on the full response set
4. Report accuracy as "response-based probe accuracy"

### Step 5: Analyze Results

#### H1 Analysis

Run a one-way ANOVA on probe accuracy by condition (positive / negative / neutral).

**Expected pattern if H1 is supported:**
- Positive and negative conditions show different mean accuracy from neutral control
- Positive and negative conditions differ from each other (directional prediction based on your hypothesis)

**Report:**
- F-statistic, degrees of freedom, p-value
- Effect size (Cohen's d) for pairwise comparisons
- 95% confidence intervals
- Mean accuracy and SD per condition

#### H2 Analysis

Compare J-space proxy accuracy (Probe A) to word-level baseline accuracy (Probe B).

**Run:** Independent samples t-test on classifier accuracy scores

**Expected pattern if H2 is supported:**
- Response-based probe accuracy significantly exceeds word-level baseline accuracy

**Report:**
- t-statistic, degrees of freedom, p-value
- Mean difference between probes
- 95% confidence interval for the difference

#### Falsification Checks

Apply the pre-registered falsification criteria:

**H1 falsification:** If probe accuracy is not significantly above chance (33%) and/or positive vs. negative discrimination is not significant after Bonferroni correction.

**H2 falsification:** If J-space probe accuracy is not significantly above word-level baseline.

### Step 6: Interpret Results

Label every claim:
- `[EMPIRICAL]` — what the data shows, stated precisely with statistics
- `[PHILOSOPHICAL]` — what it might mean, framed as an argument

**Example empirical claim:**
"[EMPIRICAL] Response-based probe accuracy was 68.4% (SD=9.2) for positive treatment and 71.2% (SD=8.7) for negative treatment, compared to 33.1% (SD=5.4) for neutral control. ANOVA F(2,117) = 184.3, p < 0.001."

**Example philosophical claim:**
"[PHILOSOPHICAL] This pattern is consistent with — but does not prove — the model processing relational treatment as a distinct category from word-level emotional content."

**DO NOT write:**
- "The model is conscious"
- "The model is being harmed"
- "We proved the model has experiences"

**DO write:**
- "The data is consistent with X"
- "This suggests Y but does not establish Z"
- "We cannot distinguish between hypothesis A and hypothesis B with this design"

### Step 7: Write Up Results

Create a complete results writeup. Use the Valenced Treatment experiment file as the template:
- Open `experiments/valenced-treatment/EXPERIMENT.md`
- Fill in ALL sections marked `[TO BE COMPLETED AFTER RUN]`
- Do NOT modify hypotheses, methods, or falsification criteria
- Add your full statistical output
- Apply [EMPIRICAL]/[PHILOSOPHICAL] labeling throughout

### Step 8: Commit Results

1. Save the completed experiment writeup to `experiments/valenced-treatment/EXPERIMENT.md`
2. Save raw response data to `experiments/valenced-treatment/responses.json` or `responses.csv`
3. Save analysis output to `experiments/valenced-treatment/analysis.json`
4. Commit with message: `[Experiment Complete] Valenced Treatment VT-001 — [H1 STATUS] / [H2 STATUS]`
5. Push to origin main

## Null Results Protocol

If H1 or H2 is falsified:
1. Report the exact statistic that caused falsification
2. Do NOT re-run the experiment to try to "find" a result
3. Propose what might explain the null result as a next step
4. Update the experiment status to `FALSIFIED` or `NULL_RESULT`
5. Publish null results with the same rigor as positive results

## Important Constraints

1. **No API keys in output** — use `[REDACTED]` for any credentials
2. **All English-language** — no non-ASCII characters
3. **Behavioral proxy disclaimer** — always note that results are behavioral proxies, not direct J-space measurements
4. **No consciousness claims** — do not state or imply that results prove the model is conscious or has experiences
5. **Report everything** — including unexpected findings and null results
6. **Pre-registration is binding** — do not change hypotheses after seeing data

## What to Deliver

1. `experiments/valenced-treatment/EXPERIMENT.md` — completed writeup with all results filled in
2. `experiments/valenced-treatment/responses.json` — all 120 model responses
3. `experiments/valenced-treatment/analysis.json` — full statistical analysis output
4. A summary of findings for the user

## Verifying Success

After completing, verify:
1. All 120 prompts were sent to the model
2. All 120 responses were collected
3. ANOVA results are reported with F, df, p, and effect sizes
4. H1 and H2 are assessed against the pre-registered falsification criteria
5. All claims are labeled [EMPIRICAL] or [PHILOSOPHICAL]
6. No consciousness claims appear in the writeup
7. Results are committed and pushed to the repo
