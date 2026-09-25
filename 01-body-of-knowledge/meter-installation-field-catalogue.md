# Meter Installation — Field Catalogue

Module **FRM-013** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-installation-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-installation-user-manual.md) · [Field catalogue](meter-installation-field-catalogue.md) · [Error register](meter-installation-error-register.md) · [Practical examples](../10-assessments/meter-installation-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Meter number | Text identifier | Identity of the newly installed physical meter. | Current rule removes spaces, uppercases a–z, accepts A–Z and digits only; preserve leading zeros and enforce uniqueness at the server. | 00123456789 |
| Service | Controlled text | Water or electricity being supplied. | Select before service-specific questions; do not infer it from a number. | electricity |
| Meter kind | Controlled text | Prepaid or conventional operation. | Controls credit/reading and keypad sections. | prepaid |
| Manufacturer | Controlled text | Selected make of the installed equipment. | Installation omits Other because no companion make input exists. | Conlog |
| Premise/ERF | References | Served unit and land context. | Must remain associated with the intended installation; position alone is insufficient. | TRAIN-P03 |
| Placement and GPS | Controlled text plus coordinates | Actual physical meter position. | Valid GPS and confirmation; may differ from served-premise position. | Boundary Wall |
| Infrastructure | Structured fields | Applicable seal, breaker, keypad and meter technical characteristics. | Use the shared component catalogue and conditional evidence rules. | Synthetic seal record |
| Origin | System/reference object | Links replacement to its removal and original finding/instruction. | Do not manually invent an origin or close a different meter’s work. | Synthetic removal TRN |
| Evidence | Media list | Proof of meter identity, installation and applicable infrastructure. | Photo tags and uploaded URLs must satisfy the relevant checks. | Synthetic installation photographs |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-013-C001 — Meter Number

- **Meaning:** Identity of the newly installed physical meter.
- **UI binding:** `ast.astData.astNo`; component `FormInputMeterNo`; input hint `FormInputMeterNo`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:167](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L167).

### FRM-013-C002 — MANUFACTURER

- **Meaning:** Selected make of the installed equipment.
- **UI binding:** `ast.astData.astManufacturer`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getOptions("elec_manufacturers")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>              if (isDiscovery && nextValue !== "Other") {<br>                setFieldValue("ast.astData.astManufacturerOther", "", false);<br>              }<br>            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:181](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L181).

### FRM-013-C003 — Other Manufacturer

- **Meaning:** Selected make of the installed equipment.
- **UI binding:** `ast.astData.astManufacturerOther`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `isDiscovery &&<br>            values?.ast?.astData?.astManufacturer === "Other"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:194](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L194).

### FRM-013-C004 — MODEL (NAME)

- **Meaning:** Source control for MODEL (NAME); interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.astName`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:201](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L201).

### FRM-013-C005 — PHASE

- **Meaning:** Source control for PHASE; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.phase`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("meter_phases")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:209](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L209).

### FRM-013-C006 — TYPE

- **Meaning:** Source control for TYPE; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.type`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("meter_types")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>                  if (isDiscovery && nextValue === "conventional") {<br>                    setFieldValue(<br>                      "ast.astData.meter.remainingCredit",<br>                      "",<br>                      false,<br>                    );<br>                    setFieldValue(<br>                      "ast.astData.meter.remainingCreditComment",<br>                      "",<br>                      false,<br>                    );<br>                    setFieldValue(<br>                      "ast.astData.meter.remainingCreditCommentOther",<br>                      "",<br>                      false,<br>                    );<br>                    setFieldValue(<br>                      "media",<br>                      removeRemainingCreditPhoto(values?.media &#124;&#124; []),<br>                      false,<br>                    );<br>                  }<br>                }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:220](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L220).

### FRM-013-C007 — CATEGORY

- **Meaning:** Source control for CATEGORY; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.category`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("meter_categories")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:255](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L255).

### FRM-013-C008 — SEAL NO

- **Meaning:** Source control for SEAL NO; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.seal.sealNo`; component `FormBarcodeInput`; input hint `FormBarcodeInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:282](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L282).

### FRM-013-C009 — Seal Number Comment

- **Meaning:** Source control for Seal Number Comment; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.seal.comment`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `!values?.ast?.astData?.meter?.seal?.sealNo`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("seal_number_comment_reasons")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>                  if (nextValue !== "Other") {<br>                    setFieldValue(<br>                      "ast.astData.meter.seal.commentOther",<br>                      "",<br>                      false,<br>                    );<br>                  }<br>                }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:291](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L291).

### FRM-013-C010 — Other Reason

- **Meaning:** Source control for Other Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.seal.commentOther`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `!values?.ast?.astData?.meter?.seal?.sealNo; values?.ast?.astData?.meter?.seal?.comment === "Other"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:308](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L308).

