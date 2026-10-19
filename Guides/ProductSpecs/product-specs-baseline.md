Managed-By: skai
Managed-Id: guide.product-specs-baseline
Managed-Source: Guides/ProductSpecs/product-specs-baseline.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-10-18

# Product Specs Baseline

Print `📖 SKAI guide: product-specs-baseline` now, as a line of its own. Read this guide fully, then follow [Project Addendum](#project-addendum).

Read when [`product-specs-authoring.md`](product-specs-authoring.md) infers Baseline.

## Orient before reading code

Establish the product before reading code. From the best non-code source — the
catalog's root index, the product overview the README points at, the designs, the running app —
draft the product paragraph that opens `_product-specs.md` first, listing that source under
`## Inputs`; only then can *from what the product does, not from how the code is shaped* be held to.

## Draft cited files first

A citation uses an ID already present in a draft or an untouched canonical file, never a predicted
one. Create cited IDs before citing them; where two new files cite each other, draft one, then the
other, then add the first's missing citations — that return pass is drafting, not a stop.

## Project Addendum

If `<active-project-root>/skai/addenda/product-specs-baseline-addendum.md` exists, read it and immediately print
`  - 📎 Addendum loaded` as a line of its own, indented under this guide's line; its rules are part of this
guide and win any conflict.
