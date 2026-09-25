# BGO Planning — Field Catalogue

Module **FRM-031** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](bgo-planning-body-of-knowledge.md) · [User Manual](../02-user-manual/web/bgo-planning-user-manual.md) · [Field catalogue](bgo-planning-field-catalogue.md) · [Error register](bgo-planning-error-register.md) · [Practical examples](../10-assessments/bgo-planning-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Source population | Reference set | Records from which the BGO is created. | Check the specific BMD/TC route and source eligibility. | Synthetic row set |
| Batch context | Structured selection | Workbase/area and available targeting values. | Use the exact implementation variant; no invented global schema. | Training context |
| Delete action | Action | Removal of an eligible unaccepted BGO. | Source names DeleteUnacceptedBgo; acceptance changes eligibility. | Review before deletion |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-031-C001 — selectedWardPcode

- **Meaning:** Source control for selectedWardPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `selectedWardPcode`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!lmPcode &#124;&#124; wardOptions.length === 0`.
- **Change handling:** `handleWardChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-158:1141](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/BmdBgoPage.jsx#L1141).

### FRM-031-C002 — selectedId

- **Meaning:** Source control for selectedId; interpret in the business definitions and its enclosing section.
- **UI binding:** `selectedId`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: rowsWithMultipleGeofences.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) =><br>                      selectRowGeofence(row.id, event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-165:1528](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TcBgoPage.jsx#L1528).

### FRM-031-C003 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:687](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L687).

### FRM-031-C004 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:698](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L698).

### FRM-031-C005 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:724](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L724).

### FRM-031-C006 — premiseFilters.address

- **Meaning:** Source control for premiseFilters.address; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.address`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            address: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1193](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1193).

### FRM-031-C007 — premiseFilters.erfNo

- **Meaning:** Source control for premiseFilters.erfNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.erfNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            erfNo: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1204](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1204).

### FRM-031-C008 — premiseFilters.propertyType

- **Meaning:** Source control for premiseFilters.propertyType; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.propertyType`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            propertyType: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1215](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1215).

### FRM-031-C009 — premiseFilters.propertyName

- **Meaning:** Source control for premiseFilters.propertyName; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.propertyName`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            propertyName: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1226](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1226).

### FRM-031-C010 — premiseFilters.unitNo

- **Meaning:** Source control for premiseFilters.unitNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.unitNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            unitNo: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1237](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1237).

### FRM-031-C011 — premiseFilters.meters

- **Meaning:** Source control for premiseFilters.meters; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.meters`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            meters: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1248](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1248).

### FRM-031-C012 — premiseFilters.createdBy

- **Meaning:** Source control for premiseFilters.createdBy; interpret in the business definitions and its enclosing section.
- **UI binding:** `premiseFilters.createdBy`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_PREMISES; conditional branch: visiblePremiseRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setPremiseFilters((prev) => ({<br>                            ...prev,<br>                            createdBy: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1270](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1270).

### FRM-031-C013 — meterFilters.meterNo

- **Meaning:** Source control for meterFilters.meterNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.meterNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            meterNo: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1373](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1373).

### FRM-031-C014 — meterFilters.premiseAddress

- **Meaning:** Source control for meterFilters.premiseAddress; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.premiseAddress`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            premiseAddress: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1384](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1384).

### FRM-031-C015 — meterFilters.erfNo

- **Meaning:** Source control for meterFilters.erfNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.erfNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({ ...prev, erfNo: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1395](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1395).

### FRM-031-C016 — meterFilters.meterType

- **Meaning:** Source control for meterFilters.meterType; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.meterType`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `meterFilterOptions.meterType`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            meterType: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1403](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1403).

### FRM-031-C017 — meterFilters.meterKind

- **Meaning:** Source control for meterFilters.meterKind; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.meterKind`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `meterFilterOptions.meterKind`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            meterKind: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1415](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1415).

### FRM-031-C018 — meterFilters.meterPhase

- **Meaning:** Source control for meterFilters.meterPhase; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.meterPhase`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `meterFilterOptions.meterPhase`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            meterPhase: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1427](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1427).

### FRM-031-C019 — meterFilters.status

- **Meaning:** Source control for meterFilters.status; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.status`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `meterFilterOptions.status`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            status: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1439](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1439).

### FRM-031-C020 — meterFilters.createdBy

- **Meaning:** Source control for meterFilters.createdBy; interpret in the business definitions and its enclosing section.
- **UI binding:** `meterFilters.createdBy`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_METERS; conditional branch: visibleMeterRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setMeterFilters((prev) => ({<br>                            ...prev,<br>                            createdBy: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1451](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1451).

### FRM-031-C021 — trnFilters.trnType

- **Meaning:** Source control for trnFilters.trnType; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.trnType`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.trnType`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({ ...prev, trnType: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1562](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1562).

### FRM-031-C022 — trnFilters.workflow

- **Meaning:** Source control for trnFilters.workflow; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.workflow`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.workflow`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({<br>                            ...prev,<br>                            workflow: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1572](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1572).

### FRM-031-C023 — trnFilters.outcome

- **Meaning:** Source control for trnFilters.outcome; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.outcome`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.outcome`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({ ...prev, outcome: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1585](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1585).

### FRM-031-C024 — trnFilters.access

- **Meaning:** Source control for trnFilters.access; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.access`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.access`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({ ...prev, access: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1595](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1595).

### FRM-031-C025 — trnFilters.erfNo

- **Meaning:** Source control for trnFilters.erfNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.erfNo`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.erfNo`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({ ...prev, erfNo: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1605](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1605).

### FRM-031-C026 — trnFilters.premiseId

- **Meaning:** Source control for trnFilters.premiseId; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.premiseId`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({<br>                            ...prev,<br>                            premiseId: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1615](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1615).

### FRM-031-C027 — trnFilters.meterNo

- **Meaning:** Source control for trnFilters.meterNo; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.meterNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({ ...prev, meterNo: value }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1626](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1626).

### FRM-031-C028 — trnFilters.executor

- **Meaning:** Source control for trnFilters.executor; interpret in the business definitions and its enclosing section.
- **UI binding:** `trnFilters.executor`; component `SelectFilter`; input hint `SelectFilter`.
- **Visibility/prerequisites:** `conditional branch: activeTab === TAB_TRNS; conditional branch: visibleTrnRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `trnFilterOptions.executor`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          setTrnFilters((prev) => ({<br>                            ...prev,<br>                            executor: value,<br>                          }))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-161:1634](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/MdBgoRowsPage.jsx#L1634).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

This family needs route-by-route release review. Do not treat every historical BGO screen as a current recommended workflow.

[Download the detailed control inventory (CSV)](bgo-planning-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](bgo-planning-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
