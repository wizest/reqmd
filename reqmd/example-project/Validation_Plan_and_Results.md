---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - VAL_1_BP_1
      - VAL_1_BP_2
      - VAL_1_BP_3
      - VAL_1_BP_4
      - VAL_1_BP_5
      - WP_13_24
      - WP_08_59
  propagation_docs:
    upstream:
      - Stakeholder_Requirements.md
      - System_Requirements.md
      - Verification_Plan_and_Results.md
    lateral:
      - Project_Management_Plan.md
      - Support_Management.md
---

# Validation Plan and Results

## [VAL_BRAKE_ASSIST_SCENARIO](@) Brake assist validation scenario

```yaml
Type: ValidationRequirement
Status: Draft
Technique: VehicleScenario
SelectionCriteria: Intended use coverage, stakeholder priority, operational target environment
ExecutionStatus: Planned
```

- When [STK_REQ_BRAKE_ASSIST](@) is validated, the validation measure shall evaluate rapid brake pedal application in representative vehicle operating conditions.
- When the brake assist validation measure is specified, the plan shall define pass/fail criteria, entry criteria, exit criteria, abort and restart criteria, vehicle or simulation environment, selected operating conditions, validation sequence, and stakeholder expectation coverage.
- When the brake assist validation measure is selected, the project shall record that the scenario covers intended-use braking support in the operational target environment and release scope.
- When the brake assist validation is performed, the result record shall include execution date, participants, validation measure data, logs or feedback, pass/fail status, and deviations routed to problem resolution.
- If the brake assist validation is not executed, then the result record shall include the not-executed status and rationale.

## [VAL_DRIVER_FEEDBACK_SCENARIO](@) Driver feedback validation scenario

```yaml
Type: ValidationRequirement
Status: Draft
Technique: UserEvaluation
SelectionCriteria: End-user satisfaction, driver interface risk, regression impact
ExecutionStatus: Planned
```

- When [STK_REQ_DRIVER_FEEDBACK](@) is validated, the validation measure shall evaluate that driver indications are understandable during active support and confirmed diagnostic faults.
- When the driver feedback validation measure is specified, the plan shall define pass/fail criteria for active and warning indications, entry and exit criteria, abort and restart criteria, evaluator role, validation sequence, and required instrument-cluster environment.
- When the driver feedback validation measure is selected, the project shall record that user evaluation is required because indication clarity affects stakeholder satisfaction and operational use.
- When driver feedback validation is performed, the result record shall include execution date, participants, pass/fail status, user feedback, and stakeholder-oriented evidence.
- If driver feedback validation is not executed, then the result record shall include the not-executed status and rationale.

## [VAL_SERVICE_DIAGNOSTICS_SCENARIO](@) Service diagnostics validation scenario

```yaml
Type: ValidationRequirement
Status: Draft
Technique: ServiceScenario
SelectionCriteria: Service stakeholder expectation, diagnostic data coverage, regression impact
ExecutionStatus: Planned
```

- When [STK_REQ_SERVICE_DIAGNOSTICS](@) is validated, the validation measure shall evaluate service tool access to brake assist status and stored fault information.
- When the service diagnostics validation measure is specified, the plan shall define pass/fail criteria for current status and stored fault access, entry and exit criteria, abort and restart criteria, service tool environment, validation sequence, and expected data fields.
- When the service diagnostics validation measure is selected, the project shall record that service diagnostic coverage is required for intended use by service stakeholders and release readiness.
- When service diagnostics validation is performed, the result record shall include execution date, participants, validation measure data, service tool logs, and pass/fail status.
- If service diagnostics validation is not executed, then the result record shall include the not-executed status and rationale.

## [VAL_TRACEABILITY](@) Validation traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
Summary: Validation result summary and affected-party communication evidence
```

- When validation measures or results are changed, the project shall maintain bidirectional traceability to stakeholder requirements, system requirements, and verification results through the ReqMd skill workflow for the `@.md` identifier index.
- When validation measures and results are reviewed, the project shall maintain consistency between validation scenarios, stakeholder expectations, system requirements, verification evidence, and problem-resolution records.
- When validation results are summarized, the project shall summarize passed, not passed, not executed, and deviating validation results with rationale and impact on intended-use expectations.
- When validation results are communicated, the project shall communicate the validation result summary, stakeholder impact, unresolved deviations, and release-readiness impact to affected parties.
