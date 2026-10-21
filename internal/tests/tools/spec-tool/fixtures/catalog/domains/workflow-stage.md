# Workflow Stage

An owner's workflow is every note they are working on, from the first reminder through to a note
that is archived or deleted. A stage is one step of that progression. This file covers what the
stages are, what belongs in each, and what makes an entry in a stage call for the owner's
attention.

## Stages

### STAGE-01
An owner's workflow is divided into seven stages, in this order: Inbox, Drafting, Approved,
Published, Locked, Archived, Deleted.

### STAGE-02
Inbox holds the notes the owner is due to revisit or has revisited without a decision. Drafting
holds those awaiting further writing. Approved holds those a reviewer has signed off. Published
holds those visible to readers. Locked holds those frozen for editing. Archived holds finished
notes. Deleted holds notes that will not be kept.

### STAGE-03
Archived and Deleted are terminal: an entry that reaches either is finished with, and the owner is not
expected to act on it again.

## Entries

### STAGE-04
Every entry in a stage names a collaborator and a note title ([PERSON-05]), and carries the date the
note reached that stage. That date is a calendar day with no time of day attached.

### STAGE-05
An entry appears in exactly one stage. An entry that moves to another stage leaves the stage it came
from.

### STAGE-06
Every entry has an identifier that is stable while it remains in the workflow, so that the same
note is recognizable from one viewing to the next.

### STAGE-07
An entry in any stage before Archived and Deleted may correspond to a reminder the owner holds
([REMINDER-01]), which happens when a reminder reaches a stage beyond Inbox while the owner
still has work outstanding on it. Where it does, the two describe the same note and the same
collaborator. A note the owner still has a reminder for never reaches a [terminal stage][g-terminal-stage] ([STAGE-03]).

## Attention

### STAGE-08
An entry in Drafting, Approved, Published or Locked that corresponds to a reminder always
calls for the owner's attention, whatever its stage date says, because the owner still has work
outstanding on that reminder ([STAGE-07]). Entries in the Inbox stage follow [STAGE-10] instead.

### STAGE-09
An entry that does not correspond to a reminder calls for attention on terms set by its stage:
every Drafting entry does; an Approved entry does once more than ten days have passed since its stage
date; a Published entry does once more than twenty-one days have passed; and a Locked, Archived
or Deleted entry never does.

### STAGE-10
An entry in the Inbox stage calls for attention when the reminder it stands for is shown
as overdue ([REMINDER-19], [LIST-09]). A reminder that is snoozed, or whose completion is being
synced, shows that instead and so does not count.

### STAGE-11
The number of entries in a stage, and how many of them call for attention, must both be reportable
per stage without opening the stage.

## Sync Service Ownership

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

[PERSON-05]: owner-and-collaborator.md#person-05
[REMINDER-01]: reminder.md#reminder-01
[STAGE-03]: #stage-03
[STAGE-07]: #stage-07
[STAGE-10]: #stage-10
[REMINDER-19]: reminder.md#reminder-19
[LIST-09]: ../apps/lumennotes/reminder-list.md#list-09
[REMINDER-08]: reminder.md#reminder-08
[g-terminal-stage]: ../glossary.md#terminal-stage
[g-workflow-entry]: ../glossary.md#workflow-entry
