# [HWE_2_PROCESS](@.md#hwe_2_process) Hardware Design


Source: Automotive SPICE PAM v4.0, section HWE.2 Hardware Design.

## Process purpose

The purpose is to provide an analyzed design, including dynamic aspects, that is consistent with the hardware requirements and suitable for manufacturing, and to derive production-relevant data.

## Process outcomes

1. A hardware architecture and hardware detailed design is developed that identifies the elements of the hardware and describes their behavior as well as their interfaces, and the dynamic interactions of the hardware elements.
2. The hardware architecture and the hardware detailed design is analyzed, and special characteristics are identified.
3. Consistency and bidirectional traceability are established between hardware requirements and hardware design.
4. Hardware production data is derived from the hardware detailed design and communicated to all affected parties.
5. Information for production test is derived from the hardware detailed design and communicated to all affected parties.
6. The hardware architecture and hardware detailed design and the special characteristics are agreed and communicated to all affected parties. 

## Base practices

### [HWE_2_BP_1](@.md#hwe_2_bp_1) Specify the hardware architecture

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP1
```

Develop the hardware architecture that identifies the hardware components. Document the rationale for the defined hardware architecture.

- Examples for aspects reflected in the hardware architecture are ground concept, supply concept, EMC concept.
- Examples for a design rationale can be implied by the reuse of a standard hardware, platform, or product line, respectively, or by a make-or-buy decision, or found in an evolutionary way.

The practice shall produce or update:

- [wp_04_52_hardware_architecture](=.md#wp_04_52_hardware_architecture)
- [wp_04_53_hardware_detailed_design](=.md#wp_04_53_hardware_detailed_design)
- [wp_04_54_hardware_schematics](=.md#wp_04_54_hardware_schematics)
- [wp_14_54_hardware_bill_of_materials](=.md#wp_14_54_hardware_bill_of_materials)
- [wp_04_55_hardware_layout](=.md#wp_04_55_hardware_layout)
- [wp_03_54_hardware_production_data](=.md#wp_03_54_hardware_production_data)
- [wp_04_56_hardware_element_interface](=.md#wp_04_56_hardware_element_interface)

### [HWE_2_BP_2](@.md#hwe_2_bp_2) Specify the hardware detailed design

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP2
```

Based on components identified in the hardware architecture, specify the detailed design description and the schematics for the intended hardware variants, including the interfaces between the hardware elements. Derive the hardware layout, the hardware bill of materials, and the production data.

- The identification of hardware parts and their suppliers in the hardware bill of materials may be subject to a pre-defined repository (see also IATF 16949:2016, clause 8.4.1.2.).
- Hardware detailed design may be subject to constraints such as availability of hardware parts on the market, hardware design rules, layout rules, creepage and clearance distances, compliance of HW parts with industry standards such as AEC-Q, REACH.

The practice shall produce or update:

- [wp_04_52_hardware_architecture](=.md#wp_04_52_hardware_architecture)
- [wp_04_53_hardware_detailed_design](=.md#wp_04_53_hardware_detailed_design)
- [wp_04_54_hardware_schematics](=.md#wp_04_54_hardware_schematics)
- [wp_14_54_hardware_bill_of_materials](=.md#wp_14_54_hardware_bill_of_materials)
- [wp_04_55_hardware_layout](=.md#wp_04_55_hardware_layout)
- [wp_03_54_hardware_production_data](=.md#wp_03_54_hardware_production_data)
- [wp_04_56_hardware_element_interface](=.md#wp_04_56_hardware_element_interface)

### [HWE_2_BP_3](@.md#hwe_2_bp_3) Specify dynamic aspects

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP3
```

Evaluate and document the dynamic behavior of the relevant hardware elements and the interaction between them.

- Not all hardware elements have dynamic behavior that needs to be described.

The practice shall produce or update:

- [wp_04_52_hardware_architecture](=.md#wp_04_52_hardware_architecture)
- [wp_04_53_hardware_detailed_design](=.md#wp_04_53_hardware_detailed_design)
- [wp_04_54_hardware_schematics](=.md#wp_04_54_hardware_schematics)
- [wp_14_54_hardware_bill_of_materials](=.md#wp_14_54_hardware_bill_of_materials)
- [wp_04_55_hardware_layout](=.md#wp_04_55_hardware_layout)
- [wp_03_54_hardware_production_data](=.md#wp_03_54_hardware_production_data)
- [wp_04_56_hardware_element_interface](=.md#wp_04_56_hardware_element_interface)

### [HWE_2_BP_4](@.md#hwe_2_bp_4) Analyze the hardware architecture and the hardware detailed design

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP4
```

Analyze the hardware architecture and hardware detailed design regarding relevant technical aspects, and support project management regarding project estimates. Identify special characteristics.

- Examples for technical aspects are manufacturability for production, suitability of pre-existing hardware components to be reused, or availability of hardware elements.
- Examples of methods suitable for analyzing technical aspects are simulations, calculations, quantitative or qualitative analyses such as FMEA.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)
- [wp_17_57_special_characteristics](=.md#wp_17_57_special_characteristics)

### [HWE_2_BP_5](@.md#hwe_2_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP5
```

Ensure consistency and establish traceability between hardware elements and hardware requirements. Ensure consistency and establish traceability between the hardware detailed design and components of the hardware architecture.

- There may be non-functional hardware requirements that the hardware design does not trace to. Examples are development process requirements. Such requirements are still subject to verification.
- Bidirectional traceability further supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g, the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [HWE_2_BP_6](@.md#hwe_2_bp_6) Communicate agreed hardware architecture and hardware detailed design

```yaml
Type: BasePractice
Process: HWE.2
BasePractice: BP6
```

Communicate the agreed hardware architecture and the hardware detailed design, including the special characteristics and relevant production data, to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
- [wp_04_54_hardware_schematics](=.md#wp_04_54_hardware_schematics)
- [wp_14_54_hardware_bill_of_materials](=.md#wp_14_54_hardware_bill_of_materials)
- [wp_04_55_hardware_layout](=.md#wp_04_55_hardware_layout)
- [wp_03_54_hardware_production_data](=.md#wp_03_54_hardware_production_data)
