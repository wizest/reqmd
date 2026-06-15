---
name: reqmd
description: Create, edit, validate, and analyze ReqMd Markdown requirements. Use when working with ReqMd requirement documents, `@.md` identifier indexes, `=.md` helper indexes, YAML requirement attributes, traceability links, requirement impact analysis, or requirement-to-design/test/code helper mapping.
---

# ReqMd

Use this skill to work on ReqMd requirement sets. ReqMd uses plain Markdown links for requirement identifiers and helpers, YAML code blocks for requirement attributes, and per-directory indexes named `@.md` and `=.md`.

## Workflow

1. Classify the request as authoring, editing, index update, validation, or impact analysis.
2. Inspect the target requirement path: read the requirement documents plus `@.md` and `=.md`.
3. Load only the needed reference:
   - For syntax details, read `references/syntax.md`.
   - For task procedures, read `references/workflows.md`.
   - For ambiguous choices, read `references/decision-rules.md`.
   - For validation criteria, read `references/validation.md`.
   - For before/after patterns, read `references/examples.md`.
4. Apply changes to requirement bodies first, then update indexes.
5. Run `scripts/validate_reqmd.py <root>` after edits when feasible.
6. Report changed requirement sections, changed indexes, validation results, and any unresolved review items.

## Core Rules

- Requirement sections start with an identifier link such as `## [SW_BLC_PEDAL_ON](@)`.
- Identifiers use `SCREAMING_SNAKE_CASE`.
- General helpers use `snake_case`, for example `[brake_lamp_request](=)`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`, and preserve actual code/model names.
- Requirement attributes are YAML code blocks in requirement bodies only.
- `@.md` and `=.md` contain link lists only; never add YAML attributes to index files.
- Index section headings link to source document sections, for example `## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)`.
- Index body links to other index entries must include index-section fragments, for example `@#sw_blc_pedal_on`, `=#brake_lamp_request`, `path/@#sys_blc_pedal_on`, or `path/=#brakelampreq`.
- Source document links in indexes use the original identifier/helper text in the section heading, not a fixed source label.
- Treat indexes as derived data. When body and index conflict, preserve the body and update or flag the index.

## Scripts

- `scripts/validate_reqmd.py <root>` checks naming, index YAML bans, index fragment links, duplicate index sections, and reachable index fragments.
- `scripts/update_index.py <root>` adds missing index sections and source links inferred from requirement documents. Review its output before relying on it for traceability semantics.
