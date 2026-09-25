# Meter Reconnection — Field Catalogue

Module **FRM-018** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-reconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-reconnection-user-manual.md) · [Field catalogue](meter-reconnection-field-catalogue.md) · [Error register](meter-reconnection-error-register.md) · [Practical examples](../10-assessments/meter-reconnection-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Instruction | Controlled selection/reference | Requested reconnection. | Required; canonical wording Reconnect meter. | Reconnect meter |
| Supply reconnected | Yes/no | Explicit completion confirmation. | Server requires yes for successful execution; a negative answer is not a completed reconnection. | yes |
| Reconnection evidence | Media | Proof of the completed reconnection. | reconnectionEvidence required for success. | Synthetic evidence |
| Access and reason | Yes/no plus controlled reason | Whether the work could be reached. | No Access keeps the prior asset state under the inspected helper. | Meter box locked |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-018-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>          setFieldValue("accessData.access.hasAccess", nextValue);<br><br>          if (nextValue === "yes") {<br>            setFieldValue("accessData.access.reason", "NAv");<br>            setFieldValue(<br>              "accessData.access.reasonSelect",<br>              makeEmptySelectWithOther(),<br>            );<br>          }<br>        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-027:481](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L481).

### FRM-018-C002 — Reconnection Instruction

- **Meaning:** Requested reconnection.
- **UI binding:** `values?.assignment?.instructionSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `FIELD_RECONNECTION_INSTRUCTION_OPTIONS`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                      setFieldValue("assignment.instructionSelect", nextValue);<br>                      setFieldValue(<br>                        "assignment.instruction.text",<br>                        selectWithOtherToText(nextValue),<br>                      );<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-027:1973](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1973).

### FRM-018-C003 — Instruction Notes

- **Meaning:** Requested reconnection.
- **UI binding:** `values?.assignment?.instruction?.notes &#124;&#124; ""`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                      setFieldValue("assignment.instruction.notes", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-027:1995](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L1995).

### FRM-018-C004 — IrepsFieldCommentSection

- **Meaning:** Source control for IrepsFieldCommentSection; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `IrepsFieldCommentSection`; input hint `IrepsFieldCommentSection`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `inProgress &#124;&#124; saveInProgress`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-027:2116](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/reconnection.jsx#L2116).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Do not infer debt clearance, safety clearance or authority solely from the form’s existence. Document the utility-approved prerequisite separately when agreed.

[Download the detailed control inventory (CSV)](meter-reconnection-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-reconnection-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
