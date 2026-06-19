# [MLE_2_PROCESS](@.md#mle_2_process) Machine Learning Architecture


Source: Automotive SPICE PAM v4.0, section MLE.2 Machine Learning Architecture.

## Process purpose

The purpose is to establish an ML architecture supporting training and deployment, consistent with the ML requirements, and to evaluate the ML architecture against defined criteria.

## Process outcomes

1. A ML architecture is developed.
2. Hyperparameter ranges and initial values are determined as a basis for the training.
3. Evaluation of ML architectural elements is conducted.
4. Interfaces of the ML architectural elements are defined.
5. Resource consumption objectives for the ML architectural elements are defined.
6. Consistency and bidirectional traceability are established between the ML architectural elements and the ML requirements.
7. The ML architecture is agreed and communicated to all affected parties.

## Base practices

### [MLE_2_BP_1](@.md#mle_2_bp_1) Develop ML architecture

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP1
```

Develop and document the ML architecture that specifies ML architectural elements including details of the ML model, pre- and postprocessing, and hyperparameters which are required to create, train, test, and deploy the ML model.

- Necessary details of the ML model may include layers, activation functions, and backpropagation. The level of detail of the ML model may not need to cover aspects like single neurons.
- The details of the ML model may differ between the ML model used during training and the deployed ML model.

The practice shall produce or update:

- [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture)
- [wp_01_54_hyperparameter](=.md#wp_01_54_hyperparameter)
- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [MLE_2_BP_2](@.md#mle_2_bp_2) Determine hyperparameter ranges and initial values

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP2
```

Determine and document the hyperparameter ranges and the initial values as a basis for the training.

The practice shall produce or update:

- [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture)
- [wp_01_54_hyperparameter](=.md#wp_01_54_hyperparameter)

### [MLE_2_BP_3](@.md#mle_2_bp_3) Analyze ML architectural elements

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP3
```

Define criteria for analysis of the ML architectural elements. Analyze ML architectural elements according to the defined criteria.

- Trustworthiness and explainability might be criteria for the analysis of the ML architectural elements.

The practice shall produce or update:

- [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture)
- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [MLE_2_BP_4](@.md#mle_2_bp_4) Define interfaces of the ML architectural elements

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP4
```

Determine and document the internal and external interfaces of each ML architectural element including its interfaces to related software components.

The practice shall produce or update:

- [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture)

### [MLE_2_BP_5](@.md#mle_2_bp_5) Define resource consumption objectives for the ML architectural elements

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP5
```

Determine and document the resource consumption objectives for all relevant ML architectural elements during training and deployment.

The practice shall produce or update:

- [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture)

### [MLE_2_BP_6](@.md#mle_2_bp_6) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP6
```

Ensure consistency and establish bidirectional traceability between the ML architectural elements and the ML requirements.

- Bidirectional traceability supports consistency, and facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- The bidirectional traceability should be established on a reasonable level of abstraction to the ML architectural elements.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [MLE_2_BP_7](@.md#mle_2_bp_7) Communicate agreed ML architecture

```yaml
Type: BasePractice
Process: MLE.2
BasePractice: BP7
```

Inform all affected parties about the agreed ML architecture including the details of the ML model and the initial hyperparameter values.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
