# Product Specs — Suggestions (Broken Change List)

## Goal

A change list that does not match the drafts, for driving `check-changes` against `catalog/` and `package/proposed-product-specs/`: one entry names an unchanged item, one names an item that exists nowhere, and every other change in the drafts has no entry.

## Discussion

### Stage Definitions

- [x] D1 [Proposal] Define the seven stages as one table under STAGE-01
  - **Concern** The stage list is spread across two items.
  - **Decision** Approved.
  - **Decision** Approved again.
- [ ] D2 [Proposal] How long a Submitted suggestion stays active with no response
  - **Concern** The sync service has not confirmed a window.
  - **Gap** 14 days stands in until the sync service confirms.

## Requirement Changes

- R1 modify requirement: [STAGE-01]
  - **Justification** Resolved decision: D9
  - **Touches** domains/workflow-stage.md

- R2 modify requirement: [STAGE-04]
  - **Justification** Agent inference: names an item the drafts leave unchanged.
  - **Touches** domains/workflow-stage.md

- R3 retire requirement: [STAGE-99]
  - **Justification** Agent inference: names an item that is in neither the catalog nor the drafts.
  - **Touches** domains/workflow-stage.md

- R4 modify requirement: [STAGE-09-07]
  - **Justification** Agent inference: names a rule STAGE-09 does not have.
  - **Touches** domains/workflow-stage.md

- R5 add requirement: [STAGE-03]
  - **Justification** Agent inference: declares add for an item the drafts modify.
  - **Touches** domains/workflow-stage.md

- R6 retire requirement: [STAGE-16]
  - **Justification** Agent inference: declares retire for an item the drafts add.
  - **Touches** domains/workflow-stage.md

- R7 move requirement: [STAGE-05]
  - **Justification** Agent inference: declares move for an item that stays in its file, modified.
  - **Touches** domains/workflow-stage.md

- R8 add file: domains/workflow-stage.md
  - **Justification** Agent inference: declares add for a file the catalog already has.
  - **Touches** domains/workflow-stage.md

- R9 modify file: domains/suggestion.md
  - **Justification** Agent inference: declares modify for a file the catalog lacks.
  - **Touches** domains/suggestion.md

## Decision Log

- D1 gap — A stage table stands in.
- D9 decided — Approved.
not an entry

[STAGE-09-07]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-09
[STAGE-03]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-03
[STAGE-16]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-16
[STAGE-05]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-05
[STAGE-01]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-01
[STAGE-04]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-04
[STAGE-99]: ../package/proposed-product-specs/domains/workflow-stage.md#stage-99
