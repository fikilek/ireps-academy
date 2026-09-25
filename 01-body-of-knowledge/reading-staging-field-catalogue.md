# Meter Reading Staging and Export — Field Catalogue

Module **FRM-032** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](reading-staging-body-of-knowledge.md) · [User Manual](../02-user-manual/web/reading-staging-user-manual.md) · [Field catalogue](reading-staging-field-catalogue.md) · [Error register](reading-staging-error-register.md) · [Practical examples](../10-assessments/reading-staging-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Municipality/workbase | Reference | Scope of the readings prepared. | Check the active workbase and explicit municipality code. | Training municipality |
| Billing period/session | Controlled selection | Period and generation context. | A session is not simply the month displayed by a filter. | Training period |
| Generation controls | Action/configuration | Initiates supported staging preparation. | Role and backend eligibility must be checked. | Generate staging |
| Export | File output | Prepared readings for downstream use. | Verify counts/identity/units and receiving-system format; download is not import. | Synthetic export |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-032-C001 — ZA2157

- **Meaning:** Source control for ZA2157; interpret in the business definitions and its enclosing section.
- **UI binding:** `lmPcode`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setLmPcode(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-157:160](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/admin/MreadStagingControllerPage.jsx#L160).

### FRM-032-C002 — billingPeriod

- **Meaning:** Source control for billingPeriod; interpret in the business definitions and its enclosing section.
- **UI binding:** `billingPeriod`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setBillingPeriod(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-157:170](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/admin/MreadStagingControllerPage.jsx#L170).

### FRM-032-C003 — Cycle, window, staging id...

- **Meaning:** Source control for Cycle, window, staging id...; interpret in the business definitions and its enclosing section.
- **UI binding:** `search`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setSearch(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-157:184](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/admin/MreadStagingControllerPage.jsx#L184).

### FRM-032-C004 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:958](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L958).

### FRM-032-C005 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:969](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L969).

### FRM-032-C006 — safeLmPcode

- **Meaning:** Source control for safeLmPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `safeLmPcode`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:1914](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L1914).

### FRM-032-C007 — billingPeriod

- **Meaning:** Source control for billingPeriod; interpret in the business definitions and its enclosing section.
- **UI binding:** `billingPeriod`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setBillingPeriod(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:1919](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L1919).

### FRM-032-C008 — Cycle, window, base cycle...

- **Meaning:** Source control for Cycle, window, base cycle...; interpret in the business definitions and its enclosing section.
- **UI binding:** `search`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setSearch(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:1934](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L1934).

### FRM-032-C009 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:2184](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L2184).

### FRM-032-C010 — draftFilter.startDate &#124;&#124; ""

- **Meaning:** Source control for draftFilter.startDate || ""; interpret in the business definitions and its enclosing section.
- **UI binding:** `draftFilter.startDate &#124;&#124; ""`; component `input`; input hint `date`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) =><br>                  updateDate("startDate", event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:2321](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L2321).

### FRM-032-C011 — draftFilter.endDate &#124;&#124; ""

- **Meaning:** Source control for draftFilter.endDate || ""; interpret in the business definitions and its enclosing section.
- **UI binding:** `draftFilter.endDate &#124;&#124; ""`; component `input`; input hint `date`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => updateDate("endDate", event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:2333](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L2333).

### FRM-032-C012 — effectiveSelectedWardPcode

- **Meaning:** Source control for effectiveSelectedWardPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `effectiveSelectedWardPcode`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `wardsLoading &#124;&#124; wardRows.length === 0`.
- **Change handling:** `handleWardChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3153](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3153).

### FRM-032-C013 — Meter no

- **Meaning:** Source control for Meter no; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.meterNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("meterNo", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3273](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3273).

### FRM-032-C014 — Days / hrs / min

- **Meaning:** Source control for Days / hrs / min; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.sincePreviousReading`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("sincePreviousReading", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3300](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3300).

### FRM-032-C015 — filters.outcome

- **Meaning:** Source control for filters.outcome; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.outcome`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("outcome", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3316](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3316).

### FRM-032-C016 — filters.mediaStatus

- **Meaning:** Source control for filters.mediaStatus; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.mediaStatus`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("mediaStatus", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3336](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3336).

### FRM-032-C017 — Reason

- **Meaning:** Source control for Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.reason`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("reason", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3353](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3353).

### FRM-032-C018 — Current

- **Meaning:** Source control for Current; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.currentReading`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("currentReading", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3367](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3367).

### FRM-032-C019 — Prev

- **Meaning:** Source control for Prev; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.previousReading`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("previousReading", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3383](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3383).

### FRM-032-C020 — Use

- **Meaning:** Source control for Use; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.consumption`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("consumption", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3399](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3399).

### FRM-032-C021 — filters.meterType

- **Meaning:** Source control for filters.meterType; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.meterType`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("meterType", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3413](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3413).

### FRM-032-C022 — Kind

- **Meaning:** Source control for Kind; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.meterKind`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("meterKind", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3430](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3430).

### FRM-032-C023 — Phase

- **Meaning:** Source control for Phase; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.meterPhase`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("meterPhase", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3444](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3444).

### FRM-032-C024 — ERF

- **Meaning:** Source control for ERF; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.erfNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("erfNo", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3458](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3458).

### FRM-032-C025 — Address / ID

- **Meaning:** Source control for Address / ID; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.premiseAddress`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("premiseAddress", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3472](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3472).

### FRM-032-C026 — No

- **Meaning:** Source control for No; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.wardNo`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("wardNo", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3488](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3488).

### FRM-032-C027 — filters.geofence

- **Meaning:** Source control for filters.geofence; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.geofence`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("geofence", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3502](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3502).

### FRM-032-C028 — User

- **Meaning:** Source control for User; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.capturedBy`; component `FilterInput`; input hint `FilterInput`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => updateFilter("capturedBy", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3522](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3522).

### FRM-032-C029 — filters.billingReadiness

- **Meaning:** Source control for filters.billingReadiness; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.billingReadiness`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("billingReadiness", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3536](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3536).

### FRM-032-C030 — filters.reviewStatus

- **Meaning:** Source control for filters.reviewStatus; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.reviewStatus`; component `FilterSelect`; input hint `FilterSelect`.
- **Visibility/prerequisites:** `conditional branch: !isRegistryOpening && mreadRows.length > 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                          updateFilter("reviewStatus", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-176:3558](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadRegistryPage.jsx#L3558).

### FRM-032-C031 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-177:1816](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L1816).

### FRM-032-C032 — effectiveSelectedWardPcode

- **Meaning:** Source control for effectiveSelectedWardPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `effectiveSelectedWardPcode`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!activeLmPcode &#124;&#124; wardsLoading &#124;&#124; wardRows.length === 0`.
- **Change handling:** `handleWardChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-177:2171](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L2171).

### FRM-032-C033 — hasWardSelection ? selectedSessionIdEffective : ""

- **Meaning:** Source control for hasWardSelection ? selectedSessionIdEffective : ""; interpret in the business definitions and its enclosing section.
- **UI binding:** `hasWardSelection ? selectedSessionIdEffective : ""`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!hasWardSelection &#124;&#124;<br>                    sessionsLoading &#124;&#124;<br>                    sessions.length === 0`.
- **Change handling:** `handleSessionChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-177:2225](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L2225).

### FRM-032-C034 — column.placeholder &#124;&#124; column.header

- **Meaning:** Source control for column.placeholder || column.header; interpret in the business definitions and its enclosing section.
- **UI binding:** `tableFilters[column.key] &#124;&#124; ""`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `conditional branch: !rowsOpening; conditional branch: column.filterType === "text"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!canLoadRows &#124;&#124; rowsQuery.isLoading`.
- **Change handling:** `handleTableFilterChange(column.key)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-177:2381](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L2381).

### FRM-032-C035 — tableFilters[column.key] &#124;&#124; "ALL"

- **Meaning:** Source control for tableFilters[column.key] || "ALL"; interpret in the business definitions and its enclosing section.
- **UI binding:** `tableFilters[column.key] &#124;&#124; "ALL"`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: !rowsOpening; conditional branch: column.filterType === "select"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!canLoadRows &#124;&#124; rowsQuery.isLoading`.
- **Change handling:** `handleTableFilterChange(column.key)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-177:2391](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/registries/MreadStagingPage.jsx#L2391).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Owner states this module needs strengthening before production readiness. Automated billing-system integration and full customer billing remain future work. Do not invent an approval button where the page only filters or downloads.

[Download the detailed control inventory (CSV)](reading-staging-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](reading-staging-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
