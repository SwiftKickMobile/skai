# Collaborator Suggestion

This file defines individual collaborator suggestions, their [notebook][g-notebook] and collaborator associations, active status, reissue and replacement, and the meanings of their word counts and dates.

## Identity

### SUGGESTION-01
A suggestion represents one proposed edit by a collaborator for one [notebook][g-notebook] ([NOTEBOOK-01]). Proposed edits remain distinct even when they share the same collaborator and template ([SUGGESTION-11]). Suggestion information comes from the sync service, including its reported status when supplied ([SUGGESTION-STATUS-01]).

### SUGGESTION-02
A collaborator may make more than one suggestion for the same [notebook][g-notebook], including suggestions under different templates. Those suggestions remain distinct, and different templates may have [active suggestions][g-active-suggestion] at the same time ([SUGGESTION-03]).

### SUGGESTION-10
A suggestion's draft or final designation is the designation supplied with the suggestion. It is distinct from whether the suggestion is active or inactive ([SUGGESTION-03]).

## Activity

### SUGGESTION-03
A suggestion is active while it remains available for the owner to consider. Any of the following makes it inactive.

| Condition | Meaning |
| --- | --- |
| Expiration | Its expiration date ([SUGGESTION-08]) has passed |
| Supersession | Another suggestion has replaced it ([SUGGESTION-12]) |
| Withdrawal | The collaborator has withdrawn it |
| Reported outcome | It is reported as Accepted, Rejected, Expired, Reverted or Merged ([SUGGESTION-STATUS-03], [SUGGESTION-STATUS-04], [SUGGESTION-STATUS-05], [SUGGESTION-STATUS-06], [SUGGESTION-STATUS-07]) |

## Word Counts And Dates

### SUGGESTION-04
A suggestion carries these word counts, each with the meaning given here and no other.

| Count | Meaning |
| --- | --- |
| Current length estimate | The collaborator's estimate of the note's length in words; distinct from what the collaborator proposes (**01**) |
| Proposed length | The length the collaborator proposes under the named template (**02**) |
| Removed words | Words the suggestion deletes from the note |
| Moved words | Words the collaborator expects to relocate and discounts when estimating the owner's net change |
| Estimated net change | Proposed length less removed words and moved words (**03**) |

- **01** The current length estimate is never presented as the proposed length.
- **02** Where the proposed length covers only a first section, it means that first section, not the full length of a suggestion with possible later sections.
- **03** Estimated net change does not imply that other edits or formatting changes have been counted. Where the proposed length covers a first section, the net relates to that first section and does not include possible later sections.

### SUGGESTION-08
A suggestion carries these dates.

| Date | Meaning |
| --- | --- |
| Received | When the sync service recorded the suggestion, not necessarily when the collaborator first made it |
| Expiration | The collaborator-specified date when the suggestion's validity ends[^1] |

[^1]: **Gap:** D3 — How long a Submitted suggestion stays active with no response. Placeholder: 14 days after Received when no Expiration arrives.

## Reissue And Replacement

### SUGGESTION-11
A revised or refreshed edit reissued by a collaborator is a new suggestion for the same [notebook][g-notebook], with its own received date ([SUGGESTION-08]). The earlier edit remains a distinct suggestion. When the reissued edit replaces an earlier suggestion, that earlier suggestion is superseded and is reported as Expired ([SUGGESTION-12], [SUGGESTION-STATUS-05]).

### SUGGESTION-12
A superseded suggestion is an earlier edit that another suggestion has replaced, including a revised or refreshed edit ([SUGGESTION-11]). The replaced suggestion is reported as Expired ([SUGGESTION-STATUS-05]). Collaborator identity alone does not establish replacement: one collaborator can have distinct suggestions under different templates for the same [notebook][g-notebook] ([SUGGESTION-02]).

[NOTEBOOK-01]: notebook.md#notebook-01
[SUGGESTION-02]: #suggestion-02
[SUGGESTION-03]: #suggestion-03
[SUGGESTION-08]: #suggestion-08
[SUGGESTION-11]: #suggestion-11
[SUGGESTION-12]: #suggestion-12
[SUGGESTION-STATUS-01]: suggestion-status.md#suggestion-status-01
[SUGGESTION-STATUS-03]: suggestion-status.md#suggestion-status-03
[SUGGESTION-STATUS-04]: suggestion-status.md#suggestion-status-04
[SUGGESTION-STATUS-05]: suggestion-status.md#suggestion-status-05
[SUGGESTION-STATUS-06]: suggestion-status.md#suggestion-status-06
[SUGGESTION-STATUS-07]: suggestion-status.md#suggestion-status-07
[g-notebook]: ../glossary.md#notebook
[g-active-suggestion]: ../glossary.md#active-suggestion
