# ReqMd LSP Requirements

This document defines implementation-ready requirements for a Language Server Protocol server that supports Markdown requirements written according to `markdown_for_requirements.md`.

The ReqMd LSP server shall support parsing, diagnostics, navigation, symbols, completion, code actions, index maintenance, and workspace updates for ReqMd requirement documents and index files.

## [REQMD_LSP_TRANSPORT_STDIO](@) Stdio transport

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When the [lsp_process](=) starts without an explicit transport option, the server shall read LSP JSON-RPC messages from [stdio_transport](=) and write responses and notifications to [stdio_transport](=).
- The [lsp_process](=) is the operating-system process that hosts the ReqMd LSP server, owns the JSON-RPC event loop, manages analysis state, and exits according to LSP shutdown semantics.
- The [stdio_transport](=) is the default bidirectional transport that reads framed JSON-RPC messages from standard input and writes framed JSON-RPC messages to standard output; logs must not be written to standard output.

## [REQMD_LSP_TRANSPORT_TCP](@) TCP transport option

```yaml
Type: Functional
Status: Draft
Priority: May
Source: markdown_for_requirements.md
Verification: Test
```

- When the [lsp_process](=) starts with a TCP host and port option, the server shall accept one LSP client connection through [tcp_transport](=).
- The [tcp_transport](=) is an optional socket transport for debugging or editor integrations that require TCP, and it shall use the same JSON-RPC framing semantics as the stdio transport.

## [REQMD_LSP_INITIALIZE_RESULT](@) Initialize result

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an LSP client sends an [initialize_request](=), the server shall return [server_capabilities](=) for text synchronization, diagnostics, document symbols, workspace symbols, definition, references, completion, document links, code actions, and execute command.
- The [initialize_request](=) is the LSP `initialize` request containing client capabilities, workspace folders, root URI, initialization options, and process metadata used before normal analysis begins.
- The [server_capabilities](=) value is the LSP capability object that declares every ReqMd feature the server can answer for Markdown documents.

## [REQMD_LSP_CAPABILITY_DOCUMENT_SELECTOR](@) Markdown document selector

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When the server reports [server_capabilities](=), the server shall restrict ReqMd language features to documents whose URI scheme is `file` and whose path ends with `.md`.

## [REQMD_LSP_SHUTDOWN_EXIT](@) Shutdown and exit

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: LSP
Verification: Test
```

- When the server receives [shutdown_request](=) followed by [exit_notification](=), the server shall stop accepting new analysis work and terminate the [lsp_process](=) with exit code `0`.
- The [shutdown_request](=) is the LSP `shutdown` request after which the server prepares to stop, and the [exit_notification](=) is the LSP notification that terminates the process.

## [REQMD_LSP_WORKSPACE_ROOT_DISCOVERY](@) Workspace root discovery

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a [workspace_folder](=) is opened, the server shall discover a [requirement_path](=) for each directory that contains at least one ReqMd Markdown document and optionally contains `@.md` or `=.md`.
- A [workspace_folder](=) is one client-provided root directory URI, and a [requirement_path](=) is a directory inside that root that forms one ReqMd traceability namespace with its requirement documents and index files.

## [REQMD_LSP_WORKSPACE_EXCLUDES](@) Workspace excludes

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When [lsp_configuration](=) contains excluded glob patterns, the server shall exclude matching files and directories from [workspace_scan](=), diagnostics, symbols, references, and index maintenance.
- The [lsp_configuration](=) is the merged server settings from initialization options, workspace configuration, and defaults; the [workspace_scan](=) is the bounded traversal that discovers Markdown files, ReqMd paths, and index files while honoring those settings.

## [REQMD_LSP_FILE_WATCHING](@) File watching

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the LSP client reports created, changed, renamed, or deleted Markdown files, the server shall update [workspace_index](=) entries affected by those file events.
- The [workspace_index](=) is the in-memory cross-document model for requirement sections, helper occurrences, index sections, relationship links, duplicate conditions, and URI-to-range mappings.

## [REQMD_LSP_TEXT_SYNC](@) Text document synchronization

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: LSP
Verification: Test
```

- When the client opens, changes, saves, or closes a text document, the server shall maintain an in-memory [document_snapshot](=) keyed by document URI and version.
- A [document_snapshot](=) contains the current versioned document text, line offsets, URI, document kind, parse result, and diagnostics derived from that exact version.

