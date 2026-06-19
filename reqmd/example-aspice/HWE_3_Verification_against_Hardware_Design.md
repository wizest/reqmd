# [HWE_3_PROCESS](@.md#hwe_3_process) Verification against Hardware Design


Source: Automotive SPICE PAM v4.0, section HWE.3 Verification against Hardware Design.

## Process purpose

The purpose is to ensure that the production data compliant hardware is verified to provide evidence for compliance with the hardware design.

## Process outcomes

1. Verification measures are specified for verification of the hardware against the hardware design, including the interfaces between hardware elements and the dynamic aspects.
2. Verification measures are selected according to the release scope considering criteria, including criteria for regression verification.
3. Verification is performed on production data compliant samples using the selected verification measures, and verification results are recorded.
4. Consistency and bidirectional traceability are established between hardware elements and verification measures.
5. Bidirectional traceability is established between verification measures and verification results.
6. Verification results are summarized and communicated to all affected parties.

## Base practices

### [HWE_3_BP_1](@.md#hwe_3_bp_1) Specify verification measures for the verification against hardware design

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP1
```

Specify the verification measures suitable to provide evidence for compliance of the hardware with the hardware design and its dynamic aspects. This includes
- techniques for the verification measures,
- pass/fail criteria for the verification measures,
- a definition of entry and exit criteria for the verification measures,
- necessary sequence of the verification measures, and
- the required verification infrastructure and environment setup.

- Examples on what a verification measure may focus on are the timeliness and timing dependencies of the correct signal flow between interfacing hardware elements, interactions between hardware components.
- Measuring points can be used for stepwise testing of hardware elements.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [HWE_3_BP_2](@.md#hwe_3_bp_2) Ensure use of compliant samples

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP2
```

Ensure that the samples used for verification against hardware design are compliant with the corresponding production data, including special characteristics. Ensure that deviations are documented and that they do not alter verification results.

- Examples of compliance are sample reports, record of visual inspection, ICT report.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [HWE_3_BP_3](@.md#hwe_3_bp_3) Select verification measures

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP3
```

Document the selection of verification measures considering selection criteria including regression criteria. The documented selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for selection criteria can be prioritization of requirements, the need for regression due to changes to the hardware design, or the intended use of the delivered hardware release (e.g., test bench, test track, public road etc.)

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [HWE_3_BP_4](@.md#hwe_3_bp_4) Verify hardware design

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP4
```

Verify the hardware design using the selected verification measures. Record the verification results including pass/fail status and corresponding verification measure output data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling of non-conformances.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [HWE_3_BP_5](@.md#hwe_3_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP5
```

Ensure consistency and establish bidirectional traceability between hardware elements and the verification measures. Establish bidirectional traceability between the verification measures and verification results.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [HWE_3_BP_6](@.md#hwe_3_bp_6) Summarize and communicate results

```yaml
Type: BasePractice
Process: HWE.3
BasePractice: BP6
```

Summarize the verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
