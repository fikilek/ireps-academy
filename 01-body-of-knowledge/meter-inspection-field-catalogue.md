# Meter Inspection — Field Catalogue

Module **FRM-016** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-inspection-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-inspection-user-manual.md) · [Field catalogue](meter-inspection-field-catalogue.md) · [Error register](meter-inspection-error-register.md) · [Practical examples](../10-assessments/meter-inspection-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Captured asset values | Structured object | The current field observation, distinct from baseline. | Service-specific fields and confirmed comparison govern changes. | Updated seal number |
| SAME / changed controls | Choice | Indicate whether each fact matches Existing iREPS. | SAME copies the baseline, including NAv where present; it is not evidence that an unknown fact was observed. | SAME after checking |
| Anomalies | Controlled values plus evidence | As-found conditions requiring attention. | Shared lists and conditional photographs apply. | Synthetic anomaly case |
| Normalisation/action | Controlled choice plus evidence | What was actually corrected or which follow-on is required. | Do not mark a future action as already completed. | Replace meter follow-on |
| Observed state | Controlled selection | Connection state found during inspection. | Current source supports Connected/Disconnected; reconcile against prior state with evidence. | DISCONNECTED |
| Comparison confirmation | Confirmation object | Acknowledgement of changed facts. | Required when detected differences need confirmation. | Confirmed after review |
| Reading and evidence | Structured observation | Reading or a supported reason plus relevant media. | Do not confuse inspection reading with a final billing export. | Synthetic register observation |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-016-C001 — Type the reason

- **Meaning:** Source control for Type the reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `normalisation?.noActionReasonOther &#124;&#124; ""`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `needsReason; normalisation?.noActionReason === NO_ACTION_REASON_OTHER`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                setFieldValue(`${base}.noActionReasonOther`, text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:1294](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L1294).

### FRM-016-C002 — `Enter ${label.toLowerCase()}`

- **Meaning:** Source control for `Enter ${label.toLowerCase()}`; interpret in the business definitions and its enclosing section.
- **UI binding:** `value &#124;&#124; ""`; component `TextInput`; input hint `keyboardType`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => {<br>            if (!String(text &#124;&#124; "").trim()) setCleared(true);<br>            onChangeText(text);<br>          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:2217](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L2217).

### FRM-016-C003 — whyMissing.label

- **Meaning:** Source control for whyMissing.label; interpret in the business definitions and its enclosing section.
- **UI binding:** `whyMissing.value`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `showWhy`.
- **Requirement/options:** `Not established by control prop alone`; `whyMissing.reasons`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `whyMissing.onChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:2265](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L2265).

### FRM-016-C004 — label

- **Meaning:** Source control for label; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:2317](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L2317).

### FRM-016-C005 — Meter Number

- **Meaning:** Source control for Meter Number; interpret in the business definitions and its enclosing section.
- **UI binding:** `astData?.astNo`; component `SameDeleteTextField`; input hint `SameDeleteTextField`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                          setFieldValue(<br>                            "inspection.captured.ast.astData.astNo",<br>                            text,<br>                          )`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:3928](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L3928).

### FRM-016-C006 — Manufacturer

- **Meaning:** Source control for Manufacturer; interpret in the business definitions and its enclosing section.
- **UI binding:** `astData?.astManufacturerSelect`; component `SameDeleteSelectField`; input hint `SameDeleteSelectField`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `manufacturerOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                          setFieldValue(<br>                            "inspection.captured.ast.astData.astManufacturerSelect",<br>                            nextValue,<br>                          );<br>                          setFieldValue(<br>                            "inspection.captured.ast.astData.astManufacturer",<br>                            selectWithOtherToText(nextValue),<br>                          );<br>                        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:3970](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L3970).

### FRM-016-C007 — Meter Model / Name

- **Meaning:** Source control for Meter Model / Name; interpret in the business definitions and its enclosing section.
- **UI binding:** `astData?.astName`; component `SameDeleteTextField`; input hint `SameDeleteTextField`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) =><br>                          setFieldValue(<br>                            "inspection.captured.ast.astData.astName",<br>                            text,<br>                          )`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4018](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4018).

### FRM-016-C008 — Placement

- **Meaning:** Source control for Placement; interpret in the business definitions and its enclosing section.
- **UI binding:** `capturedAst?.location?.placementSelect`; component `SameDeleteSelectField`; input hint `SameDeleteSelectField`.
- **Visibility/prerequisites:** `conditional branch: noAccess; isElectricityInspectionService`.
- **Requirement/options:** `Not established by control prop alone`; `placementLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                              setFieldValue(<br>                                "inspection.captured.ast.location.placementSelect",<br>                                nextValue,<br>                              );<br>                              setFieldValue(<br>                                "inspection.captured.ast.location.placement",<br>                                selectWithOtherToText(nextValue),<br>                              );<br>                            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4155](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4155).

### FRM-016-C009 — Off-grid Supply

- **Meaning:** Source control for Off-grid Supply; interpret in the business definitions and its enclosing section.
- **UI binding:** `capturedAst?.ogs?.hasOffGridSupplySelect`; component `SameDeleteSelectField`; input hint `SameDeleteSelectField`.
- **Visibility/prerequisites:** `conditional branch: noAccess; isElectricityInspectionService`.
- **Requirement/options:** `Not established by control prop alone`; `OFF_GRID_SUPPLY_OPTIONS`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                              setFieldValue(<br>                                "inspection.captured.ast.ogs.hasOffGridSupplySelect",<br>                                nextValue,<br>                              );<br>                              setFieldValue(<br>                                "inspection.captured.ast.ogs.hasOffGridSupply",<br>                                nextValue?.code &#124;&#124;<br>                                  selectWithOtherToText(nextValue),<br>                              );<br>                            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4203](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4203).

### FRM-016-C010 — METER GPS CAPTURE

- **Meaning:** Source control for METER GPS CAPTURE; interpret in the business definitions and its enclosing section.
- **UI binding:** `inspection.captured.ast.location.gps`; component `SovereignLocationPicker`; input hint `SovereignLocationPicker`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `Handled by parent/shared component`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4279](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4279).

### FRM-016-C011 — Meter Anomaly

- **Meaning:** Source control for Meter Anomaly; interpret in the business definitions and its enclosing section.
- **UI binding:** `capturedAst?.anomalies?.anomalySelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `anomalyLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomalySelect",<br>                            nextValue,<br>                          );<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomaly",<br>                            selectWithOtherToText(nextValue),<br>                          );<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomalyDetailSelect",<br>                            makeEmptySelectWithOther(),<br>                          );<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomalyDetail",<br>                            "",<br>                          );<br>                        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4316](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4316).

### FRM-016-C012 — Anomaly Detail

- **Meaning:** Source control for Anomaly Detail; interpret in the business definitions and its enclosing section.
- **UI binding:** `capturedAst?.anomalies?.anomalyDetailSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `anomalyDetailOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomalyDetailSelect",<br>                            nextValue,<br>                          );<br>                          setFieldValue(<br>                            "inspection.captured.ast.anomalies.anomalyDetail",<br>                            selectWithOtherToText(nextValue),<br>                          );<br>                        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4351](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4351).

### FRM-016-C013 — Current Status

- **Meaning:** Source control for Current Status; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.status?.stateSelect`; component `SameDeleteSelectField`; input hint `SameDeleteSelectField`.
- **Visibility/prerequisites:** `conditional branch: noAccess; !noAccess`.
- **Requirement/options:** `Not established by control prop alone`; `foundStatusOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                            setFieldValue("status.stateSelect", nextValue);<br>                            setFieldValue(<br>                              "status.state",<br>                              nextValue?.code &#124;&#124;<br>                                selectWithOtherToText(nextValue),<br>                            );<br>                            setFieldValue(<br>                              "status.id",<br>                              values?.status?.id &#124;&#124;<br>                                values?.accessData?.parents?.lmPcode &#124;&#124;<br>                                "NAv",<br>                            );<br>                            setFieldValue(<br>                              "status.detail",<br>                              values?.status?.detail &#124;&#124;<br>                                values?.accessData?.parents?.lmPcode &#124;&#124;<br>                                "NAv",<br>                            );<br>                          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4448](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4448).

### FRM-016-C014 — Meter Reading

- **Meaning:** Source control for Meter Reading; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.inspection?.captured?.mreading?.reading`; component `TextInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: noAccess; isConventional`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => {<br>                            const cleanText = text.replace(/[^\d.]/g, "");<br>                            setFieldValue(<br>                              "inspection.captured.mreading.reading",<br>                              cleanText,<br>                            );<br><br>                            if (cleanText) {<br>                              setFieldValue(<br>                                "inspection.captured.mreading.readingAt",<br>                                new Date().toISOString(),<br>                              );<br>                              setFieldValue(<br>                                "inspection.captured.mreading.noReadingReason",<br>                                makeEmptySelectWithOther(),<br>                              );<br>                            }<br>                          }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4557](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4557).

### FRM-016-C015 — No Reading Reason

- **Meaning:** Source control for No Reading Reason; interpret in the business definitions and its enclosing section.
- **UI binding:** `values?.inspection?.captured?.mreading<br>                                ?.noReadingReason`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess; isConventional; !String(<br>                          values?.inspection?.captured?.mreading?.reading &#124;&#124; "",<br>                        ).trim()`.
- **Requirement/options:** `Not established by control prop alone`; `noReadingLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) =><br>                              setFieldValue(<br>                                "inspection.captured.mreading.noReadingReason",<br>                                nextValue,<br>                              )`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-025:4630](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/inspection.js#L4630).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

The screen may say a timed-out inspection was NOT sent. A timeout does not prove the server received nothing; this wording is a release-review concern. Current saved-form success is retained with SUCCESS, unlike screens that remove successful queue items. QA corrections and financial effects remain open.

[Download the detailed control inventory (CSV)](meter-inspection-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-inspection-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
