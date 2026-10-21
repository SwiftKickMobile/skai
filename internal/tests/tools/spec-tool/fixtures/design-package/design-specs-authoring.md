# Design Specs — Notes List

## Goal

Bring the notes list's date format, badge table and stale notice in line with the approved designs.

## Discussion

### Date Format

- [x] D1 [Proposal] Show the weekday name within the last week
  - **Decision** Approved.

## Spec Changes

- S1 modify rule: [UI-NOTES-01.02]
  - **Justification** Resolved decision: [D1]
  - **Touches** [notes][s-notes]

- S2 modify item: [UI-NOTES-02]
  - **Justification** Design: `notes — badge counts`; the badge follows the 2026 guidance.
  - **Touches** [notes][s-notes]

- S3 retire item: [UI-NOTES-03]
  - **Justification** Catalog: the stale notice is shared by every list screen, so it moves to [UI-LIST-01].
  - **Touches** [notes][s-notes]

- S4 add spec file: [List Screen][s-list]
  - **Justification** Catalog: reuse on a second screen would duplicate the rule.
  - **Touches** [list-screen][s-list], [screens][s-screens]

- S5 add glossary entry: [Stale notice][s-glossary]
  - **Justification** Catalog: now cross-cutting.
  - **Touches** [glossary][s-glossary]

- S6 modify index line: [trash][s-screens]
  - **Justification** Catalog: the trash list's rules now live in `list-screen.md`; the line's text stands.
  - **Touches** [screens][s-screens]

- S7 move item: [UI-NOTES-04]
  - **Justification** Catalog: the empty state is shared by every list screen.
  - **Touches** [notes][s-notes] → [list-screen][s-list]

- S9 move glossary entry: [Reminder badge][s-glossary]
  - **Justification** Catalog: only the notes screens use the badge, so the term belongs with them.
  - **Touches** [glossary][s-glossary] → [screens-glossary][s-screens-glossary]

- S8 modify item: [UI-NOTES-04]
  - **Justification** Design: `trash — empty` adds the trash wording.
  - **Touches** [list-screen][s-list]

## Decision Log

- D1 decided — Approved.

[UI-NOTES-01.02]: proposed-design-specs/screens/notes.md#ui-notes-01
[UI-NOTES-02]: proposed-design-specs/screens/notes.md#ui-notes-02
[UI-NOTES-03]: proposed-design-specs/screens/notes.md#ui-notes-03-retired
[UI-LIST-01]: proposed-design-specs/screens/list-screen.md#ui-list-01
[UI-NOTES-04]: proposed-design-specs/screens/list-screen.md#ui-notes-04
[s-notes]: proposed-design-specs/screens/notes.md
[s-list]: proposed-design-specs/screens/list-screen.md
[s-screens]: proposed-design-specs/screens/_screens.md
[s-glossary]: proposed-design-specs/glossary.md
[s-screens-glossary]: proposed-design-specs/screens/glossary.md
[D1]: #date-format
