# Notes Screen

The list of notes, its rows and its [reminder badges][g-reminder-badge].

## Rows

How a row reads.

### UI-NOTES-01
A row shows the note's title (**01**) and its date (**02**).

- **01** The title is the note's first line, truncated to one line.
- **02** The date reads `{Today|Yesterday}` for those days and `{Mon D}` otherwise.

### UI-NOTES-02
A row carries a [reminder badge][g-reminder-badge] when the note has pending reminders ([REMIND-04]).

- **01** The badge shows the count, capped as below, following the [platform guidance][hig].

  | Count | Shows |
  | --- | --- |
  | 1 to 9 | The count |
  | 10 or more | `9+` |

## States

### UI-NOTES-03
The list shows a stale notice while it is out of date, worded by cause.

| Cause | Notice |
| --- | --- |
| Offline | `Showing saved notes` |
| Sync failed | `Could not refresh` |

- **01** The notice sits above the first row.
- **02** It stays until the list next refreshes.

> **Known difference — LumenNotes iOS:** the notice is missing on first launch.

### UI-NOTES-04
The empty state reads `No notes yet` with a prompt to write one.

[REMIND-04]: ../../requirements/features/reminders.md#remind-04
[hig]: https://example.com/guidance/badges
[g-reminder-badge]: ../glossary.md#reminder-badge
