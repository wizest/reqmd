---
name: prodoc
description: Create, edit, validate, and propagate ProDoc Markdown documents that use `reqmd_prodoc` frontmatter with `requirement_specs`, `knowledge_files`, and `propagation_docs`. Use when Codex works on programmable documentation, document-artifact requirements, ProDoc body RequirementSections, lateral/upstream/downstream propagation, or ReqMd `@.md` identifier index updates caused by ProDoc changes.
---

# ProDoc

Use this skill for Markdown documents whose YAML frontmatter contains `reqmd_prodoc:`.
ProDoc uses frontmatter as an execution plan for authoring, validation, and propagation.

ProDoc works on top of ReqMd. Use the ReqMd skill before editing any ReqMd RequirementSection or `@.md` identifier index. ProDoc does not define ReqMd identifier index syntax.

## Minimal Context Path

Use the smallest context set that fits the task.

1. For frontmatter creation, repair, or validation, read this file and `references/schema.md`.
2. For body-only edits with no propagation, read this file, the target ProDoc, and only the referenced `requirement_specs` and `knowledge_files` needed for the edited sections.
3. For propagation, read this file and `references/propagation.md`; then process one target document at a time.
4. Run `python .codex\skills\prodoc\scripts\validate_prodoc.py <file-or-root>` before finishing when files are available.
5. Run `python .codex\skills\prodoc\scripts\extract_sections.py <prodoc.md>` before editing body sections.
6. Run `python .codex\skills\prodoc\scripts\resolve_specs.py <prodoc.md>` before reading requirement specs.
7. Use `python .codex\skills\prodoc\scripts\plan_propagation.py <root> <start-doc> --input-section <REQ_ID> --summary "<change>"` before propagation.
8. Use the ReqMd skill and `python .codex\skills\reqmd\scripts\reqmd_fix.py <requirement-root>` for any ReqMd RequirementSection or `@.md` index edit.

## Core Rules

- Treat `reqmd_prodoc` frontmatter as the execution contract for the document.
- Use `requirement_specs` as requirements the document artifact must satisfy: structure, required content, quality, and traceability criteria.
- Do not confuse `requirement_specs` with the product, system, design, implementation, verification, or operation requirements described in the ProDoc body.
- Use `knowledge_files` as supporting domain context for the body.
- Use `propagation_docs` to identify candidate target documents for `lateral`, `upstream`, and `downstream` propagation.
- During propagation, track changed body RequirementSections and input-output trace relationships.
- Use the ReqMd skill for ReqMd `@.md` updates caused by changed lateral/upstream/downstream relationships.
- Report uncertain, missing, conflicting, or judgment-dependent items instead of silently resolving them.

## Frontmatter

Read `references/schema.md` when creating, repairing, or validating ProDoc frontmatter.

Supported fields are `requirement_specs`, `knowledge_files`, and `propagation_docs`.
Resolve relative paths from the ProDoc document directory.
Report missing requirement indexes, requirement IDs, knowledge files, or propagation targets as review items.

## UpdateContent

Use this conceptual operation for each ProDoc document:

```text
UpdateContent(document, incoming_change, direction)
```

- `document`: the ProDoc document being processed.
- `incoming_change`: the user request or source document body change being applied.
- `direction`: `self`, `lateral`, `upstream`, or `downstream`.

Procedure:

1. Parse frontmatter and read only the needed requirement specs and knowledge files.
2. Identify input RequirementSections from `incoming_change` when available.
3. Update only the target document's responsible body sections.
4. Record changed output RequirementSection IDs, summaries, trace relationships, and review items.
5. Validate the result against `requirement_specs`.

Return this output contract for each document:

- `changed_content`: changed RequirementSection IDs and one-line summaries, or `none`.
- `trace`: input RequirementSection IDs mapped to output RequirementSection IDs, or `none`.
- `review`: blocking or uncertain items, or `none`.
- `next_queue`: propagation Queue items to enqueue, or `none`.

Validate saved result reports with `python .codex\skills\prodoc\scripts\validate_update_result.py <result.md> --source <source.md> --target <target.md>`.

Do not enqueue propagation from a document when there is no body content change or when review items block automatic propagation.
If only trace relationships or ReqMd indexes change, update the index as needed and report that result without enqueueing downstream propagation.

## Propagation

Read `references/propagation.md` before applying `propagation_docs`.

Queue processing:

1. Run `python .codex\skills\prodoc\scripts\plan_propagation.py <root> <start-doc> --input-section <REQ_ID> --summary "<change>"`.
2. Process the emitted `QUEUE` entries in order, one target document at a time.
3. Run `UpdateContent` for the current Queue item.
4. Apply ReqMd index updates when trace relationship changes require them.
5. If a target produces `changed_content` and `next_queue` is needed, rerun `plan_propagation.py` from that target.
6. Do not manually recurse beyond the emitted Queue plan; report script `REVIEW` items.

## ReqMd Identifier Index Updates

Use the ReqMd skill before editing any ReqMd `@.md` file.
When propagation creates, changes, or removes RequirementSection relationships:

- switch to the ReqMd skill for the affected requirement root;
- run `python .codex\skills\reqmd\scripts\reqmd_fix.py <requirement-root>` after ReqMd edits;
- follow ReqMd index format and validation rules;
- report changed relationships and validation results.

## Validation Checklist

Before finishing:

- Run `python .codex\skills\prodoc\scripts\validate_prodoc.py <file-or-root>` when available.
- Run `python .codex\skills\prodoc\scripts\extract_sections.py <prodoc.md>` when body RequirementSections changed.
- Run `python .codex\skills\prodoc\scripts\resolve_specs.py <prodoc.md>` when requirement specs guide the edit.
- Run `python .codex\skills\prodoc\scripts\validate_update_result.py <result.md> --source <source.md> --target <target.md>` when a result report is saved.
- Confirm frontmatter, `requirement_specs`, `knowledge_files`, and `propagation_docs` are valid or reported.
- Confirm edited body content satisfies `requirement_specs`.
- Confirm input/output RequirementSections and trace relationships are identified at RequirementSection level.
- Confirm any ReqMd edits used the ReqMd skill and validation.
- Report changed ProDoc documents, `requirement_specs` IDs, propagation actions, ReqMd index updates, validation results, and review items.


