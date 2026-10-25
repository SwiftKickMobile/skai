# Product Specs — Suggestions

## Goal

Model the notebook, its stages and collaborator suggestions so the app can show an owner the suggestions waiting on each notebook.

## Situations

- An owner opens a [notebook][g-notebook] in Drafting that has two [active suggestions][g-active-suggestion]
  ([STAGE-01], [SUGGESTION-03]): the home view orders it by the nearer expiration.
- A suggestion arrives without an expiration date ([SUGGESTION-08]): it stays active under option A of D2,
  and the reviewer's view is in [request 001][request-001].

## Inputs

- The fixtures' catalog files.

## Mode

Scoped change.

## Discussion

### Stage Definitions

- [x] D1 [Proposal] Define the seven stages as one table under STAGE-01
  - **Concern** The catalog spreads the stage list and the stage meanings across [STAGE-01] and [STAGE-02], and the Suggestions work needs per-stage facts such as which stages are terminal ([STAGE-03]).
  - **Proposal** One table with stage, what it holds and whether it is terminal; stage-specific rules as sub-rules.
  - **Why** A reader gets every stage fact in one place and each row stays citable through the item.
  - **Decision** Approved.

### Active Suggestions

- [ ] D2 [Tradeoff] Whether a missing expiration date keeps a suggestion active
  - **Concern** The sync service does not always supply an expiration date, and [SUGGESTION-03] makes
    expiration one of the conditions that end activity.
  - **Options**
    - A — Missing expiration leaves a Submitted suggestion active.
    - B — Missing expiration makes activity unconfirmed, and the suggestion is shown with no activity
      state until a date arrives.
  - **Detail** Of the sampled suggestions, one in eight arrived without an expiration date; the reviewer raised the same in [request 001][request-001].
  - **Proposal** A.
  - **Why** Treating absence as inactivity would hide suggestions the owner can still consider.

### Suggestion Expiry Window

- [ ] D3 [Proposal] How long a Submitted suggestion stays active with no response
  - **Concern** [SUGGESTION-08] needs a window and the sync service has not confirmed one.
  - **Proposal** 14 days, the figure in the brief.
  - **Gap** 14 days stands in until the sync service confirms.

## Requirement Changes

- R1 modify requirement: [STAGE-01]
  - **Description** Define what a stage is and list the stages as a table with what each holds and whether it is terminal; the Inbox schedule role and the Drafting transition become sub-rules.
  - **Justification** Resolved decision: [D1]
  - **Touches** domains/workflow-stage.md

- R2 retire requirement: [STAGE-02]
  - **Description** ~~Inbox holds the notes the owner is due to revisit…~~ Superseded by the stage table in [STAGE-01].
  - **Justification** Resolved decision: [D1]
  - **Touches** domains/workflow-stage.md

- R3 modify requirement: [STAGE-03]
  - **Description** Adds the rule that a terminal-stage notebook has no reminder in the app.
  - **Justification** Supervisor input: the supervisor confirmed terminal-stage notebooks never have a reminder.
  - **Touches** domains/workflow-stage.md

- R4 add file: domains/suggestion.md
  - **Description** The collaborator suggestion: identity, activity, word counts and dates, reissue and replacement. Prefix `SUGGESTION-`.
  - **Justification** Supervisor input: the agreed suggestion information list.
  - **Touches** domains/suggestion.md

- R5 modify requirement: [STAGE-05]
  - **Justification** Resolved decision: [D1] — restated for a notebook that also appears in the Inbox schedule.
  - **Touches** domains/workflow-stage.md

- R6 retire requirement: [STAGE-07]
  - **Justification** Resolved decision: [D1] — split into [STAGE-16] and the terminal-stage rule under [STAGE-03].
  - **Touches** domains/workflow-stage.md

- R7 add requirement: [STAGE-16]
  - **Justification** Resolved decision: [D1]
  - **Touches** domains/workflow-stage.md

- R8 modify requirement: [STAGE-08]
  - **Justification** Catalog: cites [STAGE-16] in place of the retired STAGE-07.
  - **Touches** domains/workflow-stage.md

- R9 modify requirement: [STAGE-09]
  - **Justification** Resolved decision: [D1] — the per-stage terms become a table.
  - **Touches** domains/workflow-stage.md

- R10 modify requirement: [STAGE-11]
  - **Justification** Resolved decision: [D1] — the counts become sub-rules.
  - **Touches** domains/workflow-stage.md

- R11 add glossary entry: Active suggestion
  - **Justification** Supervisor input: the agreed suggestion information list.
  - **Touches** glossary.md

- R12 add glossary entry: Estimated net change
  - **Justification** Supervisor input: the agreed suggestion information list.
  - **Touches** glossary.md

- R13 add glossary entry: Inbox stage
  - **Justification** Resolved decision: [D1]
  - **Touches** glossary.md

- R14 add glossary entry: Notebook
  - **Justification** Supervisor input: the notebook is the thing a stage holds.
  - **Touches** glossary.md

- R15 add glossary entry: Superseded suggestion
  - **Justification** Supervisor input: the agreed suggestion information list.
  - **Touches** glossary.md

- R16 modify glossary entry: Workflow entry
  - **Justification** Catalog: defined in terms of the notebook.
  - **Touches** glossary.md

- R17 modify glossary entry: Terminal stage
  - **Justification** Support input: the web app calls it done.
  - **Touches** glossary.md

## Assumptions and TODOs

- D2 is drafted under option A.

## Out of scope

- Suggestion notifications.

## Decision Log

- D1 decided — Approved.
- D3 gap — 14 days stands in until the sync service confirms.

[STAGE-01]: proposed-product-specs/domains/workflow-stage.md#stage-01
[STAGE-02]: proposed-product-specs/domains/workflow-stage.md#stage-02-retired
[STAGE-03]: proposed-product-specs/domains/workflow-stage.md#stage-03
[STAGE-05]: proposed-product-specs/domains/workflow-stage.md#stage-05
[STAGE-07]: proposed-product-specs/domains/workflow-stage.md#stage-07-retired
[STAGE-08]: proposed-product-specs/domains/workflow-stage.md#stage-08
[STAGE-09]: proposed-product-specs/domains/workflow-stage.md#stage-09
[STAGE-11]: proposed-product-specs/domains/workflow-stage.md#stage-11
[STAGE-16]: proposed-product-specs/domains/workflow-stage.md#stage-16
[SUGGESTION-03]: proposed-product-specs/domains/suggestion.md#suggestion-03
[SUGGESTION-08]: proposed-product-specs/domains/suggestion.md#suggestion-08
[g-notebook]: proposed-product-specs/glossary.md#notebook
[g-active-suggestion]: proposed-product-specs/glossary.md#active-suggestion
[request-001]: change-requests/001/product-specs-authoring.md
[D1]: #stage-definitions
