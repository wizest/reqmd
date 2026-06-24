---
reqmd_prodoc:
  requirement_refs:
    - ../example-aspice:
      - SWE_2_BP_1
      - SWE_2_BP_2
      - SWE_2_BP_3
      - SWE_2_BP_4
      - SWE_2_BP_5
      - WP_04_04
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
Rationale: Separates signal conditioning from decision logic.
```

- When [SW_REQ_ACTIVATION_DECISION](@) is implemented, the software architecture shall define an input filter component that validates and filters pedal and brake pressure signals.
- When the input filter static aspect is specified, the software architecture shall define provided and required interfaces for raw sensor samples, validity flags, filtered acceleration, and diagnostic input status.
- When the input filter dynamic aspect is specified, the software architecture shall define sample acquisition, validation, filtering, and invalid-sample rejection behavior.

## [SW_ARCH_DECISION_LOGIC](@) Decision logic component

```yaml
Type: SoftwareArchitecture
Status: Draft
Owner: Software Architecture
View: StaticAndDynamic
Rationale: Centralizes brake assist state transitions.
```

- When [SW_REQ_ACTIVATION_DECISION](@) and [SW_REQ_FAIL_SILENT_OUTPUT](@) are implemented, the software architecture shall define a decision logic component that computes brake assist request state and fail-silent output behavior.
- When the decision logic dynamic aspect is specified, the software architecture shall define state transitions for inactive, candidate, active, and fault-inhibited states.
- When the decision logic is analyzed, the project shall record rationale that fail-silent output has priority over activation.

## [SW_ARCH_DIAGNOSTIC_COMMUNICATION](@) Diagnostic and communication component

```yaml
Type: SoftwareArchitecture
Status: Draft
Owner: Software Architecture
View: StaticAndDynamic
Rationale: Groups status publication with diagnostic service response.
```

- When [SW_REQ_INDICATION_OUTPUT](@) and [SW_REQ_DIAGNOSTIC_REPORTING](@) are implemented, the software architecture shall define a diagnostic and communication component that publishes indication and diagnostic status.
- When communication static aspects are specified, the software architecture shall define interfaces for active indication, warning indication, availability status, active state, and confirmed fault status.
- When communication dynamic aspects are specified, the software architecture shall define update timing for normal operation, active support, confirmed fault, and service request handling.

## [SW_ARCH_TRACEABILITY](@) Software architecture traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
```

- When software architecture components are changed, the project shall maintain bidirectional traceability to software requirements, system architecture, software detailed design, and verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When software architecture is agreed, the project shall communicate static aspects, dynamic aspects, analysis rationale, and affected detailed design and verification impacts to affected parties.
