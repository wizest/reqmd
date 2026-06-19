# [SUP_11_PROCESS](@.md#sup_11_process) Machine Learning Data Management


Source: Automotive SPICE PAM v4.0, section SUP.11 Machine Learning Data Management.

## Process purpose

The purpose is to define and align ML data with ML data requirements, maintain the integrity and quality of the ML data, and make them available to affected parties.

## Process outcomes

1. A ML data management system including an ML data lifecycle is established.
2. A ML data quality approach is developed including ML data quality criteria.
3. Collected ML data are processed for consistency with ML data requirements.
4. ML data are verified against defined ML data quality criteria and updated as needed.
5. ML data are agreed and communicated to all affected parties.

## Base practices

### [SUP_11_BP_1](@.md#sup_11_bp_1) Establish an ML data management system

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP1
```

Establish an ML data management system which supports
- ML data management activities,
- relevant sources of ML data,
- ML data life cycle including a status model, and
- interfaces to affected parties.

- Supported ML data management activities may include data collection, labeling/annotation, and structuring.

The practice shall produce or update:

- [wp_16_52_ml_data_management_system](=.md#wp_16_52_ml_data_management_system)

### [SUP_11_BP_2](@.md#sup_11_bp_2) Develop an ML data quality approach

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP2
```

Develop an approach to ensure that the quality of ML data is analyzed based on defined ML data quality criteria and activities are performed to support avoidance of biases of data.

- Examples of ML data quality criteria are relevant data sources, reliability and consistency of labelling, completeness against ML data requirements.
- The ML data management system should support the quality criteria and activities of the ML data quality approach.
- Biases to avoid may include sampling bias (e.g., gender, age) and feedback loop bias.
- For creation of ML data sets see [MLE_3_BP_2](@.md#mle_3_bp_2) and [MLE_4_BP_2](@.md#mle_4_bp_2).

The practice shall produce or update:

- [wp_19_50_ml_data_quality_approach](=.md#wp_19_50_ml_data_quality_approach)

### [SUP_11_BP_3](@.md#sup_11_bp_3) Collect ML data

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP3
```

Relevant sources for raw data are identified and continuously monitored for changes. The raw data is collected according to the ML data requirements.

- The identification and collection of ML data might be an organizational responsibility.
- Continuous monitoring should include the ODD and may lead to changes of the ML requirements.

The practice shall produce or update:

- [wp_03_53_ml_data](=.md#wp_03_53_ml_data)

### [SUP_11_BP_4](@.md#sup_11_bp_4) Process ML data

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP4
```

The raw data are processed (annotated, analyzed, and structured) according to the ML data requirements.

The practice shall produce or update:

- [wp_03_53_ml_data](=.md#wp_03_53_ml_data)

### [SUP_11_BP_5](@.md#sup_11_bp_5) Assure quality of ML data

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP5
```

Perform the activities according to the ML data quality approach to ensure that the ML data meets the defined ML data quality criteria.

- These activities may include sample-based reviews or statistical methods.

The practice shall produce or update:

- [wp_03_53_ml_data](=.md#wp_03_53_ml_data)

### [SUP_11_BP_6](@.md#sup_11_bp_6) Communicate agreed processed ML data

```yaml
Type: BasePractice
Process: SUP.11
BasePractice: BP6
```

Inform all affected parties about the agreed processed ML data and provide them to the affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
