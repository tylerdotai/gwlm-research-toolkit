name: New Experiment
description: Submit a new GWLM experiment to the research toolkit
title: "[Experiment] "
labels: ["experiment"]
body:
  - type: markdown
    attributes:
      value: |
        ## Before Submitting

        - Have you followed the 8-step Workshop Guide?
        - Is your research question falsifiable?
        - Have you included effect sizes and confidence intervals?
        - Have you separated empirical from philosophical claims?

  - type: textarea
    id: research-question
    attributes:
      label: Research Question
      description: What precise question does your experiment address?
      placeholder: "Does the J-space exhibit elevated activation for novel vs. familiar inputs?"
    validations:
      required: true

  - type: textarea
    id: hypothesis
    attributes:
      label: Hypothesis
      description: State H1 and H2 with falsification criteria
      placeholder: |
        **H1:** [prediction]
        **Falsification criterion:** [what would disprove this]
        **H2:** [alternative]
        **Falsification criterion:** [what would disprove this]
    validations:
      required: true

  - type: textarea
    id: method
    attributes:
      label: Method Summary
      description: Brief summary of your experimental design (full protocol goes in EXPERIMENT.md)
      placeholder: "N per condition, model used, key prompts, measurement approach"
    validations:
      required: true

  - type: textarea
    id: findings
    attributes:
      label: Key Findings
      description: What did you find? (Report null results too — "no effect found" is a finding)
      placeholder: "H1 supported / not supported. Effect size: d=X, 95% CI [X, X]"
    validations:
      required: true

  - type: textarea
    id: interpretation
    attributes:
      label: Interpretation
      description: Empirical vs. philosophical claims — use [EMPIRICAL] and [PHILOSOPHICAL] labels
      placeholder: |
        **[EMPIRICAL]** What the data shows...
        **[PHILOSOPHICAL]** What this might mean...
    validations:
      required: true

  - type: textarea
    id: limitations
    attributes:
      label: Limitations
      description: What threats to validity remain? What would you do differently?
    validations:
      required: true

  - type: textarea
    id: next-steps
    attributes:
      label: Next Steps
      description: What follow-up experiments does this suggest?
    validations:
      required: false
