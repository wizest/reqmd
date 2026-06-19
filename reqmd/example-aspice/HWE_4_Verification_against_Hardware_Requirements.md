# [HWE_4_PROCESS](@.md#hwe_4_process) Verification against Hardware Requirements


Source: Automotive SPICE PAM v4.0, section HWE.4 Verification against Hardware Requirements.

## Process purpose

The purpose is to ensure that the complete hardware is verified to be consistent with the hardware requirements.

## Process outcomes

1. Verification measures are specified for verification of the hardware against the hardware requirements.
2. Verification measures are selected considering criteria, including criteria for regression verification.
3. Verification is performed, if applicable on production data compliant samples, using the selected verification measures, and verification results are recorded.
4. Consistency and bidirectional traceability are established between verification measures and hardware requirements.
5. Bidirectional traceability is established between verification measures and verification results.
6. Verification results are summarized and communicated to all affected parties.

## Base practices

### [HWE_4_BP_1](@.md#hwe_4_bp_1) Specify verification measures for the verification against hardware requirements

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP1
```

Specify verification measures for the verification against hardware requirements. Specify the verification measure to provide evidence for compliance with the hardware requirements. This includes
- techniques for the verification measures,
- pass/fail criteria for the verification measures,
- a definition of entry and exit criteria for the verification measures,
- necessary sequence of verification the measures, and
- the required verification infrastructure and environment setup

- The verification measures may cover aspects such as thermal, environmental, robustness/lifetime, and EMC.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [HWE_4_BP_2](@.md#hwe_4_bp_2) Ensure use of compliant samples

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP2
```

Ensure that the samples used for the verification against hardware requirements are compliant with the corresponding production data, including special characteristics, provided by hardware design.

- Examples of compliance are sample reports, record of visual inspection, ICT report.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [HWE_4_BP_3](@.md#hwe_4_bp_3) Select verification measures

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP3
```

Document the selection of verification measures considering selection criteria including regression criteria. The documented selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for selection criteria can be prioritization of requirements, the need for regression due to changes to the hardware requirements, or the intended use of the delivered hardware release (e.g, test bench, test track, public road etc.).

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [HWE_4_BP_4](@.md#hwe_4_bp_4) Verify the compliant hardware samples

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP4
```

Verify the compliant hardware samples using the selected verification measures. Record the verification results including pass/fail status and corresponding verification measure output data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling of non-conformances.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [HWE_4_BP_5](@.md#hwe_4_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP5
```

Ensure consistency between hardware requirements and verification measures. Establish bidirectional traceability between hardware requirements and verification measures. Establish bidirectional traceability between verification measures and verification results.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [HWE_4_BP_6](@.md#hwe_4_bp_6) Summarize and communicate results

```yaml
Type: BasePractice
Process: HWE.4
BasePractice: BP6
```

Summarize the verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
