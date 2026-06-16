# ReqMd Workflows

Use these procedures when editing ReqMd documents.

## Add Requirement

1. Choose the requirement path and document.
2. Create a stable `SCREAMING_SNAKE_CASE` identifier.
3. Add one RequirementSection whose heading starts with `[IDENTIFIER](@)`.
4. Write one verifiable EARS-style behavior or constraint in the RequirementBody.
5. Add helper links for concepts, signals, states, variables, tests, or model items.
6. Add YAML attributes as RequirementAttributes inside the RequirementSection.
7. Add or update the identifier section in `@.md`.
8. Add or update helper sections in `=.md`.
9. Use fragment links for index-to-index links.
10. Run validation.

## Edit Requirement

1. Locate the RequirementSection by identifier.
2. Preserve the identifier unless the user explicitly requests a rename.
3. Update body text and YAML attributes.
4. Re-scan helper links in the RequirementSection only.
5. Do not collect helper links from GeneralSection content.
6. Add missing helper index sections and source links.
7. Review related identifier index links for design/test impact.
8. Report uncertain links instead of deleting them silently.

## Update Indexes

1. Collect requirement identifiers from RequirementSection headings.
2. Collect helper links from RequirementSection bodies.
3. Skip GeneralSection content.
4. Ensure `@.md` and `=.md` exist in each requirement path.
5. Add missing sections with source document links.
6. Preserve existing semantic links unless clearly obsolete.
7. Rewrite index links to include fragments when missing.
8. Keep indexes free of YAML blocks.

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
