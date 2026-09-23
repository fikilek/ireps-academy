# Sales Monthly Refresh and Population — completion evidence

Execution window began 2026-09-05 09:47:13 UTC. Status vocabulary: IMPLEMENTED means local source exists; OFFLINE VERIFIED means specified executable checks passed; LIVE ACCEPTANCE BLOCKED identifies missing live acceptance; NOT RELEASED means no deployment/data release occurred. No remote writes, deployments, commits or merges are authorized in this pass.

## Final contract

Exact-month `monthlyCategories` is the sole category authority. Missing selected/report month is unavailable. Legacy scalar fields remain frozen; no fallback or Demo restoration. Preserve `salesStatus`, valid creation metadata and operational fields. The view defaults to the latest successfully published month for its scope.

Supplier snapshots use the configured Storage bucket at `governed-sales/{lmPcode}/{provider}/snapshots/{sha256}.json`, with an authenticated scope-authorized backend and a verified scope `publication.json`. Executed evidence reports are immutable objects at the same scope's `reports/{reportSha256}.json`. Publication identifies `schemaVersion: 1`, `projectId`, `lmPcode`, `provider`, `latestMonth` and month entries with `snapshotSha256` plus `verification: {status: "PASS", complete: true, reportSha256}`. The backend verifies object hashes and executed-report binding; preflight-only or incomplete evidence cannot govern a month. Month publication follows complete sequential data verification. No population business collection/map is introduced. Local artifacts are not deployed artifacts.

The recorded DEV SPU creation convention is UID `fXBACUfMzybcqC0AbeNeyYyTeRu1`, user `Fikile Kentane`, evidenced by `ireps-web/functions/scripts/ireps2-users-20260621-2233.json`. It does not supply Sales creation timestamps. Missing Sales creation metadata requires original per-document first-capture evidence.

## Stage record

| Stage | Local implementation / evidence | Live acceptance / blocker |
|---|---|---|
| 0 identity/source baseline | Existing canonical identity inputs inspected; prior Stage 0 reconciliation evidence is unavailable. | LIVE ACCEPTANCE BLOCKED: prior evidence and July complete supplier-membership authority remain unavailable; no assumptions substitute for them. |
| 1 schema/rules | IMPLEMENTED: schema v1.4.1 and rules v1.12.1 final-state amendment; dictionary aligned. OFFLINE VERIFIED: 14/14 governance tests. | NOT RELEASED. |
| 2 backend writers | IMPLEMENTED/OFFLINE VERIFIED: metadata-preserving operational paths covered by affected Web/backend suite, 218/218 passed. | NOT RELEASED; deployed compatibility not reverified. |
| 3 monthly adapter | IMPLEMENTED/OFFLINE VERIFIED: preserved Stage03A/04 foundation and exact source-month ingestion. Final affected pipeline suite 103 passed plus 30 subtests, exit 0. | Governed originals and prior reconciliation approval remain release requirements. |
| 4 global preflight | IMPLEMENTED/OFFLINE VERIFIED: complete global classification and zero-write conflict gate included in final 103-test pipeline suite. | LIVE ACCEPTANCE BLOCKED: DEV failed before first read; process trust probe still has authentication-layer blocker. No certificate repair approved/performed; no long retry. |
| 5 monthly source support | IMPLEMENTED/OFFLINE VERIFIED: actual Stage03A CLI and Stage05→06→08 roundtrip included in final pipeline suite. | Complete July supplier-membership evidence remains unavailable. |
| 6 history-safe writes | IMPLEMENTED/OFFLINE VERIFIED: exact month additions, prior history comparison, immutable creation metadata, no-op preservation, typed backup/plan and before-write global gate; real Stage08 path exercised with fake transport. | LIVE ACCEPTANCE BLOCKED; original creator scope/actor approval and real state verification still required. |
| 7 release package | IMPLEMENTED/OFFLINE VERIFIED: publication gate 11/11 tests; path-specific recovery planner 7/7 including actual typed writer encoder; guarded Storage publisher 7/7 with fake bucket and offline CLI. Same serialized synthetic fixture accepted across Python and Web. | NOT RELEASED: exact remote scope and execution need one release approval; synthetic fixtures are not live acceptance. |
| 8 June baseline | Planned from June authoritative workbook, not current scalar values. | No June migration executed in this pass. |
| 9 July refresh | Planned from July's own category/risk source. | Requires verified June then release authorization. |
| 10 August refresh | Planned from August's own category/risk source. | Requires verified July then release authorization. |
| 11 population dashboard | IMPLEMENTED/OFFLINE VERIFIED: scoped artifacts, reconciled membership partitions and asynchronous scope/race protection; included in Web 218/218 tests. Storage emulator 2/2; DEV build and focused lint exit 0. | NOT RELEASED; no published remote snapshots or browser acceptance against governed data. |
| 12 remaining consumers | IMPLEMENTED/OFFLINE VERIFIED: exact selected/report-month readers, Web/backend 218/218. Mobile 27/27 focused tests, exit 0, process 0.36 seconds; no Mobile edits. | NOT RELEASED; deployment and affected live consumer acceptance outstanding. |
| 13 legacy freeze | IMPLEMENTED/OFFLINE VERIFIED: scalar updates/fallback/deletion prohibited in final writer/reader contract; preserved existing roots. | NOT RELEASED. |
| 14 SG/ERF | `scripts/sales_sg_erf_plan.py` and `scripts/14_plan_sales_sg_erf.py` implemented; 7/7 behavioral tests passed. Current August plan covers 10,271 rows: 7,583 authoritative single resolutions, 2,688 exceptions. | Canonical destination mapping blocked; no Firestore operations proposed or executed. |
| 15 documentation | IMPLEMENTED: local as-built, schema, rules, dictionary and stage matrix complete for this pass, with final offline evidence recorded. | NOT RELEASED; coordinator's consolidated release dossier controls proposed remote actions. |

