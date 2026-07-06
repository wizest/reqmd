---
name: prodoc
description: Create, edit, validate, and propagate ProDoc Markdown documents that use `reqmd_prodoc` frontmatter with `requirement_specs`, `knowledge_files`, and `propagation_docs`. Use when Claude works on programmable documentation, document-artifact requirements, ProDoc body RequirementSections, lateral/upstream/downstream propagation, or ReqMd `@.md` identifier index updates caused by ProDoc changes.
---

# ProDoc

Use this skill for Markdown documents whose YAML frontmatter contains `reqmd_prodoc:`.
ProDoc uses frontmatter as an execution plan for authoring, validation, and propagation.

ProDoc works on top of ReqMd. Use the ReqMd skill before editing any ReqMd RequirementSection or `@.md` identifier index. ProDoc does not define ReqMd identifier index syntax.

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

Read [schema.md](references/schema.md) when creating, repairing, or validating ProDoc frontmatter.

Minimum supported shape:

```yaml
---
reqmd_prodoc:
  requirement_specs:
    - path/to/reqmd-root-or-index:
      - REQ_ID
  knowledge_files:
    - path/to/knowledge.md
  propagation_docs:
    lateral:
      - peer.md
    upstream:
      - parent.md
    downstream:
      - child.md
---
```

Resolve relative paths from the ProDoc document directory.

## UpdateContent

Use this conceptual operation for each ProDoc document:

```text
UpdateContent(document, incoming_change, direction)
```

- `document`: the ProDoc document being processed.
- `incoming_change`: the user request or source document body change being applied.
- `direction`: `self`, `lateral`, `upstream`, or `downstream`.

UpdateContent must return:

- body content change result (`changed_content`) with changed RequirementSection IDs and change summaries;
- trace relationship changes between input and output RequirementSections;
- review items that block automatic propagation.

Procedure:

1. Parse `requirement_specs`, `knowledge_files`, and `propagation_docs`.
2. Read referenced ReqMd indexes and source RequirementSections for `requirement_specs`.
3. Read relevant `knowledge_files`.
4. Identify input RequirementSections from `incoming_change` when available.
5. Interpret `incoming_change` according to `direction`.
6. Update the body only within the target document's responsibility and artifact requirements.
7. Record changed output RequirementSection IDs and summaries.
8. Record input-output trace relationships.
9. Validate the result against `requirement_specs`.
10. Record review items when the edit is missing evidence, changes intent, has unclear traceability, or cannot identify changed RequirementSections.

Do not enqueue propagation from a document when there is no body content change or when review items block automatic propagation.
If only trace relationships or ReqMd indexes change, update the index as needed and report that result without enqueueing downstream propagation.

## Propagation

Read [propagation.md](references/propagation.md) before applying `propagation_docs`.

Direction meanings:

- `lateral`: same abstraction level; preserve consistency without abstracting or concretizing.
- `upstream`: more abstract direction; collect detailed changes into higher-level requirements, policies, architecture, or intent. Use target `knowledge_files` to interpret terminology, policy, architecture background, and prior decisions.
- `downstream`: more concrete direction; split higher-level changes into detailed requirements, design, implementation guidance, verification conditions, validation scenarios, or operational instructions.

Queue item contents:

- target document;
- incoming change;
- propagation direction;
- source document.

The incoming change should include the source document, input RequirementSection IDs when known, and per-RequirementSection change summaries.

Queue processing:

1. Enqueue the initial user request as `direction: self`.
2. Dequeue one item at a time.
3. Skip non-ProDoc documents.
4. Parse the target document frontmatter.
5. Run `UpdateContent`.
6. Apply ReqMd index updates when trace relationship changes require them.
7. If there is body `changed_content`, no blocking review item, and the target has `propagation_docs`, enqueue target-specific propagation items.
8. Stop when the queue is empty.

Use a current propagation path stack to detect cycles. Use processed Queue item history to prevent repeated processing. Consider at least target document, source document, direction, input RequirementSection IDs, and incoming change content when deciding whether a Queue item is repeated.

## ReqMd Identifier Index Updates

Use the ReqMd skill before editing any ReqMd `@.md` file.
When propagation creates, changes, or removes RequirementSection relationships:

- switch to the ReqMd skill for the affected requirement root;
- follow ReqMd index format and validation rules;
- report changed relationships and validation results.

## Validation Checklist

Before finishing:

- Run `python claude/prodoc/scripts/validate_prodoc.py <file-or-root>` when available.
- Confirm YAML frontmatter parses and contains `reqmd_prodoc`.
- Confirm every `requirement_specs` index path and ID exists.
- Confirm referenced `knowledge_files` exist or are reported.
- Confirm `propagation_docs` targets exist or are reported.
- Confirm created or edited body content satisfies `requirement_specs`.
- Confirm input RequirementSections, output RequirementSections, and trace relationships are identified at RequirementSection level.
- Confirm any ReqMd `@.md` edits were made through the ReqMd skill.
- Confirm propagation path and Queue item history prevent cycles or repeated processing.
- Report changed ProDoc documents, `requirement_specs` IDs, propagation actions, ReqMd index updates, validation results, and review items.
