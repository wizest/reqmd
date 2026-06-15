---
name: reqmd
description: Work with ReqMd Markdown requirements, including requirement sections, YAML attributes, `@.md` identifier indexes, `=.md` helper indexes, traceability links, source-section fragments, index-section fragments, validation, and impact analysis.
---

# ReqMd

Use this skill when editing, validating, creating, or analyzing ReqMd requirement documents.

ReqMd uses normal Markdown with project conventions:

- Requirement sections start with identifier links such as `## [SW_BLC_PEDAL_ON](@)`.
- Requirement attributes are YAML code blocks in requirement bodies only.
- Identifier indexes are named `@.md`.
- Helper indexes are named `=.md`.
- Index files contain Markdown headings and link lists only; do not add YAML attributes to index files.

## Workflow

1. Classify the task as authoring, editing, index update, validation, or impact analysis.
2. Inspect the target requirement root and read relevant requirement documents plus nearby `@.md` and `=.md` files.
3. Load only the needed references:
   - Syntax details: `references/syntax.md`
   - Editing procedures: `references/workflows.md`
   - Ambiguous choices: `references/decision-rules.md`
   - Validation checklist: `references/validation.md`
   - Before/after examples: `references/examples.md`
4. Apply changes to requirement bodies first, then update indexes.
5. Validate with `scripts/validate_reqmd.py <requirement-root>` when possible.
6. Report changed requirement sections, changed index files, validation results, and unresolved review items.

## Core Rules

- Identifiers use `SCREAMING_SNAKE_CASE`.
- General helpers use `snake_case`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`, and preserve actual code/model names.
- Treat requirement bodies as the source of truth and indexes as derived traceability data.
- Do not rename identifiers or implementation helpers unless the user explicitly asks.
- Do not delete uncertain traceability links silently; report them as review items.

## Index Fragment Rules

Index files use two different fragment targets. Keep them separate.

- Index section headings link to source document sections.
  - Example: `## [SW_BLC_CONTROL](SwReq.md#sw_blc_control-brake-lamp-control-software)`
  - The fragment is based on the source requirement/design/test Markdown heading.
- Index section body list items link to other index sections.
  - Example: `- [SYS_BLC_CONTROL](../sys/@#sys_blc_control)`
  - Example: `- [=BrakeLampReq](../swdd/=#brakelampreq)`
  - The fragment is based on the target index section heading's visible text, not the source document heading.
- Never use bare index links such as `@`, `=`, `path/@`, or `path/=` inside index files.
- Use VS Code-compatible Markdown heading anchors.

## Scripts

- `scripts/validate_reqmd.py <root>` checks naming, index YAML bans, index fragments, duplicate index sections, and reachable index-section fragments.
- `scripts/update_index.py <root>` adds missing index sections and source-section links inferred from requirement documents.

Review script output before relying on it for traceability semantics.
