# [SUP_8_PROCESS](@.md#sup_8_process) Configuration Management


Source: Automotive SPICE PAM v4.0, section SUP.8 Configuration Management.

## Process purpose

The purpose of the Configuration Management Process is to establish and maintain the integrity of relevant configuration items and baselines, and make them available to affected parties.

## Process outcomes

1. Selection criteria for configuration items are defined and applied.
2. Configuration item properties are defined.
3. Configuration management is established.
4. Modifications are controlled.
5. Baselining is applied.
6. The status of the configuration items is recorded and reported.
7. The completeness and consistency of the baselines is ensured.
8. The availability of backup and recovery mechanisms is verified.

## Base practices

### [SUP_8_BP_1](@.md#sup_8_bp_1) Identify configuration items

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP1
```

Define selection criteria for identifying relevant work products to be subject to configuration management. Identify and document configuration items according to the defined selection criteria. NOTE 1: Configuration items are representing work products or group of work products which are subject to configuration management as a single entity. NOTE 2: Configuration items may vary in complexity, size, and type, ranging from an entire system including all system, hardware, and software documentation down to a single element or document. NOTE 3: The selection criteria may be applied to single work products or a group of work products.

The practice shall produce or update:

- [wp_18_53_configuration_item_selection_criteria](=.md#wp_18_53_configuration_item_selection_criteria)
- [wp_01_52_configuration_item_list](=.md#wp_01_52_configuration_item_list)

### [SUP_8_BP_2](@.md#sup_8_bp_2) Define configuration item properties

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP2
```

Define the necessary properties needed for the modification and control of configuration items. NOTE 4: The configuration item properties may be defined for single configuration items or a group of items. NOTE 5: Configuration item properties may include a status model (e.g., Under Work, Tested, Released, etc.), storage location, access rights, etc. NOTE 6: The application of properties may be implemented by attributes of configuration items.

The practice shall produce or update:

- [wp_01_52_configuration_item_list](=.md#wp_01_52_configuration_item_list)

### [SUP_8_BP_3](@.md#sup_8_bp_3) Establish configuration management

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP3
```

Establish configuration management mechanisms for control of identified configuration items including the configuration item properties, including mechanisms for controlling parallel modifications of configuration items. NOTE 7: This may include specific mechanisms for different configuration item types, such as branch and merge management, or checkout control.

The practice shall produce or update:

- [wp_16_03_configuration_management_system](=.md#wp_16_03_configuration_management_system)
- [wp_14_01_change_history](=.md#wp_14_01_change_history)

### [SUP_8_BP_4](@.md#sup_8_bp_4) Control modifications

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP4
```

Control modifications using the configuration management mechanisms. NOTE 8: This may include the application of a defined status model for configuration items.

The practice shall produce or update:

- [wp_16_03_configuration_management_system](=.md#wp_16_03_configuration_management_system)
- [wp_14_01_change_history](=.md#wp_14_01_change_history)

### [SUP_8_BP_5](@.md#sup_8_bp_5) Establish baselines

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP5
```

Define and establish baselines for internal purposes, and for external product delivery, for all relevant configuration items.

The practice shall produce or update:

- [wp_16_03_configuration_management_system](=.md#wp_16_03_configuration_management_system)
- [wp_13_08_baseline](=.md#wp_13_08_baseline)

### [SUP_8_BP_6](@.md#sup_8_bp_6) Summarize and communicate configuration status

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP6
```

Record, summarize, and communicate the status of configuration items and established baselines to affected parties in order to support the monitoring of progress and status. NOTE 9: Regular communication of the configuration status, e.g., based on a defined status model supports project management, quality activities, and dedicated project phases such as software integration.

The practice shall produce or update:

- [wp_14_01_change_history](=.md#wp_14_01_change_history)
- [wp_15_56_configuration_status](=.md#wp_15_56_configuration_status)

### [SUP_8_BP_7](@.md#sup_8_bp_7) Ensure completeness and consistency

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP7
```

Ensure that the information about configuration items is correct and complete including configuration item properties. Ensure the completeness and consistency of baselines. NOTE 10: Completeness and consistency of a baseline means that all required configuration items are included and consistent, and have the required status. This can be used to support e.g., project gate approval.

The practice shall produce or update:

- [wp_01_52_configuration_item_list](=.md#wp_01_52_configuration_item_list)
- [wp_13_08_baseline](=.md#wp_13_08_baseline)
- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SUP_8_BP_8](@.md#sup_8_bp_8) Verify backup and recovery mechanisms availability

```yaml
Type: BasePractice
Process: SUP.8
BasePractice: BP8
```

Verify the availability of appropriate backup and recovery mechanisms for the configuration management including the controlled configuration items. Initiate measures in case of insufficient backup and recovery mechanisms. NOTE 11: Backup and recovery mechanisms may be defined and implemented by organizational units outside the project team. This may include references to corresponding procedures or regulations.

The practice shall produce or update:

- [wp_06_52_backup_and_recovery_mechanism_information](=.md#wp_06_52_backup_and_recovery_mechanism_information)
