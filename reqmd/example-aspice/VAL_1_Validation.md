# [VAL_1_PROCESS](@.md#val_1_process) Validation


Source: Automotive SPICE PAM v4.0, section VAL.1 Validation.

## Process purpose

The purpose is to provide evidence that the end product, allowing direct end user interaction, satisfies the intended use expectations in its operational target environment.

## Process outcomes

1. Validation measures are selected considering criteria for regression verification.
2. The product is validated using the selected validation measures and the results of validation are recorded.
3. Consistency and unidirectional traceability are established between validation measures and stakeholder requirements; and consistency and bidirectional traceability is established between validation results and validation measures.
4. Results of the validation are summarized and communicated to all affected parties. 

## Base practices

### [VAL_1_BP_1](@.md#val_1_bp_1) Specify validation measures for product validation

```yaml
Type: BasePractice
Process: VAL.1
BasePractice: BP1
```

Specify the validation measures for the end product based on the stakeholder requirements to provide evidence that it fulfills its intended use expectations in its operational target environment, and
- techniques for the validation measures,
- pass/fail criteria for validation measures,
- a definition of entry and exit criteria for the validation measures,
- necessary sequence of validation measures, and
- the required validation infrastructure and environment setup.

- An example for validation-relevant stakeholder requirements are homologation or legal type approval requirements. Further examples of sources of intended use expectations are technical risks (see [MAN_5_PROCESS](@.md#man_5_process), [SYS_3_BP_4](@.md#sys_3_bp_4), [SWE_2_BP_3](@.md#swe_2_bp_3), [HWE_2_BP_6](@.md#hwe_2_bp_6)).
- Where stakeholder requirements cannot be specified comprehensively or change frequently, repeated validation of (often rapidly developed) increments in product evolution may be employed to refine stakeholder requirements, and to mitigate risks in the correct identification of needs.
- Validation may also be conducted to confirm that the product also satisfies the often less formally expressed, but sometimes overriding, attitudes, experience, and subjective tests that comprise stakeholder or end user satisfaction.

The practice shall produce or update:

- [wp_08_59_validation_measure](=.md#wp_08_59_validation_measure)
- [wp_08_57_validation_measure_selection_set](=.md#wp_08_57_validation_measure_selection_set)

### [VAL_1_BP_2](@.md#val_1_bp_2) Select validation measures

```yaml
Type: BasePractice
Process: VAL.1
BasePractice: BP2
```

Document the selection of validation measures considering selection criteria including criteria for regression validation. The documented selection of validation measures shall have sufficient coverage according to the release scope.

- Examples for criteria for selection can be the release purpose of the delivered product (such as test bench, test track, validation on public roads, field use by end users), homologation/ type approval, confirmation of requirements, or the need for regression due to e.g., changes to stakeholder requirements and needs.

The practice shall produce or update:

- [wp_08_59_validation_measure](=.md#wp_08_59_validation_measure)
- [wp_08_57_validation_measure_selection_set](=.md#wp_08_57_validation_measure_selection_set)

### [VAL_1_BP_3](@.md#val_1_bp_3) Perform validation and evaluate results

```yaml
Type: BasePractice
Process: VAL.1
BasePractice: BP3
```

Perform the validation of the integrated end product using the selected validation measures. Record the validation results including pass/fail status. Evaluate the validation results.

- Validation results can be used as a means for identifying stakeholder or system requirements e.g, in the case of mock-ups or concept studies.
- See [SUP_9_PROCESS](@.md#sup_9_process) for handling verification results that deviate from expected results

The practice shall produce or update:

- [wp_13_24_validation_results](=.md#wp_13_24_validation_results)

### [VAL_1_BP_4](@.md#val_1_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: VAL.1
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability from validation measures to the stakeholder requirements from which they are derived. Establish bidirectional traceability between validation results and validation measures.

- Examples of sources of validation measures from which they can be derived are legal requirements, homologation requirements, results of technical risk analyses, or stakeholder and system requirements (see [SYS_1_PROCESS](@.md#sys_1_process) and [SYS_2_PROCESS](@.md#sys_2_process)).
- If sources of validation measures are e.g., legal or homologation requirements, then direct bidirectional traceability from those sources to the validation measures are not possible. In such a case, unidirectional traceability is sufficient.
- Bidirectional traceability supports consistency, and facilitates impact analyses of change requests, and demonstration of verification coverage. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [VAL_1_BP_5](@.md#val_1_bp_5) Summarize and communicate results

```yaml
Type: BasePractice
Process: VAL.1
BasePractice: BP5
```

Summarize the validation results and communicate them to all affected parties.

- Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
