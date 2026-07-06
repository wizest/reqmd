---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - SYS_3_BP_1
      - SYS_3_BP_2
      - SYS_3_BP_3
      - SYS_3_BP_4
      - SYS_3_BP_5
      - WP_04_06
  propagation_docs:
    upstream:
      - System_Requirements.md
    downstream:
      - Software_Requirements.md
      - Software_Architecture.md
      - Verification_Plan_and_Results.md
    lateral:
      - Support_Management.md
---

# System Architecture

## [SYS_ARCH_SENSOR_INTERFACE](@) Sensor interface allocation

```yaml
Type: SystemArchitecture
Status: Draft
Owner: Systems Engineering
Lifecycle: Operation
Rationale: Reuses existing pedal and brake pressure sensing interfaces.
```

- When [SYS_REQ_BRAKE_ASSIST_ACTIVATION](@) is implemented, the system architecture shall allocate pedal position and brake pressure sensing to the sensor interface element.
- When the sensor interface is specified, the architecture shall define static interfaces for pedal position, brake pressure, signal validity, and sample timestamp data.
- When the sensor interface is analyzed, the project shall record that sensing availability and signal validity are special characteristics for brake assist behavior.

## [SYS_ARCH_BRAKE_ASSIST_CONTROLLER](@) Brake assist controller allocation

```yaml
Type: SystemArchitecture
Status: Draft
Owner: Systems Engineering
Lifecycle: Operation
Rationale: Allocates brake assist decision behavior to the software-controlled element.
```

- When brake assist logic is allocated, the system architecture shall allocate activation decision, diagnostic supervision, and indication request behavior to the brake assist controller software element.
- When the brake assist controller interaction is specified, the architecture shall define dynamic behavior for inactive, active, unavailable, and fault-confirmed operating modes.
- When the controller allocation is analyzed, the project shall record rationale for allocating decision logic to software rather than actuator hardware.

## [SYS_ARCH_ACTUATOR_INTERFACE](@) Actuator interface allocation

```yaml
Type: SystemArchitecture
Status: Draft
Owner: Systems Engineering
Lifecycle: Operation
Rationale: Keeps pressure support output separate from normal hydraulic braking.
```

- When [SYS_REQ_NORMAL_BRAKING_PRESERVATION](@) is implemented, the system architecture shall allocate brake pressure support request output to the actuator interface element with a fail-silent behavior on controller fault.
- When the actuator interface is specified, the architecture shall define static output interfaces for pressure support request and diagnostic inhibition status.
- When actuator behavior is analyzed, the project shall confirm the fail-silent allocation supports maintenance, repair, and decommissioning without changing normal braking.

## [SYS_ARCH_TRACEABILITY](@) System architecture traceability

```yaml
Type: TraceabilityRequirement
Status: Draft
```

- When system architecture elements are changed, the project shall maintain bidirectional traceability to system requirements, software requirements, software architecture, and verification work products through the ReqMd skill workflow for the `@.md` identifier index.
- When system architecture is agreed, the project shall communicate static interfaces, dynamic modes, special characteristics, rationale, and changed traceability to affected parties.
