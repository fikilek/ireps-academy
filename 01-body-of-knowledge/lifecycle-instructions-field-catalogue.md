# Lifecycle Instruction Creation — Field Catalogue

Module **FRM-026** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](lifecycle-instructions-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/lifecycle-instructions-user-manual.md) · [Field catalogue](lifecycle-instructions-field-catalogue.md) · [Error register](lifecycle-instructions-error-register.md) · [Practical examples](../10-assessments/lifecycle-instructions-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Transaction type | Controlled code | Action requested for the meter. | Only supported office instruction types; vending is not one of them. | METER_INSPECTION |
| Instruction | Controlled selection | The actual requested work. | Local shared lists under UI-R003; Other handling follows source. | General inspection |
| Notes | Text | Additional factual instruction context. | Do not replace a required controlled instruction with notes. | Check marked enclosure |
| Target | Reference | Assigned eligible user/team. | Assignment validation and organisational scope apply. | Training Team A |
| Meter/premise | References | Subject of the requested work. | Existing records and eligible state required. | TRAIN-A01 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-026-C001 — instructionLookupTitle &#124;&#124; "Instruction"

- **Meaning:** The actual requested work.
- **UI binding:** `instructionSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `true`; `instructionOptions`.
- **Editability:** `busy`.
- **Change handling:** `setInstructionSelect`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-013:845](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L845).

### FRM-026-C002 — Optional notes

- **Meaning:** Additional factual instruction context.
- **UI binding:** `instructionNotes`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!busy`.
- **Change handling:** `setInstructionNotes`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-013:867](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L867).

### FRM-026-C003 — Select User

- **Meaning:** Source control for Select User; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `DynamicTargetPicker`; input hint `DynamicTargetPicker`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `userOptions`.
- **Editability:** `busy`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-013:896](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L896).

### FRM-026-C004 — Search...

- **Meaning:** Source control for Search...; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `setSearchText`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-013:1122](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/trn-origin.js#L1122).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Role inheritance remains open. Field-origin exceptions have separate checks and do not make office acceptance optional for an office-issued instruction.

[Download the detailed control inventory (CSV)](lifecycle-instructions-field-catalogue.csv).