## [REQMD_LSP_INCREMENTAL_PARSE](@) Incremental parse

```yaml
Type: Performance
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When a document change affects only one section range, the server shall reparse the affected [requirement_section](=) or [general_section](=) and preserve unchanged parsed sections.
- A [requirement_section](=) is the ReqMd section that begins with an identifier link and contributes requirements, helpers, attributes, diagnostics, and generated index entries; a [general_section](=) is any other Markdown section and is excluded from requirement indexing.

## [REQMD_LSP_FULL_PARSE_FALLBACK](@) Full parse fallback

```yaml
Type: Reliability
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- If an incremental parse cannot determine a stable section boundary, then the server shall reparse the complete [document_snapshot](=).

## [REQMD_LSP_HEADING_DETECTION](@) Markdown heading detection

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When parsing Markdown, the server shall detect headings from one to six leading `#` characters followed by at least one space and heading text.

## [REQMD_LSP_REQUIREMENT_SECTION_DETECTION](@) Requirement section detection

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a Markdown heading starts with an [identifier_link](=), the server shall classify the heading and its nested content as a [requirement_section](=).
- An [identifier_link](=) is a ReqMd Markdown link whose visible text is an identifier and whose target points to `@`, `path/@`, `@#fragment`, or `path/@#fragment`.

## [REQMD_LSP_GENERAL_SECTION_DETECTION](@) General section detection

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a Markdown heading does not start with an [identifier_link](=), the server shall classify the heading and its content as a [general_section](=).

## [REQMD_LSP_SECTION_RANGE_MODEL](@) Section range model

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a section is parsed, the server shall record [source_range](=), heading range, body range, heading depth, title text, and parent section identifier when one exists.
- A [source_range](=) is a zero-based LSP range that identifies the exact document span for a parsed section, link, diagnostic, symbol, edit, or navigation target.

## [REQMD_LSP_FENCE_AWARE_PARSING](@) Fence aware parsing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- While a fenced code block is open, the server shall not treat Markdown links or heading-like text inside the fence as ReqMd identifiers, helpers, or sections.

## [REQMD_LSP_IDENTIFIER_LINK_PARSE](@) Identifier link parsing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When parsing an [identifier_link](=), the server shall extract link text, target path, index kind, fragment, title text, and [source_range](=).

## [REQMD_LSP_HELPER_LINK_PARSE](@) Helper link parsing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When parsing a [helper_link](=), the server shall extract helper text, target path, index kind, fragment, title text, implementation-helper flag, and [source_range](=).
- A [helper_link](=) is a ReqMd Markdown link whose visible text is a helper or implementation helper and whose target points to `=`, `path/=`, `=#fragment`, or `path/=#fragment`.

## [REQMD_LSP_ATTRIBUTE_PARSE](@) Attribute parsing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a YAML fenced block appears inside a [requirement_section](=), the server shall parse it as [requirement_attributes](=) for that section.
- The [requirement_attributes](=) block stores stable metadata such as type, status, priority, source, verification, variant, and owner for the containing requirement section.

## [REQMD_LSP_INDEX_FILE_CLASSIFICATION](@) Index file classification

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a file name is `@.md` or `=.md`, the server shall classify it as an [index_file](=) and parse index sections instead of requirement sections.
- An [index_file](=) is either `@.md` for identifier relationships or `=.md` for helper relationships, and it contains index headings and relationship list links without YAML attributes.

## [REQMD_LSP_INDEX_SECTION_PARSE](@) Index section parsing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When parsing an [index_file](=), the server shall parse each level-two heading link as an [index_section](=) and each list item link under it as an index relationship.
- An [index_section](=) is a level-two heading in an index file whose heading link points to a source document section and whose body links point to related index sections.

## [REQMD_LSP_VSCODE_ANCHOR_RULE](@) VS Code anchor rule

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When generating a Markdown fragment, the server shall use a VS Code compatible [markdown_anchor](=) derived from the visible heading text after Markdown links are replaced by their link text.
- A [markdown_anchor](=) is the heading fragment used by VS Code-compatible Markdown navigation after punctuation normalization and whitespace-to-hyphen conversion.

## [REQMD_LSP_WORKSPACE_INDEX_MODEL](@) Workspace index model

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a document is parsed, the server shall update [workspace_index](=) records for identifiers, helpers, requirement sections, index sections, source links, and relationship links.

