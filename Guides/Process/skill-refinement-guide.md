# Skill Refinement Guide

A process for refining a skill — its guide document(s) — based on a cold review. Applies to any skill under development.

A fresh session running this should read: this guide, the skill's design spec, the skill guide(s) under refinement, and the cold-review findings.

## When to use this

Use it when a cold review finds real problems in a skill's guide(s). Trivial copy edits (a typo, a broken link) don't need it — just fix them. Anything touching workflow, control-flow semantics, document structure, or fidelity to the skill's design spec does.

## The cold review

The input is a **cold review**: a fresh, independent session that reads the skill's guide(s) and its design spec with no prior context and critically assesses fidelity, completeness, clarity, internal consistency, and conciseness. It produces findings — each with a severity and a suggested fix — and a verdict. The review is meant to be aggressive; it is not blunted to spare feelings.

To launch one, fill in the slots in [`cold-review-prompt-template.md`](cold-review-prompt-template.md) and hand the filled prompt to a fresh session. That reviewer must **not** read this guide or the template (both are refiner-facing and would bias the review); give it only the filled prompt and the files it names.

## The design spec is the standard

Every skill should have a **design spec** — a plan, requirements doc, or equivalent source-of-truth describing what the skill is supposed to do. That doc is the standard each finding is judged against. A guide that contradicts the spec is a defect; a finding that asks for something the spec deliberately decided against is weighed against the spec, not accepted automatically. If a skill has no design spec, refining it reliably is hard — close that gap first.

## The refinement working document

A refinement pass records its work in a **refinement working document**: the finding matrix, the triage decisions, the repair clusters, and the closure table. It is a working document — create it following `Guides/Core/working-doc-conventions.md`, placed under `working-docs/<branch-path>/`, named `<skill-name>-refinement.md`. This is the same logic the work-spec creation guide uses for its plan and work-spec documents, and the UI Map planning guide uses for its plan document: process artifacts are working docs, kept out of the skill's own committed files.

A trivial pass — a couple of clarity fixes — may skip the persisted document and keep the matrix inline in the conversation. Anything beyond that gets the working document.

## The coverage map

Across refinement passes on the same skill, a **coverage map** records every finding and its disposition. It is a durable working document under `working-docs/<branch-path>/`, named `<skill-name>-coverage.md`. Each pass's closure entries append to it.

Format — a single appended table:

| Pass date | Finding | Disposition | Evidence |
|---|---|---|---|

The map is consulted at *triage* (not by the cold reviewer — a cold review must remain fresh):

- When a new finding matches one already in the map, do not relitigate. If it restates a `rejected` one, refer back to the prior disposition and skip. If it restates a `closed` one with the same surface, the prior fix did not hold and the closure must be revisited.
- The map provides the cross-pass memory the recurrence threshold (see Across passes) depends on — without it, every pass treats every finding as a first sighting.

## Triage before editing

A cold review is intentionally aggressive — do not blunt it, but do not act on it raw. The refining agent owns a critical second pass. **Default to "no rule"** — most findings either fail to meet the codification bar or are already covered by existing rules. Classify every finding before any edit:

- **accept** — a real defect that warrants a fix to the guide.
- **log only** — valid observation that does not meet the codification bar (see below). Record it in the coverage map; do not change the guide.
- **reject** — speculative, ignores ownership already clear in the docs, or treats a hypothetical misuse as a normal-use failure.
- **human decision** — the finding may be valid, but the likely fix adds *process weight*: a new gate, a mirror/duplicate field, a checklist, a proof burden, extra validation, a wrapper, repeated re-approval. Not the refining agent's call.

**Codification check** — before classifying a finding as `accept`, work through this in order:

1. *Does an existing rule already cover this case?* If yes, the fix is sharpening that rule or adding a ❌/✅ example to it — not a new rule.
2. *Single observation, or recurring across cases?* If single (and not already in the coverage map from a prior pass), classify as `log only` — record it; codify only on recurrence.
3. *Can one principle cover the class, or is the fix per-instance?* If you find yourself adding a third sibling rule, you missed the generalization — look for the principle.

