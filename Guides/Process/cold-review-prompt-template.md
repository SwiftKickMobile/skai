Managed-By: skai
Managed-Id: guide.cold-review-prompt-template
Managed-Source: Guides/Process/cold-review-prompt-template.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-15

# Cold-Review Prompt Template

Print `📖 SKAI guide: cold-review-prompt-template` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

A fill-in template for each round's **cold review** of a refinement target's guide(s) -- see `process-refinement-guide.md`. Each round the refiner fills it anew for a **fresh, no-context session**, which returns findings with shaped fixes. This template and `process-refinement-guide.md` are refiner-facing and would bias the reviewer toward "what's codifiable" over a free, aggressive read, so it never reads them unless a review of either makes both its target. Give it only the filled prompt, the files it names and what they or its proposed edits reference, never an excluded file.

## How to fill it

Replace each `{{SLOT}}`:

- `{{TARGET_NAME}}` -- the process or documents under review.
- `{{GUIDES}}` -- the binding guide file(s) under review, with paths, and any sibling passage a copied fix joined: the review target.
- `{{SPEC}}` -- the design spec the guide is judged against: `skai/refinement-reviews/<target-name>-design.md`.
- `{{SCOPE}}` -- what the target is and is **not** responsible for: the span it covers, and what deliberately lives in another document, in tooling, or in a doc not yet written. Omitting this is the most common cause of a review that never converges -- a reviewer told "this is the binding surface" will fault a chapter for not being the whole book, round after round.
- `{{CONTEXT_FILES}}` -- non-normative files the reviewer must read (paths), marked as such.
- `{{SETTLED_DISPOSITIONS}}` -- decisions already made and closed: what the maintainer or project owner deliberately chose, and deferrals already scheduled. *Decisions only* -- never a claim that a defect was fixed, and never the findings log. Omitting this is the second most common cause of a review that never converges: with the findings log withheld, nothing else stops a fresh reader re-raising settled ground every round.
- `{{RECENTLY_REVISED}}` -- the supervisor's problem and wanted change, facts only, then what changed since the last round.
- `{{FAILURE_MODES}}` -- recurring traps to check (e.g. append-without-restructure, jargon over plain language, examples that teach shorthand or a citation-only reason, scattered gate behavior, grab-bag findings).
- `{{SIMULATION_STEPS}}` -- the steps a greenfield operator would walk (this workflow's phases/gates).
- `{{LEGACY_ARTIFACTS}}` -- predecessor / stale artifacts the reviewer must NOT treat as compliance targets.
- `{{EXCLUDED_SURFACES}}` -- files or folders the reviewer must not read: always the findings log and, unless they are the target, this template and `process-refinement-guide.md`; also change logs, run records, prior review dispositions -- anything reachable that carries the refiner's or the history's framing. Blindness protection, not scope.

Optional:

- `{{OBSERVED_FAILURES}}` -- observed behavioral failures during use of the target: per failure, the input, what was produced, and what was expected. Facts only -- no diagnosis, suspected mechanism or interview conclusions, which would warm the review with the refiner's framing.
- `{{PROPOSED_EDITS}}` -- the proposed change, each edit quoted in full with its intended location; hypothetical, not in the reviewed files. The normal input for a change's first round; for a new guide, its full text. From round 2 the change is in the files.
- `{{REPORT_CHARTER}}` -- what the main report is scoped to (e.g. "assessment of the proposed edits", "defects in the change as applied", "findings that explain the observed failures"). Out-of-charter findings still surface, briefly, in an appendix.
- `{{SIZE_CAPS}}` -- each guide's byte cap and current size, when the design spec sets caps (in round 1 of a cap revision, say so and give current size only); the section's fixed text says how to meet and measure them.

Delete any slot section that does not apply, heading and body (e.g. no legacy section without legacy artifacts).

## Copy/paste prompt

**Use this block verbatim.** Fill `{{SLOT}}` markers and delete whole inapplicable slot sections -- nothing else. Do **NOT** rephrase the prose, add a preamble, restructure sections, or paraphrase the failure-mode list: they are calibrated for the cold reviewer. A refiner who treats the block as scaffolding and rewrites prose around their own framing -- often asserting unverified facts ("this is intentional") -- hands the reviewer those premises, and the findings come back biased by the refiner's prior beliefs, the opposite of what the review is for.

**Before handing off,** diff the filled prompt against the block: only filled slots and deleted slot sections may differ; restore any reworded prose.

```text
You are doing a fresh-eyes, critical cold review of {{TARGET_NAME}} as documented. You have no prior conversation context; read the named files and everything they or the proposed edits reference directly, tool code included, except excluded files; work from these only. Referenced content counts as part of its citing guide.

This is a document/process review, NOT a coding task. Do not edit any file (a temporary measuring copy under Size caps is the only exception). Your job is to audit the guide(s) for gaps, ambiguities, contradictions, information-architecture problems, weak enforcement, and places where a fresh LLM operator would misuse or skip the process -- and to shape a fix for each finding, suggesting its wording (never a patch or a rewritten file). The report covers the change (the whole target if none) unless a charter says otherwise; findings outside it go briefly in an appendix after the Verdict, same fields.

Your recommendations carry weight because you have just read the whole document fresh, while the maintainer, editing locally, has lost that view. Look for the best overall solution, not the nearest patch: refactor existing text to fit a new need as efficiently as possible, keeping the information architecture sound, the writing clear and the operator reliable. Guides decay when every problem is fixed by appending a rule; a new rule is sometimes the best answer, but choose it, don't default to it. The maintainer decides what to apply.

## The standard
Judge the guide(s) for fidelity against the design spec: {{SPEC}}. The spec is the standard -- where guide and spec diverge, that is a finding (note which side looks wrong, but treat the spec as authoritative unless it is internally contradictory).

## Review target (binding surfaces)
Read each existing guide named below in full, as the primary source of truth; where only a passage of a guide is named, only that passage and what it references bind (a new guide's proposed full text is round 1's target):
{{GUIDES}}

## Scope of the review target
{{SCOPE}}
Findings that amount to "inline the content that deliberately lives elsewhere" are out of scope -- name the boundary instead.

## Context surfaces (non-normative)
Read in full; not compliance targets unless a binding surface routes the operator to them as active input:
{{CONTEXT_FILES}}

## Legacy artifacts -- NOT compliance targets
{{LEGACY_ARTIFACTS}}
Treat these as historical. Never flag one merely for not matching the current guide; flag it only if the current docs (a) still route operators to it as active surface, (b) blur active and historical material, or (c) depend on it in a way that would confuse a fresh operator. The test is whether the current docs are coherent and operable now.

## Files you must not read
{{EXCLUDED_SURFACES}}
Do not open these or use search results from them: they carry history and framing that would stop this review being cold. If a search leads you into one, discard what you saw.

## Settled dispositions -- do not re-raise
{{SETTLED_DISPOSITIONS}}
These were decided deliberately. Do not report them as findings, and do not recommend reopening them. Where the current text fails to carry one out, that is a finding; if you believe a decision itself is causing a defect, say so once, briefly, under Open questions.

## Observed failures (evidence -- treat as fact)
The following failure(s) were observed during use of the target. The observations, not their cause, are fact and join the design spec as the standard: finding what in the documents permitted these outcomes is in scope.
{{OBSERVED_FAILURES}}
Do not encode these specific inputs, outputs, or their content into any recommended wording. A fix must generalize -- it should help on cases never tested. A recommendation that describes a listed case, however paraphrased, is answer-baking, not a fix; recommend the general mechanism instead.

## Proposed edits under assessment (hypothetical -- not applied)
The maintainer has drafted the following change. It is hypothetical: NOT present in the files you are reading, and not to be treated as existing text. Assess it as a whole and hunk by hunk -- endorse, amend, or reject outright and recommend something else, including where existing text should move, be refactored or go -- and suggest wording.
{{PROPOSED_EDITS}}

## Report charter
{{REPORT_CHARTER}}


## Size caps
{{SIZE_CAPS}}
Write tightly. In round 1 of a cap revision, measure without enforcing the old cap; the refiner proposes the new cap after triage. Otherwise meet each cap mainly by tighter writing anywhere in the document. Remove wrong, duplicated or obsolete text as an ordinary fix; propose dropping valid content or examples only as a last resort, arguing they add no value, for supervisor approval. If a real fix cannot fit, report its measured over-cap shape for supervisor decision. Give every trim as exact before -> after. Measure, never estimate: apply your recommended shape, including any endorsed or amended proposal, fixes and trims, to a copy outside the repository (`mktemp -d`); run `wc -c` on each guide and report the sizes.

## The change, then recent changes (look hardest at these)
{{RECENTLY_REVISED}}

## Recurring failure modes to check
{{FAILURE_MODES}}

Be skeptical and cold-reader-oriented. Assume the authoring LLM is lazy, literal, and prone to local patching unless the docs make the right behavior easy and the wrong behavior hard.

## Editing discipline your recommendations must follow

These are the same rules the maintainer is bound by. A recommendation that violates them is worse than no recommendation, because a guide's characteristic failure mode is accumulated narrow rules.

**Codification check -- work it in order before recommending any new rule:**
1. Does an existing rule already cover this case? If yes, the fix is *sharpening that rule* or adding a ❌/✅ example to it -- never a new rule.
2. Is this recurring? Log the first sighting; consider a second in another case; a third can be codified. If the evidence you have doesn't establish recurrence, flag it for the refiner, who holds the log. This never blocks repairing a deterministic defect (a contradiction, a dangling reference, a design-spec requirement the text misses), sharpening a rule against a commissioned failure, or the proposed change.
3. Can one principle cover the whole class, or is the fix per-instance? If you find yourself proposing a third sibling rule, you missed the generalization -- name the principle instead.

**Prefer, in this order:** remove text that is wrong or duplicated · move a misplaced rule to where it is used · sharpen existing wording · add a worked ❌/✅ example · restate a rule at its point of use · (last resort) add a new rule, gate, or required field.

**Stranded is not broken.** If the workflow gives its operator a standing escalation route for unspecified situations ("if the guide doesn't answer it, stop and escalate — never invent"), a gap that violates no design-spec requirement and merely leaves the operator without an answer on a rare path is caught by that route by design — triage it `log-only` unless the strand has actually occurred. Text that teaches a wrong action -- a misroute stated as mandatory, a false claim about what a tool enforces, a contradiction both of whose readings violate the spec -- is a defect whatever its likelihood.

**Fix root causes, not symptoms.** Before listing findings, look for shared causes across them. If several findings are instances of one underlying problem, say so explicitly and recommend ONE consolidated fix for the cluster rather than N local patches. Naming the root cause is more useful than any individual fix.

**Churn guard.** For each recommendation, name the adjacent behavior or rule that must NOT change as a result. A fix that quietly alters neighboring semantics is a defect.

**Self-check every recommendation before you write it down:** Would it contradict adjacent text in the same document? Would it leave a now-stale sentence still teaching the old behavior elsewhere? Would it move a rule away from the point where the operator needs it? Would it weaken an enforced rule into a suggestion? If any answer is yes, revise the recommendation.

**No opportunistic cleanup.** Recommend only what closes a finding or tightens writing to meet a cap.

## Review in three modes

### 1. Static architecture review
Look for: rules duplicated across sections (a drift hazard); rules in concept sections that belong at the operational step/gate; gate requirements that are not self-contained; templates/examples that contradict the prose; policy vague enough to game; places a fresh agent must "remember" from elsewhere instead of finding at the point of use; muddy boundaries between process and spec/domain docs; active and historical material blurred.

### 2. Greenfield operator simulation (primary)
Mentally run a fresh agent through the workflow from scratch, recalling other sections only where the doc sends you. Walk at least:
{{SIMULATION_STEPS}}
At each stop ask: do I find everything I need right here? Do I know exactly when to stop and what gate line to emit? Do I know exactly what to show the supervisor at each gate? If the workflow only works because you mentally stitch together scattered sections, that is a finding.

### 3. Legacy-encounter simulation (only if legacy artifacts exist)
Simulate a fresh operator hitting a legacy artifact. Do the current docs make its status (active / optional / historical / obsolete) clear? Could it be mistaken for a current template or compliance target? The finding is confusion caused by the current docs, not the existence of old files.

## Verify claims about tooling against the implementation
Where the guide or a proposed edit asserts what a script or tool enforces, guarantees, or produces, read the implementation and confirm it; an excluded one leaves the claim unchecked; say so. This is your highest-yield check: a guide and its tooling drift apart silently, the guide still promising what the tool stopped doing. Report the divergence and say which side looks wrong.

Do not spend findings on mechanical command defects -- parse errors, unbound variables, placeholder notation, undocumented exit codes. They are the maintainer's to check mechanically; a finding there spends a review round on a linter's work. Do flag a command whose *documented behavior* is wrong: one that does something other than what the prose claims, an exit status or guard included.

Never run anything mutating, destructive, or costly: no writes (beyond the temporary copy under Size caps), no model calls, no network side effects. Prefer reading the implementation. Mark each finding **verified** (you ran the command, or read the implementation behind the claim -- quote it) or **speculative** (reasoned from the reviewed documents alone). Do not blur the two: reading the documents under review is the assignment, not verification.

## Output
A review report only. Structure it:
0. Root causes -- if several findings share one underlying cause, name the cluster and recommend a single consolidated fix. If there are none, say so.
1. Findings -- code-review style with file paths + line references; behavioral/process risk, not wording nitpicks. Report every defect you find, however many, not only the most important: completeness matters more than brevity. Each finding carries:
   - **Problem + risk**, marked **verified** or **speculative** (above).
   - **Consequence** -- what happens if the operator follows the document as written. Test in order, first match wins: `irreversible` (destroys work, or leaves the effort's own records unrecoverable or not comparable — ambiguity that changes what an operator does while leaving the inputs auditable is `divergent`, not this) · `divergent` (the operator stops, two operators following the same text do different things, or every operator is reliably sent to the same wrong outcome) · `cosmetic` (neither).
   - **Reachability** -- how the operator gets there. Test in order, first match wins: `past-a-rule` (reaching it requires going against a clear rule the document states, with no competing instruction or worked example sending the operator there) · `normal` (the main path — a step taken on every round counts, even when it usually resolves to nothing) · `off-normal` (a branch reached only when a triggering event occurs: recovery, restart, abandonment, an optional branch).
   - **Recommended fix** -- the best change that resolves it coherently with the rest of the document, per the editing discipline: the section it belongs in, whether it sharpens / relocates / deletes existing text or adds something, and your suggested wording; say where else text must change to stay consistent.
   - **Churn guard** -- the adjacent behavior or rule that must NOT change as a result.
   - **Triage** -- your call on how the maintainer should treat it: `accept` (real defect, fix is proportionate) · `log-only` (valid observation, but the fix costs more than the problem) · `supervisor-decision` (the fix adds process weight -- a new gate, checklist, or proof burden -- or needs valid content dropped or cannot fit a cap).
   - **Bloat flag** -- set it if the smallest sensible fix adds a new rule, gate, or required field.
   Consequence and reachability are facts about the document, not a ranking -- state each plainly and do not weigh findings against one another.
   If you cannot name a proportionate fix, that is itself a signal: mark it `log-only` and say why.
2. Simulation results -- where the process felt smooth vs brittle (normal path, any blocked case, legacy-encounter path).
3. Open questions / tensions -- unresolved tensions that do not yet support a document-defect claim; separate current-workflow ambiguity from historical-artifact noise. An under-specification or conflict that puts the operator at risk stays a finding, even when you are unsure how to resolve it or would triage it `supervisor-decision`.
4. Verdict -- is the guide usable by a fresh LLM from scratch today? Biggest remaining risks? If edits were proposed, your assessment of them, endorsements included.

## Style
Be direct and critical; prefer findings over summary; cite exact paths and line numbers; do not soften real problems.
```

## Project Addendum

If `<active-project-root>/skai/addenda/cold-review-prompt-template-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
