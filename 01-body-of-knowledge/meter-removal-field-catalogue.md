# Meter Removal — Field Catalogue

Module **FRM-019** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-removal-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-removal-user-manual.md) · [Field catalogue](meter-removal-field-catalogue.md) · [Error register](meter-removal-error-register.md) · [Practical examples](../10-assessments/meter-removal-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Instruction | Controlled choice | Standalone removal or replacement intention. | Current wording distinguishes Remove meter and Replace meter; retired wording must not drive new training. | Replace meter |
| Final reading | Numeric text | Conventional register observed before removal. | Reading or supported no-reading reason; required evidence when captured. | 12540.6 |
| Remaining credit | Numeric text | Prepaid credit observation before removal. | Do not call it consumption or promise a refund; photo/reason requirements apply. | 23.4 in displayed unit |
| Removal confirmation | Confirmation | Asserts the meter was actually removed. | Source success requires confirmation and removalEvidence. | Confirmed |
| No-reading reason | Controlled value | Explains unavailable reading/credit observation. | Record actual reason; zero is not a substitute. | Display damaged |
| Origin/follow-on | References | Links the old meter’s removal to finding and replacement. | Keep old and new AST/TRN identifiers distinct. | Synthetic replacement chain |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-019-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>          setFieldValue("accessData.access.hasAccess", nextValue);<br><br>          if (nextValue === "yes") {<br>            setFieldValue("accessData.access.reason", "NAv");<br>            setFieldValue(<br>              "accessData.access.reasonSelect",<br>              makeEmptySelectWithOther(),<br>            );<br>          }<br>        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-028:542](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L542).

### FRM-019-C002 — Removal Instruction

- **Meaning:** Standalone removal or replacement intention.
- **UI binding:** `values?.assignment?.instructionSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `removalInstructionLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                      setFieldValue("assignment.instructionSelect", nextValue);<br>                      setFieldValue(<br>                        "assignment.instruction.text",<br>                        selectWithOtherToText(nextValue),<br>                      );<br>                    }`.
- **Validation:** `object()<br>        .shape({<br>          code: string().notRequired(),<br>          label: string().notRequired(),<br>          otherText: string().notRequired(),<br>        })<br>        .test(<br>          "removal-instruction-required",<br>          "Removal instruction is required",<br>          (value) => isSelectWithOtherFilled(value),<br>        )`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-028:2195](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L2195).

### FRM-019-C003 — Instruction Notes

- **Meaning:** Standalone removal or replacement intention.
- **UI binding:** `values?.assignment?.instruction?.notes &#124;&#124; ""`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                      setFieldValue("assignment.instruction.notes", text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-028:2221](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L2221).

### FRM-019-C004 — isPrepaidReading ? "Remaining Credit" : "Meter Reading"

- **Meaning:** Prepaid credit observation before removal.
- **UI binding:** `(isPrepaidReading<br>                            ? values?.removal?.tokenReading<br>                            : values?.removal?.meterReading) &#124;&#124; ""`; component `TextInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => {<br>                          const clean = text.replace(/[^\d.]/g, "");<br>                          // A reading and a reason never go together.<br>                          if (clean) {<br>                            setFieldValue(<br>                              "removal.noReadingReason",<br>                              makeEmptySelectWithOther(),<br>                            );<br>                          }<br>                          setFieldValue(<br>                            isPrepaidReading<br>                              ? "removal.tokenReading"<br>                              : "removal.meterReading",<br>                            clean,<br>                          );<br>                        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-028:2350](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L2350).

### FRM-019-C005 — isPrepaidReading<br>                              ? "Reason Remaining Credit Could Not Be Captured"<br>                              : "No Reading Reason"

- **Meaning:** Prepaid credit observation before removal.
- **UI binding:** `values?.removal?.noReadingReason`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess; conditional branch: String(<br>                        (isPrepaidReading<br>                          ? values?.removal?.tokenReading<br>                          : values?.removal?.meterReading) &#124;&#124; "",<br>                      ).trim()`.
- **Requirement/options:** `Not established by control prop alone`; `(isPrepaidReading<br>                              ? REMAINING_CREDIT_REASON_LOOKUP<br>                              : noReadingReasonLookup<br>                            ).options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) =><br>                            setFieldValue("removal.noReadingReason", nextValue)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-028:2405](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/removal.jsx#L2405).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Current removal helper retains older answer/notes shapes alongside the updated confirmation UI. Decommissioned is also a legacy state guard. A single retirement/disposal policy and a stores return form are not established.

[Download the detailed control inventory (CSV)](meter-removal-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-removal-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
