# [SYS_4_PROCESS](@.md#sys_4_process) System Integration and Integration Verification


Source: Automotive SPICE PAM v4.0, section SYS.4 System Integration and Integration Verification.

## Process purpose

The purpose is to integrate systems elements and verify that the integrated system elements are consistent with the system architecture.

## Process outcomes

1. Verification measures are specified for system integration verification of the integrated system elements based on the system architecture, including the interfaces of, and interactions between, system elements.
2. System elements are integrated up to a complete integrated system consistent with the release scope.
3. Verification measures are selected according to the release scope considering criteria, including criteria for regression verification.
4. Integrated system elements are verified using the selected verification measures, and the results of the system integration verification are recorded.
5. Consistency and bidirectional traceability are established between verification measures and the elements of the system architecture.
6. Bidirectional traceability between verification results and verification measures is established.
7. Results of the system integration and integration verification are summarized and communicated to all affected parties. 

## Base practices

### [SYS_4_BP_1](@.md#sys_4_bp_1) Specify verification measures for system integration

```yaml
Type: BasePractice
Process: SYS.4
BasePractice: BP1
```

Specify the verification measures, based on a defined sequence and preconditions for the integration of system elements against the system static and dynamic aspects of the system architecture, including
- techniques for the verification measures,
- pass/fail criteria for verification measures,
- a definition of entry and exit criteria for the verification measures, and
- the required verification infrastructure and environment setup.

- Examples on what a verification measure may focus are the timing dependencies of the correct signal flow between interfacing system elements, or interactions between hardware and software, as specified in the system architecture. The system integration test cases may focus on

- Examples on what a verification measure may focus are the timing dependencies of the correct signal flow between interfacing system elements, or interactions between hardware and software, as specified in the system architecture. The system integration test cases may focus on • the correct signal flow between system items, • the timeliness and timing dependencies of signal flow between system items, • the correct interpretation of signals by all system items using an interface, and/or • the dynamic interaction between system items.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SYS_4_BP_2](@.md#sys_4_bp_2) Select verification measures

```yaml
Type: BasePractice
Process: SYS.4
BasePractice: BP2
```

Document the selection of verification measures for each integration step considering selection criteria including criteria for regression verification. The documented selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for selection criteria can be prioritization of requirements, the need for regression verification (due to e.g., changes to the system architectural design or to system components), or the intended use of the delivered product release (e.g., test bench, test track, public road etc.)

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [SYS_4_BP_3](@.md#sys_4_bp_3) Integrate system elements and perform integration verification

```yaml
Type: BasePractice
Process: SYS.4
BasePractice: BP3
```

Integrate the system elements until the system is fully integrated according to the specified interfaces and interactions between the system elements, and according to the defined sequence and defined preconditions. Perform the selected system integration verification measures. Record the verification measure data including pass/fail status and corresponding verification measure data.

- Examples for preconditions for starting system integration can be successful system element verification or qualification of pre-existing system elements.
- See [SUP_9_PROCESS](@.md#sup_9_process) for handling verification results that deviate from expected results

The practice shall produce or update:

- [wp_06_50_integration_sequence_instruction](=.md#wp_06_50_integration_sequence_instruction)
- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)
- [wp_11_06_integrated_system](=.md#wp_11_06_integrated_system)

### [SYS_4_BP_4](@.md#sys_4_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SYS.4
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between verification measures and the system architecture. Establish bidirectional traceability between verification results and verification measures.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SYS_4_BP_5](@.md#sys_4_bp_5) Summarize and communicate results

```yaml
Type: BasePractice
Process: SYS.4
BasePractice: BP5
```

Summarize the system integration and integration verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
