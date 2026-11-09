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

### Notes

- V01 modify screen: [notes](https://example.test/file?node-id=1-1)
  - **01** A `Pinned` group with its own header above the rest of the list — Resolved decision: D01
  - **02** The unread dot on each row goes[^1] — Supervisor input
  [^1]: **Gap:** D02. Placeholder: the group header shows no collapse control.
- V02 add state: [notes — empty pinned group](https://example.test/file?node-id=1-2)
  - **Description** The group with no pinned notes shows a hint line.[^2]
  - **Justification** Supervisor input
  [^2]: **Gap:** D02. Placeholder: the empty group does not collapse either.
### Note editor

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
