# Workflow Stage

This file covers [notebook][g-notebook] stages, the hybrid [Inbox stage][g-inbox-stage] and schedule, and the conditions that call for the owner's attention.

## Stages

What the stages are, what each holds, and which are terminal.

### STAGE-01
A workflow stage identifies the current phase or outcome of a [notebook][g-notebook], from its first notes through to finished work or a deleted [notebook][g-notebook]. Publication proceeds through a reviewer's approval or by the owner sharing a link directly. The stages, in this order:

| Stage | Holds | Terminal |
| --- | --- | --- |
| Inbox | [Notebooks][g-notebook] that have not yet left their first stage; also the owner's reminder schedule (**01**) | No |
| Drafting | [Notebooks][g-notebook] awaiting further writing after a reminder (**02**) | No |
| Approved | [Notebooks][g-notebook] whose reviewer has signed off the text | No |
| Published | [Notebooks][g-notebook] visible to readers through a shared link rather than a personal invitation | No |
| Locked | [Notebooks][g-notebook] shared through a link whose text is frozen for editing | No |
| Archived | [Notebooks][g-notebook] whose work has finished | Yes ([STAGE-03]) |
| Deleted | [Notebooks][g-notebook] that will not be kept by the owner | Yes ([STAGE-03]) |

- **01** A [notebook][g-notebook] starts in Inbox. This stage also serves as the owner's reminder schedule, including upcoming reminders for [notebooks][g-notebook] in downstream stages ([REMINDER-26], [LIST-02], [LIST-03]). A [notebook][g-notebook] with a reminder in a downstream stage appears in both Inbox and its current stage; its appearance in the schedule does not change its current stage ([STAGE-05]).
- **02** A [notebook][g-notebook] that remains in Inbox after its reminder is completed transitions to Drafting on the next calendar day ([REMINDER-05], [STAGE-12]).

### STAGE-02 (retired)
Superseded by the stage table in [STAGE-01].

### STAGE-03
Archived and Deleted are terminal: an entry that reaches either is finished with, and the owner is not
expected to act on it again.

- **01** A [notebook][g-notebook] in Archived or Deleted has no reminder available in the app.

## Entries

What every entry in a stage carries, and how an entry relates to a reminder.

### STAGE-04
Every entry in a stage names a collaborator and a note title ([PERSON-05]), and carries the date the
note reached that stage. That date is a calendar day with no time of day attached.

### STAGE-05
A [notebook][g-notebook] has one current workflow stage. When its stage changes, it leaves its previous stage. A reminder for that [notebook][g-notebook] can also appear in the Inbox schedule without changing the [notebook][g-notebook]'s current stage ([STAGE-01-01]).

### STAGE-06
Every entry has an identifier that is stable while it remains in the workflow, so that the same
note is recognizable from one viewing to the next.

### STAGE-07 (retired)
Superseded by [STAGE-16] and [STAGE-03-01].

### STAGE-16
A reminder associated with a [notebook][g-notebook] describes the same collaborator and note ([NOTEBOOK-02]). A change in the [notebook][g-notebook]'s stage does not change that association.

## Attention

When an entry calls for the owner's attention, and how counts are reported.

### STAGE-08
A [notebook][g-notebook] in Drafting, Approved, Published or Locked with upcoming reminder information always calls for the owner's attention, whatever its stage date says ([STAGE-16]). Its appearance in the Inbox schedule follows [STAGE-10] instead.

### STAGE-09
A [notebook][g-notebook] without upcoming reminder information calls for attention on terms set by its stage, or by an expiring suggestion (**01**).

| Stage | Calls for attention |
| --- | --- |
| Drafting | Always |
| Approved | Once more than ten days have passed since its stage date |
| Published | Once more than twenty-one days have passed since its stage date |
| Locked | Never |
| Archived | Never |
| Deleted | Never |

- **01** A [notebook][g-notebook] with an [active suggestion][g-active-suggestion] that expires within two days calls for attention whatever its stage, except in a [terminal stage][g-terminal-stage].

### STAGE-10
An entry in the [Inbox stage][g-inbox-stage] calls for attention when the reminder it stands for is shown
as overdue ([REMINDER-19], [LIST-09]). A reminder that is snoozed, or whose completion is being
synced, shows that instead and so does not count.

### STAGE-11
Each stage's entry count and attention count must be reportable without opening that stage.

- **01** Inbox counts the upcoming reminders in its schedule; other stages count the [notebooks][g-notebook] they hold.
- **02** A [notebook][g-notebook] represented in Inbox and a downstream stage contributes to both counts, and attention is determined separately under each stage's rules ([STAGE-08], [STAGE-09], [STAGE-10], [STAGE-01-01]).

## Sync Service Ownership

The sync service decides the workflow; the app reports it.

### STAGE-12
An owner's workflow is the sync service's to determine. An owner cannot add an entry to a stage, move
an entry between stages, or remove one.

### STAGE-13
A [workflow entry][g-workflow-entry] the sync service stops sending is gone: unlike a reminder, a [workflow entry][g-workflow-entry] has
no retention period and leaves the owner's workflow as soon as it leaves the sync service's
([REMINDER-08]).

### STAGE-14
A [workflow entry][g-workflow-entry] that cannot be understood is left out, and the rest of its stage is shown as usual.
One unreadable entry must never cost the owner sight of the stage it belongs to.

[STAGE-01]: #stage-01
[STAGE-01-01]: #stage-01
[STAGE-03]: #stage-03
[STAGE-03-01]: #stage-03
[STAGE-05]: #stage-05
[STAGE-08]: #stage-08
[STAGE-09]: #stage-09
[STAGE-10]: #stage-10
[STAGE-12]: #stage-12
[STAGE-16]: #stage-16
[PERSON-05]: owner-and-collaborator.md#person-05
[REMINDER-05]: reminder.md#reminder-05
[REMINDER-08]: reminder.md#reminder-08
[REMINDER-19]: reminder.md#reminder-19
[REMINDER-26]: reminder.md#reminder-26
[LIST-02]: ../apps/lumennotes/reminder-list.md#list-02
[LIST-03]: ../apps/lumennotes/reminder-list.md#list-03
[LIST-09]: ../apps/lumennotes/reminder-list.md#list-09
[NOTEBOOK-02]: notebook.md#notebook-02
[g-notebook]: ../glossary.md#notebook
[g-inbox-stage]: ../glossary.md#inbox-stage
[g-workflow-entry]: ../glossary.md#workflow-entry
[g-active-suggestion]: ../glossary.md#active-suggestion
[g-terminal-stage]: ../glossary.md#terminal-stage
