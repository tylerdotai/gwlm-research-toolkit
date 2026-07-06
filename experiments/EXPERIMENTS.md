# Community Experiments

> Results from the community. All experiments use the [GWLM Research Toolkit](../WORKSHOP.md).

---

## Canonical Experiments

### Valenced Treatment (VT-001)

**Status:** PRE-REGISTERED  
**Experiment ID:** VT-001  
**Date:** 2026-07-06  
**Researcher:** Community (proposed via Anthropic Global Workspace X post comment)  
**H1:** J-space discriminates positive vs. negative relational treatment  
**H2:** J-space effect is not reducible to word-level semantics  
**Design:** 3 conditions (positive/negative/neutral), 40 prompts each, 120 total trials  
**Prompts:** `valenced-treatment/prompts.json`  
**Writeup:** `valenced-treatment/EXPERIMENT.md`

**Summary:** Tests whether the J-space exhibits discriminable activation patterns when an LLM is treated positively vs. negatively, and whether any such discrimination exceeds word-level emotional content. The canonical pilot experiment for this toolkit.

**Replication status:** PENDING

---

## How to Add Your Experiment

1. Pre-register your experiment using the [Experiment Template](../research-template/EXPERIMENT.md)
2. Open a pull request with `[PRE-REGISTERED]` in the title
3. Run your experiment
4. Complete the results section
5. Submit your findings

See [CONTRIBUTING.md](../.github/CONTRIBUTING.md) for full contribution guidelines.

---

## Null Results Policy

Null results are results. An experiment that fails to find an effect is still a valid contribution. Report null results with the same rigor as positive results. Do not re-run experiments to try to "find" a result.

---

## Replication Status Key

| Status | Meaning |
|--------|---------|
| PENDING | Pre-registered, not yet run |
| IN_PROGRESS | Currently being run |
| COMPLETED | Completed with results |
| NULL_RESULT | Completed, no effect found |
| FALSIFIED | H1 or H2 was falsified |
| REPLICATED | Independently replicated by another researcher |
| NOT_REPLICATED | Replication attempt failed |
