# iREPS Master Dictionary

## Purpose

The iREPS Master Dictionary is the official single source of truth for words, acronyms, modules, workflows, roles, data concepts, and operational terms used inside iREPS.

The goal is to explain each term in simple language while preserving the correct iREPS meaning. This dictionary is intended for municipal users, fieldworkers, supervisors, managers, developers, support teams, trainers, and future iREPS documentation.

The iREPS Master Dictionary must be reviewed and refined continuously. Every new iREPS word, acronym, workflow name, module name, role, data concept, and operational term must be added here so that all iREPS documentation and training uses one approved meaning.

This is Version 1.5 of the iREPS Master Dictionary. It preserves the locked meanings from Version 1.4 and adds the approved source-neutral Meter Master lifecycle, ownership, refresh, conflict and reporting terminology. Meter Master lifecycle classifications are derived from canonical references and are not stored status fields.

## 1. Core iREPS Concepts

### Term: iREPS

- **Acronym:** iREPS

- **Simple meaning:** The iREPS platform is the system used to manage municipal field operations, assets, meters, premises, workflows, and operational data. It full name is Intelligent Revenue Enhancement and Protection Soluton.

- **Detailed explanation:** iREPS supports utilities, municipal and service-provider work in the field and in the office. It connects operational work, field evidence, asset records, premises, meters, user roles, mapped locations, workflow outcomes, and reporting. Instead of treating municipal information as a static list, iREPS records what happens over time: who captured the information, where it happened, what evidence was collected, what status changed, and what operational result was produced.

- **Example:** A municipality can use iREPS to discover meters, install meters, read meters, disconnect and reconnect supply, inspect assets, remove meters, and review operational reports.

- **Related terms:** Transaction (TRN), Asset (AST), Premise, Meter, Registry, Warehouse, Geofence, MREAD, BGO

### Term: iREPS Master Dictionary

- **Acronym:** None

- **Simple meaning:** The official iREPS source of truth for terms, acronyms, and meanings.

- **Detailed explanation:** The iREPS Master Dictionary is the structured knowledge base for iREPS language. It gives every important word or acronym a standard meaning so that municipal users, fieldworkers, supervisors, managers, developers, trainers, and support teams speak the same language. It supports manuals, onboarding, courses, in-app help, certification planning, website pages, support articles, and training videos.

- **Example:** A user who needs to understand Transaction can read the Transaction entry and learn that it is a work record in iREPS.

- **Related terms:** Dictionary, Knowledge Base, Training, Certification, User Manual

### Term: Dictionary

- **Acronym:** None

- **Simple meaning:** A structured list of words and meanings.

- **Detailed explanation:** In iREPS, the dictionary is more than a normal glossary. It is the official working reference for project language. It explains both the simple user meaning and the deeper operational meaning of each term. This reduces confusion when the same word appears in code, documentation, diagrams, user manuals, training, and business discussions.

- **Example:** The dictionary explains the difference between Meter Installation and Meter Discovery.

- **Related terms:** iREPS Master Dictionary, Knowledge Base, Definition, Term

### Term: Operational Data

- **Acronym:** None

- **Simple meaning:** Data created from real work done in the field or office.

- **Detailed explanation:** Operational data is information iREPS creates, updates, or stores while users perform work. It includes captured assets, meter readings, inspections, disconnections, reconnections, removals, evidence, GPS points, user actions, statuses, outcomes, and history. It is different from static reference data because it grows and changes as operations happen.

- **Example:** A completed meter reading creates operational data such as the reading value, reading date, outcome, media evidence, GPS position, and fieldworker details.

- **Related terms:** Transaction (TRN), Registry, Asset (AST), MREAD, Operational History

### Term: Operational History

- **Acronym:** None

- **Simple meaning:** The record of what has happened to an asset or meter over time.

- **Detailed explanation:** Operational history is the accumulated story of a meter, premise, asset, or workflow. For a meter, it can include readings, disconnections, reconnections, inspections, vending-linked activity, status changes, media evidence, and removal. iREPS uses operational history to support reporting, audit, investigation, and municipal decision-making.

- **Example:** A meter history may show installation, commissioning, monthly readings, one disconnection, one reconnection, an inspection finding, vending-linked activity, and eventual removal.

- **Related terms:** Meter Lifetime, Meter Reading, Transaction (TRN), Registry, Audit Trail

### Term: Data Flow

- **Acronym:** None

- **Simple meaning:** The movement of data from one part of iREPS to another.

- **Detailed explanation:** Data flow explains what iREPS creates, updates, or stores when a process happens. It helps connect the field process with the system effect. For example, Meter Reading adds reading history, Disconnection creates or completes a lifecycle transaction and updates operational status, and Removal closes the active operational life of a meter.

- **Example:** Meter Installation creates or registers meter data; Meter Commissioning activates a newly installed meter for operations.

- **Related terms:** Diagram, Transaction (TRN), Registry, Asset (AST), Meter Lifetime

## 2. Meter Lifetime Concepts

### Term: Meter

- **Acronym:** None

- **Simple meaning:** A device used to measure electricity or water usage.

- **Detailed explanation:** In iREPS, a meter is not treated only as a number or static device. It has a lifecycle. It may be installed, discovered, commissioned, read, inspected, disconnected, reconnected, linked to vending activity, and eventually removed. The meter record preserves identity, location, operational status, evidence, and history.

- **Example:** A conventional electricity meter at a premise can be captured in iREPS, read monthly, inspected when there is an anomaly, and removed when replaced.

- **Related terms:** Meter Lifetime, Meter Installation, Meter Discovery, MREAD, Asset (AST)

### Term: Meter Lifetime

- **Acronym:** None

- **Simple meaning:** The full life story of a meter inside iREPS.

- **Detailed explanation:** Meter lifetime means the meter is managed from the time it becomes known to iREPS until it exits active operations. The lifetime can start through new Meter Installation or through Meter Discovery of an existing installed meter. It continues through operational events such as readings, inspections, disconnections, reconnections, and vending-linked activity. It ends when the meter is removed from active operations, while its history remains available.

- **Example:** A meter starts as Not Captured, becomes Registered in iREPS, becomes an Operational Meter, accumulates readings and events, and is later Removed.

- **Related terms:** Meter, Operational Life, Meter Removal, Removed, Operational History

### Term: Not Captured

- **Acronym:** None

- **Simple meaning:** A meter or asset is not yet recorded in iREPS.

- **Detailed explanation:** Not Captured is the starting state before iREPS has a usable operational record for the meter or asset. The physical meter may already exist on the premises, or it may still need to be installed. Once the meter is captured through installation or discovery, it moves into the iREPS record system.

- **Example:** A fieldworker arrives at a premise and finds a meter that is not yet recorded in iREPS. Before discovery is submitted, that meter is still Not Captured in iREPS.

- **Related terms:** Meter Discovery, Meter Installation, Registered in iREPS

### Term: Registered in iREPS

- **Acronym:** None

- **Simple meaning:** The meter has a record inside iREPS.

- **Detailed explanation:** Registered in iREPS means iREPS now knows about the meter and has created or updated a meter record. Registration may happen through a new Meter Installation or through Meter Discovery of an existing installed meter. Being registered does not automatically mean the meter was commissioned; commissioning belongs only to the new installation path.

- **Example:** A discovered existing meter becomes Registered in iREPS after the fieldworker captures its details and submits the discovery record.

- **Related terms:** Meter Exists in iREPS, Meter Discovery, Meter Installation, Asset (AST)

### Term: Meter Exists in iREPS

- **Acronym:** None

- **Simple meaning:** iREPS has created or found a meter record.

- **Detailed explanation:** This term means that the meter has been captured into the iREPS system. Both Meter Installation and Meter Discovery can result in a meter existing in iREPS. However, the path after registration differs: a newly installed meter may go through commissioning, while a discovered existing installed meter goes into operational life without commissioning.

- **Example:** After a new meter is installed and captured, iREPS creates a registered meter record. After an existing installed meter is discovered, iREPS also creates or updates a registered meter record.

- **Related terms:** Registered in iREPS, Meter Installation, Meter Discovery, Meter Commissioning

### Term: Meter Installation

- **Acronym:** None

- **Simple meaning:** A new meter is physically installed and captured in iREPS.

- **Detailed explanation:** Meter Installation is the controlled process where a new meter is placed at a premise and its details are captured in iREPS. It is different from Meter Discovery. Installation is the path that can lead to Meter Commissioning because the meter is newly installed and must be activated for operational use.

- **Example:** A fieldworker installs a new conventional meter at a premise and captures the meter number, location, photos, and installation details in iREPS.

- **Related terms:** Meter Commissioning, Meter Discovery, Asset (AST), Premise, Operational Meter

### Term: Meter Discovery

- **Acronym:** None

- **Simple meaning:** An existing installed meter is found and captured in iREPS.

- **Detailed explanation:** Meter Discovery is used when a meter already exists physically on the premises but is not yet properly captured or linked in iREPS. Discovery does not mean the meter is newly installed. It means the fieldworker has found an already-installed meter and is bringing it into the iREPS operational record. A discovered meter does not go through commissioning because commissioning applies to the installation path only.

- **Example:** A fieldworker visits a premise and finds an electricity meter already mounted on the wall. The meter is captured through Meter Discovery because it already exists physically.

- **Related terms:** Meter Installation, Registered in iREPS, Existing Installed Meter, Meter Master

### Term: Existing Installed Meter

- **Acronym:** None

- **Simple meaning:** A meter that is already physically installed before it is captured in iREPS.

- **Detailed explanation:** An existing installed meter is not a new meter installation. It is already on the premises and may already be in use. iREPS may discover it later during fieldwork. This concept is important because Meter Discovery does not follow the same commissioning path as Meter Installation.

- **Example:** A municipality may have thousands of meters already installed before iREPS is introduced. Those meters can be brought into iREPS through Meter Discovery.

- **Related terms:** Meter Discovery, Not Captured, Registered in iREPS, Operational Meter

### Term: New Meter

- **Acronym:** None

- **Simple meaning:** A meter that is being installed for the first time through the iREPS workflow.

- **Detailed explanation:** A new meter is captured through Meter Installation. It is different from an existing installed meter discovered in the field. A newly installed meter may require commissioning before it becomes operational in iREPS.

- **Example:** A contractor replaces a missing meter with a new one and captures it through the Meter Installation workflow.

- **Related terms:** Meter Installation, Meter Commissioning, Asset (AST), Operational Meter

### Term: Meter Commissioning

- **Acronym:** None

- **Simple meaning:** Activating a newly installed meter for operational use.

- **Detailed explanation:** Meter Commissioning applies only to the Meter Installation path. It confirms that a newly installed meter is ready to be treated as operational. It must not be applied to a discovered existing meter because that meter was already installed before discovery. Commissioning is therefore an activation step for new installations, not a general step for every registered meter.

- **Example:** After a new meter is installed, iREPS records commissioning to show that the newly installed meter is ready for readings and other operations.

- **Related terms:** Meter Installation, Commissioned / Active Meter, Operational Meter, Activation

### Term: Commissioned / Active Meter

- **Acronym:** None

- **Simple meaning:** A newly installed meter that has been activated for operations.

- **Detailed explanation:** A Commissioned / Active Meter is the result of the installation path after commissioning. It means the newly installed meter is ready for operational use. This term should not imply that discovered existing meters were commissioned through iREPS. Discovered existing meters can still become operational meters, but they enter operational life through the discovery path.

- **Example:** A new meter is installed, checked, commissioned, and then becomes available for meter reading and future operational events.

- **Related terms:** Meter Commissioning, Meter Installation, Operational Meter

### Term: Operational Meter

- **Acronym:** None

- **Simple meaning:** A meter that can participate in normal iREPS operations.

- **Detailed explanation:** An Operational Meter is a meter that has entered active operational use in iREPS. It may come from a commissioned installation path or from discovery of an already-installed existing meter. Once operational, it can accumulate readings, lifecycle transactions, inspections, vending-linked activity, and status changes.

- **Example:** A discovered existing meter and a newly installed commissioned meter can both become operational meters in iREPS.

- **Related terms:** Meter Lifetime, Operational Life, Meter Reading, Meter Inspection

### Term: Operational Life

- **Acronym:** None

- **Simple meaning:** The period when a meter is active and operational events can happen to it.

- **Detailed explanation:** Operational Life is the main working stage of a meter in iREPS. During this stage, the meter can be read, disconnected, reconnected, inspected, linked to vending data, and eventually removed. Most operational events can repeat many times before the meter exits active operations.

- **Example:** A meter may receive monthly readings, be disconnected for a valid operational reason, reconnected later, inspected for anomalies, and eventually removed.

- **Related terms:** Operational Meter, Meter Reading, Meter Disconnection, Meter Reconnection, Meter Inspection, Vending, Meter Removal

### Term: Meter Reading

- **Acronym:** MREAD

- **Simple meaning:** Capturing a meter reading value and outcome.

- **Detailed explanation:** Meter Reading is the process of recording meter usage information from a meter. In iREPS, meter reading is captured as an operational activity and contributes to the meter’s reading history. It may include the reading value, date, outcome, reason, evidence, media, and user information.

- **Example:** A fieldworker captures a reading of 14582 on a conventional electricity meter and submits the result through iREPS Mobile.

- **Related terms:** MREAD, Registry MREAD, MREAD Staging, Reading History, Meter Lifetime

### Term: Reading History

- **Acronym:** None

- **Simple meaning:** The list of readings captured for a meter over time.

- **Detailed explanation:** Reading History shows how a meter’s readings have changed over time. It helps iREPS support reporting, review, staging, validation, and investigation. It is part of the larger operational history of a meter.

- **Example:** A meter may have readings for Cycle 9, Cycle 10, and Cycle 11, each with a date, value, and outcome.

- **Related terms:** Meter Reading, MREAD, Registry MREAD, Operational History

### Term: Meter Disconnection

- **Acronym:** DCN

- **Simple meaning:** Disconnecting supply to a meter or premise when required.

- **Detailed explanation:** Meter Disconnection is an operational event where supply is disconnected according to an authorised workflow. In iREPS, it should create or complete a lifecycle transaction and update operational status. Disconnection is part of the meter’s operational life and may happen more than once over time.

- **Example:** A meter may be disconnected after an authorised disconnection work order is executed in the field.

- **Related terms:** DCN, Meter Reconnection, Transaction (TRN), Operational Status, Lifecycle Transaction

### Term: Meter Reconnection

- **Acronym:** RCN

- **Simple meaning:** Restoring supply after a meter or premise was disconnected.

- **Detailed explanation:** Meter Reconnection is the operational event that reverses a disconnection when the correct conditions are met. In iREPS, it creates or completes a lifecycle transaction and updates operational status. Like disconnection, reconnection becomes part of the meter’s operational history.

- **Example:** After a customer resolves a disconnection issue, a fieldworker executes a reconnection transaction and supply is restored.

- **Related terms:** RCN, Meter Disconnection, Transaction (TRN), Operational Status, Lifecycle Transaction

### Term: Meter Inspection

- **Acronym:** INSP

- **Simple meaning:** Checking the condition, correctness, and physical connection details of a meter.

- **Detailed explanation:** Meter Inspection is an operational event used to capture findings, anomalies, condition, photos, and possible normalisation actions. It can help detect issues such as tampering, damaged meters, incorrect details, poor access, mismatched records, or suspicious wiring. Inspections can happen repeatedly during the meter’s operational life.

- **Example:** A fieldworker inspects a meter and records that the seal is broken, the meter box is damaged, and the wiring must be investigated.

- **Related terms:** INSP, Anomaly, Normalisation, Evidence, Meter Lifetime, Operational History

### Term: Vending

- **Acronym:** VEND

- **Simple meaning:** Commercial or usage-related activity linked to a meter.

- **Detailed explanation:** Vending is not treated exactly the same as field-executed work such as Meter Reading or Disconnection. It is a linked operational or commercial data stream connected to the meter’s life. Vending helps show that the meter may have usage or commercial activity associated with it during operational life.

- **Example:** A prepaid meter may have vending activity that can be linked to the meter lifecycle for operational or commercial visibility.

- **Related terms:** VEND, Meter, Operational Life, Commercial Stream, Usage Activity, Meter Master

### Term: Meter Removal

- **Acronym:** REM

- **Simple meaning:** Removing a meter from active operations.

- **Detailed explanation:** Meter Removal is the end-of-life or exit event for a meter’s active operational life. After removal, the meter should no longer be treated as active, but its history must remain available for reporting, audit, and investigation. Removal is different from disconnection because disconnection may be temporary, while removal closes the active meter lifecycle.

- **Example:** A damaged old meter is physically removed and replaced with a new meter. The old meter is marked as removed, but its reading and event history remains available.

- **Related terms:** REM, Removed, Meter Lifetime, Operational History, Asset (AST)

### Term: Removed

- **Acronym:** REM

- **Simple meaning:** The meter is no longer active in operations.

- **Detailed explanation:** Removed is the final state after Meter Removal. A removed meter should not continue to receive normal active operational events. However, its historical record remains important because it may still be needed for reporting, audit, investigations, or understanding meter replacement history.

- **Example:** A meter removed from a premise is no longer active, but iREPS can still show when it was installed, read, inspected, and removed.

- **Related terms:** Meter Removal, Operational History, Exit Event

## 3. Workflow and Transaction Concepts

### Term: Transaction

- **Acronym:** TRN

- **Simple meaning:** A transaction or work record in iREPS.

- **Detailed explanation:** A Transaction represents a specific piece of operational work in iREPS. It records the workflow, assignment, execution, outcome, user actions, evidence, and status changes. Transactions are central to iREPS because they preserve what was done, who did it, when it was done, where it was done, and what result was produced. A Transaction / TRN is not part of the iREPS Geography hierarchy because it is an action or work record on a meter or AST, not a geography level.

- **Example:** A Meter Reading transaction records that a fieldworker visited a premise, captured a reading, submitted evidence, and completed the reading outcome.

- **Related terms:** TRN, MREAD, DCN, RCN, REM, Lifecycle Transaction, Outcome

### Term: Lifecycle Transaction

- **Acronym:** TRN

- **Simple meaning:** A transaction that records or changes an important stage in an asset’s operational life.

- **Detailed explanation:** A lifecycle transaction records events that affect the life, condition, or status of a meter or asset. Examples include disconnection, reconnection, removal, installation, discovery, or inspection. These transactions help build the operational history of the asset.

- **Example:** A Disconnection transaction updates the meter’s operational story by recording that supply was disconnected on a specific date.

- **Related terms:** Transaction, Meter Lifetime, Operational Status, Operational History

### Term: BGO

- **Acronym:** BGO

- **Simple meaning:** A bulk geofenced origination work process in iREPS.

