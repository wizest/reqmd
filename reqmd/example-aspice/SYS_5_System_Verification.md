# [SYS_5_PROCESS](@.md#sys_5_process) System Verification


Source: Automotive SPICE PAM v4.0, section SYS.5 System Verification.

## Process purpose

The purpose is to ensure that the system is verified to be consistent with the system requirements.

## Process outcomes

1. Verification measures are specified for system verification of the system based on the system requirements.
2. Verification measures are selected according to the release scope considering criteria, including criteria for regression verification.
3. The integrated system is verified using the selected verification measures and the results of system verification are recorded.
4. Consistency and bidirectional traceability are established between verification measures and system requirements.
5. Bidirectional traceability is established between verification results and verification measures.
6. Verification results are summarized and communicated to all affected parties.

## Base practices

### [SYS_5_BP_1](@.md#sys_5_bp_1) Specify verification measures for system verification

```yaml
Type: BasePractice
Process: SYS.5
BasePractice: BP1
```

Specify the verification measures for system verification suitable to provide evidence for compliance with the functional and non-functional information in the system requirements, including
- techniques for the verification measures,
- pass/fail criteria for verification measures,
- a definition of entry and exit criteria for the verification measures,
- necessary sequence of verification measures, and
- the required verification infrastructure and environment setup.

- The system verification measures may cover aspects such as thermal, environmental, robustness/lifetime, and EMC.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SYS_5_BP_2](@.md#sys_5_bp_2) Select verification measures

```yaml
Type: BasePractice
Process: SYS.5
BasePractice: BP2
```

Document the selection of verification measures considering selection criteria including criteria for regression verification. The selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for criteria for selection can be prioritization of requirements, the need for regression verification (due to e.g., changes to the system requirements), the intended use of the delivered product release (test bench, test track, public road etc.)

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [SYS_5_BP_3](@.md#sys_5_bp_3) Perform verification of the integrated system

```yaml
Type: BasePractice
Process: SYS.5
BasePractice: BP3
```

Perform the verification of the integrated system using the selected verification measures. Record the verification results including pass/fail status and corresponding verification measure data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling verification results that deviate from expected results

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [SYS_5_BP_4](@.md#sys_5_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SYS.5
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between verification measures and system requirements. Establish bidirectional traceability between verification results and verification measures.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SYS_5_BP_5](@.md#sys_5_bp_5) Summarize and communicate results

```yaml
Type: BasePractice
Process: SYS.5
BasePractice: BP5
```

Summarize the system verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
