Change Request Status: Proposed
Reviewer Response:

# Suggestion Reminder Lead Time

## Goal

Give the owner a reminder before a suggestion expires, which needs the suggestion to carry a lead time.

## Requested Changes

- R1 add requirement: [SUGGESTION-13][suggestion]
  - **Justification** Design: the suggestion card shows a reminder two days before expiration, and no requirement says the suggestion carries that lead time.
  - **Touches** domains/suggestion.md

- R2 modify requirement: [SUGGESTION-08]
  - **Justification** Design: the dates table gains a row for the reminder date derived from the lead time.
  - **Touches** domains/suggestion.md

[suggestion]: ../../proposed-product-specs/domains/suggestion.md
[SUGGESTION-08]: ../../proposed-product-specs/domains/suggestion.md#suggestion-08
