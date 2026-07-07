---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SWE_3_BP_1
      - SWE_3_BP_2
      - SWE_3_BP_3
      - SWE_3_BP_4
      - SWE_3_BP_5
      - WP_04_05
      - WP_11_05
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    upstream:
      - Software_Architecture.md
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
UnitBoundary: BrakeAssistFilter conceptual software unit
Inputs: PedalSample[-100..100 %], BrakePressure[0..250 bar], SampleValidity[boolean]
Outputs: FilteredPedalAcceleration[-200..200 %/s], InvalidSampleStatus[boolean]
DataStructures: Bounded sample buffer, validity counter
Rationale: Implements filtered acceleration input for activation decision.
```

- When [SW_ARCH_INPUT_FILTER](@) is realized, the detailed design shall compute filtered pedal acceleration from the latest valid pedal samples using a bounded moving average.
- When static aspects of the filter unit are specified, the detailed design shall define inputs, outputs, calibration parameters, internal buffer, and invalid-sample status.
- When dynamic aspects of the filter unit are specified, the detailed design shall define initialization, sample update, bounded averaging, and invalid-sample rejection sequence.
- When input and output formats are specified, the detailed design shall define application-domain value ranges and physical or measurement units for pedal sample, brake pressure, filtered pedal acceleration, and validity status.
- When the filter software unit is developed, the implementation shall apply range checks for sampled values and shall avoid implicit type conversions in the bounded averaging calculation.
- When the filter design is reviewed, the project shall record explanatory annotations for control flow, buffer update rules, calibration parameter usage, and invalid-sample handling.
- When the filter software unit is completed, the project shall communicate unit boundary, interface formats, construction constraints, and unit verification impact to verification stakeholders.

## [SW_DD_DECISION_STATE_MACHINE](@) Decision state machine design

```yaml
Type: SoftwareDetailedDesign
Status: Draft
Owner: Software Design
Unit: BrakeAssistDecision
UnitBoundary: BrakeAssistDecision conceptual software unit
Inputs: FilteredPedalAcceleration[-200..200 %/s], SignalValidity[boolean], DiagnosticFault[boolean]
Outputs: BrakeAssistRequest[Inactive|Active], DecisionState[Inactive|Candidate|Active|FaultInhibited]
DataStructures: Decision state variable, candidate confirmation counter
Rationale: Implements activation and fail-silent behavior in one state machine.
```

- When [SW_ARCH_DECISION_LOGIC](@) is realized, the detailed design shall define inactive, candidate, active, and fault-inhibited states for brake assist request computation.
- If [SW_REQ_FAIL_SILENT_OUTPUT](@) applies, then the state machine shall transition to fault-inhibited and command inactive output.
- When the decision unit is developed, the software unit shall expose deterministic state transition functions and shall isolate calibration thresholds from state transition code.
- When the decision unit design is analyzed, the project shall record rationale that fault-inhibited transitions override candidate and active transitions.
- When input and output formats are specified, the detailed design shall define state enumeration values, Boolean diagnostic inputs, request output values, and units for filtered pedal acceleration.
- When dynamic behavior is specified, the detailed design shall define transition guards, transition priority, one-entry one-exit transition evaluation, and candidate confirmation counter update behavior.
- When the decision software unit is developed, the implementation shall use explicit state enumeration checks and shall avoid hidden global state outside the documented decision state variable.
- When the decision software unit is completed, the project shall communicate state-machine behavior, transition priority, unit boundary, and unit verification impact to verification stakeholders.

## [SW_DD_STATUS_INTERFACE](@) Status interface design

```yaml
Type: SoftwareDetailedDesign
Status: Draft
Owner: Software Design
Unit: BrakeAssistStatus
UnitBoundary: BrakeAssistStatus conceptual software unit
Inputs: BrakeAssistRequest[Inactive|Active], InhibitionStatus[boolean], DiagnosticFault[boolean]
Outputs: ActiveIndication[boolean], WarningIndication[boolean], AvailabilityStatus[Available|Unavailable], DiagnosticResponse[record]
DataStructures: Status snapshot, diagnostic response record
Rationale: Implements status outputs and diagnostic service data.
```

- When [SW_ARCH_DIAGNOSTIC_COMMUNICATION](@) is realized, the detailed design shall map internal active state and confirmed fault state to communication signals and diagnostic service responses.
- When static aspects of the status unit are specified, the detailed design shall define active indication, warning indication, availability, active state, and confirmed fault outputs.
- When dynamic aspects of the status unit are specified, the detailed design shall define periodic signal publication and request-driven diagnostic response behavior.
- When input and output formats are specified, the detailed design shall define Boolean indication values, availability enumeration values, diagnostic response fields, and no-unit status semantics.
- When the status software unit is developed, the implementation shall keep periodic publication and request-driven diagnostic response code paths consistent through a shared status snapshot.
- When the status design is reviewed, the project shall record explanatory annotations for signal mapping, diagnostic response field mapping, and communication timing assumptions.
- When the status software unit is completed, the project shall communicate status snapshot structure, signal mapping, diagnostic response mapping, and unit verification impact to verification stakeholders.

## [SW_DD_TRACEABILITY](@) Detailed design traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
ConsistencyEvidence: Architecture-to-design, design-to-unit, design-to-requirement, unit-to-verification
```

- When software detailed design elements are changed, the project shall maintain bidirectional traceability to software architecture, software requirements, and software unit verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When developed software units are reviewed, the project shall confirm that each conceptual software unit boundary, input/output format, data structure, and control flow definition is consistent with the software architecture and related software requirements.
- When software detailed design is analyzed, the project shall record static consistency, dynamic consistency, unit construction constraints, interface-format consistency, and potential impact on unit verification.
- When software unit verification is planned, the project shall maintain traceability from each developed software unit to its detailed design section and corresponding software unit verification measure.
- When detailed design and software units are agreed, the project shall communicate static design, dynamic design, developed unit boundaries, rationale, and verification impact to affected parties.