## Stage 14 retained evidence

`ireps-pipeline-sales/output/monthly_only/ZA5241/03_sg_one_to_one_assessment/one_to_one_summary.json` reports 10,216 assessed meters, 7,583 one-to-one matches and 2,633 exceptions. Every match uses the recorded comparison-only trailing-zero rule after removing K241 from the authoritative parcel key. The summary is `REVIEW_REQUIRED`; no Firestore operations occurred.

The corresponding `02_enriched_psd_sg_fixed` summary is a local PSD `PASSED` result, not remote Sales enrichment acceptance. Street-address enrichment alone proves no cadastral relationship. The inspected Sales schema has no canonical `sgCode`/`erfNo` destination definition; retain authoritative `sg.prclKey` as source evidence until the projection is settled.

All three assessment input hashes were rechecked during this pass and match the current bytes: END workbook `ba7a080a12d78c1e41c9d0ddd6f960037d91fec5fa04ac5e539f16482de8e641`; valuation bridge `f7529e0b931b1640055aa99e60ef4a1fb8e06f83d3ad5e72a9efe031a7fdccb3`; authoritative B04 ERF JSONL `1d92aa151384445fbe5fe94f2b65ff92ac1669d167816b67dc46fa3a7bb31298`.

The new `ireps-pipeline-sales/output/logs/completion_pass__20260905T094713Z/stage14_evidence_plan.json` binds the current August 10,271-row input fingerprint. It records 7,583 authoritative single resolutions and 2,688 exceptions: the retained 2,633 plus 55 current IDs absent from the older assessment. `tests/test_sales_sg_erf_plan_offline.py` passed 7/7. No Firestore operations are proposed while destination semantics remain blocked.

## Verification limits

`scripts/sales_recovery_plan.py` prepares path-specific restoration with current update-time preconditions, blocks diverged after-values and never proposes deletion of new documents. `scripts/publish_sales_governed_artifacts.py` defaults to offline validation; explicit execution uses create-only immutable artifacts and changes publication last with an exact generation precondition. Failed publication can leave unreferenced immutable artifacts, without publishing an incomplete month. No remote publisher or recovery execution occurred.

Mobile evidence is recorded at `ireps-pipeline-sales/output/logs/completion_pass__20260905T094713Z/mobile_regression_evidence.md`. It covers Targeted lifecycle, No Access, premise context and Sales listener source assertions. Existing Node `MODULE_TYPELESS_PACKAGE_JSON` warnings did not fail the run. Mobile's Sales listener reads preserved `tbRefs.fieldWork` data, not monthly/scalar category values.

Final pipeline evidence: `ireps-pipeline-sales/output/logs/completion_pass__20260905T094713Z/pipeline/pipeline_tests.result.json` and `pipeline_tests.stdout.log`: 103 passed plus 30 subtests, exit 0, process wall time 6.888 seconds. Coverage includes real local CLI/roundtrip paths, immutable-source and user evidence, complete exception scope, metadata/no-op creation behavior, atomic snapshot creation and write-contract guard. All remote behavior used fake transport.

Final Web evidence: `ireps-pipeline-sales/output/logs/completion_pass__20260905T094713Z/web_result.json`: 218/218 affected Web/backend/Targeted tests passed, focused lint exit 0, DEV build exit 0, Storage emulator 2/2 passed. Build warnings about large chunks and ineffective dynamic imports remain. The unrelated existing PrepaidSales effect lint limitation was preserved. Final serialized Python/Web publication fixtures passed including `planEvidence`; these are synthetic offline evidence only.

TLS remains LIVE ACCEPTANCE BLOCKED. The trusted Avast root has non-critical CA Basic Constraints, rejected by the current authentication HTTPS verifier. Supported Avast repair/reissue is a separate proposed administrator action; it was neither approved nor performed. No machine trust changes, verification bypasses or further preflight retries occurred.

No documentation assertion substitutes for a passing executable test, deployed backend, successful read-only acceptance or verified database execution. Incomplete write waves must not advance publication. Recovery must preserve legitimate concurrent operational updates through exact preconditions and before-images.
