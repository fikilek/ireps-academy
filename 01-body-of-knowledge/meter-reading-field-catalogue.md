# Meter Reading — Field Catalogue

Module **FRM-015** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](meter-reading-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/meter-reading-user-manual.md) · [Field catalogue](meter-reading-field-catalogue.md) · [Error register](meter-reading-error-register.md) · [Practical examples](../10-assessments/meter-reading-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Instruction | Controlled selection/reference | Reason for this reading visit. | Server requires a reading instruction; office context must match the accepted instruction. | Scheduled read |
| Reading | Numeric text | Observed conventional register value. | Numeric when supplied; missing value needs a no-reading reason. Preserve display precision; do not assume currency. | 12540.6 |
| Reading time | Timestamp | When the register was observed. | Required for a successful reading; late transmission does not change observation time. | 2026-09-25T08:00:00Z |
| Reading GPS | Coordinates | Device position at capture. | Known meter GPS and reading GPS required; inspected server rejects distance greater than 5 metres (or an uncomputable distance). Confirm location accuracy and release behaviour. | Synthetic co-located point |
| Lower-reading reason | Controlled selection plus explanation | Explains a value below the prior register reading. | Use the source options; investigate rollover/replacement/context rather than assuming negative consumption. | Previous reading incorrect |
| No-reading reason | Controlled selection | Why no usable register value was captured. | Alternative to a reading; not a zero reading. | Display blank |
| Evidence | Media list | Visible register or access/reading exception proof. | meterReadingEvidence for a successful read; follow No Access evidence requirements. | Synthetic register photograph |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-015-C001 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => setFieldValue(answerPath, nextValue)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:741](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L741).

### FRM-015-C002 — Reason / Notes

- **Meaning:** Source control for Reason / Notes; interpret in the business definitions and its enclosing section.
- **UI binding:** `notes`; component `TextInput`; input hint `TextInput`.
- **Visibility/prerequisites:** `value === "no"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => setFieldValue(notesPath, text)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:768](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L768).

### FRM-015-C003 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `RadioButton.Group`; input hint `RadioButton.Group`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>          setFieldValue("accessData.access.hasAccess", nextValue);<br><br>          if (nextValue === "yes") {<br>            setFieldValue("accessData.access.reason", "NAv");<br>            setFieldValue(<br>              "accessData.access.reasonSelect",<br>              makeEmptySelectWithOther(),<br>            );<br>          }<br>        }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:799](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L799).

### FRM-015-C004 — Meter Reading Instruction

- **Meaning:** Reason for this reading visit.
- **UI binding:** `values?.assignment?.instructionSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: instructionLocked`.
- **Requirement/options:** `Not established by control prop alone`; `meterReadingInstructionLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                      setFieldValue("assignment.instructionSelect", nextValue);<br>                      setFieldValue(<br>                        "assignment.instruction.text",<br>                        selectWithOtherToText(nextValue),<br>                      );<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:2422](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L2422).

### FRM-015-C005 — Token Reading

