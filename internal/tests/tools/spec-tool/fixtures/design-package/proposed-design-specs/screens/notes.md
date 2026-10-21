# Notes Screen

The list of notes, its rows and its [reminder badges][g-reminder-badge].

## Rows

How a row reads.

### UI-NOTES-01
A row shows the note's title (**01**) and its date (**02**).

- **01** The title is the note's first line, truncated to one line.
- **02** The date reads `{Today|Yesterday}` for those days, the weekday name within the last week, and `{Mon D}` otherwise.

### UI-NOTES-02
A row carries a [reminder badge][g-reminder-badge] when the note has pending reminders ([REMIND-04]).

- **01** The badge shows the count, capped as below, following the [platform guidance][hig].

  | Count | Reads |
  | --- | --- |
  | 10 or more | `9+` |
  | 1 to 9 | The count |

## States

### UI-NOTES-03 (retired)
Superseded by [UI-LIST-01], which every list screen shares.

[REMIND-04]: ../../../requirements/features/reminders.md#remind-04
[hig]: https://example.com/guidance/badges-2026
[UI-LIST-01]: list-screen.md#ui-list-01
[g-reminder-badge]: glossary.md#reminder-badge
