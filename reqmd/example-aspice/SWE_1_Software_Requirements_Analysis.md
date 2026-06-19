# [SWE_1_PROCESS](@.md#swe_1_process) Software Requirements Analysis


Source: Automotive SPICE PAM v4.0, section SWE.1 Software Requirements Analysis.

## Process purpose

The purpose is to establish a structured and analyzed set of software requirements consistent with the system requirements, and the system architecture.

## Process outcomes

1. Software requirements are specified.
2. Software requirements are structured and prioritized.
3. Software requirements are analyzed for correctness and technical feasibility.
4. The impact of software requirements on the operating environment is analyzed.
5. Consistency and bidirectional traceability are established between software requirements and system requirements.
6. Consistency and bidirectional traceability are established between software requirements and system architecture.
7. The software requirements are agreed and communicated to all affected parties.

## Base practices

### [SWE_1_BP_1](@.md#swe_1_bp_1) Specify software requirements

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP1
```

Use the system requirements and the system architecture to identify and document the functional and non-functional requirements for the software according to defined characteristics for requirements.

- Characteristics of requirements are defined in standards such as ISO IEEE 29148, ISO 26262-8:2018, or the INCOSE Guide for Writing Requirements.
- Examples for defined characteristics of requirements shared by technical standards are verifiability (i.e., verification criteria being inherent in the requirements text), unambiguity/comprehensibility, freedom from design and implementation, and not contradicting any other requirement).
- In case of software-only development, the system requirements and the system architecture refer to a given operating environment. In that case, stakeholder requirements can be used as the basis for identifying the required functions and capabilities of the software.
- The hardware-software-interface (HSI) definition puts in context hardware and therefore it is an interface decision at the system design level. If such a HSI exists, then it may provide input to software requirements.

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)

### [SWE_1_BP_2](@.md#swe_1_bp_2) Structure software requirements

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP2
```

Structure and prioritize the software requirements.

- Examples for structuring criteria can be grouping (e.g., by functionality) or expressing product variants.
- Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Refer to [SPL_2_BP_1](@.md#spl_2_bp_1).

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)
- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)

### [SWE_1_BP_3](@.md#swe_1_bp_3) Analyze software requirements

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP3
```

Analyze the specified software requirements including their interdependencies to ensure correctness, technical feasibility, and to support project management regarding project estimates.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.
- Technical feasibility can be evaluated based on e.g., platform or product line, or by prototyping.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [SWE_1_BP_4](@.md#swe_1_bp_4) Analyze the impact on the operating environment

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP4
```

Analyze the impact that the software requirements will have on elements in the operating environment.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [SWE_1_BP_5](@.md#swe_1_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP5
```

Ensure consistency and establish bidirectional traceability between software requirements and system architecture. Ensure consistency and establish bidirectional traceability between software requirements and system requirements.

- Redundant traceability is not intended.
- There may be non-functional system requirements that the software requirements do not trace to. Examples are process requirements or requirements related to later software product lifecycle phases such as incident handling. Such requirements are still subject to verification.
- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- In case of software development only, the system requirements and system architecture refer to a given operating environment. In that case, consistency and bidirectional traceability can be ensured between stakeholder requirements and software requirements.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SWE_1_BP_6](@.md#swe_1_bp_6) Communicate agreed software requirements and impact on the operating environment

```yaml
Type: BasePractice
Process: SWE.1
BasePractice: BP6
```

Communicate agreed software requirements and impact on the operating environment. Communicate the agreed software requirements, and the results of the analysis of impact on the operating environment, to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
