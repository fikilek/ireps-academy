# Lifecycle Instruction Control — Field Catalogue

Module **FRM-027** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](instruction-control-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/instruction-control-user-manual.md) · [Field catalogue](instruction-control-field-catalogue.md) · [Error register](instruction-control-error-register.md) · [Practical examples](../10-assessments/instruction-control-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Instruction | Reference | Existing lifecycle transaction being managed. | Must be in a state that permits the action. | Synthetic TRN |
| Action | Controlled operation | Reassign/cancel or other supported management action. | Server enforces transitions; rejected/cancelled instructions cannot execute. | Reassign |
| Target and reason | Reference plus text | New responsibility and explanation. | Reason required where the source requires it; select eligible target. | Crew unavailable |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-027-C001 — Reason for reassignment

- **Meaning:** Source control for Reason for reassignment; interpret in the business definitions and its enclosing section.
- **UI binding:** `reason`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!busy`.
- **Change handling:** `setReason`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-008:1425](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/dashboard/control.js#L1425).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Confirm concurrency and the handling of an offline execution submitted after reassignment. Do not silently discard either party’s evidence.

[Download the detailed control inventory (CSV)](instruction-control-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](instruction-control-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
