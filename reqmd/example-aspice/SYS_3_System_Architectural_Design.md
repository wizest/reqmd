# [SYS_3_PROCESS](@.md#sys_3_process) System Architectural Design


Source: Automotive SPICE PAM v4.0, section SYS.3 System Architectural Design.

## Process purpose

The purpose is to establish an analyzed system architecture, comprising static and dynamic aspects, consistent with the system requirements.

## Process outcomes

1. A system architecture is designed including a definition of the system elements with their behavior, their interfaces, their relationships, and their interactions.
2. The system architecture is analyzed against defined criteria, and special characteristics are identified.
3. Consistency and bidirectional traceability are established between system architecture and system requirements.
4. The agreed system architecture and the special characteristics are communicated to all affected parties.

## Base practices

### [SYS_3_BP_1](@.md#sys_3_bp_1) Specify static aspects of the system architecture

```yaml
Type: BasePractice
Process: SYS.3
BasePractice: BP1
```

Specify and document the static aspects of the system architecture with respect to the functional and non-functional system requirements, including external interfaces and a defined set of system elements with their interfaces and relationships.

The practice shall produce or update:

- [wp_04_06_system_architecture](=.md#wp_04_06_system_architecture)

### [SYS_3_BP_2](@.md#sys_3_bp_2) Specify dynamic aspects of the system architecture

```yaml
Type: BasePractice
Process: SYS.3
BasePractice: BP2
```

Specify and document the dynamic aspects of the system architecture with respect to the functional and non-functional system requirements including the behavior of the system elements and their interaction in different system modes.

- Examples of interactions of system elements are timing diagrams reflecting inertia of mechanical components, processing times of ECUs, and signal propagation times of bus systems.

The practice shall produce or update:

- [wp_04_06_system_architecture](=.md#wp_04_06_system_architecture)

### [SYS_3_BP_3](@.md#sys_3_bp_3) Analyze system architecture

```yaml
Type: BasePractice
Process: SYS.3
BasePractice: BP3
```

Analyze the system architecture regarding relevant technical design aspects related to the product lifecycle, and to support project management regarding project estimates, and derive special characteristics for non-software system elements. Document a rationale for the system architectural design decisions.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.
- Examples for product lifecycle phases are production, maintenance & repair, decommissioning.
- Examples for technical aspects are manufacturability for production, suitability of pre-existing system elements to be reused, or availability of system elements.
- Examples for methods being suitable for analyzing technical aspects are prototypes, simulations, and qualitative analyses (e.g., FMEA approaches)
- Examples of design rationales are proven-in-use, reuse of a product platform or product line), a make-or-buy decision, or found in an evolutionary way (e.g., set-based design).

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)
- [wp_17_57_special_characteristics](=.md#wp_17_57_special_characteristics)

### [SYS_3_BP_4](@.md#sys_3_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SYS.3
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between the elements of the system architecture and the system requirements that represent properties or characteristics of the physical end product.

- Bidirectional traceability further supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- There may be non-functional requirements that the system architectural design does not trace to. Examples are do not address, or represent, direct properties or characteristics of the physical end product. Such requirements are still subject to verification.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SYS_3_BP_5](@.md#sys_3_bp_5) Communicate agreed system architecture

```yaml
Type: BasePractice
Process: SYS.3
BasePractice: BP5
```

Communicate the agreed system architecture, including the special characteristics, to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
