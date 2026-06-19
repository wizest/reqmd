# [HWE_1_PROCESS](@.md#hwe_1_process) Hardware Requirements Analysis


Source: Automotive SPICE PAM v4.0, section HWE.1 Hardware Requirements Analysis.

## Process purpose

The purpose is to establish a structured and analyzed set of hardware requirements consistent with the system requirements, and the system architectural design.

## Process outcomes

1. Hardware requirements are specified.
2. Hardware requirements are structured and prioritized.
3. Hardware requirements are analyzed for correctness and technical feasibility.
4. The impact of hardware requirements on the operating environment is analyzed.
5. Consistency and bidirectional traceability are established between hardware requirements and system requirements.
6. Consistency and bidirectional traceability are established between hardware requirements and system architectural design.
7. The hardware requirements are agreed and communicated to all affected parties.

## Base practices

### [HWE_1_BP_1](@.md#hwe_1_bp_1) Specify hardware requirements

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP1
```

Use the system requirements, and the system architecture including interface definitions, to identify and document the functional and non- functional requirements of the hardware according to defined characteristics for requirements.

- Characteristics of requirements are defined in standards such as ISO IEEE 29148, ISO/IEC IEEE 24765, ISO 26262-8:2018, or the INCOSE Guide For Writing Requirements.
- Examples for defined characteristics of requirements shared by the above-mentioned standards are verifiability (i.e., verification criteria being inherent in the requirements text), unambiguity/comprehensibility, freedom from design and implementation, and not contradicting any other requirement).
- In case of hardware-only development, the system requirements and the system architecture refer to a given operating environment. In that case, stakeholder requirements can be used as the basis for identifying the required functions and capabilities of the hardware.
- The hardware-software-interface (HSI) definition puts in context software and therefore is an interface decision at the system design level. If such a HSI exists, then it may provide input to hardware requirements.

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)

### [HWE_1_BP_2](@.md#hwe_1_bp_2) Structure hardware requirements

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP2
```

Structure and prioritize the hardware requirements.

- Examples for structuring criteria can be grouping (e.g., by functionality) or variants identification.
- Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Refer to [SPL_2_BP_1](@.md#spl_2_bp_1).

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)
- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)

### [HWE_1_BP_3](@.md#hwe_1_bp_3) Analyze hardware requirements

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP3
```

Analyze the specified hardware requirements including their interdependencies to ensure correctness, technical feasibility, and to support project management regarding project estimates.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.
- The analyses of technical feasibility can be done based on a given hardware design (e.g., platform) or by prototype development.

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)
- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [HWE_1_BP_4](@.md#hwe_1_bp_4) Analyze the impact on the operating environment

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP4
```

Identify the interfaces between the specified hardware and other elements of the operating environment. Analyze the impact that the hardware requirements will have on these interfaces and the operating environment.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [HWE_1_BP_5](@.md#hwe_1_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP5
```

Ensure consistency and establish traceability between hardware requirements and the system architecture. Ensure consistency and establish traceability between hardware requirements and system requirements.

- Redundant traceability is not intended.
- There may be non-functional hardware requirements that the hardware design does not trace to. Examples are development process requirements. Such requirements are still subject to verification.
- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- In case of hardware development only, the system requirements and system architecture refer to a given operating environment. In that case, consistency and bidirectional traceability can be ensured between stakeholder requirements and hardware requirements.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [HWE_1_BP_6](@.md#hwe_1_bp_6) Communicate agreed hardware requirements and impact on the operating environment

```yaml
Type: BasePractice
Process: HWE.1
BasePractice: BP6
```

Communicate agreed hardware requirements and impact on the operating environment. Communicate the agreed hardware requirements and results of the analysis of impact on the operating environment to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
