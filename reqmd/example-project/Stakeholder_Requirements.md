---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SYS_1_BP_1
      - SYS_1_BP_2
      - SYS_1_BP_3
      - SYS_1_BP_4
      - WP_13_52
      - WP_15_51
      - WP_17_00
      - WP_17_54
  knowledge_files:
    - Project_Knowledge.md
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
Source: Driver
AgreementStatus: Proposed
AffectedParties: Driver, Systems Engineering, Validation, Project Management
Release: Demonstrator
```

- When the driver applies the brake pedal rapidly, the vehicle shall provide brake assist support to reduce stopping distance.
- When the brake assist function is unavailable, the vehicle shall preserve normal braking behavior.
- When this stakeholder expectation is recorded, the project shall record the driver as the stakeholder source and keep the expectation status available for agreement and change analysis.
- When this stakeholder expectation is agreed, the project shall record agreement evidence from driver representation, systems engineering, validation, and project management affected parties.
- If the brake assist expectation changes, then the project shall analyze impact on system requirements, validation scenarios, project scope, and support management before accepting the change.

## [STK_REQ_DRIVER_FEEDBACK](@) Driver feedback expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: Medium
Source: Driver
AgreementStatus: Proposed
AffectedParties: Driver Interface, Service, Systems Engineering, Validation
Release: Demonstrator
```

- When brake assist support is active, the vehicle shall provide driver-visible feedback through the instrument cluster.
- If a brake assist diagnostic fault is active, then the vehicle shall provide a driver-visible warning.
- When this stakeholder expectation is agreed, the project shall record affected parties for driver interface, service, system engineering, and validation review.
- When this stakeholder expectation is analyzed, the project shall record understandability, feasibility, verifiability, and potential negative impact on driver interface behavior.
- If the feedback expectation changes, then the project shall communicate the changed status and disposition to affected parties.

## [STK_REQ_SERVICE_DIAGNOSTICS](@) Service diagnostics expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: Medium
Source: Service
AgreementStatus: Proposed
AffectedParties: Service, Diagnostics, Systems Engineering, Validation
Release: Demonstrator
```

- When a service tool requests brake assist diagnostic information, the system shall provide current diagnostic status and stored fault information.
- When this stakeholder expectation is recorded, the project shall record service as the stakeholder source and retain the requirement status for communication.
- When this stakeholder expectation is agreed, the project shall record agreement evidence from service, diagnostics, systems engineering, and validation affected parties.
- If the diagnostic expectation changes, then the project shall assess service impact, validation impact, and change-control need before updating downstream documents.

## [STK_REQ_PROJECT_COMMUNICATION](@) Project communication expectation

```yaml
Type: StakeholderRequirement
Status: Draft
Priority: Medium
Source: Project Management
AgreementStatus: Proposed
AffectedParties: Project Management, Customer Interface, Systems Engineering, Validation, Support Management
Release: Demonstrator
```

- When stakeholder expectations are agreed for the demonstrator release, the project shall communicate release scope, affected stakeholder group, representative role, information need, and agreed commitment status to affected parties.
- If project scope, lifecycle milestone, feasibility assumption, schedule, or progress status changes, then the project shall communicate the changed status and disposition to affected stakeholder groups before accepting affected stakeholder requirement updates.

## [STK_REQ_AGREEMENT_STATUS](@) Stakeholder agreement and status control

```yaml
Type: TraceabilityRequirement
Status: Draft
Priority: High
Source: SYS.1
AgreementStatus: Proposed
AffectedParties: Project Management, Systems Engineering, Validation, Support Management
Release: Demonstrator
```

- When a stakeholder requirement is recorded, the stakeholder requirements document shall identify the source, affected parties, release scope, agreement status, and current disposition for that requirement.
- When stakeholder requirements are agreed, the project shall maintain communication evidence showing explicit agreement from affected parties and shall keep the agreed requirement set available for downstream system requirements and validation planning.
- If a stakeholder requirement changes, then the project shall record the object under analysis, analysis criteria, decision, rationale, assumptions, potential negative impact, risk, and required change-control or mitigation action before updating downstream ProDoc documents.
