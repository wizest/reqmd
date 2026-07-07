---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SYS_2_BP_1
      - SYS_2_BP_2
      - SYS_2_BP_3
      - SYS_2_BP_4
      - SYS_2_BP_5
      - SYS_2_BP_6
      - WP_17_00
      - WP_17_54
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    upstream:
      - Stakeholder_Requirements.md
    downstream:
      - System_Architecture.md
      - Software_Requirements.md
      - Verification_Plan_and_Results.md
    lateral:
      - Validation_Plan_and_Results.md
      - Support_Management.md
---

# System Requirements

## [SYS_REQ_BRAKE_ASSIST_ACTIVATION](@) Brake assist activation

```yaml
Type: SystemRequirement
Status: Draft
Priority: High
Verification: SystemTest
Release: Demonstrator
Rationale: Derived from stakeholder brake assist expectation.
Source: STK_REQ_BRAKE_ASSIST
AgreementStatus: Proposed
```

- When [STK_REQ_BRAKE_ASSIST](@) applies and brake pedal deceleration exceeds the activation threshold, the system shall request brake assist pressure support within 50 ms.
- When the activation requirement is analyzed, the project shall confirm it is technically feasible for the selected brake controller platform and does not contradict normal braking preservation.
- When the activation requirement is agreed, the project shall communicate its status and system-context impact to architecture, software, verification, validation, and project management stakeholders.

## [SYS_REQ_NORMAL_BRAKING_PRESERVATION](@) Normal braking preservation

```yaml
Type: SystemRequirement
Status: Draft
Priority: High
Verification: SystemTest
Release: Demonstrator
Rationale: Preserves baseline braking behavior when support is unavailable.
Source: STK_REQ_BRAKE_ASSIST
AgreementStatus: Proposed
```

- If brake assist support is unavailable, then the system shall allow normal hydraulic braking without additional brake assist pressure request.
- When this requirement is analyzed, the project shall confirm fail-silent behavior is feasible in the actuator interface and compatible with diagnostic status handling.

## [SYS_REQ_DRIVER_INDICATION](@) Driver indication

```yaml
Type: SystemRequirement
Status: Draft
Priority: Medium
Verification: SystemTest
Release: Demonstrator
Rationale: Derived from stakeholder driver feedback expectation.
Source: STK_REQ_DRIVER_FEEDBACK
AgreementStatus: Proposed
```

- When [STK_REQ_DRIVER_FEEDBACK](@) applies and brake assist support is active, the system shall send a brake assist active indication to the instrument cluster.
- If a brake assist diagnostic fault is confirmed, then the system shall send a brake assist warning indication to the instrument cluster.
- When this requirement is structured, the project shall keep driver indication behavior separate from diagnostic service reporting while maintaining shared fault status consistency.

## [SYS_REQ_DIAGNOSTIC_STATUS](@) Diagnostic status

```yaml
Type: SystemRequirement
Status: Draft
Priority: Medium
Verification: SystemTest
Release: Demonstrator
Rationale: Derived from stakeholder service diagnostics expectation.
Source: STK_REQ_SERVICE_DIAGNOSTICS
AgreementStatus: Proposed
```

- When [STK_REQ_SERVICE_DIAGNOSTICS](@) applies and a service tool requests diagnostic status, the system shall provide current brake assist availability and stored diagnostic fault status.
- When this requirement is analyzed, the project shall confirm diagnostic status can be provided without changing the braking operating context.

## [SYS_REQ_TRACEABILITY](@) System requirements traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
Priority: High
```

- When system requirements are changed, the project shall maintain bidirectional traceability to stakeholder requirements, system architecture, software requirements, verification, and validation work products through the ReqMd skill workflow for the `@.md` identifier index.
- When a system requirement is changed, the project shall record consistency evidence for stakeholder coverage, system-context impact, and downstream work product impact.
- When stakeholder requirement agreement status or disposition changes, the project shall review affected system requirements for consistency before accepting downstream updates.
- When system requirements are agreed, the project shall communicate agreed system requirements, requirement attributes, analysis rationale, system-context impact, and unresolved risks to affected architecture, software, verification, validation, and project-management parties.
