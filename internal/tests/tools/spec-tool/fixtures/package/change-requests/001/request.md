Change Request Status: Proposed
Reviewer Response:

# Attention For Notebooks With Suggestions

## Goal

Let the home view order notebooks by how much they need the owner, which needs attention to account for expiring suggestions, not only stage.

## Requested Changes

- R1 modify requirement: [STAGE-09]
  - **Description** Add a rule: a notebook with an active suggestion that expires within two days calls for attention whatever its stage, except in a terminal stage. The statement mentions the new rule.
  - **Justification** Design: the home view orders notebooks by urgency, and a suggestion expiring tomorrow is more urgent than a Drafting entry with no suggestions. The stage-only terms give that ordering no spec to stand on.
  - **Touches** domains/workflow-stage.md

[STAGE-09]: ../../proposed-product-specs/domains/workflow-stage.md#stage-09
