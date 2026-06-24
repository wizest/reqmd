# ProDoc Frontmatter Schema

Use this reference when creating, repairing, or validating `reqmd_prodoc` frontmatter.

## Detection

A Markdown document is ProDoc when its YAML frontmatter contains the top-level key `reqmd_prodoc`.
If the key is missing, do not apply the ProDoc workflow unless the user explicitly asks to convert the document to ProDoc.

## Fields

`requirement_refs` is required for ProDoc authoring and validation.
It declares ReqMd requirements the document artifact must satisfy.
These requirements are about the document type, structure, content, quality, and traceability; they are not necessarily the product requirements described inside the document.

Shape:

```yaml
requirement_refs:
  - path/to/reqmd-root-or-index:
    - REQ_ID_1
    - REQ_ID_2
```

`knowledge_files` is optional.
Use it for domain context such as product descriptions, design background, terminology, policies, and writing rules.

```yaml
knowledge_files:
  - knowledge.md
```

`propagation_docs` is optional.
Use it to declare documents affected by changes to the current document.

```yaml
propagation_docs:
  lateral:
    - peer.md
  upstream:
    - parent.md
  downstream:
    - child.md
```

## Path And Missing-Value Rules

- Resolve relative paths from the ProDoc document directory.
- Treat empty lists as explicitly declared with no targets.
- Treat missing optional fields as no work for that step.
- If a requirement index, requirement ID, knowledge file, or propagation target is missing, report it as a review item.
- Do not invent IDs, create placeholder target files, or silently remove missing references unless the user explicitly asks.

## Validation Script

When available, run:

```bash
python claude/prodoc/scripts/validate_prodoc.py <file-or-root>
```

The script validates the supported ProDoc frontmatter subset, checks that `requirement_refs` IDs exist in the referenced ReqMd `@.md` index, and checks that `knowledge_files` and `propagation_docs` targets exist.
It intentionally uses no external YAML dependency.
