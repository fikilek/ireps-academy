# Meter Disconnection — Field Catalogue

Module **FRM-017** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-disconnection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-disconnection-user-manual.md) · [Field catalogue](meter-disconnection-field-catalogue.md) · [Error register](meter-disconnection-error-register.md) · [Practical examples](../10-assessments/meter-disconnection-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Instruction | Controlled value/reference | The requested disconnection work. | Required; current local instruction list applies. | Synthetic instruction |
| Access | Yes/no with reason | Whether the meter could be reached for this work. | No requires the appropriate reason and noAccessPhoto. | no |
| Disconnection level | Controlled code | What level of disconnection was actually carried out. | Server validates one of three source codes; service-specific applicability needs review. | LEVEL_1_CB_ONLY |
| Level evidence | Media | Proof corresponding to the recorded action. | disconnectionLevelEvidence is the current tag; older draft tag also appears in helper. | Synthetic evidence |
| Origin | Reference object | Links execution to instruction or prior finding. | Must remain consistent with the authorised source and meter. | Synthetic origin TRN |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-017-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>          setFieldValue("accessData.access.hasAccess", nextValue);<br><br>          if (nextValue === "yes") {<br>            setFieldValue("accessData.access.reason", "NAv");<br>            setFieldValue(<br>              "accessData.access.reasonSelect",<br>              makeEmptySelectWithOther(),<br>            );<br>          }<br>        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-024:531](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L531).

### FRM-017-C002 — Disconnection Instruction

- **Meaning:** The requested disconnection work.
- **UI binding:** `values?.assignment?.instructionSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `FIELD_DISCONNECTION_INSTRUCTION_OPTIONS`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                      setFieldValue("assignment.instructionSelect", nextValue);<br>                      setFieldValue(<br>                        "assignment.instruction.text",<br>                        selectWithOtherToText(nextValue),<br>                      );<br>                    }`.
- **Validation:** `object()<br>        .shape({<br>          code: string().notRequired(),<br>          label: string().notRequired(),<br>          otherText: string().notRequired(),<br>        })<br>        .test(<br>          "disconnection-instruction-required",<br>          "Disconnection instruction is required",<br>          (value) => isSelectWithOtherFilled(value),<br>        )`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-024:2118](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L2118).

### FRM-017-C003 — Instruction Notes

- **Meaning:** The requested disconnection work.
- **UI binding:** `values?.assignment?.instruction?.notes &#124;&#124; ""`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                      setFieldValue("assignment.instruction.notes", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-024:2140](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L2140).

### FRM-017-C004 — Level

- **Meaning:** Source control for Level; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.disconnection?.level`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `FIELD_DISCONNECTION_LEVEL_OPTIONS`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) =><br>                          setFieldValue("disconnection.level", nextValue)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-024:2230](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L2230).

### FRM-017-C005 — IrepsFieldCommentSection

- **Meaning:** Source control for IrepsFieldCommentSection; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `IrepsFieldCommentSection`; input hint `IrepsFieldCommentSection`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `inProgress &#124;&#124; saveInProgress`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-024:2274](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/disconnection.jsx#L2274).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

The generic validator accepts water and electricity while its disconnection levels describe circuit-breaker actions. Water-specific teaching and product rules need resolution. Physical work instructions require the utility’s authorised procedure.

[Download the detailed control inventory (CSV)](meter-disconnection-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-disconnection-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
