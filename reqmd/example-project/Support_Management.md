---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SUP_1_BP_3
      - SUP_1_BP_4
      - SUP_1_BP_5
      - SUP_1_BP_6
      - SUP_1_BP_7
      - SUP_8_BP_1
      - SUP_8_BP_2
      - SUP_8_BP_3
      - SUP_8_BP_4
      - SUP_8_BP_5
      - SUP_8_BP_6
      - SUP_8_BP_7
      - SUP_8_BP_8
      - SUP_9_BP_1
      - SUP_9_BP_2
      - SUP_9_BP_3
      - SUP_9_BP_4
      - SUP_9_BP_5
      - SUP_9_BP_6
      - SUP_9_BP_7
      - SUP_10_BP_1
      - SUP_10_BP_2
      - SUP_10_BP_3
      - SUP_10_BP_4
      - SUP_10_BP_5
      - SUP_10_BP_6
      - WP_13_08
      - WP_13_16
      - WP_13_07
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    lateral:
      - Project_Management_Plan.md
      - Verification_Plan_and_Results.md
      - Validation_Plan_and_Results.md
---

# Support Management

## [SUP_BASELINE_CONTROL](@) Baseline control

```yaml
Type: SupportRequirement
Status: Draft
Owner: Configuration Management
```

- When a project baseline is established, configuration management shall include all ProDoc work products, ReqMd identifier indexes, verification evidence, validation evidence, and approved change records.
- When configuration items are identified, configuration management shall record selection criteria, owner, version, status, release milestone, baseline membership, and project-status relationship for each ProDoc document and ReqMd index.
- If a baseline item is modified, then configuration management shall control the modification through change history and approved change request status before updating the baseline.
- When configuration status is summarized, configuration management shall communicate baseline completeness, configuration item consistency, backup or recovery readiness, and unresolved configuration deviations to affected parties.

## [SUP_CHANGE_TRACEABILITY](@) Change request traceability

```yaml
Type: SupportRequirement
Status: Draft
Owner: Change Management
```

- When a change request affects a stakeholder requirement, system requirement, architecture element, design element, verification measure, or validation measure, change management shall update impacted ProDoc documents and ReqMd `@.md` identifier index links through the ReqMd skill workflow.
- When a change request is identified, change management shall record the request, affected work products, requester, reason, status, and required analysis criteria.
- When a change request is assessed, change management shall record impact on scope, lifecycle milestone, feasibility assumption, schedule, resource allocation, stakeholder commitment, affected baseline, affected verification or validation evidence, and disposition.
- When traceability is affected by a change request, change management shall maintain bidirectional traceability between the change request, stakeholder requirement source, affected work products, consistency evidence, and closure status.
- When a change request is approved, implemented, and closed, change management shall record approval status, implementation confirmation, closure evidence, unresolved risk, and communication evidence.

## [SUP_PROBLEM_RESOLUTION](@) Problem resolution traceability

```yaml
Type: SupportRequirement
Status: Draft
Owner: Problem Resolution
```

- When a problem is identified in verification or validation, problem resolution shall record the affected requirement, design, verification, validation, baseline, and change request relationships.
- When a problem is identified, problem resolution shall record the problem description, source, affected work products, initial status, and responsible owner.
- When a problem is analyzed, problem resolution shall record cause, impact, risk, required corrective action, and related change request.
- When a problem is tracked to closure, problem resolution shall record closure evidence, recurrence-prevention action, affected project progress status, and verify that affected ProDoc documents and traceability remain consistent.
- When urgent action or alert notification is required, problem resolution shall record authorization, affected parties, alert content, initiated resolution action, and communicated problem-resolution status.

## [SUP_QUALITY_EVIDENCE](@) Quality assurance evidence

```yaml
Type: SupportRequirement
Status: Draft
Owner: Quality Assurance
```

- When a ProDoc work product is reviewed, quality assurance shall record whether the work product satisfies its `requirement_specs`, propagation expectations, and ReqMd skill validation for identifier index consistency.
- When quality assurance reviews work products or process activities, quality assurance shall apply documented quality criteria for stakeholder source identification, affected-party agreement, change analysis, scope, lifecycle, feasibility, schedule, skills, commitments, consistency, progress reporting, record review evidence, record quality conformance evidence, and trigger corrective action for deviations.
- If quality assurance identifies a nonconformance, then quality assurance shall communicate the finding to affected parties and track the corrective action to closure.
- When quality assurance activities are summarized, quality assurance shall communicate quality status, unresolved nonconformances, escalation status, corrective action status, and affected work products to project management and affected process owners.
