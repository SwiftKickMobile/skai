# Maintainer migration bookkeeping — review standard

## Purpose

Maintain SKAI so an upgrading agent has the information required to migrate existing host
installations when shipped assets, formats, or conventions change. This standard applies to the
maintainer's bookkeeping and maintenance retro, not to implementing requirements issue #64.

## Existing contract

The maintainer runbook's Required bookkeeping section makes the changelog's audience the installing
agent. It requires entries to provide what that agent needs to migrate, including renamed/moved
assets, additions/removals, managed-content changes, and required reruns. Pure-internal changes with
no host effect are omitted. Released notes remain frozen; a session records its net host-visible
change under Unreleased.

The maintenance retro checks work completed in the session for omissions and fixes straightforward
misses. It is a completeness backstop, not a transcript or a detailed diff report.

The update-installation guide reads applicable changelog sections, reports changes for review,
then runs each installed adapter's migration-capable algorithm. Each adapter discovers, classifies,
plans, obtains approval, and executes. Project-owned content and canonical artifact ownership remain
protected. A claim that this process cannot use changelog migration instructions must be supported
by inspection of these documents, not assumed.

## Desired outcome

A maintainer considering a change that affects stored host artifacts accounts for existing artifacts
as well as future outputs and leaves usable migration instructions when migration is necessary.
For changes requiring none, the maintainer can explain why; this does not require new permanent
fields, extra gates, or a prescribed extra artifact.

The failure under assessment is a session's omission of existing-artifact migration from its initial
proposal and its unsupported claim that changelog instructions alone would be insufficient. The
review may conclude that existing rules were overlooked and no guide edit is justified. Judge any
proposed text against the existing contract and proportionality rather than treating the proposal
as an approved new requirement.

## Boundaries

Preserve current safety and approval rules, existing installer workflow, changelog audience and
release-history rules, and concise maintenance guidance. Do not implement issue #64, alter host
catalog ownership, generalize presentation rules, or add new installer capability in this pass.
