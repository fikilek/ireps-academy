# Informal ERF Capture — Error Register

Module **FRM-012** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](informal-erf-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/informal-erf-user-manual.md) · [Field catalogue](informal-erf-field-catalogue.md) · [Error register](informal-erf-error-register.md) · [Practical examples](../10-assessments/informal-erf-scenarios.md)

## How to interpret this register

Academy IDs identify documentation entries; they are not runtime codes. Source messages can be dynamic templates. Informational or success notifications found beside errors are labelled source messages and must not be counted as failures. A refusal before the business commit differs from an unknown outcome after a network timeout.

| Situation | Meaning / data state | User response |
| --- | --- | --- |
| Local validation | The current attempt has not passed the form validator; a prior draft or prior attempt can still exist. | Correct the named field and recheck dependent fields/evidence. |
| Server permission/state refusal | The request was refused at a checked condition; inspect the code-specific stage before asserting that nothing at all was saved. | Retain the reference and resolve authority, subject or state; do not bypass the check with another identity. |
| Timeout or dropped connection | Outcome can be uncertain; late processing may succeed. | Reconcile the original attempt and use the workflow’s duplicate-safe recovery path when verified. |
| Local save or media failure | The intended evidence or draft may not be durable yet. | Retain the screen/context and verify storage/upload before leaving. |
| Partial success | One system step may have succeeded while a later write failed. | Follow the effective credential/record state and escalate the incomplete step with identifiers. |

## Source error and message evidence

[Complete extracted register with trigger expressions (CSV)](informal-erf-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-012-E001 | `LOCAL_MESSAGE` | The Informal ERF boundary is captured, but iREPS has not yet captured the phone GPS required for the forensic submission record. Keep location enabled, return to the map, and try again. | Client source: FormInformalErf · [FS-041:501](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L501) |
| FRM-012-E002 | `LOCAL_MESSAGE` | submissionResult?.duplicate<br>              ? "This Informal ERF was already created. No duplicate was added."<br>              : `The Informal ERF was created successfully.\n\n${submissionResult?.erfId &#124;&#124; ""}` | Client source: FormInformalErf · [FS-041:556](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L556) |
| FRM-012-E003 | `LOCAL_MESSAGE` | submissionResult?.message &#124;&#124;<br>              "The Informal ERF is saved on this device and will submit automatically when the network is available." | Client source: FormInformalErf · [FS-041:573](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L573) |
| FRM-012-E004 | `LOCAL_MESSAGE` | submissionResult?.message &#124;&#124;<br>              "The server rejected this Informal ERF." | Client source: FormInformalErf · [FS-041:589](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L589) |
| FRM-012-E005 | `LOCAL_MESSAGE` | submissionResult?.message &#124;&#124;<br>            "The Informal ERF could not be submitted or saved locally." | Client source: FormInformalErf · [FS-041:598](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/erfs/FormInformalErf.js#L598) |
| FRM-012-E006 | `error?.code` | error?.message | Client source: submitInformalErfOnline · [FS-055:445](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L445) |
| FRM-012-E007 | `code` | message | Client source: getInformalErfErrorDetails · [FS-055:526](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L526) |
| FRM-012-E008 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:629](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L629) |
| FRM-012-E009 | `OFFLINE` | queueResult?.success<br>        ? "No network was available. The Informal ERF was saved locally."<br>        : queueResult?.message | Client source: submitInformalErfWithFallback · [FS-055:659](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L659) |
| FRM-012-E010 | `onlineResult?.result?.code &#124;&#124; "INFORMAL_ERF_CREATED"` | onlineResult?.result?.message &#124;&#124;<br>        "Informal ERF created successfully." | Client source: submitInformalErfWithFallback · [FS-055:676](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L676) |
| FRM-012-E011 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:695](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L695) |
| FRM-012-E012 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:701](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L701) |
| FRM-012-E013 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:713](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L713) |
| FRM-012-E014 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:719](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L719) |
| FRM-012-E015 | `errorInfo.code` | errorInfo.message | Client source: submitInformalErfWithFallback · [FS-055:733](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L733) |
| FRM-012-E016 | `errorInfo.code` | queueResult?.success<br>        ? "The server is temporarily unavailable. The Informal ERF was saved locally and will retry automatically."<br>        : queueResult?.message | Client source: submitInformalErfWithFallback · [FS-055:746](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/services/informalErfSubmissionController.js#L746) |
| FRM-012-E017 | `invalid-argument` | message | Server source: throwInvalidArgument · [FS-090:63](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L63) |
| FRM-012-E018 | `permission-denied` | message | Server source: throwPermissionDenied · [FS-090:71](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L71) |
| FRM-012-E019 | `failed-precondition` | message | Server source: throwFailedPrecondition · [FS-090:79](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L79) |
| FRM-012-E020 | `already-exists` | message | Server source: throwAlreadyExists · [FS-090:87](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L87) |
| FRM-012-E021 | `unavailable` | The Informal ERF exists, but geofence counts could not be refreshed. Retry safely with the same erfId. | Server source: refreshMatchedGeoFenceCountsOrThrow · [FS-090:234](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L234) |
| FRM-012-E022 | `unavailable` | The Informal ERF exists, but the ERF registry could not be refreshed. Retry safely with the same erfId. | Server source: refreshErfRegistryProjectionOrThrow · [FS-090:296](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L296) |
| FRM-012-E023 | `unavailable` | The Informal ERF exists, but the Ward Registry could not be refreshed. Retry safely with the same erfId. | Server source: refreshWardRegistryProjectionOrThrow · [FS-090:369](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L369) |
| FRM-012-E024 | `duplicate<br>      ? "INFORMAL_ERF_ALREADY_CREATED"<br>      : "INFORMAL_ERF_CREATED"` | duplicate<br>      ? "This Informal ERF was already created."<br>      : "Informal ERF created successfully." | Server source: buildSuccessResult · [FS-090:385](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L385) |
| FRM-012-E025 | `unauthenticated` | Authentication is required. | Server source: submitInformalErfCallable · [FS-090:410](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L410) |
| FRM-012-E026 | `internal` | The Firebase Storage bucket is not configured. | Server source: submitInformalErfCallable · [FS-090:458](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L458) |
| FRM-012-E027 | `internal` | The Informal ERF could not be created. | Server source: submitInformalErfCallable · [FS-090:924](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/informal-erfs/submitInformalErfCallable.js#L924) |

## Module-specific recovery and unresolved cases

Operational geometry must not be described as cadastral proof. Confirm overlap handling, queue recovery and server validation on the intended release.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
