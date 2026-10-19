# Unreleased

**Spec tool**

- 2026-10-18 **`check-changes` accepts `retire requirement` for an absorbed item.** An item whose heading the drafts drop entirely (its content folded into another item's table or rules, no `(retired)` stub) shows as `missing` in the projection; a `retire` entry now matches it, as it already matched `retired` and `removed`. The catalog guide's retire-with-stub rule is unchanged; this covers a supervisor-approved rework that burns the ID without a stub. **Migration:** none; the tool is read from the checkout.
- 2026-10-18 **`check-changes` matches entries by kind.** A change-list entry names only things of its own type: a glossary entry, an index line, a file or folder, or an item. A glossary term, an index line and a section sharing a name (`Appointment`, the `appointment` index line, an `## Attention` section beside the `attention` term) no longer collide. **Migration:** none.
- 2026-10-18 **`render` and `check-changes` take `--base DIR`** (repeatable): further base roots layered over the catalog, each later one winning, so a package can be drafted on top of another open package's drafts and diff against them, the way `validate` already projects several roots. **Migration:** none.
