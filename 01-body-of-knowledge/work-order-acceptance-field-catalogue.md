# My Work Orders and Acceptance — Field Catalogue

Module **FRM-028** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](work-order-acceptance-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/work-order-acceptance-user-manual.md) · [Field catalogue](work-order-acceptance-field-catalogue.md) · [Error register](work-order-acceptance-error-register.md) · [Practical examples](../10-assessments/work-order-acceptance-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Work item | Reference | The instruction or batch being accepted. | Check type as well as identifier. | Training batch |
| Decision | Controlled action | Acceptance or refusal. | Do not accept an unrelated item to bypass a lock. | Accept |
| Reason | Text/selection | Explanation where refusal/reversal requires it. | Follow the specific mutation’s validation. | Outside assigned work area |
| Premise selection | Reference | Individual premise associated with a Sales row. | Same-batch row locks and server cross-batch checks apply. | Flat 2 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-028-C001 — Search meter no., ERF or street

- **Meaning:** Source control for Search meter no., ERF or street; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onSearchTextChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-010:4776](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/my-workorders.js#L4776).

### FRM-028-C002 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `values.rejectReason`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!busy && !isSubmitting`.
- **Change handling:** `handleChange("rejectReason")`.
- **Validation:** `string()<br>    .trim()<br>    .min(5, "Give a short but useful reason")<br>    .max(500, "Keep the reason below 500 characters")<br>    .required("Reject reason is required")<br>string()<br>    .trim()<br>    .min(5, "Give a short but useful reason")<br>    .max(500, "Keep the reason below 500 characters")<br>string()<br>    .trim()<br>    .min(5, "Give a short but useful reason")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-010:5904](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/my-workorders.js#L5904).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

A wrong association has backend capabilities but may lack a phone correction interface. Cross-batch Not joined labels may be misleading; server refusal remains authoritative.

[Download the detailed control inventory (CSV)](work-order-acceptance-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](work-order-acceptance-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