- **Detailed explanation:** BGO is used where iREPS needs to manage a group of related fieldwork items (a group) as a controlled operation. It can organise bulk tasks such as meter discovery, data cleansing, or other guided operational work. The details depend on the module, but the key idea is that work is grouped, controlled, issued, executed, and tracked.

- **Example:** A Meter Discovery BGO may guide fieldworkers through a group of premises where meters need to be discovered and captured.

- **Related terms:** Bulk Work, Transaction (TRN), Meter Discovery, Field Operation, Supervisor

### Term: Outcome

- **Acronym:** None

- **Simple meaning:** The result of a completed iREPS task.

- **Detailed explanation:** Outcome records what happened when a transaction or workflow was completed. Outcomes must be clear and consistent because they are used for reporting, registries, staging, and operational decisions. For MREAD, canonical outcomes include Successful Reading, Unsuccessful Reading, and No Access.

- **Example:** A meter reading task may end with the outcome Successful Reading if a valid reading was captured.

- **Related terms:** Transaction (TRN), MREAD, No Access, Successful Reading, Unsuccessful Reading

### Term: No Access

- **Acronym:** None

- **Simple meaning:** The fieldworker can see the meter but cannot physically touch it with their hand.

- **Detailed explanation:** No Access means physical access to the meter is blocked. The user may be able to see the meter with the eye, but the hand cannot reach the meter. This distinction is important in meter discovery and inspection because illegal connections or suspicious wiring may not be fully investigated unless the fieldworker can physically touch the meter and examine its wires, seals, and connections. No Access is therefore not just “I cannot see the meter”; it means the fieldworker cannot physically access it enough to do the required work safely and properly.

- **Example:** A meter is visible behind a locked gate or inside a locked box. The fieldworker can see it, but cannot reach it or touch the wires. The task is recorded as No Access.

- **Related terms:** MREAD, Meter Discovery, Meter Inspection, Outcome, Fieldworker, Evidence

### Term: Successful Reading

- **Acronym:** None

- **Simple meaning:** A meter reading was captured successfully.

- **Detailed explanation:** Successful Reading means the reading task produced a valid reading result according to iREPS rules. This outcome can feed into registry reporting and later staging processes.

- **Example:** A fieldworker reads a meter, captures the value, submits the evidence, and the value passes validation.

- **Related terms:** MREAD, Meter Reading, Registry MREAD, Outcome

### Term: Unsuccessful Reading

- **Acronym:** None

- **Simple meaning:** A reading attempt happened but did not produce a successful valid reading.

- **Detailed explanation:** Unsuccessful Reading is used when the fieldworker attempted the reading but the result could not be accepted as a successful reading. This may include a captured value failing validation or another issue that prevents the reading from being treated as successful. It is different from No Access, where the problem is physical access to the meter.

- **Example:** A fieldworker captures a reading that is lower than the previous reading and fails validation. The attempt may be recorded as Unsuccessful Reading.

- **Related terms:** MREAD, Outcome, No Access, Successful Reading

## 4. Asset and Location Concepts

### Term: iREPS Geography

- **Acronym:** None

- **Simple meaning:** The approved iREPS location hierarchy from country down to meter.

- **Detailed explanation:** iREPS Geography is the official way iREPS represents where work belongs. The locked geography hierarchy must always be shown as: Country → Province → District Municipality → Local Municipality / workbase / LM / Metro → Ward → ERF → Premise → Asset / AST / Meter. This hierarchy explains the location and operational scope of iREPS data. Transaction / TRN is not part of the geography hierarchy because a TRN is an action or work record performed on a meter or AST, not a place.

- **Example:** A fieldworker works inside a selected workbase / LM and ward. The ward controls which ERFs appear. From an ERF, the user can open or create premises, then work with assets, ASTs, and meters.

- **Related terms:** Country, Province, District Municipality, Local Municipality, Workbase, LM, Metro, Ward, ERF, Premise, Asset, AST, Meter, Operational Scope

### Term: iREPS Geography Hierarchy

- **Acronym:** None

- **Simple meaning:** The locked diagram flow used to show geography in iREPS.

- **Detailed explanation:** The iREPS Geography Hierarchy is the approved diagram flow for manuals, training, diagrams, and user guidance. It must be represented as: Country → Province → District Municipality → Local Municipality / workbase / LM / Metro → Ward → ERF → Premise → Asset / AST / Meter. The hierarchy stops at Meter. Transaction / TRN must not be added to this geography flow because TRN belongs to workflow and action concepts.

- **Example:** The ERFs training page should show the user that ERFs sit below Ward and above Premise in the iREPS hierarchy.

- **Related terms:** iREPS Geography, Ward, ERF, Premise, Asset, AST, Meter, Transaction (TRN)

### Term: Country

- **Acronym:** None

- **Simple meaning:** The national geography level in iREPS.

- **Detailed explanation:** Country is the top level of the iREPS Geography hierarchy. It groups all lower administrative and operational geography levels under the national context.

- **Example:** South Africa is the country level for South African iREPS municipal work.

- **Related terms:** iREPS Geography, Province, District Municipality, Local Municipality, Workbase

### Term: Province

- **Acronym:** None

- **Simple meaning:** The provincial geography level below Country.

- **Detailed explanation:** Province is the second level of the iREPS Geography hierarchy. It groups district municipalities, local municipalities, metros, wards, ERFs, and related operational records under the correct provincial context.

- **Example:** Eastern Cape is a province that can contain district municipalities, local municipalities, wards, and ERFs.

- **Related terms:** iREPS Geography, Country, District Municipality, Local Municipality, Ward

### Term: District Municipality

- **Acronym:** DM

- **Simple meaning:** The district municipal geography level below Province.

- **Detailed explanation:** District Municipality is an administrative geography level that groups local municipalities under a district context. In iREPS Geography, it sits between Province and Local Municipality / workbase / LM / Metro.

- **Example:** OR Tambo District Municipality can contain local municipalities such as King Sabata Dalindyebo.

- **Related terms:** DM, iREPS Geography, Province, Local Municipality, LM, Workbase

### Term: Local Municipality

- **Acronym:** LM

- **Simple meaning:** A municipal geography and workbase level inside iREPS.

- **Detailed explanation:** Local Municipality is the municipal level where iREPS operational work is commonly organised. In the locked iREPS Geography hierarchy, this level is represented as Local Municipality / workbase / LM / Metro because a user's operational workbase may be a local municipality or a metro.

- **Example:** King Sabata Dalindyebo is a Local Municipality that can operate as a workbase in iREPS.

- **Related terms:** LM, Workbase, Metro, Ward, Operational Scope

### Term: Metro

- **Acronym:** None

- **Simple meaning:** A metropolitan municipality used as a workbase level in iREPS.

- **Detailed explanation:** Metro is included in the locked iREPS Geography hierarchy at the same operational level as Local Municipality / workbase / LM. A metro can act as the user's workbase and contain wards, ERFs, premises, assets, and meters.

- **Example:** City of Johannesburg can be treated as a Metro workbase in iREPS.

- **Related terms:** Local Municipality, LM, Workbase, Ward, Operational Scope

### Term: Asset

- **Acronym:** AST

- **Simple meaning:** A physical or operational item that iREPS tracks.

- **Detailed explanation:** An Asset is something with operational value that can be captured, located, updated, inspected, acted on, and tracked over time. In the locked iREPS Geography hierarchy, the final level is shown as Asset / AST / Meter because the meter is the key service asset used in many iREPS mobile workflows. A Transaction / TRN is not a geography level; it is an action or work record performed on an Asset / AST / Meter.

- **Example:** A newly installed meter creates or updates an Asset record linked to the premise where the meter is installed.

- **Related terms:** AST, Meter, Meter Installation, Meter Discovery, Operational Status, Transaction (TRN), iREPS Geography

### Term: Premise

- **Acronym:** None

- **Simple meaning:** A property, dwelling, business, unit, or service location where municipal service activity happens.

- **Detailed explanation:** A premise is the operational service point or location where iREPS links meters, fieldwork, address details, occupancy, property type, and related operations. A meter is normally linked to a premise so that iREPS knows where it is located and what property or unit it serves. A premise always has address information. In iREPS address language, strNo means street number; strName means street name; strType means the street type such as Street, Road, Avenue, Drive, or Close; name means the property, complex, building, business, flats, sectional title, or place name where needed; and unitNo means the specific flat, unit, room, or sectional title unit number where applicable.

- **Example:** For a flat, the premise address may include strNo: 12, strName: Nelson Mandela, strType: Drive, name: Sunrise Flats, and unitNo: Unit 8.

- **Related terms:** Meter, ERF, Ward, Geofence, Address, strNo, strName, strType, name, unitNo

### Term: Address

- **Acronym:** None

- **Simple meaning:** The structured location description of a premise.

- **Detailed explanation:** An address helps fieldworkers and office users identify where a premise is located. In iREPS, address fields should be structured so they can support search, display, field navigation, and reporting. The main address fields are strNo, strName, strType, name, and unitNo.

- **Example:** A premise address can be displayed as “12 Nelson Mandela Drive, Sunrise Flats, Unit 8”.

- **Related terms:** Premise, strNo, strName, strType, name, unitNo

### Term: strNo

- **Acronym:** None

- **Simple meaning:** The street number of a premise address.

- **Detailed explanation:** strNo identifies the number assigned to the property or service location on a street. It is a core part of the premise address because it helps fieldworkers locate the correct property.

- **Example:** In “12 Nelson Mandela Drive”, the strNo is 12.

- **Related terms:** Premise, Address, strName, strType

### Term: strName

- **Acronym:** None

- **Simple meaning:** The street name of a premise address.

- **Detailed explanation:** strName stores the actual name of the street without the street type. Keeping the street name separate from the street type supports cleaner searching and consistent address formatting.

- **Example:** In “12 Nelson Mandela Drive”, the strName is Nelson Mandela.

- **Related terms:** Premise, Address, strNo, strType

### Term: strType

- **Acronym:** None

- **Simple meaning:** The type of street used in a premise address.

- **Detailed explanation:** strType describes the kind of street or road. Examples include Street, Road, Avenue, Drive, Close, Crescent, Boulevard, and Way. Separating strType from strName helps avoid inconsistent address capture.

- **Example:** In “12 Nelson Mandela Drive”, the strType is Drive.

- **Related terms:** Premise, Address, strNo, strName

### Term: name

- **Acronym:** None

- **Simple meaning:** The property, building, complex, business, or place name used in the premise address when needed.

- **Detailed explanation:** The name field gives extra location context where a street address alone is not enough. It is especially useful for flats, sectional title properties, complexes, commercial properties, schools, churches, estates, and government buildings.

- **Example:** For “Sunrise Flats, Unit 8”, the name can be Sunrise Flats.

- **Related terms:** Premise, Address, unitNo, Property Type

### Term: unitNo

- **Acronym:** None

- **Simple meaning:** The unit, flat, room, or sectional title number inside a property or building.

- **Detailed explanation:** unitNo identifies a specific unit within a larger property. It is important for flats, sectional title, townhouse complexes, estates, commercial buildings, and multi-tenant properties.

- **Example:** In “Sunrise Flats, Unit 8”, the unitNo is Unit 8.

- **Related terms:** Premise, Address, name, Sectional Title, Flats

### Term: ERF

- **Acronym:** ERF

- **Simple meaning:** A cadastral land parcel, property stand, or property unit.

- **Detailed explanation:** An ERF is a cadastral property parcel used to understand land and property boundaries. In the locked iREPS Geography hierarchy, ERF sits below Ward and above Premise. ERFs help connect premises and municipal operations to the correct geographic and cadastral base.

- **Example:** A premise may be located on ERF 1234 within a specific ward and local municipality.

- **Related terms:** Premise, Ward, LM, Cadastral, Geofence, iREPS Geography

### Term: Ward

- **Acronym:** None

- **Simple meaning:** A municipal ward area used for operational scope.

- **Detailed explanation:** A ward is a local government area inside a Local Municipality / workbase / LM / Metro. In the locked iREPS Geography hierarchy, Ward sits below Local Municipality / workbase / LM / Metro and above ERF. In iREPS Mobile, the selected ward controls which ERFs are loaded and shown on the ERFs page. Ward must be explicit for operational data and workflows.

- **Example:** A fieldworker may be assigned meter reading work for a ward such as ZA21570003.

- **Related terms:** LM, Workbase, Metro, ERF, Premise, Geofence, Scope, iREPS Geography

### Term: LM

- **Acronym:** LM

- **Simple meaning:** Local Municipality.

- **Detailed explanation:** LM is the local municipality level in iREPS operational scope. In the locked iREPS Geography hierarchy, this level is shown as Local Municipality / workbase / LM / Metro. Many iREPS workflows, records, and imports are organised by LM or Metro and then by Ward. LM helps iREPS separate operational data by municipal jurisdiction.

- **Example:** King Sabata Dalindyebo Local Municipality uses LM pCode ZA2157 in the iREPS context.

- **Related terms:** Ward, Municipality, LM pCode, Workbase, Metro, Scope, Governance, iREPS Geography

### Term: Geofence

- **Acronym:** Gf

- **Simple meaning:** A digital boundary used to locate or control work geographically.

- **Detailed explanation:** A geofence is a mapped boundary around an operational area, such as a ward, premise, ERF, or work zone. iREPS can use geofences to support location validation, operational scoping, reporting, and fieldwork routing. The abbreviation Gf may be used where space is limited.

- **Example:** A fieldworker’s meter reading task may be linked to a ward geofence to confirm the work falls inside the correct area.

- **Related terms:** Gf, Ward, ERF, Premise, Location, GPS

### Term: Pcode

- **Acronym:** Pcode

- **Simple meaning:** A coded identifier for an administrative area or geography.

- **Detailed explanation:** Pcodes identify geographic or administrative units such as local municipalities and wards. They help iREPS stamp records with the correct municipal scope and avoid relying only on names, which may be duplicated or written differently.

- **Example:** ZA2157 is the pCode for King Sabata Dalindyebo Local Municipality. ZA21570003 is a ward-style pCode example under that LM.

- **Related terms:** LM, Ward, Scope, Admin, Geography

## 5. Sales Pipeline Concepts

This section is the official iREPS terminology source for Sales Pipeline business, data, collection, validation, build, and upload concepts. The Sales Pipeline rules govern how the pipeline operates. This dictionary governs what the approved terms mean.

### Term: Sales Pipeline

- **Acronym:** None

- **Simple meaning:** The controlled process that prepares, validates, aggregates, links, and uploads approved sales data into iREPS.

- **Detailed explanation:** The iREPS Sales Pipeline moves provider sales data through governed layers: RAW provider download → RAW STAGING → Atomic Sales → Monthly Sales → Meter Master → Sales All Meters. Each layer has a different purpose. The pipeline must preserve traceability, validate every required scope, reconcile totals, and stop when data is unsafe or inconsistent.

- **Example:** A Conlog file for July 2026 is prepared for one LM and one month, converted into Atomic Sales, aggregated into Monthly Sales, and then included in controlled downstream Meter Master and Sales All Meters builds.

- **Related terms:** RAW Provider Download, RAW STAGING, Atomic Sales, Monthly Sales, Meter Master, Sales All Meters

### Term: Sales Provider

- **Acronym:** None

- **Simple meaning:** The external system or company that supplies sales transaction data.

- **Detailed explanation:** A Sales Provider is the source of commercial or vending transactions used by the Sales Pipeline. Provider identity must remain explicit so iREPS knows where the sales data came from and does not mix incompatible provider data inside a provider-specific collection family.

- **Example:** Conlog is the current governed sales provider for the TEST Sales Pipeline.

- **Related terms:** Conlog, Provider Code, Sales Data, Provider-neutral Architecture

### Term: Provider Code

- **Acronym:** None

- **Simple meaning:** The approved short value used to identify a sales provider in data.

- **Detailed explanation:** Provider Code is the canonical machine-readable identifier for the provider. The current governed value is `conlog`. A provider code must be validated and must not be silently changed, guessed, or mixed with another provider’s records.

- **Example:** A Sales All Meters document currently uses `provider: "conlog"`.

- **Related terms:** Sales Provider, Conlog, Sales All Meters

### Term: Conlog

- **Acronym:** None

- **Simple meaning:** The current vending and sales-data provider used by the governed iREPS Sales Pipeline.

- **Detailed explanation:** Conlog is the current provider for the active TEST collection family. The current collections retain Conlog-specific names during TEST stabilisation. A future provider-neutral redesign may support other providers, but that is a separate governed architecture and migration process.

- **Example:** Conlog portal downloads are placed unchanged in the RAW sales folder before pipeline preparation.

- **Related terms:** Sales Provider, Provider Code, Conlog Sales Collection Family, Provider-neutral Architecture

### Term: Sales Data

- **Acronym:** None

- **Simple meaning:** Commercial transaction and meter-related information received from a sales or vending environment.

- **Detailed explanation:** Sales Data can include meter numbers, transaction dates, purchase amounts, costs, VAT, customer numbers, account numbers, and last-purchase information. It is different from field operational data. The Sales Pipeline may establish a sales match, but it must not decide operational visibility.

- **Example:** A Conlog purchase for a meter is Sales Data; a fieldworker’s meter photo is operational field data.

- **Related terms:** Sales Repository, Atomic Sales, Monthly Sales, Sales Match, Operational Data

### Term: Sales Repository

- **Acronym:** None

- **Simple meaning:** The governed collections and approved files where sales-related records are stored.

- **Detailed explanation:** The Sales Repository contains approved sales-side data used for reporting, aggregation, meter awareness, and downstream linking. It is not the same as the mobile Warehouse and should not be loaded into the mobile app as one large operational dataset.

- **Example:** `conlog_sales_atomic`, the Monthly Sales collections, and `sales-all-meters` form part of the current Sales Repository.

- **Related terms:** Sales Data, Conlog Sales Collection Family, Warehouse, Sales Pipeline

### Term: Conlog Sales Collection Family

- **Acronym:** None

- **Simple meaning:** The four current Conlog Firestore collections used for Atomic and Monthly Sales.

- **Detailed explanation:** The current collection family is `conlog_sales_atomic`, `conlog_sales_monthly`, `conlog_sales_monthly_lm`, and `conlog_sales_monthly_lm_groups`. These names remain active during TEST stabilisation and must not contain another provider’s data.

- **Example:** A monthly Conlog upload writes to the three governed Monthly Sales collections only after Atomic Sales is complete.

- **Related terms:** conlog_sales_atomic, conlog_sales_monthly, conlog_sales_monthly_lm, conlog_sales_monthly_lm_groups

### Term: RAW Provider Download

- **Acronym:** RAW

