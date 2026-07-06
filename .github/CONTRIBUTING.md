# Contributing to GWLM Research Toolkit

Welcome. We're building a rigorous, community-run research repository for experiments investigating the Global Workspace Theory and J-space in large language models.

---

## What Belongs Here

### Valid Contributions

- New experiments (following the Workshop Guide structure)
- Replication attempts of existing experiments (successful or not)
- Methodology improvements to existing protocols
- Analysis improvements or extensions
- Documentation improvements (clarity, completeness, examples)
- Bug reports on existing experiment documents

### Not Valid Contributions

- Philosophical arguments without empirical backing (post in Issues, don't file PRs)
- Reinterpretations of existing results that change the empirical record (edits to completed EXPERIMENT.md files are not permitted — add a follow-up experiment instead)
- Promotional content or advocacy for particular philosophical positions
- Results that skip the Workshop Guide steps (the 8-step structure exists for scientific rigor — all experiments must follow it)

---

## Process

### For New Experiments

1. **Fork the repo**
2. **Run the full workshop** — complete all 8 steps in order using the Workshop Guide
3. **Create your experiment document** at `experiments/[name]/EXPERIMENT.md`
4. **Update the experiment catalog** `experiments/EXPERIMENTS.md`
5. **Submit a PR** with a clear description of the experiment and findings

### For Replications

1. Fork the repo
2. Copy the experiment protocol from the original EXPERIMENT.md
3. Run it independently (do not look at the original results before completing your replication)
4. Create your replication document at `experiments/[name]-replication/EXPERIMENT.md`
5. Mark status as "Replication Attempt" in the catalog

### For Methodology Improvements

- File an Issue first describing the methodological concern
- If the concern is valid, the maintainer may create a discussion thread
- Do not submit PRs that change the scientific record of existing experiments

---

## Standards

### Scientific Rigor

- All claims must be supported by data
- Effect sizes and confidence intervals required — not just p-values
- Null results must be reported (not just significant findings)
- Pre-registration is encouraged but not required
- Post-hoc analysis must be labeled as post-hoc

### Documentation Standards

- Methods section must be complete enough to reproduce
- All prompts must be included verbatim
- All data must be available (or linked if too large for the repo)

### Philosophical Claims

- Empirical claims and philosophical claims must be clearly separated
- Use `[EMPIRICAL]` and `[PHILOSOPHICAL]` labels
- Do not present philosophical claims as empirical findings

---

## Code of Conduct

Be respectful. The intersection of AI consciousness research attracts strong opinions. Scientific disagreement is welcome. Ad hominem attacks are not.

---

## Questions?

Open an Issue with the `question` label.
