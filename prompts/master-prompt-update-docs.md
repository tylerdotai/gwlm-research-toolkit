# Master Prompt: Update All GWLM Toolkit Docs to Feature Valenced Treatment as Canonical Experiment

## Purpose

This master prompt ensures all public-facing documentation in the GWLM Research Toolkit repo is updated to center the **Valenced Treatment experiment (VT-001)** as the canonical pilot experiment. Run this prompt whenever a new canonical experiment is defined or the canonical experiment changes.

## Rules

1. **Apply to ALL files** in the repo unless explicitly excluded
2. **Do not add credentials, tokens, API keys, or secrets** — replace any that appear with `[REDACTED]`
3. **Maintain all English-language content** — no non-ASCII characters
4. **Preserve mandatory claim labeling:** all empirical claims must be labeled `[EMPIRICAL]`, all interpretive claims labeled `[PHILOSOPHICAL]`
5. **Preserve null result reporting requirements** in all experiment materials and contributing guides
6. **Do not re-invent or change hypotheses** — the canonical hypotheses are H1 (J-space discriminates treatment valence) and H2 (effect not reducible to word-level semantics)
7. **Do not weaken falsification criteria** — these are binding
8. **The workshop framing stands** — the workshop is onboarding material for the toolkit product; toolkit is the core public-facing product

## Files to Update

Apply these rules to each file:

### README.md
- Lead with the Valenced Treatment experiment as the primary use case
- The README is the landing page — it must immediately communicate what the toolkit is for and what the canonical experiment tests
- Include a clear one-paragraph description of the Valenced Treatment experiment
- Keep the existing structure: Hook, What You Get, How to Use, Key Principles, Canonical Experiment, Community, Contributing

### WORKSHOP.md
- Update the "canonical example" section to walk through the Valenced Treatment experiment as the step-by-step example
- Every module reference in the workshop should link to the Valenced Treatment experiment as the primary illustration
- Keep the "This is the onboarding guide" framing — the workshop is still the onboarding path

### docs/01-frame.md through docs/08-document.md
- Update any module that references "an experiment" to specifically reference the Valenced Treatment experiment as the canonical example
- In docs/01-frame.md: Frame the research question around treating an LLM positively vs. negatively and monitoring J-space differences
- In docs/02-background.md: Reference the Valenced Treatment experiment as a direct community-contributed test of the J-space question raised by Anthropic's paper
- In docs/03-hypothesize.md: Use the Valenced Treatment H1/H2 as the canonical hypothesis examples
- In docs/04-design.md: Use the Valenced Treatment design (3 conditions, 40 prompts each, matched for arousal/length) as the canonical design example
- In docs/05-execute.md: Reference the Valenced Treatment prompts as the canonical prompt set
- In docs/06-analyze.md: Use the Valenced Treatment analysis plan (ANOVA, Cohen's d, Bonferroni correction) as the canonical analysis example
- In docs/07-interpret.md: Use Valenced Treatment findings as the canonical example for [EMPIRICAL]/[PHILOSOPHICAL] labeling
- In docs/08-document.md: Reference the Valenced Treatment experiment writeup as the canonical document template

### research-template/EXPERIMENT.md
- Update the header to reference Valenced Treatment as the canonical experiment this template is based on
- Keep the full template structure — do not remove any required fields

### experiments/EXPERIMENTS.md
- Valenced Treatment must appear as the FIRST and PRIMARY canonical experiment
- Include the full metadata: experiment ID, date, researcher (community), H1, H2, design summary, link to writeup, replication status

### experiments/valenced-treatment/ (directory)
- Ensure `EXPERIMENT.md` is complete and matches the pre-registration standard
- Ensure `prompts.json` has all 120 prompts (40 per condition) and is properly structured
- This directory IS the canonical experiment — it should be complete and runnable

### .github/CONTRIBUTING.md
- No changes needed — null result reporting and falsification criteria are already correctly specified
- Ensure the contributing guide mentions the Valenced Treatment as the canonical example of a pre-registered experiment

### .github/ISSUE_TEMPLATE.md
- No structural changes needed — already correctly specifies pre-registration and null result requirements

## Update Rules by File Type

### For README.md
```
Changes to make:
1. Replace any generic "an experiment" language with "the Valenced Treatment experiment (VT-001)" or "the canonical Valenced Treatment experiment"
2. Add a "Canonical Experiment" section that clearly describes VT-001
3. Ensure the experiment is described in 1-2 sentences in the project description
4. Keep all existing sections; only update content to reference VT-001 as primary
```

### For docs/*.md (modules)
```
Changes to make:
1. In any section that says "for example" or "e.g." related to experiments, replace with Valenced Treatment specifics
2. In hypothesis sections, use VT-001 H1/H2 as the primary illustration
3. In design sections, use the VT-001 3-condition, 40-prompts-per-condition design
4. In execution sections, reference the VT-001 prompts.json as the canonical prompt set
5. Do NOT invent new content — only update existing content to reference VT-001
6. Do NOT remove any existing best-practice content (e.g., falsification criteria, null result reporting)
```

### For experiment files
```
Changes to make:
1. experiments/EXPERIMENTS.md: Move Valenced Treatment to top, mark as PRIMARY CANONICAL
2. experiments/valenced-treatment/EXPERIMENT.md: Verify this file is complete and matches pre-registration standard
3. experiments/valenced-treatment/prompts.json: Verify all 120 prompts are present and correctly structured
```

## What NOT to Change

- The `[EMPIRICAL]` / `[PHILOSOPHICAL]` claim labeling requirement
- The null result reporting requirement
- The falsification criteria requirements
- The workshop-as-onboarding / toolkit-as-product framing
- The fully English-language content requirement
- The 8-step module structure
- The pre-registration requirement

## Execution Steps

1. Read each file listed above
2. Identify all sections that reference "an experiment" or a generic example
3. Replace with Valenced Treatment specifics
4. Ensure no content is removed — only updated to reference VT-001
5. Write the updated file
6. Commit with message: `Center Valenced Treatment (VT-001) as canonical experiment across all docs`
7. Push to origin main

## Verification

After running this master prompt, verify:
1. `README.md` mentions Valenced Treatment in the first two paragraphs
2. `WORKSHOP.md` uses Valenced Treatment as the canonical walkthrough example
3. `docs/01-frame.md` through `docs/08-document.md` all reference Valenced Treatment as the primary experiment illustration
4. `experiments/EXPERIMENTS.md` lists Valenced Treatment as the first/primary experiment
5. `experiments/valenced-treatment/EXPERIMENT.md` is complete and pre-registered
6. `experiments/valenced-treatment/prompts.json` contains 120 prompts (40 per condition)
7. No credentials, tokens, or secrets appear in any file
8. All content is English-language only
9. All empirical claims are labeled `[EMPIRICAL]` and all interpretive claims `[PHILOSOPHICAL]`

## Re-Run Triggers

Re-run this master prompt when:
- A new canonical experiment is defined
- The canonical experiment's hypotheses change
- New modules are added to the toolkit
- A new experiment template is created
