# Unreleased

**Figma designer guides**

- 2026-11-19 **The structure check no longer stops on grouped layers or mixed values** (`Bin/figma-page-check.js` `has`, `above0`; `internal/tests/tools/figma-page-check/test.py`): on a real design file the check stopped with a TypeError, because Figma throws when a node is asked for a property its type lacks (a group has no text ranges) and a corner radius or spacing that differs across a node's parts is `figma.mixed`, which no number comparison accepts. Each read is now tested first and only numbers are compared, so a mixed value is not reported; a numeric corner beside it still is. The test's stand-in for Figma throws on a missing property for a node marked strict and supports a mixed value. **Migration:** none; run the check again where it stopped.
