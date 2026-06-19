# [SWE_6_PROCESS](@.md#swe_6_process) Software Verification


Source: Automotive SPICE PAM v4.0, section SWE.6 Software Verification.

## Process purpose

The purpose of the Software Verification process is to ensure that the integrated software is verified to be consistent with the software requirements.

## Process outcomes

1. Verification measures are specified for software verification of the software based on the software requirements.
2. Verification measures are selected according to the release scope considering criteria, including criteria for regression verification.
3. The integrated software is verified using the selected verification measures and the results of software verification are recorded.
4. Consistency and bidirectional traceability are established between verification measures and software requirements; and bidirectional traceability is established between verification results and verification measures.
5. Results of the software verification are summarized and communicated to all affected parties.

## Base practices

### [SWE_6_BP_1](@.md#swe_6_bp_1) Specify verification measures for software verification

```yaml
Type: BasePractice
Process: SWE.6
BasePractice: BP1
```

Specify the verification measures for software verification suitable to provide evidence for compliance of the integrated software with the functional and non-functional information in the software requirements, including
- techniques for the verification measures,
- pass/fail criteria for verification measures,
- a definition of entry and exit criteria for the verification measures,
- necessary sequence of verification measures, and
- the required verification infrastructure and environment setup.

- The selection of appropriate techniques for verification measures may depend on the content of the respective software requirement (e.g, boundary values and equivalence classes for data range-oriented requirements, positive/sunny-day-test vs. negative testing such as fault injection), or on requirements-based testing vs. "error guessing based on knowledge or experience".

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SWE_6_BP_2](@.md#swe_6_bp_2) Select verification measures

```yaml
Type: BasePractice
Process: SWE.6
BasePractice: BP2
```

Document the selection of verification measures considering selection criteria including criteria for regression verification. The documented selection of verification measures shall have sufficient coverage according to the release scope.

- Examples for selection criteria can be prioritization of requirements, continuous development, the need for regression verification (due to e.g., changes to the software requirements), or the intended use of the delivered product release (test bench, test track, public road etc.)

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [SWE_6_BP_3](@.md#swe_6_bp_3) Verify the integrated software

```yaml
Type: BasePractice
Process: SWE.6
BasePractice: BP3
```

Perform the verification of the integrated software using the selected verification measures. Record the verification results including pass/fail status and corresponding verification measure data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling verification results that deviate from expected results.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [SWE_6_BP_4](@.md#swe_6_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SWE.6
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between verification measures and software requirements. Establish bidirectional traceability between verification results and verification measures.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SWE_6_BP_5](@.md#swe_6_bp_5) Summarize and communicate results

```yaml
Type: BasePractice
Process: SWE.6
BasePractice: BP5
```

Summarize the software verification results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