Only when all three pass does adding a new rule fit. The failure mode this prevents: codifying from a single observation, adding sibling rules instead of generalizing, and writing new rules when the real issue is a rule the agent failed to apply.

## The `human decision` rule

For every `human decision` finding, STOP before editing and present the tradeoff plainly:

- the real failure the reviewer is worried about
- what existing rule or artifact already covers it, if anything
- the smallest documentation-only fix
- the heavier, control-oriented fix
- a recommendation

Do not implement the heavy fix unless the human explicitly chooses it. Record the decision; don't re-litigate it in the same pass.

## Finding matrix

Before editing, organize every finding into one table in the refinement working document:

| Finding | Triage | Touches (spec § + skill doc §) | Minimal fix | Must remain unchanged |
|---|---|---|---|---|

The last column is the churn guard — name the adjacent semantics the fix must not disturb.

**Prefer examples over rules.** When the minimal fix is to teach a distinction, add a ❌/✅ worked example to an existing rule rather than write a new rule. Examples teach without inflating rule count.

## Architecture vs. content

If a finding exposes a genuine *design* contradiction — not just unclear guide wording — do not repair it directly. Frame it as a decision topic:

- the exact contradiction
- the minimum decision that resolves it
- what downstream docs the decision would ripple to

Discuss it, get a decision, update the skill's design spec, then repair the guide. Pure content/clarity findings are lighter — fix them directly once triaged.

## Repairing

- Group accepted findings into small clusters of related fixes.
- **Patch exactly one cluster, then STOP and run the self-check below in writing before touching the next cluster.** Do not batch several clusters into a single edit pass — patching every finding at once is the failure mode this prevents: it produces shallow fixes that break adjacent behavior. (Architecture findings are resolved and the spec updated *before* any cluster is patched — see above.)
- Do not fold opportunistic cleanup into a repair — if it isn't needed to close a finding, leave it.
- After each cluster, self-check (record the result before proceeding): Did I contradict adjacent text in the same file or a sibling guide? Did I leave a stale sentence teaching the old behavior? Did I move a rule away from the point where the agent needs it? Did I weaken an enforced rule into a suggestion?

## Closing the pass

In the refinement working document, mark every finding `closed` / `downgraded` / `still open` / `rejected` / `deferred` / `logged`, each with one line of evidence. For `rejected` and `logged` entries, that evidence must be the **rationale** — *why* the finding was declined or didn't meet the bar — not merely the disposition: these are exactly what a later cold review will re-raise, and the recorded rationale is what lets the next pass refer back and skip instead of relitigating. `logged` means the finding was classified `log only` at triage and recorded in the coverage map without a guide change. A finding is not `closed` if the underlying problem still reproduces under different wording.

Append every entry to the skill's coverage map at this step, so future passes have the cross-pass record.

## Scaling the ceremony

This is the lightweight form. Heavier repair protocols add a dated worklog, a large audit catalog, stale-text sweeps, and cold-reader simulations — weight calibrated for a large, in-use, multi-doc workflow. Match the ceremony to the change: a handful of clarity fixes needs only the finding matrix and the closure list; a structural repair spanning several guides warrants a fuller written repair record and a re-read of every guide it touches. Scale up when a change is genuinely that heavy — do not default to the full apparatus.

## Across passes

The disciplines below apply when a skill receives more than one refinement pass over time. A single-pass user can ignore this section.

**Recurrence threshold.** Do not codify from a single observation. First sighting = `log only` (recorded in the coverage map). Second sighting in a different case = consider codification. Third = codify. The coverage map provides the cross-pass memory this rule depends on.

**Periodic restructure.** Every several passes, refactor the guide for accumulated cruft — consolidate overlapping rules, remove dead text, reorganize sections by what is actually load-bearing. Bloat is fought retrospectively as well as at the entry point. This is a deliberate pass of its own; do not fold it into a normal refinement pass.