- **Meaning:** Observed conventional register value.
- **UI binding:** `values?.meterReading?.tokenReading`; component `TextInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: noAccess; conditional branch: isPrepaidReading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => {<br>                              const cleanText = text.replace(/[^\d.]/g, "");<br>                              const previousText = String(<br>                                values?.meterReading?.tokenReading &#124;&#124; "",<br>                              ).trim();<br><br>                              setFieldValue(<br>                                "meterReading.tokenReading",<br>                                cleanText,<br>                              );<br><br>                              if (cleanText) {<br>                                setFieldValue(<br>                                  "meterReading.noReadingReason",<br>                                  makeEmptySelectWithOther(),<br>                                );<br>                                setFieldValue(<br>                                  "meterReading.noReadingMode",<br>                                  false,<br>                                );<br>                                stampReadingAtIfNeeded();<br><br>                                if (!previousText) {<br>                                  captureReadingGpsIfNeeded();<br>                                }<br>                              } else {<br>                                setFieldValue("meterReading.readingGps", null);<br>                                setFieldValue(<br>                                  "meterReading.readingVarianceReasonSelect",<br>                                  makeEmptySelectWithOther(),<br>                                );<br>                                setFieldValue(<br>                                  "meterReading.readingVarianceReason",<br>                                  "",<br>                                );<br>                                setCurrentGps(null);<br>                              }<br>                            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:2605](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L2605).

### FRM-015-C006 — Meter Reading

- **Meaning:** Observed conventional register value.
- **UI binding:** `values?.meterReading?.reading`; component `TextInput`; input hint `numeric`.
- **Visibility/prerequisites:** `conditional branch: noAccess; conditional branch: isPrepaidReading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(text) => {<br>                              const cleanText = text.replace(/[^\d.]/g, "");<br>                              const previousText = String(<br>                                values?.meterReading?.reading &#124;&#124; "",<br>                              ).trim();<br><br>                              setFieldValue("meterReading.reading", cleanText);<br><br>                              if (cleanText) {<br>                                if (<br>                                  !isReadingLowerThanPrevious(<br>                                    cleanText,<br>                                    latestSuccessfulReading,<br>                                  )<br>                                ) {<br>                                  setFieldValue(<br>                                    "meterReading.readingVarianceReasonSelect",<br>                                    makeEmptySelectWithOther(),<br>                                  );<br>                                  setFieldValue(<br>                                    "meterReading.readingVarianceReason",<br>                                    "",<br>                                  );<br>                                }<br><br>                                setFieldValue(<br>                                  "meterReading.noReadingReason",<br>                                  makeEmptySelectWithOther(),<br>                                );<br>                                setFieldValue(<br>                                  "meterReading.noReadingMode",<br>                                  false,<br>                                );<br>                                stampReadingAtIfNeeded();<br><br>                                if (!previousText) {<br>                                  captureReadingGpsIfNeeded();<br>                                }<br>                              } else {<br>                                setFieldValue("meterReading.readingGps", null);<br>                                setFieldValue(<br>                                  "meterReading.readingVarianceReasonSelect",<br>                                  makeEmptySelectWithOther(),<br>                                );<br>                                setFieldValue(<br>                                  "meterReading.readingVarianceReason",<br>                                  "",<br>                                );<br>                                setCurrentGps(null);<br>                              }<br>                            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:2674](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L2674).

### FRM-015-C007 — Reason for lower reading

- **Meaning:** Observed conventional register value.
- **UI binding:** `values?.meterReading<br>                                    ?.readingVarianceReasonSelect`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess; conditional branch: isPrepaidReading; lowerReadingRequiresReason`.
- **Requirement/options:** `true`; `LOWER_READING_REASON_OPTIONS`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                                  const normalized =<br>                                    normalizeSelectWithOtherValue(nextValue);<br><br>                                  setFieldValue(<br>                                    "meterReading.readingVarianceReasonSelect",<br>                                    normalized,<br>                                  );<br>                                  setFieldValue(<br>                                    "meterReading.readingVarianceReason",<br>                                    selectWithOtherToText(normalized),<br>                                  );<br>                                }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:2765](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L2765).

### FRM-015-C008 — No Reading Reason

- **Meaning:** Observed conventional register value.
- **UI binding:** `values?.meterReading?.noReadingReason`; component `IrepsSelectWithOther`; input hint `IrepsSelectWithOther`.
- **Visibility/prerequisites:** `conditional branch: noAccess; !String(values?.meterReading?.reading &#124;&#124; "").trim() &&<br>                        !String(<br>                          values?.meterReading?.tokenReading &#124;&#124; "",<br>                        ).trim() &&<br>                        values?.meterReading?.noReadingMode`.
- **Requirement/options:** `Not established by control prop alone`; `noReadingReasonLookup.options`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(nextValue) => {<br>                                setFieldValue(<br>                                  "meterReading.noReadingReason",<br>                                  nextValue,<br>                                );<br><br>                                if (isSelectWithOtherFilled(nextValue)) {<br>                                  stampReadingAtIfNeeded();<br>                                }<br>                              }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-026:2859](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/asts/meter-reading.js#L2859).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Production readiness remains open by owner direction. Do not teach prepaid token capture as accepted MREAD. Validate exact proximity threshold, units, register multipliers and export acceptance on the relevant release.

[Download the detailed control inventory (CSV)](meter-reading-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](meter-reading-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
