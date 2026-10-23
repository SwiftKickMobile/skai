# Design — Pinned Notes
[Review page](design-review.html)

## Goal

Pinned notes sit in their own group above the list.

## Inputs

- The notes brief ([brief](../brief.md)).

## Discussion

### Pinned notes

- [x] D01 [Proposal] Pinned notes sit in their own group above the list
  - **Concern** The brief says "pinned notes are easy to find" but not where they go.
  - **Proposal** A `Pinned` group with its own header above the rest of the list.
  - **Decision** Approved as proposed.
- [ ] D02 [Question] Does the group collapse?
  - **Concern** Nothing in the brief says.
  - **Gap** As drawn: it does not.

## Design Changes

- V01 modify screen: [notes](https://example.test/file?node-id=1-1)
  - **Description** A `Pinned` group with its own header above the rest of the list.
  - **Justification** Resolved decision: D01
- V02 add state: [notes — empty pinned group](https://example.test/file?node-id=1-2)
  - **Description** The group with no pinned notes shows a hint line.
  - **Justification** Supervisor input
- V03 remove state: notes — legacy pin glyph
  - **Description** The pin glyph on list rows goes.
  - **Justification** Resolved decision: D01
V04 add state: not an entry (no list marker)

## Assumptions and TODOs

- None.

## Out of scope

Nothing.

## Decision Log

- D01 decided — approved as proposed.
- D02 gap — not collapsible as drawn.
