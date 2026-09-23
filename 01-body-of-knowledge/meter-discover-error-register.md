# Meter Discover — error and outcome register

**MDIS · version 0.1 · review draft.** Runtime codes below are extracted from the inspected discovery validator/callable, master helper, batch linkage/membership helpers and local queue. `MD-E...` identifiers are Academy references, **not application error codes**. A code can occur at more than one stage. Variable templates retain placeholders. Sources identify file and line through the [source baseline](../00-academy-governance/source-assessments/meter-discover-source-baseline-2026-09-23.md).

The [CSV register](meter-discover-error-register.csv) contains a separate stage, message, data-state warning, recovery and source for each entry. Batch helper errors cover related preparation and derivation as well as discovery submission; their inclusion does not mean every code is reachable from every discovery route. Generic Firebase transport/storage/device errors remain a separate family and are not exhaustively enumerated here.

## First establish what happened

| Stage | Typical result | What to do |
| --- | --- | --- |
| Form validation | Highlighted field / Submit blockers | Correct the unsent form; inspect missing conditional evidence |
| Local persistence | Saved as Draft / Saved Offline / Saved Locally | Verify the queue item exists; this is not proof of server acceptance |
| Storage/camera/upload | Capture or upload error | Preserve the form; check permissions/file availability and connectivity |
| Server refusal | Structured success:false, code, message | Resolve the field, parent, identity or authority issue; retry the same item when appropriate |
| Timeout/lost response | Outcome not confirmed | Server may still finish. Check existing transaction/queue before retry; do not create a second capture merely to obtain a response |
| Accepted, derivation pending | Meter not ready / linked work unavailable | Investigate original transaction, derived asset and downstream processing |
| Queue conflict | CONFLICT rather than SUCCESS | Supervisor/support must reconcile identity or assignment; repeated submission is not a resolution |

For an escalation, supply the build/environment, route, transaction ID, queue ID/status, expected and observed meter numbers, ERF/premise, time, exact message and relevant evidence reference. Do not include account secrets. A local capture disappearing from view is not by itself proof of deletion or submission.

## Exact local messages and outcomes without stable product codes

| Message / title | Trigger or meaning | Recovery |
| --- | --- | --- |
| Meter number is required | Accessed form has no identity | Read or scan the real serial; escalate an unreadable identity |
| Meter number may only contain letters and digits. Remove dashes, slashes, dots or other symbols. | Input fails number pattern | Recheck physical serial; do not replace it with a fabricated value |
| DUPLICATE METER DETECTED | Loaded local data already contain the number | Verify existing meter/premise; local warning is not a complete global search |
| Please provide a reason for no access / Please provide details for Other | Missing or incomplete No Access reason | Select truthful reason and supply custom explanation if needed |
| No Access photo required / Meter photo required / Meter No. photo required | Required tag absent | Add the relevant photo, not an unrelated one |
| Manufacturer is required / Other manufacturer is required / Model name is required | Identity-description dependency incomplete | Complete the actual description; water Other mismatch needs support |
| Seal number or comment is required | Neither seal value nor alternative explanation provided | Record visible number or reason |
| Other Seal Number Reason is required / Other Keypad Serial Number Reason is required / Other Circuit Breaker Reason is required | Other chosen without text | Explain the actual missing-value condition |
| GPS location is required / Invalid GPS coordinates | Missing or invalid position | Confirm actual meter pin; parcel centre is not automatically correct |
| Meter status is required | Connection state blank | Record observed state; do not infer from Sales visibility |
| Enter a valid Remaining Credit value | Balance fails decimal pattern | Signed decimal only, no commas or unit suffix |
| Remaining Credit reason is required / Specify the other Remaining Credit reason | Missing balance needs explanation | Supply reason; zero is a real value, not an unknown marker |
| Remaining Credit photo required | Balance present without usable proof | Capture and confirm the balance photo |
| Choose one: disconnect or replace. | Two follow-on jobs chosen | Select the actual job; do not claim both sequences in one finding |
| Draft not found. | Queue ID no longer resolves | Check queue/server state; support investigates before creating a new capture |
| Premise data not found. | Form lost its parent context | Return to correct premise and preserve existing draft identity |
| Saved as Draft | Parent premise is not yet successfully saved | Save/sync parent before submitting child |
| Draft Save Failed | Local persistence failed | Capture is not proven safely stored; keep form open and escalate storage failure |
| Saved Offline / Saved Locally | Local retention or uncertain response | Inspect queue entry and exact message; server outcome is not established by title |
| Submission Failed / Error | Server, upload or other failure | Read full message and inspect transaction/queue state |
| MISSION SUCCESS / Trn saved successfully | Generic success UI also reused after some local-save branches | Use the preceding specific message and actual queue/server status |
| Meter saved, disconnection still to do / Meter saved, removal still to do | Accepted capture but asset not ready for automatic handoff | Open job from meter card when available; do not rediscover |
| This meter still needs to be disconnected. Issue the disconnection to a field worker from the meter card (DISC). | Actor cannot perform the follow-on field job | Responsible office role issues the work |
| This meter still needs to be replaced. Issue the removal to a field worker from the meter card (REM). | Replacement follow-on requires another actor | Issue removal/replacement work; discovery alone did not replace meter |

`SUBMISSION_TIMEOUT` is an internal timeout marker handled by the form, not proof that the backend cancelled the request. `DUPLICATE_METER` is recognised by the form's compatibility display; the inspected master validator commonly reports the more specific `MM_AST_REFERENCE_CONFLICT` instead.

