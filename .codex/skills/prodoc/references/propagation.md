# ProDoc Propagation

Use this reference when applying `propagation_docs`.

## Direction Semantics

`lateral` targets are at the same abstraction level.
Update them to preserve consistency in terms, interfaces, constraints, decisions, and traceability.
Do not turn a lateral update into a higher-level policy rewrite or a lower-level implementation expansion.

`upstream` targets are more abstract.
Collect detailed RequirementSection changes into higher-level requirements, policy, architecture, or intent.
Use the target document's `knowledge_files` to interpret terminology, policy, architecture background, and prior decisions.
Because upstream edits can change intent, report a review item unless the required edit is direct and unambiguous.

`downstream` targets are more concrete.
Split higher-level or mid-level changes into detailed requirements, design, implementation guidance, verification conditions, validation scenarios, or operational instructions.

## Chain Propagation

When a propagation target is also ProDoc:

1. Create a Queue item with target document, incoming change, direction, and source document.
2. Parse the target document's own frontmatter.
3. Run `UpdateContent(document, incoming_change, direction)`.
4. Record body changed content as changed RequirementSection IDs and change summaries.
5. Record input-output trace relationships.
6. Update ReqMd indexes when trace relationship changes require it.
7. If there is body changed content, no blocking review item, and the target has `propagation_docs`, enqueue target-specific propagation items.

Use the current propagation path stack to detect cycles.
Use processed Queue item history to avoid repeated work.
Consider at least target document, source document, direction, input RequirementSection IDs, and incoming change content when deciding whether a Queue item is repeated.

## Stop Conditions

Stop the current Queue item when:

- a propagation target file, ReqMd index, or requirement ID is missing;
- automatic editing would alter intent and requires user judgment;
- the same Queue item has already been processed;
- a review item blocks automatic propagation.

Stop the whole propagation when the current propagation path would cycle.

Always include the stop reason in the final report when propagation was requested.
