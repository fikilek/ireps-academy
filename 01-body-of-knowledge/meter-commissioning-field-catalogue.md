# Meter Commissioning — Field Catalogue

Module **FRM-014** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-commissioning-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-commissioning-user-manual.md) · [Field catalogue](meter-commissioning-field-catalogue.md) · [Error register](meter-commissioning-error-register.md) · [Practical examples](../10-assessments/meter-commissioning-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Vending confirmation | Yes/no plus notes | Prepaid electricity readiness check. | Required for prepaid electricity; yes needs vendingEvidence, no needs explanatory notes. | yes |
| Final switch-on | Yes/no plus notes | Electricity service/energisation confirmation. | Applicable electricity check; yes needs finalSwitchOnEvidence. | yes |
| Keypad issued | Yes/no plus notes | Prepaid keypad handover check. | Required for prepaid electricity; yes needs keypadIssuedEvidence. | no, keypad not yet supplied |
| Water operational | Yes/no plus notes | Water meter/service operation confirmation. | Water only; yes needs waterOperationalEvidence. | yes |
| Water reading/flow | Yes/no plus notes | Confirmation of the applicable water operation check. | Water only; yes needs waterReadingEvidence. | yes |
| Meter identity | Inherited reference | Existing asset being commissioned. | Server requires FIELD and recognised service; cannot commission a different asset by editing the caption. | TRAIN-A01 |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-014-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => setFieldValue(answerPath, nextValue)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:329](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L329).

### FRM-014-C002 — Reason / Notes

- **Meaning:** Source control for Reason / Notes; interpret in the business definitions and its enclosing section.
- **UI binding:** `notes`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `value === "no"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => setFieldValue(notesPath, text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:356](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L356).

### FRM-014-C003 — Confirm vending

- **Meaning:** Source control for Confirm vending; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.commissioning?.vendingConfirmed?.answer`; component `YesNoQuestion`; input hint `YesNoQuestion`.
- **Visibility/prerequisites:** `isPrepaidElectricityMeter`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `string().oneOf(["yes", "no"]).required("Required")<br>string().oneOf(["yes", "no"])`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:1149](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1149).

### FRM-014-C004 — Final switch-on / energisation confirmed

- **Meaning:** Electricity service/energisation confirmation.
- **UI binding:** `values?.commissioning?.finalSwitchOnTested?.answer`; component `YesNoQuestion`; input hint `YesNoQuestion`.
- **Visibility/prerequisites:** `isElectricityMeter`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `string().oneOf(["yes", "no"]).required("Required")<br>string().oneOf(["yes", "no"])`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:1177](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1177).

### FRM-014-C005 — Keypad issued

- **Meaning:** Prepaid keypad handover check.
- **UI binding:** `values?.commissioning?.keypadIssued?.answer`; component `YesNoQuestion`; input hint `YesNoQuestion`.
- **Visibility/prerequisites:** `isPrepaidElectricityMeter`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `string().oneOf(["yes", "no"]).required("Required")<br>string().oneOf(["yes", "no"])`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:1205](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1205).

### FRM-014-C006 — Meter operational / service confirmed

- **Meaning:** Source control for Meter operational / service confirmed; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.commissioning?.waterMeterOperational?.answer`; component `YesNoQuestion`; input hint `YesNoQuestion`.
- **Visibility/prerequisites:** `isWaterMeter`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `string().oneOf(["yes", "no"]).required("Required")<br>string().oneOf(["yes", "no"])`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:1233](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1233).

### FRM-014-C007 — Reading or flow confirmed

- **Meaning:** Source control for Reading or flow confirmed; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.commissioning?.waterReadingOrFlowConfirmed<br>                          ?.answer`; component `YesNoQuestion`; input hint `YesNoQuestion`.
- **Visibility/prerequisites:** `isWaterMeter`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-023:1263](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/commissioning.jsx#L1263).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Current generic lifecycle helper also contains older commissioning logic, but the dedicated callable is the relevant route. Verify the callable/trigger pair and result refresh in the chosen environment.

[Download the detailed control inventory (CSV)](meter-commissioning-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-commissioning-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
