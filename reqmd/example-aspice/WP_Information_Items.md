# [WP_INFORMATION_ITEMS](@.md#wp_information_items) Work Product Information Items

Source: Automotive SPICE PAM v4.0, Annex B Information Item Characteristics.

This document rewrites Annex B information item characteristics as ReqMd sections and links each item to its `wp_*` helper.

## [WP_01_03](@.md#wp_01_03) Software component

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 01-03
```

When [wp_01_03_software_component](=.md#wp_01_03_software_component) is produced, the information item shall provide the characteristics defined for 01-03 Software component.

### Characteristics

- Software element in the software architecture above the software unit level.
- Represented by a design model element or executable code such as libs or scripts and a configuration description, if applicable.

## [WP_01_50](@.md#wp_01_50) Integrated software

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 01-50
```

When [wp_01_50_integrated_software](=.md#wp_01_50_integrated_software) is produced, the information item shall provide the characteristics defined for 01-50 Integrated software.

### Characteristics

- Software executable (e.g, simulator with stubbing, debug-able, object code) including:
  - application parameter files (being a technical implementation solution for configurability-oriented requirements)
  - all configured software elements

## [WP_01_52](@.md#wp_01_52) Configuration item list

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 01-52
```

When [wp_01_52_configuration_item_list](=.md#wp_01_52_configuration_item_list) is produced, the information item shall provide the characteristics defined for 01-52 Configuration item list.

### Characteristics

- Items under configuration control
- The name of work products and an associated reference (to file, to tool artifact)
- Configuration item attributes and properties

## [WP_01_53](@.md#wp_01_53) Trained ML model

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 01-53
```

When [wp_01_53_trained_ml_model](=.md#wp_01_53_trained_ml_model) is produced, the information item shall provide the characteristics defined for 01-53 Trained ML model.

### Characteristics

- The trained ML model is the output of the training process. It consists of the software representing the ML architecture, the set of weights which were optimized during the training, and the final set of hyperparameters.

## [WP_01_54](@.md#wp_01_54) Hyperparameter

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 01-54
```

When [wp_01_54_hyperparameter](=.md#wp_01_54_hyperparameter) is produced, the information item shall provide the characteristics defined for 01-54 Hyperparameter.

### Characteristics

- Hyperparameters are used to control the ML model which has to be trained, e.g.:
  - Learn rate of training
  - Scaling of network (number of layers or neurons per layer)
  - Loss function
- Minimum characteristics:
  - Description
  - Initial value
  - Final value upon communicating the results of the ML training

## [WP_02_01](@.md#wp_02_01) Commitment / agreement

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 02-01
```

When [wp_02_01_commitment_agreement](=.md#wp_02_01_commitment_agreement) is produced, the information item shall provide the characteristics defined for 02-01 Commitment / agreement.

### Characteristics

- Signed off by all parties involved in the commitment/agreement
- Establishes what the commitment is for
- Establishes the resources required to fulfill the commitment, such as:
  - time
  - people
  - budget
  - equipment
  - facilities

## [WP_03_06](@.md#wp_03_06) Process performance information

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 03-06
```

When [wp_03_06_process_performance_information](=.md#wp_03_06_process_performance_information) is produced, the information item shall provide the characteristics defined for 03-06 Process performance information.

### Characteristics

- Measurements about defined quantitative or qualitative measurable indicators, that match defined information needs.
- Measurement metrics for the calculation of the quantitatively or qualitatively measurable indicators
- Data comparing process performance against expected levels
- Examples for project performance information:
  - resource utilization against established target
  - time schedule against established target
  - activity or task completion criteria met
  - defined input and output work products available
  - process quality against quality expectations and/or criteria
  - product quality against quality expectations and/or criteria
  - highlight product performance issues, trends
- Examples for service level performance information:
  - references any goals established
  - real time metrics related to aspects such as:
    - capacity
    - throughput
    - operational performance
    - operational service
    - service outage time
    - up time
    - job run time

## [WP_03_50](@.md#wp_03_50) Verification Measure data

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 03-50
```

When [wp_03_50_verification_measure_data](=.md#wp_03_50_verification_measure_data) is produced, the information item shall provide the characteristics defined for 03-50 Verification Measure data.

### Characteristics

- Verification measure data are data recorded during the execution of a verification measure, e.g.:
  - for test cases: raw data, logs, traces, tool generated outputs
  - measurements: values
  - calculations: values
  - simulations: protocol
  - reviews such as optical inspections a findings record
  - analyses: values

## [WP_03_51](@.md#wp_03_51) ML data set

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 03-51
```

When [wp_03_51_ml_data_set](=.md#wp_03_51_ml_data_set) is produced, the information item shall provide the characteristics defined for 03-51 ML data set.

### Characteristics

- Selection of ML Data for e.g., ML model training (ML Training and Validation Data Set) or test of the trained and deployed ML model (ML Test Data Set).

## [WP_03_53](@.md#wp_03_53) ML data

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 03-53
```

When [wp_03_53_ml_data](=.md#wp_03_53_ml_data) is produced, the information item shall provide the characteristics defined for 03-53 ML data.

### Characteristics

- Datum to be used for Machine Learning. The datum has to be attributed by metadata, e.g., unique ID and data characteristics. Examples:
  - Visual data like a photo or videos (but a video could also be considered as sequence of photos depending on the intended use)
  - Audio recording
  - Sensor data
  - Data created by an algorithm
  - Data might be processed to create additional data. E.g., processing could add noise, change colors or merge pictures.

## [WP_03_54](@.md#wp_03_54) Hardware production data

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 03-54
```

When [wp_03_54_hardware_production_data](=.md#wp_03_54_hardware_production_data) is produced, the information item shall provide the characteristics defined for 03-54 Hardware production data.

### Characteristics

- Consists of bill of materials
- Consists of layout e.g, GERBER data
- Specifies requirements for EOL test e.g.:
  - Test type (AOI, ICT, boundary scan)
  - Test coverage
  - Electrical loads
  - Acceptance criteria
- In case of semiconductor development: mask data (GDS2)

## [WP_04_04](@.md#wp_04_04) Software architecture

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-04
```

When [wp_04_04_software_architecture](=.md#wp_04_04_software_architecture) is produced, the information item shall provide the characteristics defined for 04-04 Software architecture.

### Characteristics

- A justifying rationale for the chosen architecture.
- Individual functional and non-functional behavior of the software component
- Settings for application parameters (being a technical implementation solution for configurability-oriented requirements)
- Technical characteristics of interfaces for relationships between software components such as:
  - Synchronization of Processes and tasks
  - Programming language call
  - APIs
  - Specifications of SW libraries
  - Method definitions in an object- oriented class definitions or UML/SysML interface classes
  - Callback functions, "hooks"
- Dynamics of software components and software states such as:
  - Logical software operating modes (e.g, start-up, shutdown, normal mode, calibration, diagnosis, etc.)
  - intercommunication (processes, tasks, threads) and priority
  - time slices and cycle time
  - interrupts with their priorities
  - interactions between software components
- Explanatory annotations, e.g, with natural language, for single elements or entire diagrams/models.

## [WP_04_05](@.md#wp_04_05) Software detailed design

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-05
```

When [wp_04_05_software_detailed_design](=.md#wp_04_05_software_detailed_design) is produced, the information item shall provide the characteristics defined for 04-05 Software detailed design.

### Characteristics

- Elements of a software detailed design:
  - Control flow definition
  - Format of input/output data
  - Algorithms
  - Defined data structures
  - Justified global variables
  - Explanatory annotations, e.g, with natural language, for single elements or entire diagrams/models
- Examples for expression languages, depending on the complexity or criticality of a software unit:
  - natural language or informal languages
  - semi-formal languages (e.g, UML, SysML)
  - formal languages (e.g, model-based approach)

## [WP_04_06](@.md#wp_04_06) System architecture

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-06
```

When [wp_04_06_system_architecture](=.md#wp_04_06_system_architecture) is produced, the information item shall provide the characteristics defined for 04-06 System architecture.

### Characteristics

- A justifying rationale for the chosen architecture.
- Individual behavior of system elements
- Interrelationships between system elements Settings for system parameters (such as application parameters) Manual/human control actions, e.g., according to STPA
- Interface Definitions:
  - Technical characteristics of interfaces for relationships between two system elements
- Interfaces between system elements e.g.:
  - bus interfaces (CAN, MOST, LIN, Flexray etc.)
  - thermal influences
  - hardware-software-interfaces (HSI), see below
  - electromagnetic interfaces
  - optical interfaces
  - hardware-mechanical-interfaces (e.g., a cable satisfying both mechanical and electrical requirements, housing interface to a PCB)
  - hardware-mechanical interconnection technology such as connectors, pressfit
  - creepage and clearance distances
- Fixations such as adhesive joints, screw bolts/fitting, riveted bolts, welding
- System interfaces related to EE Hardware e.g.:
  - analogue or digital interfaces (PWM, I/O) and their pin configurations
  - SPI bus, I2C bus, electrical interconnections
  - placement, e.g., thermal interfaces between hardware elements (heat dissipation)
  - soldering
  - creepage and clearance distances
- Interfaces for mechanical engineering e.g.:
  - friction
  - thermal influences
  - tolerances
  - clutches
  - fixations such as adhesive joints, screw bolts/fitting, riveted bolts, welding
  - forces (as a result of e.g., vibrations or friction)
  - placement
  - shape
  - A hardware-software interface, e.g.:
    - connector pin configurations and floating IOs for uCs/MOSFETs
    - signal scaling & resolution to be reflected by the application software
- Mechanical-hardware interfaces e.g.
  - such as mechanical dimensioning
  - positioning of connectors
  - positioning of e.g., hall sensors in relation to the bus-bar
  - tolerances
- Dynamics of system elements and system states:
  - Description of the system states and operation modes (startup, shutdown, sleep mode, diagnosis/calibration mode, production mode, degradation, emergency such as "limp-home", etc.)
  - Description of the dependencies among the system components regarding the operation modes
  - Interactions between system elements such as inertia of mechanical components to be reflected by the ECU, signal propagation and processing time through the hardware and software and e.g., bus systems
- Explanatory annotations, e.g., with natural language, for single elements or entire diagrams/models.

## [WP_04_51](@.md#wp_04_51) ML architecture

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-51
```

When [wp_04_51_ml_architecture](=.md#wp_04_51_ml_architecture) is produced, the information item shall provide the characteristics defined for 04-51 ML architecture.

### Characteristics

- An ML architecture is basically a special part of a software architecture (see 04-04). Additionally
  - ML architecture describes the overall structure of the ML-based software element
  - ML architecture specifies ML architectural elements including an ML model and other ML architectural elements, provided to train, deploy, and test the ML model.
  - describes interfaces within the ML-based software element and to other software elements
  - ML architecture describes details of the ML model like used layers, activation functions, loss function, and backpropagation
  - ML architecture contains defined hyperparameter ranges and initial values for training start
  - resource consumption objectives are defined
  - ML architecture contains allocated ML requirements

## [WP_04_52](@.md#wp_04_52) Hardware architecture

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-52
```

When [wp_04_52_hardware_architecture](=.md#wp_04_52_hardware_architecture) is produced, the information item shall provide the characteristics defined for 04-52 Hardware architecture.

### Characteristics

- Describes the initial floorplan and the overall hardware structure
- Identifies the required hardware components
- Includes the rationale for chosen options of hardware architecture
- Identifies own developed and supplied hardware components
- Identifies the required internal and external hardware component interfaces
- Specifies the interfaces of the hardware components
- Specifies the dynamic behavior
- Identifies the relationship and dependency between hardware components
- Describes all hardware variants to be developed
- Describes power supply, thermal and grounding concepts

## [WP_04_53](@.md#wp_04_53) Hardware detailed design

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-53
```

When [wp_04_53_hardware_detailed_design](=.md#wp_04_53_hardware_detailed_design) is produced, the information item shall provide the characteristics defined for 04-53 Hardware detailed design.

### Characteristics

- Describes the interconnections between the hardware parts
- Specifies the interfaces of the hardware parts
- Specifies the dynamic behavior (examples are: transitions between electrical states of hardware parts, power-up and power-down sequences, frequencies, modulations, signal delays, debounce times, filters, short circuit behavior, self-protection)
- Describes the conclusions and decisions based on e.g., analysis reports, datasheets, application notes
- Describes the constraints for layout

## [WP_04_54](@.md#wp_04_54) Hardware Schematics

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-54
```

When [wp_04_54_hardware_schematics](=.md#wp_04_54_hardware_schematics) is produced, the information item shall provide the characteristics defined for 04-54 Hardware Schematics.

### Characteristics

- Identifies the hardware parts
- Specifies the connections of the hardware parts
- Specifies the unique identification of all hardware parts
- Specifies unique variant identification

## [WP_04_55](@.md#wp_04_55) Hardware Layout

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-55
```

When [wp_04_55_hardware_layout](=.md#wp_04_55_hardware_layout) is produced, the information item shall provide the characteristics defined for 04-55 Hardware Layout.

### Characteristics

- Specifies the placement of the hardware parts and labels
- Specifies manufacturing data e.g., circuit paths (width, routing), vias, testing points, number of layers, drillings, material of the PCB, shape, soldering resist mask, PCB coating
- Specifies a unique layout identification

## [WP_04_56](@.md#wp_04_56) Hardware element interface

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 04-56
```

When [wp_04_56_hardware_element_interface](=.md#wp_04_56_hardware_element_interface) is produced, the information item shall provide the characteristics defined for 04-56 Hardware element interface.

### Characteristics

- is defined by output, input, type, and electrical characteristics including signal tolerances.
- Examples of interfaces are
  - high level interfaces like SPI, I2C, CAN, LIN, Ethernet
  - electrical interconnections
  - thermal interfaces between hardware elements (heat dissipation)

## [WP_06_04](@.md#wp_06_04) Training material

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 06-04
```

When [wp_06_04_training_material](=.md#wp_06_04_training_material) is produced, the information item shall provide the characteristics defined for 06-04 Training material.

### Characteristics

- Updated and available for new releases
- Coverage of system, application, operations, maintenance as appropriate to the application
- Course listings and availability

## [WP_06_50](@.md#wp_06_50) Integration sequence instruction

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 06-50
```

When [wp_06_50_integration_sequence_instruction](=.md#wp_06_50_integration_sequence_instruction) is produced, the information item shall provide the characteristics defined for 06-50 Integration sequence instruction.

### Characteristics

- Identification of required physical elements (e.g., hardware, mechanical, wiring elements), and software executables and application parameters (being a technical implementation solution for configurability-oriented requirements)
- necessary sequence or ordering of integration
- preconditions for starting system integration

## [WP_06_51](@.md#wp_06_51) Tailoring guideline

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 06-51
```

When [wp_06_51_tailoring_guideline](=.md#wp_06_51_tailoring_guideline) is produced, the information item shall provide the characteristics defined for 06-51 Tailoring guideline.

### Characteristics

- Criteria for tailoring,
- Proceeding of tailoring describing how to derive and document the defined process from the standard process including responsibility for tailoring and corresponding approval
- Requirements for the defined process to ensure integrity and consistency of the defined process
- Subset of process assets that is essential for the defined process

## [WP_06_52](@.md#wp_06_52) Backup and recovery mechanism information

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 06-52
```

When [wp_06_52_backup_and_recovery_mechanism_information](=.md#wp_06_52_backup_and_recovery_mechanism_information) is produced, the information item shall provide the characteristics defined for 06-52 Backup and recovery mechanism information.

### Characteristics

- Description / confirmation of existing backup and recovery mechanisms
- References to corresponding procedures or regulations

## [WP_07_04](@.md#wp_07_04) Process metric

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-04
```

When [wp_07_04_process_metric](=.md#wp_07_04_process_metric) is produced, the information item shall provide the characteristics defined for 07-04 Process metric.

### Characteristics

- Measurements about the process' performance:
  - ability to produce sufficient work products
  - adherence to the process
  - time it takes to perform process
  - defects related to the process
- Measures the impact of process change
- Measures the efficiency of the process

## [WP_07_05](@.md#wp_07_05) Project metric

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-05
```

When [wp_07_05_project_metric](=.md#wp_07_05_project_metric) is produced, the information item shall provide the characteristics defined for 07-05 Project metric.

### Characteristics

- Monitors key processes and critical tasks, provides status information to the project on:
  - project performance against established plan
  - resource utilization against established plan
  - time schedule against established plan
  - process quality against quality expectations and/or criteria
  - product quality against quality expectations and/or criteria
  - highlight product performance problems, trends
- Measures the results of project activities:
  - tasks are performed on schedule
  - product's development is within the resource commitments allocated
- References any goals established

## [WP_07_06](@.md#wp_07_06) Quality metric

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-06
```

When [wp_07_06_quality_metric](=.md#wp_07_06_quality_metric) is produced, the information item shall provide the characteristics defined for 07-06 Quality metric.

### Characteristics

- Measures quality attributes of the work products defined:
  - functionality
  - reliability
  - usability
  - efficiency
  - maintainability
  - portability
- Measures quality attributes of the "end customer" quality perception Note: Refer ISO/IEC 25010 for detailed information on measurement of product quality.

## [WP_07_08](@.md#wp_07_08) Service level metric

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-08
```

When [wp_07_08_service_level_metric](=.md#wp_07_08_service_level_metric) is produced, the information item shall provide the characteristics defined for 07-08 Service level metric.

### Characteristics

- Real time metrics taken while a system is operational, it measures the system's performance or expected service level
- Identifies aspects such as:
  - capacity
  - throughput
  - operational performance
  - operational service
  - service outage time
  - up time
  - job run time

## [WP_07_51](@.md#wp_07_51) Measurement result

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-51
```

When [wp_07_51_measurement_result](=.md#wp_07_51_measurement_result) is produced, the information item shall provide the characteristics defined for 07-51 Measurement result.

### Characteristics

- Measurements about the process' performance:
  - ability to produce sufficient work products
  - adherence to the process
  - time it takes to perform process
  - defects related to the process
- Measures the impact of process change
- Measures the efficiency of the process Project metric
- Monitors key processes and critical tasks, provides status information to the project on:
  - project performance against established plan
  - resource utilization against established plan
  - time schedule against established plan
  - process quality against quality expectations and/or criteria
  - product quality against quality expectations and/or criteria
  - highlight product performance problems, trends
- Measures the results of project activities:
- tasks are performed on schedule
- product's development is within the resource commitments allocated
- References any goals established Quality metric
- Measures quality attributes of the work products defined:
  - functionality
  - reliability
  - usability
  - efficiency
  - maintainability
  - portability
- Measures quality attributes of the "end customer" quality perceptionService level metric
- Benchmarking data
- Customer satisfaction survey

## [WP_07_61](@.md#wp_07_61) Quantitative process metric

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-61
```

When [wp_07_61_quantitative_process_metric](=.md#wp_07_61_quantitative_process_metric) is produced, the information item shall provide the characteristics defined for 07-61 Quantitative process metric.

### Characteristics

- Quantitatively measurable indicators that match information needs derived from business goals
- Relation of the quantitatively measurable indicators to process elements in process descriptions or repositories and tools
- Process measurement metrics for the calculation of the quantitatively measurable indicators, based on data from related process elements, repositories, or tools

## [WP_07_62](@.md#wp_07_62) Process analysis technique

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-62
```

When [wp_07_62_process_analysis_technique](=.md#wp_07_62_process_analysis_technique) is produced, the information item shall provide the characteristics defined for 07-62 Process analysis technique.

### Characteristics

- Methods for statistical analysis of process data
- Frequency of data collection.

## [WP_07_63](@.md#wp_07_63) Process control limits

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-63
```

When [wp_07_63_process_control_limits](=.md#wp_07_63_process_control_limits) is produced, the information item shall provide the characteristics defined for 07-63 Process control limits.

### Characteristics

- Quantitative control limits for the quantitative process metrics

## [WP_07_64](@.md#wp_07_64) Process measurement data

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 07-64
```

When [wp_07_64_process_measurement_data](=.md#wp_07_64_process_measurement_data) is produced, the information item shall provide the characteristics defined for 07-64 Process measurement data.

### Characteristics

- Data collected across process instances
- Attributes of data, e.g., timestamps
- Relation to process measurement metrics
- Storage and retrieval
- Effective controls over access

## [WP_15_57](@.md#wp_15_57) Quantitative process analysis results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-57
```

When [wp_15_57_quantitative_process_analysis_results](=.md#wp_15_57_quantitative_process_analysis_results) is produced, the information item shall provide the characteristics defined for 15-57 Quantitative process analysis results.

### Characteristics

- Deviations, and distributions, of the quantitative performance of individual process instances performance from the established quantitative control limits (special causes of variations)

## [WP_08_66](@.md#wp_08_66) Measures against deviations in quantitative process analysis

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-66
```

When [wp_08_66_measures_against_deviations_in_quantitative_process_analysis](=.md#wp_08_66_measures_against_deviations_in_quantitative_process_analysis) is produced, the information item shall provide the characteristics defined for 08-66 Measures against deviations in quantitative process analysis.

### Characteristics

- Definition of counter measures actions to address each assignable cause of special causes of variation, or common causes of variation
- Effective implementation of these counter measures

## [WP_15_58](@.md#wp_15_58) Common cause of variation analysis results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-58
```

When [wp_15_58_common_cause_of_variation_analysis_results](=.md#wp_15_58_common_cause_of_variation_analysis_results) is produced, the information item shall provide the characteristics defined for 15-58 Common cause of variation analysis results.

### Characteristics

- Identification of common causes
  - deviations of the quantitative performance of all process instances from the established quantitative control limits
  - distributions of the quantitative performance of all process instances within established quantitative control limits

## [WP_08_53](@.md#wp_08_53) Scope of work

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-53
```

When [wp_08_53_scope_of_work](=.md#wp_08_53_scope_of_work) is produced, the information item shall provide the characteristics defined for 08-53 Scope of work.

### Characteristics

- Summary of deliverables for a project
- Intended use for the deliverables
- Main functions to be realized
- Target delivery date and major milestones
- Work products and activities that are not in scope of the project as needed
- Target markets
- Applicable standards and legal requirements
- Reuse options
- Integration of third party deliveries

## [WP_08_54](@.md#wp_08_54) Feasibility analysis

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-54
```

When [wp_08_54_feasibility_analysis](=.md#wp_08_54_feasibility_analysis) is produced, the information item shall provide the characteristics defined for 08-54 Feasibility analysis.

### Characteristics

- Statement about the ability of the project to achieve the project objectives with available resources

## [WP_08_55](@.md#wp_08_55) Risk measure

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-55
```

When [wp_08_55_risk_measure](=.md#wp_08_55_risk_measure) is produced, the information item shall provide the characteristics defined for 08-55 Risk measure.

### Characteristics

- Identifies
  - the risk to be mitigated, avoided, or shared (transferred)
  - the activities to mitigate, avoid, or share (transfer) the risk
  - the originator of the measure
  - criteria for successful implementation
  - criteria for cancellation of activities
  - frequency of monitoring
- Risk treatment alternatives:
  - treatment option selected- avoid/reduce/transfer
  - alternative descriptions
  - recommended alternative(s)
  - justifications

## [WP_08_56](@.md#wp_08_56) Schedule

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-56
```

When [wp_08_56_schedule](=.md#wp_08_56_schedule) is produced, the information item shall provide the characteristics defined for 08-56 Schedule.

### Characteristics

- Identifies the activities to be performed
- Identifies the expected, and actual, start and completion date for required activities against progress/completion of activities
- Identifies dependencies between activities and critical path
- Has a mapping to scheduled resources and input data
- Identifies resource allocation, resource workload, and critical resources NOTE: A schedule is consistent with the defined work packages, see 14- 10

## [WP_08_57](@.md#wp_08_57) Validation Measure Selection Set

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-57
```

When [wp_08_57_validation_measure_selection_set](=.md#wp_08_57_validation_measure_selection_set) is produced, the information item shall provide the characteristics defined for 08-57 Validation Measure Selection Set.

### Characteristics

- Include criteria for re-validation in the case of changes (regression).
- Identification of validation measures, also for regression

## [WP_08_58](@.md#wp_08_58) Verification Measure Selection Set

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-58
```

When [wp_08_58_verification_measure_selection_set](=.md#wp_08_58_verification_measure_selection_set) is produced, the information item shall provide the characteristics defined for 08-58 Verification Measure Selection Set.

### Characteristics

- Include criteria for re-verification in the case of changes (regression).
- Identification of verification measures, also for regression testing

## [WP_08_59](@.md#wp_08_59) Validation Measure

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-59
```

When [wp_08_59_validation_measure](=.md#wp_08_59_validation_measure) is produced, the information item shall provide the characteristics defined for 08-59 Validation Measure.

### Characteristics

- A validation measure can be a test case, a measurement, a simulation, an emulation, or an end user survey
- The specification of a validation measure includes
  - pass/fail criteria for validation measures (completion and end criteria)
  - a definition of entry and exit criteria for the validation measures, and abort and re-start criteria
- Techniques
- Necessary validation environment & infrastructure
- Necessary sequence or ordering

## [WP_08_60](@.md#wp_08_60) Verification Measure

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-60
```

When [wp_08_60_verification_measure](=.md#wp_08_60_verification_measure) is produced, the information item shall provide the characteristics defined for 08-60 Verification Measure.

### Characteristics

- A verification measure can be a test case, a measurement, a calculation, a simulation, a review, an optical inspection, or an analysis
- The specification of a verification measure includes
  - pass/fail criteria for verification measures (test completion and ending criteria)
  - a definition of entry and exit criteria for the verification measures, and abort and re-start criteria
- Techniques (e.g., black-box and/or white-box-testing, equivalence classes and boundary values, fault injection for Functional Safety, penetration testing for Cybersecurity, back-to- back testing for model- based development, ICT)
- Necessary verification environment & infrastructure
- Necessary sequence or ordering

## [WP_08_61](@.md#wp_08_61) Resource allocation

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-61
```

When [wp_08_61_resource_allocation](=.md#wp_08_61_resource_allocation) is produced, the information item shall provide the characteristics defined for 08-61 Resource allocation.

### Characteristics

- Detailed / named resources are allocated to process tasks
- Overall resource workload is considered (e.g., allocation of resources to multiple projects) NOTE: Work breakdown structure may be used to refine the detailed resource allocation NOTE: A resource allocation may be integrated in a/ be a part of the schedule, see 08-56 NOTE: Resources to be allocated are e.g., personnel/human resources for project roles and physical and material resources such as (special/limited) equipment, tool, licenses, test hardware, test vehicle, climate chambers etc.

## [WP_08_62](@.md#wp_08_62) Communication matrix

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-62
```

When [wp_08_62_communication_matrix](=.md#wp_08_62_communication_matrix) is produced, the information item shall provide the characteristics defined for 08-62 Communication matrix.

### Characteristics

- List of relevant process internal / external stakeholders
- Roles and contact information of the parties involved
- Definition of required interfaces between stakeholders
- Communication subject
- Communication means and frequency
- Documentation needs of the communication (e.g., type of communication record)

## [WP_08_63](@.md#wp_08_63) Process Monitoring Method

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-63
```

When [wp_08_63_process_monitoring_method](=.md#wp_08_63_process_monitoring_method) is produced, the information item shall provide the characteristics defined for 08-63 Process Monitoring Method.

### Characteristics

- Measures including criteria for monitoring effectiveness, suitability, and adequacy of the standard process
- Method for collecting and analyzing the monitoring measures

## [WP_08_64](@.md#wp_08_64) ML test approach

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-64
```

When [wp_08_64_ml_test_approach](=.md#wp_08_64_ml_test_approach) is produced, the information item shall provide the characteristics defined for 08-64 ML test approach.

### Characteristics

- The ML test approach describes
  - ML test scenarios with distribution of data characteristics (e.g., gender, weather conditions, street conditions within the ODD) defined by ML requirements
  - quantity of each ML test scenario inside the test data set
  - expected test result per test datum
  - pass/fail criteria for the ML testing
  - entry and exit criteria for the ML testing
  - the required ML testing infrastructure and environment configuration

## [WP_08_65](@.md#wp_08_65) ML training and validation approach

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 08-65
```

When [wp_08_65_ml_training_and_validation_approach](=.md#wp_08_65_ml_training_and_validation_approach) is produced, the information item shall provide the characteristics defined for 08-65 ML training and validation approach.

### Characteristics

- The ML Training and Validation approach describes at least:
  - entry and exit criteria of the ML training
  - approaches for hyperparameter tuning / optimization to be used in the training
  - approach for data set creation and modification
  - training environment, including required training hardware (e.g., GPU, or supercomputer to be used)
  - interface adapter for provision of input data and storage of output data
  - if required, actions to organize the data set and training environment
- The ML training and validation approach may additionally include robustification methods like random dropout

## [WP_10_00](@.md#wp_10_00) Process description

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 10-00
```

When [wp_10_00_process_description](=.md#wp_10_00_process_description) is produced, the information item shall provide the characteristics defined for 10-00 Process description.

### Characteristics

- Process description of a standard or defined process (e.g., after tailoring), including:
  - scope and the intended use of the process
  - process activities including description and dependencies
  - entry and exit criteria such as input information needed and expected outputs for activities
  - Roles assigned to process activities (e.g., as RASIC ) or work products
  - guidelines
  - templates
  - specific methods/work instructions

## [WP_10_50](@.md#wp_10_50) Role description

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 10-50
```

When [wp_10_50_role_description](=.md#wp_10_50_role_description) is produced, the information item shall provide the characteristics defined for 10-50 Role description.

### Characteristics

- Name/identifier (unique within the organization)
- Assigned activities (e.g., as RASIC)
- Responsibilities and authorities
- Required competencies, skills, and experience

## [WP_10_51](@.md#wp_10_51) Qualification method description

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 10-51
```

When [wp_10_51_qualification_method_description](=.md#wp_10_51_qualification_method_description) is produced, the information item shall provide the characteristics defined for 10-51 Qualification method description.

### Characteristics

- Training courses
- Training materials
- Mentoring/coaching concepts
- Self-learning material

## [WP_10_52](@.md#wp_10_52) Process resource and infrastructure description

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 10-52
```

When [wp_10_52_process_resource_and_infrastructure_description](=.md#wp_10_52_process_resource_and_infrastructure_description) is produced, the information item shall provide the characteristics defined for 10-52 Process resource and infrastructure description.

### Characteristics

- Required facilities
- Required tools and corresponding licenses
- Required networks
- Required services
- Required samples

## [WP_11_03](@.md#wp_11_03) Release note

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 11-03
```

When [wp_11_03_release_note](=.md#wp_11_03_release_note) is produced, the information item shall provide the characteristics defined for 11-03 Release note.

### Characteristics

- Coverage for key elements (as appropriate to the application):
- Description of what is new or changed (including features removed)
- System information and requirements
- Identification of conversion programs and instructions
- Release numbering implementation may include:
  - the major release number
  - the feature release number
  - the defect repair number
  - the alpha or beta release; and the iteration within the alpha or beta release
- Identification of the component list (version identification included):
  - hardware / software / product elements, libraries, etc.
  - associated documentation list
- New/changed parameter information (e.g., for application parameters or global variables) and/or commands. Note that application parameters are a technical implementation solution for configurability-oriented requirements)
- Backup and recovery information
- List of open known problems, faults, warning information, etc.
- Identification of verification and diagnostic procedures
- Technical support information
- Copyright and license information
- The release note may include an introduction, the environmental requirements, installation procedures, product invocation, new feature identification and a list of defect resolutions, known defects and workarounds

## [WP_11_04](@.md#wp_11_04) Product release package

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 11-04
```

When [wp_11_04_product_release_package](=.md#wp_11_04_product_release_package) is produced, the information item shall provide the characteristics defined for 11-04 Product release package.

### Characteristics

- Includes the hardware/software/product
- Includes and associated release elements such as:
  - system hardware/software/product elements
  - associated customer documentation
  - application parameter definitions defined
  - command language defined
  - installation instructions
  - release letter

## [WP_11_05](@.md#wp_11_05) Software Unit

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 11-05
```

When [wp_11_05_software_unit](=.md#wp_11_05_software_unit) is produced, the information item shall provide the characteristics defined for 11-05 Software Unit.

### Characteristics

- a representation of a software element at the lowest level in a conceptual model, which is decided not to be further subdivided and that is a part of a software component, or
- a representation of a software unit under verification such as commented source code, auto-code, an object file, a library, an executable, or an executable model as input to verification

## [WP_11_06](@.md#wp_11_06) Integrated System

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 11-06
```

When [wp_11_06_integrated_system](=.md#wp_11_06_integrated_system) is produced, the information item shall provide the characteristics defined for 11-06 Integrated System.

### Characteristics

- Integrated product
- Application parameter files (being a technical implementation solution for configurability-oriented requirements)
- All configured elements for the product release are included

## [WP_11_50](@.md#wp_11_50) Deployed ML model

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 11-50
```

When [wp_11_50_deployed_ml_model](=.md#wp_11_50_deployed_ml_model) is produced, the information item shall provide the characteristics defined for 11-50 Deployed ML model.

### Characteristics

- It is derived from the trained ML model (see 01-53) and is to be integrated into the target system.
- It may differ from the trained ML model which often requires powerful hardware and uses interpretative languages.

## [WP_12_03](@.md#wp_12_03) Reuse candidate

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 12-03
```

When [wp_12_03_reuse_candidate](=.md#wp_12_03_reuse_candidate) is produced, the information item shall provide the characteristics defined for 12-03 Reuse candidate.

### Characteristics

- Identifies the product to be reused
- Identifies the responsible person for the products to be reused
- Identifies the reuse goals and objectives
- Identifies the list of reuse assets
- Identifies the issues/risks of reusing the component including specific requirements (hardware, software, resource and other reuse components)
- Identifies the person who will be qualifying the reuse candidate

## [WP_13_06](@.md#wp_13_06) Delivery evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-06
```

When [wp_13_06_delivery_evidence](=.md#wp_13_06_delivery_evidence) is produced, the information item shall provide the characteristics defined for 13-06 Delivery evidence.

### Characteristics

- Evidence of items shipped/delivered electronically to customer
- Identification of:
  - to whom it was sent
  - address, where delivered
  - delivery date
  - receipt of delivered product

## [WP_13_07](@.md#wp_13_07) Problem

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-07
```

When [wp_13_07_problem](=.md#wp_13_07_problem) is produced, the information item shall provide the characteristics defined for 13-07 Problem.

### Characteristics

- Identifies the submitter of the problem
- Identifies the group/person(s) responsible for providing problem resolution
- Includes a description of the problem
- Identifies classification of the problem (criticality, urgency, relevance etc.)
- Identifies the status of the problem
  - States such as "open", "in review", "in implementation", "closed", "rejected", "cancelled", ...
  - Transitions between states with conditions and authorities
- Identifies the expected closure date

## [WP_13_08](@.md#wp_13_08) Baseline

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-08
```

When [wp_13_08_baseline](=.md#wp_13_08_baseline) is produced, the information item shall provide the characteristics defined for 13-08 Baseline.

### Characteristics

- Identifies a state of one or a set of work products and artifacts which are consistent and complete
- Basis for next process steps and/or delivery
- Is unique and may not be changed NOTE: This should be established before a release to identify consistent and complete delivery

## [WP_13_09](@.md#wp_13_09) Meeting support evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-09
```

When [wp_13_09_meeting_support_evidence](=.md#wp_13_09_meeting_support_evidence) is produced, the information item shall provide the characteristics defined for 13-09 Meeting support evidence.

### Characteristics

- Agenda and minutes that are records that define:
  - purpose of meeting
  - attendees
  - date, place held
  - reference to previous minutes
  - what was accomplished
  - identifies issues raised
  - any open issues
  - next meeting if any

## [WP_13_13](@.md#wp_13_13) Product release approval

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-13
```

When [wp_13_13_product_release_approval](=.md#wp_13_13_product_release_approval) is produced, the information item shall provide the characteristics defined for 13-13 Product release approval.

### Characteristics

- Content information of what is to be shipped or delivered
- Identification of:
  - for whom it is intended
  - the address where to deliver
  - the date released
  - Evidence of supplier approval

## [WP_13_14](@.md#wp_13_14) Progress status

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-14
```

When [wp_13_14_progress_status](=.md#wp_13_14_progress_status) is produced, the information item shall provide the characteristics defined for 13-14 Progress status.

### Characteristics

- Status of a plan(s) (actual against planned) such as:
  - status of actual activities/work packages against planned activities/work package
  - status of actual results against established objectives/goals
  - status of actual resources allocation against planned resources
  - status of actual cost against budget estimates
  - status of actual time against planned schedule
  - status of actual quality against planned quality
- Record of any deviations from planned activities and reason why

## [WP_13_16](@.md#wp_13_16) Change request

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-16
```

When [wp_13_16_change_request](=.md#wp_13_16_change_request) is produced, the information item shall provide the characteristics defined for 13-16 Change request.

### Characteristics

- Identifies purpose of change
- Identifies requester contact information
- Impacted system(s)
- Impact to operations of existing system(s) defined
- Impact to associated documentation defined
- Criticality of the request, due date
- Information supporting the tracking of change requests to closure
  - progress status attribute (e.g., open, allocated, implemented, closed)
  - time stamp of status change
  - person who changed a status
  - rationale for changing a status

## [WP_13_18](@.md#wp_13_18) Quality conformance evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-18
```

When [wp_13_18_quality_conformance_evidence](=.md#wp_13_18_quality_conformance_evidence) is produced, the information item shall provide the characteristics defined for 13-18 Quality conformance evidence.

### Characteristics

- Identifies what tasks/activities/process produce the information
- Identifies when the data was collected
- Identifies source of any associated data
- Identifies the associated quality criteria
- Identifies any associated measurements using the information

## [WP_13_19](@.md#wp_13_19) Review evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-19
```

When [wp_13_19_review_evidence](=.md#wp_13_19_review_evidence) is produced, the information item shall provide the characteristics defined for 13-19 Review evidence.

### Characteristics

- Provides the context information about the review:
  - what was reviewed
  - lists reviewers who attended and their area of responsibility
  - status of the review
- Provides information about the scope of the review:
  - checklists
  - review criteria
  - requirements
  - compliance to standards
- Effort information about:
  - preparation time spent for the review
  - time spent in the review
- Review findings:
  - non-conformances
  - improvement suggestions

## [WP_13_24](@.md#wp_13_24) Validation results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-24
```

When [wp_13_24_validation_results](=.md#wp_13_24_validation_results) is produced, the information item shall provide the characteristics defined for 13-24 Validation results.

### Characteristics

- Validation data, logs, feedback, or documentation
- Validation measure passed
- Validation measure not passed
- Validation measure not executed, and a rationale
- Information about the validation execution (date, participants etc.)
- Abstraction or summary of validation results

## [WP_13_25](@.md#wp_13_25) Verification results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-25
```

When [wp_13_25_verification_results](=.md#wp_13_25_verification_results) is produced, the information item shall provide the characteristics defined for 13-25 Verification results.

### Characteristics

- Verification data and logs
- Verification measure passed
- Verification measure not passed
- Verification measure not executed, and a rationale
- Information about the verification execution (date, "object-under- verification", etc.)
- Abstraction or summary of verification results

## [WP_13_50](@.md#wp_13_50) ML test results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-50
```

When [wp_13_50_ml_test_results](=.md#wp_13_50_ml_test_results) is produced, the information item shall provide the characteristics defined for 13-50 ML test results.

### Characteristics

- Test data and logs
- Test data with correct results
- Test data with incorrect results
- Test data not executed, and a rationale
- Information about the test execution (date, participants, model version etc.)
- Abstraction or summary of ML test results

## [WP_13_51](@.md#wp_13_51) Consistency Evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-51
```

When [wp_13_51_consistency_evidence](=.md#wp_13_51_consistency_evidence) is produced, the information item shall provide the characteristics defined for 13-51 Consistency Evidence.

### Characteristics

- Demonstrates bidirectional traceability between artifacts or information in artifacts, throughout all phases of the life cycle, by e.g.,
  - tool links
  - hyperlinks
  - editorial references
  - naming conventions
- Evidence that the content of the referenced or mapped information coheres semantically along the traceability chain, e.g., by
  - performing pair working or group work
  - performing by peers, e.g., spot checks
  - maintaining revision histories in documents
  - providing change commenting (via e.g., meta-information) of database or repository entries Note: This evidence can be accompanied by e.g., Definition of Done (DoD) approaches.

## [WP_13_52](@.md#wp_13_52) Communication Evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-52
```

When [wp_13_52_communication_evidence](=.md#wp_13_52_communication_evidence) is produced, the information item shall provide the characteristics defined for 13-52 Communication Evidence.

### Characteristics

- All forms of interpersonal communication such as
  - e-mails, also automatically generated ones
  - tool-supported workflows
  - meeting, verbally or via meeting minutes (e.g., daily standups)
  - podcast
  - blog
  - videos
  - forum
  - live chat
  - wikis
  - photo protocol

## [WP_13_55](@.md#wp_13_55) Process resource and infrastructure documentation

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 13-55
```

When [wp_13_55_process_resource_and_infrastructure_documentation](=.md#wp_13_55_process_resource_and_infrastructure_documentation) is produced, the information item shall provide the characteristics defined for 13-55 Process resource and infrastructure documentation.

### Characteristics

- Information on availability, allocation, and usage of
  - Facilities
  - Tools and corresponding licenses
  - Networks
  - Services
  - Samples
- for non-standard and critical resources and infrastructure.

## [WP_14_01](@.md#wp_14_01) Change history

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-01
```

When [wp_14_01_change_history](=.md#wp_14_01_change_history) is produced, the information item shall provide the characteristics defined for 14-01 Change history.

### Characteristics

- Historical records of all changes made to an object (document, file, software component, etc.):
  - description of change
  - version information about changed object
  - date of change
  - change requester information
  - change control record information

## [WP_14_02](@.md#wp_14_02) Corrective action

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-02
```

When [wp_14_02_corrective_action](=.md#wp_14_02_corrective_action) is produced, the information item shall provide the characteristics defined for 14-02 Corrective action.

### Characteristics

- Identifies the initial problem
- Identifies the ownership for completion of defined action
- Defines a solution (series of actions to fix problem)
- Identifies the open date and target closure date
- Contains a status indicator
- Indicates follow up audit actions

## [WP_14_10](@.md#wp_14_10) Work package

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-10
```

When [wp_14_10_work_package](=.md#wp_14_10_work_package) is produced, the information item shall provide the characteristics defined for 14-10 Work package.

### Characteristics

- Defines activities to be performed
- Documents ownership for activities e.g., by domains
- Documents critical dependencies to other work packages
- Documents input and output work products
- Documents the critical dependencies between defined work products
- Information needed to perform these activities
- Estimates of effort, duration NOTE: The work package descriptions may be integrated into the/be a part of a schedule, see 08-56

## [WP_14_50](@.md#wp_14_50) Stakeholder groups list

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-50
```

When [wp_14_50_stakeholder_groups_list](=.md#wp_14_50_stakeholder_groups_list) is produced, the information item shall provide the characteristics defined for 14-50 Stakeholder groups list.

### Characteristics

- Identifies:
- involved parties
- weight/importance of each stakeholder group
- representative(s) for each stakeholder group
- information needs of each stakeholder group

## [WP_14_53](@.md#wp_14_53) Role Assignment

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-53
```

When [wp_14_53_role_assignment](=.md#wp_14_53_role_assignment) is produced, the information item shall provide the characteristics defined for 14-53 Role Assignment.

### Characteristics

- Assignment of person(s) to roles
  - required competencies vs existing competencies
  - required skills vs existing skills
  - required experience and trainings based on identified competencies / skills gap

## [WP_14_54](@.md#wp_14_54) Hardware Bill of materials

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 14-54
```

When [wp_14_54_hardware_bill_of_materials](=.md#wp_14_54_hardware_bill_of_materials) is produced, the information item shall provide the characteristics defined for 14-54 Hardware Bill of materials.

### Characteristics

- Uniquely identifies type, supplier, and amount of the complete set of all hardware parts of the hardware

## [WP_15_06](@.md#wp_15_06) Project status

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-06
```

When [wp_15_06_project_status](=.md#wp_15_06_project_status) is produced, the information item shall provide the characteristics defined for 15-06 Project status.

### Characteristics

- Status of in regards to progress and consistency of schedule, work item content, tasks, resources (human resources, infrastructure, hardware/materials, budget), skills and competence of human resources
- planned progress and expenditure against dates/deadlines and actual expenditure
- reasons for variance from planned progress
- threats to continued progress
- issues which may affect the ability of the project to achieve its goals
- contingency actions

## [WP_15_07](@.md#wp_15_07) Reuse analysis evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-07
```

When [wp_15_07_reuse_analysis_evidence](=.md#wp_15_07_reuse_analysis_evidence) is produced, the information item shall provide the characteristics defined for 15-07 Reuse analysis evidence.

### Characteristics

- Identification of reuse opportunities
- Identification of constraints for reuse
- Identification of regression test cases
- Identification of reuse infrastructure
- Identification of known defects

## [WP_15_09](@.md#wp_15_09) Risk status

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-09
```

When [wp_15_09_risk_status](=.md#wp_15_09_risk_status) is produced, the information item shall provide the characteristics defined for 15-09 Risk status.

### Characteristics

- Identifies the status, or the change, of an identified risk:
  - risk statement
  - risk source
  - risk impact and risk probability
  - categories and risk thresholds, e.g., for prioritization or setting a status
  - risk treatment activities in progress

## [WP_15_12](@.md#wp_15_12) Problem status

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-12
```

When [wp_15_12_problem_status](=.md#wp_15_12_problem_status) is produced, the information item shall provide the characteristics defined for 15-12 Problem status.

### Characteristics

- Indicates progress of problem resolution
- Status of problem e.g.,
  - by problem categories/classification
  - by problem resolution stage

## [WP_15_13](@.md#wp_15_13) Assessment/audit report

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-13
```

When [wp_15_13_assessment_audit_report](=.md#wp_15_13_assessment_audit_report) is produced, the information item shall provide the characteristics defined for 15-13 Assessment/audit report.

### Characteristics

- States the purpose of assessment
- Method used for assessment
- Requirements used for the assessment
- Assumptions and limitations
- Identifies the context and scope information required:
  - date of assessment
  - organizational unit assessed
  - sponsor information
  - assessment team
  - attendees
  - scope/coverage
  - assesses and information
  - assessment tool used
- Records the result:
  - Data
  - identifies the gaps, potentials, weaknesses or non-conformances that require corrective actions

## [WP_15_16](@.md#wp_15_16) Improvement opportunity

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-16
```

When [wp_15_16_improvement_opportunity](=.md#wp_15_16_improvement_opportunity) is produced, the information item shall provide the characteristics defined for 15-16 Improvement opportunity.

### Characteristics

- Identifies what the problem is
- Identifies what the cause of a problem is
- Suggest what could be done to fix the problem
- Identifies the value (expected benefit) in performing the improvement
- Identifies the penalty for not making the improvement

## [WP_15_51](@.md#wp_15_51) Analysis Results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-51
```

When [wp_15_51_analysis_results](=.md#wp_15_51_analysis_results) is produced, the information item shall provide the characteristics defined for 15-51 Analysis Results.

### Characteristics

- Identification of the object under analysis.
- The analysis criteria used, e.g.:
  - selection criteria or prioritization scheme used
  - decision criteria
  - quality criteria
- The analysis results, e.g.:
  - what was decided/selected
  - reason for the selection
  - assumptions made
  - potential negative impact
- Aspects of the analysis may include
  - correctness
  - understandability
  - verifiability
  - feasibility
  - validity

## [WP_15_52](@.md#wp_15_52) Verification Results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-52
```

When [wp_15_52_verification_results](=.md#wp_15_52_verification_results) is produced, the information item shall provide the characteristics defined for 15-52 Verification Results.

### Characteristics

- Verification data and logs
- Verification measure passed
- Verification measure not passed
- Verification measure not executed
- information about the test execution (date, tester name etc.)
- Abstraction or summary of verification results

## [WP_15_54](@.md#wp_15_54) Tailoring documentation

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-54
```

When [wp_15_54_tailoring_documentation](=.md#wp_15_54_tailoring_documentation) is produced, the information item shall provide the characteristics defined for 15-54 Tailoring documentation.

### Characteristics

- Applied criteria for tailoring,
- Evidence that the defined process is tailored from the standard process according to the defined criteria

## [WP_15_55](@.md#wp_15_55) Problem analysis evidence

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-55
```

When [wp_15_55_problem_analysis_evidence](=.md#wp_15_55_problem_analysis_evidence) is produced, the information item shall provide the characteristics defined for 15-55 Problem analysis evidence.

### Characteristics

- Author and involved parties
- Date of the analysis
- Context and root cause of the problem
- Analysis result may include
  - Impact
  - Potential negative impact
  - Affected parties
  - Potential solution (if known)

## [WP_15_56](@.md#wp_15_56) Configuration status

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 15-56
```

When [wp_15_56_configuration_status](=.md#wp_15_56_configuration_status) is produced, the information item shall provide the characteristics defined for 15-56 Configuration status.

### Characteristics

- Summary of configuration management records including relevant status
- Analysis of the configuration management overall state
- Identification of baselines made

## [WP_16_03](@.md#wp_16_03) Configuration management system

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 16-03
```

When [wp_16_03_configuration_management_system](=.md#wp_16_03_configuration_management_system) is produced, the information item shall provide the characteristics defined for 16-03 Configuration management system.

### Characteristics

- Supports the configuration management for the scope of the configuration item list contents
- Correct configuration of products
- Can recreate any release or test configuration
- Ability to report configuration status
- Has to cover all relevant tools

## [WP_16_06](@.md#wp_16_06) Process repository

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 16-06
```

When [wp_16_06_process_repository](=.md#wp_16_06_process_repository) is produced, the information item shall provide the characteristics defined for 16-06 Process repository.

### Characteristics

- Contains process descriptions
- Supports multiple presentations of process assets

## [WP_16_50](@.md#wp_16_50) Organizational structure

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 16-50
```

When [wp_16_50_organizational_structure](=.md#wp_16_50_organizational_structure) is produced, the information item shall provide the characteristics defined for 16-50 Organizational structure.

### Characteristics

- Disciplinary reporting line
- Organizational units and sub-units, if applicable

## [WP_16_52](@.md#wp_16_52) ML data management system

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 16-52
```

When [wp_16_52_ml_data_management_system](=.md#wp_16_52_ml_data_management_system) is produced, the information item shall provide the characteristics defined for 16-52 ML data management system.

### Characteristics

- The ML data management system is part of the configuration management system (see 16-03) and
- Supports data management activities like data collection, description, ingestion, exploration, profiling, labeling/annotation, selection, structuring and cleansing
- Provides the data for different purposes, e.g., training, testing
- Supports the relevant sources of ML data

## [WP_17_00](@.md#wp_17_00) Requirement

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 17-00
```

When [wp_17_00_requirement](=.md#wp_17_00_requirement) is produced, the information item shall provide the characteristics defined for 17-00 Requirement.

### Characteristics

- An expectation of functions and capabilities (e.g., non-functional requirements), or one of its interfaces
- from a black-box perspective
- that is verifiable, does not imply a design or implementation decision, is unambiguous, and does not introduce contradictions to other requirements.
- A requirements statement that implies, or represents, a design or implementation decision is called "Design Constraint".
- Examples for requirements aspects at the system level are thermal characteristics such as
  - heat dissipation
  - dimensions
  - weight
  - materials
- Examples of aspects related to requirements about system interfaces are
  - connectors
  - cables
  - housing
- Examples for requirements at the hardware level are
  - lifetime and mission profile, lifetime robustness
  - maximum price
  - storage and transportation requirements
  - functional behavior of analog or digital circuits and logic
  - quiescent current, voltage impulse responsiveness to crank, start- stop, drop-out, load dump
  - temperature, maximum hardware heat dissipation
  - power consumption depending on the operating state such as sleep-mode, start-up, reset conditions
  - frequencies, modulation, signal delays, filters, control loops
  - power-up and power-down sequences, accuracy and precision of signal acquisition or signal processing time
  - computing resources such as memory space and CPU clock tolerances
  - maximum abrasive wear and shearing forces for e.g., pins or soldering joints
  - requirements resulting from lessons learned
  - safety related requirements derived from the technical safety concept

## [WP_17_05](@.md#wp_17_05) Requirements for work products

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 17-05
```

When [wp_17_05_requirements_for_work_products](=.md#wp_17_05_requirements_for_work_products) is produced, the information item shall provide the characteristics defined for 17-05 Requirements for work products.

### Characteristics

- Requirements for content and structure, storage and control
  - Identifies documentation specific meta data, such as id, date, author information, ownership, access rights, review and approval status with, where applicable, status model and workflow, or others
  - Identifies requirements on documentation structure, e.g., table of content or figures or other formal aspects
  - May be provided by documentation templates
  - May be based on tool specific templates
  - Defines the storage location such as data repository, tool, versioning system
  - Requirements for versioning
  - Requirements for baselining
  - Distribution of the documents
  - Maintenance and disposal of the documents
  - May be specific for certain types of documents

## [WP_17_54](@.md#wp_17_54) Requirement Attribute

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 17-54
```

When [wp_17_54_requirement_attribute](=.md#wp_17_54_requirement_attribute) is produced, the information item shall provide the characteristics defined for 17-54 Requirement Attribute.

### Characteristics

- Meta-attributes that support structuring and definition of release scopes of requirements.
- Can be realized by means of tools. NOTE: usage of requirements attributes may further support analysis of requirements.

## [WP_17_55](@.md#wp_17_55) Resource needs

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 17-55
```

When [wp_17_55_resource_needs](=.md#wp_17_55_resource_needs) is produced, the information item shall provide the characteristics defined for 17-55 Resource needs.

### Characteristics

- Identification of required resources for process performance
- Staff including competencies, skills and authorities needs
- Material, equipment, and infrastructure
- Time and budget NOTE: Needs are derived from Work Breakdown structure and schedule

## [WP_17_57](@.md#wp_17_57) Special Characteristics

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 17-57
```

When [wp_17_57_special_characteristics](=.md#wp_17_57_special_characteristics) is produced, the information item shall provide the characteristics defined for 17-57 Special Characteristics.

### Characteristics

- Special Characteristics in terms of relevant standards such as IATF 16949, VDA 6.x Guidelines, ISO 26262.
- Special Characteristics according to IATF 16949:2016-10 [15], Chapters 8.3.3.3, are product characteristics or production process parameters that may have an impact on safety or compliance with official regulations, the fit, the function, the performance or further processing of the product.
- Special characteristics shall be verifiable according to VDA vol. 1 NOTE: A typical method for identifying and rate special characteristics is an FMEA.

## [WP_18_00](@.md#wp_18_00) Standard

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-00
```

When [wp_18_00_standard](=.md#wp_18_00_standard) is produced, the information item shall provide the characteristics defined for 18-00 Standard.

### Characteristics

- Identification of to whom/what they apply
- Expectations for conformance are identified
- Conformance to requirements can be demonstrated
- Provisions for tailoring or exception to the requirements are included

## [WP_18_06](@.md#wp_18_06) Product release criteria

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-06
```

When [wp_18_06_product_release_criteria](=.md#wp_18_06_product_release_criteria) is produced, the information item shall provide the characteristics defined for 18-06 Product release criteria.

### Characteristics

- Defines expectations for product release:
  - release type and status
  - required elements of the release
  - product completeness including documentation
  - adequacy and coverage of testing
  - limit for open defects
  - change control status

## [WP_18_07](@.md#wp_18_07) Quality criteria

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-07
```

When [wp_18_07_quality_criteria](=.md#wp_18_07_quality_criteria) is produced, the information item shall provide the characteristics defined for 18-07 Quality criteria.

### Characteristics

- Defines the expectations for work products and process performance
- Including thresholds/tolerance levels, required measurements, required checkpoints
- Defines what is an adequate work product (required elements, completeness expected, accuracy, etc.)
- Defines what constitutes the completeness of the defined tasks
- Defines what constitutes the performance of the defined tasks
- Establishes expected performance attributes

## [WP_18_52](@.md#wp_18_52) Escalation path

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-52
```

When [wp_18_52_escalation_path](=.md#wp_18_52_escalation_path) is produced, the information item shall provide the characteristics defined for 18-52 Escalation path.

### Characteristics

- Defined mechanisms to report and confirm escalation relevant issues
- Identifies stakeholders to be included in the escalation path
- Identifies levels of escalation

## [WP_18_53](@.md#wp_18_53) Configuration item selection criteria

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-53
```

When [wp_18_53_configuration_item_selection_criteria](=.md#wp_18_53_configuration_item_selection_criteria) is produced, the information item shall provide the characteristics defined for 18-53 Configuration item selection criteria.

### Characteristics

- Identify types of work products to be subject to configuration control

## [WP_18_57](@.md#wp_18_57) Change analysis criteria

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-57
```

When [wp_18_57_change_analysis_criteria](=.md#wp_18_57_change_analysis_criteria) is produced, the information item shall provide the characteristics defined for 18-57 Change analysis criteria.

### Characteristics

- Defines analysis criteria, such as
  - resource requirements
  - scheduling issues
  - risks
  - benefits

## [WP_18_58](@.md#wp_18_58) Process performance objectives

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-58
```

When [wp_18_58_process_performance_objectives](=.md#wp_18_58_process_performance_objectives) is produced, the information item shall provide the characteristics defined for 18-58 Process performance objectives.

### Characteristics

- Objectives for the process of creating the process outcomes and capability level 2 achievements, and corresponding evaluation criteria
- Assumptions and constraints, if applicable
- Used as the basis for deriving a detailed planning
- Examples:
  - Effort, costs, or budget targets (e.g., min/max limits)
  - Process-specific deadlines in line with milestones, or frequency of activities (o e.g., dates for deliveries to the customer, quality gates)
  - Metrics (e.g., max. number of open change requests per release, max. ratio of configuration items in status "in work" at certain milestones before next delivery / release date)

## [WP_18_59](@.md#wp_18_59) Review and approval criteria for work products

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-59
```

When [wp_18_59_review_and_approval_criteria_for_work_products](=.md#wp_18_59_review_and_approval_criteria_for_work_products) is produced, the information item shall provide the characteristics defined for 18-59 Review and approval criteria for work products.

### Characteristics

- Specifies for each type of work products review and approval needs
  - If and when a review is required
  - Who shall review it
  - Who shall approve it
  - Review method(s) to be used
  - Criteria for approval

## [WP_18_70](@.md#wp_18_70) Business goals

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-70
```

When [wp_18_70_business_goals](=.md#wp_18_70_business_goals) is produced, the information item shall provide the characteristics defined for 18-70 Business goals.

### Characteristics

- Explanation of the business goals
- Requirements for the business needs
- Associations to other goals
- Reasons for the existence of the goals and needs, level of degree of the need and effect on the business not having that need
- Conditions, constraints, assumptions
- Timeframe for achievement
- Authorization at the highest level

## [WP_18_80](@.md#wp_18_80) Improvement opportunity

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-80
```

When [wp_18_80_improvement_opportunity](=.md#wp_18_80_improvement_opportunity) is produced, the information item shall provide the characteristics defined for 18-80 Improvement opportunity.

### Characteristics

- Cause of the improvement need, e.g.,
  - from qualitative or quantitative process performance analysis, evaluations, and monitoring
  - industry best practice review, state-of-the-art observations, market studies etc.
- Improvement objectives derived from organizational business goals and improvement needs
- Organizational scope
- Process scope
- Activities to be performed to keep all those affected by the improvement informed
- Priorities

## [WP_18_81](@.md#wp_18_81) Improvement evaluation results

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 18-81
```

When [wp_18_81_improvement_evaluation_results](=.md#wp_18_81_improvement_evaluation_results) is produced, the information item shall provide the characteristics defined for 18-81 Improvement evaluation results.

### Characteristics

- Operational impacts of identified changes on the product(s) and processes
- Expected benefit
- Conditions, constraints, assumptions

## [WP_19_01](@.md#wp_19_01) Process performance strategy

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 19-01
```

When [wp_19_01_process_performance_strategy](=.md#wp_19_01_process_performance_strategy) is produced, the information item shall provide the characteristics defined for 19-01 Process performance strategy.

### Characteristics

- The operational approach to achieve the process outcomes, consistent with the Process Performance Objectives (18-58), e.g.:
  - proceedings, including the monitoring of the performance of the process
  - methodology
- scope(s) of the strategy within the process, e.g.:
  - development sites
  - application domain-specific differences (e.g., software drivers versus. powertrain software)
  - disciplines (e.g., different configuration management approaches for software and hardware, or combined approaches)
  - options due to socio-cultural differences

## [WP_19_50](@.md#wp_19_50) ML data quality approach

```yaml
Type: WorkProduct
Source: Automotive SPICE PAM v4.0 Annex B
InformationItem: 19-50
```

When [wp_19_50_ml_data_quality_approach](=.md#wp_19_50_ml_data_quality_approach) is produced, the information item shall provide the characteristics defined for 19-50 ML data quality approach.

### Characteristics

- The ML data quality approach
- Defines Quality criteria (see 18-07) e.g., the relevant data sources, reliability and consistency of labelling, completeness against ML data requirementsv
- Describes analysis activities of the data
- Describes activities to ensure the quality of the data to avoid issues e.g., data bias, bad labeling
