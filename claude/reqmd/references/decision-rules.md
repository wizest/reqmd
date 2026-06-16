# ReqMd Decision Rules

Apply these rules when the request or documents are ambiguous.

- Treat RequirementSection content as source of truth; treat `@.md` and `=.md` as derived indexes.
- Write RequirementBody content in EARS style before updating derived indexes.
- Treat GeneralSection content as explanatory text, not index input.
- If a body and an index disagree, update the index or report the conflict.
- Do not add YAML attributes to index files.
- Prefer reusing an existing helper when the concept is the same.
- Create a new helper when the semantics are different, even if names look similar.
- Use implementation helpers (`=ActualName`) when preserving code, model, port, data dictionary, or generated-symbol names matters.
- Do not rename implementation helpers to satisfy `snake_case`.
- Write only one direction of traceability unless project context explicitly requires both.
- Compute reverse relationships by scanning indexes instead of forcing duplicate links.
- Do not delete uncertain links. Mark them as review items.
- When a relationship type is not explicit, infer meaning from path context such as `sys`, `sw`, `swdd`, and `swqt`.
- If a fragment is missing in an index link, repair it to point to the matching section when the target exists.
- If the target section does not exist, create it only when the target entity is clearly present in source documents; otherwise report a missing target.
