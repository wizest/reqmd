# [SWE_2_PROCESS](@.md#swe_2_process) Software Architectural Design


Source: Automotive SPICE PAM v4.0, section SWE.2 Software Architectural Design.

## Process purpose

The purpose is to establish an analyzed software architecture, comprising static and dynamic aspects, consistent with the software requirements.

## Process outcomes

1. A software architecture is designed including static and dynamic aspects.
2. The software architecture is analyzed against defined criteria.
3. Consistency and bidirectional traceability are established between software architecture and software requirements.
4. The software architecture is agreed and communicated to all affected parties.

## Base practices

### [SWE_2_BP_1](@.md#swe_2_bp_1) Specify static aspects of the software architecture

```yaml
Type: BasePractice
Process: SWE.2
BasePractice: BP1
```

Specify and document the static aspects of the software architecture with respect to the functional and non-functional software requirements, including external interfaces and a defined set of software components with their interfaces and relationships.

- The hardware-software-interface (HSI) definition puts in context the hardware design and therefore is an aspect of system design ([SYS_3_PROCESS](@.md#sys_3_process)).

The practice shall produce or update:

- [wp_04_04_software_architecture](=.md#wp_04_04_software_architecture)

### [SWE_2_BP_2](@.md#swe_2_bp_2) Specify dynamic aspects of the software architecture

```yaml
Type: BasePractice
Process: SWE.2
BasePractice: BP2
```

Specify and document the dynamic aspects of the software architecture with respect to the functional and non- functional software requirements, including the behavior of the software components and their interaction in different software modes, and concurrency aspects.

- Examples for concurrency aspects are application-relevant interrupt handling, preemptive processing, multi-threading.
- Examples for behavioral descriptions are natural language or semi-formal notation (e.g, SysML, UML).

The practice shall produce or update:

- [wp_04_04_software_architecture](=.md#wp_04_04_software_architecture)

### [SWE_2_BP_3](@.md#swe_2_bp_3) Analyze software architecture

```yaml
Type: BasePractice
Process: SWE.2
BasePractice: BP3
```

Analyze the software architecture regarding relevant technical design aspects and to support project management regarding project estimates. Document a rationale for the software architectural design decision.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.
- The analysis may include the suitability of pre-existing software components for the current application.
- Examples of methods suitable for analyzing technical aspects are prototypes, simulations, qualitative analyses.
- Examples of technical aspects are functionality, timings, and resource consumption (e.g, ROM, RAM, external / internal EEPROM or Data Flash or CPU load).
- Design rationales can include arguments such as proven-in-use, reuse of a software framework or software product line, a make-or-buy decision, or found in an evolutionary way (e.g, set-based design).

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [SWE_2_BP_4](@.md#swe_2_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SWE.2
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between the software architecture and the software requirements.

- There may be non-functional software requirements that the software architectural design does not trace to. Examples are development process requirements. Such requirements are still subject to verification.
- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g, the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SWE_2_BP_5](@.md#swe_2_bp_5) Communicate agreed software architecture

```yaml
Type: BasePractice
Process: SWE.2
BasePractice: BP5
```

Communicate the agreed software architecture to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
