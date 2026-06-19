# [SYS_2_PROCESS](@.md#sys_2_process) System Requirements Analysis


Source: Automotive SPICE PAM v4.0, section SYS.2 System Requirements Analysis.

## Process purpose

The purpose is to establish a structured and analyzed set of system requirements consistent with the stakeholder requirements.

## Process outcomes

1. System requirements are specified.
2. System requirements are structured and prioritized.
3. System requirements are analyzed for correctness and technical feasibility.
4. The impact of system requirements on the operating environment is analyzed.
5. Consistency and bidirectional traceability are established between system requirements and stakeholder requirements.
6. The system requirements are agreed and communicated to all affected parties.

## Base practices

### [SYS_2_BP_1](@.md#sys_2_bp_1) Specify system requirements

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP1
```

Use the stakeholder requirements to identify and document the functional and non-functional requirements for the system according to defined characteristics for requirements.

- Characteristics of requirements are defined in standards such as ISO IEEE 29148, ISO 26262-8:2018, or the INCOSE Guide For Writing Requirements.
- Examples for defined characteristics of requirements shared by technical standards are verifiability (i.e., verification criteria being inherent in the requirements text), unambiguity/comprehensibility, freedom from design and implementation, and not contradicting any other requirement).

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)

### [SYS_2_BP_2](@.md#sys_2_bp_2) Structure system requirements

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP2
```

Structure and prioritize the system requirements.

- Examples for structuring criteria can be grouping (e.g., by functionality) or product variants identification.
- Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Please refer to [SPL_2_BP_1](@.md#spl_2_bp_1).

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)
- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)

### [SYS_2_BP_3](@.md#sys_2_bp_3) Analyze system requirements

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP3
```

Analyze the specified system requirements including their interdependencies to ensure correctness, technical feasibility, and to support project management regarding project estimates.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.
- Technical feasibility can be evaluated based on e.g., platform or product line, or by means of prototype development or product demonstrators.

The practice shall produce or update:

- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)
- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [SYS_2_BP_4](@.md#sys_2_bp_4) Analyze the impact on the system context

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP4
```

Analyze the impact that the system requirements will have on elements in the relevant system context.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [SYS_2_BP_5](@.md#sys_2_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP5
```

Ensure consistency and establish bidirectional traceability between system requirements and stakeholder requirements.

- Bidirectional traceability supports consistency, facilitates impact analyses of change requests, and supports the demonstration of coverage of stakeholder requirements. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- There may be non-functional stakeholder requirements that the system requirements do not trace to. Examples are process requirements. Such stakeholder requirements are still subject to verification.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SYS_2_BP_6](@.md#sys_2_bp_6) Communicate agreed system requirements and impact on the system context

```yaml
Type: BasePractice
Process: SYS.2
BasePractice: BP6
```

Communicate agreed system requirements and impact on the system context. Communicate the agreed system requirements, and results of the impact analysis on the system context, to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
