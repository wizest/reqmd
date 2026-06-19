# [MLE_1_PROCESS](@.md#mle_1_process) Machine Learning Requirements Analysis


Source: Automotive SPICE PAM v4.0, section MLE.1 Machine Learning Requirements Analysis.

## Process purpose

The purpose is to refine the machine learning-related software requirements into a set of ML requirements.

## Process outcomes

1. The ML requirements including ML data requirements are identified and specified based on the software requirements and the components of the software architecture.
2. ML requirements are structured and prioritized.
3. ML requirements are analyzed for correctness and verifiability.
4. The impact of ML requirements on the ML operating environment is analyzed.
5. Consistency and bidirectional traceability are established between ML requirements and software requirements, and between ML requirements and software architecture.
6. The ML requirements are agreed and communicated to all affected parties.

## Base practices

### [MLE_1_BP_1](@.md#mle_1_bp_1) Specify ML requirements

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP1
```

Use the software requirements and the software architecture to identify and specify functional and non-functional ML requirements, as well as ML data requirements specifying data characteristics (e.g., gender, weather conditions, street conditions within the ODD) and their expected distributions.

- Non-functional requirements may include relevant characteristics of the ODD and KPIs as robustness, performance, and level of trustworthiness.
- The ML data requirements are input for [SUP_11_PROCESS](@.md#sup_11_process) Machine Learning Data Management but also for other MLE processes.
- In case of ML development only, stakeholder requirements represent the software requirements.

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)

### [MLE_1_BP_2](@.md#mle_1_bp_2) Structure ML requirements

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP2
```

Structure and prioritize the ML requirements.

- Examples for structuring criteria can be grouping (e.g., by functionality) or variants identification.
- Prioritization can be done according to project or stakeholder needs via e.g., definition of release scopes. Refer to [SPL_2_BP_1](@.md#spl_2_bp_1).

The practice shall produce or update:

- [wp_17_00_requirement](=.md#wp_17_00_requirement)
- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)

### [MLE_1_BP_3](@.md#mle_1_bp_3) Analyze ML requirements

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP3
```

Analyze the specified ML requirements including their interdependencies to ensure correctness, technical feasibility, and ability for machine learning model testing, and to support project management regarding project estimates.

- See [MAN_3_BP_3](@.md#man_3_bp_3) for project feasibility and [MAN_3_BP_5](@.md#man_3_bp_5) for project estimates.

The practice shall produce or update:

- [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute)
- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [MLE_1_BP_4](@.md#mle_1_bp_4) Analyze the impact on the ML operating environment

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP4
```

Analyze the impact that the ML requirements will have on interfaces of software components and the ML operating environment.

- The ML operating environment is defined as the infrastructure and information which both the trained ML model and the deployed ML model need for execution.

The practice shall produce or update:

- [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results)

### [MLE_1_BP_5](@.md#mle_1_bp_5) Ensure consistency and establish bidirectional traceability

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP5
```

Ensure consistency and establish bidirectional traceability between ML requirements and software requirements and between ML requirements and the software architecture.

- Bidirectional traceability supports consistency, facilitates impact analyses of change requests, and verification coverage demonstration. Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent with each other.
- Redundant traceability is not intended, but at least one out of the given traceability paths.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [MLE_1_BP_6](@.md#mle_1_bp_6) Communicate agreed ML requirements and impact on the operating environment

```yaml
Type: BasePractice
Process: MLE.1
BasePractice: BP6
```

Communicate agreed ML requirements and impact on the operating environment. Communicate the agreed ML requirements, and the results of the impact analysis on the ML operating environment to all affected parties.

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
