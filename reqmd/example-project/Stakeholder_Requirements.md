---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SYS_1_BP_1
      - SYS_1_BP_2
      - SYS_1_BP_3
      - SYS_1_BP_4
      - WP_17_00
  propagation_docs:
    upstream:
      - Project_Management_Plan.md
    downstream:
      - System_Requirements.md
      - Validation_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# Stakeholder Requirements

## [STK_REQ_BRAKE_ASSIST](@) Brake assist expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: High
```

- When the driver applies the brake pedal rapidly, the vehicle shall provide brake assist support to reduce stopping distance.
- When the brake assist function is unavailable, the vehicle shall preserve normal braking behavior.
- When this stakeholder expectation is recorded, the project shall record the driver as the stakeholder source and keep the expectation status available for agreement and change analysis.
- If the brake assist expectation changes, then the project shall analyze impact on system requirements, validation scenarios, project scope, and support management before accepting the change.

## [STK_REQ_DRIVER_FEEDBACK](@) Driver feedback expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: Medium
```

- When brake assist support is active, the vehicle shall provide driver-visible feedback through the instrument cluster.
- If a brake assist diagnostic fault is active, then the vehicle shall provide a driver-visible warning.
- When this stakeholder expectation is agreed, the project shall record affected parties for driver interface, service, system engineering, and validation review.
- If the feedback expectation changes, then the project shall communicate the changed status and disposition to affected parties.

## [STK_REQ_SERVICE_DIAGNOSTICS](@) Service diagnostics expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: Medium
```

- When a service tool requests brake assist diagnostic information, the system shall provide current diagnostic status and stored fault information.
- When this stakeholder expectation is recorded, the project shall record service as the stakeholder source and retain the requirement status for communication.
- If the diagnostic expectation changes, then the project shall assess service impact, validation impact, and change-control need before updating downstream documents.
