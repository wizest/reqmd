---
name: reqmd
description: Create, edit, validate, and analyze ReqMd Markdown requirements, including RequirementSection and GeneralSection documents, RequirementSection YAML attributes, `@.md` identifier indexes, `=.md` helper indexes, traceability links, source-section fragments, index-section fragments, validation, and impact analysis.
---

# ReqMd

Use this skill when working with ReqMd requirement documents.

ReqMd is normal Markdown with project conventions:

- Requirement sections start with identifier links such as `## [SW_BLC_PEDAL_ON](@)`.
- RequirementSection bodies use EARS-style requirement statements.
- General sections do not start with identifiers and are not indexed.
- Requirement attributes are YAML blocks inside requirement sections.
- Identifier indexes are named `@.md`; helper indexes are named `=.md`.
- Index files contain headings and link lists only; do not add YAML attributes to index files.
- Identifier index headings link to source requirement sections; helper index headings are plain helper names without links.

## Workflow

Minimal context path:

1. For ordinary edits, read this file and `references/workflows.md` only.
2. Run `python .codex\skills\reqmd\scripts\reqmd_fix.py <requirement-root>` after edits.
3. Read `references/syntax.md`, `references/validation.md`, `references/decision-rules.md`, or `references/examples.md` only when the task or script output requires it.

1. Classify the task as authoring, editing, index update, validation, or impact analysis.
2. Work on one requirement path at a time. Do not edit unrelated directories in the same pass.
3. Inspect the target requirement file plus nearby `@.md` and `=.md` files.
4. Load only the needed reference for the task:
   - Syntax details: `references/syntax.md`
   - Editing procedures: `references/workflows.md`
   - Ambiguous choices: `references/decision-rules.md`
   - Validation checklist: `references/validation.md`
   - Before/after examples: `references/examples.md`
5. Apply changes to RequirementSection content first. Do not hand-rewrite whole index files.
6. Run `python .codex\skills\reqmd\scripts\reqmd_fix.py <requirement-root>` after content edits.
7. If validation still reports `REPAIRABLE`, run the named script once before editing by hand.
8. Treat `REVIEW` output as unresolved review items unless the source text makes the fix explicit.
9. Report changed requirement sections, changed index files, validation results, and unresolved review items.

For read-only analysis tasks, inspect only the relevant requirement paths and indexes before expanding scope.

When uncertain:

- Keep existing identifiers, helpers, implementation helpers, and semantic links unchanged.
- Add missing helper usage links inferred from RequirementSection bodies.
- Do not delete or rename links to make validation pass; report uncertain links instead.
- For impact analysis, report `confirmed`, `inferred`, and `review needed` groups separately.
- Do not invent cross-directory impact links. Only report links already found in indexes or source sections.

## Core Rules

- Identifiers use `SCREAMING_SNAKE_CASE`.
- General helpers use `snake_case`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`, and preserve actual code/model names.
- Write RequirementBody content with EARS-style conditions and responses, such as "When ...", "While ...", "Where ...", or "If ..., then ...".
- Treat requirement sections as source of truth and indexes as derived traceability data.
- Do not collect identifiers or helpers from GeneralSection content for indexes.
- Do not rename identifiers or implementation helpers unless the user explicitly asks.
- Do not delete uncertain traceability links silently; report them as review items.

## Index Fragment Rules

Index files use different fragment targets. Keep them separate.

- `@.md` headings link to source requirement sections.
- `=.md` headings are plain helper names.
- Index body links point to other index sections and must include fragments.
- Never use bare index links such as `@`, `=`, `path/@`, or `path/=` inside index files.
- Use `python .codex\skills\reqmd\scripts\reqmd_fix.py <root>` to generate and repair fragments.
- Read `references/syntax.md` only when fragment details are needed.

## Scripts

- `python .codex\skills\reqmd\scripts\validate_reqmd.py <root>` checks naming, index YAML bans, index fragments, duplicate index sections, reachable index-section fragments, missing source index sections, and missing helper usage links.
- `python .codex\skills\reqmd\scripts\reqmd_fix.py <root>` runs the standard repair pipeline: `update_index.py`, `repair_index_links.py`, then `validate_reqmd.py`.
- `python .codex\skills\reqmd\scripts\update_index.py <root>` adds missing index sections and usage links inferred from requirement sections. It skips GeneralSection content.
- `python .codex\skills\reqmd\scripts\repair_index_links.py <root>` repairs bare index links such as `@`, `=`, `path/@`, and `path/=` when the target index section already exists.
- `python .codex\skills\reqmd\scripts\analyze_impact.py <root> <identifier-or-helper> [...]` reports existing indexed impact links as `confirmed`, reverse indexed matches as `inferred`, and leaves semantic gaps as `review needed`.

Review script output before relying on it for traceability semantics.
