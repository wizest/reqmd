---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SWE_2_BP_1
      - SWE_2_BP_2
      - SWE_2_BP_3
      - SWE_2_BP_4
      - SWE_2_BP_5
      - WP_04_04
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    upstream:
      - Software_Requirements.md
      - System_Architecture.md
    downstream:
      - Software_Detailed_Design.md
      - Verification_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# Software Architecture

## [SW_ARCH_INPUT_FILTER](@) Input filter component

```yaml
Type: SoftwareArchitecture
Status: Draft
Owner: Software Architecture
View: StaticAndDynamic
Interfaces: RawSensorSample, SensorValidity, FilteredAcceleration, DiagnosticInputStatus
Timing: One control cycle input update
Parameters: PedalAccelerationThreshold, FilterWindowLength, InvalidSampleLimit
Modes: Normal, DegradedInput, Diagnostic
Rationale: Separates signal conditioning from decision logic.
```

- When [SW_REQ_ACTIVATION_DECISION](@) is implemented, the software architecture shall define an input filter component that validates and filters pedal and brake pressure signals.
- When the input filter static aspect is specified, the software architecture shall define required interfaces for raw sensor samples, sample timestamps, and validity flags, and provided interfaces for filtered acceleration, filtered signal validity, and diagnostic input status.
- When the input filter interface characteristics are specified, the software architecture shall define cyclic sample exchange, one-control-cycle update timing, validity flag semantics, and data ownership between sensing, filtering, and decision logic.
- When application parameters are specified, the software architecture shall define pedal acceleration threshold, filter window length, and invalid sample limit as calibratable parameters used by the input filter.
- When the input filter dynamic aspect is specified, the software architecture shall define sample acquisition, validation, filtering, invalid-sample rejection, and degraded-input behavior for normal, degraded input, and diagnostic modes.
- When the input filter is analyzed, the project shall record rationale that bounded filtering reduces false activation while preserving one-control-cycle activation feasibility.
- When the input filter architecture is agreed, the project shall communicate its interfaces, parameters, modes, timing assumptions, and traceability to detailed design and verification stakeholders.

## [SW_ARCH_DECISION_LOGIC](@) Decision logic component

```yaml
Type: SoftwareArchitecture
Status: Draft
Owner: Software Architecture
View: StaticAndDynamic
Interfaces: FilteredAcceleration, FilteredSignalValidity, BrakeAssistRequest, InhibitionStatus
Timing: One control cycle decision update
Parameters: ActivationThreshold, FaultInhibitPriority, CandidateConfirmationCount
Modes: Inactive, Candidate, Active, FaultInhibited
Rationale: Centralizes brake assist state transitions.
```

- When [SW_REQ_ACTIVATION_DECISION](@) and [SW_REQ_FAIL_SILENT_OUTPUT](@) are implemented, the software architecture shall define a decision logic component that computes brake assist request state and fail-silent output behavior.
- When the decision logic static aspect is specified, the software architecture shall define required interfaces for filtered acceleration, filtered signal validity, diagnostic fault status, and provided interfaces for brake assist request and inhibition status.
- When the decision logic interface characteristics are specified, the software architecture shall define synchronous function-call interaction with the input filter and diagnostic communication components within one control cycle.
- When application parameters are specified, the software architecture shall define activation threshold, candidate confirmation count, and fault-inhibit priority as parameters affecting decision behavior.
- When the decision logic dynamic aspect is specified, the software architecture shall define state transitions for inactive, candidate, active, and fault-inhibited states, including transition guards and priority of fault-inhibited transitions.
- When the decision logic is analyzed, the project shall record rationale that fail-silent output has priority over activation.
- When the decision logic is analyzed for project estimates, the project shall record timing and state-count assumptions used for detailed design, unit verification, and software integration planning.

## [SW_ARCH_DIAGNOSTIC_COMMUNICATION](@) Diagnostic and communication component

```yaml
Type: SoftwareArchitecture
Status: Draft
Owner: Software Architecture
View: StaticAndDynamic
Interfaces: ActiveIndication, WarningIndication, AvailabilityStatus, ActiveState, ConfirmedFaultStatus
Timing: Periodic publication and request-driven diagnostic response
Parameters: StatusPublicationPeriod, DiagnosticResponseTimeout
Modes: Normal, ActiveSupport, FaultConfirmed, ServiceRequest
Rationale: Groups status publication with diagnostic service response.
```

- When [SW_REQ_INDICATION_OUTPUT](@) and [SW_REQ_DIAGNOSTIC_REPORTING](@) are implemented, the software architecture shall define a diagnostic and communication component that publishes indication and diagnostic status.
- When communication static aspects are specified, the software architecture shall define required interfaces for brake assist request, inhibition status, and confirmed fault status, and provided interfaces for active indication, warning indication, availability status, active state, and confirmed fault status.
- When communication interface characteristics are specified, the software architecture shall define periodic signal publication, request-driven diagnostic service response, signal ownership, and status value semantics for vehicle communication integration.
- When application parameters are specified, the software architecture shall define status publication period and diagnostic response timeout as configurable communication parameters.
- When communication dynamic aspects are specified, the software architecture shall define update timing and state-dependent output behavior for normal operation, active support, confirmed fault, and service request handling.
- When communication behavior is analyzed, the project shall record rationale that indication publication and diagnostic response are grouped to keep externally visible status consistent.
- When diagnostic and communication architecture is agreed, the project shall communicate status value semantics, publication timing, diagnostic response timing, and interface ownership to detailed design, integration verification, and validation stakeholders.

## [SW_ARCH_TRACEABILITY](@) Software architecture traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
AnalysisCriteria: Timing, interface consistency, state coverage, parameter configurability
```

- When software architecture components are changed, the project shall maintain bidirectional traceability to software requirements, system architecture, software detailed design, and verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When software architecture consistency is checked, the project shall confirm that each software requirement affecting activation, fail-silent output, indication, or diagnostic reporting traces to at least one software architecture component and related verification work product.
- When software architecture analysis is performed, the project shall evaluate timing, interface consistency, state coverage, and parameter configurability, and shall record assumptions that affect project estimates for detailed design, integration, and verification.
- When software architecture analysis is performed, the project shall also record correctness, feasibility, verifiability, and potential impact on detailed design and verification measures.
- When software architecture information is reviewed, the project shall provide explanatory annotations for each component covering rationale, interfaces, application parameters, dynamic behavior, operating modes, and affected downstream work products.
- When software architecture is agreed, the project shall communicate static aspects, dynamic aspects, analysis rationale, and affected detailed design and verification impacts to affected parties.
