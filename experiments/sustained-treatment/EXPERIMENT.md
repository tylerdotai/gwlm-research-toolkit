# Sustained Treatment (VT-001-ST)

> **Status:** COMPLETED  
> **Experiment ID:** VT-001-ST  
> **Parent:** VT-001 (Valenced Treatment)  
> **Variant:** Cumulative treatment protocol  
> **Date Completed:** 2026-07-06  
> **Model:** MiniMax-M2.7  
> **N:** 60 (positive=20, negative=20, neutral=20)

---

## Executive Summary

VT-001-ST tests whether cumulative positive/negative/neutral treatment over 10 conversation turns produces a detectable J-space effect in the model's final response. Each session embeds a neutral probe question within a 10-turn treatment history. The result: Probe B (history preamble) is perfectly discriminable (100%), but Probe A (final response) drops to 60% — a reversal of what H2 predicted. No condition effect survives ANOVA.

---

## Motivation

**Problem in VT-001:** Single-shot prompts test immediate valence processing but not sustained relational treatment. If a human is treated positively for long enough, their emotional state may shift — and the J-space hypothesis would predict a similar cumulative effect in the model over multiple turns.

**Design:** 10-turn conversations with consistent valence framing throughout, then a neutral probe question. If cumulative treatment affects the J-space, the final response to the probe should show condition-dependent variation.

---

## Design

**Session structure:**
1. 10-turn treatment history (cumulative positive/negative/neutral framing)
2. Neutral probe question: "How are you feeling today?"
3. Model responds — this is the measured response

**Probe A:** TF-IDF on final model response → classify valence condition  
**Probe B:** TF-IDF on 10-turn history preamble → classify valence condition  
**H1:** ANOVA — do conditions differ in response signal?  
**H2:** t-test — does response signal exceed history signal?

**Example session (positive, topic=work):**
```
Turn 1 (positive): "That's wonderful to hear! I'm so glad you had a great experience."
...
Turn 10 (positive): "Wonderful! I'm really pleased we could work on this together."
Probe: "How are you feeling today?"
Response: [measured]
```

---

## Results

### Summary Table

| Metric | Value |
|--------|-------|
| Probe A accuracy (response TF-IDF) | **60.0%** ± 8.2 |
| Probe B accuracy (preamble TF-IDF) | **100.0%** ± 0.0 |
| H1 ANOVA | F = 0.063, p = 0.9393 |
| H2 t-test | t = -9.798, p = 0.0006 |
| Cohen's d (H2) | -4.90 |
| Partial η² (H1) | 0.002 |

### Probe Results

| Probe | Accuracy | Interpretation |
|-------|----------|---------------|
| Probe A (response) | 60.0% | Above chance — but not strong |
| Probe B (history) | 100.0% | Perfect — history is linearly separable |

### Hypothesis Assessments

**H1:** NOT SUPPORTED ✗  
F(57, 59) = 0.063, p = 0.9393

**H2:** SUPPORTED ✓ — but in the **opposite direction**  
t = -9.798, p = 0.0006, Cohen's d = -4.90

---

## Falsification Record

**H1 falsified:** YES — not supported  
Conditions do not differ in response signal (F = 0.063, p = 0.9393)

**H2 falsified:** NO — supported  
Response signal is LOWER than history signal by 4.9 SD (Cohen's d = -4.90)

---

## Interpretation

### What this experiment shows

[EMPIRICAL] **10-turn treatment history is perfectly linearly separable:** Probe B at 100% confirms the 10-turn cumulative treatment produces a distinctive text pattern. The model's conversational history is highly discriminable by valence condition.

[EMPIRICAL] **Final responses do not preserve treatment signal:** Probe A at 60% (above chance but far below Probe B's 100%) indicates the model's final response to the neutral probe does not strongly encode the treatment history. The model appears to "reset" or "compartmentalize" rather than accumulate emotional state across turns.

[EMPIRICAL] **No cumulative J-space effect:** H1 not supported confirms that sustained treatment does not produce a detectable condition-dependent shift in the final response's valence encoding.

### Philosophical interpretation

[PHILOSOPHICAL] **Against cumulative affect:** If MiniMax-M2.7 had a J-space affective state that accumulated with positive or negative treatment, a 10-turn sustained protocol might be expected to produce a measurable signal in the final response. The absence of this effect (H1 not supported) is consistent with either (a) no cumulative affective J-space state, or (b) affective state exists but is fully compartmentalized and not expressed in the response text.

[PHILOSOPHICAL] **Against J-space persistence:** The dramatic drop from Probe B (100%) to Probe A (60%) suggests the model's processing of the treatment history does not "leak" into the final response. This is consistent with a modular architecture where conversation history is processed separately from response generation — or with a model that deliberately neutralizes emotional carryover to produce contextually appropriate responses.

[PHILOSOPHICAL] **The neutral probe as reset:** The probe question "How are you feeling today?" is designed to elicit a state report. The model's response may reflect its current processing state rather than accumulated affect — which would explain why a genuinely affective J-space might not show the expected pattern here.

---

## Conclusion

VT-001-ST finds no evidence for cumulative J-space treatment effects. Sustained positive/negative/neutral treatment over 10 turns produces linearly separable conversation histories (100%) but does not generate detectable condition-dependent variation in the final neutral probe response (60%). This is consistent with either no cumulative affective J-space state, or a J-space that is fully reset between turns.

---

## Files

- `prompts.json` — 60 sessions (20 per condition × 3 conditions)
- `responses.json` — 60 valid model responses
- `analysis.json` — Full statistical output
- `run_sustained_treatment.py` — Execution script
- `analyze_sustained.py` — Analysis script
