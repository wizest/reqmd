# [MLE_3_PROCESS](@.md#mle_3_process) Machine Learning Training


Source: Automotive SPICE PAM v4.0, section MLE.3 Machine Learning Training.

## Process purpose

The purpose is to optimize the ML model to meet the defined ML requirements.

## Process outcomes

1. A ML training and validation approach is specified.
2. The data set for ML training and ML validation is created.
3. The ML model, including hyperparameter values, is optimized to meet the defined ML requirements.
4. Consistency and bidirectional traceability are established between the ML training and validation data set and the ML data requirements.
5. Results of optimization are summarized, and the trained ML model is agreed and communicated to all affected parties.

## Base practices

### [MLE_3_BP_1](@.md#mle_3_bp_1) Specify ML training and validation approach

```yaml
Type: BasePractice
Process: MLE.3
BasePractice: BP1
```

Specify an approach which supports the training and validation of the ML model to meet the defined ML requirements. The ML training and validation approach includes
- entry and exit criteria of the training and validation,
- approaches for hyperparameter tuning / optimization,
- approach for data set creation and modification, and
- training and validation environment

- The ML training and validation approach may include random dropout and other robustification methods.
- ML validation is the optimization of the hyperparameters during Machine Learning Training ([MLE_3_PROCESS](@.md#mle_3_process)). The term "validation" has a different meaning than [VAL_1_PROCESS](@.md#val_1_process).
- The training environment should reflect the environment of the deployed model.

The practice shall produce or update:

- [wp_08_65_ml_training_and_validation_approach](=.md#wp_08_65_ml_training_and_validation_approach)

### [MLE_3_BP_2](@.md#mle_3_bp_2) Create ML training and validation data set

```yaml
Type: BasePractice
Process: MLE.3
BasePractice: BP2
```

Select data from the ML data collection provided by [SUP_11_PROCESS](@.md#sup_11_process) and assign them to the data set for training and validation of the ML model according to the specified ML training and validation approach.

- The ML training and validation data set may include corner cases, unexpected cases, and normal cases depending on the ML requirements.
- A separated data set for training and validation might not be required in some cases (e.g., k- fold cross validation, no optimization of hyperparameters).

The practice shall produce or update:

- [wp_03_51_ml_data_set](=.md#wp_03_51_ml_data_set)

### [MLE_3_BP_3](@.md#mle_3_bp_3) Create and optimize ML model

```yaml
Type: BasePractice
Process: MLE.3
BasePractice: BP3
```

Create the ML model according to the ML architecture and train it, using the identified ML training and validation data set according to the ML training and validation approach to meet the defined ML requirements, and training and validation exit criteria.

The practice shall produce or update:

- [wp_01_53_trained_ml_model](=.md#wp_01_53_trained_ml_model)
- [wp_01_54_hyperparameter](=.md#wp_01_54_hyperparameter)

### [MLE_3_BP_4](@.md#mle_3_bp_4) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: MLE.3
BasePractice: BP4
```

Ensure consistency and establish bidirectional traceability between the ML training and validation data set and the ML data requirements.

- Bidirectional traceability supports consistency and facilitates impact analyses of change requests. Traceability alone, e.g., the existence of links, does not necessarily mean that the

information is consistent with each other.


- Bidirectional traceability supports consistency and facilitates impact analyses of change requests. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [MLE_3_BP_5](@.md#mle_3_bp_5) Summarize and communicate agreed trained ML model

```yaml
Type: BasePractice
Process: MLE.3
BasePractice: BP5
```

Summarize the results of the optimization and inform all affected parties about the agreed trained ML model.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
