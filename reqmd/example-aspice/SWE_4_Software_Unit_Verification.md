# [SWE_4_PROCESS](@.md#swe_4_process) Software Unit Verification


Source: Automotive SPICE PAM v4.0, section SWE.4 Software Unit Verification.

## Process purpose

The purpose is to verify that software units are consistent with the software detailed design.

## Process outcomes

1. Verification measures for software unit verification are specified.
2. Software unit verification measures are selected according to the release scope, including criteria for regression verification.
3. Software units are verified using the selected verification measures, and results are recorded.
4. Consistency and bidirectional traceability are established between verification measures and software units; and bidirectional traceability is established between verification results and verification measures.
5. Results of the software unit verification are summarized and communicated to all affected parties.

## Base practices

### [SWE_4_BP_1](@.md#swe_4_bp_1) Specify software unit verification measures

```yaml
Type: BasePractice
Process: SWE.4
BasePractice: BP1
```

Specify verification measures for each software unit defined in the software detailed design, including
- pass/fail criteria for verification measures,
- entry and exit criteria for verification measures, and
- the required verification infrastructure.

- Examples for unit verification measures are static analysis, code reviews, and unit testing.
- Static analysis can be done based on MISRA rulesets and other coding standards.

The practice shall produce or update:

- [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure)

### [SWE_4_BP_2](@.md#swe_4_bp_2) Select software unit verification measures

```yaml
Type: BasePractice
Process: SWE.4
BasePractice: BP2
```

Document the selection of verification measures considering selection criteria including criteria for regression verification. The documented selection of verification measures shall have sufficient coverage according to the release scope.

The practice shall produce or update:

- [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set)

### [SWE_4_BP_3](@.md#swe_4_bp_3) Verify software units

```yaml
Type: BasePractice
Process: SWE.4
BasePractice: BP3
```

Perform software unit verification using the selected verification measures. Record the verification results including pass/fail status and corresponding verification measure data.

- See [SUP_9_PROCESS](@.md#sup_9_process) for handling of verification results that deviate from expected results.

The practice shall produce or update:

- [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data)
- [wp_15_52_verification_results](=.md#wp_15_52_verification_results)

### [SWE_4_BP_4](@.md#swe_4_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: SWE.4
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between verification measures and the software units defined in the detailed design. Establish bidirectional traceability between the verification results and the verification measures.

- Bidirectional traceability supports consistency, and facilitates impact analysis of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SWE_4_BP_5](@.md#swe_4_bp_5) Summarize and communicate results

```yaml
Type: BasePractice
Process: SWE.4
BasePractice: BP5
```

Summarize the results of software unit verification and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