- **Simple meaning:** The original file downloaded from the sales provider.

- **Detailed explanation:** A RAW Provider Download is source evidence. Its contents must remain unchanged. It must not be opened, edited, re-saved, converted manually, or overwritten by the pipeline. A controlled local filename may be applied without changing the file contents.

- **Example:** `conlog_raw_sales__ZA7423__2026-07.csv` is the governed local name for an unchanged July 2026 Conlog download.

- **Related terms:** RAW Sales File, Source Evidence, RAW STAGING, Source Traceability

### Term: RAW Sales File

- **Acronym:** RAW

- **Simple meaning:** The unchanged provider file used as the starting evidence for one sales period.

- **Detailed explanation:** The RAW Sales File belongs in the approved raw-sales input folder. It is not upload-ready and is not Atomic Sales. The pipeline validates and transforms it through Stage 00 while preserving the original file.

- **Example:** The operator downloads the Conlog CSV, renames it under the approved filename contract, and places it in `input/raw-sales`.

- **Related terms:** RAW Provider Download, RAW STAGING, Pipeline Stage, Source Evidence

### Term: Source Evidence

- **Acronym:** None

- **Simple meaning:** Original information preserved so the source of pipeline data can be proven.

- **Detailed explanation:** Source Evidence allows iREPS to trace generated outputs back to an unchanged provider file. It supports investigation, reconciliation, audit, and repeatable rebuilding.

- **Example:** The original provider CSV and its SHA-256 value form part of the source evidence for a monthly run.

- **Related terms:** RAW Provider Download, Source Traceability, SHA-256, Audit Report

### Term: RAW STAGING

- **Acronym:** None

- **Simple meaning:** A standardised provider-specific input created from the original RAW file.

- **Detailed explanation:** RAW STAGING is a validated intermediate layer between the original provider download and Atomic Sales. It uses the approved provider-specific columns and is not uploaded to Firestore. For current Conlog data, it is generated by Stage 00 and consumed by Stage 01.

- **Example:** A six-column Conlog staging file containing LM, transaction date, meter number, amount, cost, and VAT is RAW STAGING.

- **Related terms:** RAW Provider Download, Atomic Sales, Stage 00, Stage 01

### Term: Atomic Sales

- **Acronym:** None

- **Simple meaning:** The transaction-level sales layer in which one record represents one normalised source transaction.

- **Detailed explanation:** Atomic Sales is the downstream source of truth for Monthly Sales aggregation. It preserves transaction identity, meter identity, time, monetary values, provider context, and source lineage. Atomic outputs are not considered uploaded until the approved uploader writes and verifies them in Firestore.

- **Example:** One Conlog purchase made by one meter at a specific time becomes one Atomic Sales record.

- **Related terms:** Atomic Sales Transaction, conlog_sales_atomic, Monthly Sales, Source Traceability

### Term: Atomic Sales Transaction

- **Acronym:** None

- **Simple meaning:** One normalised purchase or sales transaction in the Atomic layer.

- **Detailed explanation:** An Atomic Sales Transaction represents the smallest governed sales event used by the pipeline. Its identity must be deterministic and unique within the governed source so duplicate identities can be detected and stopped.

- **Example:** A purchase of R100.00 becomes one Atomic transaction with `amountTotalC = 10000`.

- **Related terms:** Atomic Sales, Deterministic Identity, Integer Cents, Transaction Date

### Term: conlog_sales_atomic

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing Conlog Atomic Sales transactions.

- **Detailed explanation:** `conlog_sales_atomic` stores the approved transaction-level Conlog records. It is upstream of all Monthly Sales datasets and must be uploaded and verified before the related monthly aggregates are treated as complete.

- **Example:** The Atomic uploader writes verified July 2026 Conlog transactions for ZA7423 into `conlog_sales_atomic`.

- **Related terms:** Atomic Sales, Conlog Sales Collection Family, Monthly Sales, Upload Verification

### Term: Monthly Sales

- **Acronym:** None

- **Simple meaning:** Sales totals aggregated from approved Atomic Sales for one month.

- **Detailed explanation:** Monthly Sales is derived only from approved Atomic outputs. The pipeline builds three linked views for one LM and one month: meter-month, LM-month, and LM-month sales-group totals. These layers must reconcile with Atomic Sales before upload.

- **Example:** All July purchases for one meter are combined into one July meter-month record.

- **Related terms:** Meter-Month Sales, LM-Month Sales, LM-Month Sales Group, Monthly Reconciliation

### Term: Meter-Month Sales

- **Acronym:** None

- **Simple meaning:** One meter’s aggregated sales result for one LM and one month.

- **Detailed explanation:** Meter-Month Sales combines all approved Atomic transactions for the same normalized meter number, LM, and month. It records purchase count, amounts, and first and last purchase times according to the canonical monthly schema.

- **Example:** Meter 04085345850 may have four purchases totalling 45,000 cents in July 2026.

- **Related terms:** conlog_sales_monthly, Monthly Sales, Normalized Meter Number, Purchase Count

### Term: conlog_sales_monthly

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing one Conlog sales aggregate per meter, LM, and month.

- **Detailed explanation:** The deterministic identity combines LM pCode, normalized meter number, and year-month. The collection must contain only the canonical fields defined by its locked schema.

- **Example:** `ZA7423__04085345850__2026-07` is a meter-month document identity.

- **Related terms:** Meter-Month Sales, Monthly Sales, Deterministic Document ID

### Term: LM-Month Sales

- **Acronym:** None

- **Simple meaning:** The total approved sales result for one LM in one month.

- **Detailed explanation:** LM-Month Sales summarises purchase count, meter count, monetary totals, and first and last purchase times across the selected LM/month. It must reconcile with Atomic Sales and the sum of all meter-month records.

- **Example:** ZA7423 has one LM-Month record for July 2026.

- **Related terms:** conlog_sales_monthly_lm, Monthly Sales, LM pCode, Monthly Reconciliation

### Term: conlog_sales_monthly_lm

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing one Conlog aggregate per LM and month.

- **Detailed explanation:** Its deterministic identity combines LM pCode and year-month. It is the LM-level monthly summary and must equal the reconciled totals from the Atomic and meter-month layers.

- **Example:** `ZA7423__2026-07` is an LM-month document identity.

- **Related terms:** LM-Month Sales, Monthly Reconciliation, Deterministic Document ID

### Term: LM-Month Sales Group

- **Acronym:** None

- **Simple meaning:** One LM-month sales total separated into an approved sales-value group.

- **Detailed explanation:** LM-Month Sales Groups help reports compare meters and purchases across governed sales bands. The sum of all groups for the LM/month must reconcile to the LM-Month Sales result.

- **Example:** July 2026 purchases may be summarised into GR1 through GR5 groups.

- **Related terms:** conlog_sales_monthly_lm_groups, Sales Group, Monthly Reconciliation

### Term: conlog_sales_monthly_lm_groups

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing Conlog LM-month totals by sales group.

- **Detailed explanation:** Its deterministic identity combines LM pCode, year-month, and sales group ID. It is a reporting aggregate and must not independently reinterpret RAW data.

- **Example:** `ZA7423__2026-07__GR3` is an LM-month-group document identity.

- **Related terms:** LM-Month Sales Group, Sales Group, Deterministic Document ID

### Term: Sales Group

- **Acronym:** GR

- **Simple meaning:** An approved monthly sales-value band used for grouping meters and purchases.

- **Detailed explanation:** Sales Groups classify monthly sales amounts for reporting without changing Atomic Sales. The current groups are GR1 below R99.99, GR2 from R100.00 to R299.99, GR3 from R300.00 to R499.99, GR4 from R500.00 to R999.99, and GR5 from R1,000.00 upward.

- **Example:** A meter with R450.00 in monthly purchases belongs to GR3 for that month.

- **Related terms:** LM-Month Sales Group, Monthly Sales, Sales Analytics

### Term: Monthly Reconciliation

- **Acronym:** None

- **Simple meaning:** Proving that all monthly sales layers agree.

- **Detailed explanation:** For one LM and month, Atomic totals must equal the sum of meter-month records, the LM-month record, and the sum of LM-month sales groups. Purchase counts, meter counts, amount, cost, VAT, and first and last purchase times must be checked where applicable.

- **Example:** The July Atomic amount equals the July meter-month total, LM-month total, and grouped total.

- **Related terms:** Reconciliation, Atomic Sales, Monthly Sales, Validation

### Term: Pipeline Stage

- **Acronym:** Stage

- **Simple meaning:** One numbered step in the governed Sales Pipeline.

- **Detailed explanation:** Each Pipeline Stage has one controlled responsibility. Stages 00 to 04 process one LM and one month. Stages 05 and 06 build one explicit continuous full-period range. Stages 07 and 08 upload one frozen approved full-period CSV to one explicitly selected Firebase project.

- **Example:** Stage 03 builds the three Monthly Sales datasets from one approved Atomic file.

- **Related terms:** Stage 00, Stage 01, Stage 02, Stage 03, Stage 04, Stage 05, Stage 06, Stage 07, Stage 08

### Term: Stage 00

- **Acronym:** None

- **Simple meaning:** The step that validates an original provider download and creates RAW STAGING.

- **Detailed explanation:** Stage 00 processes exactly one LM and one month, preserves the RAW source unchanged, validates the provider structure and values, reports rejected rows, and writes no staging output when critical validation fails.

- **Example:** Stage 00 transforms the unchanged July Conlog download into the approved July Conlog RAW STAGING file.

- **Related terms:** RAW Provider Download, RAW STAGING, Rejected Row, Preflight Validation

### Term: Stage 01

- **Acronym:** None

- **Simple meaning:** The step that converts approved RAW STAGING into Atomic Sales.

- **Detailed explanation:** Stage 01 is the controlled boundary where current Conlog decimal rand source values are converted exactly once into integer cents for Atomic Sales. It creates upload-ready Atomic CSV outputs.

- **Example:** Stage 01 converts `100.00` rand into `10000` cents.

- **Related terms:** RAW STAGING, Atomic Sales, Integer Cents, Monetary Conversion Boundary

### Term: Stage 02

- **Acronym:** None

- **Simple meaning:** The step that uploads and verifies Atomic Sales in Firestore.

- **Detailed explanation:** Stage 02 writes the approved Atomic CSV for one LM and month to the governed Atomic collection using explicit environment controls and post-upload verification.

- **Example:** Stage 02 uploads the verified July Atomic file to `ireps-test/conlog_sales_atomic`.

- **Related terms:** conlog_sales_atomic, Upload Verification, Explicit Project Selection

### Term: Stage 03

- **Acronym:** None

- **Simple meaning:** The step that builds the three Monthly Sales datasets and their manifest.

- **Detailed explanation:** Stage 03 consumes exactly one approved Atomic CSV for one LM/month, builds meter-month, LM-month, and LM-month-group outputs, reconciles them, fingerprints them, and creates a month-specific successful build manifest.

- **Example:** Stage 03 creates the July 2026 monthly outputs and one July Stage 03 manifest.

- **Related terms:** Monthly Sales, Build Manifest, SHA-256, Monthly Reconciliation

### Term: Stage 04

- **Acronym:** None

- **Simple meaning:** The step that uploads and verifies the three Monthly Sales datasets.

- **Detailed explanation:** Stage 04 consumes the exact successful Stage 03 manifest for one Firebase project, LM, and month. Normal mode is create-only. Controlled resume is limited to recovery of the same partial upload.

- **Example:** Stage 04 uploads the three reconciled July datasets after confirming their SHA-256 values.

- **Related terms:** Create-only, Controlled Resume, Monthly Sales, Upload Audit Report

### Term: Stage 05

- **Acronym:** None

- **Simple meaning:** The step that builds one complete Meter Master staging file for an explicit continuous month range.

- **Detailed explanation:** Stage 05 combines all required monthly meter-level data in the selected range with approved reference data. It dynamically discovers every required month, resolves governed duplicate identities, and produces one complete Meter Master CSV and successful manifest.

- **Example:** Stage 05 builds Meter Master for ZA7423 from September 2025 through July 2026.

- **Related terms:** Meter Master, Full-Period Build, Continuous Month Range, Customer Details, 90 Days No Purchase Report

### Term: Stage 06

- **Acronym:** None

- **Simple meaning:** The step that builds Sales All Meters from the approved Meter Master and monthly sales history.

- **Detailed explanation:** Stage 06 keeps every Meter Master identity, adds monthly and total sales measures, uses an explicit as-of date for recency, creates a successful manifest, and must not derive or output operational visibility.

- **Example:** A meter with no purchases remains in the Stage 06 output with zero sales totals.

- **Related terms:** Sales All Meters, As-of Date, monthlyTotalsC, Operational Visibility Ownership

### Term: Stage 07

- **Acronym:** None

- **Simple meaning:** The step that uploads one frozen approved Meter Master CSV.

- **Detailed explanation:** Stage 07 validates the successful Stage 05 manifest and exact CSV before connecting to Firestore. `create-only` performs the initial approved load into an empty Meter Master collection, `refresh` safely applies a newly approved full-period build to an established collection, and `resume` is only recovery of the exact same failed frozen upload contract.

- **Example:** Stage 07 uploads the same approved Meter Master build to an explicitly approved TEST project.

- **Related terms:** Meter Master, Frozen CSV, Initial Meter Master load, Recurring Meter Master refresh, Controlled Resume

### Term: Stage 08

- **Acronym:** None

- **Simple meaning:** The step that uploads one frozen approved Sales All Meters CSV.

- **Detailed explanation:** Stage 08 validates the successful Stage 06 manifest, exact source CSV, project, provider, month range, totals, and ownership contract. It writes only Sales Pipeline-owned fields and must preserve and ignore any existing approved operational `master.visibility` value during controlled recovery.

- **Example:** Stage 08 rejects a staging CSV that contains a `visibility` column.

- **Related terms:** Sales All Meters, Operational Visibility Ownership, Frozen CSV, Upload Verification

### Term: Pipeline Dependency

- **Acronym:** None

- **Simple meaning:** The rule that a downstream stage cannot proceed until its required upstream data is complete and verified.

- **Detailed explanation:** The mandatory dependency is RAW provider download → RAW STAGING → Atomic Sales → Monthly Sales → Meter Master → Sales All Meters. A missing, unreconciled, or unverified upstream month blocks downstream building or uploading.

- **Example:** Meter Master cannot be built from July data until July Atomic and Monthly Sales are complete and verified.

- **Related terms:** Sales Pipeline, Upload Order, Validation, Reconciliation

### Term: Upload Order

- **Acronym:** None

- **Simple meaning:** The required order in which Sales Pipeline collections are loaded.

- **Detailed explanation:** The governed Firestore order is Atomic Sales first; then the three Monthly Sales collections; then Meter Master; then Sales All Meters. This protects downstream integrity.

- **Example:** `sales-all-meters` must not be uploaded before the approved Meter Master exists.

- **Related terms:** Pipeline Dependency, conlog_sales_atomic, Meter Master, Sales All Meters

### Term: LM-Month Execution

- **Acronym:** None

- **Simple meaning:** Running a stage for exactly one LM and one month.

- **Detailed explanation:** Stages 00 through 04 use one explicit LM pCode and one `YYYY-MM` month per execution. The requested LM, filename LM, requested month, source month, and transaction month must agree.

- **Example:** One Stage 03 run processes only ZA7423 and 2026-07.

- **Related terms:** Pipeline Stage, LM pCode, Month, Monthly Sales

### Term: Full-Period Build

- **Acronym:** None

- **Simple meaning:** One controlled downstream build covering an explicit continuous range of months.

- **Detailed explanation:** Stages 05 and 06 are Full-Period Builders. They use one LM plus an explicit from-month and to-month, discover every required month dynamically, and stop when the range is incomplete or inconsistent.

- **Example:** A full-period build may cover 2025-09 through 2026-07.

- **Related terms:** Continuous Month Range, Stage 05, Stage 06, Frozen CSV

### Term: Continuous Month Range

- **Acronym:** None

- **Simple meaning:** A month range with no missing month between the start and end.

- **Detailed explanation:** A downstream full-period build must contain every month from the approved from-month through the approved to-month. Missing, duplicated, or unexpected months stop the build.

- **Example:** 2026-01, 2026-02, and 2026-03 are continuous; 2026-01 and 2026-03 without February are not.

- **Related terms:** Full-Period Build, Missing Month, Validation

### Term: Meter Master

- **Acronym:** MASTER

- **Simple meaning:** The thin canonical identity and cross-reference bridge for a meter.

- **Detailed explanation:** `meter_master` is the universal source-neutral meter identity and cross-reference register. It links approved sales data independently to an operational AST without storing sales history, operational lifecycle status, premise structure, service-provider allocation, or visibility. It uses the normalized meter number as its deterministic document identity and preserves strict field ownership across Sales Pipeline and operational writers.

- **Example:** Meter Master can show that meter 04085345850 has a Conlog sales reference and, separately, an AST reference when an approved operational workflow links one.

- **Related terms:** MASTER, meter_master, Sales Link, AST Link, Normalized Meter Number

### Term: MASTER

- **Acronym:** MASTER

- **Simple meaning:** The short iREPS name for Meter Master.

- **Detailed explanation:** MASTER refers to the governed Meter Master bridge. It supports direct identity lookup and cross-writer linking without copying large sales histories into operational mobile data.

- **Example:** FormInputMeterNo may check MASTER for controlled sales awareness.

- **Related terms:** Meter Master, Sales Link, Backend Check

### Term: meter_master

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing canonical Meter Master documents.

- **Detailed explanation:** Each document ID equals the canonical normalized meter number. The Sales Pipeline owns customer, account, and sales-reference fields. Approved operational writers own the AST reference. Meter Master itself does not contain a `visibility` field.

- **Example:** `meter_master/04085345850` is the canonical identity document for that normalized meter number.

- **Related terms:** Meter Master, Deterministic Document ID, Field Ownership, AST Link

### Term: Meter Master document identity

- **Acronym:** None
- **Simple meaning:** The permanent normalized meter number used as the Meter Master document ID.
- **Detailed explanation:** The Firestore path is `meter_master/{normalizedMeterNo}`, and the document ID must equal `meterNo.normalized`. Normalisation removes all whitespace, converts letters to uppercase, preserves leading zeroes, and imposes no universal fixed length. The identity is immutable after creation.
- **Example:** ` 04 085 345 850 ` resolves to `meter_master/04085345850`.
- **Related terms:** Meter Master, Normalized Meter Number, Deterministic Document ID

### Term: AST reference

- **Acronym:** None
- **Simple meaning:** The Meter Master link to the operational AST.
- **Detailed explanation:** `refs.asts.id` is owned by approved operational writers. A blank string means that no operational AST relationship exists. The Sales Pipeline never creates, changes, or clears this field.
- **Example:** A field installation populates the AST reference while preserving existing sales fields.
- **Related terms:** Meter Master, FIELD_ONLY, MATCHED, Operationally owned field

