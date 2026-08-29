---
name: skai-process-refinement
description: Refines a process guide against a cold review using skai (commissioning the review, triaging findings, cluster-at-a-time repair, round scoring, and when to stop). Use when a guide or process document needs hardening, when a cold review has produced findings to act on, or when the user asks to refine or harden a process document.
---

# SKAI: Process refinement

## Instructions

- Read:
  - `Submodules/skai/Guides/Process/process-refinement-guide.md`
  - `Submodules/skai/Guides/Process/cold-review-prompt-template.md`
- The cold reviewer must NOT read either of the above — both are refiner-facing and would bias the review. Give it only the filled prompt and the files it names.
- Record the pass in a working doc under `skai/working-docs/<branch-path>/<session-name>/` per `Submodules/skai/Guides/Core/working-doc-conventions.md`, and append dispositions to the target's findings log at `skai/refinement-reviews/<target-name>-findings.md`.
