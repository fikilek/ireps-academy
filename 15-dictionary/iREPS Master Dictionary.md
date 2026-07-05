# iREPS Master Dictionary

## Purpose

The iREPS Master Dictionary is the official single source of truth for words, acronyms, modules, workflows, roles, data concepts, and operational terms used inside iREPS.

The goal is to explain each term in simple language while preserving the correct iREPS meaning. This dictionary is intended for municipal users, fieldworkers, supervisors, managers, developers, support teams, trainers, and future iREPS documentation.

The iREPS Master Dictionary must be reviewed and refined continuously. Every new iREPS word, acronym, workflow name, module name, role, data concept, and operational term must be added here so that all iREPS documentation and training uses one approved meaning.

This is Version 1.2 of the iREPS Master Dictionary. It preserves Version 1.1 locked meanings and enriches the master dictionary using the TEST environment readiness workstream, iREPS Test APK and Web setup, Firebase lookup migration, offline lookup persistence, Cadastral Pipeline v6 context, Zamo demo walkthrough items, and the current logout/sign-out stability investigation.

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

- **Detailed explanation:** A Transaction represents a specific piece of operational work in iREPS. It records the workflow, assignment, execution, outcome, user actions, evidence, and status changes. Transactions are central to iREPS because they preserve what was done, who did it, when it was done, where it was done, and what result was produced.

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

### Term: Asset

- **Acronym:** AST

- **Simple meaning:** A physical or operational item that iREPS tracks.

- **Detailed explanation:** An Asset is something with operational value that can be captured, located, updated, inspected, acted on, and tracked over time. In the meter context, the meter is an Asset with a lifetime. An Asset may have an identifier, location, status, linked premise, linked transactions, evidence, and operational history. AST is the iREPS acronym used for Asset.

- **Example:** A newly installed meter creates or updates an Asset record linked to the premise where the meter is installed.

- **Related terms:** AST, Meter, Meter Installation, Meter Discovery, Operational Status, Transaction (TRN)

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

- **Simple meaning:** A cadastral land parcel or property unit.

- **Detailed explanation:** An ERF is a cadastral property parcel used to understand land and property boundaries. In iREPS, ERFs help connect premises and municipal operations to a geographic and cadastral base.

- **Example:** A premise may be located on ERF 1234 within a specific ward and local municipality.

- **Related terms:** Premise, Ward, LM, Cadastral, Geofence

### Term: Ward

- **Acronym:** None

- **Simple meaning:** A municipal ward area used for operational scope.

- **Detailed explanation:** A ward is a local government area inside a municipality. In iREPS, ward scope is important because fieldwork, reporting, geofences, premises, ERFs, and operations are often organised by ward. Ward must be explicit for operational data and workflows.

- **Example:** A fieldworker may be assigned meter reading work for a ward such as ZA21570003.

- **Related terms:** LM, ERF, Premise, Geofence, Scope

### Term: LM

- **Acronym:** LM

- **Simple meaning:** Local Municipality.

- **Detailed explanation:** LM is the local municipality level in iREPS operational scope. Many iREPS workflows, records, and imports are organised by LM and then by ward. LM helps iREPS separate operational data by municipal jurisdiction.

- **Example:** King Sabata Dalindyebo Local Municipality uses LM pCode ZA2157 in the iREPS context.

- **Related terms:** Ward, Municipality, LM pCode, Scope, Governance

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

## 5. Meter Data and Sales Link Concepts

### Term: Meter Master

- **Acronym:** MASTER

- **Simple meaning:** A thin bridge record for a meter identity.

- **Detailed explanation:** Meter Master connects meter identity across operational and sales-related contexts without loading large sales collections into the mobile app or Warehouse. It helps iREPS know whether a meter is in the sales repository, linked to an Asset, or visible for certain operational purposes. The Master record should remain a thin bridge, not a heavy operational collection.

- **Example:** A normalized meter number can be checked against meter_master to see whether the meter exists in sales and whether it is already linked to an Asset.

- **Related terms:** MASTER, Meter Discovery, Sales Repository, Visibility, Asset (AST), Normalized Meter Number

### Term: MASTER

- **Acronym:** MASTER

- **Simple meaning:** The short name for Meter Master.

- **Detailed explanation:** MASTER refers to the meter master bridge concept. It supports point lookups and identity linking for meters. It helps iREPS avoid expensive queries across large sales datasets while still giving controlled awareness of sales linkage.

- **Example:** When a meter number is typed or scanned, iREPS can check MASTER to see whether the meter appears in the sales repository.

- **Related terms:** Meter Master, Sales Repository, Visibility, Meter Discovery

### Term: Normalized Meter Number

- **Acronym:** None

- **Simple meaning:** A cleaned, standard version of a meter number.

- **Detailed explanation:** A normalized meter number is the meter number after applying the same standard formatting rules everywhere. Normalization helps iREPS match the same meter even if users type spaces, lowercase letters, or different formatting. The same normalizer should be used in the form, backend lookup, Asset creation, Meter Master, and sales import logic.

- **Example:** A meter number typed as “010 236 70951” may be normalized to “01023670951”.

- **Related terms:** Meter Master, Meter Number, Sales Repository, FormInputMeterNo

### Term: Sales Repository

- **Acronym:** None

- **Simple meaning:** The source or collection where sales-related meter records are kept.

- **Detailed explanation:** The sales repository contains meter numbers and related commercial or billing-side meter information. It is not the same as iREPS operational field data. In iREPS design, sales data should not be loaded into Warehouse or treated as normal field data. Instead, a thin Meter Master bridge can provide controlled awareness of whether a discovered meter appears in the sales repository.