## [REQMD_LSP_DUPLICATE_IDENTIFIER_MODEL](@) Duplicate identifier model

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When two [requirement_section](=) headings in the same [requirement_path](=) use the same identifier text, the server shall record a duplicate identifier condition in [workspace_index](=).

## [REQMD_LSP_DIAGNOSTIC_PUBLISHING](@) Diagnostic publishing

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: LSP
Verification: Test
```

- When analysis completes for an open document, the server shall publish LSP diagnostics with stable diagnostic codes, severity, message, range, and optional related information.

## [REQMD_LSP_IDENTIFIER_NAME_DIAGNOSTIC](@) Identifier name diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an [identifier_link](=) text does not match `[A-Z][A-Z0-9_]*`, the server shall report diagnostic code `REQMD001`.

## [REQMD_LSP_HELPER_NAME_DIAGNOSTIC](@) Helper name diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a non-implementation [helper_link](=) text does not match `[a-z][a-z0-9_]*`, the server shall report diagnostic code `REQMD002`.

## [REQMD_LSP_IMPLEMENTATION_HELPER_RULE](@) Implementation helper rule

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a [helper_link](=) text starts with `=`, the server shall classify it as an implementation helper and shall not apply the general helper naming diagnostic to the remaining text.

## [REQMD_LSP_MALFORMED_LINK_DIAGNOSTIC](@) Malformed link diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a ReqMd link target cannot be parsed as an identifier target or helper target, the server shall report diagnostic code `REQMD003`.

## [REQMD_LSP_INDEX_BARE_LINK_DIAGNOSTIC](@) Bare index link diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an [index_file](=) contains a link target equal to `@`, `=`, `path/@`, or `path/=`, the server shall report diagnostic code `REQMD004`.

## [REQMD_LSP_INDEX_FRAGMENT_DIAGNOSTIC](@) Unresolved index fragment diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an [index_file](=) link contains a fragment that does not resolve to an [index_section](=) in the target index file, the server shall report diagnostic code `REQMD005`.

## [REQMD_LSP_INDEX_YAML_DIAGNOSTIC](@) Index YAML diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an [index_file](=) contains a YAML fenced block, the server shall report diagnostic code `REQMD006`.

## [REQMD_LSP_DUPLICATE_INDEX_DIAGNOSTIC](@) Duplicate index diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When two [index_section](=) headings in the same [index_file](=) produce the same [markdown_anchor](=), the server shall report diagnostic code `REQMD007`.

## [REQMD_LSP_DUPLICATE_IDENTIFIER_DIAGNOSTIC](@) Duplicate identifier diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When two [requirement_section](=) headings in the same [requirement_path](=) use the same identifier text, the server shall report diagnostic code `REQMD008`.

## [REQMD_LSP_YAML_SYNTAX_DIAGNOSTIC](@) YAML syntax diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When [requirement_attributes](=) cannot be parsed as YAML mapping data, the server shall report diagnostic code `REQMD009`.

## [REQMD_LSP_MISSING_INDEX_SECTION_DIAGNOSTIC](@) Missing index section diagnostic

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When an [identifier_link](=) or significant [helper_link](=) appears in a [requirement_section](=) and the matching [index_section](=) is absent, the server shall report diagnostic code `REQMD010`.

## [REQMD_LSP_GENERAL_SECTION_EXCLUSION](@) General section exclusion

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When an [identifier_link](=) or [helper_link](=) appears only inside a [general_section](=), the server shall exclude that link from missing-index diagnostics and generated index sections.

## [REQMD_LSP_DOCUMENT_SYMBOL_REQUIREMENTS](@) Requirement document symbols

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When the client requests [document_symbols](=), the server shall return hierarchical symbols for [requirement_section](=) headings using the identifier as the symbol name and the heading subtitle as detail.
- The [document_symbols](=) response exposes the requirement and helper structure of the active Markdown document to the editor outline and symbol UI.

## [REQMD_LSP_DOCUMENT_SYMBOL_HELPERS](@) Helper document symbols

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the client requests [document_symbols](=), the server shall include helper symbols below the containing [requirement_section](=) when the client supports hierarchical document symbols.

## [REQMD_LSP_WORKSPACE_SYMBOL_SEARCH](@) Workspace symbol search

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the client requests [workspace_symbols](=) with a query string, the server shall return identifiers and helpers whose text contains the query using case-insensitive matching.
- The [workspace_symbols](=) response searches identifiers and helpers across the current workspace index.

## [REQMD_LSP_DEFINITION_IDENTIFIER_BODY](@) Identifier body definition

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When definition is requested on an [identifier_link](=) in a requirement document, the server shall return the matching [index_section](=) when the link target points to an index and a matching section exists.

## [REQMD_LSP_DEFINITION_INDEX_HEADING](@) Index heading definition

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When definition is requested on an [index_section](=) heading, the server shall return the source document section referenced by that heading link.

## [REQMD_LSP_DEFINITION_INDEX_RELATIONSHIP](@) Index relationship definition

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When definition is requested on an index relationship link, the server shall return the target [index_section](=) referenced by the relationship link fragment.

## [REQMD_LSP_REFERENCES_IDENTIFIER](@) Identifier references

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When references are requested for an identifier, the server shall return locations for matching [identifier_link](=) occurrences in requirement documents and [identifier_index](=) files.
- The [identifier_index](=) is the `@.md` index for a requirement path that maps requirement identifiers to source sections and related identifier index sections.

## [REQMD_LSP_REFERENCES_HELPER](@) Helper references

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When references are requested for a helper, the server shall return locations for matching [helper_link](=) occurrences in requirement documents and [helper_index](=) files.
- The [helper_index](=) is the `=.md` index for a requirement path that maps helpers to source sections and related helper index sections.

## [REQMD_LSP_COMPLETION_IDENTIFIER_TEXT](@) Identifier text completion

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When completion is requested inside identifier link text, the server shall offer known identifier names from the active [requirement_path](=) and reachable requirement paths.

## [REQMD_LSP_COMPLETION_HELPER_TEXT](@) Helper text completion

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When completion is requested inside helper link text, the server shall offer known helper names from the active [requirement_path](=), preserving implementation helper names exactly.

## [REQMD_LSP_COMPLETION_LINK_TARGET](@) Link target completion

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When completion is requested inside a ReqMd link target, the server shall offer valid `@`, `=`, `path/@`, `path/=`, `@#fragment`, and `=#fragment` forms according to the current document kind.

