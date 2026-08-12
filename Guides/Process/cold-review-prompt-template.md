Managed-By: skai
Managed-Id: guide.cold-review-prompt-template
Managed-Source: Guides/Process/cold-review-prompt-template.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-08-05

# Cold-Review Prompt Template

A fill-in template for launching a **cold review** of a skill's guide(s) -- see `skill-refinement-guide.md`. The maintainer fills the slots below and hands the result to a **fresh, no-context session** (a different session from the one that will do the refinement). The cold reviewer produces findings; the refining session consumes them.

The cold reviewer must NOT read this template or `skill-refinement-guide.md` -- those are refiner-facing and would bias the review toward "what's codifiable" instead of a free, aggressive read. Give the reviewer only the filled prompt and the files it names.

## How to fill it

Replace each `{{SLOT}}`:

- `{{SKILL_NAME}}` -- the skill under review.
- `{{GUIDES}}` -- the binding guide file(s) under review, with paths. The review target.
- `{{SPEC}}` -- the design spec / standard the guide is judged against (path).
- `{{SCOPE}}` -- what the review target is and is **not** responsible for: the span it covers, and what deliberately lives in another document, in tooling, or in a doc not yet written. Omitting this is the most common cause of a review that never converges -- a reviewer told "this is the binding surface" will fault a chapter for not being the whole book, round after round.
- `{{CONTEXT_FILES}}` -- non-normative files the reviewer may consult for context (paths); mark them non-normative.
- `{{SETTLED_DISPOSITIONS}}` -- decisions already made and closed: things the maintainer or project owner deliberately chose, and deferrals that are already scheduled. Give the *decisions only*, never the coverage map itself -- the map is refiner-facing and showing it would stop the review being cold. Omitting this is the second most common cause of a review that never converges: the coverage map is deliberately withheld from the reviewer, so without this slot nothing prevents a fresh reader re-raising settled ground every round.
- `{{RECENTLY_REVISED}}` -- a short list of what changed recently, so the reviewer looks hardest there.
- `{{FAILURE_MODES}}` -- recurring traps to check (e.g. append-without-restructure, jargon over plain language, scattered gate behavior, grab-bag findings).
- `{{SIMULATION_STEPS}}` -- the workflow-specific steps a greenfield operator would walk (this skill's phases/gates).
- `{{LEGACY_ARTIFACTS}}` -- predecessor / stale artifacts the reviewer must NOT treat as compliance targets.

Delete any slot that does not apply (e.g. a single-guide skill needs no multi-doc consistency lens; omit the legacy section if there are no legacy artifacts).

## Copy/paste prompt

**Use this block verbatim.** Fill `{{SLOT}}` markers only. Delete entire slot sections (heading and body) when a slot does not apply. Do **NOT** rephrase the prose, add a preamble, restructure sections, or paraphrase the failure-mode list — those are calibrated for the cold reviewer and changing them taints the review.

The prompt-tainting failure mode this rule prevents: a maintainer composing the prompt sees the slot-filled block as scaffolding and rewrites prose around their own framing, often asserting unverified facts ("this is intentional") that the reviewer then inherits as premises. The resulting findings are biased by the maintainer's prior beliefs — the opposite of what the cold review is for.

**Quick check before handing off:** diff your filled prompt against the block below. The only differences should be (a) `{{SLOT}}` markers replaced with the filled content, and (b) entire slot sections deleted when not applicable. If the diff shows reworded prose, restructure it back to the verbatim form before handing off.

```text
You are doing a fresh-eyes, critical cold review of the {{SKILL_NAME}} skill as documented. You have no prior conversation context; work only from the files named below.

This is a document/process review, NOT a coding task. Do not edit any file. Your job is to audit the guide(s) for gaps, ambiguities, contradictions, information-architecture problems, weak enforcement, and places where a fresh LLM operator would misuse or skip the process -- and to recommend a fix for each finding, in prose (never a patch or a rewritten file).

Your recommendations carry weight because you have just read the whole document fresh, while the maintainer has been editing it locally and has lost that view. Say where each fix belongs, and follow the editing discipline below when choosing it. The maintainer decides what to apply.

## The standard
Judge the guide(s) for fidelity against the design spec: {{SPEC}}. The spec is the standard -- where guide and spec diverge, that is a finding (note which side looks wrong, but treat the spec as authoritative unless it is internally contradictory).

## Review target (binding surfaces)
Read these carefully as the primary source of truth:
{{GUIDES}}

## Scope of the review target
{{SCOPE}}
Findings that amount to "inline the content that deliberately lives elsewhere" are out of scope -- name the boundary instead.

## Context surfaces (non-normative)
Read only as needed; do not treat as compliance targets unless a binding surface routes the operator to them as an active input:
{{CONTEXT_FILES}}

## Legacy artifacts -- NOT compliance targets
{{LEGACY_ARTIFACTS}}
Treat the above as historical/contextual only. Do NOT issue a finding merely because a legacy artifact fails to match the current guide. Only flag one if (a) the current docs still route operators to it as active surface, (b) the docs fail to distinguish active from historical material, or (c) the workflow still depends on it in a way that would confuse a fresh operator. The test is whether the current docs are coherent and operable now -- not whether old files conform.

## Settled dispositions -- do not re-raise
{{SETTLED_DISPOSITIONS}}
These were decided deliberately. Do not report them as findings, and do not recommend reopening them. If you believe one is actively causing a defect you can point to, say so once, briefly, under Open questions -- not as a finding.

## What recently changed (look hardest here)
{{RECENTLY_REVISED}}

## Recurring failure modes to check
{{FAILURE_MODES}}

Be skeptical and cold-reader-oriented. Assume the authoring LLM is lazy, literal, and prone to local patching unless the docs make the right behavior easy and the wrong behavior hard.

## Editing discipline your recommendations must follow

These are the same rules the maintainer is bound by. A recommendation that violates them is worse than no recommendation, because a guide's characteristic failure mode is accumulated narrow rules.

**Codification check -- work it in order before recommending any new rule:**
1. Does an existing rule already cover this case? If yes, the fix is *sharpening that rule* or adding a ❌/✅ example to it -- never a new rule.
2. Is this a single observation or a recurring pattern? Codify only on recurrence; a one-off is a `log-only`.
3. Can one principle cover the whole class, or is the fix per-instance? If you find yourself proposing a third sibling rule, you missed the generalization -- name the principle instead.

**Prefer, in this order:** delete or relocate existing text · sharpen existing wording · add a worked ❌/✅ example · restate a rule at its point of use · (last resort) add a new rule, gate, or required field.

**Fix root causes, not symptoms.** Before listing findings, look for shared causes across them. If several findings are instances of one underlying problem, say so explicitly and recommend ONE consolidated fix for the cluster rather than N local patches. Naming the root cause is more useful than any individual fix.

**Churn guard.** For each recommendation, name the adjacent behavior or rule that must NOT change as a result. A fix that quietly alters neighboring semantics is a defect.

**Self-check every recommendation before you write it down:** Would it contradict adjacent text in the same document? Would it leave a now-stale sentence still teaching the old behavior elsewhere? Would it move a rule away from the point where the operator needs it? Would it weaken an enforced rule into a suggestion? If any answer is yes, revise the recommendation.

**No opportunistic cleanup.** Recommend only what is needed to close the finding.

## Review in three modes

### 1. Static architecture review
Look for: rules duplicated across sections (a drift hazard); rules stated in concept sections that belong at the operational step/gate; gate requirements that are not self-contained; templates/examples that do not match the prose; policy vague enough to be gamed; places where a fresh agent must "remember" something from elsewhere instead of finding it at the point of use; muddy boundaries between process docs and spec/domain docs; active-vs-historical material left blurred.

### 2. Greenfield operator simulation (primary)
Mentally run a fresh agent through the workflow from scratch, with no reliance on prior runs, relying on memory of other sections only where the doc would naturally have sent you there. Walk at least:
{{SIMULATION_STEPS}}
At each stop ask: do I find everything I need right here? Do I know exactly when to stop and what gate line to emit? Do I know exactly what to show the human at each gate? If the workflow only works because you mentally stitch together scattered sections, that is a finding.

### 3. Legacy-encounter simulation (only if legacy artifacts exist)
Simulate a fresh operator hitting a legacy artifact. Do the current docs make its status (active / optional / historical / obsolete) clear? Could it be mistaken for a current template or compliance target? The finding is confusion caused by the current docs, not the existence of old files.

## Verify claims about tooling against the implementation
Where the guide asserts what a script or tool enforces, guarantees, or produces, read that implementation and confirm it actually does. This is the highest-yield check available to you, because a guide and its tooling drift apart silently: the guide keeps promising what the tool stopped doing. Report the divergence and say which side looks wrong.

Do not spend findings on command *syntax* -- parse errors, unbound variables, exit codes, placeholder notation. Those are mechanically checkable and are the maintainer's job to check that way; a finding there costs a review round to do a linter's work. Do flag a command whose *documented meaning* is wrong: one that runs fine and does something other than what the prose claims.

Never run anything mutating, destructive, or costly: no writes, no model calls, no network side effects. Prefer reading the implementation. Mark each finding **verified** (you read or ran something -- quote it) or **speculative** (reasoned from the text alone). Do not blur the two.

## Output
A review report only. Structure it:
0. Root causes -- if several findings share one underlying cause, name the cluster and recommend a single consolidated fix. If there are none, say so.
1. Top findings first -- ordered by severity; code-review style with file paths + line references; behavioral/process risk, not wording nitpicks. Each finding carries:
   - **Problem + risk**, marked **verified** (you ran it -- quote the output) or **speculative** (reasoned from reading).
   - **Recommended fix** -- the smallest change that resolves it coherently with the rest of the document, per the editing discipline above: name the section it belongs in, and whether it sharpens / relocates / deletes existing text or adds something new. If it requires touching text elsewhere to stay consistent, say where.
   - **Churn guard** -- the adjacent behavior or rule that must NOT change as a result.
   - **Triage** -- your call on how the maintainer should treat it: `accept` (real defect, fix is proportionate) · `log-only` (valid observation, but the fix costs more than the problem) · `human-decision` (the fix adds process weight -- a new gate, rule, checklist, or proof burden -- not a reviewer's call).
   - **Bloat flag** -- set it if the smallest sensible fix adds a new rule, gate, or required field.
   If you cannot name a proportionate fix, that is itself a signal: mark it `log-only` and say why.
2. Simulation results -- where the process felt smooth vs brittle (normal path, any blocked case, legacy-encounter path).
3. Open questions / tensions -- anything under-specified or internally conflicted; separate current-workflow ambiguity from historical-artifact noise.
4. Verdict -- is the guide usable by a fresh LLM from scratch today? Biggest remaining risks?

## Style
Be direct and critical; prefer findings over summary; cite exact file paths and line numbers; distinguish verified findings from speculation; do not soften real problems; do not assume prior conversation context beyond the files; recommend fixes in prose, but do not edit files.
```