### Term: Sales reference

- **Acronym:** None
- **Simple meaning:** The Meter Master link to approved sales data.
- **Detailed explanation:** `refs.sales.id` is owned by the Sales Pipeline and normally equals the canonical normalized meter number. `refs.sales.provider` records the governed provider. Operational writers never create, change, or clear either sales field.
- **Example:** A Conlog sale populates the sales reference and provider without changing an AST reference.
- **Related terms:** Meter Master, SALES_ONLY, MATCHED, Pipeline-owned field

### Term: SALES_ONLY

- **Acronym:** None
- **Simple meaning:** A meter has approved sales data but no operational AST link.
- **Detailed explanation:** This conceptual classification is derived when `refs.sales.id` is populated and `refs.asts.id` is blank. It is not stored as a Meter Master status field.
- **Example:** A sales-originated Meter Master document before field matching is SALES_ONLY.
- **Related terms:** FIELD_ONLY, MATCHED, Sales reference

### Term: FIELD_ONLY

- **Acronym:** None
- **Simple meaning:** A meter has an operational AST link but no approved sales link.
- **Detailed explanation:** This conceptual classification is derived when `refs.asts.id` is populated and `refs.sales.id` is blank. It is not stored as a Meter Master status field.
- **Example:** A newly installed meter that has not appeared in sales is FIELD_ONLY.
- **Related terms:** SALES_ONLY, MATCHED, AST reference

### Term: MATCHED

- **Acronym:** None
- **Simple meaning:** A meter has both operational and sales links.
- **Detailed explanation:** This conceptual classification is derived when both `refs.asts.id` and `refs.sales.id` are populated. It is not stored as a Meter Master status field.
- **Example:** A FIELD_ONLY meter becomes MATCHED when its first approved sale is linked.
- **Related terms:** SALES_ONLY, FIELD_ONLY, Meter Master

### Term: EMPTY_OR_INCOMPLETE

- **Acronym:** None
- **Simple meaning:** A Meter Master record has neither an AST link nor a sales link.
- **Detailed explanation:** This conceptual classification is derived when both canonical references are blank. It signals an incomplete record requiring investigation and is not stored as a Meter Master status field.
- **Example:** A document with both reference IDs blank is EMPTY_OR_INCOMPLETE.
- **Related terms:** Record-level conflict, Meter Master

### Term: Pipeline-owned field

- **Acronym:** None
- **Simple meaning:** A Meter Master field only the approved Sales Pipeline may change.
- **Detailed explanation:** Current pipeline-owned fields are `customerNo`, `accountNo`, `refs.sales.id`, and `refs.sales.provider`. Operational writers must preserve them.
- **Example:** A recurring refresh may enrich `customerNo` but may not change `refs.asts.id`.
- **Related terms:** Operationally owned field, Field Ownership, Sales Pipeline

### Term: Operationally owned field

- **Acronym:** None
- **Simple meaning:** A Meter Master field only an approved operational workflow may change.
- **Detailed explanation:** The current operationally owned Meter Master field is `refs.asts.id`. The Sales Pipeline must preserve it during initial loading, refresh, and resume.
- **Example:** Meter Discovery may populate a blank AST reference on a compatible SALES_ONLY record.
- **Related terms:** Pipeline-owned field, AST reference, Field Ownership

### Term: Initial Meter Master load

- **Acronym:** None
- **Simple meaning:** The first governed creation of Meter Master from an approved sales build.
- **Detailed explanation:** Stage 07 `create-only` loads complete canonical sales-originated documents into an empty Meter Master collection using one approved frozen Stage 05 contract.
- **Example:** The first approved TEST load uses `create-only`, not `refresh`.
- **Related terms:** create-only, Stage 07, Meter Master

### Term: Recurring Meter Master refresh

- **Acronym:** None
- **Simple meaning:** A governed comparison of a new approved sales build with established Meter Master records.
- **Detailed explanation:** Stage 07 `refresh` creates missing sales-originated documents, updates only approved sales-owned fields, skips unchanged records, preserves operational links and original creation metadata, and continues after record-level conflicts. It never deletes a Meter Master document merely because it is absent from the sales build.
- **Example:** A monthly refresh enriches a FIELD_ONLY record into MATCHED without replacing its AST link.
- **Related terms:** CREATED, UPDATED, UNCHANGED, CONFLICT, Stage 07

### Term: Record-level conflict

- **Acronym:** None
- **Simple meaning:** A problem limited to one Meter Master record that makes its proposed change unsafe.
- **Detailed explanation:** The affected record is not written. A stable conflict code and existing/incoming evidence are reported, and processing continues for other valid records. A widespread version of the problem may become a run-level failure.
- **Example:** An LM mismatch on one document is reported while other compatible meters continue.
- **Related terms:** CONFLICT, COMPLETED_WITH_CONFLICTS, Conflict Report

### Term: CREATED

- **Acronym:** None
- **Simple meaning:** Refresh created a missing canonical Meter Master document.
- **Detailed explanation:** The incoming approved record had no existing canonical document and was safely created using the complete sales-originated shape.
- **Example:** A newly sold meter absent from Meter Master is classified CREATED.
- **Related terms:** Recurring Meter Master refresh, UPDATED

### Term: UPDATED

- **Acronym:** None
- **Simple meaning:** Refresh safely changed approved sales-owned fields.
- **Detailed explanation:** The existing document was compatible and required a material sales enrichment. Operational fields, controlled identity, and original creation metadata were preserved.
- **Example:** A FIELD_ONLY document receiving its first sales reference is UPDATED.
- **Related terms:** Recurring Meter Master refresh, MATCHED

### Term: UNCHANGED

- **Acronym:** None
- **Simple meaning:** The existing Meter Master already matches the approved incoming sales values.
- **Detailed explanation:** No Firestore write occurs and `metadata.updated*` remains unchanged.
- **Example:** Rerunning the same approved refresh classifies an identical compatible record as UNCHANGED.
- **Related terms:** Idempotency, Recurring Meter Master refresh

### Term: CONFLICT

- **Acronym:** None
- **Simple meaning:** Refresh skipped an unsafe Meter Master change.
- **Detailed explanation:** The affected record is not written, receives a stable conflict code and investigation evidence, and does not stop remaining valid records.
- **Example:** A conflicting controlled LM is classified CONFLICT.
- **Related terms:** Record-level conflict, COMPLETED_WITH_CONFLICTS

### Term: COMPLETED

- **Acronym:** None
- **Simple meaning:** The complete governed run finished without unresolved conflicts.
- **Detailed explanation:** Every incoming row was accounted for and final verification passed without conflicts or record failures that require investigation.
- **Example:** A refresh containing only CREATED, UPDATED, and UNCHANGED records may finish COMPLETED.
- **Related terms:** COMPLETED_WITH_CONFLICTS, FAILED

### Term: COMPLETED_WITH_CONFLICTS

- **Acronym:** None
- **Simple meaning:** Safe records completed while conflicting records were skipped and reported.
- **Detailed explanation:** This is a completed run result, not a run-level failure. Every safely processable record finished, and the conflict report identifies records requiring investigation.
- **Example:** A refresh with two isolated LM conflicts may finish COMPLETED_WITH_CONFLICTS.
- **Related terms:** Record-level conflict, CONFLICT, COMPLETED

### Term: FAILED

- **Acronym:** None
- **Simple meaning:** A genuine run-level failure prevented the complete result from being trusted.
- **Detailed explanation:** FAILED is reserved for systemic conditions such as invalid frozen input, project or credential mismatch, systemic Firestore failure, inability to report, invalid run accounting, or failed final verification. An isolated record conflict does not by itself make the run FAILED.
- **Example:** A CSV fingerprint mismatch produces FAILED before writes begin.
- **Related terms:** COMPLETED, COMPLETED_WITH_CONFLICTS, Run-level Failure

### Term: Sales All Meters

- **Acronym:** None

- **Simple meaning:** The governed sales-awareness projection for every approved Meter Master identity.

- **Detailed explanation:** Sales All Meters combines Meter Master identity and customer references with approved monthly sales history. It includes meters with sales and meters without sales. It supports reporting and quick sales awareness without becoming the canonical operational meter record.

- **Example:** A customer-only Meter Master identity appears in Sales All Meters with zero monthly totals when no approved sales transactions exist.

- **Related terms:** sales-all-meters, Meter Master, monthlyTotalsC, Sales Match

### Term: sales-all-meters

- **Acronym:** None

- **Simple meaning:** The Firestore collection containing Sales All Meters projection documents.

- **Detailed explanation:** The canonical document identity is the normalized meter number. Pipeline-owned fields include meter identity, provider, customer and account references, total sales, monthly totals, and recency fields. The Sales Pipeline must omit operational `master.visibility`.

- **Example:** `sales-all-meters/04085345850` can contain the meter’s monthly Conlog totals and latest purchase date.

- **Related terms:** Sales All Meters, Operational Visibility Ownership, totalAmountC, monthlyTotalsC

### Term: Normalized Meter Number

- **Acronym:** None

- **Simple meaning:** The canonical cleaned string used to identify the same meter consistently.

- **Detailed explanation:** The normalizer casts to string, trims outer whitespace, removes embedded whitespace, converts letters to uppercase, and preserves leading zeroes. It must not silently remove punctuation, force a fixed length, pad, truncate, or convert the meter number to a numeric value.

- **Example:** `010 236 70951` becomes `01023670951`, while a prohibited punctuation value must be rejected rather than silently rewritten.

- **Related terms:** Meter Master, Deterministic Document ID, Sales Match, Meter Number

### Term: Deterministic Document ID

- **Acronym:** None

- **Simple meaning:** A document ID calculated from governed business identity instead of generated randomly.

- **Detailed explanation:** Deterministic IDs allow repeatable lookup, duplicate prevention, reconciliation, and controlled recovery. The same approved input identity must always produce the same Firestore document ID.

- **Example:** A meter-month ID combines LM pCode, normalized meter number, and year-month.

- **Related terms:** Normalized Meter Number, Idempotent, Build Fingerprint, Firestore

### Term: Sales Link

- **Acronym:** None

- **Simple meaning:** A confirmed connection between a meter identity and approved sales-side data.

- **Detailed explanation:** A Sales Link means the meter has a canonical sales reference or matching approved sales data. It is separate from AST linkage and operational visibility. A sales-linked meter is not automatically VISIBLE, and a meter without current sales is not automatically INVISIBLE.

- **Example:** `refs.sales.id` and `refs.sales.provider` can establish the sales-side link in Meter Master.

- **Related terms:** Sales Match, Meter Master, AST Link, Visibility

### Term: Sales Match

- **Acronym:** None

- **Simple meaning:** A result showing that a normalized meter number was found in approved sales data.

- **Detailed explanation:** Sales Match is the correct term for sales-side presence. It must not be called operational visibility. A match can support an `IN SALES` badge or report result, while the backend and operational rules separately govern visibility.

- **Example:** The normalized meter number exists in the approved Sales Repository, so the form shows `IN SALES`.

- **Related terms:** IN SALES, NO SALES MATCH, Sales Link, Backend Check

### Term: IN SALES

- **Acronym:** None

- **Simple meaning:** Approved sales data was found for the normalized meter number.

- **Detailed explanation:** `IN SALES` is a sales-awareness result, not an operational visibility status. It may be shown in a form or report after a controlled lookup, but it does not authorise the Sales Pipeline to set `VISIBLE`.

- **Example:** A meter has one or more approved Conlog transactions, so the report marks it `IN SALES`.

- **Related terms:** Sales Match, Sales Repository, Visibility, Form-side Check

### Term: NO SALES MATCH

- **Acronym:** None

- **Simple meaning:** No approved sales-side match was found for the normalized meter number in the checked scope.

- **Detailed explanation:** `NO SALES MATCH` means only that the governed lookup did not find qualifying sales data. It does not prove that the physical meter is absent, unregistered, undiscovered, or operationally INVISIBLE.

- **Example:** A newly discovered meter has no current Conlog match, so the result is `NO SALES MATCH`, not `INVISIBLE`.

- **Related terms:** Sales Match, IN SALES, Visibility, Meter Discovery

### Term: AST Link

- **Acronym:** None

- **Simple meaning:** The canonical reference connecting Meter Master to an iREPS operational Asset.

- **Detailed explanation:** The AST Link is stored through the approved Meter Master AST reference and is owned by approved operational Meter Discovery and Meter Installation writers. A blank AST link means only that no AST reference is present in that pipeline record; it does not prove invisibility.

- **Example:** After an approved discovery workflow links an AST, Meter Master stores its AST identifier.

- **Related terms:** Meter Master, Asset (AST), Field Ownership, Operational Visibility Ownership

### Term: Field Ownership

- **Acronym:** None

- **Simple meaning:** The rule stating which approved writer may create or change a specific field.

- **Detailed explanation:** Field Ownership prevents one pipeline or workflow from overwriting another workflow’s truth. The Sales Pipeline owns sales-side customer, account, and sales-reference values. Approved operational workflows own AST linkage and operational visibility.

- **Example:** Stage 08 may update no operational visibility field because that field is outside Sales Pipeline ownership.

- **Related terms:** Meter Master, Operational Visibility Ownership, Sales Pipeline-owned Fields

### Term: Sales Pipeline-owned Fields

- **Acronym:** None

- **Simple meaning:** The fields the Sales Pipeline is authorised to create, validate, or upload.

- **Detailed explanation:** These are the canonical sales-side fields defined by the locked schemas and rules. They include approved sales identity, provider, customer, account, totals, monthly totals, purchase recency, and sales references. They do not include operational visibility or operational AST ownership.

- **Example:** Stage 08 owns `totalAmountC` but does not own `master.visibility`.

- **Related terms:** Field Ownership, Sales All Meters, Operational Visibility Ownership

### Term: Visibility

- **Acronym:** None

- **Simple meaning:** An operational status controlled by approved operational meter workflows, not by sales matching.

- **Detailed explanation:** Visibility describes whether the meter is operationally exposed or available according to approved iREPS operational rules. Sales history, Meter Master presence, customer references, and blank or populated pipeline AST fields do not by themselves determine visibility. The Sales Pipeline must not create, derive, default, merge, overwrite, or clear `master.visibility`.

- **Example:** A meter can be `IN SALES` while its operational visibility is still governed separately by Meter Discovery or Meter Installation.

- **Related terms:** VISIBLE, INVISIBLE, Operational Visibility Ownership, Sales Match

### Term: VISIBLE

- **Acronym:** None

- **Simple meaning:** The approved operational visibility value showing that a meter is visible under iREPS operational rules.

- **Detailed explanation:** `VISIBLE` is written only by an approved operational meter-registration, Meter Discovery, or Meter Installation writer according to the operational contract. It does not mean merely that sales data exists.

- **Example:** An approved Meter Discovery backend writer may establish `VISIBLE` after completing its governed operational checks.

- **Related terms:** Visibility, INVISIBLE, Operational Visibility Ownership, Meter Discovery

### Term: INVISIBLE

- **Acronym:** None

- **Simple meaning:** The approved operational visibility value showing that a meter is not visible under iREPS operational rules.

- **Detailed explanation:** `INVISIBLE` is an operational value and must not be inferred from no sales, a blank AST link, an absent customer number, or any other Sales Pipeline field. Only an approved operational writer may set it.

- **Example:** A meter with no Conlog purchases is not automatically INVISIBLE.

- **Related terms:** Visibility, VISIBLE, Operational Visibility Ownership, NO SALES MATCH

### Term: Operational Visibility Ownership

- **Acronym:** None

- **Simple meaning:** The rule that only approved operational meter writers control `master.visibility`.

- **Detailed explanation:** Operational meter-registration, Meter Discovery, and Meter Installation writers own visibility. Stage 06 must not output a visibility column. Stage 08 must not create, upload, overwrite, default, merge, or clear `master.visibility`. Existing approved operational visibility is outside Stage 08 ownership and must be preserved during controlled recovery.

- **Example:** Stage 08 validates sales totals but ignores and preserves an existing operational `master.visibility` value.

- **Related terms:** Visibility, Field Ownership, Stage 06, Stage 08

### Term: Backend Check

- **Acronym:** None

- **Simple meaning:** A server-side validation that confirms governed data before saving or acting.

- **Detailed explanation:** A Backend Check normalizes the meter number, checks approved data sources, applies business rules, and confirms the result independently of a form-side hint. Sales matching and operational visibility remain separate backend responsibilities.

- **Example:** The backend rechecks whether a scanned meter is `IN SALES` before the transaction is saved.

- **Related terms:** Form-side Check, Sales Match, Validation, Operational Visibility Ownership

### Term: Form-side Check

- **Acronym:** None

- **Simple meaning:** A helpful early lookup or message shown on the user form.

- **Detailed explanation:** A Form-side Check can show a soft sales-awareness result while the user types or scans. It is not the final authority for saving canonical data or setting operational visibility.

- **Example:** A badge below the meter field shows `IN SALES`, but the backend verifies again on submission.

- **Related terms:** Backend Check, FormInputMeterNo, IN SALES, UI Badge

### Term: FormInputMeterNo

- **Acronym:** None

- **Simple meaning:** The iREPS form component used to type or scan a meter number.

- **Detailed explanation:** FormInputMeterNo may normalize input, help detect local duplicates, and request a controlled sales lookup. It must not invent canonical linkage or operational visibility.

- **Example:** A fieldworker scans a meter number and the component displays a soft `IN SALES` result.

- **Related terms:** Meter Number, Normalized Meter Number, Form-side Check, Backend Check

### Term: Customer Details

- **Acronym:** None

- **Simple meaning:** The approved reference file containing customer, account, meter, status, and purchase information used by Meter Master.

- **Detailed explanation:** Customer Details can populate or improve Meter Master customer and account references. Duplicate resolution may use only the governed identity, account-status, and latest-purchase fields. Customer name, ERF, and address are not Meter Master duplicate-resolution inputs.

- **Example:** A stronger active customer/account row may replace a weak placeholder identity under the approved duplicate rules.

- **Related terms:** Reference Data, Meter Master, Duplicate Resolution, Customer Number

### Term: 90 Days No Purchase Report

- **Acronym:** NPR

- **Simple meaning:** An approved reference report containing meters with no recent purchase activity.

- **Detailed explanation:** The report can add meter identities missing from other sources and may provide a customer number under governed precedence rules. It is reference input for Meter Master, not proof of operational invisibility.

- **Example:** An NPR-only meter is added to Meter Master even though it has no monthly purchase in the selected range.

