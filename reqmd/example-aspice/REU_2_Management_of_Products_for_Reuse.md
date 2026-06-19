# [REU_2_PROCESS](@.md#reu_2_process) Management of Products for Reuse


Source: Automotive SPICE PAM v4.0, section REU.2 Management of Products for Reuse.

## Process purpose

The purpose is to ensure that reused work products are analyzed, verified, and approved for their target context.

## Process outcomes

1. Products for reuse are selected using defined criteria.
2. Products for reuse are analyzed for portability and interoperability.
3. Limitations for reuse are defined and communicated.
4. Products for reuse are verified.
5. Products for reuse are provided to affected parties.
6. Communication mechanism is established with the reuse product provider.

## Base practices

### [REU_2_BP_1](@.md#reu_2_bp_1) Select products for reuse

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP1
```

Select the products to be reused using defined criteria.

- Products for reuse may be systems, hardware or software components, third party components or legacy components.

The practice shall produce or update:

- [wp_12_03_reuse_candidate](=.md#wp_12_03_reuse_candidate)

### [REU_2_BP_2](@.md#reu_2_bp_2) Analyze the reuse capability of the product

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP2
```

Analyze the designated target architecture and the product to be reused to determine its applicability in the target architecture according to relevant criteria.

- Examples for criteria can be requirements compliance, verifiability of the product to be reused in the target architecture, or portability/interoperability.

The practice shall produce or update:

