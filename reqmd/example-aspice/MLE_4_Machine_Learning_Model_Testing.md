# [MLE_4_PROCESS](@.md#mle_4_process) Machine Learning Model Testing


Source: Automotive SPICE PAM v4.0, section MLE.4 Machine Learning Model Testing.

## Process purpose

The purpose is to ensure compliance of the trained ML model and the deployed ML model with the ML requirements.

## Process outcomes

1. A ML test approach is defined.
2. A ML test data set is created.
3. The trained ML model is tested.
4. The deployed ML model is derived from the trained ML model and tested.
5. Consistency and bidirectional traceability are established between the ML test approach and the ML requirements, and the ML test data set and the ML data requirements; and bidirectional traceability is established between the ML test approach and ML test results.
6. Results of the ML model testing are summarized and communicated with the deployed ML model to all affected parties.

## Base practices

### [MLE_4_BP_1](@.md#mle_4_bp_1) Specify an ML test approach

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP1
```

Specify an ML test approach suitable to provide evidence for compliance of the trained ML model and the deployed ML model with the ML requirements. The ML test approach includes
- ML test scenarios with distribution of data characteristics (e.g., gender, weather conditions, street conditions within the ODD) defined by ML requirements,
- distribution and frequency of each ML test scenario inside the ML test data set,
- expected test result per test datum,
- entry and exit criteria of the testing,
- approach for data set creation and modification, and
- the required testing infrastructure and environment setup.

- Expected test result per test datum might require labeling of test data to support comparison of output of the ML model with the expected output.
- Test datum is the smallest amount of data which is processed by the ML model into only one output. E.g., one image in photo processing or an audio sequence in voice recognition.
- Data characteristic is one property of the data that may have different expressions in the ODD. E.g., weather condition may contain expressions like sunny, foggy or rainy.
- An ML test scenario is a combination of expressions of all defined data characteristics e.g., weather conditions = sunny, street conditions = gravel road.

The practice shall produce or update:

- [wp_08_64_ml_test_approach](=.md#wp_08_64_ml_test_approach)

### [MLE_4_BP_2](@.md#mle_4_bp_2) Create ML test data set

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP2
```

Create the ML test data set needed for testing of the trained ML model and testing of the deployed ML model from the ML data collection provided by [SUP_11_PROCESS](@.md#sup_11_process) considering the ML test approach. The ML test data set shall not be used for training.

- The ML test data set for the trained ML model might differ from the test data set of the deployed ML model.
- Additional data sets might be used for special purposes like assurance of safety, fairness, robustness.

The practice shall produce or update:

- [wp_03_51_ml_data_set](=.md#wp_03_51_ml_data_set)

### [MLE_4_BP_3](@.md#mle_4_bp_3) Test trained ML model

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP3
```

Test the trained ML model according to the ML test approach using the created ML test data set. Record and evaluate the ML test results.

- Evaluation of test logs might include pattern analysis of failed test data to support e.g., trustworthiness.

The practice shall produce or update:

- [wp_13_50_ml_test_results](=.md#wp_13_50_ml_test_results)

### [MLE_4_BP_4](@.md#mle_4_bp_4) Derive deployed ML model

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP4
```

Derive the deployed ML model from the trained ML model according to the ML architecture. The deployed ML model shall be used for testing and delivery to software integration.

- The deployed ML model will be integrated into the target system and may differ from the trained ML model which often requires powerful hardware and uses interpretative languages.

The practice shall produce or update:

- [wp_13_50_ml_test_results](=.md#wp_13_50_ml_test_results)
- [wp_11_50_deployed_ml_model](=.md#wp_11_50_deployed_ml_model)

### [MLE_4_BP_5](@.md#mle_4_bp_5) Test deployed ML model

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP5
```

Test the deployed ML model according to the ML test approach using the created ML test data set. Record and evaluate the ML test results.

The practice shall produce or update:

- [wp_13_50_ml_test_results](=.md#wp_13_50_ml_test_results)
- [wp_11_50_deployed_ml_model](=.md#wp_11_50_deployed_ml_model)

### [MLE_4_BP_6](@.md#mle_4_bp_6) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP6
```

Ensure consistency and establish bidirectional traceability between the ML test approach and the ML requirements, and the ML test data set and the ML data requirements; and bidirectional traceability is established between the ML test approach and ML test results.

- Bidirectional traceability supports consistency, and facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [MLE_4_BP_7](@.md#mle_4_bp_7) Summarize and communicate results

```yaml
Type: BasePractice
Process: MLE.4
BasePractice: BP7
```

Summarize the ML test results of the ML model. Inform all affected parties about the agreed results and the deployed ML model.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