- **Related terms:** Reference Data, Meter Master, Days Since Last Purchase, NO SALES MATCH

### Term: Reference Data

- **Acronym:** None

- **Simple meaning:** Approved supporting data used to enrich or reconcile the sales pipeline.

- **Detailed explanation:** Reference Data is not a replacement for Atomic Sales. It supports identity and customer/account linking under explicit precedence and duplicate-resolution rules.

- **Example:** Customer Details and the 90 Days No Purchase Report are current Meter Master reference inputs.

- **Related terms:** Customer Details, 90 Days No Purchase Report, Meter Master

### Term: Duplicate Resolution

- **Acronym:** None

- **Simple meaning:** The governed process for choosing one supported record when source files contain competing rows for the same identity.

- **Detailed explanation:** Duplicate Resolution must use only approved decision fields and precedence rules. Unresolved ties or unsupported conflicts stop the build. The pipeline must report how many duplicates were resolved by each approved rule.

- **Example:** A normal customer/account identity may replace a weak row where customer number, account number, and meter number are all the same placeholder.

- **Related terms:** Customer Details, Reference Data, Validation, Conflict

### Term: Conflict

- **Acronym:** None

- **Simple meaning:** Two or more values disagree in a way the approved rules cannot safely resolve.

- **Detailed explanation:** A Conflict must stop the affected build or upload. It must not be hidden by merge, overwrite, default values, or skipped rows.

- **Example:** Two different customer identities with tied latest-purchase dates create an unresolved conflict.

- **Related terms:** Duplicate Resolution, Validation, Controlled Resume

### Term: Integer Cents

- **Acronym:** C

- **Simple meaning:** Money stored as whole cents instead of decimal rand values.

- **Detailed explanation:** From Atomic Sales onward, approved fields ending in `C` contain integer cents. Stage 01 is the single controlled conversion boundary for current Conlog RAW STAGING decimal rand values. Downstream stages must not convert those cents again.

- **Example:** R100.00 is stored as `10000`.

- **Related terms:** Monetary Conversion Boundary, amountTotalC, totalAmountC, VAT

### Term: Monetary Conversion Boundary

- **Acronym:** None

- **Simple meaning:** The one approved point where current Conlog decimal rand values become integer cents.

- **Detailed explanation:** Stage 01 performs this conversion exactly once. RAW STAGING retains the approved provider decimal representation; Atomic and downstream layers use integer cents.

- **Example:** `86.96` becomes `8696` at Stage 01.

- **Related terms:** Stage 01, RAW STAGING, Integer Cents

### Term: amountTotalC

- **Acronym:** None

- **Simple meaning:** A governed total sales amount expressed in integer cents at Atomic and Monthly layers.

- **Detailed explanation:** `amountTotalC` must reconcile with cost and VAT according to the applicable schema and layer. It must never mix rand and cents inside the same governed layer.

- **Example:** `amountTotalC = costC + vatC`.

- **Related terms:** Integer Cents, costC, vatC, Monthly Reconciliation

### Term: totalAmountC

- **Acronym:** None

- **Simple meaning:** The total approved sales amount for one Sales All Meters document across the included month range.

- **Detailed explanation:** `totalAmountC` is expressed in integer cents and must equal the sum of all included monthly sales amounts for that meter.

- **Example:** If monthly totals are 10,000 and 15,000 cents, `totalAmountC` is 25,000 cents.

- **Related terms:** Sales All Meters, monthlyTotalsC, Integer Cents, Reconciliation

### Term: monthlyTotalsC

- **Acronym:** None

- **Simple meaning:** The map of one meter’s approved sales total for each included month, expressed in integer cents.

- **Detailed explanation:** The month keys are dynamic and follow `YYYY-MM`. Every included month must be present according to the approved range, including zero where the meter had no sales.

- **Example:** `"2026-06": 20000` means R200.00 in approved June sales.

- **Related terms:** Sales All Meters, totalAmountC, Continuous Month Range

### Term: Last Purchase Date

- **Acronym:** None

- **Simple meaning:** The latest valid approved purchase date for a meter within the governed source scope.

- **Detailed explanation:** Last Purchase Date supports duplicate resolution and Sales All Meters recency. It must come from approved source data and must reconcile with the selected month range.

- **Example:** If the latest valid purchase is 27 June 2026, that date becomes the meter’s last purchase date for the build.

- **Related terms:** lastPurchaseAtISO, Days Since Last Purchase, Duplicate Resolution

### Term: lastPurchaseAtISO

- **Acronym:** None

- **Simple meaning:** The Sales All Meters field containing the latest valid purchase timestamp in ISO format.

- **Detailed explanation:** A meter with no sales in the approved range uses the schema-approved no-sales value. The field must remain consistent with `daysSinceLastPurchase`.

- **Example:** `2026-06-27T10:35:00Z`.

- **Related terms:** Last Purchase Date, Days Since Last Purchase, Sales All Meters

### Term: Days Since Last Purchase

- **Acronym:** None

- **Simple meaning:** The number of days between the approved as-of date and the latest valid purchase date.

- **Detailed explanation:** The value must be calculated from an explicit build as-of date so the same frozen inputs produce the same result. A meter with no sales uses the schema-approved no-sales value.

- **Example:** An as-of date 17 days after the last purchase produces `daysSinceLastPurchase = 17`.

- **Related terms:** As-of Date, lastPurchaseAtISO, 90 Days No Purchase Report

### Term: As-of Date

- **Acronym:** None

- **Simple meaning:** The explicit date used as the reference point for reproducible recency calculations.

- **Detailed explanation:** Stage 06 must receive an explicit As-of Date and must not silently use the current machine date. This keeps `daysSinceLastPurchase` repeatable across rebuilds.

- **Example:** Rebuilding the same CSV with `--as-of-date 2026-07-14` produces the same recency values.

- **Related terms:** Days Since Last Purchase, Reproducible Build, Stage 06

### Term: Build Manifest

- **Acronym:** Manifest

- **Simple meaning:** A governed JSON record proving exactly what a pipeline build used and produced.

- **Detailed explanation:** A Build Manifest records status, result, scope, input files, output files, schemas, row counts, SHA-256 values, reconciliation results, and fingerprints. An uploader must consume the exact successful manifest, not merely discover a CSV in an output folder.

- **Example:** Stage 04 reads the successful Stage 03 manifest to select the exact three monthly CSVs.

- **Related terms:** SHA-256, Build Fingerprint, Frozen CSV, Upload Contract

### Term: SHA-256

- **Acronym:** SHA-256

- **Simple meaning:** A digital fingerprint used to prove that a file has not changed.

- **Detailed explanation:** Even a small file change produces a different SHA-256 value. The Sales Pipeline records and checks SHA-256 values for source, staging, build, manifest, and upload safety.

- **Example:** Stage 08 stops when the supplied CSV SHA-256 differs from the value in the Stage 06 manifest.

- **Related terms:** Build Manifest, Frozen CSV, File Integrity, Build Fingerprint

### Term: Build Fingerprint

- **Acronym:** None

- **Simple meaning:** A deterministic identity for one exact governed build contract.

- **Detailed explanation:** A Build Fingerprint combines the important scope, input, output, schema, range, and integrity facts needed to prove that the same build is being used. It protects controlled resume from changed or expanded inputs.

- **Example:** A different month range produces a different build fingerprint.

- **Related terms:** Build Manifest, Upload Contract, Controlled Resume, SHA-256

### Term: Frozen CSV

- **Acronym:** None

- **Simple meaning:** An approved pipeline output that must not be edited before upload.

- **Detailed explanation:** A Frozen CSV has passed validation and is tied to a successful manifest and fingerprint. The same approved file may be uploaded to explicitly approved projects when the cross-project contract allows it.

- **Example:** The Meter Master CSV approved in TEST must not be manually changed before an approved Trials upload.

- **Related terms:** Build Manifest, SHA-256, Create-only, Upload Contract

### Term: Reproducible Build

- **Acronym:** None

- **Simple meaning:** A build that produces the same governed result from the same approved inputs and parameters.

- **Detailed explanation:** Reproducibility depends on explicit scope, frozen inputs, deterministic IDs, stable monetary rules, explicit as-of dates, and recorded fingerprints.

- **Example:** Running Stage 06 with the same monthly files, Meter Master, manifest, range, and as-of date produces the same output fingerprint.

- **Related terms:** As-of Date, Deterministic Document ID, Build Fingerprint

### Term: Preflight Validation

- **Acronym:** Preflight

- **Simple meaning:** All safety checks completed before a pipeline write or upload begins.

- **Detailed explanation:** Preflight validates scope, schema, identities, provider, totals, files, fingerprints, project selection, target state, and ownership rules. A failed preflight must write no governed output or Firestore data.

- **Example:** Stage 08 rejects a CSV with a visibility column before connecting to Firestore.

- **Related terms:** Validation, Create-only, Upload Contract, Explicit Project Selection

### Term: Validation

- **Acronym:** None

- **Simple meaning:** Checking that data and execution conditions comply with the approved rules.

- **Detailed explanation:** Validation includes file presence, schema, row count, identities, dates, provider, monetary values, duplicates, continuous months, target environment, and ownership. Critical validation failures stop the process loudly.

- **Example:** A missing required month stops a full-period build.

- **Related terms:** Preflight Validation, Reconciliation, Conflict, Rejected Row

### Term: Reconciliation

- **Acronym:** None

- **Simple meaning:** Proving that related inputs and outputs agree.

- **Detailed explanation:** Reconciliation compares counts, totals, identities, dates, and linked layers. No upload is complete until the applicable reconciliation checks pass.

- **Example:** `totalAmountC` equals the sum of all `monthlyTotalsC` values.

- **Related terms:** Monthly Reconciliation, Validation, Upload Verification

### Term: Rejected Row

- **Acronym:** None

- **Simple meaning:** A source row that fails a required validation rule.

- **Detailed explanation:** Rejected rows must be reported clearly. Stage 00 writes no RAW STAGING output when rejected rows exist, preventing partial unsafe data from progressing.

- **Example:** A transaction outside the requested month is written to the rejected-row report and blocks the monthly staging output.

- **Related terms:** Stage 00, Validation, Audit Report

### Term: Create-only

- **Acronym:** None

- **Simple meaning:** The normal upload mode that creates new documents only in an approved empty target scope.

- **Detailed explanation:** Create-only prevents silent overwrite, merge, update, and stale-field preservation. Existing documents in a scope that should be empty block the normal upload.

- **Example:** Stage 04 uses Firestore create operations for all three monthly collections.

- **Related terms:** Controlled Resume, Firestore Create, Upload Safety

### Term: Controlled Resume

- **Acronym:** Resume

- **Simple meaning:** A restricted recovery mode for finishing the exact same verified partial upload.

- **Detailed explanation:** Controlled Resume is not a general update, refresh, migration, enrichment, or changed-file mode. It requires the same project, failed report, manifest, fingerprint, CSV, document-ID set, range, provider, and totals. Exact existing expected documents may be skipped; conflicts and unexpected documents stop recovery.

- **Example:** A failed Stage 08 run may resume only with its original untampered report and unchanged frozen CSV.

- **Related terms:** Create-only, Upload Contract, Frozen CSV, Conflict

### Term: Upload Contract

- **Acronym:** None

- **Simple meaning:** The complete set of approved facts that define one exact upload.

- **Detailed explanation:** The contract includes project, service account, collection, mode, source CSV, manifest, fingerprints, schema, row count, planned IDs, LM, month range, provider, totals, and ownership rules.

- **Example:** Changing the CSV after a partial upload changes the contract and blocks resume.

- **Related terms:** Build Manifest, Build Fingerprint, Controlled Resume, Explicit Project Selection

### Term: Upload Audit Report

- **Acronym:** None

- **Simple meaning:** A JSON record of what an uploader checked, attempted, created, skipped, verified, or rejected.

- **Detailed explanation:** Every governed preflight and execution attempt must produce an audit report. The report supports recovery, investigation, and proof of the exact upload contract.

- **Example:** A failed Stage 08 report is required before a controlled resume attempt.

- **Related terms:** Controlled Resume, Upload Contract, Audit Trail, Upload Verification

### Term: Upload Verification

- **Acronym:** None

- **Simple meaning:** Confirming after upload that Firestore contains the exact expected governed result.

- **Detailed explanation:** Verification includes final counts and deterministic document samples with exact shapes, field values, and data types. An upload is not complete merely because write batches finished.

- **Example:** The uploader checks the final collection count and selected deterministic sample documents before reporting PASS.

- **Related terms:** Reconciliation, Audit Report, Deterministic Document ID

### Term: Source Traceability

- **Acronym:** None

- **Simple meaning:** The ability to trace a generated record back through every approved source and pipeline layer.

- **Detailed explanation:** Traceability uses source filenames, row references, transaction identities, manifests, SHA-256 values, logs, and reports so a result can be explained and reproduced.

- **Example:** A monthly total can be traced back to the Atomic transactions and original provider file.

- **Related terms:** Source Evidence, Build Manifest, SHA-256, Audit Trail

### Term: Environment-neutral Build

- **Acronym:** None

- **Simple meaning:** A local builder that does not silently choose or connect to a Firebase project.

- **Detailed explanation:** Build stages create and validate local outputs independently of DEV, TEST, Trials, or Production. Environment selection belongs only to an uploader and must be explicit.

- **Example:** Stage 06 builds Sales All Meters without connecting to Firebase.

- **Related terms:** Explicit Project Selection, Build Stage, Firebase Environment

### Term: Explicit Project Selection

- **Acronym:** None

- **Simple meaning:** Naming and confirming the exact Firebase project before an upload.

- **Detailed explanation:** Uploaders require an explicit project ID, matching confirmation, and a service account whose project ID matches the target. Production must never be selected by default.

- **Example:** `--project-id ireps-test` and `--confirm-project ireps-test` must agree.

- **Related terms:** Environment-neutral Build, Upload Contract, Preflight Validation

### Term: Sales Pipeline System Actor

- **Acronym:** None

- **Simple meaning:** The approved audit identity used when the Meter Master Pipeline creates or updates Meter Master data.

- **Detailed explanation:** The approved actor is UID `SYSTEM` and user name `METER MASTER PIPELINE`. It identifies a governed system write and does not represent a human user.

- **Example:** A Sales-created Meter Master document records `createdByUid = SYSTEM` and `createdByUser = METER MASTER PIPELINE`.

- **Related terms:** Meter Master, Metadata, Audit Trail, Stage 07

### Term: Provider-neutral Architecture

- **Acronym:** None

- **Simple meaning:** A future design that can support multiple sales providers through generic collections and explicit provider identity.

- **Detailed explanation:** The current TEST architecture keeps the Conlog collection names. A provider-neutral redesign is deferred to a separate controlled architecture and migration sprint and must not be introduced silently into the current pipeline.

- **Example:** Future support for Conlog and Landis+Gyr may use a provider-neutral sales architecture after formal approval.

- **Related terms:** Sales Provider, Conlog Sales Collection Family, Migration

## 6. MREAD and Reporting Concepts

### Term: MREAD

- **Acronym:** MREAD

- **Simple meaning:** Meter Reading.

- **Detailed explanation:** MREAD is the iREPS meter reading process and related module. It captures reading attempts, outcomes, evidence, reasons, and meter information. Completed MREAD transactions can feed into registry_mread, which then supports reporting and staging.

- **Example:** A fieldworker completes an MREAD task for a ward and submits a successful reading.

- **Related terms:** Meter Reading, Registry MREAD, MREAD Staging, Transaction (TRN), Outcome

### Term: Registry

- **Acronym:** None

- **Simple meaning:** A structured record collection used for reporting or reference.

- **Detailed explanation:** A registry is a collection of standardised records that iREPS can use for visibility, reporting, review, and analytics. Registry data should be structured and consistent so that pages and reports can read it easily.

- **Example:** registry_mread stores raw meter reading records for reporting and analytics.

- **Related terms:** Registry MREAD, MREAD, Reporting, Staging

### Term: MREAD Registry

- **Acronym:** registry_mread

- **Simple meaning:** The raw meter reading registry in iREPS.

- **Detailed explanation:** MREAD Registry, also called Registry MREAD in older wording, stores completed MREAD records for reporting and analytics. It is the raw reporting layer for meter reading attempts and outcomes. It receives canonical outcomes directly from completed MREAD transactions and makes them available for registry-style views and later staging processes. It keeps one registry record per meter reading attempt or completed reading event, depending on the locked registry rule for that flow.

- **Example:** A completed MREAD transaction with outcome Successful Reading can create or update a registry_mread record showing the reading value, date, outcome, fieldworker, and evidence.

- **Related terms:** MREAD, MREAD Staging, Transaction (TRN), Successful Reading, No Access, Registry MREAD

### Term: MREAD Staging

- **Acronym:** None

- **Simple meaning:** A preserved review snapshot of meter reading data for a selected cycle.

- **Detailed explanation:** MREAD Staging is not a billing engine. It creates a preserved snapshot of meter reading data for inspection, review, and downstream use. It pulls from registry_mread using selected cycles and keeps each staging run as a historical session. In the current iREPS direction, staging uses selected-cycle generation rather than DRAFT, OPEN, or CLOSED workflow meanings.

- **Example:** A user selects Cycle 10 and generates an MREAD Staging session showing current readings, previous readings, consumption, no access rows, and evidence counts.

- **Related terms:** Registry MREAD, MREAD, Staging Cycle, Reading History, Consumption

### Term: Staging

- **Acronym:** None

- **Simple meaning:** A prepared snapshot of data for review or downstream processing.

- **Detailed explanation:** In iREPS, staging means preparing data into a structured view or session without treating it as final billing approval. Staging preserves what was generated at a point in time so users can inspect the data and understand what was available.

- **Example:** MREAD Staging creates a snapshot of meter readings for a selected cycle.

- **Related terms:** MREAD Staging, Registry, Cycle, Review

### Term: Cycle

- **Acronym:** None

- **Simple meaning:** A defined meter reading or staging period.

- **Detailed explanation:** A cycle is a configured period used to group meter reading or staging activity. In iREPS, cycles can be selected for staging so users can generate a preserved view for that period.

- **Example:** Cycle 9, Cycle 10, and Cycle 11 can each have separate staging sessions.

- **Related terms:** MREAD Staging, Staging Cycle, Reading History, Selected Cycle

### Term: Selected Cycle

- **Acronym:** None

- **Simple meaning:** The cycle chosen by the user for staging or review.

- **Detailed explanation:** Selected Cycle is the cycle the user chooses from configured cycle data. iREPS uses that selected cycle to generate the relevant staging snapshot. This avoids relying on DRAFT, OPEN, or CLOSED workflow status labels for staging decisions.

