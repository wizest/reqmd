# ReqMd Validation

Run `scripts/validate_reqmd.py` when possible. Use this checklist for manual review or when script output needs interpretation.

## Syntax

- Requirement headings start with `[IDENTIFIER](@)` or `[IDENTIFIER](path/@)`.
- GeneralSection headings do not start with identifiers and are excluded from requirement/index checks.
- Identifiers match `[A-Z][A-Z0-9_]*`.
- General helpers match `[a-z][a-z0-9_]*`.
- Implementation helpers start with `=` and are exempt from general helper naming.
- YAML attributes appear only inside RequirementSection content.
- `@.md` and `=.md` contain no YAML blocks.

## Indexes

- `@.md` section headings link to source requirement sections, for example `## [IDENTIFIER](SwReq.md#identifier-title)`.
- `=.md` section headings are plain helper names without links, for example `## helper`.
- Index body links point to other index sections and contain fragments, for example `../sys/@#sys_blc_control` or `../swdd/=#brakelampreq`.
- `@.md` source document links use the actual identifier text in the section heading.
- `@.md` sections include helper links used by that requirement when helpers appear in the RequirementSection body.
- `=.md` sections include identifier links for RequirementSections that use that helper.
- Duplicate index sections are not allowed.
- Link fragments resolve to real index sections when the target index file exists.
- Bare index links such as `@`, `=`, `path/@`, and `path/=` are not allowed inside index files.

## Traceability

- Requirement identifiers found in RequirementSection headings should have `@.md` sections.
- Helpers found in RequirementSection bodies should have `=.md` sections when significant for implementation or verification.
- Helpers that appear only in GeneralSection content are not required in `=.md`.
- Requirement-to-test and requirement-to-design links should be present when those artifacts exist.
- Reverse relationships may be computed; missing reverse links are not necessarily errors.

## Quality

- One requirement should express one verifiable behavior or constraint.
- RequirementBody statements should follow EARS-style structure with a clear condition, trigger, state, option, or exception when applicable, plus the expected response.
- Avoid vague words such as "appropriate", "quickly", "sufficiently", and "as needed".
- Include numeric limits, state conditions, timing, and exception behavior when required for verification.
- Avoid over-constraining implementation in software requirements unless the constraint is intentional.
