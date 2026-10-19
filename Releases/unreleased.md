# Unreleased

**Spec tool**

- 2026-10-18 **`check-changes` accepts `retire requirement` for an absorbed item.** An item whose heading the drafts drop entirely (its content folded into another item's table or rules, no `(retired)` stub) shows as `missing` in the projection; a `retire` entry now matches it, as it already matched `retired` and `removed`. The catalog guide's retire-with-stub rule is unchanged; this covers a supervisor-approved rework that burns the ID without a stub. **Migration:** none; the tool is read from the checkout.