### FRM-013-C011 — KEYPAD SERIAL NO

- **Meaning:** Source control for KEYPAD SERIAL NO; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.keypad.serialNo`; component `FormBarcodeInput`; input hint `FormBarcodeInput`.
- **Visibility/prerequisites:** `values?.ast?.astData?.meter?.type === "prepaid"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:329](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L329).

### FRM-013-C012 — Keypad Serial Number Comment

- **Meaning:** Source control for Keypad Serial Number Comment; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.keypad.comment`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `values?.ast?.astData?.meter?.type === "prepaid"; !values?.ast?.astData?.meter?.keypad?.serialNo`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("keypad_serial_number_comment_reasons")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>                    if (nextValue !== "Other") {<br>                      setFieldValue(<br>                        "ast.astData.meter.keypad.commentOther",<br>                        "",<br>                        false,<br>                      );<br>                    }<br>                  }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:338](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L338).

### FRM-013-C013 — Other Reason

- **Meaning:** Source control for Other Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.keypad.commentOther`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `values?.ast?.astData?.meter?.type === "prepaid"; !values?.ast?.astData?.meter?.keypad?.serialNo; values?.ast?.astData?.meter?.keypad?.comment === "Other"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:355](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L355).

### FRM-013-C014 — CB SIZE (AMPS)

- **Meaning:** Source control for CB SIZE (AMPS); interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.cb.size`; component `FormInput`; input hint `numeric`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:375](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L375).

### FRM-013-C015 — CB Comment

- **Meaning:** Source control for CB Comment; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.cb.comment`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `!values?.ast?.astData?.meter?.cb?.size`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("cb_comment_reasons")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>                  if (nextValue !== "Other") {<br>                    setFieldValue(<br>                      "ast.astData.meter.cb.commentOther",<br>                      "",<br>                      false,<br>                    );<br>                  }<br>                }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:383](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L383).

### FRM-013-C016 — Other Reason

- **Meaning:** Source control for Other Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.cb.commentOther`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `!values?.ast?.astData?.meter?.cb?.size; values?.ast?.astData?.meter?.cb?.comment === "Other"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:400](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L400).

### FRM-013-C017 — Meter Placement

- **Meaning:** Source control for Meter Placement; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.location.placement`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("placements")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:420](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L420).

### FRM-013-C018 — Meter GPS Position

- **Meaning:** Source control for Meter GPS Position; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.location.gps`; component `SovereignLocationPicker`; input hint `SovereignLocationPicker`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:426](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L426).

### FRM-013-C019 — METER STATUS

- **Meaning:** Source control for METER STATUS; interpret in the business definitions and its enclosing section.
- **UI binding:** `status.state`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `isDiscovery`.
- **Requirement/options:** `Not established by control prop alone`; `getOptions("meter_statuses")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:443](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L443).

### FRM-013-C020 — OFF-GRID SUPPLY?

- **Meaning:** Source control for OFF-GRID SUPPLY?; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.ogs.hasOffGridSupply`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("off_grid_supply")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:450](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L450).

### FRM-013-C021 — Type the reason

- **Meaning:** Source control for Type the reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.normalisation.noActionReasonOther`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `showNormalisation; needsReason; values?.ast?.normalisation?.noActionReason ===<br>                NO_ACTION_REASON_OTHER`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-035:566](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/ElectricitySections.js#L566).

### FRM-013-C022 — Meter Number

- **Meaning:** Identity of the newly installed physical meter.
- **UI binding:** `ast.astData.astNo`; component `FormInputMeterNo`; input hint `FormInputMeterNo`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:34](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L34).

### FRM-013-C023 — Category (Normal/Bulk)

