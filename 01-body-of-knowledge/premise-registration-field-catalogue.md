# Premise Registration — Field Catalogue

Module **FRM-010** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](premise-registration-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/premise-registration-user-manual.md) · [Field catalogue](premise-registration-field-catalogue.md) · [Error register](premise-registration-error-register.md) · [Practical examples](../10-assessments/premise-registration-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Property Type | Controlled text | Kind of premises represented; names and unit requirements depend on it. | Current controlled values and repeatability rules apply; changing type reconciles dependent values. | Flat |
| Property name | Text | Name of the block/complex or business where applicable. | Conditional; Commercial and Industrial use Business Name in current work. | Example Court |
| Unit number | Text | Individual unit, preserving leading zeros and suffixes. | Conditional on type and uniqueness/repeatability rules; copying requires checking it. | 03B |
| Property Status | Controlled text | Observed occupancy/status of this premise. | Required; do not substitute connection status. | Occupied |
| Address | Structured text | Suburb, street number, street name and type. | Required fields in the client schema; street name is formatted on input. | 12 Example Street |
| Context | Controlled text | Township or Suburb contextual selection. | Required; explicit yes/no switch maps to these values. | Suburb |
| Position | Latitude/longitude | Confirmed premise position. | Valid coordinates and location confirmation; ERF association is not inferred only from nearest point. | Synthetic map point |
| Media | Evidence list | Images supporting premise identification. | Client conditional photo test; use required tags and check upload acknowledgement. | Synthetic facade photo |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-010-C001 — values.context === "Township"

- **Meaning:** Township or Suburb contextual selection.
- **UI binding:** `values.context === "Township"`; component `Switch`; input hint `Switch`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(v) =><br>                          setFieldValue("context", v ? "Township" : "Suburb")`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1769](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1769).

### FRM-010-C002 — Property Status

- **Meaning:** Observed occupancy/status of this premise.
- **UI binding:** `occupancy.status`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `premiseOccupancySatusOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string()<br>          .oneOf(<br>            [<br>              "Occupied",<br>              "Unoccupied",<br>              "Vandalised",<br>              "Under Construction",<br>              "Dilapidated",<br>              "Accessed",<br>            ],<br>            "Invalid Status",<br>          )<br>          .required("Required")<br>Yup.string()<br>          .oneOf(<br>            [<br>              "Occupied",<br>              "Unoccupied",<br>              "Vandalised",<br>              "Under Construction",<br>              "Dilapidated",<br>              "Accessed",<br>            ],<br>            "Invalid Status",<br>          )`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1778](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1778).

### FRM-010-C003 — Property Type

- **Meaning:** Kind of premises represented; names and unit requirements depend on it.
- **UI binding:** `propertyType.type`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `propertyTypeOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextType) => {<br>                        if (nextType === values?.propertyType?.type) return;<br><br>                        const reconciled = reconcilePropertyTypeChange(nextType);<br>                        setValues(<br>                          {<br>                            ...values,<br>                            propertyType: {<br>                              ...values.propertyType,<br>                              type: nextType,<br>                              name: reconciled.name,<br>                              unitNo: reconciled.unitNo,<br>                            },<br>                          },<br>                          true,<br>                        );<br>                      }`.
- **Validation:** `Yup.string()<br>          .notOneOf(["Select..."], "Please select a property type")<br>          .required("Required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1789](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1789).

### FRM-010-C004 — premiseNameLabel(values?.propertyType?.type)

- **Meaning:** Source control for premiseNameLabel(values?.propertyType?.type); interpret in the business definitions and its enclosing section.
- **UI binding:** `propertyType.name`; component `FormInput`; input hint `default`.
- **Visibility/prerequisites:** `requiresPropertyName(values?.propertyType?.type)`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string().when("type", ([type], schema) =><br>          requiresPropertyName(type)<br>            ? schema.trim().required(`${premiseNameLabel(type)} is mandatory`)<br>            : schema.optional(),<br>        )<br>schema.trim().required(`${premiseNameLabel(type)} is mandatory`)`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1817](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1817).

### FRM-010-C005 — Unit Number

- **Meaning:** Individual unit, preserving leading zeros and suffixes.
- **UI binding:** `propertyType.unitNo`; component `FormInput`; input hint `default`.
- **Visibility/prerequisites:** `supportsUnitNo(values?.propertyType?.type)`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string().when("type", {<br>          is: (val) => requiresUnitNo(val, unitNoValidationContext),<br>          then: (schema) => schema.trim().required("Unit No is mandatory"),<br>          otherwise: (schema) => schema.optional(),<br>        })`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1830](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1830).

### FRM-010-C006 — SUBURB NAME

- **Meaning:** Source control for SUBURB NAME; interpret in the business definitions and its enclosing section.
- **UI binding:** `address.suburbName`; component `FormInput`; input hint `default`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string().trim().required("Mandatory")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1852](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1852).

### FRM-010-C007 — STR NO

- **Meaning:** Source control for STR NO; interpret in the business definitions and its enclosing section.
- **UI binding:** `address.strNo`; component `FormInput`; input hint `default`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string().trim().required("Mandatory")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1864](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1864).

### FRM-010-C008 — STR NAME

- **Meaning:** Source control for STR NAME; interpret in the business definitions and its enclosing section.
- **UI binding:** `address.strName`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                            setFieldValue(<br>                              "address.strName",<br>                              formatStreetName(text),<br>                            )`.
- **Validation:** `Yup.string().trim().required("Mandatory")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1872](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1872).

### FRM-010-C009 — STREET TYPE

- **Meaning:** Source control for STREET TYPE; interpret in the business definitions and its enclosing section.
- **UI binding:** `address.strType`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `streetTypeOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Yup.string()<br>          .notOneOf(["Select..."], "Please select a street type")<br>          .required("Required")`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-048:1887](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/premises/formPremise.js#L1887).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Current source uses a 10-second premise submit timeout, unlike the proposed universal 15-second policy. Some successful queued submissions remove the local queue item. Cross-batch picker labels can understate server locks; ambiguous multi-meter ERF fallback remains open.

[Download the detailed control inventory (CSV)](premise-registration-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](premise-registration-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
