---
reqmd_prodoc:
  requirement_specs:
    - ../example-aspice:
      - MAN_3_BP_1
      - MAN_3_BP_2
      - MAN_3_BP_3
      - MAN_3_BP_4
      - MAN_3_BP_5
      - MAN_3_BP_6
      - MAN_3_BP_7
      - MAN_3_BP_8
      - MAN_3_BP_9
      - MAN_3_BP_10
      - WP_08_53
      - WP_08_54
      - WP_08_56
      - WP_13_16
      - WP_13_51
      - WP_13_52
      - WP_14_02
      - WP_14_10
      - WP_14_50
      - WP_15_06
      - WP_18_52
  knowledge_files:
    - Project_Knowledge.md
  propagation_docs:
    downstream:
      - Stakeholder_Requirements.md
      - Support_Management.md
---

# Project Management Plan

## [PRJ_PLAN_SCOPE](@) Project scope

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When the brake assist controller project is planned, the project team shall define the scope as stakeholder requirements analysis, system requirements analysis, system architecture, software requirements, software architecture, software detailed design, verification, validation, configuration management, change management, problem resolution, and quality assurance.
- When the scope of work is defined, the project management plan shall identify the project goal as a brake assist controller demonstrator, the motivation as rapid-braking support with preserved normal braking, and the project boundary as requirements through validation work products for the demonstrator release.
- When scope changes are approved, the project team shall update impacted ProDoc work products and related ReqMd identifier index links through the ReqMd skill workflow.
- When the scope of work is defined, the project team shall identify all ProDoc work products as work packages with responsible discipline, expected input, expected output, and affected stakeholder group.
- If a requested work package is outside the brake assist controller scope, then project management shall record the exclusion and communicate the disposition to affected parties.

## [PRJ_PLAN_LIFECYCLE](@) Project lifecycle and release scope

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When the project life cycle is defined, the project management plan shall sequence elicitation, system requirements, system architecture, software requirements, software architecture, detailed design, verification, validation, baseline control, and release readiness review as the planned life-cycle stages.
- When project milestones are defined, the plan shall identify draft baseline, engineering baseline, verification-ready baseline, validation-ready baseline, and demonstrator release decision as release-scope milestones.
- When customer or organizational process alignment is required, the plan shall record the aligned development process, affected stakeholder group, and communication evidence for the agreed life-cycle approach.

## [PRJ_PLAN_FEASIBILITY_AND_RESOURCES](@) Feasibility and resources

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When project feasibility is evaluated, the project management plan shall record feasibility with respect to schedule, effort, available people, tool infrastructure, demonstrator hardware, and technical constraints for brake assist timing, diagnostics, and validation environment.
- When project estimates are defined, the plan shall record effort, duration, responsible role, required resource, resource workload, and critical resource for each work package.
- If feasibility, resource availability, or estimate assumptions change, then project management shall create or update the affected change request, corrective action, consistency evidence, and communication evidence.

## [PRJ_PLAN_SCHEDULE](@) Project schedule

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When project work packages are planned, the project team shall schedule requirements work before architecture work, architecture work before detailed design, detailed design before verification, and verification before validation.
- When the schedule is defined, the project management plan shall record planned and actual start date, planned and actual completion date, dependency, critical-path status, mapped input data, assigned resource, resource allocation, resource workload, and critical resource for each required activity.
- When a downstream work product date changes, the project team shall analyze the impact on dependent work products and update affected propagation targets.
- When work packages are monitored, the project team shall record status, dependency, due date, and corrective action for each ProDoc work product.
- If a schedule deviation affects verification, validation, or release readiness, then project management shall create a change request or corrective action and update impacted work products.

## [PRJ_PLAN_SKILLS_AND_COMMITMENTS](@) Skills, interfaces, and commitments

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When work packages are assigned, the project management plan shall identify required skills, knowledge, experience, existing competency status, and training or coaching action for the responsible discipline.
- When project interfaces are agreed, the plan shall identify affected stakeholder groups, representative role, information need, agreed commitment, due date, and escalation path for unfulfilled commitments.
- If required skills, stakeholder interfaces, or commitments are insufficient for planned work, then project management shall update the schedule, work package, change request, corrective action, and communication evidence.

## [PRJ_PLAN_CONSISTENCY](@) Project consistency control

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When a project work product is changed, the project team shall check consistency with [SUP_BASELINE_CONTROL](@), [SYS_REQ_TRACEABILITY](@), [SW_REQ_TRACEABILITY](@), and [VER_TRACEABILITY](@).
- If a change affects lateral, upstream, or downstream work products, then the project team shall update the relevant ReqMd `@.md` identifier index relationships through the ReqMd skill workflow.
- When consistency is checked, the project team shall compare scope, stakeholder sources, affected-party agreement status, estimates, resources, skills, work package status, dependencies, schedule, plans, interfaces, commitments, change requests, and baseline status across affected ProDoc documents.
- If inconsistency remains after review, then project management shall record escalation path, corrective action, and communication evidence.

## [PRJ_PLAN_PROGRESS_REPORTING](@) Project progress reporting

```yaml
Type: Plan
Status: Draft
Owner: Project Management
```

- When project progress is reviewed, the project management plan shall report status for schedule progress, work package content, tasks, resources, skills, competence, planned expenditure, actual expenditure, and fulfillment of estimated effort and duration.
- If project progress varies from the plan, then project management shall record the variance reason, threat to continued progress, issue affecting project goals, contingency action, corrective action, and affected change request.
- When project review identifies a recurring problem, project management shall communicate project status to affected parties and update problem-resolution or corrective-action records to prevent recurrence.
