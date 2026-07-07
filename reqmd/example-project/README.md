# Example Project ProDoc Set

This folder contains sample project work products written as ProDoc Markdown documents.
Each document uses `reqmd_prodoc` frontmatter and declares `requirement_specs` from the Automotive SPICE process and work product requirements in `../example-aspice`.

The sample project is a compact brake assist controller example used to demonstrate requirement, architecture, design, verification, validation, and support work products.

`Project_Knowledge.md` provides shared domain and responsibility context for ProDoc `UpdateContent` operations.

Propagation is intentionally connected through nearby abstraction levels. For example, a change in `SW_REQ_ACTIVATION_DECISION` should propagate downstream to software architecture and verification, while its upstream impact is summarized toward system requirements or system architecture rather than copied verbatim. RequirementSection-level relationships created by those updates are maintained in `@.md`.
