Managed-By: skai
Managed-Id: guide.writing-style
Managed-Source: Guides/Core/writing-style.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-24

# Writing Style

Print `📖 SKAI guide: writing-style` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read before writing for people: discussion items and sub-bullets, descriptions, reasons, footnotes, spec text, gate messages, requests, replies. Write as to a colleague who knows the product but was not in the session.

1. **Sentences stand alone.** With IDs, links and terms of art removed, the words still read correctly; citations supplement: "the specs dropped the unconfirmed status", not "per D15".
2. **Give reasons, then cite.** A justification or Why is a reason sentence, then its source.
3. **Name the thing, not the instance.** Use product words for screens, states, behavior or rules: "the unconfirmed offer is gone from the customer's past activity", not "Casey Cedar's Homeward card is gone". Frame names, node IDs and code names only where readers must go; sample data never.
4. **Use everyday words.** No shorthand readers haven't seen defined, coined labels or contract phrasing. Guide words stay in guides: "draw", "the package" become mock up, design, add a screen, show a state, this request.
5. **First person for your own actions, recommendations and questions; one idea per sentence.** "I was asked to wrap the kit's tab bar so we could add the badge. Should I show the Offers tab badged?"
6. **Lead with the point.** Summaries and descriptions say first what is decided or changed.

❌ "A base placeholder its page no longer draws is owed by this request." ✅ "The earlier round mocked up this placeholder and was reverted; this request mocks it up again."

Before a gate, hide IDs, links and terms of art; rewrite what stops making sense.

## Project Addendum

If `<active-project-root>/skai/addenda/writing-style-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
