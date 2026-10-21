Managed-By: skai
Managed-Id: guide.known-gaps
Managed-Source: Guides/Core/known-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-20

# Known Gaps

Print `📖 SKAI guide: known-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

How to work with a **gap**: something that must be decided before the work ships, but not yet, so work proceeds on a placeholder and nothing undecided reaches canon. Examples are LumenNotes, SKAI's fictional theme.

1. **A gap must be decided before shipping.** ❌ "PDF support?" is not a gap if text-only sharing ships either way: that is out of scope or a known difference. ✅ "Which formats share a note?" is a gap if export cannot be built until one is named.
2. **Build on the placeholder until closure.** It is the provisional answer; record one whenever you can. Without it, the gap gives nothing to build on. Downstream never second-guesses it; if it seems wrong, file a change request upstream.
3. **Keep gaps open through authoring's completion.** Use the Discussion and Decision Log formats your workflow inlines:
   - All artifacts: an unchecked Discussion item with a **Gap** line.
   - Spec file: mark the placeholder with the spec-file shape's footnote.
   - UI Map proposal and Figma change page: mirror each open gap as their guides say.
4. **Resolve gaps one of three ways.** Answered: the decision replaces the placeholder in the drafts. Placeholder adopted: the text becomes the rule as written; a follow-up is a ticket, not this artifact's concern. Omitted: remove the dependent behavior from the drafts and record it under Out of scope. Record which, and the outcome, in the item's Decision and the artifact's Decision Log; check the box and remove the artifact's marker.
5. **Inherit upstream gaps.** With a placeholder, proceed without a decision; carry your own gap item and artifact marker naming the upstream gap, and close it when that gap closes (see 7). Without a placeholder, raise a Discussion item recommending one of: request a placeholder upstream (a change request), omit the dependent part (Out of scope), or wait at a blocked gate for an answer. The supervisor rules.
6. **Every package needs zero open gaps for promotion.** An open gap fails readiness: the blocked gate lists them and the package returns to authoring, where each is answered, adopted or omitted. Promotion never resolves a gap.
7. **Use the normal input catch-up and Discussion rules.** Adopted upstream as written: nothing changes; close your inherited gap as answered. An answer differing from the placeholder may undercut an approved decision. Omitted upstream: remove the dependent part from your drafts too.
8. **Work through the supervisor.** There is no owner field: skai knows only the supervisor. The question may name who is awaited; guides and tools never read that name. Leave change requests and promotion for the supervisor to start; a decision you cannot make returns to your workflow's gate.

## Project Addendum

If `<active-project-root>/skai/addenda/known-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