## Structured runtime entries

| Reference | Runtime code | Stage |
| --- | --- | --- |
| [MD-E001](#md-e001) | `ANOMALY_PHOTO_REQUIRED` | Payload validation |
| [MD-E002](#md-e002) | `BATCH_CHECK_UNAVAILABLE` | Batch ownership guard |
| [MD-E003](#md-e003) | `CB_PHOTO_REQUIRED` | Payload validation |
| [MD-E004](#md-e004) | `CB_SIZE_OR_COMMENT_REQUIRED` | Payload validation |
| [MD-E005](#md-e005) | `DEVICE_OFFLINE` | Local queue / connectivity |
| [MD-E006](#md-e006) | `DUPLICATE_NORMALISATION_ACTION` | Payload validation |
| [MD-E007](#md-e007) | `DUPLICATE_OTHER_ANOMALY` | Payload validation |
| [MD-E008](#md-e008) | `FIELDWORK_INVALID` | Batch preparation / submission / derivation |
| [MD-E009](#md-e009) | `INVALID_ACCESS_VALUE` | Payload validation |
| [MD-E010](#md-e010) | `INVALID_METER_CATEGORY` | Payload validation |
| [MD-E011](#md-e011) | `INVALID_METER_GPS` | Payload validation |
| [MD-E012](#md-e012) | `INVALID_METER_NUMBER` | Discovery callable |
| [MD-E013](#md-e013) | `INVALID_METER_PHASE` | Payload validation |
| [MD-E014](#md-e014) | `INVALID_METER_PLACEMENT` | Payload validation |
| [MD-E015](#md-e015) | `INVALID_METER_STATUS` | Payload validation |
| [MD-E016](#md-e016) | `INVALID_METER_SUBTYPE` | Payload validation |
| [MD-E017](#md-e017) | `INVALID_METER_TYPE` | Payload validation |
| [MD-E018](#md-e018) | `INVALID_NORMALISATION_ACTION` | Payload validation |
| [MD-E019](#md-e019) | `INVALID_NO_ACCESS_METER_TYPE` | Payload validation |
| [MD-E020](#md-e020) | `INVALID_OTHER_ANOMALIES` | Payload validation |
| [MD-E021](#md-e021) | `INVALID_OTHER_ANOMALY` | Payload validation |
| [MD-E022](#md-e022) | `INVALID_PREMISE_ID` | Discovery callable |
| [MD-E023](#md-e023) | `INVALID_REMAINING_CREDIT` | Payload validation |
| [MD-E024](#md-e024) | `INVALID_REMAINING_CREDIT_COMMENT` | Payload validation |
| [MD-E025](#md-e025) | `INVALID_TRN_ID` | Payload validation |
| [MD-E026](#md-e026) | `INVALID_TRN_TYPE` | Payload validation |
| [MD-E027](#md-e027) | `KEYPAD_PHOTO_REQUIRED` | Payload validation |
| [MD-E028](#md-e028) | `KEYPAD_SERIAL_OR_COMMENT_REQUIRED` | Payload validation |
| [MD-E029](#md-e029) | `METER_IN_ANOTHER_TEAMS_BATCH` | Batch ownership guard |
| [MD-E030](#md-e030) | `METER_PHOTO_REQUIRED` | Payload validation |
| [MD-E031](#md-e031) | `METER_PLACEMENT_REQUIRED` | Payload validation |
| [MD-E032](#md-e032) | `METER_READING_PHOTO_REQUIRED` | Payload validation |
| [MD-E033](#md-e033) | `METER_READING_REQUIRED` | Payload validation |
| [MD-E034](#md-e034) | `MISSING_REQUIRED_FIELD` | Payload validation |
| [MD-E035](#md-e035) | `MISSING_REQUIRED_PARENT` | Payload validation |
| [MD-E036](#md-e036) | `MM_AST_REFERENCE_CONFLICT` | Master identity / derivation |
| [MD-E037](#md-e037) | `MM_CANONICAL_FIELD_MISSING` | Master identity / derivation |
| [MD-E038](#md-e038) | `MM_CREATED_METADATA_INVALID` | Master identity / derivation |
| [MD-E039](#md-e039) | `MM_DOCUMENT_ID_NONCANONICAL` | Master identity / derivation |
| [MD-E040](#md-e040) | `MM_DOCUMENT_SHAPE_UNSAFE` | Master identity / derivation |
| [MD-E041](#md-e041) | `MM_GOVERNED_FIELD_TYPE_INVALID` | Master identity / derivation |
| [MD-E042](#md-e042) | `MM_LM_CONFLICT` | Master identity / derivation |
| [MD-E043](#md-e043) | `MM_METER_TYPE_CONFLICT` | Master identity / derivation |
| [MD-E044](#md-e044) | `MM_NORMALIZED_IDENTITY_CONFLICT` | Master identity / derivation |
| [MD-E045](#md-e045) | `NON_CANONICAL_CB_COMMENT_OTHER` | Payload validation |
| [MD-E046](#md-e046) | `NON_CANONICAL_KEYPAD_COMMENT_OTHER` | Payload validation |
| [MD-E047](#md-e047) | `NON_CANONICAL_MANUFACTURER_OTHER` | Payload validation |
| [MD-E048](#md-e048) | `NON_CANONICAL_NO_ACTION_REASON_OTHER` | Payload validation |
| [MD-E049](#md-e049) | `NON_CANONICAL_SEAL_COMMENT_OTHER` | Payload validation |
| [MD-E050](#md-e050) | `NORMALISATION_ACTIONS_REQUIRED` | Payload validation |
| [MD-E051](#md-e051) | `NORMALISATION_NONE_NOT_EXCLUSIVE` | Payload validation |
| [MD-E052](#md-e052) | `NORMALISATION_ONE_JOB_ONLY` | Payload validation |
| [MD-E053](#md-e053) | `NORMALISATION_PHOTO_REQUIRED` | Payload validation |
| [MD-E054](#md-e054) | `NORMALISATION_REASON_NOT_EXPECTED` | Payload validation |
| [MD-E055](#md-e055) | `NORMALISATION_REASON_REQUIRED` | Payload validation |
| [MD-E056](#md-e056) | `NO_ACCESS_PHOTO_REQUIRED` | Payload validation |
| [MD-E057](#md-e057) | `NO_ACCESS_REASON_REQUIRED` | Payload validation |
| [MD-E058](#md-e058) | `OFF_GRID_PHOTO_REQUIRED` | Payload validation |
| [MD-E059](#md-e059) | `OFF_GRID_STATUS_REQUIRED` | Payload validation |
| [MD-E060](#md-e060) | `PREMISE_NOT_FOUND` | Discovery callable |
| [MD-E061](#md-e061) | `PREMISE_NOT_READY` | Local queue / connectivity |
| [MD-E062](#md-e062) | `QUEUE_BUSY` | Local queue / connectivity |
| [MD-E063](#md-e063) | `REMAINING_CREDIT_COMMENT_NOT_ALLOWED` | Payload validation |
| [MD-E064](#md-e064) | `REMAINING_CREDIT_COMMENT_OTHER_REQUIRED` | Payload validation |
| [MD-E065](#md-e065) | `REMAINING_CREDIT_COMMENT_REQUIRED` | Payload validation |
| [MD-E066](#md-e066) | `REMAINING_CREDIT_PHOTO_REQUIRED` | Payload validation |
| [MD-E067](#md-e067) | `SALES_TB_REFS_INVALID` | Batch preparation / submission / derivation |
| [MD-E068](#md-e068) | `SALES_TB_REF_DUPLICATE` | Batch preparation / submission / derivation |
| [MD-E069](#md-e069) | `SALES_TB_REF_METER_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E070](#md-e070) | `SALES_TB_REF_NOT_FOUND` | Batch preparation / submission / derivation |
| [MD-E071](#md-e071) | `SALES_TB_REF_PREMISE_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E072](#md-e072) | `SALES_TB_REF_ROW_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E073](#md-e073) | `SALES_TB_REF_TRN_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E074](#md-e074) | `SEAL_NUMBER_OR_COMMENT_REQUIRED` | Payload validation |
| [MD-E075](#md-e075) | `SEAL_PHOTO_REQUIRED` | Payload validation |
| [MD-E076](#md-e076) | `TARGETED_BATCH_ACCESS_DENIED` | Batch preparation / submission / derivation |
| [MD-E077](#md-e077) | `TARGETED_BATCH_ALLOCATION_TARGET_INVALID` | Batch preparation / submission / derivation |
| [MD-E078](#md-e078) | `TARGETED_BATCH_COMPLETION_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E079](#md-e079) | `TARGETED_BATCH_CONTEXT_INCOMPLETE` | Batch preparation / submission / derivation |
| [MD-E080](#md-e080) | `TARGETED_BATCH_CONTEXT_INVALID` | Batch preparation / submission / derivation |
| [MD-E081](#md-e081) | `TARGETED_BATCH_ERF_LINK_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E082](#md-e082) | `TARGETED_BATCH_EXECUTION_COMPLETED` | Batch preparation / submission / derivation |
| [MD-E083](#md-e083) | `TARGETED_BATCH_EXECUTION_STATE_INVALID` | Batch preparation / submission / derivation |
| [MD-E084](#md-e084) | `TARGETED_BATCH_LM_SCOPE_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E085](#md-e085) | `TARGETED_BATCH_METER_DISCOVERY_RESULT_INCOMPLETE` | Batch preparation / submission / derivation |
| [MD-E086](#md-e086) | `TARGETED_BATCH_NOT_ACCEPTED` | Batch preparation / submission / derivation |
| [MD-E087](#md-e087) | `TARGETED_BATCH_NOT_ALLOCATED` | Batch preparation / submission / derivation |
| [MD-E088](#md-e088) | `TARGETED_BATCH_NOT_ASSIGNED_TO_ACTOR` | Batch preparation / submission / derivation |
| [MD-E089](#md-e089) | `TARGETED_BATCH_NOT_READY` | Batch preparation / submission / derivation |
| [MD-E090](#md-e090) | `TARGETED_BATCH_OPERATION_TYPE_INVALID` | Batch preparation / submission / derivation |
| [MD-E091](#md-e091) | `TARGETED_BATCH_PARENT_ID_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E092](#md-e092) | `TARGETED_BATCH_PREMISE_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E093](#md-e093) | `TARGETED_BATCH_PREMISE_CONTEXT_CONFLICT` | Batch preparation / submission / derivation |
| [MD-E094](#md-e094) | `TARGETED_BATCH_PREMISE_CONTEXT_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E095](#md-e095) | `TARGETED_BATCH_PREMISE_LINK_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E096](#md-e096) | `TARGETED_BATCH_PREMISE_LINK_MISSING` | Batch preparation / submission / derivation |
| [MD-E097](#md-e097) | `TARGETED_BATCH_ROW_EXECUTION_STATE_INVALID` | Batch preparation / submission / derivation |
| [MD-E098](#md-e098) | `TARGETED_BATCH_ROW_ID_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E099](#md-e099) | `TARGETED_BATCH_ROW_NOT_ACCEPTED` | Batch preparation / submission / derivation |
| [MD-E100](#md-e100) | `TARGETED_BATCH_ROW_NOT_ALLOCATABLE` | Batch preparation / submission / derivation |
| [MD-E101](#md-e101) | `TARGETED_BATCH_ROW_NOT_ALLOCATED` | Batch preparation / submission / derivation |
| [MD-E102](#md-e102) | `TARGETED_BATCH_ROW_PARENT_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E103](#md-e103) | `TARGETED_BATCH_SALES_LINK_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E104](#md-e104) | `TARGETED_BATCH_SCOPE_MISSING` | Batch preparation / submission / derivation |
| [MD-E105](#md-e105) | `TARGETED_BATCH_USE_NO_ACCESS_FLOW` | Batch preparation / submission / derivation |
| [MD-E106](#md-e106) | `TARGETED_BATCH_WARD_SCOPE_MISMATCH` | Batch preparation / submission / derivation |
| [MD-E107](#md-e107) | `TOKEN_READING_PHOTO_REQUIRED` | Payload validation |
| [MD-E108](#md-e108) | `TOKEN_READING_REQUIRED` | Payload validation |
| [MD-E109](#md-e109) | `UNAUTHENTICATED` | Batch preparation / submission / derivation |
| [MD-E110](#md-e110) | `UNKNOWN_QUEUE_FORM_TYPE` | Local queue / connectivity |

<a id="md-e001"></a>

### MD-E001 — `ANOMALY_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Anomaly photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:700

<a id="md-e002"></a>

### MD-E002 — `BATCH_CHECK_UNAVAILABLE`

- **Stage:** Batch ownership guard
- **Message / template:** iREPS could not check which batch this meter is in. Nothing was saved. Please try again.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Retain captured evidence; restore connectivity and retry the same item after the batch check is available.
- **Source:** MD-S44:42

<a id="md-e003"></a>

### MD-E003 — `CB_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Circuit Breaker photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:794

<a id="md-e004"></a>

### MD-E004 — `CB_SIZE_OR_COMMENT_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Electricity meter circuit breaker size or comment is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:792

<a id="md-e005"></a>

### MD-E005 — `DEVICE_OFFLINE`

- **Stage:** Local queue / connectivity
- **Message / template:** Device offline
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Check that a local item exists; restore connectivity and inspect its status rather than assuming background transmission.
- **Source:** MD-S17:65

<a id="md-e006"></a>

### MD-E006 — `DUPLICATE_NORMALISATION_ACTION`

- **Stage:** Payload validation
- **Message / template:** The same action cannot be chosen twice.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:200

<a id="md-e007"></a>

### MD-E007 — `DUPLICATE_OTHER_ANOMALY`

- **Stage:** Payload validation
- **Message / template:** ast.anomalies.otherAnomalies cannot contain duplicates
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:378

<a id="md-e008"></a>

### MD-E008 — `FIELDWORK_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Sales fieldWork value is invalid.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1395

<a id="md-e009"></a>

### MD-E009 — `INVALID_ACCESS_VALUE`

- **Stage:** Payload validation
- **Message / template:** accessData.access.hasAccess must be yes or no
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:558

<a id="md-e010"></a>

### MD-E010 — `INVALID_METER_CATEGORY`

- **Stage:** Payload validation
- **Message / template:** Meter category must be Normal or Bulk
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:660

<a id="md-e011"></a>

### MD-E011 — `INVALID_METER_GPS`

- **Stage:** Payload validation
- **Message / template:** ast.location.gps must contain valid numeric lat and lng
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:653

<a id="md-e012"></a>

### MD-E012 — `INVALID_METER_NUMBER`

- **Stage:** Discovery callable
- **Message / template:** Meter number must contain a non-whitespace value
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare with the physical serial, preserve leading zeros, remove spaces and correct invalid symbols; escalate genuinely unreadable identity.
- **Source:** MD-S40:3124

<a id="md-e013"></a>

### MD-E013 — `INVALID_METER_PHASE`

- **Stage:** Payload validation
- **Message / template:** Electricity meter phase must be single or three
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:746

<a id="md-e014"></a>

### MD-E014 — `INVALID_METER_PLACEMENT`

- **Stage:** Payload validation
- **Message / template:** Electricity meter placement must use an approved Meter Placement option
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:329

<a id="md-e015"></a>

### MD-E015 — `INVALID_METER_STATUS`

- **Stage:** Payload validation
- **Message / template:** status.state must be one of CONNECTED, DISCONNECTED
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:681

<a id="md-e016"></a>

### MD-E016 — `INVALID_METER_SUBTYPE`

- **Stage:** Payload validation
- **Message / template:** Meter type must be prepaid or conventional
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:667

<a id="md-e017"></a>

### MD-E017 — `INVALID_METER_TYPE`

- **Stage:** Payload validation
- **Message / template:** Access submissions must use water or electricity meterType
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:590

<a id="md-e018"></a>

### MD-E018 — `INVALID_NORMALISATION_ACTION`

- **Stage:** Payload validation
- **Message / template:** This action is not on the list.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:193

<a id="md-e019"></a>

### MD-E019 — `INVALID_NO_ACCESS_METER_TYPE`

- **Stage:** Payload validation
- **Message / template:** No-access submissions must use meterType NA
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:566

<a id="md-e020"></a>

### MD-E020 — `INVALID_OTHER_ANOMALIES`

- **Stage:** Payload validation
- **Message / template:** ast.anomalies.otherAnomalies must be an array
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:361

<a id="md-e021"></a>

### MD-E021 — `INVALID_OTHER_ANOMALY`

- **Stage:** Payload validation
- **Message / template:** ast.anomalies.otherAnomalies contains an unsupported value
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:371

<a id="md-e022"></a>

### MD-E022 — `INVALID_PREMISE_ID`

- **Stage:** Discovery callable
- **Message / template:** A valid saved premise id is required before meter discovery can be submitted
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Complete or verify the saved parent premise, then reopen the existing discovery draft; do not attach it to a different premise to force acceptance.
- **Source:** MD-S27:3484; MD-S40:3156

<a id="md-e023"></a>

### MD-E023 — `INVALID_REMAINING_CREDIT`

- **Stage:** Payload validation
- **Message / template:** Remaining Credit must be a signed decimal value
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Enter signed decimal balance with its photo, or leave it blank and provide the approved reason. Do not use zero for unknown credit.
- **Source:** MD-S41:466

<a id="md-e024"></a>

### MD-E024 — `INVALID_REMAINING_CREDIT_COMMENT`

- **Stage:** Payload validation
- **Message / template:** Remaining Credit reason must use an approved option or Other with details
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Enter signed decimal balance with its photo, or leave it blank and provide the approved reason. Do not use zero for unknown credit.
- **Source:** MD-S41:517

<a id="md-e025"></a>

### MD-E025 — `INVALID_TRN_ID`

- **Stage:** Payload validation
- **Message / template:** Template: TRN id must start with ${METER_DISCOVERY_TRN_PREFIX}
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Preserve the draft and report transaction/queue ID, exact message, route and build. Retry the same record when the underlying condition is resolved.
- **Source:** MD-S41:544

<a id="md-e026"></a>

### MD-E026 — `INVALID_TRN_TYPE`

- **Stage:** Payload validation
- **Message / template:** Template: trnType must be ${METER_DISCOVERY_TRN_TYPE}
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Preserve the draft and report transaction/queue ID, exact message, route and build. Retry the same record when the underlying condition is resolved.
- **Source:** MD-S41:551

<a id="md-e027"></a>

### MD-E027 — `KEYPAD_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Keypad photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:812

<a id="md-e028"></a>

### MD-E028 — `KEYPAD_SERIAL_OR_COMMENT_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Prepaid keypad serial number or comment is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:810

<a id="md-e029"></a>

### MD-E029 — `METER_IN_ANOTHER_TEAMS_BATCH`

- **Stage:** Batch ownership guard
- **Message / template:** Refusal identifies the allocated team/provider; exact sentence is assembled from current batch facts.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Return to supervisor for allocation/identity review. Do not relabel a finding to bypass the ownership check.
- **Source:** MD-S44:245

<a id="md-e030"></a>

### MD-E030 — `METER_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Meter number photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:688

<a id="md-e031"></a>

### MD-E031 — `METER_PLACEMENT_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Electricity meter placement is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:322

<a id="md-e032"></a>

### MD-E032 — `METER_READING_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Meter reading photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:724

<a id="md-e033"></a>

### MD-E033 — `METER_READING_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Conventional water meter reading is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck the water subtype and required creation reading/token reading plus its photograph; escalate undefined units rather than guessing.
- **Source:** MD-S41:722

<a id="md-e034"></a>

### MD-E034 — `MISSING_REQUIRED_FIELD`

- **Stage:** Payload validation
- **Message / template:** Template: ${missingField[0]} is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:628

<a id="md-e035"></a>

### MD-E035 — `MISSING_REQUIRED_PARENT`

- **Stage:** Payload validation
- **Message / template:** Template: accessData.parents.${missingParent} is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Preserve the draft and report transaction/queue ID, exact message, route and build. Retry the same record when the underlying condition is resolved.
- **Source:** MD-S41:646

<a id="md-e036"></a>

### MD-E036 — `MM_AST_REFERENCE_CONFLICT`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master is already linked to a different AST
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:281

<a id="md-e037"></a>

### MD-E037 — `MM_CANONICAL_FIELD_MISSING`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master is missing required canonical fields
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:167

<a id="md-e038"></a>

### MD-E038 — `MM_CREATED_METADATA_INVALID`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master creation metadata is invalid
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:206

<a id="md-e039"></a>

### MD-E039 — `MM_DOCUMENT_ID_NONCANONICAL`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master document ID is empty or noncanonical | Meter Master document ID is not canonical
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:142; MD-S51:149

<a id="md-e040"></a>

### MD-E040 — `MM_DOCUMENT_SHAPE_UNSAFE`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master document is not an object | Meter Master canonical shape is unsafe
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:158; MD-S51:179

<a id="md-e041"></a>

### MD-E041 — `MM_GOVERNED_FIELD_TYPE_INVALID`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master contains invalid governed field types | Meter Master update metadata is invalid
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:199; MD-S51:214

<a id="md-e042"></a>

### MD-E042 — `MM_LM_CONFLICT`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master LM conflicts with the operational workflow
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:244

<a id="md-e043"></a>

### MD-E043 — `MM_METER_TYPE_CONFLICT`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master meter type conflicts with the operational workflow
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:252

<a id="md-e044"></a>

### MD-E044 — `MM_NORMALIZED_IDENTITY_CONFLICT`

- **Stage:** Master identity / derivation
- **Message / template:** Meter Master normalized identity conflicts with its document ID | Meter Master raw meter number does not resolve to its canonical identity
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Compare actual number, service and LM with the existing asset. Escalate the identity/schema conflict with transaction ID; do not create a new serial or overwrite master data.
- **Source:** MD-S51:222; MD-S51:235

<a id="md-e045"></a>

### MD-E045 — `NON_CANONICAL_CB_COMMENT_OTHER`

- **Stage:** Payload validation
- **Message / template:** Circuit Breaker comment must contain the canonical custom explanation, not Other
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:796

<a id="md-e046"></a>

### MD-E046 — `NON_CANONICAL_KEYPAD_COMMENT_OTHER`

- **Stage:** Payload validation
- **Message / template:** Keypad comment must contain the canonical custom explanation, not Other
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:814

<a id="md-e047"></a>

### MD-E047 — `NON_CANONICAL_MANUFACTURER_OTHER`

- **Stage:** Payload validation
- **Message / template:** ast.astData.astManufacturer must contain the canonical custom manufacturer, not Other
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:601

<a id="md-e048"></a>

### MD-E048 — `NON_CANONICAL_NO_ACTION_REASON_OTHER`

- **Stage:** Payload validation
- **Message / template:** Type the reason.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:257

<a id="md-e049"></a>

### MD-E049 — `NON_CANONICAL_SEAL_COMMENT_OTHER`

- **Stage:** Payload validation
- **Message / template:** Seal comment must contain the canonical custom explanation, not Other
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:780

<a id="md-e050"></a>

### MD-E050 — `NORMALISATION_ACTIONS_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Say what was done about this finding.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:186

<a id="md-e051"></a>

### MD-E051 — `NORMALISATION_NONE_NOT_EXCLUSIVE`

- **Stage:** Payload validation
- **Message / template:** None cannot be used with another action.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:207

<a id="md-e052"></a>

### MD-E052 — `NORMALISATION_ONE_JOB_ONLY`

- **Stage:** Payload validation
- **Message / template:** Choose one: disconnect or replace.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:214

<a id="md-e053"></a>

### MD-E053 — `NORMALISATION_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Photo proof of Normalisation is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:836

<a id="md-e054"></a>

### MD-E054 — `NORMALISATION_REASON_NOT_EXPECTED`

- **Stage:** Payload validation
- **Message / template:** A reason for not acting belongs to a finding that needs action. | The work was done, so there is no reason for not acting.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:227; MD-S41:237

<a id="md-e055"></a>

### MD-E055 — `NORMALISATION_REASON_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Say why the meter was not disconnected. / Say why the meter was not replaced.
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck finding, one follow-on job at most, on-site fixes and any required reason. If phone accepts choices the server rejects, check release compatibility.
- **Source:** MD-S41:244

<a id="md-e056"></a>

### MD-E056 — `NO_ACCESS_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** No-access photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:580

<a id="md-e057"></a>

### MD-E057 — `NO_ACCESS_REASON_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** No-access reason is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:573

<a id="md-e058"></a>

### MD-E058 — `OFF_GRID_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Off-Grid Supply photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:826

<a id="md-e059"></a>

### MD-E059 — `OFF_GRID_STATUS_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Off-grid supply status is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:753

<a id="md-e060"></a>

### MD-E060 — `PREMISE_NOT_FOUND`

- **Stage:** Discovery callable
- **Message / template:** Parent premise does not exist in premises collection
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Complete or verify the saved parent premise, then reopen the existing discovery draft; do not attach it to a different premise to force acceptance.
- **Source:** MD-S27:3499; MD-S40:3171

<a id="md-e061"></a>

### MD-E061 — `PREMISE_NOT_READY`

- **Stage:** Local queue / connectivity
- **Message / template:** Parent premise is not ready yet. This draft will retry later.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Complete or verify the saved parent premise, then reopen the existing discovery draft; do not attach it to a different premise to force acceptance.
- **Source:** MD-S17:339

<a id="md-e062"></a>

### MD-E062 — `QUEUE_BUSY`

- **Stage:** Local queue / connectivity
- **Message / template:** Queue processing already in progress
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Preserve the draft and report transaction/queue ID, exact message, route and build. Retry the same record when the underlying condition is resolved.
- **Source:** MD-S17:50

<a id="md-e063"></a>

### MD-E063 — `REMAINING_CREDIT_COMMENT_NOT_ALLOWED`

- **Stage:** Payload validation
- **Message / template:** Remaining Credit reason must be blank when a value is captured
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Enter signed decimal balance with its photo, or leave it blank and provide the approved reason. Do not use zero for unknown credit.
- **Source:** MD-S41:473

<a id="md-e064"></a>

### MD-E064 — `REMAINING_CREDIT_COMMENT_OTHER_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Specify the other Remaining Credit reason
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Enter signed decimal balance with its photo, or leave it blank and provide the approved reason. Do not use zero for unknown credit.
- **Source:** MD-S41:501

<a id="md-e065"></a>

### MD-E065 — `REMAINING_CREDIT_COMMENT_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Remaining Credit reason is required when no value is captured
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Enter signed decimal balance with its photo, or leave it blank and provide the approved reason. Do not use zero for unknown credit.
- **Source:** MD-S41:490

<a id="md-e066"></a>

### MD-E066 — `REMAINING_CREDIT_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Remaining Credit photo is required when a value is captured
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:480

<a id="md-e067"></a>

### MD-E067 — `SALES_TB_REFS_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Sales document has an invalid tbRefs field.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:501; MD-S43:1050

<a id="md-e068"></a>

### MD-E068 — `SALES_TB_REF_DUPLICATE`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: The Sales document contains duplicate references to ${tbId}.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:523; MD-S43:1072

<a id="md-e069"></a>

### MD-E069 — `SALES_TB_REF_METER_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Sales Targeted Batch reference points to another meter.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1420

<a id="md-e070"></a>

### MD-E070 — `SALES_TB_REF_NOT_FOUND`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: The Sales document is not linked to ${tbId}.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:516; MD-S43:1065

<a id="md-e071"></a>

### MD-E071 — `SALES_TB_REF_PREMISE_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: The Sales reference for ${tbId} is linked to another premise. | The Sales Targeted Batch reference points to another premise.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:558; MD-S43:1409

<a id="md-e072"></a>

### MD-E072 — `SALES_TB_REF_ROW_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: The Sales reference for ${tbId} belongs to another TB Row.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:540; MD-S43:1083

<a id="md-e073"></a>

### MD-E073 — `SALES_TB_REF_TRN_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Sales Targeted Batch reference points to another TRN.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1431

<a id="md-e074"></a>

### MD-E074 — `SEAL_NUMBER_OR_COMMENT_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Electricity meter seal number or comment is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Correct the named field using the field catalogue; if no valid truthful value is possible, retain the capture and escalate the field/contract gap.
- **Source:** MD-S41:776

<a id="md-e075"></a>

### MD-E075 — `SEAL_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Seal photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:778

<a id="md-e076"></a>

### MD-E076 — `TARGETED_BATCH_ACCESS_DENIED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Targeted Batch access denied.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:996

<a id="md-e077"></a>

### MD-E077 — `TARGETED_BATCH_ALLOCATION_TARGET_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** A TEAM or Service Provider allocation is required.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1006

<a id="md-e078"></a>

### MD-E078 — `TARGETED_BATCH_COMPLETION_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch row is already completed with different linkage.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1639

<a id="md-e079"></a>

### MD-E079 — `TARGETED_BATCH_CONTEXT_INCOMPLETE`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: Targeted Batch premise context is missing: ${missing.join(", ")}.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:469

<a id="md-e080"></a>

### MD-E080 — `TARGETED_BATCH_CONTEXT_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Meter Discovery Targeted Batch context is invalid. | The Meter Discovery TRN carries invalid Targeted Batch context.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1204; MD-S43:1525

<a id="md-e081"></a>

### MD-E081 — `TARGETED_BATCH_ERF_LINK_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch Row points to another ERF. | The premise payload points to another ERF. | The linked premise belongs to another ERF.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:700; MD-S43:707; MD-S43:1145; MD-S43:1159

<a id="md-e082"></a>

### MD-E082 — `TARGETED_BATCH_EXECUTION_COMPLETED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${tbId} has already completed execution. | Template: ${rowId} has already completed execution. | Template: The Sales field work for ${tbId} has already completed.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:272; MD-S43:318; MD-S43:551

<a id="md-e083"></a>

### MD-E083 — `TARGETED_BATCH_EXECUTION_STATE_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${tbId} has unsupported execution status ${executionStatus || "UNKNOWN"}.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:279

<a id="md-e084"></a>

### MD-E084 — `TARGETED_BATCH_LM_SCOPE_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch, TB Row, ERF and premise do not share one LM scope.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:136

<a id="md-e085"></a>

### MD-E085 — `TARGETED_BATCH_METER_DISCOVERY_RESULT_INCOMPLETE`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Meter Discovery result is missing its premise, meter or TRN linkage.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1544

<a id="md-e086"></a>

### MD-E086 — `TARGETED_BATCH_NOT_ACCEPTED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${tbId} has not been accepted for field execution.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:264

<a id="md-e087"></a>

### MD-E087 — `TARGETED_BATCH_NOT_ALLOCATED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${tbId} has not been allocated for field execution.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:256

<a id="md-e088"></a>

### MD-E088 — `TARGETED_BATCH_NOT_ASSIGNED_TO_ACTOR`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch is not assigned to this field user.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1030

<a id="md-e089"></a>

### MD-E089 — `TARGETED_BATCH_NOT_READY`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${tbId} has not completed permanent Targeted Batch creation.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:248

<a id="md-e090"></a>

### MD-E090 — `TARGETED_BATCH_OPERATION_TYPE_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Premise creation is only supported for Meter Discovery Targeted Batch rows.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:480

<a id="md-e091"></a>

### MD-E091 — `TARGETED_BATCH_PARENT_ID_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch parent ID does not match the request.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:669; MD-S43:1110

<a id="md-e092"></a>

### MD-E092 — `TARGETED_BATCH_PREMISE_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${context.rowId} is linked to another premise. | The existing premise belongs to another ERF.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:738; MD-S43:346

<a id="md-e093"></a>

### MD-E093 — `TARGETED_BATCH_PREMISE_CONTEXT_CONFLICT`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The existing premise is linked to another Targeted Batch row.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:363

<a id="md-e094"></a>

### MD-E094 — `TARGETED_BATCH_PREMISE_CONTEXT_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The linked premise does not carry the expected Targeted Batch context.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1169

<a id="md-e095"></a>

### MD-E095 — `TARGETED_BATCH_PREMISE_LINK_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch Row points to another premise.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1152

<a id="md-e096"></a>

### MD-E096 — `TARGETED_BATCH_PREMISE_LINK_MISSING`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** A linked Targeted Batch premise is required.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:1234

<a id="md-e097"></a>

### MD-E097 — `TARGETED_BATCH_ROW_EXECUTION_STATE_INVALID`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${rowId} has unsupported execution status ${executionStatus || "UNKNOWN"}.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:325

<a id="md-e098"></a>

### MD-E098 — `TARGETED_BATCH_ROW_ID_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch Row ID does not match the request.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:683; MD-S43:1124

<a id="md-e099"></a>

### MD-E099 — `TARGETED_BATCH_ROW_NOT_ACCEPTED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${rowId} is not an accepted Targeted Batch row.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:295

<a id="md-e100"></a>

### MD-E100 — `TARGETED_BATCH_ROW_NOT_ALLOCATABLE`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${rowId} is not allocatable.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:303

<a id="md-e101"></a>

### MD-E101 — `TARGETED_BATCH_ROW_NOT_ALLOCATED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${rowId} has not been allocated for field execution.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:310

<a id="md-e102"></a>

### MD-E102 — `TARGETED_BATCH_ROW_PARENT_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch Row belongs to another parent batch.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:676; MD-S43:1117

<a id="md-e103"></a>

### MD-E103 — `TARGETED_BATCH_SALES_LINK_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch Row points to another Sales document. | The Targeted Batch context points to another Sales document.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:693; MD-S43:1131; MD-S43:1138

<a id="md-e104"></a>

### MD-E104 — `TARGETED_BATCH_SCOPE_MISSING`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Template: ${label} does not carry the required LM and ward scope.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:103

<a id="md-e105"></a>

### MD-E105 — `TARGETED_BATCH_USE_NO_ACCESS_FLOW`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Use the Targeted Batch No Access action when the site cannot be accessed.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Use the dedicated Targeted Batch No Access action for this assigned visit. Preserve any existing draft/evidence and resolve the route with the supervisor; do not invent an accessed meter.
- **Source:** MD-S43:1213

<a id="md-e106"></a>

### MD-E106 — `TARGETED_BATCH_WARD_SCOPE_MISMATCH`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** The Targeted Batch, TB Row, ERF and premise do not share one ward scope.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Reopen the assigned row, confirm team/workbase/ERF/premise and current row state; supervisor resolves correlation conflicts. Preserve the original transaction identity.
- **Source:** MD-S43:156

<a id="md-e107"></a>

### MD-E107 — `TOKEN_READING_PHOTO_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Token reading photo is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Capture or restore the photograph for the named evidence tag; verify its URI and upload. An unrelated photo does not satisfy this requirement.
- **Source:** MD-S41:735

<a id="md-e108"></a>

### MD-E108 — `TOKEN_READING_REQUIRED`

- **Stage:** Payload validation
- **Message / template:** Prepaid water token reading is required
- **Record state:** At callable validation this attempt is refused before its write. The same validator also runs during derivation, when a transaction already exists. Check the original ID after any uncertain attempt.
- **Response:** Recheck the water subtype and required creation reading/token reading plus its photograph; escalate undefined units rather than guessing.
- **Source:** MD-S41:733

<a id="md-e109"></a>

### MD-E109 — `UNAUTHENTICATED`

- **Stage:** Batch preparation / submission / derivation
- **Message / template:** Authentication is required.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Sign in with the intended account, preserve the existing draft and retry after the session is restored.
- **Source:** MD-S43:1222

<a id="md-e110"></a>

### MD-E110 — `UNKNOWN_QUEUE_FORM_TYPE`

- **Stage:** Local queue / connectivity
- **Message / template:** This local queue item does not have a recognised form type and cannot be synced safely.
- **Record state:** Depends on calling stage; queued or already accepted records may exist. Check original transaction before retry.
- **Response:** Preserve the draft and report transaction/queue ID, exact message, route and build. Retry the same record when the underlying condition is resolved.
- **Source:** MD-S17:197

## Exceptions requiring further verification

Authentication failures can surface as `unauthenticated` (or a Firebase-prefixed variant); storage and callable infrastructure can return additional codes. Their exact presentation depends on the SDK/build and needs device evidence. A triggered backend failure may appear only as a missing derived record and server diagnostic, not a neat form error.

The core validator's parameterised equipment errors are included. CB/keypad missing-value codes are declared but the reviewed call sites pass `required: false`; do not teach those codes as unconditional blockers. Master codes declared but not exercised by the inspected classification path are not all listed as discovery errors. The register is bounded to the documented source paths and will grow with verified release evidence.
