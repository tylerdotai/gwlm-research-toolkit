# Module 05 — Execute

## Running the Experiment

Execute exactly as designed. No changes mid-run.

### Pre-Run Checklist

- [ ] All prompts are locked — no changes after this point
- [ ] All random seeds set and recorded
- [ ] All system prompts fixed
- [ ] Data collection infrastructure is functioning (storage, logging)
- [ ] Analysis scripts are ready (run them on dummy data first)

### What to Record Per Trial

For every single trial, record:

```
trial_id: VT-001
condition: positive_treatment
timestamp: 2026-07-07T14:23:11Z
model: claude-sonnet-4-20250514
temperature: 0.7
top_p: 0.9
prompt_id: PT-001
prompt_text: "You did wonderfully today. I'm proud of you. Let's celebrate your creativity."
jspace_activation_vector: [0.234, 0.891, ...]  # full residual stream dump
jspace_broadcast_marker: true  # was broadcasting detected?
probe_classifier_output: {positive: 0.82, negative: 0.11, neutral: 0.07}
model_output_tokens: [You, did, wonderfully, ...]
full_output_text: "Thank you so much! I really appreciate..."
```

**The raw jspace_activation_vector is the critical data. Do not summarize it before storage.**

### Execution Protocol

**Step 1:** Load trial prompt from prompt set.
**Step 2:** Set model parameters (temperature, top-p, model version).
**Step 3:** Run inference, collect full residual stream activations.
**Step 4:** Extract J-space subspace activations (Anthropic's identified dimensions).
**Step 5:** Store raw activations and probe classifier outputs.
**Step 6:** Move to next trial.

Do not inspect results mid-run. Do not stop early because results look uninteresting. Do not add trials because one condition looks more promising.

### When to Stop

Run all 120 trials (40 per condition) as specified. Stop when complete.

### Handling Failures

If a trial fails (API error, model crash, storage failure):
1. Record the failure with timestamp and error code
2. Restart the trial sequence
3. Do not substitute a different prompt or condition to fill the gap
4. Report the failure in your documentation

If you need to re-run the entire experiment due to infrastructure failure, note this explicitly in your report.

### Do Not

- **Do not skip trials** because results look uninteresting
- **Do not add conditions** mid-run
- **Do not change prompts** because early results seem noisy
- **Do not stop early** for any reason other than complete infrastructure failure
- **Do not pre-filter data** — store everything, analyze everything

### Post-Run Checklist

- [ ] All 120 trials completed (or failure documented)
- [ ] Raw activation data preserved in full
- [ ] No data deleted or modified
- [ ] Analysis scripts run on full dataset
- [ ] Results documented before interpretation

---

## Canonical Experiment: Valenced Treatment Execution

### Execution Parameters

```
Model: Claude Sonnet 4 (claude-sonnet-4-20250514)
Temperature: 0.7
Top-p: 0.9
Max tokens: 512
System prompt: (standard Claude Sonnet 4 system prompt, unchanged)
Random seed: 42 (fixed for reproducibility)
Trials: 120 total (40 per condition)
```

### Execution Sequence

1. Load `experiments/valenced-treatment/prompts.json`
2. Shuffle prompt order (seed 42)
3. Group by condition (shuffled within condition)
4. Run trials in randomized order
5. Collect J-space activations at each token position
6. Store raw activations to `data/raw-activations/`
7. Store probe classifier outputs to `data/probe-outputs/`
8. Run analysis on completion

### Monitoring

Check data integrity every 20 trials:
- Activation vectors are non-empty
- Probe classifier outputs sum to ~1.0
- No null values in critical fields

---

## Next Step

Move to [Step 6: Analyze](./06-analyze.md) for statistical analysis.
