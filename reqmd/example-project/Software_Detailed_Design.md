---
reqmd_prodoc:
  requirement_refs:
    - ../example-aspice:
      - SWE_3_BP_1
      - SWE_3_BP_2
      - SWE_3_BP_3
      - SWE_3_BP_4
      - SWE_3_BP_5
      - WP_04_05
      - WP_11_05
  propagation_docs:
    upstream:
      - Software_Architecture.md
      - Software_Requirements.md
    downstream:
      - Verification_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# Software Detailed Design

## [SW_DD_FILTER_ALGORITHM](@) Filter algorithm design

```yaml
Type: SoftwareDetailedDesign
Status: Draft
Owner: Software Design
Unit: BrakeAssistFilter
Rationale: Implements filtered acceleration input for activation decision.
```

- When [SW_ARCH_INPUT_FILTER](@) is realized, the detailed design shall compute filtered pedal acceleration from the latest valid pedal samples using a bounded moving average.
- When static aspects of the filter unit are specified, the detailed design shall define inputs, outputs, calibration parameters, internal buffer, and invalid-sample status.
- When dynamic aspects of the filter unit are specified, the detailed design shall define initialization, sample update, bounded averaging, and invalid-sample rejection sequence.

## [SW_DD_DECISION_STATE_MACHINE](@) Decision state machine design

```yaml
Type: SoftwareDetailedDesign
Status: Draft
Owner: Software Design
Unit: BrakeAssistDecision
Rationale: Implements activation and fail-silent behavior in one state machine.
```

- When [SW_ARCH_DECISION_LOGIC](@) is realized, the detailed design shall define inactive, candidate, active, and fault-inhibited states for brake assist request computation.
- If [SW_REQ_FAIL_SILENT_OUTPUT](@) applies, then the state machine shall transition to fault-inhibited and command inactive output.
- When the decision unit is developed, the software unit shall expose deterministic state transition functions and shall isolate calibration thresholds from state transition code.
- When the decision unit design is analyzed, the project shall record rationale that fault-inhibited transitions override candidate and active transitions.

## [SW_DD_STATUS_INTERFACE](@) Status interface design

```yaml
Type: SoftwareDetailedDesign
Status: Draft
Owner: Software Design
Unit: BrakeAssistStatus
Rationale: Implements status outputs and diagnostic service data.
```

- When [SW_ARCH_DIAGNOSTIC_COMMUNICATION](@) is realized, the detailed design shall map internal active state and confirmed fault state to communication signals and diagnostic service responses.
- When static aspects of the status unit are specified, the detailed design shall define active indication, warning indication, availability, active state, and confirmed fault outputs.
- When dynamic aspects of the status unit are specified, the detailed design shall define periodic signal publication and request-driven diagnostic response behavior.

## [SW_DD_TRACEABILITY](@) Detailed design traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
```

- When software detailed design elements are changed, the project shall maintain bidirectional traceability to software architecture, software requirements, and software unit verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When detailed design and software units are agreed, the project shall communicate static design, dynamic design, developed unit boundaries, rationale, and verification impact to affected parties.