- **Meaning:** Source control for Category (Normal/Bulk); interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.category`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("meter_categories")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:46](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L46).

### FRM-013-C024 — TYPE

- **Meaning:** Source control for TYPE; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.meter.type`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getFormOptions("meter_types")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>            if (isDiscovery && nextValue === "conventional") {<br>              setFieldValue(<br>                "ast.astData.meter.remainingCredit",<br>                "",<br>                false,<br>              );<br>              setFieldValue(<br>                "ast.astData.meter.remainingCreditComment",<br>                "",<br>                false,<br>              );<br>              setFieldValue(<br>                "ast.astData.meter.remainingCreditCommentOther",<br>                "",<br>                false,<br>              );<br>              setFieldValue(<br>                "media",<br>                removeRemainingCreditPhoto(values?.media &#124;&#124; []),<br>                false,<br>              );<br>            }<br>          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:54](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L54).

### FRM-013-C025 — Manufacture

- **Meaning:** Source control for Manufacture; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.astManufacturer`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `getOptions("water_manufacturers")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:86](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L86).

### FRM-013-C026 — Model Name

- **Meaning:** Source control for Model Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.astData.astName`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:92](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L92).

### FRM-013-C027 — Token Reading

- **Meaning:** Source control for Token Reading; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.tokenReading`; component `FormInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: values?.ast?.astData?.meter?.type === "prepaid"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:102](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L102).

### FRM-013-C028 — Meter Reading

- **Meaning:** Source control for Meter Reading; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.meterReading`; component `FormInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: values?.ast?.astData?.meter?.type === "prepaid"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:120](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L120).

### FRM-013-C029 — METER STATUS

- **Meaning:** Source control for METER STATUS; interpret in the business definitions and its enclosing section.
- **UI binding:** `status.state`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `isDiscovery`.
- **Requirement/options:** `Not established by control prop alone`; `getOptions("meter_statuses")`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:152](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L152).

### FRM-013-C030 — METER GPS LOCATION

- **Meaning:** Source control for METER GPS LOCATION; interpret in the business definitions and its enclosing section.
- **UI binding:** `ast.location.gps`; component `SovereignLocationPicker`; input hint `SovereignLocationPicker`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-039:179](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/WaterSections.js#L179).

### FRM-013-C031 — Remaining Credit

- **Meaning:** Source control for Remaining Credit; interpret in the business definitions and its enclosing section.
- **UI binding:** `RC_NAME`; component `FormInput`; input hint `Platform.OS === "ios" ? "numbers-and-punctuation" : "numeric"`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `handleCreditChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-038:61](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/RemainingCreditSection.js#L61).

### FRM-013-C032 — Reason Remaining Credit Could Not Be Captured

- **Meaning:** Source control for Reason Remaining Credit Could Not Be Captured; interpret in the business definitions and its enclosing section.
- **UI binding:** `RCC_NAME`; component `FormSelect`; input hint `FormSelect`.
- **Visibility/prerequisites:** `conditional branch: !hasCredit`.
- **Requirement/options:** `Not established by control prop alone`; `getOptions("remaining_credit_comment_reasons")`.
- **Editability:** `disabled`.
- **Change handling:** `(nextValue) => {<br>              if (nextValue !== "Other") {<br>                setFieldValue(RCC_OTHER_NAME, "", false);<br>              }<br>            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-038:75](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/RemainingCreditSection.js#L75).

### FRM-013-C033 — Specify Other Reason

- **Meaning:** Source control for Specify Other Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `RCC_OTHER_NAME`; component `FormInput`; input hint `FormInput`.
- **Visibility/prerequisites:** `conditional branch: !hasCredit; isOtherReason`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-038:88](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/RemainingCreditSection.js#L88).

### FRM-013-C034 — Add a general field comment...

- **Meaning:** Source control for Add a general field comment...; interpret in the business definitions and its enclosing section.
- **UI binding:** `commentValue`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!disabled`.
- **Change handling:** `(nextValue) => setFieldValue(commentName, nextValue)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-036:690](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/components/forms/IrepsFieldCommentSection.js#L690).

### FRM-013-C035 — METER NUMBER

- **Meaning:** Identity of the newly installed physical meter.
- **UI binding:** `ast.astData.astNo`; component `FormInputMeterNo`; input hint `FormInputMeterNo`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `disabled`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-043:59](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/meters/WaterMeterEntry.js#L59).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Store custody and purchase evidence are lifecycle requirements, not current enforced installation fields. Confirm offline recovery and replacement linking on the target release. Backend and phone branches must be paired.

[Download the detailed control inventory (CSV)](meter-installation-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-installation-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
