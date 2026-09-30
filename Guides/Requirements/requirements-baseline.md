Managed-By: skai
Managed-Id: guide.requirements-baseline
Managed-Source: Guides/Requirements/requirements-baseline.md
Managed-Adapter: repo-source
Managed-Updated-At: 2026-09-28

# Requirements Baseline

Read this when [`requirements-authoring.md`](requirements-authoring.md) infers Baseline mode. Three
things go wrong wherever every file being drafted is new, and nowhere else.

## Orient before reading the implementation

Establish what the product is before its code can frame it. Take the account from the best non-code
source available — the catalog's existing root index, the product overview the project's README
points at, the designs, the running app — and from it draft the product paragraph that opens
`_requirements.md` first (`requirements-catalog.md` § Root index), listing that source under `## Inputs`. Every draft is then held to the
*from what the product does, not from how the code is shaped* clause of *Working a backfill*
([`requirements-authoring.md`](requirements-authoring.md)), which has nothing to be held against until
the product's outside is on the page.

## Draft cited files first

A citation is written only against an ID that already exists in a draft, never predicted: a guessed
ID that happens to exist is a wrong citation that reads as correct, and nothing downstream catches
it. So the file whose IDs are cited is drafted before the files that cite it. Where two files cite
each other, draft one, then the other, then return to the first for the citations it could not yet
make. That return pass is part of drafting, not a stop.

## Delegation

Research and review may be delegated; authoring may not. A delegated session writes nothing in the
package — nothing under `proposed-requirements/`, no Discussion item, no ID — and what it returns is
input the one author reads and drafts from, exactly like a design or the code, never text carried
into a draft as returned. Every failure delegated authoring invites is a coherence failure — guessed
citations, one term meaning two things, `D<n>` numbered per author and renumbered on merge, the
product rebuilt differently from each author's fragment — and one author holding the whole package
avoids all of them.