## [REQMD_LSP_HOVER_REQUIREMENT](@) Requirement hover

```yaml
Type: Functional
Status: Draft
Priority: May
Source: markdown_for_requirements.md
Verification: Test
```

- When hover is requested on an identifier, the server shall return the requirement title, source URI, status, priority, verification method, and first requirement body sentence when available.

## [REQMD_LSP_HOVER_HELPER](@) Helper hover

```yaml
Type: Functional
Status: Draft
Priority: May
Source: markdown_for_requirements.md
Verification: Test
```

- When hover is requested on a helper, the server shall return the helper kind, source URI, and related index relationships when available.

## [REQMD_LSP_DOCUMENT_LINKS](@) Document links

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the client requests [document_links](=), the server shall return document links for ReqMd identifier links, helper links, index source links, and index relationship links that resolve to a file location.
- The [document_links](=) response makes ReqMd source links and relationship links clickable when their targets can be resolved to document locations.

## [REQMD_LSP_CODE_ACTION_ADD_INDEX_SECTION](@) Add index section code action

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When diagnostic `REQMD010` is reported, the server shall offer a [code_action](=) that creates the missing [index_section](=) in the appropriate `@.md` or `=.md` file.
- A [code_action](=) is an LSP quick fix or command associated with a diagnostic that applies a deterministic workspace edit or invokes a server command.

## [REQMD_LSP_CODE_ACTION_REPAIR_BARE_INDEX_LINK](@) Repair bare index link code action

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When diagnostic `REQMD004` is reported and a unique target [index_section](=) exists, the server shall offer a [code_action](=) that appends the correct fragment to the bare index link.

## [REQMD_LSP_CODE_ACTION_REMOVE_INDEX_YAML](@) Remove index YAML code action

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When diagnostic `REQMD006` is reported, the server shall offer a [code_action](=) that removes only the YAML fenced block from the [index_file](=).

## [REQMD_LSP_RENAME_IDENTIFIER](@) Identifier rename

```yaml
Type: Functional
Status: Draft
Priority: May
Source: markdown_for_requirements.md
Verification: Test
```

- When a rename request targets an identifier and rename support is enabled, the server shall update matching ReqMd identifier link text and matching [index_section](=) headings in the same [requirement_path](=).

## [REQMD_LSP_RENAME_HELPER](@) Helper rename

