# ReqMd Workflows

Use these procedures when editing ReqMd documents.

## Add Requirement

1. Choose the requirement path and document.
2. Create a stable `SCREAMING_SNAKE_CASE` identifier.
3. Write one verifiable behavior or constraint per requirement section.
4. Add helper links for concepts, signals, states, variables, tests, or model items.
5. Add YAML attributes in the requirement body.
6. Add or update the identifier section in `@.md`.
7. Add or update helper sections in `=.md`.
8. Use fragment links for index-to-index links.
9. Run validation.

## Edit Requirement

1. Locate the requirement section by identifier.
2. Preserve the identifier unless the user explicitly requests a rename.
3. Update body text and YAML attributes.
4. Re-scan helper links in the section.
5. Add missing helper index sections and source links.
6. Review related identifier index links for design/test impact.
7. Report links that are uncertain instead of deleting them silently.

## Update Indexes

1. Collect requirement identifiers from headings.
2. Collect helper links from requirement bodies.
3. Ensure `@.md` and `=.md` exist in each requirement path.
4. Add missing sections with source document links.
5. Preserve existing semantic links unless clearly obsolete.
6. Rewrite index links to include fragments when missing.
7. Keep indexes free of YAML blocks.

## Analyze Impact

1. Start from the changed identifiers and helpers.
2. Follow `@.md` links to related requirements, design, and tests.
3. Follow `=.md` links to related helpers, implementation helpers, and observed test values.
4. Compute reverse links by scanning all index files.
5. Report impacted requirements, design items, tests, and implementation symbols separately.

## Validate

Run:

```powershell
python .codex\skills\reqmd\scripts\validate_reqmd.py reqmd
```

Use the project root or a specific requirement root as the argument.
