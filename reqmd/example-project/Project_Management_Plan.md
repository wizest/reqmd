---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - MAN_3_BP_1
      - MAN_3_BP_4
      - MAN_3_BP_8
      - MAN_3_BP_9
      - WP_08_56
      - WP_14_10
  propagation_docs:
    downstream:
      - Stakeholder_Requirements.md
      - System_Requirements.md
      - System_Architecture.md
      - Software_Requirements.md
      - Software_Architecture.md
      - Software_Detailed_Design.md
      - Verification_Plan_and_Results.md
      - Validation_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# Project Management Plan

## [PRJ_PLAN_SCOPE](@) Project scope

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When the brake assist controller project is planned, the project team shall define the scope as stakeholder requirements analysis, system requirements analysis, system architecture, software requirements, software architecture, software detailed design, verification, validation, configuration management, change management, problem resolution, and quality assurance.
- When scope changes are approved, the project team shall update impacted ProDoc work products and related ReqMd identifier index links through the ReqMd skill workflow.
- When the scope of work is defined, the project team shall identify all ProDoc work products as work packages with responsible discipline, expected input, expected output, and affected stakeholder group.
- If a requested work package is outside the brake assist controller scope, then project management shall record the exclusion and communicate the disposition to affected parties.

## [PRJ_PLAN_SCHEDULE](@) Project schedule

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When project work packages are planned, the project team shall schedule requirements work before architecture work, architecture work before detailed design, detailed design before verification, and verification before validation.
- When a downstream work product date changes, the project team shall analyze the impact on dependent work products and update affected propagation targets.
- When work packages are monitored, the project team shall record status, dependency, due date, and corrective action for each ProDoc work product.
- If a schedule deviation affects verification, validation, or release readiness, then project management shall create a change request or corrective action and update impacted work products.

## [PRJ_PLAN_CONSISTENCY](@) Project consistency control

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When a project work product is changed, the project team shall check consistency with [SUP_BASELINE_CONTROL](@), [SYS_REQ_TRACEABILITY](@), [SW_REQ_TRACEABILITY](@), and [VER_TRACEABILITY](@).
- If a change affects lateral, upstream, or downstream work products, then the project team shall update the relevant ReqMd `@.md` identifier index relationships through the ReqMd skill workflow.
- When consistency is checked, the project team shall compare scope, work package status, schedule, change requests, and baseline status across affected ProDoc documents.
- If inconsistency remains after review, then project management shall record escalation path, corrective action, and communication evidence.
