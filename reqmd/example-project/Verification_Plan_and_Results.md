---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SWE_4_BP_1
      - SWE_4_BP_2
      - SWE_4_BP_3
      - SWE_4_BP_4
      - SWE_4_BP_5
      - SWE_5_BP_1
      - SWE_5_BP_2
      - SWE_5_BP_3
      - SWE_5_BP_4
      - SWE_5_BP_5
      - SWE_5_BP_6
      - SWE_5_BP_7
      - SWE_6_BP_1
      - SWE_6_BP_2
      - SWE_6_BP_3
      - SWE_6_BP_4
      - SWE_6_BP_5
      - SYS_4_BP_1
      - SYS_4_BP_2
      - SYS_4_BP_3
      - SYS_4_BP_4
      - SYS_4_BP_5
      - SYS_5_BP_1
      - SYS_5_BP_2
      - SYS_5_BP_3
      - SYS_5_BP_4
      - SYS_5_BP_5
      - WP_13_25
      - WP_08_60
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    upstream:
      - System_Requirements.md
      - System_Architecture.md
      - Software_Requirements.md
      - Software_Architecture.md
      - Software_Detailed_Design.md
    lateral:
      - Validation_Plan_and_Results.md
      - Support_Management.md
---

# Verification Plan and Results

## [VER_UNIT_FILTER_TEST](@) Unit verification for filter algorithm

```yaml
Type: VerificationRequirement
Status: Draft
Level: SoftwareUnit
Technique: UnitTest
SelectionCriteria: Unit boundary risk, requirement priority, regression impact
ExecutionStatus: Planned
```

- When [SW_DD_FILTER_ALGORITHM](@) is verified, the unit test shall demonstrate that filtered pedal acceleration is computed from valid samples and rejects invalid samples.
- When the filter unit verification measure is specified, the plan shall define pass/fail criteria for valid-sample averaging, invalid-sample rejection, boundary value ranges, entry criteria for detailed design availability, exit criteria for recorded results, abort and restart criteria, and required unit-test harness infrastructure.
- When the filter unit verification measure is selected, the project shall record that unit-test coverage is required because the filter unit affects high-priority activation behavior and regression risk.
- When filter unit verification is summarized, the project shall communicate selected measure rationale, executed result status, deviations, and regression impact to detailed design and project-management stakeholders.
- When the filter unit verification is performed, the result record shall include execution date, object under verification, pass/fail status, verification data, logs, and measured evidence for each criterion.
- If the filter unit verification is not executed, then the result record shall include the not-executed status and rationale.

## [VER_UNIT_DECISION_TEST](@) Unit verification for decision state machine

```yaml
Type: VerificationRequirement
Status: Draft
Level: SoftwareUnit
Technique: UnitTest
SelectionCriteria: State transition coverage, fail-silent priority, regression impact
ExecutionStatus: Planned
```

- When [SW_DD_DECISION_STATE_MACHINE](@) is verified, the unit test shall demonstrate active request, inactive request, and fault-inhibited transitions.
- When the decision unit verification measure is specified, the plan shall define pass/fail criteria for each state transition, entry and exit criteria, abort and restart criteria, test data, fault-injection conditions, and unit-test harness infrastructure.
- When the decision unit verification measure is selected, the project shall record that state-transition and fault-injection coverage is required because fail-silent behavior has priority over activation behavior.
- When decision unit verification is summarized, the project shall communicate selected measure rationale, executed result status, deviations, and regression impact to detailed design and project-management stakeholders.
- When the decision unit verification is performed, the result record shall include execution date, object under verification, pass/fail status, verification data, logs, and measured evidence for transition coverage.
- If a decision unit verification result deviates from expected behavior, then the project shall route the deviation to problem resolution.
- If the decision unit verification is not executed, then the result record shall include the not-executed status and rationale.

## [VER_SOFTWARE_INTEGRATION_TEST](@) Software integration verification

```yaml
Type: VerificationRequirement
Status: Draft
Level: SoftwareIntegration
Technique: IntegrationTest
SelectionCriteria: Architecture interface coverage, integration sequence, timing dependency
ExecutionStatus: Planned
```

- When [SW_ARCH_INPUT_FILTER](@), [SW_ARCH_DECISION_LOGIC](@), and [SW_ARCH_DIAGNOSTIC_COMMUNICATION](@) are integrated, the integration test shall demonstrate signal flow from validated inputs to pressure request, indication output, and diagnostic status.
- When software integration verification is specified, the plan shall define integration sequence, preconditions, interface checks, timing checks, pass/fail criteria, entry and exit criteria, abort and restart criteria, and required integration environment.
- When software integration verification is selected, the project shall record that interface dataflow and timing coverage are required for static and dynamic software architecture consistency.
- When software integration verification is summarized, the project shall communicate selected integration measure rationale, integration result status, deviations, and regression impact to software architecture and project-management stakeholders.
- When software integration verification is performed, the result record shall include execution date, integrated software configuration, object under verification, verification measure data, logs, and pass/fail status.
- If software integration verification is not executed, then the result record shall include the not-executed status and rationale.

## [VER_SYSTEM_VERIFICATION_TEST](@) System verification

```yaml
Type: VerificationRequirement
Status: Draft
Level: System
Technique: SystemTest
SelectionCriteria: System requirement priority, integrated system readiness, release scope
ExecutionStatus: Planned
```

- When [SYS_REQ_BRAKE_ASSIST_ACTIVATION](@), [SYS_REQ_NORMAL_BRAKING_PRESERVATION](@), [SYS_REQ_DRIVER_INDICATION](@), and [SYS_REQ_DIAGNOSTIC_STATUS](@) are verified, the system test shall demonstrate expected behavior on the integrated system.
- When system verification is specified, the plan shall define system integration preconditions, pass/fail criteria, entry and exit criteria, abort and restart criteria, necessary sequence, required test environment, and evidence to show compliance with system requirements.
- When system verification is selected, the project shall record that the measure covers release-scope system requirements and regression risk from stakeholder or system requirement changes.
- When system verification is summarized, the project shall communicate selected system verification measure rationale, verification result status, deviations, and release-readiness impact to system engineering, validation, and project-management stakeholders.
- When system verification is performed, the result record shall include execution date, integrated system configuration, object under verification, verification measure data, logs, and pass/fail status.
- If system verification is not executed, then the result record shall include the not-executed status and rationale.

## [VER_TRACEABILITY](@) Verification traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
Summary: Unit, integration, software, and system verification result summary
```

- When verification measures or results are changed, the project shall maintain bidirectional traceability to requirements, architecture, detailed design, validation, and verification result work products through the ReqMd skill workflow for the `@.md` identifier index.
- When verification results are recorded, the project shall maintain consistency between verification measures, verification results, software units, architecture elements, requirements, and problem-resolution records.
- When verification results are summarized, the project shall report passed, not passed, not executed, and deviating verification results with rationale, affected work products, problem-resolution links, and communication evidence.
- When verification evidence is summarized, the project shall summarize passed, not passed, not executed, and deviating verification results by verification level and communicate the impact to affected requirements, architecture, detailed design, validation, and support stakeholders.
- When verification coverage is reviewed, the project shall confirm that verification measures trace to software units, software architecture, software requirements, system architecture, system requirements, and that verification results trace back to the executed measures.
