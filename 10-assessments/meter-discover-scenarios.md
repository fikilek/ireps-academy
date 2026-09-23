# Meter Discover — scenarios and acceptance evidence

**MDIS · version 0.1 · proposed training and release-review pack.** These are scenarios to execute and assess, not results obtained by the Academy documentation task. Source TP-001 contains its own historical claims and an empty repeat-test table; this pack does not turn those claims into a new pass result.

## Practical scenarios

| ID | Scenario | Expected explanation / evidence |
| --- | --- | --- |
| MD-A01 | One ERF with two flats and two electricity meters | Correct ERF → premise → meter associations; each physical serial and evidence kept separate |
| MD-A02 | Shared kiosk outside two ERFs | Pins at actual kiosk; each meter linked to correct served premise; no forced parcel-centre placement |
| MD-A03 | Ordinary electricity discovery with no Sales match | Field asset/master created; absence of Sales link explained without calling the meter nonexistent |
| MD-A04 | Expected meter in accepted batch | Actor/assignment valid; expected and found identifiers match; transaction, asset, master and row outcomes correlate |
| MD-A05 | Different physical meter at expected ERF | Actual serial captured; expected Sales identity preserved; different-meter outcome does not falsely report expected serial found |
| MD-A06 | Ordinary discovery of a Sales meter outside a batch | Correct linkage/visibility and applicable batch ownership behaviour; no bypass assumption |
| MD-A07 | Another team's allocated ERF / meter | Correct refusal/exception interpretation; no inaccurate anomaly used to defeat checks |
| MD-A08 | Meter Ok / Operationally Ok | Appropriate response; required identity proof; no anomaly photo requirement invented for this detail |
| MD-A09 | Meter Ok / Bridge Suspicion or Bypass Suspicion | Suspicion remains labelled; anomaly photo present; not taught as a confirmed offence |
| MD-A10 | Faulty or damaged electricity meter, Replace meter selected | Discovery first; linked removal and installation recorded separately; final asset/Sales/batch effects checked |
| MD-A11 | Illegally Connected, Disconnect meter selected | Accepted discovery followed by correct separate disconnection; original finding remains traceable |
| MD-A12 | Expected job cannot be done | Truthful no-action reason required even if another fix selected; Other expanded to explanatory text |
| MD-A13 | On-site fix plus selected job | Evidence for fix; selected job not counted complete until its own transaction; as-found versus later state understood |
| MD-A14 | Conventional water | Reading plus tagged photo; no electricity-only controls assumed; units/precision clarified before publishing |
| MD-A15 | Prepaid water | Token reading versus remaining credit explained by owner; both observed field dependencies tested |
| MD-A16 | Water manufacturer not listed | Bare Other mismatch reproduced/resolved; no false manufacturer used as workaround |
| MD-A17 | No Access, including Other | Complete reason and evidence; visit recorded without a new asset; distinguish standalone batch No Access route |
| MD-A18 | Unsent parent premise | Child retained, parent saved, resolved parent ID used, no duplicate child created |
| MD-A19 | Prepaid zero, negative balance and unreadable display | Zero treated as value; signed decimal proof; unknown uses reason; subtype switch removes inapplicable credit/photo |
| MD-A20 | Seal/keypad/CB alternatives | Correct required/optional distinction and reason-to-photo matrix exercised |
| MD-A21 | Unreadable or conflicting meter identity | Escalation without fabricated serial; existing master conflict and correction gap explained |
| MD-A22 | GPS outside parcel / poor position | Actual meter position retained; no claim that finite coordinates prove accuracy or service association |

## Submission and recovery matrix

Run both electricity and water where applicable, and both ordinary and batch routes. Use a controlled environment authorised by the owner; this document does not authorise live submissions.

| Case | Required observation |
| --- | --- |
| Online accessed capture | Evidence upload, callable result, derived asset and relevant views; measure the actual scope of timeout |
| Online No Access | Local queue/media exist before network attempt; server result and queue state checked |
| Offline at start | Dropdowns usable, truthful local-save result, actual queue record and evidence available |
| Upload fails | Form/evidence retained or a precise limitation shown; no unsupported safe-storage promise |
| Parent not ready | Child waits without losing context; successful parent correlation verified |
| Callable exceeds 15 seconds | Same transaction may finish later; timeout does not imply cancellation |
| Connectivity returns | Verify which coordinator runs, which records retry and whether app must be open/signed in |
| App closes/restarts | Inspect durability, media references and retry; do not infer OS background support |
| Duplicate retry with same ID | Existing success recognised without new logical work; also test concurrent requests separately |
| Different ID with same meter number | Master identity conflict handled without overwriting existing asset |
| CONFLICT item | Evidence remains accessible; no silent retry loop treated as resolution |
| Successful queue submission | Record retention/deletion and No Access media cleanup documented separately |
| Background success needing follow-on | Outstanding job discoverable; no assumption that navigation automatically resumes |
| Accepted transaction, failed derivation | Support can trace original ID and report missing asset/master/row without rediscovery |
| Reset/back navigation | Actual draft/media behaviour demonstrated; warning is not mistaken for server deletion |

## Learner assessment

1. Explain why a meter at a roadside kiosk can serve a premise on another ERF. Correct answer separates record association, physical location and legal ownership.
2. Distinguish connection state, finding, normalisation and Sales visibility. A VISIBLE meter is not necessarily healthy or already normalised.
3. Describe the evidence for Meter Ok with Bypass Suspicion. The suspicion detail still requires an anomaly photograph.
4. Explain why a missing prepaid balance must not be entered as zero. Zero is data; unknown requires a reason.
5. Describe the difference between retrying a queued transaction and creating another discovery. Identity and payment/reporting consequences must be acknowledged.
6. Explain what remains to do after Replace meter is selected. Removal and installation are separate linked tasks, not completed by a tick.
7. Show how to determine whether a green success display means local save or server acceptance. Specific message, queue status and server evidence must be checked.

Suggested assessment rule for review: critical identity, association, evidence and submission-state errors require another supervised attempt. Scoring/certification thresholds have not been approved.

## Publication record to complete

For each executed case record: tester, date, environment, mobile build/commit, backend deployment revision, role/provider/team, synthetic fixture IDs, steps, screenshots, transaction/queue IDs, derived records checked, actual outcome, defects and reviewer. Never fill a blank result with Pass solely because a test plan says what should happen.

Publication needs owner resolution of material gaps, a matched application release, reviewed screenshots, demonstrated recovery, accessible diagrams and an approved manual. Video scripts and recordings should be derived from that accepted version; none are claimed produced by this package.
