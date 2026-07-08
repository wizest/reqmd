# ReqMd Workflows

Use these procedures when editing ReqMd documents.

## Default Workflow

Use this workflow for all ReqMd edits.

1. Limit the pass to one requirement directory.
2. Read the requirement document being changed plus local `@.md` and `=.md`.
3. Make the smallest RequirementSection body or YAML change that satisfies the request.
4. Run `python claude\reqmd\scripts\reqmd_fix.py <root>`.
5. If validation still reports `REPAIRABLE`, run the named script once before hand-editing.
6. Fix only `ERROR` items that are directly supported by source sections.
7. Report `REVIEW` items instead of deleting or inventing traceability.

## Add Requirement

1. Choose the requirement path and document.
2. Create a stable `SCREAMING_SNAKE_CASE` identifier.
3. Add one RequirementSection whose heading starts with `[IDENTIFIER](@)`.
4. Write one verifiable EARS-style behavior or constraint in the RequirementBody.
5. Add helper links for concepts, signals, states, variables, tests, or model items.
6. Add YAML attributes as RequirementAttributes inside the RequirementSection.
7. Run `python claude\reqmd\scripts\reqmd_fix.py <root>`.
8. Fix only reported structural errors.
9. Report uncertain design/test traceability instead of inventing links.

## Edit Requirement

1. Locate the RequirementSection by identifier.
2. Preserve the identifier unless the user explicitly requests a rename.
3. Update body text and YAML attributes.
4. Re-scan helper links in the RequirementSection only.
5. Do not collect helper links from GeneralSection content.
6. Run `python claude\reqmd\scripts\reqmd_fix.py <root>`.
7. Review related identifier index links for design/test impact.
8. Report uncertain links instead of deleting them silently.

## Update Indexes

1. Collect requirement identifiers from RequirementSection headings.
2. Collect helper links from RequirementSection bodies.
3. Skip GeneralSection content.
4. Ensure `@.md` and `=.md` exist in each requirement path.
5. Add missing `@.md` sections with source requirement links.
6. Add missing `=.md` sections with plain helper headings.
7. Add helper usage links to `@.md` and identifier usage links to `=.md`.
8. Run `python claude\reqmd\scripts\reqmd_fix.py <root>`.
9. Preserve existing semantic links unless clearly obsolete.
10. Keep indexes free of YAML blocks.

## Analyze Impact

1. Start from the changed identifiers and helpers.
2. Run `python claude\reqmd\scripts\analyze_impact.py <root> <identifier-or-helper> [...]`.
3. Follow `@.md` links to related requirements, design, and tests only when the script output needs local explanation.
4. Follow `=.md` links to related helpers, implementation helpers, and observed test values only when the script output needs local explanation.
5. Stop at indexed links and source-section links; do not infer new cross-directory links.
6. Report impacted requirements, design items, tests, and implementation symbols separately.
7. Separate results into `confirmed`, `inferred`, and `review needed`.

## Validate

Run:

```powershell
python claude\reqmd\scripts\validate_reqmd.py reqmd
```

Use the project root or a specific requirement root as the argument.
