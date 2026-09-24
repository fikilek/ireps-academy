# Meter Discovery — source baseline and review gaps

**MDIS version 0.1 · 23 September 2026 · content draft.** The owner requested a comprehensive Body of Knowledge and User Manual for each module, beginning with Meter Discovery. This package provides both legs, diagrams, field/evidence references, errors, data lifecycle and review scenarios. It is an Academy documentation change, not an application implementation or production certification.

## Baseline and reproducibility

Academy base: `296629ed7f58db28c30a050fca3c58cd776528dc`. Development branch: `docs/meter-discover-20260923`, in an isolated worktree. Six concurrent changes in the original Academy checkout's video/field-guide files were left outside this module's change set.

The following source revisions were inspected. All 52 selected files were clean relative to their recorded source checkout when captured. Exact SHA-256 fingerprints and original locations are in the [Academy source register](../SOURCE_REGISTER.csv), rows MD-S01 through MD-S52. The field and error records use those IDs; error references also include the one-based source line.

| Source checkout | Branch | Recorded commit | Relationship to publication |
| --- | --- | --- | --- |
| ireps-mobile | `feature/meter-normalisation-v1` | `c8a5dbcaa041a1546235a27e15e3e5f1c65d3a21` | Source evidence only; deployment not verified |
| ireps-web | `feature/sales-targeted-batch-v3` | `c5be2edb25fbcd2a090c4db1e8b4f3140ddcd116` | Source evidence only; deployment not verified |
| ireps-rules | `main` | `9e53d264c1d45383e8583c3918bc0a3f78880e74` | Source evidence only; deployment not verified |
| ireps-schemas | `main` | `6ad8c444f986c8d271130ffe9f7ef0f50477d194` | Source evidence only; deployment not verified |
| ireps-web-normalisation | `feature/meter-normalisation-v1` | `93050c279b3ed6aba2ed527f25459a76321c0ddf` | Source evidence only; deployment not verified |

The two web checkouts are worktrees of the same application repository. The normalisation feature is used for the newer normalisation contract; the other web branch is retained as comparison evidence for differing action values and related batch logic. This is not a declaration that these branches form a tested release. Rules and schemas describe intended contracts and can differ from implementation.

No application was launched, no Firebase data was queried or changed, and no owner/device test results were manufactured. TP-001 contains previous development-test assertions and a pending repeat-test table; its existence does not certify this package. External Claude artifacts were not needed as authoritative evidence for the new field/error catalogues.

## Source map

