---
name: prodoc
description: Create, edit, validate, and propagate ProDoc Markdown documents that use `reqmd_prodoc` frontmatter to drive agent behavior. Use when Codex needs to work with programmable documentation, ProDoc frontmatter, ReqMd-backed requirement references, `knowledge_files`, `propagation_docs`, multi-step propagation across ProDoc documents, or when ProDoc changes require invoking the ReqMd skill for ReqMd `@.md` identifier index updates.
---

# ProDoc

Use this skill for Markdown documents whose YAML frontmatter contains `reqmd_prodoc:`.
ProDoc documents are programmable documentation: the frontmatter declares document requirements, domain knowledge sources, and propagation targets that guide how the document should be written, checked, and propagated.

ProDoc works on top of ReqMd. When editing requirement sections or `@.md` identifier indexes, invoke and follow the ReqMd skill. ProDoc does not define, extend, or override ReqMd identifier index rules.

## Core Rules

- Treat `reqmd_prodoc` frontmatter as the execution contract for the document.
- Use `requirement_refs` to determine what the document itself must satisfy. These are requirements about the document artifact, not necessarily requirements about the product described by the document.
- Use `knowledge_files` only as supporting domain context. Do not treat knowledge files as mandatory requirements unless the ProDoc requirements say so.
- Use `propagation_docs` to identify affected lateral, upstream, and downstream documents.
- Use the ReqMd skill for any ReqMd `@.md` identifier index update caused by propagation.
- Do not silently delete uncertain traceability; report uncertain relationships as review items.
- Track visited ProDoc documents during propagation to prevent cycles.

## Workflow

1. Identify the ProDoc document by checking for YAML frontmatter containing `reqmd_prodoc:`.
2. Parse `requirement_refs`, `knowledge_files`, and `propagation_docs`.
3. Read the referenced ReqMd identifier indexes and source requirement sections named by `requirement_refs`.
4. Read only the relevant `knowledge_files`.
5. Create or edit the ProDoc body so it satisfies the referenced document requirements and uses the knowledge context.
6. Validate the body against referenced requirements and record missing, conflicting, or uncertain items.
7. If `propagation_docs` is present, analyze lateral, upstream, and downstream impacts.
8. Apply safe propagation updates to target documents.
9. If changed lateral/upstream/downstream relationships require ReqMd `@.md` updates, use the ReqMd skill to perform those updates.
10. Repeat propagation for target ProDoc documents that also declare `propagation_docs`, using the target document's own changes as the next changed content.
11. Stop when there are no affected targets, no actual document/index changes, a visited ProDoc would repeat, a referenced file/ID is missing, or user judgment is needed.
12. Report changed ProDoc documents, referenced requirement IDs, propagation actions, identifier index updates, validation results, and review items.

## Frontmatter Handling

Read `references/schema.md` when creating, repairing, or validating ProDoc frontmatter.

Minimum supported shape:

```yaml
---
reqmd_prodoc:
  requirement_refs:
    - path/to/reqmd-index:
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

Path rules:

- Resolve paths relative to the ProDoc document directory.
- Treat `requirement_refs` as required for ProDoc authoring and validation.
- Treat `knowledge_files` and `propagation_docs` as optional.
- Treat empty lists as explicitly declared with no targets.
- If a referenced file or requirement ID is missing, do not invent a replacement; report it.

## Propagation

Read `references/propagation.md` before performing propagation.

Direction meanings:

- `lateral`: same abstraction level; keep peer documents consistent without abstracting or concretizing the content.
- `upstream`: more abstract direction; summarize detailed changes as impacts on higher-level requirements, policies, architecture, or intent. Prefer review items over automatic edits when the change affects intent.
- `downstream`: more concrete direction; translate higher-level changes into detailed design, implementation, verification, validation, or operational work products.

When a target document is also ProDoc and declares `propagation_docs`, first update that target document, then treat it as the current ProDoc document and propagate the target document's actual changed content.

## ReqMd Identifier Index Updates

Use the ReqMd skill before editing any ReqMd `@.md` file.
Do not use ProDoc-specific identifier index rules, relationship formats, fragments, or validation criteria.
Treat all identifier index behavior as owned by ReqMd.

When propagation changes requirement relationships:

- Switch to the ReqMd skill for the affected requirement root.
- Follow the ReqMd skill's current workflow, references, scripts, and validation checklist.
- Report the ReqMd skill actions and validation results in the ProDoc final report.

## Validation Checklist

Before finishing:

- Run `python .codex/skills/prodoc/scripts/validate_prodoc.py <file-or-root>` when the ProDoc validator is available.
- Confirm YAML frontmatter parses and contains `reqmd_prodoc`.
- Confirm every `requirement_refs` index path and ID exists.
- Confirm referenced knowledge files exist or are reported as review items.
- Confirm propagation target files exist or are reported as review items.
- Confirm any ReqMd `@.md` edits were made through the ReqMd skill.
- Run the ReqMd skill's validation workflow for affected requirement roots when available.
- Report any missing files, missing IDs, cycles, ambiguous upstream changes, and unresolved traceability decisions.


