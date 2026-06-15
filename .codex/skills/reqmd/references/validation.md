# ReqMd Validation

Run `scripts/validate_reqmd.py` when possible. Use this checklist for manual review or when script output needs interpretation.

## Syntax

- Requirement headings start with `[IDENTIFIER](@)` or `[IDENTIFIER](path/@)`.
- Identifiers match `[A-Z][A-Z0-9_]*`.
- General helpers match `[a-z][a-z0-9_]*`.
- Implementation helpers start with `=` and are exempt from general helper naming.
- YAML attributes appear only in requirement bodies.
- `@.md` and `=.md` contain no YAML blocks.

## Indexes

- `@.md` section headings link to source requirement sections, for example `## [IDENTIFIER](SwReq.md#identifier-title)`.
- `=.md` section headings link to source helper sections, for example `## [helper](SwReq.md#identifier-title)`.
- Index body links point to other index sections and contain fragments, for example `../sys/@#sys_blc_control` or `../swdd/=#brakelampreq`.
- Source document links use the actual identifier/helper text in the section heading.
- Duplicate index sections are not allowed.
- Link fragments resolve to real sections when the target index file exists.

## Traceability

- Requirement identifiers found in body documents should have `@.md` sections.
- Helpers found in body documents should have `=.md` sections when they are significant for implementation or verification.
- Requirement-to-test and requirement-to-design links should be present when those artifacts exist.
- Reverse relationships may be computed; missing reverse links are not necessarily errors.

## Quality

- One requirement should express one verifiable behavior or constraint.
- Avoid vague words such as "appropriate", "quickly", "sufficiently", and "as needed".
- Include numeric limits, state conditions, timing, and exception behavior when required for verification.
- Avoid over-constraining implementation in software requirements unless the constraint is intentional.