| ID | Checkout / repository-relative file | Lines |
| --- | --- | --- |
| MD-S01 | `ireps-mobile/src/features/meters/FormMeterDiscovery.js` | 2696 |
| MD-S02 | `ireps-mobile/components/forms/ElectricitySections.js` | 1034 |
| MD-S03 | `ireps-mobile/components/forms/WaterSections.js` | 193 |
| MD-S04 | `ireps-mobile/components/forms/AnomalySection.js` | 23 |
| MD-S05 | `ireps-mobile/components/forms/OtherAnomalySection.js` | 97 |
| MD-S06 | `ireps-mobile/components/forms/RemainingCreditSection.js` | 107 |
| MD-S07 | `ireps-mobile/components/forms/IrepsNoAccessSection.js` | 279 |
| MD-S08 | `ireps-mobile/components/forms/IrepsFieldCommentSection.js` | 1201 |
| MD-S09 | `ireps-mobile/components/forms/LocationPickerSection.js` | 462 |
| MD-S10 | `ireps-mobile/src/features/meters/formOptions.js` | 472 |
| MD-S11 | `ireps-mobile/src/features/meters/meterNumberRule.js` | 21 |
| MD-S12 | `ireps-mobile/src/features/meters/noAccessReasons.js` | 28 |
| MD-S13 | `ireps-mobile/src/features/meters/remainingCreditContract.js` | 181 |
| MD-S14 | `ireps-mobile/src/features/meters/normalisationHandover.js` | 202 |
| MD-S15 | `ireps-mobile/src/features/meters/findingInstructions.js` | 42 |
| MD-S16 | `ireps-mobile/src/features/meters/FormInputMeterNo.js` | 222 |
| MD-S17 | `ireps-mobile/src/services/processSubmissionQueue.js` | 379 |
| MD-S18 | `ireps-mobile/src/services/startSubmissionQueueSyncService.js` | 43 |
| MD-S19 | `ireps-mobile/src/services/startMeterDiscoveryNoAccessQueueSyncService.js` | 102 |
| MD-S20 | `ireps-mobile/src/utils/submissionQueue.js` | 780 |
| MD-S21 | `ireps-mobile/src/utils/persistNoAccessMeterDiscoveryMedia.js` | 97 |
| MD-S22 | `ireps-mobile/src/redux/trnsApi.js` | 629 |
| MD-S23 | `ireps-mobile/src/features/premises/targetedBatchPremiseContext.js` | 157 |
| MD-S24 | `ireps-mobile/src/features/targetedBatches/askBatchOrOtherDiscovery.js` | 332 |
| MD-S25 | `ireps-mobile/src/features/targetedBatches/foundMeter.js` | 54 |
| MD-S26 | `ireps-mobile/app/(tabs)/premises/form.js` | 5 |
| MD-S27 | `ireps-web/functions/index.js` | 5763 |
| MD-S28 | `ireps-web/functions/meterDiscovery/validation.js` | 706 |
| MD-S29 | `ireps-web/functions/meterDiscovery/astMedia.js` | 11 |
| MD-S30 | `ireps-web/functions/registry/meterRegistryRowRebuild.js` | 175 |
| MD-S31 | `ireps-rules/test-plans/meter-discovery-test-plan.md` | 126 |
| MD-S32 | `ireps-rules/logic-rules/meter-normalisation-rules.md` | 344 |
| MD-S33 | `ireps-rules/logic-rules/meter-anomaly-rules.md` | 49 |
| MD-S34 | `ireps-rules/logic-rules/meter-visibility-rules.md` | 94 |
| MD-S35 | `ireps-rules/ui-rules/field-form-dropdowns.md` | 88 |
| MD-S36 | `ireps-rules/targeted-batches/targeted-batches-rules.md` | 1597 |
| MD-S37 | `ireps-schemas/meter-master/meter_master.schema.md` | 927 |
| MD-S38 | `ireps-schemas/sales-all-meters/sales-all-meters-schema.md` | 1254 |
| MD-S39 | `ireps-schemas/general-monthly-report/general-monthly-report-schema.md` | 150 |
| MD-S40 | `ireps-web-normalisation/functions/index.js` | 5436 |
| MD-S41 | `ireps-web-normalisation/functions/meterDiscovery/validation.js` | 858 |
| MD-S42 | `ireps-web-normalisation/functions/meterDiscovery/astMedia.js` | 11 |
| MD-S43 | `ireps-web-normalisation/functions/targetedBatches/premiseLink.js` | 1756 |
| MD-S44 | `ireps-web-normalisation/functions/targetedBatches/batch-work-guard.js` | 522 |
| MD-S45 | `ireps-web-normalisation/functions/targetedBatches/differentMeterAtErf.js` | 445 |
| MD-S46 | `ireps-mobile/src/features/meters/ForensicFooter.js` | 163 |
| MD-S47 | `ireps-mobile/components/maps/SovereignLocationPicker.js` | 670 |
| MD-S48 | `ireps-mobile/components/media/IrepsMedia.js` | 352 |
| MD-S49 | `ireps-mobile/app/_layout.js` | 280 |
| MD-S50 | `ireps-mobile/components/media/IrepsCamera.js` | 460 |
| MD-S51 | `ireps-web-normalisation/functions/meterMaster/helpers.js` | 295 |
| MD-S52 | `ireps-web-normalisation/functions/salesAllMeters/sales-batch-policy.js` | 328 |

## Key claim-to-source map

| Subject | Evidence |
| --- | --- |
| ERF → premise → meter, Normal Path and Sales Path | MD-S31; MD-S01 parent gate/payload; MD-S27 and MD-S40 callable/trigger |
| Form inputs, defaults, conditions, canonicalisation | MD-S01–MD-S16; MD-S41 |
| Electricity/water screen differences | MD-S02, MD-S03 |
| Controlled values / findings / preselected actions | MD-S10, MD-S02, MD-S32, MD-S33 |
| Number cleaning and local duplicate warning | MD-S11, MD-S16; backend identity classification MD-S51 |
| GPS pin and absence of discovery parcel-containment check | MD-S01 validator, MD-S47 map confirmation, MD-S41 validator |
| No Access durable media and automatic coordinator | MD-S01, MD-S17, MD-S19, MD-S21, MD-S49 |
| General queue handling and success retention | MD-S17, MD-S18, MD-S20 |
| Camera media shape / fallback GPS | MD-S50; optional comment evidence MD-S08 |
| Payload errors and branch incompatibility | MD-S28 versus MD-S41; MD-S27 versus MD-S40 |
| Batch actor/correlation/No Access route | MD-S23, MD-S24, MD-S43, MD-S44, MD-S52 |
| Different-meter-at-ERF rule | MD-S36, MD-S38, MD-S45 |
| Async derivation and visible/master relationships | MD-S27, MD-S40, MD-S34, MD-S37 |
| Follow-on disconnect/remove/install handoff | MD-S14, MD-S32 |
| Submit/reset/result UI | MD-S01, MD-S46 |
| Reporting relevance and financial boundary | MD-S39; Academy owner decisions DEC-008/009 |