- **Example:** A discovered meter number is checked against the sales repository. If a match is found, the discovered meter is treated as VISIBLE.

- **Related terms:** Sales Data, Meter Master, MASTER, Visibility, Warehouse, Meter Discovery

### Term: Sales Data

- **Acronym:** None

- **Simple meaning:** Meter or customer data from the municipal sales or billing environment.

- **Detailed explanation:** Sales Data may contain meter information from municipal commercial systems. It is not the same as iREPS operational field data. The mobile app should not preload all sales meters into Warehouse. Instead, iREPS should use controlled backend or Master-based checks to determine whether a captured meter number appears in the sales repository.

- **Example:** A discovered meter may be found in sales data, meaning iREPS can mark it VISIBLE after backend checks.

- **Related terms:** Sales Repository, Meter Master, MASTER, Visibility, Warehouse, Meter Discovery

### Term: Visibility

- **Acronym:** None

- **Simple meaning:** Whether a discovered meter is VISIBLE or INVISIBLE based on whether its captured meter number appears in the sales repository.

- **Detailed explanation:** A meter is VISIBLE if the captured meter number appears in the sales repository. When a meter is discovered in the field and registered in iREPS, iREPS checks that meter number against the sales repository. If a matching meter number is found, the meter is termed VISIBLE. If no match is found, the meter is termed INVISIBLE. The backend check remains the authority for this decision.

- **Example:** A fieldworker discovers meter 01023670951. iREPS checks the sales repository. If 01023670951 is found, the meter becomes VISIBLE; if it is not found, the meter is INVISIBLE.

- **Related terms:** VISIBLE, INVISIBLE, Sales Repository, Meter Master, Backend Check, Meter Discovery

### Term: VISIBLE

- **Acronym:** None

- **Simple meaning:** A discovered meter whose captured meter number appears in the sales repository.

- **Detailed explanation:** VISIBLE means the meter captured in the field has a matching meter number in the sales repository. It indicates that iREPS has found a sales-side match for the field-captured meter number. This does not mean the form alone is the final truth; the backend must still confirm and stamp the final linkage.

- **Example:** The fieldworker captures meter number 01023670951, and the backend finds that same number in the sales repository. The meter is termed VISIBLE.

- **Related terms:** Visibility, INVISIBLE, Sales Repository, Meter Master

### Term: INVISIBLE

- **Acronym:** None

- **Simple meaning:** A discovered meter whose captured meter number is not found in the sales repository.

- **Detailed explanation:** INVISIBLE means the meter was captured in the field but no matching meter number was found in the sales repository. This protects iREPS from treating an unmatched field-captured meter as a confirmed sales-linked meter. The meter may still exist physically and operationally, but the sales linkage is not confirmed.

- **Example:** The fieldworker captures meter number 999888777, but that number is not found in the sales repository. The meter is termed INVISIBLE.

- **Related terms:** Visibility, VISIBLE, Sales Repository, Meter Master

### Term: Backend Check

- **Acronym:** None

- **Simple meaning:** A server-side validation that confirms the real truth.

- **Detailed explanation:** In iREPS, form-side checks can help users, but the backend check must remain the authority. For meter discovery and sales linkage, the backend should normalize the meter number, check the sales repository or Meter Master, apply rules, and stamp the final Asset or visibility values.

- **Example:** Even if the mobile form shows “In Sales,” the backend must still re-check the meter number when the user submits.

- **Related terms:** Server-side Check, Form-side Check, Meter Master, Validation

### Term: Form-side Check

- **Acronym:** None

- **Simple meaning:** A helpful check shown on the user form before submission.

- **Detailed explanation:** A form-side check gives the user early awareness while typing or scanning. It should not be treated as the final truth. In meter discovery, a form-side check may show whether a meter appears to exist in sales, but the backend must confirm again on save.

- **Example:** A small badge below the meter number field may show “IN SALES” while the fieldworker captures the meter.

- **Related terms:** Backend Check, FormInputMeterNo, Meter Master, UI Badge

### Term: FormInputMeterNo

- **Acronym:** None

- **Simple meaning:** The form component used to capture a meter number.

- **Detailed explanation:** FormInputMeterNo is the user interface field where a meter number can be typed or scanned. It may perform local duplicate checks and can also show a soft awareness badge based on a debounced Meter Master or sales-link lookup. It should not become the final authority for whether a meter is valid or linked.

- **Example:** A fieldworker scans a meter number and the FormInputMeterNo field shows whether the meter appears to be in sales.

- **Related terms:** Meter Number, Meter Master, Form-side Check, Backend Check

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

- **Detailed explanation:** A workbase tells iREPS which LM or operational context the user is currently working under. It helps scope data, screens, and workflows so users do not accidentally work in the wrong municipality.

- **Example:** In TEST, the SPU demo user can switch between King Sabata Dalindyebo and Lesedi workbases.

- **Related terms:** Active Workbase, LM, Ward, Operational Scope, SPU

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

- **Simple meaning:** The LM and ward context where iREPS work happens.

- **Detailed explanation:** Operational scope controls which data and workflows belong together. The locked iREPS rule is that operational scope is LM plus Ward, and ward must be explicit for operational data and workflows where required.

- **Example:** A premise, ERF, or meter reading should be linked to the correct LM and ward scope.

- **Related terms:** LM, Ward, Workbase, Cadastral, Geofence

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
