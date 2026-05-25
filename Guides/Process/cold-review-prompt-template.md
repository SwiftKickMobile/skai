# Cold-Review Prompt Template

A fill-in template for launching a **cold review** of a skill's guide(s) -- see `skill-refinement-guide.md`. The maintainer fills the slots below and hands the result to a **fresh, no-context session** (a different session from the one that will do the refinement). The cold reviewer produces findings; the refining session consumes them.

The cold reviewer must NOT read this template or `skill-refinement-guide.md` -- those are refiner-facing and would bias the review toward "what's codifiable" instead of a free, aggressive read. Give the reviewer only the filled prompt and the files it names.

## How to fill it

Replace each `{{SLOT}}`:

- `{{SKILL_NAME}}` -- the skill under review.
- `{{GUIDES}}` -- the binding guide file(s) under review, with paths. The review target.
- `{{SPEC}}` -- the design spec / standard the guide is judged against (path).
- `{{CONTEXT_FILES}}` -- non-normative files the reviewer may consult for context (paths); mark them non-normative.
- `{{RECENTLY_REVISED}}` -- a short list of what changed recently, so the reviewer looks hardest there.
- `{{FAILURE_MODES}}` -- recurring traps to check (e.g. append-without-restructure, jargon over plain language, scattered gate behavior, grab-bag findings).
- `{{SIMULATION_STEPS}}` -- the workflow-specific steps a greenfield operator would walk (this skill's phases/gates).
- `{{LEGACY_ARTIFACTS}}` -- predecessor / stale artifacts the reviewer must NOT treat as compliance targets.

Delete any slot that does not apply (e.g. a single-guide skill needs no multi-doc consistency lens; omit the legacy section if there are no legacy artifacts).

## Copy/paste prompt

```text
You are doing a fresh-eyes, critical cold review of the {{SKILL_NAME}} skill as documented. You have no prior conversation context; work only from the files named below.

This is a document/process review, NOT a coding task. Do not implement changes, do not rewrite docs, do not propose edits in patch form. Your job is to audit the guide(s) for gaps, ambiguities, contradictions, information-architecture problems, weak enforcement, and places where a fresh LLM operator would misuse or skip the process.

## The standard
Judge the guide(s) for fidelity against the design spec: {{SPEC}}. The spec is the standard -- where guide and spec diverge, that is a finding (note which side looks wrong, but treat the spec as authoritative unless it is internally contradictory).

## Review target (binding surfaces)
Read these carefully as the primary source of truth:
{{GUIDES}}

## Context surfaces (non-normative)
Read only as needed; do not treat as compliance targets unless a binding surface routes the operator to them as an active input:
{{CONTEXT_FILES}}

## Legacy artifacts -- NOT compliance targets
{{LEGACY_ARTIFACTS}}
Treat the above as historical/contextual only. Do NOT issue a finding merely because a legacy artifact fails to match the current guide. Only flag one if (a) the current docs still route operators to it as active surface, (b) the docs fail to distinguish active from historical material, or (c) the workflow still depends on it in a way that would confuse a fresh operator. The test is whether the current docs are coherent and operable now -- not whether old files conform.

## What recently changed (look hardest here)
{{RECENTLY_REVISED}}

## Recurring failure modes to check
{{FAILURE_MODES}}

Be skeptical and cold-reader-oriented. Assume the authoring LLM is lazy, literal, and prone to local patching unless the docs make the right behavior easy and the wrong behavior hard.

## Review in three modes

### 1. Static architecture review
Look for: rules duplicated across sections (a drift hazard); rules stated in concept sections that belong at the operational step/gate; gate requirements that are not self-contained; templates/examples that do not match the prose; policy vague enough to be gamed; places where a fresh agent must "remember" something from elsewhere instead of finding it at the point of use; muddy boundaries between process docs and spec/domain docs; active-vs-historical material left blurred.

### 2. Greenfield operator simulation (primary)
Mentally run a fresh agent through the workflow from scratch, with no reliance on prior runs, relying on memory of other sections only where the doc would naturally have sent you there. Walk at least:
{{SIMULATION_STEPS}}
At each stop ask: do I find everything I need right here? Do I know exactly when to stop and what gate line to emit? Do I know exactly what to show the human at each gate? If the workflow only works because you mentally stitch together scattered sections, that is a finding.

### 3. Legacy-encounter simulation (only if legacy artifacts exist)
Simulate a fresh operator hitting a legacy artifact. Do the current docs make its status (active / optional / historical / obsolete) clear? Could it be mistaken for a current template or compliance target? The finding is confusion caused by the current docs, not the existence of old files.

## Output
A review report only. Structure it:
1. Top findings first -- ordered by severity; code-review style with file paths + line references; behavioral/process risk, not wording nitpicks.
2. Simulation results -- where the process felt smooth vs brittle (normal path, any blocked case, legacy-encounter path).
3. Open questions / tensions -- anything under-specified or internally conflicted; separate current-workflow ambiguity from historical-artifact noise.
4. Verdict -- is the guide usable by a fresh LLM from scratch today? Biggest remaining risks?

## Style
Be direct and critical; prefer findings over summary; cite exact file paths and line numbers; distinguish verified findings from speculation; do not soften real problems; do not assume prior conversation context beyond the files; do not start fixing anything.
```