- **Example:** A user selects Cycle 10 and generates staging for Cycle 10 only.

- **Related terms:** Cycle, MREAD Staging, Staging Session

### Term: Staging Session

- **Acronym:** None

- **Simple meaning:** One preserved generated staging run.

- **Detailed explanation:** A staging session records the output of a staging generation at a specific point in time. Each run is preserved, so users can inspect or compare generated rows later.

- **Example:** A generated session may have 22 rows, a generation timestamp, and linked staging rows.

- **Related terms:** MREAD Staging, Selected Cycle, Staging Rows

## 7. User Role and Governance Concepts

### Term: Fieldworker

- **Acronym:** FWR

- **Simple meaning:** A user who performs work in the field.

- **Detailed explanation:** A Fieldworker executes operational tasks such as meter reading, meter discovery, inspections, disconnections, reconnections, removals, and evidence capture. Fieldworkers are central to iREPS Mobile because they collect field truth. FWR is the iREPS role acronym for Fieldworker.

- **Example:** A Fieldworker uses the mobile app to capture a discovered meter, take photos, and submit the transaction.

- **Related terms:** FWR, Transaction (TRN), Mobile App, Supervisor

### Term: Supervisor

- **Acronym:** SPV

- **Simple meaning:** A user who supervises field operations.

- **Detailed explanation:** A Supervisor manages or oversees fieldworkers, assigned work, acceptance, execution progress, and operational results. In iREPS, supervisors may belong to a main contractor or subcontractor context depending on the governance model. SPV is the iREPS acronym for Supervisor.

- **Example:** A Supervisor allocates meter discovery work to Fieldworkers and monitors completion.

- **Related terms:** SPV, Fieldworker, FWR, Main Contractor, Subcontractor, BGO

### Term: Manager

- **Acronym:** MNG

- **Simple meaning:** A management user in iREPS.

- **Detailed explanation:** A Manager has visibility over operations, reports, teams, and municipal or contractor performance depending on scope and permissions. MNG is the iREPS acronym for Manager.

- **Example:** A municipal Manager views registry pages, staging summaries, and operational progress.

- **Related terms:** MNG, Supervisor, Governance, LM

### Term: Superuser

- **Acronym:** SPU

- **Simple meaning:** A high-level setup or administration user in iREPS.

- **Detailed explanation:** A Superuser is used for controlled setup, administration, bootstrap, or high-level configuration tasks. It is not a normal fieldworker role. SPU is the iREPS acronym for Superuser.

- **Example:** A Superuser may be created during TEST environment bootstrap with elevated setup permissions.

- **Related terms:** SPU, Admin, Setup, Test Environment, User Role

### Term: Main Contractor

- **Acronym:** MNC

- **Simple meaning:** The main contractor governance layer in iREPS.

- **Detailed explanation:** Main Contractor refers to the contractor layer that may supervise or coordinate subcontractors and field operations under a municipal arrangement. MNC is the iREPS acronym for Main Contractor.

- **Example:** A Main Contractor Supervisor may monitor subcontractor teams executing work in a municipality.

- **Related terms:** MNC, Subcontractor, Supervisor, Governance

### Term: Subcontractor

- **Acronym:** SUBC

- **Simple meaning:** The subcontractor governance layer in iREPS.

- **Detailed explanation:** Subcontractor refers to a service-provider layer that may provide field teams, supervisors, and fieldworkers to execute operational work. SUBC is the iREPS acronym for Subcontractor.

- **Example:** A Subcontractor team may be assigned meter reading work in a specific ward.

- **Related terms:** SUBC, Main Contractor, Supervisor, Fieldworker

## 8. Interface, Evidence, and System Concepts

### Term: Warehouse

- **Acronym:** None

- **Simple meaning:** The local working data context used by the app.

- **Detailed explanation:** Warehouse is the app-side working store or context that gives screens access to operational data. It should not be overloaded with large sales datasets or heavy backend-only collections. Warehouse should support field and UI needs without becoming a duplicate of all backend data.

- **Example:** The mobile app may use Warehouse to access premises and meters needed for fieldwork, but not to preload all sales meters.

- **Related terms:** Mobile App, Sales Data, Meter Master, Operational Data

### Term: Mobile App

- **Acronym:** None

- **Simple meaning:** The iREPS app used by field users on mobile devices.

- **Detailed explanation:** The iREPS Mobile App supports field execution, capture, evidence collection, GPS, meter reading, discovery, inspections, and other operational workflows. It should guide fieldworkers through simple screens while preserving correct backend data rules.

- **Example:** A Fieldworker uses iREPS Mobile to scan a meter number and capture a photo of the meter.

- **Related terms:** Fieldworker, FWR, Transaction (TRN), Evidence, FormInputMeterNo

### Term: Web App

- **Acronym:** None

- **Simple meaning:** The iREPS web interface used for management, registries, setup, and review.

- **Detailed explanation:** The Web App supports office and management workflows such as registry viewing, staging review, reporting, configuration, and administrative functions. It complements the mobile app by giving managers and supervisors broader visibility.

- **Example:** A Manager opens the MREAD Registry page on iREPS Web to view meter reading outcomes.

- **Related terms:** Registry, MREAD Staging, Manager, Supervisor

### Term: Evidence

- **Acronym:** None

- **Simple meaning:** Proof captured during fieldwork.

- **Detailed explanation:** Evidence can include photos, GPS points, timestamps, notes, readings, user identity, signatures, or other supporting material. iREPS uses evidence to strengthen auditability and trust in operational outcomes.

- **Example:** A meter reading may include a photo of the meter face as evidence.

- **Related terms:** Media, Transaction (TRN), Fieldworker, Audit Trail

### Term: Media

- **Acronym:** None

- **Simple meaning:** Photos or other captured files attached to work.

- **Detailed explanation:** Media is part of field evidence. It helps prove that work was done and supports later review, disputes, quality checks, and reporting.

- **Example:** A meter discovery record may include a photo of the meter, the premise, and the meter number.

- **Related terms:** Evidence, Photo, Transaction (TRN), Inspection

### Term: Audit Trail

- **Acronym:** None

- **Simple meaning:** A record showing what happened, when, and by whom.

- **Detailed explanation:** Audit Trail helps iREPS preserve accountability. It can include created dates, updated dates, user IDs, roles, status changes, outcomes, and evidence. Audit trails support investigation, governance, and trust.

- **Example:** A removal transaction may show who removed the meter, when it was removed, what evidence was captured, and what status changed.

- **Related terms:** Transaction (TRN), Evidence, Operational History, Governance

### Term: Status

- **Acronym:** None

- **Simple meaning:** The current condition or workflow position of a record.

- **Detailed explanation:** Status tells users where a record or task currently stands. It can apply to transactions, assets, meters, sessions, and operational processes. Status must be used carefully so it does not create false business meaning.

- **Example:** A meter may have an operational status such as connected, disconnected, removed, or active depending on the workflow.

- **Related terms:** Operational Status, Outcome, Transaction (TRN), Meter Lifetime

### Term: Operational Status

- **Acronym:** None

- **Simple meaning:** The current operational condition of a meter or asset.

- **Detailed explanation:** Operational Status describes whether a meter is active, disconnected, reconnected, removed, or otherwise affected by operations. It is updated by lifecycle events such as disconnection, reconnection, and removal.

- **Example:** After a successful disconnection transaction, the meter’s operational status may show disconnected.

- **Related terms:** Status, Meter Disconnection, Meter Reconnection, Meter Removal

### Term: Anomaly

- **Acronym:** None

- **Simple meaning:** Something unusual or incorrect found during work.

- **Detailed explanation:** An anomaly is a condition that does not match expected data, rules, or field reality. In meter operations, anomalies may include tampering, broken seals, mismatched meter numbers, damaged meters, unexpected readings, suspicious wiring, or location issues.

- **Example:** A fieldworker discovers that the meter number on the device does not match the meter number in iREPS.

- **Related terms:** Inspection, Normalisation, Evidence, Data Quality

### Term: Normalisation

- **Acronym:** None

- **Simple meaning:** Correcting or standardising data so it can be used reliably.

- **Detailed explanation:** Normalisation can refer to fixing inconsistent records, cleaning values, or applying standard rules so data becomes consistent. In inspection or discovery work, normalisation may follow findings or anomalies.

- **Example:** If a meter number is captured with spaces in one place and no spaces in another, normalisation can standardise it for matching.

- **Related terms:** Normalized Meter Number, Anomaly, Data Quality, Meter Master

### Term: Data Quality

- **Acronym:** None

- **Simple meaning:** How accurate, complete, and reliable iREPS data is.

- **Detailed explanation:** Data quality is important because iREPS decisions depend on field records, meter identity, location, readings, and statuses. Poor data quality can lead to wrong reports, wrong assignments, wrong meter links, or incorrect operational decisions.

- **Example:** A meter with no premise link, wrong ward, or incorrect meter number has data quality problems.

- **Related terms:** Normalisation, Anomaly, Audit Trail, Registry

## 9. Diagram and Documentation Concepts

### Term: Diagram

- **Acronym:** None

- **Simple meaning:** A visual explanation of a process or system.

- **Detailed explanation:** In iREPS, diagrams help explain complex workflows in a simple visual way. A good diagram should show both the field process and the system data effect without overwhelming the reader with backend details.

- **Example:** The Meter Lifetime Diagram shows how a meter moves from not captured, to registered, to operational, to removed.

- **Related terms:** Data Flow, State Ribbon, Process Flow, User Manual

### Term: Meter Lifetime Diagram

- **Acronym:** None

- **Simple meaning:** A one-page diagram showing the life of a meter in iREPS.

- **Detailed explanation:** The Meter Lifetime Diagram explains how a meter enters iREPS, becomes operational, accumulates events, and eventually exits active operations. It distinguishes Meter Installation from Meter Discovery and shows that commissioning applies only to newly installed meters.

- **Example:** The diagram can be used in the Getting Started Guide, Test Pack, user manuals, presentations, marketing, and training videos.

- **Related terms:** Meter Lifetime, Data Flow, State Ribbon, Operational Life

### Term: State Ribbon

- **Acronym:** None

- **Simple meaning:** A simple visual row showing the main states of a process.

- **Detailed explanation:** A state ribbon makes it easy to see how a record moves through high-level states. For the meter lifetime, the corrected ribbon is: Not Captured → Registered in iREPS → Operational Meter → Operational History Accumulates → Removed.

- **Example:** The Meter Lifetime Diagram uses a state ribbon to show the major meter lifecycle states.

- **Related terms:** Diagram, Meter Lifetime, Operational Meter, Removed

### Term: Process Flow

- **Acronym:** None

- **Simple meaning:** The step-by-step movement through a workflow.

- **Detailed explanation:** A process flow shows what happens first, next, and last. In iREPS diagrams, process flow should be simple enough for users but accurate enough for technical and design discussions.

- **Example:** Not Captured → Meter Installation or Discovery → Registered in iREPS → Operational Life → Removal.

- **Related terms:** Diagram, Data Flow, Workflow, Lifecycle

### Term: Legend

- **Acronym:** None

- **Simple meaning:** A small explanation of symbols used in a diagram.

- **Detailed explanation:** A legend helps readers understand arrows, loops, icons, colours, and special markers in a diagram. In the Meter Lifetime Diagram, the legend explains normal arrows, repeat indicators, vending, and removal.

- **Example:** A dashed loop icon means the event can happen many times during operational life.

- **Related terms:** Diagram, State Ribbon, Process Flow

### Term: Repeatable Event

- **Acronym:** None

- **Simple meaning:** An event that can happen more than once.

- **Detailed explanation:** In iREPS meter lifetime, repeatable events are operational actions that may occur many times while the meter is active. These include Meter Reading, Disconnection, Reconnection, Inspection, and Vending-linked activity.

- **Example:** A meter can be read every month and inspected more than once during its life.

- **Related terms:** Operational Life, Meter Reading, Inspection, Vending

### Term: Exit Event

- **Acronym:** None

- **Simple meaning:** An event that closes or ends an active lifecycle.

- **Detailed explanation:** An exit event is not just another repeatable operational event. It moves the meter out of active operations. In the meter lifetime, Meter Removal is the exit event.

- **Example:** Removing a meter ends its active operational life, although its history remains in iREPS.

- **Related terms:** Meter Removal, Removed, Operational Life, Lifecycle

## 10. Environment and Testing Concepts

### Term: Test Pack

- **Acronym:** None

- **Simple meaning:** A packaged version of iREPS prepared for testing.

- **Detailed explanation:** A Test Pack is a controlled build or release used for testing features, fixes, workflows, and user feedback. It can include mobile APK builds, web updates, test users, seed data, and known test scenarios.

- **Example:** iREPS Test Pack v1 may include a mobile APK, web changes, test users, and selected workflows for field testing.

- **Related terms:** APK, Test Environment, Bug Register, Trial

### Term: Test Environment

- **Acronym:** TEST

- **Simple meaning:** A separate environment used for testing iREPS safely.

- **Detailed explanation:** The test environment allows the team to validate workflows, users, data, builds, and bug fixes without affecting production or DEV work. In the current setup, TEST is represented by the Firebase project `ireps-test`. TEST should use controlled seed data, test users, copied lookup/reference data, and clean operational scenarios.

- **Example:** The `ireps-test` Firebase project can contain test users, KSD and Lesedi workbases, clean ERF data, copied lookup options, and controlled workflow scenarios for Zamo testing.

- **Related terms:** Test Pack, DEV, Trial, Production, Seed Data

### Term: DEV

- **Acronym:** DEV

- **Simple meaning:** The development environment.

- **Detailed explanation:** DEV is used for active development and early testing by the development team. In the current project, DEV is represented by the Firebase project `ireps2`. It is less stable than TEST and should not be treated as production or as the formal testing environment.

- **Example:** Developers may test new code against `ireps2` before building a TEST APK or running iREPS Web against `ireps-test`.

- **Related terms:** TEST, Production, CI/CD, Build

### Term: APK

- **Acronym:** APK

- **Simple meaning:** Android app package file.

- **Detailed explanation:** APK is the Android package format used to install the iREPS mobile app on Android devices for testing or distribution outside the Play Store.

- **Example:** Testers may install the iREPS Test APK to test new mobile features.

- **Related terms:** Mobile App, Test Pack, EAS Build, Android

### Term: Bug Register

- **Acronym:** None

- **Simple meaning:** A structured list of bugs and their status.

- **Detailed explanation:** The bug register records each bug with details such as bug ID, build, environment, module, role, device, reproduction steps, expected result, actual result, severity, priority, owner, evidence, fix build, and retest result. It helps keep bug-fix work systematic and traceable.

- **Example:** A logout bug can be recorded with steps, expected result, actual result, fix commit, and retest outcome.

- **Related terms:** Test Pack, QA, Retest, Bug ID

## 11. Cadastral and Boundary Concepts

### Term: Cadastral

- **Acronym:** None

- **Simple meaning:** Land parcel and property boundary data.

- **Detailed explanation:** Cadastral data helps iREPS understand land parcels, ERFs, boundaries, and spatial relationships. It supports operational scope by linking premises and fieldwork to the correct municipal geography.

- **Example:** A cadastral import can load ERF records for a local municipality.

- **Related terms:** ERF, Boundary, Ward, LM, Geofence

### Term: Boundary

- **Acronym:** None

- **Simple meaning:** A mapped line or area defining a place.

- **Detailed explanation:** Boundaries define areas such as ERFs, wards, local municipalities, or districts. In iREPS, boundaries help assign records to the correct operational scope and detect cases where features straddle or overlap areas.

- **Example:** An ERF boundary may be used to determine which ward a premise belongs to.

- **Related terms:** ERF, Ward, LM, Geofence, Cadastral

### Term: Duplicate

- **Acronym:** None

- **Simple meaning:** A record that appears more than once when it should be unique.

- **Detailed explanation:** Duplicates are important in iREPS because duplicate meters, ERFs, premises, or IDs can cause incorrect links, wrong assignments, and bad reporting. The system needs predefined handling rules for duplicates during imports and operations.

- **Example:** Two ERF records with the same ERF ID may be flagged as duplicates during cadastral import QA.

- **Related terms:** QA, Cadastral, Data Quality, Overlap

### Term: Overlap

- **Acronym:** None

- **Simple meaning:** Two spatial features cover the same area when they should not.

- **Detailed explanation:** Overlap is a spatial data condition where boundaries or features intersect in a problematic way. In cadastral processing, overlaps need predefined handling so the pipeline can continue or stop according to locked rules.

- **Example:** Two ERF polygons overlap each other inside the same municipality.

- **Related terms:** Boundary, ERF, QA, Cadastral

### Term: Boundary Straddle

- **Acronym:** None

- **Simple meaning:** A feature crosses a ward or municipal boundary.

- **Detailed explanation:** Boundary straddle occurs when an ERF or feature falls across more than one ward or local municipality boundary. iREPS must handle this carefully because operational scope depends on correct ward and LM assignment.

- **Example:** An ERF polygon may partially fall in two wards, requiring a predefined assignment rule.

- **Related terms:** Boundary, Ward, LM, ERF, QA

## 12. TEST Environment, Build, and Demo Concepts

### Term: TEST

- **Acronym:** TEST

- **Simple meaning:** The controlled testing version of iREPS.

- **Detailed explanation:** TEST is the environment used after DEV but before trial or production. It is where selected users validate features, data, workflows, and bugs using controlled data. TEST must be separate from DEV so that active development does not disturb formal testing.

- **Example:** Zamo uses the iREPS Test APK and TEST Web connection to validate field workflows against the `ireps-test` backend.

- **Related terms:** Test Environment, iREPS Test APK, ireps-test, Test Pack, Bug Register

### Term: ireps-test

- **Acronym:** None

- **Simple meaning:** The Firebase project used for the iREPS TEST environment.

- **Detailed explanation:** `ireps-test` is the backend project used by the TEST mobile APK and TEST web configuration. It holds TEST users, TEST workbases, copied lookup/reference data, selected cadastral data, and test workflow records. It must remain separate from `ireps2`, which is the DEV Firebase project.

- **Example:** The iREPS Test APK should log that it is connecting APP_ENV="test" to project "ireps-test".

- **Related terms:** TEST, Firebase Project, DEV, ireps2, iREPS Test APK

### Term: ireps2

- **Acronym:** None

- **Simple meaning:** The Firebase project used as the current iREPS DEV backend.

- **Detailed explanation:** `ireps2` is the development backend where active work and early experiments happen. Reference data may be copied from `ireps2` into `ireps-test`, but TEST should not accidentally connect to DEV during formal testing.

- **Example:** The recursive lookup copy script read `irepsSelectLookups` from `ireps2` and wrote them into `ireps-test`.

