---
reqmd_prodoc:
  requirement_refs:
    - ../example-aspice:
      - SWE_1_BP_1
      - SWE_1_BP_2
      - SWE_1_BP_3
      - SWE_1_BP_4
      - SWE_1_BP_5
      - SWE_1_BP_6
      - WP_17_00
      - WP_17_54
  propagation_docs:
    upstream:
      - System_Requirements.md
      - System_Architecture.md
    downstream:
      - Software_Architecture.md
      - Software_Detailed_Design.md
      - Verification_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# Software Requirements

## [SW_REQ_ACTIVATION_DECISION](@) Activation decision

```yaml
Type: SoftwareRequirement
Status: Draft
Priority: High
Verification: SoftwareTest
Release: Demonstrator
Rationale: Refines system activation behavior into software decision behavior.
```

- When [SYS_REQ_BRAKE_ASSIST_ACTIVATION](@) applies and filtered pedal acceleration exceeds the configured threshold, the software shall set the brake assist request state to active within one control cycle.
- When this software requirement is analyzed, the project shall confirm threshold filtering, one-cycle response, and platform timing feasibility.
- When this software requirement is agreed, the project shall communicate the requirement and operating-environment impact to software architecture, detailed design, and verification stakeholders.

## [SW_REQ_FAIL_SILENT_OUTPUT](@) Fail-silent output

```yaml
Type: SoftwareRequirement
Status: Draft
Priority: High
Verification: SoftwareTest
Release: Demonstrator
Rationale: Refines system normal braking preservation into software output behavior.
```

- If sensor validity is false or a controller diagnostic fault is confirmed, then the software shall set the brake assist pressure request to inactive.
- When this software requirement is analyzed, the project shall confirm it is consistent with activation decision behavior and diagnostic reporting.

## [SW_REQ_INDICATION_OUTPUT](@) Indication output

```yaml
Type: SoftwareRequirement
Status: Draft
Priority: Medium
Verification: SoftwareTest
Release: Demonstrator
Rationale: Refines system driver indication behavior.
```

- When the brake assist request state is active, the software shall transmit an active indication signal to the vehicle communication interface.
- If a controller diagnostic fault is confirmed, then the software shall transmit a warning indication signal to the vehicle communication interface.
- When this software requirement is structured, the project shall keep active indication and warning indication as separately verifiable behavior.

## [SW_REQ_DIAGNOSTIC_REPORTING](@) Diagnostic reporting

```yaml
Type: SoftwareRequirement
Status: Draft
Priority: Medium
Verification: SoftwareTest
Release: Demonstrator
Rationale: Refines system diagnostic status behavior.
```

- When a diagnostic service requests brake assist status, the software shall report availability, active state, and confirmed diagnostic fault status.
- When this software requirement is analyzed, the project shall confirm service reporting is feasible within the communication interface and does not conflict with fail-silent output.

## [SW_REQ_TRACEABILITY](@) Software requirements traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
```

- When software requirements are changed, the project shall maintain bidirectional traceability to system requirements, system architecture, software architecture, detailed design, and verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When a software requirement is changed, the project shall record consistency evidence for system requirement coverage, operating-environment impact, architecture impact, and verification impact.