- [wp_04_02_domain_architecture](=.md#wp_04_02_domain_architecture)
- [wp_15_07_reuse_analysis_evidence](=.md#wp_15_07_reuse_analysis_evidence)

### [REU_2_BP_3](@.md#reu_2_bp_3) Define limitations for reuse

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP3
```

Define and communicate limitations for the products to be reused.

- Limitations may address parameters of operational environment.

The practice shall produce or update:

- [wp_04_02_domain_architecture](=.md#wp_04_02_domain_architecture)
- [wp_15_07_reuse_analysis_evidence](=.md#wp_15_07_reuse_analysis_evidence)

### [REU_2_BP_4](@.md#reu_2_bp_4) Ensure qualification of products for reuse

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP4
```

Provide evidence that the product for reuse is qualified for the intended use of the deliverable.

- Qualification may be demonstrated by verification evidence.
- Verification may include the appropriateness of documentation.

The practice shall produce or update:

- [wp_13_53_qualification_evidence](=.md#wp_13_53_qualification_evidence)

### [REU_2_BP_5](@.md#reu_2_bp_5) Provide products for reuse

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP5
```

Make available the product to be reused to affected parties.

- Refer to [HWE_3_PROCESS](@.md#hwe_3_process), [SWE_5_PROCESS](@.md#swe_5_process) or [SYS_4_PROCESS](@.md#sys_4_process) for more information on integration of hardware, software, or system components.

The practice shall produce or update:

- [wp_12_03_reuse_candidate](=.md#wp_12_03_reuse_candidate)

### [REU_2_BP_6](@.md#reu_2_bp_6) Communicate information about effectiveness of reuse activities

```yaml
Type: BasePractice
Process: REU.2
BasePractice: BP6
```

Establish communication and notification mechanism about experiences and technical outcomes to the provider of reused products.

- The communication with the provider of a reused product may depend on whether the product is under development or not.
- Budget targets and delivery dates to the customer, targets for test coverage and process lead time are examples for process performance objectives.
- Performance objectives are the basis for planning and monitoring. Assumptions and constraints are considered when identifying the performance objectives. Approach and methodology for the process performance is determined.
- A process performance strategy may not necessarily be document-ed specifically for each process. Elements applicable for multiple processes may be documented jointly, e.g, as part of a common project handbook or in a joint test strategy. GP 2.1.2: Plan the performance of the process. The planning for the performance of the process is established according to the defined objectives, criteria, and strategy. Process activities and work packages are defined. Estimates for work packages are identified using appropriate methods.
- Schedule and milestones are defined. GP 2.1.3: Determine resource needs. The required amount of human resources, and experience, knowledge and skill needs for the for process performance are determined based on the planning. The needs for physical and material resources are determined based on the planning.
- Physical and material resources may include equipment, laboratories, materials, tools, licenses etc. Required responsibilities and authorities to perform the process, and to manage the corresponding work products are determined.
- The definition of responsibilities and authorities does not necessarily require formal role descriptions. GP 2.1.4: Identify and make available resources. The individuals performing and managing the process are identified and allocated according to the determined needs. The individuals performing and managing the process are being qualified to execute their responsibilities.
- Qualification of individuals may include training, mentoring, or coaching. The other resources, necessary for performing the process are identified, made available, allocated and used according to the determined needs. GP 2.1.5: Monitor and adjust the performance of the process. Process performance is monitored to identify deviations from the planning. Appropriate actions in case of deviations from the planning are taken. The planning is adjusted as necessary. GP 2.1.6: Manage the interfaces between involved parties. The individuals and groups including required external parties involved in the process performance are determined. Responsibilities are assigned to the relevant individuals or parties. Communication mechanisms between the involved parties are determined. Effective communication between the involved parties is established and maintained. PA 2.1 Process Performance Management Achievement 1 Achievement 2 Achievement 3 Achievement 4 Achievement 5 Achievement 6 Achievement 7 Achievement 8
- Possible sources of documentation requirements may be e.g., best practices or lessons learned from other projects, standards, organization requirements, customer requirements, etc.
- There may be types of work products for which no review or approval is required, thus then there would be no need to define the corresponding criteria. GP 2.2.2 Define the requirements for storage and control of the work products. Requirements for the storage and control of the work products are defined, including their identification and distribution.
- Possible sources for the identification of requirements for storage and control may be e.g., legal requirements, data policies, best practices from other projects, tool related requirements, etc.
- Examples for work product storage are files in a file system, ticket in a tool, Wiki entry, paper documents etc.
- Where status of a work product is required in base practices, this should be managed via a defined status model. GP 2.2.3 Identify, store and control the work products. The work products to be controlled are identified. The work products are stored and controlled in accordance with the requirements. Change control is established for work products. Versioning and baselining of the work products is performed in accordance with the requirements for storage and control of the work products. The work products including the revision status are made available through appropriate mechanisms. GP 2.2.4 Review and adjust work products. The work products are reviewed against the defined requirements and criteria. Resolution of issues arising from work products reviews is ensured. PA 2.2 Work product management process attribute Achievement 1 Achievement 2 Achievement 3 Achievement 4
- An example for describing the involvement of the process roles in the activities is a RASI/RASIC representation. Suitable guidance, procedures, and templates are provided to support the execution of the process as needed.
- Procedures may also include description of specific methods to be used. Appropriate tailoring guidelines including predefined unambiguous criteria as well as predefined and unambiguous proceedings are defined based on identified deployment needs and context of the standard process. The standard process is maintained according to corresponding feedback from the monitoring of the deployed processes.
- For guidance on how to perform process improvements see the Process Improvement process ([PIM_3_PROCESS](@.md#pim_3_process)). GP 3.1.2 Determine the required competencies. Required competencies, skills, and experience for performing the standard process are determined for the identified roles. Appropriate qualification methods to acquire the necessary competencies and skills are determined, maintained, and made available for the identified roles.
- Qualification methods are e.g., trainings, mentoring, self-study.
- Preparation includes e.g., identification or definition of trainings, mentoring concepts, self- learning material. GP 3.1.3 Determine the required resources. Required physical and material resources and process infrastructure needs for performing the standard process are determined.
- This may include e.g., facilities, tools, licenses, networks, services, and samples supporting the establishment of the required work environment. GP 3.1.4 Determine suitable methods to monitor the standard process. Methods and required activities for monitoring the effectiveness and adequacy of the standard process are determined.
- Methods and activities to gather feedback regarding the standard process may be lessons learned, process compliance checks, internal audits, management reviews, change requests, reflection of state-of-the-art such as applicable international standards, etc. Appropriate criteria and information needed to monitor the standard process are defined.
- Information about process performance may be of qualitative or quantitative nature. PA 3.1 Process definition process attribute Achievement 1 Achievement 2 Achievement 3 Achievement 4 Achievement 5 Achievement 6
- Changes in the standard process may require updates of the defined process. GP 3.2.2 Ensure required competencies for the defined roles. Human resources are allocated to the defined roles according to the required competencies and skills. Assignment of persons to roles and corresponding responsibilities and authorities for performing the defined process are communicated. Gaps in competencies and skills are identified, and corresponding qualification measures are initiated and monitored. Availability and usage of the project staff are measured and monitored. GP 3.2.3 Ensure required resources to support the performance of the defined process. Required information to perform the defined process is made available, allocated and used. Required physical and material resources, process infrastructure and work environment are made available, allocated and used. Availability and usage of resources are measured and monitored. GP 3.2.4 Monitor the performance of the defined process. Information is collected and analyzed according to the determined process monitoring methods to understand the effectiveness and adequacy of the defined process. Results of the analysis are made available to all effected parties and used to identify where continual improvement of the standard and/or defined process can be made.
- For guidance on how to perform process improvements see the Process Improvement process ([PIM_3_PROCESS](@.md#pim_3_process)). PA 3.2 Process deployment process attribute Achievement 1 Achievement 2 Achievement 3 Achievement 4 Achievement 5
- Examples of process elements are work products, activities, tasks. GP 4.1.4 Derive process measurement approach and select analysis techniques. Based on the measurable relationships of process elements, or set of process elements, the process measurement metrics are derived to satisfy the established process information needs. Frequency of data collection is defined. Select analysis techniques, appropriate to collected data. Algorithms and methods to create derived measurement results from base measures are defined, as appropriate. Verification mechanism for base and derived measures is defined.
- Typically, the standard process definition is extended to include the collection of data for process measurement. GP 4.1.5 Establish quantitative control limits. Establish quantitative control limits for the derived metrics. Agreement with process stakeholders is established. GP 4.1.6 Collect product and process measurement results through performing the defined process. Data collection mechanisms are created for all identified metrics. Required data is collected across process instances of within the defined frequency and recorded. Measurement results are analyzed and reported to the identified stakeholders.
- A product measure can contribute to a process measure, e.g., the productivity of testing characterized by the number of defects found in a given timeframe in relation to the product defect rate in the field. PA 4.1 Quantitative analysis process attribute Achievement 1 Achievement 2 Achievement 3 Achievement 4 Achievement 5 Achievement 6
- Assignable cause may indicate a possible problem in the defined process. PA 4.2 Quantitative control process attribute Achievement 1 Achievement 2 Achievement 3 Achievement 4

The practice shall produce or update:

- [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence)
