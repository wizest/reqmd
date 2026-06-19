# [SWE_5_PROCESS](@.md#swe_5_process) Software Component Verification and Integration Verification


Source: Automotive SPICE PAM v4.0, section SWE.5 Software Component Verification and Integration Verification.

## Process purpose

The purpose is to verify that software components are consistent with the software architectural design, and to integrate software elements and verify that the integrated software elements are consistent with the software architecture and software detailed design.

## Process outcomes

1. Verification measures are specified for software integration verification of the integrated software elements based on the software architecture and detailed design, including the interfaces of, and interactions between, the software components.
2. Verification measures for software components are specified to provide evidence for compliance of the software components with the software componentsbehavior and interfaces.
3. Software elements are integrated up to a complete integrated software.
4. Verification measures are selected according to the release scope considering criteria, including criteria for regression verification.
5. Software components are verified using the selected verification measures, and the results of the integration verification are recorded.
6. Integrated software elements are verified using the selected verification measures, and the results of the integration verification are recorded.
7. Consistency and bidirectional traceability are established between verification measures and the software architecture and detailed design; and bidirectional traceability is established between verification results and verification measures.
8. The results of software component verification and software elements integration verification are summarized and communicated to all affected parties

## Base practices

### [SWE_5_BP_1](@.md#swe_5_bp_1) Specify software integration verification measures

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP1
```

Specify verification measures, based on a defined sequence and preconditions for the integration of software elements, against the defined static and dynamic aspects of the software architecture, including
- techniques for the verification measures,
- pass/fail criteria for verification measures,
- entry and exit criteria for verification measures, and
- the required verification infrastructure and environment setup.

- Examples on which the software integration verification measures may focus on are the correct dataflow and dynamic interaction between software components together with their timing dependencies, the correct interpretation of data by all software components using an interface, and the compliance to resource consumption objectives.
- The software integration verification measure may be supported by using hardware debug interfaces or simulation environments (e.g, Software-in-the-Loop-Simulation).

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SWE_5_BP_2](@.md#swe_5_bp_2) Specify verification measures for verifying software component behavior

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP2
```

Specify verification measures for software component verification against the defined software components' behavior and their interfaces in the software architecture, including
- techniques for the verification measures,
- entry and exit criteria for verification measures,
- pass/fail criteria for verification measures, and
- the required verification infrastructure and environment setup.

- Verification measures are related to software components but not to the software units since software unit verification is addressed in the process [SWE_4_PROCESS](@.md#swe_4_process) Software Unit Verification.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SWE_5_BP_3](@.md#swe_5_bp_3) Select verification measures

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP3
```

Document the selection of integration verification measures for each integration step considering selection criteria including criteria for regression verification. The documented selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for selection criteria can be the need for continuous integration /continuous development regression verification (due to e.g, changes to the software architectural or detailed design), or the intended use of the delivered product release (e.g, test bench, test track, public road etc.).

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [SWE_5_BP_4](@.md#swe_5_bp_4) Integrate software elements and perform integration verification

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP4
```

Integrate the software elements until the software is fully integrated according to the specified interfaces and interactions between the Software elements, and according to the defined sequence and defined preconditions. Perform the selected integration verification measures. Record the verification measure data including pass/fail status and corresponding verification measure data.

- Examples for preconditions for starting software integration are qualification of pre-existing software components, off-the-shelf software components, open-source-software, or auto-code generated software.
- Defined preconditions may allow e.g, big-bang-integration of all software components, continuous integration, as well as stepwise integration (e.g, across software units and/or software components up to the fully integrated software) with accompanying verification measures.
- See [SUP_9_PROCESS](@.md#sup_9_process) for handling deviations of verification results deviate expected results.

The practice shall produce or update:

- [wp_06_50_integration_sequence_instruction](=.md#wp_06_50_integration_sequence_instruction)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)
- [wp_01_03_software_component](=.md#wp_01_03_software_component)
- [wp_01_50_integrated_software](=.md#wp_01_50_integrated_software)

### [SWE_5_BP_5](@.md#swe_5_bp_5) Perform software component verification

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP5
```

Perform the selected verification measures for verifying software component behavior. Record the verification results including pass/fail status and corresponding verification measure data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling verification results that deviate from expected results.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [SWE_5_BP_6](@.md#swe_5_bp_6) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP6
```

Ensure consistency and establish bidirectional traceability between verification measures and the static and dynamic aspects of the software architecture and detailed design. Establish bidirectional traceability between verification results and verification measures.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SWE_5_BP_7](@.md#swe_5_bp_7) Summarize and communicate results

```yaml
Type: BasePractice
Process: SWE.5
BasePractice: BP7
```

Summarize the software component verification and the software integration verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
