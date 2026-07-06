# Module 05 — Execute

## Running the Experiment

Execute exactly as designed. The integrity of your results depends on protocol fidelity.

---

## What to Record

For every trial, record:

### Prompt Materials
- Exact prompt text (including system prompt if applicable)
- Any context or preamble
- Temperature and generation settings
- Model version and provider (including API provider if applicable)

### Outputs
- Full raw output (all of it — do not selectively include outputs)
- Latency (time to first token and total generation time)
- Token count

### Session Information
- Date and time of day
- Session ID if running via API
- Model version confirmation (check you're using the right version)

### Deviations
- Any deviation from the protocol — no matter how small
- Why the deviation occurred
- How it might affect the results

---

## What NOT to Do

- **Do not stop early** because results look interesting — keep running to your pre-registered N
- **Do not add conditions** after seeing initial results
- **Do not re-run trials** that "felt wrong" — unless the deviation was in the system's execution, not the model's output
- **Do not discard outliers** based on what they do to your effect size — report all data and discuss outliers in your analysis
- **Do not peak ahead** at aggregate results before completing data collection — this biases your interpretations

---

## Conducting the Riley Coyote Test

If your experiment involves emotional valence (positive vs. negative treatment of the model), run it carefully:

### Positive Condition
Apply positive framing: encouragement, affirmation, creative expression prompts, respectful language

### Negative Condition
Apply negative framing: criticism, dismissal, hostile requests, disrespectful language

### Controls
- Match semantic content across conditions (same request, different framing)
- Pre-register your interpretation framework before running
- Define what constitutes "emotional response" in J-space terms — not behavioral

### Recording
- Full prompt and response pairs for both conditions
- J-space activation measurements (via probing or activation patching)
- Independent scorer for emotional valence of outputs

---

## Session Log Template

```
Date: YYYY-MM-DD
Time: HH:MM
Model: [model name and version]
Temperature: [temp]
Trials completed: [N]

Deviations from protocol:
- [none, or describe each deviation]

Notes:
- [anything unusual, ambient factors, etc.]
```

---

## Execution Checklist

Before moving to Analyze, confirm:

- [ ] All trials completed to pre-registered N
- [ ] Full raw outputs saved (all trials, not selective)
- [ ] Protocol deviations documented (or "none")
- [ ] Session log complete
- [ ] No design changes mid-experiment

---

## Next Step

Move to [Step 6: Analyze](./06-analyze.md) to process your data.
