Managed-By: skai
Managed-Id: guide.known-gaps
Managed-Source: Guides/Core/known-gaps.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-11-11

# Known Gaps

Print `📖 SKAI guide: known-gaps` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Examples are LumenNotes, SKAI's fictional theme.

1. **A gap is a decision needed before shipping that nobody in the work can make yet: the answer is not known outside it.** Within your authority: decide and record it for review. Otherwise a Discussion item, blocking; only the supervisor rules it a gap. ❌ "PDF support?" is not a gap if text-only sharing ships either way: out of scope or a known difference. ✅ "Which formats share a note?" is one while the partner app has not said which it opens.
2. **Build on the placeholder until closure.** It is the supervisor's provisional answer; with none, the dependent part stays out of the drafts. Downstream never second-guesses it; if it seems wrong, file a change request upstream.
3. **Open gaps never block authoring's completion, except as rule 5 says.** Your own: unchecked Discussion items with a **Gap** line, logged per your workflow's formats. Mark own gaps and inherited placeholders: footnotes per [`spec-file-gaps.md`](spec-file-gaps.md) in spec files, inherited only in design change lists; UI Map and Figma mirrors per their guides.
4. **The supervisor closes your own gaps one of three ways.** Answered: the decision replaces the placeholder in the drafts. Adopted: the placeholder becomes the rule as written; a follow-up is a ticket, not the artifact's concern. Omitted: the dependent part leaves the drafts, recorded under Out of scope. Record which and the outcome in the item's Decision and the artifact's Decision Log; check the box and remove its markers.
5. **Inherit upstream gaps as markers, not items, on what stands on the placeholder.** With a placeholder, proceed, no decision, until the owning item closes (7). Without one, if the missing part blocks progress, wait at a blocked gate; else omit it, unmarked.
6. **Promotion into production needs zero open gaps, in promoted requests too: items and markers.** Open gaps fail readiness: the blocked gate lists them; the package returns to authoring: own gaps close per (4), a promoted request's as [`change-requests.md`](change-requests.md) says, inherited markers when their owning items close (5, 7). Promotion never moves, renumbers or resolves a gap; a fold checks off base items already ruled in the request.
7. **When an upstream gap closes, build on the outcome under your workflow's Discussion rules and clear the markers.** Adopted as written: nothing else. An answer differing from the placeholder, or an upstream omission, is a change that may undercut an approved decision.
8. **Work through the supervisor.** No owner field or line names who is to answer; Concern states what is not yet known. The supervisor starts promotion; file requests when your workflow says; a decision you cannot make returns to your workflow's gate.

## Project Addendum

If `<active-project-root>/skai/addenda/known-gaps-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
