# [SUP_10_PROCESS](@.md#sup_10_process) Change Request Management


Source: Automotive SPICE PAM v4.0, section SUP.10 Change Request Management.

## Process purpose

The purpose of the Change Request Management Process is to ensure that change requests are recorded, analyzed, tracked, approved, and implemented.

## Process outcomes

1. Requests for changes are recorded and identified.
2. Change requests are analyzed, dependencies and relationships to other change requests are identified, and the impact is estimated.
3. Change requests are approved before implementation and prioritized accordingly.
4. Bidirectional traceability is established between change requests and affected work products.
5. Implementation of change requests is confirmed.
6. Change requests are tracked to closure and status of change requests is communicated to affected parties.

## Base practices

### [SUP_10_BP_1](@.md#sup_10_bp_1) Identify and record the change requests

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP1
```

The scope for application of change requests is identified. Each change request is uniquely identified, described, and recorded, including the initiator and reason of the change request. A status is assigned to each change request to facilitate tracking. NOTE 1: Change requests may be used for changes related to e.g., product, process, methods. NOTE 2: Example values for the change request status are "open", "under investigation", "implemented", etc. NOTE 3: The change request handling may differ across the product life cycle e.g., during prototype
construction and series development

The practice shall produce or update:

- [wp_13_16_change_request](=.md#wp_13_16_change_request)

### [SUP_10_BP_2](@.md#sup_10_bp_2) Analyze and assess change requests

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP2
```

Change requests are analyzed by relevant parties according to analysis criteria. Work products affected by the change request and dependencies to other change requests are determined. The impact of the change requests is assessed. NOTE 4: Examples for analysis criteria are: resource requirements, scheduling issues, risks, benefits, etc.

The practice shall produce or update:

- [wp_18_57_change_analysis_criteria](=.md#wp_18_57_change_analysis_criteria)
- [wp_13_16_change_request](=.md#wp_13_16_change_request)

### [SUP_10_BP_3](@.md#sup_10_bp_3) Approve change requests before implementation

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP3
```

Change requests are prioritized and approved for implementation based on analysis results and availability of resources. NOTE 5: A Change Control Board (CCB) is an example mechanism used to approve change requests. NOTE 6: Prioritization of change requests may be done by allocation to releases.

The practice shall produce or update:

- [wp_13_16_change_request](=.md#wp_13_16_change_request)

### [SUP_10_BP_4](@.md#sup_10_bp_4) Establish bidirectional traceability

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP4
```

Establish bidirectional traceability between change requests and work products affected by the change requests. In case that the change request is initiated by a problem, establish bidirectional traceability between change requests and the corresponding problem reports.

The practice shall produce or update:

- [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence)

### [SUP_10_BP_5](@.md#sup_10_bp_5) Confirm the implementation of change requests

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP5
```

The implementation of change requests is confirmed before closure by relevant stakeholders.

The practice shall produce or update:

- [wp_13_16_change_request](=.md#wp_13_16_change_request)

### [SUP_10_BP_6](@.md#sup_10_bp_6) Track change requests to closure

```yaml
Type: BasePractice
Process: SUP.10
BasePractice: BP6
```

Change requests are tracked to closure. The status of change requests is communicated to all affected parties. NOTE 7: Examples for informing affected parties can be daily standup meetings or tool-supported workflows.

The practice shall produce or update:

- [wp_13_16_change_request](=.md#wp_13_16_change_request)
