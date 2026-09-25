# Geofence Planning — Error Register

Module **FRM-025** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](geofences-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/geofences-user-manual.md) · [Field catalogue](geofences-field-catalogue.md) · [Error register](geofences-error-register.md) · [Practical examples](../10-assessments/geofences-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](geofences-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-025-E001 | `LOCAL_MESSAGE` | Filtering will be implemented next. | Client source: handleFilterPress · [FS-009:269](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L269) |
| FRM-025-E002 | `LOCAL_MESSAGE` | Geofence points must be placed inside the selected ward. | Client source: handleMapPress · [FS-009:292](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L292) |
| FRM-025-E003 | `LOCAL_MESSAGE` | `Geofence "${fenceName}" created successfully.` | Client source: handleSave · [FS-009:329](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L329) |
| FRM-025-E004 | `LOCAL_MESSAGE` | err?.message &#124;&#124; "Failed" | Client source: handleSave · [FS-009:336](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L336) |
| FRM-025-E005 | `LOCAL_MESSAGE` | `The geofence "${geoFence?.name &#124;&#124; "Unknown"}" has no location data to zoom to.` | Client source: handleOpenGeoFenceOnMap · [FS-009:362](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/operations/geo-fences.js#L362) |
| FRM-025-E006 | `unauthenticated` | Authentication is required. | Server source: createGeoFenceRequest · [FS-081:28](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/callables.js#L28) |
| FRM-025-E007 | `invalid-argument` | nameCheck.reason | Server source: createGeoFenceRequest · [FS-081:38](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/callables.js#L38) |
| FRM-025-E008 | `invalid-argument` | A geofence must have at least 3 valid coordinate points. | Server source: createGeoFenceRequest · [FS-081:58](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/callables.js#L58) |
| FRM-025-E009 | `already-exists` | duplicateGeofenceNameMessage(duplicate) | Server source: createGeoFenceRequest · [FS-081:70](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/callables.js#L70) |
| FRM-025-E010 | `invalid-argument` | Geofence name is required. | Server source: validateCreateGeoFencePayload · [FS-083:50](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L50) |
| FRM-025-E011 | `invalid-argument` | A geofence must have at least 3 points. | Server source: validateCreateGeoFencePayload · [FS-083:54](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L54) |
| FRM-025-E012 | `invalid-argument` | Local Municipality is required. | Server source: validateCreateGeoFencePayload · [FS-083:61](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L61) |
| FRM-025-E013 | `invalid-argument` | Ward is required. | Server source: validateCreateGeoFencePayload · [FS-083:65](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L65) |
| FRM-025-E014 | `not-found` | Actor user profile not found. | Server source: getActorUserDoc · [FS-083:322](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L322) |
| FRM-025-E015 | `permission-denied` | Supervisor is not linked to a valid service provider. | Server source: assertCanCreateGeoFence · [FS-083:392](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L392) |
| FRM-025-E016 | `permission-denied` | Supervisor service provider could not be resolved. | Server source: assertCanCreateGeoFence · [FS-083:403](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L403) |
| FRM-025-E017 | `permission-denied` | Only MNC supervisors may create geofences. | Server source: assertCanCreateGeoFence · [FS-083:410](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L410) |
| FRM-025-E018 | `permission-denied` | You are not allowed to create geofences. | Server source: assertCanCreateGeoFence · [FS-083:419](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/geofences/helpers.js#L419) |

## Module-specific recovery and unresolved cases

Geometry validation and role scope are release-specific. Do not interpret a boundary selection as allocation or acceptance of work.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
