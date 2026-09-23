# Meter Discover — field catalogue

**MDIS · version 0.1 · source-based review draft.** This catalogue covers the inspected discovery form's named inputs, composite media input, generated context and batch payload context. It distinguishes UI helpers from canonical fields. Every reference is to the [source baseline](../00-academy-governance/source-assessments/meter-discover-source-baseline-2026-09-23.md); backend validation references use the normalisation feature snapshot unless marked otherwise.

Read [the Body of Knowledge](meter-discover-body-of-knowledge.md) first. Use the [manual](../02-user-manual/mobile/meter-discover-user-manual.md) for task sequence and the [error register](meter-discover-error-register.md) for recovery. The same records are available in the [CSV catalogue](meter-discover-field-catalogue.csv).

Types describe the application's payload representation, not a claim that every layer rejects every other JavaScript type. Numeric keyboards and string-presence validation are weaker than a numeric business rule. Examples are synthetic and must not be submitted to a live utility.

## Index

| ID | Field | Group | Type |
| --- | --- | --- | --- |
| [MD-F001](#md-f001) | Access outcome | Visit | enum string |
| [MD-F002](#md-f002) | No Access reason | Visit | string |
| [MD-F003](#md-f003) | Service / mission | Visit | enum string |
| [MD-F004](#md-f004) | Meter number | Identity | string |
| [MD-F005](#md-f005) | Manufacturer | Identity | string / selected value |
| [MD-F006](#md-f006) | Other manufacturer | Identity | string, form helper |
| [MD-F007](#md-f007) | Model / name | Identity | string |
| [MD-F008](#md-f008) | Phase | Identity | enum string |
| [MD-F009](#md-f009) | Meter subtype | Identity | enum string |
| [MD-F010](#md-f010) | Meter category | Identity | enum string |
| [MD-F011](#md-f011) | Placement | Location | enum string |
| [MD-F012](#md-f012) | Meter GPS | Location | object {lat: number, lng: number} |
| [MD-F013](#md-f013) | Meter status | State | enum string |
| [MD-F014](#md-f014) | Seal number | Equipment | string |
| [MD-F015](#md-f015) | Seal comment | Equipment | enum string or canonical free text |
| [MD-F016](#md-f016) | Seal Other reason | Equipment | string, form helper |
| [MD-F017](#md-f017) | Keypad number | Equipment | string |
| [MD-F018](#md-f018) | Keypad comment | Equipment | enum string or canonical free text |
| [MD-F019](#md-f019) | Keypad Other reason | Equipment | string, form helper |
| [MD-F020](#md-f020) | Circuit breaker size (amps) | Equipment | string |
| [MD-F021](#md-f021) | Circuit breaker comment | Equipment | enum string or canonical free text |
| [MD-F022](#md-f022) | Circuit breaker Other reason | Equipment | string, form helper |
| [MD-F023](#md-f023) | Water meter reading | Readings | string |
| [MD-F024](#md-f024) | Water token reading | Readings | string |
| [MD-F025](#md-f025) | Remaining credit | Readings | signed decimal string |
| [MD-F026](#md-f026) | Remaining credit reason | Readings | string |
| [MD-F027](#md-f027) | Other remaining credit reason | Readings | string, form helper |
| [MD-F028](#md-f028) | Primary finding / anomaly | Findings | enum string |
| [MD-F029](#md-f029) | Finding detail | Findings | enum string |
| [MD-F030](#md-f030) | Other anomalies | Findings | array<string> |
| [MD-F031](#md-f031) | Off-grid supply | Findings | enum string |
| [MD-F032](#md-f032) | Normalisation actions | Response | array<string> |
| [MD-F033](#md-f033) | Reason for not acting | Response | string |
| [MD-F034](#md-f034) | Other no-action reason | Response | string, form helper |
| [MD-F035](#md-f035) | Field comment | Commentary | string |
| [MD-F036](#md-f036) | Tagged media | Evidence | array<object> |
| [MD-F037](#md-f037) | id | System | string |
| [MD-F038](#md-f038) | accessData.trnType | System | string |
| [MD-F039](#md-f039) | meterDiscoveryContractVersion | System | number |
| [MD-F040](#md-f040) | ERF document identity | System | string |
| [MD-F041](#md-f041) | Human-facing ERF number | System | string |
| [MD-F042](#md-f042) | countryPcode | System | string |
| [MD-F043](#md-f043) | provincePcode | System | string |
| [MD-F044](#md-f044) | dmPcode | System | string |
| [MD-F045](#md-f045) | lmPcode | System | string |
| [MD-F046](#md-f046) | wardPcode | System | string |
| [MD-F047](#md-f047) | Premise id | System | string |
| [MD-F048](#md-f048) | Premise address | System | string |
| [MD-F049](#md-f049) | Premise propertyType | System | string |
| [MD-F050](#md-f050) | Service provider id | System | string |
| [MD-F051](#md-f051) | Service provider name | System | string |
| [MD-F052](#md-f052) | Status id | System | string |
| [MD-F053](#md-f053) | Status detail | System | string |
| [MD-F054](#md-f054) | createdAt | System | ISO timestamp string |
| [MD-F055](#md-f055) | createdByUid | System | string |
| [MD-F056](#md-f056) | createdByUser | System | string |
| [MD-F057](#md-f057) | updatedAt | System | ISO timestamp string |
| [MD-F058](#md-f058) | updatedByUid | System | string |
| [MD-F059](#md-f059) | updatedByUser | System | string |
| [MD-F060](#md-f060) | sourceModule | Batch context | string or null |
| [MD-F061](#md-f061) | operationType | Batch context | string or null |
| [MD-F062](#md-f062) | tbId | Batch context | string or null |
| [MD-F063](#md-f063) | rowId | Batch context | string or null |
| [MD-F064](#md-f064) | rowNo | Batch context | positive integer or null |
| [MD-F065](#md-f065) | salesDocId | Batch context | string or null |
| [MD-F066](#md-f066) | erfId | Batch context | string or null |
| [MD-F067](#md-f067) | premiseId | Batch context | string or null |
| [MD-F068](#md-f068) | targetedMeterNo | Batch context | string or null |
| [MD-F069](#md-f069) | meterNo | Batch context | string or null |
| [MD-F070](#md-f070) | returnTo | Batch context | string or null |
| [MD-F071](#md-f071) | accountNumber | Batch context | string or null |
| [MD-F072](#md-f072) | customerName | Batch context | string or null |
| [MD-F073](#md-f073) | sourceAddress.addressLine1 | Batch context | string or null |
| [MD-F074](#md-f074) | sourceAddress.town | Batch context | string or null |
| [MD-F075](#md-f075) | Source module | Batch context | string |

<a id="md-f001"></a>

## MD-F001 — Access outcome

- **Meaning:** Whether the worker can access the meter for capture.
- **Form/context path:** accessData.access.hasAccess.
- **Data type:** enum string.
- **Prerequisite and requirement:** All visits; set by entry action.
- **Validation and dependencies:** Exactly yes or no; No Access changes the schema and suppresses asset capture.
- **Initial/default value:** From entry action; not a boolean.
- **Canonical storage / transformation:** Same payload path.
- **Evidence:** None specifically required.
- **Synthetic example:** yes.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f002"></a>

## MD-F002 — No Access reason

- **Meaning:** Why the attempted visit could not inspect the meter.
- **Form/context path:** accessData.access.reason.
- **Data type:** string.
- **Prerequisite and requirement:** No Access; required.
- **Validation and dependencies:** Approved local choices; Other must have explanation. Server requires nonempty text; form rejects bare Other.
- **Initial/default value:** Blank on No Access; NAv in accessed initial form.
- **Canonical storage / transformation:** Same path; Other represented with explanatory text.
- **Evidence:** noAccessPhoto.
- **Synthetic example:** Property Locked.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f003"></a>

## MD-F003 — Service / mission

- **Meaning:** Which service is being discovered or whether this is a No Access visit.
- **Form/context path:** meterType.
- **Data type:** enum string.
- **Prerequisite and requirement:** All submissions; inherited from entry selection.
- **Validation and dependencies:** electricity or water when accessed; NA when No Access.
- **Initial/default value:** Entry action; fallback electricity in draft hydration.
- **Canonical storage / transformation:** Same root path.
- **Evidence:** None specifically required.
- **Synthetic example:** water.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f004"></a>

## MD-F004 — Meter number

- **Meaning:** Serial/identifier of the actual meter; leading zeros matter.
- **Form/context path:** ast.astData.astNo.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Remove all whitespace; uppercase ASCII a-z; allow only A-Z and 0-9. Local duplicate warning uses loaded data; backend master checks remain authoritative. Do not guess unreadable numbers.
- **Initial/default value:** Blank; electricity batch route can prefill targetedMeterNo.
- **Canonical storage / transformation:** Same path; normalised identity also keys meter_master.
- **Evidence:** astNoPhoto.
- **Synthetic example:** 00AB123456.
- **Evidence references:** MD-S01; MD-S11; MD-S16; MD-S51.

<a id="md-f005"></a>

## MD-F005 — Manufacturer

- **Meaning:** Manufacturer shown on the physical equipment.
- **Form/context path:** ast.astData.astManufacturer.
- **Data type:** string / selected value.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Required. Electricity Other requires custom text which replaces Other before transmission. Water offers Other but has no equivalent helper in the reviewed component: unresolved mismatch.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Custom electricity manufacturer replaces literal Other.
- **Evidence:** Meter identity photograph.
- **Synthetic example:** Conlog.
- **Evidence references:** MD-S01; MD-S02; MD-S03; MD-S41.

<a id="md-f006"></a>

## MD-F006 — Other manufacturer

- **Meaning:** Manufacturer absent from electricity list.
- **Form/context path:** ast.astData.astManufacturerOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Electricity when Manufacturer = Other; required.
- **Validation and dependencies:** Trimmed nonempty text.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into ast.astData.astManufacturer; helper deleted.
- **Evidence:** Meter identity photograph.
- **Synthetic example:** Example Meter Works.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f007"></a>

## MD-F007 — Model / name

- **Meaning:** Model/name printed on meter.
- **Form/context path:** ast.astData.astName.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Required for water; required after manufacturer is chosen for electricity. No product-wide model enumeration is asserted.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** Meter identity photograph.
- **Synthetic example:** MODEL-X.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f008"></a>

## MD-F008 — Phase

- **Meaning:** Electricity phase category.
- **Form/context path:** ast.astData.meter.phase.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed electricity discovery; required.
- **Validation and dependencies:** single or three.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** single.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f009"></a>

## MD-F009 — Meter subtype

- **Meaning:** Prepaid or conventional metering.
- **Form/context path:** ast.astData.meter.type.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** prepaid or conventional. Switching to conventional clears remaining-credit inputs and removes its photo.
- **Initial/default value:** Water conventional; electricity blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** Dependent evidence below.
- **Synthetic example:** prepaid.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f010"></a>

## MD-F010 — Meter category

- **Meaning:** Normal or bulk classification.
- **Form/context path:** ast.astData.meter.category.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Exactly Normal or Bulk. Selecting Bulk alone does not define a network hierarchy or customer-billing arrangement.
- **Initial/default value:** Water Normal; electricity blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** Normal.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f011"></a>

## MD-F011 — Placement

- **Meaning:** Physical mounting/location category.
- **Form/context path:** ast.location.placement.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed electricity discovery; required.
- **Validation and dependencies:** Eight controlled options listed below. Other has no dedicated explanation control; use Field Comment.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** Context photo may be added; no dedicated placement tag.
- **Synthetic example:** Kiosk.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f012"></a>

## MD-F012 — Meter GPS

- **Meaning:** Confirmed physical meter position.
- **Form/context path:** ast.location.gps.
- **Data type:** object {lat: number, lng: number}.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Finite coordinates, latitude -90..90, longitude -180..180, not 0/0. Validator uses numeric conversion. No parcel-containment or accuracy threshold is enforced here.
- **Initial/default value:** Null until confirmation; map can initialise at premise centroid.
- **Canonical storage / transformation:** Same path.
- **Evidence:** Map pin is separate from media GPS.
- **Synthetic example:** {lat: -26.20, lng: 28.04}; synthetic only.
- **Evidence references:** MD-S01; MD-S47; MD-S41.

<a id="md-f013"></a>

## MD-F013 — Meter status

- **Meaning:** Connection state observed during discovery.
- **Form/context path:** status.state.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** CONNECTED or DISCONNECTED; neither a QA verdict nor Sales visibility.
- **Initial/default value:** Null.
- **Canonical storage / transformation:** Root status.state; projected to asset.
- **Evidence:** None specifically required.
- **Synthetic example:** CONNECTED.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f014"></a>

## MD-F014 — Seal number

- **Meaning:** Identifier read from the associated equipment.
- **Form/context path:** ast.astData.meter.seal.sealNo.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed electricity discovery; value OR comment required.
- **Validation and dependencies:** A nonempty value requires its tagged photo. Comments are alternatives to a missing value, not substitutes for reading a visible identifier.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; nonempty value clears canonical comment.
- **Evidence:** sealPhoto.
- **Synthetic example:** SYN001.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f015"></a>

## MD-F015 — Seal comment

- **Meaning:** Explanation when the associated value could not be captured.
- **Form/context path:** ast.astData.meter.seal.comment.
- **Data type:** enum string or canonical free text.
- **Prerequisite and requirement:** Accessed electricity discovery; required if value blank.
- **Validation and dependencies:** Select approved reason; Other needs explanatory text. Certain reasons require evidence; see matrix. Bare Other rejected by server.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; Other helper becomes the actual explanation.
- **Evidence:** Conditional: sealPhoto.
- **Synthetic example:** Seal Missing.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f016"></a>

## MD-F016 — Seal Other reason

- **Meaning:** Specific reason not covered by list.
- **Form/context path:** ast.astData.meter.seal.commentOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Accessed electricity discovery; required when corresponding value blank and comment = Other.
- **Validation and dependencies:** Trimmed nonempty text.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into ast.astData.meter.seal.comment; helper deleted.
- **Evidence:** No automatic extra photo for custom reason.
- **Synthetic example:** Identifier plate obscured by an unreadable label.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f017"></a>

## MD-F017 — Keypad number

- **Meaning:** Identifier read from the associated equipment.
- **Form/context path:** ast.astData.meter.keypad.serialNo.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed electricity discovery with prepaid subtype; value optional in inspected schema.
- **Validation and dependencies:** A nonempty value requires its tagged photo. Comments are alternatives to a missing value, not substitutes for reading a visible identifier.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; nonempty value clears canonical comment.
- **Evidence:** keypadPhoto.
- **Synthetic example:** SYN001.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f018"></a>

## MD-F018 — Keypad comment

- **Meaning:** Explanation when the associated value could not be captured.
- **Form/context path:** ast.astData.meter.keypad.comment.
- **Data type:** enum string or canonical free text.
- **Prerequisite and requirement:** Accessed electricity discovery with prepaid subtype; optional if value blank.
- **Validation and dependencies:** Select approved reason; Other needs explanatory text. Certain reasons require evidence; see matrix. Bare Other rejected by server.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; Other helper becomes the actual explanation.
- **Evidence:** Conditional: keypadPhoto.
- **Synthetic example:** Keypad Integrated With Meter.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f019"></a>

## MD-F019 — Keypad Other reason

- **Meaning:** Specific reason not covered by list.
- **Form/context path:** ast.astData.meter.keypad.commentOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Accessed electricity discovery with prepaid subtype; required when corresponding value blank and comment = Other.
- **Validation and dependencies:** Trimmed nonempty text.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into ast.astData.meter.keypad.comment; helper deleted.
- **Evidence:** No automatic extra photo for custom reason.
- **Synthetic example:** Identifier plate obscured by an unreadable label.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f020"></a>

## MD-F020 — Circuit breaker size (amps)

- **Meaning:** Recorded circuit-breaker rating; numeric-looking text, no numeric range asserted.
- **Form/context path:** ast.astData.meter.cb.size.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed electricity discovery; value optional in inspected schema.
- **Validation and dependencies:** A nonempty value requires its tagged photo. Comments are alternatives to a missing value, not substitutes for reading a visible identifier.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; nonempty value clears canonical comment.
- **Evidence:** astCbPhoto.
- **Synthetic example:** 60.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f021"></a>

## MD-F021 — Circuit breaker comment

- **Meaning:** Explanation when the associated value could not be captured.
- **Form/context path:** ast.astData.meter.cb.comment.
- **Data type:** enum string or canonical free text.
- **Prerequisite and requirement:** Accessed electricity discovery; optional if value blank.
- **Validation and dependencies:** Select approved reason; Other needs explanatory text. Certain reasons require evidence; see matrix. Bare Other rejected by server.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; Other helper becomes the actual explanation.
- **Evidence:** Conditional: astCbPhoto.
- **Synthetic example:** Circuit Breaker Inaccessible.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f022"></a>

## MD-F022 — Circuit breaker Other reason

- **Meaning:** Specific reason not covered by list.
- **Form/context path:** ast.astData.meter.cb.commentOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Accessed electricity discovery; required when corresponding value blank and comment = Other.
- **Validation and dependencies:** Trimmed nonempty text.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into ast.astData.meter.cb.comment; helper deleted.
- **Evidence:** No automatic extra photo for custom reason.
- **Synthetic example:** Identifier plate obscured by an unreadable label.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f023"></a>

## MD-F023 — Water meter reading

- **Meaning:** Opening/current register observation made at discovery.
- **Form/context path:** ast.meterReading.
- **Data type:** string.
- **Prerequisite and requirement:** Water conventional; required.
- **Validation and dependencies:** Nonempty reading; numeric-oriented UI. Reviewed schema/server validate presence rather than a complete decimal/unit/range contract.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** mreadings[0].reading with readingAt, trnId and source AST_CREATION; removed from ast.
- **Evidence:** meterReadingPhoto.
- **Synthetic example:** 12345.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f024"></a>

## MD-F024 — Water token reading

- **Meaning:** Prepaid water token-reading input shown by this form.
- **Form/context path:** ast.tokenReading.
- **Data type:** string.
- **Prerequisite and requirement:** Water prepaid; required.
- **Validation and dependencies:** Nonempty reading; numeric-oriented UI. Meaning, unit and distinction from remaining credit need owner clarification.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** treadings[0].tokenReading with readingAt, trnId and source AST_CREATION; removed from ast.
- **Evidence:** tokenReadingPhoto.
- **Synthetic example:** 125.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f025"></a>

## MD-F025 — Remaining credit

- **Meaning:** Prepaid balance displayed by meter.
- **Form/context path:** ast.astData.meter.remainingCredit.
- **Data type:** signed decimal string.
- **Prerequisite and requirement:** Accessed prepaid electricity or water discovery; value OR reason required.
- **Validation and dependencies:** Pattern ^[+-]?\d+(?:\.\d+)?$; zero and negative values allowed. No commas, exponent notation or unit suffix. Unit is not specified by this contract.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path on prepaid; removed on conventional.
- **Evidence:** remainingCreditPhoto when value supplied.
- **Synthetic example:** -12.50.
- **Evidence references:** MD-S13; MD-S41.

<a id="md-f026"></a>

## MD-F026 — Remaining credit reason

- **Meaning:** Why the prepaid balance could not be captured.
- **Form/context path:** ast.astData.meter.remainingCreditComment.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed prepaid electricity or water discovery; required only if value blank.
- **Validation and dependencies:** Approved reason or Other with details. Must be blank when value captured; placeholder zero must not replace an unknown value.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; Other canonicalised to Other: followed by text.
- **Evidence:** No remaining-credit photo required when no value.
- **Synthetic example:** Display unreadable.
- **Evidence references:** MD-S13; MD-S41.

<a id="md-f027"></a>

## MD-F027 — Other remaining credit reason

- **Meaning:** Custom explanation for missing balance.
- **Form/context path:** ast.astData.meter.remainingCreditCommentOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Accessed prepaid electricity or water discovery with blank value and reason Other; required.
- **Validation and dependencies:** Trimmed nonempty text.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into remainingCreditComment with Other: prefix; helper deleted.
- **Evidence:** None specifically required.
- **Synthetic example:** Balance screen cannot be reached.
- **Evidence references:** MD-S13; MD-S41.

<a id="md-f028"></a>

## MD-F028 — Primary finding / anomaly

- **Meaning:** Principal observation about meter condition.
- **Form/context path:** ast.anomalies.anomaly.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Select listed finding. Form and server require nonempty text; do not assume backend comprehensively checks every finding/detail pairing.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path; transaction records as-found observation.
- **Evidence:** Conditional anomalyPhoto.
- **Synthetic example:** Meter Faulty.
- **Evidence references:** MD-S01; MD-S04; MD-S10; MD-S41.

<a id="md-f029"></a>

## MD-F029 — Finding detail

- **Meaning:** Specific observation within selected finding.
- **Form/context path:** ast.anomalies.anomalyDetail.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed discovery, electricity or water; required.
- **Validation and dependencies:** Required once finding selected; choose detail associated with it. Water applicability of shared electricity-oriented options remains under review.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** anomalyPhoto for every detail except Operationally Ok.
- **Synthetic example:** Meter Display Blank.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f030"></a>

## MD-F030 — Other anomalies

- **Meaning:** Additional observations alongside primary finding.
- **Form/context path:** ast.anomalies.otherAnomalies.
- **Data type:** array<string>.
- **Prerequisite and requirement:** Accessed electricity/water; optional.
- **Validation and dependencies:** Approved five values; no duplicates. Not a free-text replacement for the principal finding.
- **Initial/default value:** [].
- **Canonical storage / transformation:** Same path, canonical array.
- **Evidence:** No separate evidence tag mandated; explain/evidence relevant finding.
- **Synthetic example:** ["Keypad Faulty"].
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f031"></a>

## MD-F031 — Off-grid supply

- **Meaning:** Recorded presence of off-grid supply at site.
- **Form/context path:** ast.ogs.hasOffGridSupply.
- **Data type:** enum string.
- **Prerequisite and requirement:** Accessed electricity discovery; required.
- **Validation and dependencies:** UI yes/no. Backend checks nonempty value and requires photo when yes; do not infer a full energy-source inventory or capacity field.
- **Initial/default value:** no.
- **Canonical storage / transformation:** Same path.
- **Evidence:** ogsPhoto when yes.
- **Synthetic example:** yes.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f032"></a>

## MD-F032 — Normalisation actions

- **Meaning:** On-site response and/or requested follow-on job.
- **Form/context path:** ast.normalisation.actionTaken.
- **Data type:** array<string>.
- **Prerequisite and requirement:** Accessed electricity discovery; required answer.
- **Validation and dependencies:** Nonempty list; no duplicates; None exclusive; at most one job; expected job omitted requires reason. Mobile preselects expected action on finding change.
- **Initial/default value:** [none], changed with finding.
- **Canonical storage / transformation:** Same path in newer normalisation contract; incompatible action labels exist in older branch.
- **Evidence:** normalisationPhoto for on-site fix; not for job-only choice.
- **Synthetic example:** ["Replace meter"].
- **Evidence references:** MD-S02; MD-S10; MD-S41.

<a id="md-f033"></a>

## MD-F033 — Reason for not acting

- **Meaning:** Why the expected disconnect/replace job was not selected.
- **Form/context path:** ast.normalisation.noActionReason.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed electricity discovery when expected action omitted; required.
- **Validation and dependencies:** Choose reason or Other with text. Reason must be empty when expected job selected or finding needs no job. Current server accepts canonical custom explanation.
- **Initial/default value:** Blank; reset on finding/action changes.
- **Canonical storage / transformation:** Same path; Other replaced with helper text.
- **Evidence:** No dedicated reason-photo tag.
- **Synthetic example:** No meter available to replace.
- **Evidence references:** MD-S02; MD-S10; MD-S41.

<a id="md-f034"></a>

## MD-F034 — Other no-action reason

- **Meaning:** Custom reason for not doing expected work.
- **Form/context path:** ast.normalisation.noActionReasonOther.
- **Data type:** string, form helper.
- **Prerequisite and requirement:** Accessed electricity discovery with reason Other; required.
- **Validation and dependencies:** Trimmed nonempty explanation.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Folded into noActionReason; helper deleted.
- **Evidence:** None specifically required.
- **Synthetic example:** Replacement model unavailable.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f035"></a>

## MD-F035 — Field comment

- **Meaning:** Additional site explanation or unresolved ambiguity.
- **Form/context path:** fieldComment.text.
- **Data type:** string.
- **Prerequisite and requirement:** Every route; optional.
- **Validation and dependencies:** Trimmed text; no maximum length established in inspected discovery schema.
- **Initial/default value:** Blank.
- **Canonical storage / transformation:** Same path.
- **Evidence:** Optional comment media.
- **Synthetic example:** Meter in shared roadside kiosk; serves Unit B.
- **Evidence references:** MD-S01; MD-S08.

<a id="md-f036"></a>

## MD-F036 — Tagged media

- **Meaning:** Pictures/recordings supporting specific fields or commentary.
- **Form/context path:** media.
- **Data type:** array<object>.
- **Prerequisite and requirement:** Every route; particular tags conditionally required.
- **Validation and dependencies:** Required tags below. Server checks nonempty uri or url; several client checks test tag presence only. Upload/quality is a separate concern.
- **Initial/default value:** [].
- **Canonical storage / transformation:** Root media; core meter tags projected to asset; comment media retained with transaction.
- **Evidence:** See complete tag matrix.
- **Synthetic example:** [{tag: astNoPhoto, uri: local-or-remote-path}].
- **Evidence references:** MD-S01; MD-S41; MD-S42; MD-S48; MD-S50.

<a id="md-f037"></a>

## MD-F037 — id

- **Meaning:** Stable identity of this capture; retain on retry.
- **Form/context path:** id.
- **Data type:** string.
- **Prerequisite and requirement:** All new current-client captures; system supplied.
- **Validation and dependencies:** id must start TRN_MDIS_; trnType must equal METER_DISCOVERY. Version is emitted as 2; older payload compatibility remains in server.
- **Initial/default value:** Generated.
- **Canonical storage / transformation:** Same root/nested path.
- **Evidence:** None specifically required.
- **Synthetic example:** TRN_MDIS_<time>_ELC_<ward>_<erf>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f038"></a>

## MD-F038 — accessData.trnType

- **Meaning:** Identifies the transaction operation.
- **Form/context path:** accessData.trnType.
- **Data type:** string.
- **Prerequisite and requirement:** All new current-client captures; system supplied.
- **Validation and dependencies:** id must start TRN_MDIS_; trnType must equal METER_DISCOVERY. Version is emitted as 2; older payload compatibility remains in server.
- **Initial/default value:** Generated.
- **Canonical storage / transformation:** Same root/nested path.
- **Evidence:** None specifically required.
- **Synthetic example:** METER_DISCOVERY.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f039"></a>

## MD-F039 — meterDiscoveryContractVersion

- **Meaning:** Selects current discovery contract / remaining-credit validation.
- **Form/context path:** meterDiscoveryContractVersion.
- **Data type:** number.
- **Prerequisite and requirement:** All new current-client captures; system supplied.
- **Validation and dependencies:** id must start TRN_MDIS_; trnType must equal METER_DISCOVERY. Version is emitted as 2; older payload compatibility remains in server.
- **Initial/default value:** Generated.
- **Canonical storage / transformation:** Same root/nested path.
- **Evidence:** None specifically required.
- **Synthetic example:** 2.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f040"></a>

## MD-F040 — ERF document identity

- **Meaning:** ERF document identity inherited from premise.
- **Form/context path:** accessData.erfId.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; do not manually edit.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** SYNTHETIC-ERF.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f041"></a>

## MD-F041 — Human-facing ERF number

- **Meaning:** Human-facing ERF number inherited from premise.
- **Form/context path:** accessData.erfNo.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; do not manually edit.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** SYNTHETIC-ERF.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f042"></a>

## MD-F042 — countryPcode

- **Meaning:** Geographic scope inherited from parent premise.
- **Form/context path:** accessData.parents.countryPcode.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; verify geography when parent incorrect.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <approved countryPcode>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f043"></a>

## MD-F043 — provincePcode

- **Meaning:** Geographic scope inherited from parent premise.
- **Form/context path:** accessData.parents.provincePcode.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; verify geography when parent incorrect.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <approved provincePcode>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f044"></a>

## MD-F044 — dmPcode

- **Meaning:** Geographic scope inherited from parent premise.
- **Form/context path:** accessData.parents.dmPcode.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; verify geography when parent incorrect.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <approved dmPcode>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f045"></a>

## MD-F045 — lmPcode

- **Meaning:** Geographic scope inherited from parent premise.
- **Form/context path:** accessData.parents.lmPcode.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; verify geography when parent incorrect.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <approved lmPcode>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f046"></a>

## MD-F046 — wardPcode

- **Meaning:** Geographic scope inherited from parent premise.
- **Form/context path:** accessData.parents.wardPcode.
- **Data type:** string.
- **Prerequisite and requirement:** Parent premise selected.
- **Validation and dependencies:** Required nonempty non-NAv for accessed payload; verify geography when parent incorrect.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <approved wardPcode>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f047"></a>

## MD-F047 — Premise id

- **Meaning:** Saved parent premise identity.
- **Form/context path:** accessData.premise.id.
- **Data type:** string.
- **Prerequisite and requirement:** All routes inherit premise context; saved premise gate applies to No Access too.
- **Validation and dependencies:** Accessed payload requires these text fields; callable verifies saved premise exists. Address/type are snapshots, not new editable discovery inputs.
- **Initial/default value:** Inherited / resolved after premise sync.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <premise id>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f048"></a>

## MD-F048 — Premise address

- **Meaning:** Premise address snapshot.
- **Form/context path:** accessData.premise.address.
- **Data type:** string.
- **Prerequisite and requirement:** All routes inherit premise context; saved premise gate applies to No Access too.
- **Validation and dependencies:** Accessed payload requires these text fields; callable verifies saved premise exists. Address/type are snapshots, not new editable discovery inputs.
- **Initial/default value:** Inherited / resolved after premise sync.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <premise address>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f049"></a>

## MD-F049 — Premise propertyType

- **Meaning:** Premise property-type description.
- **Form/context path:** accessData.premise.propertyType.
- **Data type:** string.
- **Prerequisite and requirement:** All routes inherit premise context; saved premise gate applies to No Access too.
- **Validation and dependencies:** Accessed payload requires these text fields; callable verifies saved premise exists. Address/type are snapshots, not new editable discovery inputs.
- **Initial/default value:** Inherited / resolved after premise sync.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <premise propertyType>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f050"></a>

## MD-F050 — Service provider id

- **Meaning:** Provider context resolved from worker organisation toward main contractor.
- **Form/context path:** serviceProvider.id.
- **Data type:** string.
- **Prerequisite and requirement:** User/provider data available.
- **Validation and dependencies:** Required nonempty non-NAv on accessed payload. Form resolution is not proof of a complete authorisation policy.
- **Initial/default value:** Resolved from organisation; fallback may be rejected.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <provider id>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f051"></a>

## MD-F051 — Service provider name

- **Meaning:** Provider context resolved from worker organisation toward main contractor.
- **Form/context path:** serviceProvider.name.
- **Data type:** string.
- **Prerequisite and requirement:** User/provider data available.
- **Validation and dependencies:** Required nonempty non-NAv on accessed payload. Form resolution is not proof of a complete authorisation policy.
- **Initial/default value:** Resolved from organisation; fallback may be rejected.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <provider name>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f052"></a>

## MD-F052 — Status id

- **Meaning:** Municipality identifier for status context.
- **Form/context path:** status.id.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed route.
- **Validation and dependencies:** Generated from parent LM; not worker-selectable connection state.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <LM id>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f053"></a>

## MD-F053 — Status detail

- **Meaning:** Municipality name or identifier.
- **Form/context path:** status.detail.
- **Data type:** string.
- **Prerequisite and requirement:** Accessed route.
- **Validation and dependencies:** Generated from parent LM; not worker-selectable connection state.
- **Initial/default value:** Inherited.
- **Canonical storage / transformation:** Same path.
- **Evidence:** None specifically required.
- **Synthetic example:** <LM detail>.
- **Evidence references:** MD-S01; MD-S41.

<a id="md-f054"></a>

## MD-F054 — createdAt

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.createdAt.
- **Data type:** ISO timestamp string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server createdAt>.
- **Evidence references:** MD-S40.

<a id="md-f055"></a>

## MD-F055 — createdByUid

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.createdByUid.
- **Data type:** string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server createdByUid>.
- **Evidence references:** MD-S40.

<a id="md-f056"></a>

## MD-F056 — createdByUser

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.createdByUser.
- **Data type:** string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server createdByUser>.
- **Evidence references:** MD-S40.

<a id="md-f057"></a>

## MD-F057 — updatedAt

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.updatedAt.
- **Data type:** ISO timestamp string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server updatedAt>.
- **Evidence references:** MD-S40.

<a id="md-f058"></a>

## MD-F058 — updatedByUid

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.updatedByUid.
- **Data type:** string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server updatedByUid>.
- **Evidence references:** MD-S40.

<a id="md-f059"></a>

## MD-F059 — updatedByUser

- **Meaning:** Server-attributed capture audit metadata.
- **Form/context path:** metadata.updatedByUser.
- **Data type:** string.
- **Prerequisite and requirement:** Accepted callable with signed-in caller.
- **Validation and dependencies:** Server discards submitted metadata and supplies its time and authenticated actor. Related master documents use their own Timestamp schema.
- **Initial/default value:** Client provisional, then server supplied.
- **Canonical storage / transformation:** Same path in trns; do not equate local capture time with server receipt time.
- **Evidence:** None specifically required.
- **Synthetic example:** <server updatedByUser>.
- **Evidence references:** MD-S40.

<a id="md-f060"></a>

## MD-F060 — sourceModule

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.sourceModule.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** SALES_TARGETED_BATCH.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f061"></a>

## MD-F061 — operationType

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.operationType.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** METER_DISCOVERY.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f062"></a>

## MD-F062 — tbId

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.tbId.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <batch ID>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f063"></a>

## MD-F063 — rowId

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.rowId.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <row ID>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f064"></a>

## MD-F064 — rowNo

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.rowNo.
- **Data type:** positive integer or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** 3.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f065"></a>

## MD-F065 — salesDocId

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.salesDocId.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <Sales document ID>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f066"></a>

## MD-F066 — erfId

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.erfId.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <ERF ID>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f067"></a>

## MD-F067 — premiseId

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.premiseId.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <resolved premise ID>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f068"></a>

## MD-F068 — targetedMeterNo

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.targetedMeterNo.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** 0012345.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f069"></a>

## MD-F069 — meterNo

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.meterNo.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** 0012345.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f070"></a>

## MD-F070 — returnTo

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.returnTo.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** /(tabs)/admin/operations/my-workorders.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f071"></a>

## MD-F071 — accountNumber

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.accountNumber.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <account context>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f072"></a>

## MD-F072 — customerName

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.customerName.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <customer context>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f073"></a>

## MD-F073 — sourceAddress.addressLine1

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.sourceAddress.addressLine1.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <source address>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f074"></a>

## MD-F074 — sourceAddress.town

- **Meaning:** Carried route/correlation context; expected meter and actual meter must remain separate.
- **Form/context path:** targetedBatchContext.sourceAddress.town.
- **Data type:** string or null.
- **Prerequisite and requirement:** Only when valid Sales Targeted Batch context is present.
- **Validation and dependencies:** SourceModule, tbId, rowId, salesDocId and erfId are client-required. Server validates authority, parent/row/Sales/ERF/premise correlations. Normalisation accepts more fields than route serialisation carries; not all optional fields reach payload.
- **Initial/default value:** Inherited; absent values normalise to null.
- **Canonical storage / transformation:** Normalised payload context; server may replace with authoritative context.
- **Evidence:** None specifically required.
- **Synthetic example:** <source town>.
- **Evidence references:** MD-S23; MD-S43.

<a id="md-f075"></a>

## MD-F075 — Source module

- **Meaning:** Top-level route discriminator.
- **Form/context path:** sourceModule.
- **Data type:** string.
- **Prerequisite and requirement:** Targeted Batch context present.
- **Validation and dependencies:** Must agree with normalised context source module.
- **Initial/default value:** Absent on ordinary route.
- **Canonical storage / transformation:** Same root path.
- **Evidence:** None specifically required.
- **Synthetic example:** SALES_TARGETED_BATCH.
- **Evidence references:** MD-S01; MD-S23.

## Controlled values

The following lists are taken from `formOptions.js` (MD-S10) and `noAccessReasons.js` (MD-S12). They describe the recorded mobile feature; their availability on a deployed build remains unverified.

| List | Values |
| --- | --- |
| Electricity manufacturers | Conlog; Landis+gyr; Cashpower; Hexing; Powercom; Itron; Other |
| Water manufacturers | Conlog; Sensus; Elster Kent; Itron; Kamstrup; Lesira Teq; Aqua Loc; Reonet; Other |
| Electricity placement | Kiosk; Pole Top; Pole Bottom; Boundary Wall; Meter Room; Wall Indoors; Inside Property; Other |
| No Access reasons | Property Locked; Access Refused by Occupant; Unsafe / Dangerous Environment; Meter Box Inaccessible; Meter Obstructed; Property Demolished; Property Vacant; Other with explanation |
| Remaining-credit reasons | Display blank / no reading; Display damaged; Display unreadable; Unable to obtain balance; Meter not responding; Other with explanation |
| Normalisation choices | None (`none`); Disconnect meter; Replace meter; Tamper removed; Keypad normalised; Service point completed; Meter registered |
| No-action reasons | Threatened or chased away; Customer refused; Unsafe to work on; Meter could not be reached; No meter available to replace; Office said to leave it; Other with explanation |
| Other anomalies | Meter Blocked (By Munic); Meter Bridged (By Munic); Incomplete Service Points; Meter Not Registered; Keypad Faulty |

The finding/detail combinations are tabulated in the [Body of Knowledge](meter-discover-body-of-knowledge.md). Changing a finding changes the applicable normalisation choices and can preselect a job. Recheck the whole response section after changing a finding.

## Evidence matrix

| Tag in root media array | Applies when | Requirement / purpose |
| --- | --- | --- |
| `astNoPhoto` | Every accessed electricity/water capture | Required; support physical meter identity |
| `noAccessPhoto` | No Access visit | Required; support recorded access limitation |
| `anomalyPhoto` | Primary finding/detail | Required except Operationally Ok, including Meter Ok suspicions |
| `sealPhoto` | Electricity | Required for captured seal number or a photo-requiring seal reason |
| `keypadPhoto` | Prepaid electricity | Required for captured serial or a photo-requiring keypad reason |
| `astCbPhoto` | Electricity | Required for captured CB size or a photo-requiring CB reason |
| `ogsPhoto` | Electricity with off-grid supply yes | Required |
| `normalisationPhoto` | Electricity on-site fix | Required for fixes; job-only disconnect/replace uses subsequent form evidence in newer contract |
| `meterReadingPhoto` | Conventional water with reading | Required |
| `tokenReadingPhoto` | Prepaid water with token reading | Required |
| `remainingCreditPhoto` | Any prepaid discovery with balance value | Required; URI/URL must be usable; removed when no value or subtype conventional |
| `fieldCommentPhoto` | Optional commentary | Supplementary; cannot replace another required tag |
| `fieldCommentVoice` | Optional commentary | Supplementary audio; microphone permissions and upload apply |
| `fieldCommentVideo` | Optional commentary | Supplementary video; permissions, capture and upload apply |

| Equipment reason list | Photo required | Photo not required solely by this reason |
| --- | --- | --- |
| Seal | Seal Broken; Seal Damaged; Seal Number Not Visible; Seal Number Unreadable; Meter Not Sealed | Seal Missing; Seal Removed; Other with explanation |
| Keypad | Keypad Integrated With Meter; Keypad Serial Number Not Visible; Keypad Serial Number Unreadable; Keypad Damaged | Keypad Missing; Keypad Not Installed; Keypad Inaccessible; Other with explanation |
| Circuit breaker | Circuit Breaker Size Not Visible; Circuit Breaker Size Unreadable; Circuit Breaker Damaged | Circuit Breaker Missing; Circuit Breaker Inaccessible; No Dedicated Circuit Breaker; Distribution Board Inaccessible; Other with explanation |

No general maximum photo count, byte-size limit, minimum resolution or acceptable GPS accuracy is established by this catalogue. Those must be specified and tested before being taught as product limits.

## Media object and reading-entry subfields

These composite records expand MD-F's media and reading fields; they are generated by components, not separate typed form inputs.

| Path | Type | Meaning / population / validation |
| --- | --- | --- |
| `media[].tag` | string | Evidence purpose; one of the applicable tags above; required-tag checks use it |
| `media[].uri` | string | Local capture URI, then remote download URL after upload; required evidence must have URI or URL |
| `media[].url` | string or null | Initially null in camera output; alternate remote-media reference understood by validators |
| `media[].type` | string | Camera uses `image`; comment components also support voice/video records; verify exact recorder payload before integration changes |
| `media[].gps.lat/lng` | number or null | Device GPS where available, otherwise supplied fallback, otherwise null; not necessarily the manually placed meter pin |
| `media[].created.at/byUid/byUser` | strings | Capture-time ISO timestamp and actor supplied to camera; distinct from server transaction audit |
| `media[].updated.at/byUid/byUser` | strings | Camera initially copies capture metadata |
| `mreadings[].reading` | string | Conventional water creation reading |
| `treadings[].tokenReading` | string | Prepaid water creation token reading |
| `mreadings[]/treadings[].readingAt` | ISO timestamp string | Client capture/submission-build time for this entry |
| `mreadings[]/treadings[].trnId` | string | Originating discovery transaction |
| `mreadings[]/treadings[].source` | string | `AST_CREATION` for these discovery entries |

Sources: MD-S01 payload builder; MD-S08 comment component; MD-S50 camera. The CSV contains primary field records; this section supplies composite subfield semantics. Queues, server-derived identifiers and linked-work fields are explained in [rules and data](meter-discover-rules-and-data.md).

## Important asymmetries and gaps

- Electricity has a placement dropdown; water currently does not.
- Seal requires a value or reason. Keypad/CB can be completely blank in the reviewed schema; if populated, their validation/evidence dependencies apply. Do not silently strengthen those rules in a manual.
- Water Manufacturer includes Other, but the water form has no corresponding custom manufacturer field and the backend rejects bare Other. This needs development resolution; selecting a false manufacturer is not a workaround.
- Discovery requires an identifier even when a finding says the meter number is not clearly visible. Unidentified assets need an agreed workflow.
- A water opening reading/token reading is not a completed monthly reading/billing process. Units, decimal precision and the meaning of token reading need explicit decisions.
- The normalisation feature accepts newer action names; the other inspected backend branch retains older values. Use a matched, verified application release.
- No asset legal-owner, enclosure identifier, supply-tracing proof, GPS-accuracy threshold or dedicated water-placement field was identified among these inputs. Record these as requirements to consider, not existing fields.