```yaml
Type: Functional
Status: Draft
Priority: May
Source: markdown_for_requirements.md
Verification: Test
```

- When a rename request targets a non-implementation helper and rename support is enabled, the server shall update matching ReqMd helper link text and matching [index_section](=) headings in the same [requirement_path](=).

## [REQMD_LSP_RENAME_IMPLEMENTATION_HELPER_GUARD](@) Implementation helper rename guard

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a rename request targets an implementation helper, the server shall reject the request unless [lsp_configuration](=) explicitly enables implementation helper rename.

## [REQMD_LSP_EXECUTE_UPDATE_INDEX](@) Update index command

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the client executes [update_index_command](=), the server shall add missing identifier and helper [index_section](=) headings inferred from [requirement_section](=) content and shall preserve existing relationship list items.
- The [update_index_command](=) is the server command for adding missing index sections inferred from requirement sections while preserving existing relationship links.

## [REQMD_LSP_EXECUTE_VALIDATE_WORKSPACE](@) Validate workspace command

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When the client executes [validate_workspace_command](=), the server shall analyze all discovered ReqMd Markdown files and publish diagnostics for open files plus a summary notification.
- The [validate_workspace_command](=) is the server command that reruns ReqMd validation across discovered requirement paths and reports diagnostics plus a workspace-level summary.

## [REQMD_LSP_CONFIGURATION_SCHEMA](@) Configuration schema

```yaml
Type: Functional
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When [lsp_configuration](=) is loaded, the server shall support settings for requirement roots, excluded paths, diagnostic severities, update-index-on-save, rename support, and implementation-helper rename support.

## [REQMD_LSP_CONFIGURATION_DEFAULTS](@) Configuration defaults

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a setting is not provided, the server shall use defaults that enable diagnostics, disable automatic file writes, disable implementation helper rename, and exclude `.git` directories.

## [REQMD_LSP_SAVE_INDEX_POLICY](@) Save index policy

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When update-index-on-save is disabled, the server shall not modify `@.md` or `=.md` during document save.

## [REQMD_LSP_PATH_NORMALIZATION](@) Path normalization

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When resolving ReqMd links, the server shall normalize file URIs and relative paths without escaping outside the containing workspace folder.

## [REQMD_LSP_MULTI_ROOT_ISOLATION](@) Multi root isolation

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When multiple [workspace_folder](=) values are open, the server shall keep [workspace_index](=) records isolated by workspace folder unless a ReqMd link explicitly targets another folder through a relative path.

## [REQMD_LSP_ANALYSIS_CANCELLATION](@) Analysis cancellation

```yaml
Type: Performance
Status: Draft
Priority: Should
Source: LSP
Verification: Test
```

- When a newer document version is received while analysis is running, the server shall cancel obsolete analysis work for the older [document_snapshot](=).

## [REQMD_LSP_PERFORMANCE_SMALL_WORKSPACE](@) Small workspace performance

```yaml
Type: Performance
Status: Draft
Priority: Should
Source: markdown_for_requirements.md
Verification: Test
```

- When analyzing a workspace with 1,000 Markdown files and 20,000 ReqMd links, the server shall complete initial [workspace_scan](=) within 10 seconds on a typical developer workstation.

## [REQMD_LSP_PERFORMANCE_EDIT_LATENCY](@) Edit latency

```yaml
Type: Performance
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- When a user edits a document with 2,000 lines or fewer, the server shall publish updated diagnostics for that document within 500 milliseconds after receiving the change notification.

## [REQMD_LSP_ERROR_RESILIENCE](@) Error resilience

```yaml
Type: Reliability
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Test
```

- If a ReqMd Markdown document contains malformed Markdown, YAML, or links, then the server shall continue serving LSP requests and report recoverable diagnostics for the malformed content.

## [REQMD_LSP_LOGGING](@) Logging

```yaml
Type: Observability
Status: Draft
Priority: Should
Source: LSP
Verification: Review
```

- When analysis or command execution fails unexpectedly, the server shall send a concise error log message through LSP window logging without including full document contents.

## [REQMD_LSP_TEST_FIXTURES](@) Test fixtures

```yaml
Type: Verification
Status: Draft
Priority: Must
Source: markdown_for_requirements.md
Verification: Review
```

- When the LSP server is implemented, the project shall include test fixtures for valid documents, malformed documents, index files, duplicate sections, unresolved fragments, and multi-root workspaces.
