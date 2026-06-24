# ProDoc Propagation

Use this reference when applying `propagation_docs`.

## Direction Semantics

`lateral` targets are at the same abstraction level.
Update them to preserve consistency in terms, interfaces, constraints, decisions, and traceability.
Do not turn a lateral update into a higher-level policy rewrite or a lower-level implementation expansion.

`upstream` targets are more abstract.
Evaluate whether detailed changes imply a change to higher-level requirements, policy, architecture, or intent.
Because upstream edits can change intent, prefer reporting a review item unless the required edit is direct and unambiguous.

`downstream` targets are more concrete.
Translate higher-level or mid-level changes into detailed requirements, design, implementation guidance, verification conditions, validation scenarios, or operational instructions.

## Chain Propagation

When a propagation target is also ProDoc:

1. Update the target document for the incoming change.
2. Summarize the actual changed content in that target document.
3. Read the target document's own `propagation_docs`.
4. Propagate the target document's changed content to its targets.

Track visited ProDoc documents by normalized path.
Stop if the next target has already been visited.

## Stop Conditions

Stop propagation when:

- no target document is affected;
- the current step creates no document or index change;
- a visited ProDoc document would repeat;
- a propagation target file, ReqMd index, or requirement ID is missing;
- an upstream change would alter intent and requires user judgment.

Always include the stop reason in the final report when propagation was requested.
