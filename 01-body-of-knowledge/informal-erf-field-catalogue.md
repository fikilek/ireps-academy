# Informal ERF Capture — Field Catalogue

Module **FRM-012** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](informal-erf-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/informal-erf-user-manual.md) · [Field catalogue](informal-erf-field-catalogue.md) · [Error register](informal-erf-error-register.md) · [Practical examples](../10-assessments/informal-erf-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Boundary points | Array of coordinates | Drawn operational boundary. | At least 3 valid unique latitude/longitude points; source rounds comparison to 7 decimal places. | Synthetic polygon |
| Reason | Controlled code | Why a usable formal ERF was not selected. | One of the listed creation reasons; Other needs text. | NO_FORMAL_ERF |
| Other reason | Text | Explanation for an unlisted reason. | Required when reason is OTHER. | Survey layer absent in this training area |
| Evidence | Media list | Context supporting the capture. | Follow the current form/controller evidence requirements. | Synthetic area image |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-012-C001 — INFORMAL ERF BOUNDARY

- **Meaning:** Source control for INFORMAL ERF BOUNDARY; interpret in the business definitions and its enclosing section.
- **UI binding:** `boundaryPoints`; component `InformalErfLocationPicker`; input hint `InformalErfLocationPicker`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-041:651](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L651).

### FRM-012-C002 — OTHER CREATION REASON

- **Meaning:** Why a usable formal ERF was not selected.
- **UI binding:** `values?.reasonOther`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `conditional branch: values?.reasonCode === "OTHER"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) =><br>                        setFieldValue("reasonOther", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-041:691](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L691).

### FRM-012-C003 — values?.reasonCode

- **Meaning:** Why a usable formal ERF was not selected.
- **UI binding:** `values?.reasonCode`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `async (reasonCode) => {<br>                        await setValues(<br>                          {<br>                            ...values,<br>                            reasonCode,<br>                            reasonOther:<br>                              reasonCode === "OTHER" ? values.reasonOther : "",<br>                          },<br>                          true,<br>                        );<br><br>                        setReasonModalVisible(false);<br>                      }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-041:761](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L761).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Operational geometry must not be described as cadastral proof. Confirm overlap handling, queue recovery and server validation on the intended release.

[Download the detailed control inventory (CSV)](informal-erf-field-catalogue.csv).