- **Related terms:** DEV, ireps-test, Firebase Project, Test Environment

### Term: Firebase Project

- **Acronym:** None

- **Simple meaning:** A separate Firebase backend used by an iREPS environment.

- **Detailed explanation:** A Firebase project contains services such as Firestore, Authentication, Functions, Storage, Hosting, rules, and indexes. iREPS uses separate Firebase projects to separate DEV, TEST, trial, and future production data.

- **Example:** `ireps2` is the DEV Firebase project, while `ireps-test` is the TEST Firebase project.

- **Related terms:** Firestore, Firebase Auth, Firebase Functions, Firebase Hosting, TEST

### Term: iREPS Test APK

- **Acronym:** APK

- **Simple meaning:** The Android installation file for the TEST mobile app.

- **Detailed explanation:** The iREPS Test APK is the Android package built using the TEST build profile. It should use TEST environment variables so that the installed app connects to `ireps-test`. It is the mobile app package testers install before structured testing begins.

- **Example:** After changing Redux persistence for lookup options, a new iREPS Test APK had to be built because `store.js` is bundled into the installed app.

- **Related terms:** APK, EAS Build, Build Profile, TEST, APP_ENV

### Term: TEST Build Profile

- **Acronym:** None

- **Simple meaning:** The build configuration used to produce the TEST mobile app.

- **Detailed explanation:** A build profile defines how EAS Build should package the app. The TEST build profile sets the app environment to TEST through values such as `APP_ENV=test` and `EXPO_PUBLIC_APP_ENV=test`, and produces the iREPS Test APK.

- **Example:** Running `eas build --platform android --profile test` builds the Android TEST APK.

- **Related terms:** EAS Build, iREPS Test APK, APP_ENV, EXPO_PUBLIC_APP_ENV

### Term: EAS Build

- **Acronym:** EAS

- **Simple meaning:** Expo's cloud build service used to build the mobile app.

- **Detailed explanation:** EAS Build packages the Expo React Native app into installable Android or iOS builds. In iREPS, it is used to create APKs for TEST and later app-store builds for trial or production. EAS Build needs network access to Expo services.

- **Example:** The TEST APK build moved from versionCode 12 to 13 and uploaded the project archive to EAS Build.

- **Related terms:** APK, Build Profile, Expo, versionCode, iREPS Test APK

### Term: versionCode

- **Acronym:** None

- **Simple meaning:** The Android build number that increases with each APK build.

- **Detailed explanation:** `versionCode` is used by Android to identify a newer app build. When EAS increments the versionCode, the phone can install the newer APK over the previous one.

- **Example:** The TEST build incremented versionCode from 12 to 13 before uploading to EAS Build.

- **Related terms:** APK, Android, EAS Build, Build Profile

### Term: APP_ENV

- **Acronym:** None

- **Simple meaning:** A mobile environment setting that tells iREPS which backend to use.

- **Detailed explanation:** `APP_ENV` is an environment variable used by the mobile app build or local run to decide whether the app should behave as DEV, TEST, trial, or live. It helps prevent the app from accidentally connecting to the wrong Firebase project.

- **Example:** Setting `APP_ENV=test` makes the mobile app use TEST configuration when running or building correctly.

- **Related terms:** EXPO_PUBLIC_APP_ENV, TEST, Firebase Project, iREPS Test APK

### Term: EXPO_PUBLIC_APP_ENV

- **Acronym:** None

- **Simple meaning:** A public Expo environment setting that the mobile app can read.

- **Detailed explanation:** `EXPO_PUBLIC_APP_ENV` is a mobile environment variable exposed to the Expo app at runtime or build time. It works with `APP_ENV` to make the app connect to the correct Firebase project.

- **Example:** The TEST build profile sets `EXPO_PUBLIC_APP_ENV=test` so the mobile app knows it is a TEST build.

- **Related terms:** APP_ENV, Expo, EAS Build, TEST

### Term: VITE_APP_ENV

- **Acronym:** None

- **Simple meaning:** A web environment setting that tells iREPS Web which backend to use.

- **Detailed explanation:** `VITE_APP_ENV` is used by the Vite web app to select the correct environment configuration. In PowerShell, setting `$env:VITE_APP_ENV="test"` tells the local web server that iREPS Web should connect to the TEST backend.

- **Example:** Before running local TEST Web, the user sets `$env:VITE_APP_ENV="test"` and then starts Vite in test mode.

- **Related terms:** Vite Mode, iREPS Web, TEST, ireps-test

### Term: Vite Mode

- **Acronym:** None

- **Simple meaning:** The mode used by Vite when starting or building iREPS Web.

- **Detailed explanation:** Vite mode tells the web app which environment settings to load. Running `npx vite --mode test` starts the local web server in TEST mode. Running `npx vite build --mode test` builds the TEST web files for deployment.

- **Example:** For Zamo's TEST demo, iREPS Web can be run locally with `npx vite --mode test`.

- **Related terms:** VITE_APP_ENV, Local Web Server, Web Build, Firebase Hosting

### Term: Local Web Server

- **Acronym:** None

- **Simple meaning:** The web app running from the developer's machine.

- **Detailed explanation:** A local web server lets the developer open iREPS Web in a browser on the laptop without deploying it. It is useful for demos and debugging, but it does not publish the app online.

- **Example:** Running `npx vite --mode test` starts iREPS Web locally and can connect it to `ireps-test`.

- **Related terms:** iREPS Web, Vite Mode, Web Build, Firebase Hosting

### Term: Web Build

- **Acronym:** None

- **Simple meaning:** Prepared iREPS Web files ready for deployment.

- **Detailed explanation:** A web build packages the web application into static files that can be hosted. For TEST, the build must be made using TEST mode so that the deployed web app connects to `ireps-test`.

- **Example:** `npx vite build --mode test` prepares TEST web files before deploying hosting.

- **Related terms:** Vite Mode, Firebase Hosting, iREPS Web, TEST

### Term: Firebase Hosting

- **Acronym:** None

- **Simple meaning:** Firebase service used to publish iREPS Web online.

- **Detailed explanation:** Firebase Hosting serves the built iREPS Web files. Deploying only hosting updates the visible web app without changing Firestore rules, indexes, or cloud functions.

- **Example:** After a successful TEST web build, `firebase deploy --only hosting` publishes the web app to the selected Firebase project.

- **Related terms:** Web Build, iREPS Web, Firebase Project, TEST

### Term: PowerShell Environment Variable

- **Acronym:** None

- **Simple meaning:** A temporary setting given to commands in a PowerShell window.

- **Detailed explanation:** In the iREPS workflow, PowerShell environment variables are used to tell tools which environment to use. The setting applies only to the current PowerShell session unless configured permanently.

- **Example:** `$env:VITE_APP_ENV="test"` tells the current PowerShell window to run iREPS Web with TEST environment settings.

- **Related terms:** APP_ENV, VITE_APP_ENV, EXPO_PUBLIC_APP_ENV, TEST

### Term: NODE_OPTIONS

- **Acronym:** None

- **Simple meaning:** A Node.js setting used to help Node commands behave correctly.

- **Detailed explanation:** In the current workflow, `NODE_OPTIONS="--dns-result-order=ipv4first"` helped Node-based tools reach Expo and npm services when network calls were failing through IPv6 or DNS ordering problems.

- **Example:** Before running EAS Build, the user set `$env:NODE_OPTIONS="--dns-result-order=ipv4first"` to avoid network fetch failures.

- **Related terms:** EAS Build, Expo, npm ping, Network Path

### Term: npm ping

- **Acronym:** None

- **Simple meaning:** A quick test to check whether npm can be reached.

- **Detailed explanation:** `npm ping` checks whether the machine can connect to the npm registry. In the iREPS build workflow, it is used to tell whether build failures are caused by project code or by local network reachability.

- **Example:** When `npm ping` returned PONG, it showed that the network path had improved before retrying the EAS build.

- **Related terms:** NODE_OPTIONS, EAS Build, Network Path, Expo

### Term: Test Readiness

- **Acronym:** None

- **Simple meaning:** The state where TEST is ready for guided user testing.

- **Detailed explanation:** Test readiness means the APK, web access, backend data, users, workbases, lookups, premises, and test scenarios are prepared enough for testers to start. It does not mean the product is bug-free; it means testing can begin in a controlled way.

- **Example:** Before Zamo's test session, iREPS confirmed the Test APK, `ireps-test`, workbases, lookup dropdowns, premises loading, and bug register approach.

- **Related terms:** TEST, Test Pack, Guided Testing, Bug Register, Zamo Demo

### Term: Guided Testing

- **Acronym:** None

- **Simple meaning:** Testing where the user follows agreed demo or test scenarios.

- **Detailed explanation:** Guided testing uses a controlled list of tasks so that issues can be reproduced and logged systematically. It is safer than random testing because the team knows what workflow, user role, environment, and expected result were being tested.

- **Example:** Zamo's test scenarios included electricity services such as create geofence, create premise, discover meter, commission meter, disconnect, reconnect, and remove meter.

- **Related terms:** Test Readiness, Bug Register, Electricity Services, Water Services

### Term: Demo Walkthrough

- **Acronym:** None

- **Simple meaning:** A guided presentation of selected iREPS features.

- **Detailed explanation:** A demo walkthrough is not full acceptance testing. It shows a prepared sequence of important workflows, explains the current state, and confirms that the test environment is ready for deeper testing.

- **Example:** The Zamo walkthrough presented TEST environment readiness, mobile APK, web access, workbases, premises loading, lookup readiness, and structured bug tracking.

- **Related terms:** Guided Testing, Test Readiness, Zamo Demo, Test Pack

### Term: Zamo Demo

- **Acronym:** None

- **Simple meaning:** The guided iREPS TEST demonstration prepared for Zamo.

- **Detailed explanation:** The Zamo Demo is the user-facing walkthrough used to show TEST readiness and begin structured testing. It includes mobile APK readiness, TEST web connection, workbase selection, premises loading, lookup dropdowns, offline readiness, electricity service scenarios, water service scenarios, MREAD Registry, and MREAD Staging.

- **Example:** The demo included separate visual pages for Electricity Services and Water Services walkthrough items.

- **Related terms:** Demo Walkthrough, Guided Testing, TEST, iREPS Test APK

## 13. Offline, Redux, and Lookup Concepts

### Term: Offline Readiness

- **Acronym:** None

- **Simple meaning:** The app can continue important work when the network is weak or unavailable.

- **Detailed explanation:** Offline readiness in iREPS means the mobile app has enough local data and queue support to allow fieldworkers to keep working during poor network conditions. It does not mean everything is available offline. The current focus is to make lookup options available after they have loaded once online, so form completion is not blocked by missing dropdowns.

- **Example:** A fieldworker opens a form online, lookup options load and persist, then the app can still show those options when the network drops.

- **Related terms:** Redux Persist, Lookup Options, Offline Queue, RTK Query Cache

### Term: Offline Queue

- **Acronym:** None

- **Simple meaning:** Local storage for work that must sync later.

- **Detailed explanation:** The offline queue stores work submissions or actions that cannot be sent immediately because the device is offline or network conditions are poor. It should be protected during sign-out and persistence changes unless the app intentionally clears it.

- **Example:** A completed field form may be kept in the offline queue until the device reconnects and can submit it.

- **Related terms:** Offline Readiness, Sync, Redux Persist, Field Form Flow

### Term: Redux Persist

- **Acronym:** None

- **Simple meaning:** A tool that saves selected Redux state between app restarts.

- **Detailed explanation:** Redux Persist allows selected parts of the mobile app state to survive app closing and reopening. In iREPS, persistence should be small and valuable: offline state and selected lookup option caches may persist, while large or sensitive live data should not be persisted blindly.

- **Example:** The store was changed to persist `offline` and `irepsLookupOptionsApi` so lookup dropdowns can work better offline after loading once online.

- **Related terms:** Persist Whitelist, Persist Blacklist, RTK Query Cache, Offline Readiness

### Term: Persist Whitelist

- **Acronym:** None

- **Simple meaning:** The list of Redux state slices that are allowed to be saved locally.

- **Detailed explanation:** A persist whitelist keeps local storage small by saving only approved parts of app state. In iREPS, this is important because saving all RTK Query caches could store too much data, stale data, or sensitive information.

- **Example:** The mobile store originally whitelisted only `offline`; the lookup persistence patch added `irepsLookupOptionsApi.reducerPath`.

- **Related terms:** Redux Persist, Persist Blacklist, Offline Readiness, RTK Query Cache

### Term: Persist Blacklist

- **Acronym:** None

- **Simple meaning:** The list of Redux state slices that must not be saved locally.

- **Detailed explanation:** A persist blacklist prevents large, sensitive, or scope-dependent caches from being stored in local persistence. Auth, users, premises, ERFs, work orders, and other live data should generally stay out of persistence unless there is a locked offline design.

- **Example:** `authApi`, `usersApi`, `premisesApi`, `erfsApi`, and many other APIs are blacklisted in the mobile store.

- **Related terms:** Redux Persist, Persist Whitelist, Auth, RTK Query Cache

### Term: RTK Query Cache

- **Acronym:** RTK Query

- **Simple meaning:** Stored API result data managed by Redux Toolkit Query.

- **Detailed explanation:** RTK Query caches results from API calls or streams so screens can reuse loaded data. Some caches are useful to keep briefly, but persisting large auth-dependent caches can cause stale data or security problems after sign-out.

- **Example:** The lookup options query cache can be persisted for offline dropdown use, but live premises or user caches should not be persisted blindly.

- **Related terms:** Redux Persist, Lookup Options, API Cache Reset, Sign-out Cleanup

### Term: Lookup Options

- **Acronym:** None

- **Simple meaning:** Dropdown choices used by iREPS forms.

- **Detailed explanation:** Lookup options are the selectable values used in forms, such as meter anomaly, anomaly detail, meter manufacturer, phase, placement, no access reason, and no reading reason. Field forms can be blocked if these options are missing.

- **Example:** A meter discovery form may need Meter Manufacturer and Meter Phase options before the fieldworker can complete it.

- **Related terms:** iREPS Select Lookups, Lookup Options Persistence, Field Form Flow, Offline Readiness

### Term: iREPS Select Lookups

- **Acronym:** None

- **Simple meaning:** The master lookup definitions used for iREPS select/dropdown fields.

- **Detailed explanation:** `irepsSelectLookups` is the Firestore collection that stores parent lookup documents and related subcollections. The parent document defines the lookup, while subcollections such as `options` hold selectable values and `audit` preserves changes.

- **Example:** `irepsSelectLookups/METER_ANOMALY` defines the meter anomaly lookup and has options underneath it.

- **Related terms:** Lookup Options, Parent Lookup Document, Options Subcollection, Audit Subcollection

### Term: Parent Lookup Document

- **Acronym:** None

- **Simple meaning:** The main document that defines a lookup list.

- **Detailed explanation:** A parent lookup document stores metadata such as lookup key, title, domain, field key, option count, status, and version. It may have subcollections for options and audit history.

- **Example:** `irepsSelectLookups/METER_PHASE` is a parent lookup document for meter phase choices.

- **Related terms:** iREPS Select Lookups, Options Subcollection, Audit Subcollection

### Term: Options Subcollection

- **Acronym:** None

- **Simple meaning:** The subcollection that stores actual dropdown values.

- **Detailed explanation:** The options subcollection lives under a parent lookup document and holds the values users select in forms. Copying only the parent lookup documents is incomplete if the options subcollections are not copied.

- **Example:** The TEST lookup copy had to include both parent docs and `options` subcollection docs.

- **Related terms:** Lookup Options, Parent Lookup Document, Recursive Copy Script

### Term: Audit Subcollection

- **Acronym:** None

- **Simple meaning:** The subcollection that stores lookup change history.

- **Detailed explanation:** The audit subcollection records changes made to lookup definitions or options. It supports traceability and helps explain how lookup values changed over time.

- **Example:** The recursive lookup copy found `audit` and `options` subcollections under the lookup parent documents.

- **Related terms:** Audit Trail, iREPS Select Lookups, Recursive Copy Script

### Term: Lookup Options Persistence

- **Acronym:** None

- **Simple meaning:** Saving lookup dropdown options locally so forms can still use them offline.

- **Detailed explanation:** Lookup options persistence means the mobile app keeps selected lookup option query data in persisted Redux storage. This supports form completion in weak-network conditions after the options have loaded at least once online.

- **Example:** The app persists `irepsLookupOptionsApi` so meter anomaly and no access reason dropdowns can remain available after restart or offline mode.

- **Related terms:** Offline Readiness, Redux Persist, Lookup Options, Persist Whitelist

### Term: First Load

- **Acronym:** None

- **Simple meaning:** The first time the app loads data after install, login, or cache reset.

- **Detailed explanation:** First load can feel slow because the app is downloading data, warming caches, opening streams, and preparing local state for the first time. It does not always indicate a bug.

- **Example:** Premises seemed missing in TEST at first, but they appeared after the first load completed.

- **Related terms:** Cache Warm-Up, Offline Readiness, Premises Loading, TEST

### Term: Cache Warm-Up

- **Acronym:** None

- **Simple meaning:** The app preparing local data after first opening.

- **Detailed explanation:** Cache warm-up happens when the app loads user profile, workbase, premises, lookup options, and other data into memory or local persistence. During warm-up, lists may take longer to appear.

- **Example:** The first TEST run took unusually long before premises appeared, but later loads were smoother.

- **Related terms:** First Load, RTK Query Cache, Offline Readiness

## 14. Workbase, Scope, and Access Concepts

### Term: Workbase

- **Acronym:** None

- **Simple meaning:** The municipality or operational area a user is working in.

- **Detailed explanation:** A workbase tells iREPS which Local Municipality, LM, Metro, or operational context the user is currently working under. In the locked iREPS Geography hierarchy, Workbase is represented at the Local Municipality / workbase / LM / Metro level. It helps scope data, screens, and workflows so users do not accidentally work in the wrong municipality.

- **Example:** In TEST, the SPU demo user can switch between King Sabata Dalindyebo and Lesedi workbases.

- **Related terms:** Active Workbase, LM, Metro, Ward, Operational Scope, SPU, iREPS Geography

### Term: Active Workbase

- **Acronym:** None

- **Simple meaning:** The currently selected workbase for the user.

- **Detailed explanation:** Active Workbase is the workbase iREPS uses right now for loading and filtering operational data. If the active workbase is wrong, the user may see the wrong premises, wards, or workflows.

- **Example:** Setting active workbase to Lesedi makes the user work inside the Lesedi TEST context.

- **Related terms:** Workbase, Workbase Selection, Operational Scope, LM

### Term: Workbase Selection

- **Acronym:** None

- **Simple meaning:** Choosing the municipality or workbase where the user will work.

