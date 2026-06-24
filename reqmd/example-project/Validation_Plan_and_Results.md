---
reqmd_prodoc:
  requirement_refs:
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
```

- When [STK_REQ_BRAKE_ASSIST](@) is validated, the validation measure shall evaluate rapid brake pedal application in representative vehicle operating conditions.
- When the brake assist validation measure is specified, the plan shall define pass/fail criteria, entry criteria, exit criteria, vehicle or simulation environment, selected operating conditions, and stakeholder expectation coverage.
- When the brake assist validation is performed, the result record shall include validation measure data, pass/fail status, and deviations routed to problem resolution.

## [VAL_DRIVER_FEEDBACK_SCENARIO](@) Driver feedback validation scenario

```yaml
Type: ValidationRequirement
Status: Draft
Technique: UserEvaluation
```

- When [STK_REQ_DRIVER_FEEDBACK](@) is validated, the validation measure shall evaluate that driver indications are understandable during active support and confirmed diagnostic faults.
- When the driver feedback validation measure is specified, the plan shall define pass/fail criteria for active and warning indications, entry and exit criteria, evaluator role, and required instrument-cluster environment.
- When driver feedback validation is performed, the result record shall include pass/fail status and stakeholder-oriented evidence.

## [VAL_SERVICE_DIAGNOSTICS_SCENARIO](@) Service diagnostics validation scenario

```yaml
Type: ValidationRequirement
Status: Draft
Technique: ServiceScenario
```

- When [STK_REQ_SERVICE_DIAGNOSTICS](@) is validated, the validation measure shall evaluate service tool access to brake assist status and stored fault information.
- When the service diagnostics validation measure is specified, the plan shall define pass/fail criteria for current status and stored fault access, entry and exit criteria, service tool environment, and expected data fields.
- When service diagnostics validation is performed, the result record shall include validation measure data and pass/fail status.

## [VAL_TRACEABILITY](@) Validation traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
```

- When validation measures or results are changed, the project shall maintain bidirectional traceability to stakeholder requirements, system requirements, and verification results through the ReqMd skill workflow for the `@.md` identifier index.
- When validation measures and results are reviewed, the project shall maintain consistency between validation scenarios, stakeholder expectations, system requirements, verification evidence, and problem-resolution records.
