# Meter Discover — mobile user manual

**MDIS-UM · version 0.2 · review draft.** This guide follows the recorded mobile normalisation feature, with the branch differences and unresolved behaviour listed in the [source baseline](../../00-academy-governance/source-assessments/meter-discover-source-baseline-2026-09-23.md). It must be walked through on the intended release before field publication. Screens may still say **Meter Discovery**.

For explanations use the [Body of Knowledge](../../01-body-of-knowledge/meter-discover-body-of-knowledge.md). For mounting examples use the [placement image guide](../../01-body-of-knowledge/meter-discover-body-of-knowledge.md#placement-examples-context-and-closer-views). For any field's detailed meaning, allowed values or photograph requirement use the [field catalogue](../../01-body-of-knowledge/meter-discover-field-catalogue.md). For refusals and recovery use the [error register](../../01-body-of-knowledge/meter-discover-error-register.md).

## 1. Before starting

Confirm your signed-in account, organisation, active workbase and intended environment. Check that the ERF and premise you are about to use describe the service location. A premise is required; an ERF alone is not the parent record for a meter. If working from My Work Orders, use your assigned/accepted batch and the relevant row.

Have the device permissions needed for camera/location and any optional recording. Know where to find local queued forms. Do not assume that an offline dropdown implies the entire workflow is ready to complete offline. This manual does not grant authority to disconnect, remove, install or interfere with service equipment; follow-on work uses its own assigned task and procedure.

## 2. Choose the entry path

The only names for these entry paths are **Normal Path** and **Sales Path**, as defined in the [master dictionary](../../15-dictionary/iREPS_Master_Dictionary.md#meter-discover-entry-paths). Reopening a saved draft continues its original path.

### A. Normal Path

1. Select the correct municipality/ward and ERF through the available geography/navigation controls.
2. Open its **Premises** and select the actual service premise, or create the required premise using the premise workflow.
3. Verify the address, property type and unit. A shared ERF can contain several premises. Use the [property-type examples](../../01-body-of-knowledge/meter-discover-body-of-knowledge.md#property-type-case-index) to distinguish the type grouping from each individual premise.
4. Start the meter discovery action. Choose electricity or water if access is available, or choose the No Access route if it is not.
5. Check the premise address and ERF number shown by the form before entering the meter details.

If the parent premise is still only on the device, you can encounter a Saved as Draft result. The discovery cannot be submitted to the server until the parent premise is saved. Do not select another premise merely to remove the blocker.

### B. Sales Path

1. Open the accepted work in **My Work Orders** and select the relevant row.
2. Follow the row to the correct ERF/premise. Keep the expected Sales meter and assigned work context.
3. Check the meter actually present. An electricity number may be prefilled from the target; it still needs physical verification.
4. If offered a choice between the batch meter and another meter, choose truthfully. Do not retype the expected number over a different physical serial.
5. Continue through the same accessed electricity/water capture steps below. If access is unavailable, use the batch's dedicated **No Access** action; the inspected backend rejects a generic discovery carrying batch context with No Access and directs you to that separate route.
6. After submission, verify both the found meter and the work-row outcome. A different-meter completion must retain the distinction between expected and found.

Batch checks can refuse work for another team or refuse when allocation cannot be verified. Going through the Normal Path is not a reliable or authorised workaround. Ask the supervisor to resolve assignment or correlation.

### C. Resume a local draft

Open the existing item in **Admin → Offline Submission Forms** (the queue screen route is `admin/storage/forms-submission-queue`). Confirm the transaction and premise context. Correct the unsent draft and submit that same item. A queued form's edit mode is not an editor for submitted transactions. If the item is missing or already successful, establish the server outcome before creating a replacement capture.

## 3. Accessed electricity discovery

### Identify the equipment

1. Type or scan **Meter Number**. Compare the result with the physical serial. Spaces are removed and lowercase ASCII letters become capitals; leading zeros remain significant.
2. Capture the **meter number photo** so the actual serial can be checked.
3. Select **Manufacturer**. For Other, enter the actual manufacturer in **Other Manufacturer**. Enter **Model (Name)**.
4. Select **Phase**, **Type** (prepaid/conventional) and **Category** (Normal/Bulk). Select what is observed rather than accepting a default without checking.

A duplicate warning means the number appears in loaded records; a server master conflict can also occur later. Verify the existing record. If the serial is genuinely unreadable, do not invent a number: record/escalate the identification problem through the responsible supervisor.

### Associated equipment and prepaid credit

5. Record the **Seal No**, or choose the reason it cannot be recorded. If Other, explain. Capture a seal photo when the field catalogue requires it.
6. For a prepaid meter, record **Keypad Serial No** or an applicable explanation where needed. The reviewed schema allows both to be blank; that is a current implementation fact, not a recommendation to omit useful information.
7. Record **CB Size (Amps)** or a relevant explanation where available. Capture the corresponding photo when a value or evidence-requiring reason is supplied.
8. For prepaid meters, record **Remaining Credit** and its photograph, or leave the value blank and select the reason it cannot be captured. Use a signed decimal without a unit suffix. Zero means zero; it does not mean unknown.

Switching the subtype to conventional clears remaining-credit inputs and removes their photo from the canonical payload. Recheck dependent fields after changing subtype.

### Location, state and findings

9. Select **Meter Placement**. Use the physical mounting arrangement, such as Kiosk, Pole Top or Boundary Wall. Explain an Other location in Field Comment.
10. Open **Meter GPS Position**, place/confirm the pin at the meter's actual position and check it before continuing. The meter may be outside the ERF it serves; do not force the pin to the parcel centre.
11. Select the observed **Meter Status**: Connected or Disconnected.
12. Answer **Off-Grid Supply?** and provide its photograph when Yes.
13. Select the **finding/anomaly** and its **detail**. Add the required anomaly photo. Meter Ok with Bridge Suspicion or Bypass Suspicion still needs evidence.
14. Select any applicable **Other Anomalies**. These supplement the primary finding.

### Response and commentary

15. Review **Normalisation**. The mobile feature can preselect Disconnect meter for Illegally Connected, or Replace meter for Faulty/Damaged. Confirm the intended work; a preselected tick is not proof that it has occurred.
16. Select any actual on-site fixes and provide the required normalisation photograph. At most one follow-on job can be selected; None cannot be combined with other actions.
17. If the expected job is not selected, give the **Reason for not acting**, including text for Other. Selecting a different action does not remove that reason requirement.
18. Add useful **Field Comment** text and optional photo/voice/video evidence for ambiguity, enclosure context or an unresolved issue. Optional evidence does not replace required tagged photos.

## 4. Accessed water discovery

1. Confirm the premise and water service route.
2. Record the meter number and its photograph, category, subtype, manufacturer and model.
3. For a **conventional** water meter, enter the displayed **Meter Reading** and photograph it.
4. For **prepaid** water, the inspected form asks for **Token Reading** and its photograph, plus **Remaining Credit** or a reason. The distinction and units need clarification before publication; do not assume they are interchangeable.
5. Select Connected/Disconnected, finding/detail and any other anomalies; supply the applicable finding photograph.
6. Confirm actual GPS location and add helpful field commentary.
7. Review and submit using the common procedure below.

The current water form has no electricity placement, phase, seal/keypad/CB or electricity normalisation controls. Its manufacturer list includes Other but lacks the electricity custom-manufacturer helper; the server rejects bare Other. If that is the truthful choice, escalate the mismatch rather than selecting a false listed manufacturer.

## 5. No Access visit

1. Use the No Access entry action for the correct premise/visit.
2. Choose the reason that describes the actual access limitation. For Other, supply the explanation.
3. Capture **No Access photo** evidence supporting that limitation.
4. Add optional field comment/media if helpful.
5. Submit and read the specific result. The reviewed No Access path attempts to preserve the queue item and evidence locally before transmission.

A No Access visit records an attempted visit; it does not create a discovered meter or establish a meter condition you could not observe. A batch can also have a separate No Access action with its own route/endpoint. Do not assume that every button labelled No Access uses this discovery form; that related workflow needs its own guide.

## 6. Review, submit and interpret the result

Before pressing **SUBMIT**, check the premise/ERF, actual serial, service/subtype, GPS pin, connection state, finding/detail, selected response and all evidence. Resolve the displayed Submit blockers.

The owner's standard calls for a confirmation before submission, progress during it and a result afterwards. The inspected discovery footer currently invokes submission directly; a universal pre-submit confirmation window is not established by this source. Perform the review yourself and record this UI gap for development.

Press Submit and read the complete outcome:

| Result | Meaning and next action |
| --- | --- |
| Saved as Draft | Parent premise is not ready; inspect local item and save/sync parent |
| Saved Offline / Saved Locally | Local retention or unconfirmed online outcome; verify queue item and preserve the original transaction |
| Draft Save Failed | Local safety is not established; keep the form/evidence and escalate |
| Submission Failed | Read exact message; correct a truthful input or resolve the identified conflict |
| Server-confirmed success | Check the resulting meter/transaction; derived records can take time |
| Preparing the disconnection/removal | Discovery accepted; app is waiting for the asset needed by the next job |
| Meter saved, work still to do | Open the indicated job from the meter card when available; do not rediscover |

The generic **MISSION SUCCESS** display can appear after some local-save branches. The specific message and queue/server state take precedence over the green icon. A timeout does not establish that the server rejected the submission.

**RESET** clears the current form after its confirmation. The warning refers to captured form data; it is not a command to delete an existing server transaction. Do not reset merely to resolve an uncertain submission outcome.

## 7. Complete follow-on work

When the newer electricity normalisation feature is correctly paired with its backend, a confirmed discovery can open the separate disconnection form, or removal followed by installation. Check the carried meter, premise and originating discovery. Complete each authorised job under its own manual; do not report a replacement as finished because Replace meter was selected on discovery.

If your role cannot perform the field job, the result directs the responsible office process to issue it. If only a local draft exists, the automatic follow-on cannot start yet. After background sync, verify the meter and outstanding work; automatic resumption of the next screen has not been established.

## 8. Verify before leaving the task

For an accessed capture, check the expected transaction and actual meter identity, associated premise, physical location and observed state. For Sales/batch work, check expected-versus-found correlation and row outcome. Verify a selected follow-on job separately. For No Access, confirm a visit outcome rather than expecting a new asset.

If the app is offline, verify that the local item and necessary evidence exist. Do not clear app storage, reinstall, delete evidence or create a new discovery as a way to force an uncertain submission through. The product-wide retention/recovery policy is still under discussion.

## 9. Supervisor and support review

Check the original capture and evidence, the meter/master identity, parent relationships, route/assignment and any outstanding derived or linked work. A spelling mistake in a submitted meter number needs a controlled correction decision. The QA module is planned; this guide does not provide a QA reject/edit/resubmit workflow that is not yet implemented.

Use the [error register](../../01-body-of-knowledge/meter-discover-error-register.md) and [acceptance scenarios](../../10-assessments/meter-discover-scenarios.md). Keep the transaction ID, exact message, build/environment and a clear account of what was observed, sent, saved locally and seen afterwards.
