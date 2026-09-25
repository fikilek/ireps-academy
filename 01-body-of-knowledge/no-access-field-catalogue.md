# No Access — Field Catalogue

Module **FRM-020** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](no-access-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/no-access-user-manual.md) · [Field catalogue](no-access-field-catalogue.md) · [Error register](no-access-error-register.md) · [Practical examples](../10-assessments/no-access-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Has access | Yes/no | Whether the worker can reach the task’s subject. | No changes which task-specific fields apply. | no |
| Reason | Controlled selection | Observed obstacle to access. | Use complete reason; Other requires explanatory text where implemented. | Meter box locked |
| Evidence | Media list | Context for the failed access attempt. | noAccessPhoto appears in lifecycle validators. | Synthetic locked enclosure |
| Work context | References | Task or batch row to which the failed visit belongs. | Do not close an unrelated row or meter task. | TRAIN-ROW02 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-020-C001 — Other NA Reason

- **Meaning:** Observed obstacle to access.
- **UI binding:** `selectedOtherText`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: isOtherSelected`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleOtherTextChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-037:145](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/IrepsNoAccessSection.js#L145).

### FRM-020-C002 — selectedCode

- **Meaning:** Source control for selectedCode; interpret in the business definitions and its enclosing section.
- **UI binding:** `selectedCode`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleReasonChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-037:181](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/IrepsNoAccessSection.js#L181).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Reason lists and evidence rules must be checked per workflow. Row completion and reallocation after No Access are workflow-specific; a generic automatic revisit policy is not approved.

[Download the detailed control inventory (CSV)](no-access-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](no-access-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
