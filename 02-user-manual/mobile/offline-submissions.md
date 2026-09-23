# Offline submissions

Status: current behaviour varies; common design pending. This is not a promise of a fully implemented offline system.

## Current teaching boundary

Follow the named release's form-specific instructions. Saving locally, attempting transmission and receiving server acknowledgement are separate events. Current inspection code has explicit saved/not-sent outcomes. The inspected application has several queue services; their existence does not prove universal automatic retry or safe local deletion.

Check the form's result and the relevant local submission queue. Do not assume that reconnecting sends every type of saved form. Do not uninstall or clear application storage while unsubmitted work is present. A future operational guide must state the exact supported recovery steps for each form and release.

## Owner's intended common model

1. Store every server-bound submission locally first.
2. If connected, attempt submission; if offline, retain it locally.
3. If an attempt exceeds the proposed 15 seconds, stop waiting and retain the unresolved record.
4. Reconcile acknowledgement and retry under the policy still to be agreed.

The server may complete a request after the device stops waiting. Timeout must not automatically be described as rejection. Retry identity, late acknowledgement, duplicate prevention and reconciliation remain design questions.

Whether an acknowledged submission is automatically deleted, retained for a period or archived locally is undecided. No automatic deletion rule is approved here.

See [DEC-005 through DEC-007](../../00-academy-governance/OWNER_DECISIONS.md). The 27 September scripts are version-specific drafts and do not override this status.