## Open issues and publication gates

| ID | Finding / question | Evidence / status | Required resolution |
| --- | --- | --- | --- |
| MD-G01 | Mobile uses new normalisation labels; another backend branch accepts older canonical action strings | MD-S10, MD-S28, MD-S41 | Identify and verify the actual mobile/backend release pair; do not combine claims from incompatible branches |
| MD-G02 | Accessed online capture is not uniformly local-first; uploads precede the callable timeout | MD-S01 | Agree/implement durable ordering, failure retention and exact 15-second boundary |
| MD-G03 | No Access automatic coordinator is mounted; general queue-sync service has no startup caller in the scoped search | MD-S18, MD-S19, MD-S49 | Demonstrate accessed-draft retry route and lifecycle, including app close/restart |
| MD-G04 | Success/deletion handling differs: queue SUCCESS retained, direct reopened success removes item, No Access media cleaned | MD-S01, MD-S17, MD-S20/21 | Owner retention/acknowledgement decision and tested recovery behaviour |
| MD-G05 | Green success display can follow local save | MD-S01 | Distinguish device save, server acceptance and completed derivation in UI and training |
| MD-G06 | Owner standard calls for pre-submit confirmation; inspected footer submits directly | MD-S46; C:/dev/CLAUDE.md shared direction | Confirm target behaviour and update/retest application before promising a confirmation dialog |
| MD-G07 | Water manufacturer Other lacks custom-text helper, while backend rejects bare Other | MD-S03, MD-S41 | Resolve truthful custom-manufacturer capture; no false-value workaround |
| MD-G08 | No water placement field or approved water-specific enclosure taxonomy | MD-S03 | Decide whether structured placement is required and define vocabulary |
| MD-G09 | Unreadable-number finding coexists with mandatory identifier | MD-S10, MD-S01/41 | Define supported unidentified-meter/identity-correction journey |
| MD-G10 | Credit units, water token-reading meaning and reading precision/ranges not established by form contract | MD-S03, MD-S13, MD-S41 | Agree units, semantics and validation; give tested examples |
| MD-G11 | Shared anomaly list includes electricity-oriented options for water | MD-S03, MD-S04, MD-S10 | Review water applicability and any service-specific filtering |
| MD-G12 | UI-R003 describes value-or-reason requirements for CB/keypad, while discovery schema/backend permit both blank | MD-S35 versus MD-S01/41 | Reconcile documented rule, implementation and intended requirement |
| MD-G13 | Accessed capture need not lie within parcel; no accuracy threshold is checked | MD-S01/47/41 | Preserve outside-ERF cases; define any required accuracy/proof separately from association |
| MD-G14 | Batch discovery context refuses No Access and directs to dedicated batch No Access action | MD-S43 | Complete and cross-link separate batch No Access manual; do not collapse routes into one endpoint |
| MD-G15 | Automatic follow-on after direct success exists; after background queue success not demonstrated | MD-S01, MD-S14, MD-S17 | Verify outstanding-work recovery and duplicate-safe return to linked jobs |
| MD-G16 | Same-ID read-then-write retry is not a full concurrent-idempotency proof | MD-S27/40 | Test race/collision/late-response cases and define acknowledgement semantics |
| MD-G17 | Permission inheritance and QA corrections remain unresolved | Owner DEC-004, DEC-008/009 | Approve action matrix and immutable correction/financial effects; retain original evidence |
| MD-G18 | Complete deployment/device evidence, screenshots, demonstrations and reviewer acceptance absent | This Academy pass is source-based | Run scenario pack, record release evidence, review screenshots and publish only accepted material |

## Module outputs and checks

The package contains a substantial Body of Knowledge, separate user manual, 75 primary field/context records plus composite subfield/evidence definitions, 110 structured code/stage error entries, six Mermaid diagrams, 22 practical scenarios and a submission/recovery matrix. Structured errors include related batch helpers and do not imply every entry is reachable on every route. The common Academy module standard defines the outputs to reuse for future modules.

Document validation checks internal file/anchor links, catalogue paths against named controls, source IDs and line bounds, source fingerprints, CSV/Markdown parity, diagram block structure and the exact Git change set. These are documentation checks, not application acceptance tests. A named release still needs the device and backend evidence specified in the scenario pack.
