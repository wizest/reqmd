---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SUP_1_BP_3
      - SUP_1_BP_4
      - SUP_8_BP_1
      - SUP_8_BP_4
      - SUP_8_BP_5
      - SUP_9_BP_1
      - SUP_9_BP_2
      - SUP_9_BP_6
      - SUP_10_BP_1
      - SUP_10_BP_2
      - SUP_10_BP_4
      - WP_13_08
      - WP_13_16
      - WP_13_07
  propagation_docs:
    lateral:
      - Project_Management_Plan.md
      - Stakeholder_Requirements.md
      - System_Requirements.md
      - System_Architecture.md
      - Software_Requirements.md
      - Software_Architecture.md
      - Software_Detailed_Design.md
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
- When configuration items are identified, configuration management shall record selection criteria, owner, version, status, and baseline membership for each ProDoc document and ReqMd index.
- If a baseline item is modified, then configuration management shall control the modification through change history and approved change request status before updating the baseline.

## [SUP_CHANGE_TRACEABILITY](@) Change request traceability

```yaml
Type: SupportRequirement
Status: Draft
Owner: Change Management
```

- When a change request affects a requirement, architecture element, design element, verification measure, or validation measure, change management shall update impacted ProDoc documents and ReqMd `@.md` identifier index links through the ReqMd skill workflow.
- When a change request is identified, change management shall record the request, affected work products, requester, reason, status, and required analysis criteria.
- When a change request is assessed, change management shall record impact, risk, affected baseline, affected verification or validation evidence, and disposition.
- When traceability is affected by a change request, change management shall maintain bidirectional traceability between the change request, affected work products, consistency evidence, and closure status.

## [SUP_PROBLEM_RESOLUTION](@) Problem resolution traceability

```yaml
Type: SupportRequirement
Status: Draft
Owner: Problem Resolution
```

- When a problem is identified in verification or validation, problem resolution shall record the affected requirement, design, verification, validation, baseline, and change request relationships.
- When a problem is identified, problem resolution shall record the problem description, source, affected work products, initial status, and responsible owner.
- When a problem is analyzed, problem resolution shall record cause, impact, risk, required corrective action, and related change request.
- When a problem is tracked to closure, problem resolution shall record closure evidence and verify that affected ProDoc documents and traceability remain consistent.

## [SUP_QUALITY_EVIDENCE](@) Quality assurance evidence

```yaml
Type: SupportRequirement
Status: Draft
Owner: Quality Assurance
```

- When a ProDoc work product is reviewed, quality assurance shall record whether the work product satisfies its ASPICE requirement references, propagation expectations, and ReqMd skill validation for identifier index consistency.
- When quality assurance reviews work products or process activities, quality assurance shall apply documented quality criteria, record review evidence, record quality conformance evidence, and trigger corrective action for deviations.
- If quality assurance identifies a nonconformance, then quality assurance shall communicate the finding to affected parties and track the corrective action to closure.
