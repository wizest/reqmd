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

1. Run `python .codex\skills\prodoc\scripts\plan_propagation.py <root> <start-doc> --input-section <REQ_ID> --summary "<change>"`.
2. Process emitted `QUEUE` entries in order.
3. Parse only the current target document's own frontmatter.
4. Run `UpdateContent(document, incoming_change, direction)`.
5. Record body changed content as changed RequirementSection IDs and change summaries.
6. Record input-output trace relationships.
7. Update ReqMd indexes when trace relationship changes require it.
8. If the current target produces `changed_content`, rerun `plan_propagation.py` from that target to plan the next hop.
9. Report script `REVIEW` items; do not manually follow recursive links outside the emitted Queue plan.

Use this Queue item shape:

```text
target: path/to/target.md
source: path/to/source.md
direction: self | lateral | upstream | downstream
input_sections: REQ_ID[, REQ_ID...]
change_summary: one short sentence
```

Use the current propagation path stack to detect cycles.
Use processed Queue item history to avoid repeated work.
Consider at least target document, source document, direction, input RequirementSection IDs, and incoming change content when deciding whether a Queue item is repeated.
Process one Queue item completely before reading the next target document.
The planning script performs graph traversal, cycle detection, and repeated Queue item detection. Its default depth is one hop to keep context small. Treat its `REVIEW` output as the propagation boundary.

## Stop Conditions

Stop the current Queue item when:

- a propagation target file, ReqMd index, or requirement ID is missing;
- automatic editing would alter intent and requires user judgment;
- the same Queue item has already been processed;
- a review item blocks automatic propagation.

Stop the whole propagation when the current propagation path would cycle.

Always include the stop reason in the final report when propagation was requested.

## Output Groups

Report propagation results in these groups:

- `changed_content`: target document, changed RequirementSection IDs, and short summaries.
- `trace`: input RequirementSection IDs mapped to output RequirementSection IDs.
- `reqmd_index`: affected ReqMd roots and validation results.
- `review`: missing evidence, unclear intent, missing target files, missing requirement IDs, cycles, or repeated Queue items.