- **Detailed explanation:** Workbase selection is important for SPU, ADM, and users who can access more than one municipality. It prevents confusion and ensures data is loaded for the intended LM.

- **Example:** During the Zamo demo, the workbase switcher showed King Sabata Dalindyebo and Lesedi.

- **Related terms:** Workbase, Active Workbase, SPU, LM

### Term: Operational Scope

- **Acronym:** None

- **Simple meaning:** The workbase / LM / Metro and ward context where iREPS work happens.

- **Detailed explanation:** Operational scope controls which data and workflows belong together. The locked iREPS rule is that operational scope is Workbase / LM / Metro plus Ward, and ward must be explicit for operational data and workflows where required. This is why the ERFs page depends on the selected ward.

- **Example:** A premise, ERF, or meter reading should be linked to the correct workbase / LM / Metro and ward scope.

- **Related terms:** LM, Metro, Ward, Workbase, Cadastral, Geofence, iREPS Geography

### Term: SPU Workbase Patch

- **Acronym:** None

- **Simple meaning:** A temporary TEST data correction for the SPU user's available workbases.

- **Detailed explanation:** The SPU workbase patch updated the TEST user document so the SPU demo user could see KSD and Lesedi instead of old or unrelated workbases. It was a safe data correction for demo readiness, not the final long-term role-resolution design.

- **Example:** The patch set TEST SPU workbases to King Sabata Dalindyebo and Lesedi.

- **Related terms:** SPU, Workbase, Active Workbase, Test Readiness

### Term: Role-Based Access

- **Acronym:** RBAC

- **Simple meaning:** Showing users only what their role allows.

- **Detailed explanation:** Role-based access controls what a user can see and do in iREPS. It works with user role, service provider, workbase, and operational scope.

- **Example:** A Fieldworker can execute assigned fieldwork, while an SPU demo user can access broader setup or test views.

- **Related terms:** Fieldworker, Supervisor, Manager, Superuser, Workbase

## 15. Cadastral Pipeline and Import Safety Concepts

### Term: Cadastral Pipeline

- **Acronym:** None

- **Simple meaning:** The step-by-step process for preparing and importing cadastral ERF data.

- **Detailed explanation:** The cadastral pipeline converts source geography data into clean iREPS-standard Firestore records. It includes source inspection, parent geography QA, ERF generation, duplicate diagnosis, boundary-risk handling, create-only import, and verification.

- **Example:** The Lesedi pipeline prepared ZA7423 ERFs for safe loading into `ireps-test`.

- **Related terms:** Cadastral, ERF, Parent Geography, Create-only Import, Verification

### Term: Parent Geography

- **Acronym:** None

- **Simple meaning:** The higher-level geography that an ERF belongs to.

- **Detailed explanation:** Parent geography includes country, province, district municipality, local municipality, and ward references. It must be correct before ERFs are imported because iREPS uses these parents for operational scope and filtering.

- **Example:** A Lesedi ERF must point to the correct province, district, LM, and ward pcodes.

- **Related terms:** Admin Geography, LM, Ward, Pcode, Cadastral Pipeline

### Term: Admin Geography

- **Acronym:** None

- **Simple meaning:** The official administrative geography used to organise iREPS data.

- **Detailed explanation:** Admin geography is the structure of municipal and ward boundaries used to attach operational records to the correct place. It supports reporting, workbase selection, and field assignment.

- **Example:** Lesedi's admin geography must be validated before importing Lesedi ERFs.

- **Related terms:** Parent Geography, Boundary, Ward, LM, Workbase

### Term: PRCLKEY

- **Acronym:** PRCLKEY

- **Simple meaning:** A parcel key used as the stable ERF identifier in the Lesedi pipeline.

- **Detailed explanation:** PRCLKEY is important where the final ERF document ID must align to a stable parcel identifier rather than an unstable generated ID. In the Lesedi workstream, rekeying focused on using PRCLKEY-only document IDs for resolved ERFs.

- **Example:** A resolved Lesedi ERF may be rekeyed so the Firestore document ID is based on PRCLKEY.

- **Related terms:** ERF, Rekey, Cadastral Pipeline, Create-only Import

### Term: Rekey

- **Acronym:** None

- **Simple meaning:** Changing the document key or ID strategy for records.

- **Detailed explanation:** Rekeying is used when records were created or prepared with the wrong ID and must be aligned to the locked identifier rule. It must be done carefully with dry-run verification because keys affect references and duplicate detection.

- **Example:** The Lesedi pipeline included rekeying 33,213 resolved ERFs to PRCLKEY-only document IDs.

- **Related terms:** PRCLKEY, ERF, Create-only Import, Verification

### Term: Create-only Import

- **Acronym:** None

- **Simple meaning:** An import that creates missing records but does not overwrite existing ones.

- **Detailed explanation:** Create-only import is a safety rule for loading data into Firestore. It avoids accidental overwriting of existing documents and is preferred when importing cadastral or base data into TEST.

- **Example:** A create-only import can load clean Lesedi ERFs into `ireps-test` without replacing existing documents.

- **Related terms:** Dry Run, Write Mode, Firestore, Cadastral Pipeline

### Term: Dry Run

- **Acronym:** None

- **Simple meaning:** A safe test run that shows what would happen without writing data.

- **Detailed explanation:** Dry run mode is used before any dangerous or important write operation. It reads inputs, prepares a plan, counts records, and reports expected changes without modifying Firestore.

- **Example:** The recursive lookup copy first ran in dry-run mode and reported 220 documents queued before write mode was used.

- **Related terms:** Write Mode, Verification, Create-only Import, Script

### Term: Write Mode

- **Acronym:** None

- **Simple meaning:** The script mode that actually writes changes.

- **Detailed explanation:** Write mode performs the Firestore changes after a dry run has passed and the user provides the required confirmation flag. It should be used carefully and only when the planned changes are understood.

- **Example:** The lookup copy script entered write mode only after the confirm flag `COPY_IREPS_SELECT_LOOKUPS_RECURSIVE_TO_TEST` was provided.

- **Related terms:** Dry Run, Confirm Flag, Firestore, Script

### Term: Confirm Flag

- **Acronym:** None

- **Simple meaning:** A special command argument required before a script performs writes.

- **Detailed explanation:** A confirm flag is a safety gate. It prevents accidental writes when a user only intended to run a dry run. The script checks for the exact confirmation text before writing.

- **Example:** The recursive lookup copy script required `--confirm COPY_IREPS_SELECT_LOOKUPS_RECURSIVE_TO_TEST` before writing to `ireps-test`.

- **Related terms:** Dry Run, Write Mode, Script, Firestore

### Term: Verification

- **Acronym:** QA

- **Simple meaning:** Checking that imported or generated data is correct.

- **Detailed explanation:** Verification confirms that counts, IDs, parent geography, document shape, duplicates, and Firestore writes match the expected result. It is a required safety step after data generation, import, rekey, or cleanup.

- **Example:** KSD's full ERF import was verified with zero failures and zero duplicate ERF ID groups.

- **Related terms:** QA, Cadastral Pipeline, Create-only Import, Duplicate, Boundary Risk

### Term: Duplicate Exclusion

- **Acronym:** None

- **Simple meaning:** Temporarily keeping duplicate-risk records out of the final import.

- **Detailed explanation:** Duplicate exclusion removes or separates records that need manual map review or deeper investigation. This prevents risky duplicates from entering the clean operational dataset.

- **Example:** The Lesedi pipeline excluded duplicate groups for map review before continuing with resolved ERF QA.

- **Related terms:** Duplicate, Boundary Risk, ERF, Cadastral Pipeline

### Term: Boundary Risk

- **Acronym:** None

- **Simple meaning:** A spatial data condition that may affect safe assignment to a ward or LM.

- **Detailed explanation:** Boundary risk refers to ERFs or spatial features that may cross, straddle, overlap, or sit close to important administrative boundaries. These records require special handling because wrong boundary assignment can break operational scope.

- **Example:** A Lesedi ERF near a ward boundary may be excluded from automatic import until reviewed.

- **Related terms:** Boundary, Boundary Straddle, Ward, LM, Duplicate Exclusion

### Term: Pilot Import

- **Acronym:** None

- **Simple meaning:** A small controlled import used to prove the process before full import.

- **Detailed explanation:** A pilot import writes a small number of records first so the team can verify document shape, IDs, permissions, and read-back results before committing a full dataset.

- **Example:** The pipeline may import 10 ERFs as a pilot before importing thousands of records.

- **Related terms:** Create-only Import, Verification, Dry Run, Cadastral Pipeline

### Term: Wrong Pilot Docs

- **Acronym:** None

- **Simple meaning:** Pilot documents created with the wrong key, shape, or rule.

- **Detailed explanation:** Wrong pilot docs are temporary test records that must be cleaned up before final import. They should be deleted only with a controlled, explicit, dry-run-first script.

- **Example:** The Lesedi workstream included a script to delete 10 wrong pilot ERFs only.

- **Related terms:** Pilot Import, Cleanup Script, Dry Run, Rekey

### Term: Cleanup Script

- **Acronym:** None

- **Simple meaning:** A script that safely removes or corrects specific unwanted records.

- **Detailed explanation:** A cleanup script should be narrow, explicit, and dry-run-first. It must target only the approved records and should not perform broad deletes.

- **Example:** A cleanup script can remove only 10 wrong Lesedi pilot ERF documents after user approval.

- **Related terms:** Dry Run, Write Mode, Wrong Pilot Docs, Cadastral Pipeline

### Term: Service Account

- **Acronym:** None

- **Simple meaning:** A credential file that allows scripts to access Firebase Admin services.

- **Detailed explanation:** A service account lets trusted backend scripts read or write Firestore with admin privileges. It must be protected and never included in ZIP files sent for code delivery.

- **Example:** The TEST scripts use the local service account path `C:\dev\secrets\ireps-test-firebase-adminsdk-fbsvc-d02929e1e3.json`.

- **Related terms:** Firebase Admin SDK, Script, Firestore, Security

### Term: Firebase Admin SDK

- **Acronym:** SDK

- **Simple meaning:** Backend Firebase tools used by Node scripts.

- **Detailed explanation:** Firebase Admin SDK lets trusted Node scripts read and write Firebase data with admin privileges. In iREPS, it is used for controlled imports, patches, verification, and data-copy scripts.

- **Example:** The recursive lookup copy script used Firebase Admin SDK connections to read from `ireps2` and write to `ireps-test`.

- **Related terms:** Service Account, Firestore, Script, Dry Run

### Term: functions/scripts Folder

- **Acronym:** None

- **Simple meaning:** The standard folder for iREPS backend utility scripts.

- **Detailed explanation:** Current iREPS convention is that Node utility scripts for the functions project should go under `functions/scripts/` unless instructed otherwise. This keeps scripts organised and close to the Firebase functions project.

- **Example:** The recursive lookup copy script was placed under `C:\dev\ireps-web\functions\scripts`.

- **Related terms:** Script, Firebase Admin SDK, ES Modules, Service Account

### Term: ES Modules

- **Acronym:** ESM

- **Simple meaning:** JavaScript import/export syntax used by the functions project.

- **Detailed explanation:** The iREPS functions project uses ES modules because `functions/package.json` has `"type": "module"`. Scripts with `.js` extension should use `import` syntax instead of CommonJS `require`, unless the script is explicitly `.cjs`.

- **Example:** A functions script should use `import admin from "firebase-admin";` rather than `const admin = require("firebase-admin");`.

- **Related terms:** functions/scripts Folder, Node Script, Firebase Admin SDK

## 16. Sign-out, Firebase Listener, and Stability Concepts

### Term: Sign-out Cleanup

- **Acronym:** None

- **Simple meaning:** The safe shutdown process when a user logs out.

- **Detailed explanation:** Sign-out cleanup must stop authenticated streams, clear auth-dependent caches, and return the UI to the login flow without leaving Firebase listeners running. This prevents permission errors and crashes after the user is signed out.

- **Example:** A correct logout sequence resets auth-dependent RTK Query APIs and unsubscribes Firestore listeners before or during Firebase sign-out.

- **Related terms:** Firebase Listener, API Cache Reset, Auth State, RTK Query Cache

### Term: Firebase Listener

- **Acronym:** None

- **Simple meaning:** A live Firebase data subscription.

- **Detailed explanation:** A Firebase listener watches Firestore or Auth for changes and updates the app when data changes. Listeners must be unsubscribed when screens unmount or when the user signs out, otherwise they may continue reading protected data after auth becomes null.

- **Example:** A Firestore `onSnapshot` listener for work orders must stop when the user signs out.

- **Related terms:** onSnapshot, Sign-out Cleanup, Firestore, Auth State

### Term: onSnapshot

- **Acronym:** None

- **Simple meaning:** Firestore's live data listening function.

- **Detailed explanation:** `onSnapshot` streams data from Firestore in real time. It returns an unsubscribe function that must be called during cleanup. In iREPS Mobile, any `onSnapshot` used inside RTK Query or context providers must be guarded for logout.

- **Example:** WMS work item streams use Firestore snapshots and must unsubscribe safely during sign-out.

- **Related terms:** Firebase Listener, Firestore, RTK Query Cache, Sign-out Cleanup

### Term: Auth State

- **Acronym:** None

- **Simple meaning:** Whether the app currently has a signed-in user.

- **Detailed explanation:** Auth state drives whether iREPS shows authenticated screens or the login flow. Components must handle the transition from signed-in to signed-out without assuming `user`, `profile`, or `activeWorkbase` still exists.

- **Example:** After Firebase sign-out, Auth State becomes signed out and protected screens should stop rendering.

- **Related terms:** Firebase Auth, Sign-out Cleanup, Role-Based Access, Active Workbase

### Term: API Cache Reset

- **Acronym:** None

- **Simple meaning:** Clearing API caches that depend on the signed-in user.

- **Detailed explanation:** API cache reset removes stale or protected data from RTK Query APIs during logout or environment changes. It helps prevent old listeners or cached data from continuing after auth state changes.

- **Example:** On sign-out, user, premise, ERF, TRN, WMS, and geofence APIs may need reset, while offline and lookup option persistence should be preserved if safe.

- **Related terms:** RTK Query Cache, Sign-out Cleanup, Persist Whitelist, Offline Queue

### Term: Logout Guard

- **Acronym:** None

- **Simple meaning:** Defensive logic that stops authenticated work during logout.

- **Detailed explanation:** A logout guard prevents components, providers, and API streams from starting or continuing while logout is in progress. It avoids race conditions where screens recreate listeners after sign-out has started.

- **Example:** A provider can avoid starting a Firestore query if logout is in progress or if no user is signed in.

- **Related terms:** Sign-out Cleanup, Firebase Listener, Auth State, API Cache Reset

## 17. Electricity and Water Demo Scenario Concepts

### Term: Electricity Services

- **Acronym:** None

- **Simple meaning:** The iREPS demo group for electricity-related workflows.

- **Detailed explanation:** Electricity Services groups workflows involving electricity meters and supply actions. The Zamo demo list includes geofence creation, premise creation inside and outside the geofence, meter discovery, installation, data cleansing, commissioning, disconnection, reconnection, and removal.

- **Example:** An electricity demo scenario may discover a meter in a geofence and then later test disconnection and reconnection.

- **Related terms:** Meter Discovery, Meter Installation, Meter Commissioning, Meter Disconnection, Meter Reconnection, Meter Removal

### Term: Water Services

- **Acronym:** None

- **Simple meaning:** The iREPS demo group for water-related workflows.

- **Detailed explanation:** Water Services groups water meter discovery, controlled and uncontrolled meter reading, and review through MREAD Registry and MREAD Staging. It shows that iREPS workflow logic can support water operations as well as electricity operations.

- **Example:** A water demo scenario may discover a water meter, perform an uncontrolled read, then view the reading in MREAD Registry.

- **Related terms:** MREAD, MREAD Registry, MREAD Staging, Meter Reading

### Term: Field Form Flow

- **Acronym:** None

- **Simple meaning:** The sequence a fieldworker follows to complete a mobile form.

- **Detailed explanation:** Field Form Flow includes opening the relevant premise or task, starting the form, selecting lookup options, capturing required data, adding photos or evidence, and saving or completing the workflow.

- **Example:** For meter discovery, the fieldworker opens the premise, captures meter details, selects lookup values, takes evidence photos, and submits the transaction.

- **Related terms:** Mobile App, Lookup Options, Evidence, Transaction (TRN), Offline Readiness

### Term: Create Geofence

- **Acronym:** None

- **Simple meaning:** Creating a mapped area used to group or control work.

- **Detailed explanation:** Create Geofence is a demo/test action where the user creates a geographic boundary used to organise premises, meters, or workflows. It helps test spatial scope and inside/outside behaviour.

- **Example:** The electricity services demo starts by creating a geofence before creating premises inside and outside it.

- **Related terms:** Geofence, Boundary, Premise, Operational Scope

### Term: Premise Inside Geofence

- **Acronym:** None

- **Simple meaning:** A premise whose location falls inside a selected geofence.

- **Detailed explanation:** This term is used in testing to confirm that iREPS correctly recognises a premise as being inside a mapped boundary. It supports workflow scoping, geofence-based operations, and spatial validation.

- **Example:** A test premise may be created inside Gf Test to confirm that it appears as part of that geofence.

- **Related terms:** Premise, Geofence, Boundary, Operational Scope

### Term: Premise Outside Geofence

- **Acronym:** None

- **Simple meaning:** A premise whose location falls outside a selected geofence.

- **Detailed explanation:** This term is used to prove that iREPS can distinguish records inside and outside a boundary. It is important for validating geofence logic and preventing incorrect work grouping.

- **Example:** A test premise created outside Gf Test should not behave like a premise inside the geofence.

- **Related terms:** Premise, Geofence, Boundary, Data Quality

### Term: Data Cleansing

- **Acronym:** None

- **Simple meaning:** Fixing or improving incorrect, incomplete, or inconsistent data.

- **Detailed explanation:** Data cleansing in iREPS means reviewing field or imported data and correcting it so records can be trusted. It may involve meter numbers, premise links, geofence relationships, statuses, or lookup values.

- **Example:** A meter already on sales may need data cleansing so iREPS and the sales repository agree on its details.

- **Related terms:** Data Quality, Sales Repository, Meter Master, Normalisation

## Dictionary changelog

### Version 1.5 — 2026-07-19

- Amended Meter Master as the source-neutral canonical identity and cross-reference register.
- Added Meter Master identity, AST and sales references, derived lifecycle classifications, ownership, initial-load, recurring-refresh, record-result, conflict, and final-run terminology.
- Confirmed that lifecycle classifications are derived concepts and are not persisted Meter Master status fields.
