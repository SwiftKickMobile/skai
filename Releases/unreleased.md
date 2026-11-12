# Unreleased

**Review pages**

- 2026-11-12 **A review page no longer fails when a gap owner's item links another package** (`spec-tool.py` `owner_tips`; both `spec-tool.py render` and `design-tool.py render`): rendering the popovers of a gap owner's Discussion items read in any further artifact those items link, while the owners were being listed, and the render stopped with "dictionary changed size during iteration". Owners read in that way now get their own popovers too. **Migration:** none; re-render any page that failed to render.
