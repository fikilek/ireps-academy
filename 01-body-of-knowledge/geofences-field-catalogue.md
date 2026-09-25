# Geofence Planning — Field Catalogue

Module **FRM-025** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](geofences-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/geofences-user-manual.md) · [Field catalogue](geofences-field-catalogue.md) · [Error register](geofences-error-register.md) · [Practical examples](../10-assessments/geofences-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Name | Text | Operational name of the planning area. | Required where shown; use a meaningful local identifier. | Training Route West |
| Description | Text | Reason/scope of the boundary. | Explain work-planning purpose, not legal ownership. | September inspections |
| Geometry | Coordinates/polygon | Boundary used for planning. | Valid geometry and scope checks; inspect the rendered shape. | Synthetic polygon |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-025-C001 — Geofence Name

- **Meaning:** Operational name of the planning area.
- **UI binding:** `draftName`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `isCreateMode; showDraftInputs`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setDraftName`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-009:623](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L623).

### FRM-025-C002 — Description

- **Meaning:** Reason/scope of the boundary.
- **UI binding:** `draftDescription`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `isCreateMode; showDraftInputs`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setDraftDescription`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-009:631](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L631).

### FRM-025-C003 — wardPcode

- **Meaning:** Source control for wardPcode; interpret in the business definitions and its enclosing section.
- **UI binding:** `wardPcode`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `wardOptions.length === 0`.
- **Change handling:** `handleWardChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-159:1536](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeoFencesPage.jsx#L1536).

### FRM-025-C004 — geofenceKind

- **Meaning:** Source control for geofenceKind; interpret in the business definitions and its enclosing section.
- **UI binding:** `geofenceKind`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `event => setGeofenceKind(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-159:1561](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeoFencesPage.jsx#L1561).

### FRM-025-C005 — salesCategoryMonth &#124;&#124; ""

- **Meaning:** Source control for salesCategoryMonth || ""; interpret in the business definitions and its enclosing section.
- **UI binding:** `salesCategoryMonth &#124;&#124; ""`; component `input`; input hint `month`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `event => setSalesMonthSelection({ scope: salesScopeKey, month: event.target.value })`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-159:1571](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeoFencesPage.jsx#L1571).

### FRM-025-C006 — e.g. Albert Street

- **Meaning:** Source control for e.g. Albert Street; interpret in the business definitions and its enclosing section.
- **UI binding:** `geofenceNamePart(draftName)`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `conditional branch: createModalOpen; conditional branch: wardNumber`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setDraftName(`${geofenceNamePrefix(wardNumber)}${event.target.value}`)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-167:241](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/geofence-shared-ui.jsx#L241).

### FRM-025-C007 — Select a Ward first

- **Meaning:** Source control for Select a Ward first; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `input`.
- **Visibility/prerequisites:** `conditional branch: createModalOpen; conditional branch: wardNumber`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `true`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-167:249](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/geofence-shared-ui.jsx#L249).

### FRM-025-C008 — Optional description

- **Meaning:** Reason/scope of the boundary.
- **UI binding:** `draftDescription`; component `textarea`; input hint `textarea`.
- **Visibility/prerequisites:** `conditional branch: createModalOpen`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setDraftDescription(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-167:262](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/geofence-shared-ui.jsx#L262).

### FRM-025-C009 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `onChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-160:393](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/GeofencePlanningLayers.jsx#L393).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Geometry validation and role scope are release-specific. Do not interpret a boundary selection as allocation or acceptance of work.

[Download the detailed control inventory (CSV)](geofences-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](geofences-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
