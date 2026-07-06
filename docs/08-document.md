# Module 08 — Document

## Writing It Up

Documentation is what makes your experiment reproducible. An experiment that cannot be reproduced is not science — it is an anecdote.

### Required Sections

Your experiment writeup (in `experiments/[experiment-name]/EXPERIMENT.md`) must include:

#### 1. Executive Summary (250 words max)
What did you test, what did you find, and what does it mean in one paragraph.

#### 2. Research Question
The specific question this experiment addresses. From [Module 01](./01-frame.md).

#### 3. Background
What was already known about this question. From [Module 02](./02-background.md).

#### 4. Hypotheses
H1 and H2 as stated before running. Include falsification criteria. From [Module 03](./03-hypothesize.md).

#### 5. Methods
Complete enough that another researcher could reproduce your experiment exactly:
- Model and version
- Temperature and generation settings
- Full prompt text (or reference to prompt file)
- Sample size and randomization procedure
- Analysis methods and software

#### 6. Results
All results, including null results and unexpected findings. From [Module 06](./06-analyze.md).

#### 7. Interpretation
Claims labeled `[EMPIRICAL]` or `[PHILOSOPHICAL]`. From [Module 07](./07-interpret.md).

#### 8. Limitations
What your design does not rule out. What threats to validity remain.

#### 9. Next Steps
What a follow-up experiment should test based on your findings.

#### 10. References
All cited literature, including Anthropic's J-space paper.

### Pre-Registration

Before running, commit your hypotheses and methods to the repository. This prevents inadvertent HARKing (Hypothesizing After Results are Known).

To pre-register:
1. Complete Sections 1-5 of your writeup
2. Create `experiments/[experiment-name]/EXPERIMENT.md` with your pre-registration
3. Open a PR or commit with "[PRE-REGISTERED]" in the title
4. Do not modify the pre-registration after opening the PR

### Null Results

Null results are results. Report them with the same rigor as positive results.

**Null results report template:**
```
H1 was not supported. Probe classifier accuracy for treatment valence was X% (SD=Y%),
not distinguishable from chance (33%). [Full statistical report.]

Post-hoc analysis suggests [possible explanation for null result].

This result suggests that [what the null result implies, framed as a finding].
```

Do not describe null results as "no findings" or "no effect" — they are findings.

### Updating the Experiment Catalog

After completing your experiment, update `experiments/EXPERIMENTS.md` with:
- Experiment name
- Date completed
- Summary of key finding
- Link to full writeup
- Replication status (original / replicated / not replicated / pending)

---

## Submitting to the Repository

1. Create your experiment directory: `experiments/[experiment-name]/`
2. Write `experiments/[experiment-name]/EXPERIMENT.md` following the template above
3. Include all raw data or a link to stored raw data (do not commit large activation files to git — store externally and link)
4. Submit a pull request with:
   - Title: `[Experiment] [Experiment Name] — [Summary Finding]`
   - Description: Brief motivation, method, and result
   - Checklists confirmed: pre-registration, null results policy, [EMPIRICAL]/[PHILOSOPHICAL] labeling

---

## After Publication

- Respond to questions from replicators
- Update your experiment if methodology issues are identified
- Publish in a peer-reviewed venue if the finding is significant
- Pre-register follow-up experiments building on your results

---

## When the Canonical Experiment Changes

If the canonical experiment (VT-001) changes, run the [Master Prompt: Update Docs](../prompts/master-prompt-update-docs.md) to consistently update all public-facing documentation.

---

## Next Step

Return to the [WORKSHOP.md](../WORKSHOP.md) to run another experiment, or use the [Master Prompt: Execute Valenced Treatment](../prompts/master-prompt-execute.md) to run the canonical VT-001 experiment.
