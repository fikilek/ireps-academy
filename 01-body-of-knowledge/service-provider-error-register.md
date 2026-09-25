# Service Provider Registration and Editing — Error Register

Module **FRM-023** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](service-provider-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/service-provider-user-manual.md) · [Field catalogue](service-provider-field-catalogue.md) · [Error register](service-provider-error-register.md) · [Practical examples](../10-assessments/service-provider-scenarios.md)

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

[Complete extracted register with trigger expressions (CSV)](service-provider-error-register.csv). The following index preserves source code/message pairs; shared server entries can apply to more than one module. `LOCAL_MESSAGE` and `dynamic code` are Academy classifications, not server-returned codes.

| ID | Code / classification | Message or resolver expression | Stage / source |
| --- | --- | --- | --- |
| FRM-023-E001 | `LOCAL_MESSAGE` | Trading Name is required. | Client source: handleCreateServiceProvider · [FS-051:63](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormCreateServiceProvider.js#L63) |
| FRM-023-E002 | `LOCAL_MESSAGE` | This manager is not linked to a valid Service Provider. | Client source: handleCreateServiceProvider · [FS-051:68](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormCreateServiceProvider.js#L68) |
| FRM-023-E003 | `LOCAL_MESSAGE` | `${createPayload.tradingName} was created successfully.` | Client source: handleCreateServiceProvider · [FS-051:78](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormCreateServiceProvider.js#L78) |
| FRM-023-E004 | `LOCAL_MESSAGE` | The Service Provider could not be created. | Client source: handleCreateServiceProvider · [FS-051:84](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormCreateServiceProvider.js#L84) |
| FRM-023-E005 | `LOCAL_MESSAGE` | Trading Name is required. | Client source: handleUpdateServiceProvider · [FS-052:112](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormEditServiceProvider.js#L112) |
| FRM-023-E006 | `LOCAL_MESSAGE` | `${updatePayload.patch.profile.tradingName} was updated successfully.` | Client source: handleUpdateServiceProvider · [FS-052:119](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormEditServiceProvider.js#L119) |
| FRM-023-E007 | `LOCAL_MESSAGE` | Service Provider could not be updated. | Client source: handleUpdateServiceProvider · [FS-052:126](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/src/features/serviceProviders/FormEditServiceProvider.js#L126) |
| FRM-023-E008 | `unauthenticated` | Authentication required | Server source: createServiceProvider · [FS-088:559](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L559) |
| FRM-023-E009 | `permission-denied` | Only SPU or ADM may create Service Providers | Server source: createServiceProvider · [FS-088:565](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L565) |
| FRM-023-E010 | `invalid-argument` | Service Provider name is required | Server source: createServiceProvider · [FS-088:600](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L600) |
| FRM-023-E011 | `invalid-argument` | At least one workbase must be assigned | Server source: createServiceProvider · [FS-088:607](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L607) |
| FRM-023-E012 | `unauthenticated` | Authentication required | Server source: updateServiceProvider · [FS-088:672](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L672) |
| FRM-023-E013 | `invalid-argument` | spId and patch are required | Server source: updateServiceProvider · [FS-088:678](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L678) |
| FRM-023-E014 | `not-found` | Service Provider not found | Server source: updateServiceProvider · [FS-088:699](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L699) |
| FRM-023-E015 | `permission-denied` | Managers may only edit their own Service Provider | Server source: updateServiceProvider · [FS-088:711](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L711) |
| FRM-023-E016 | `permission-denied` | Managers may not edit contract-level fields | Server source: updateServiceProvider · [FS-088:722](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L722) |

## Module-specific recovery and unresolved cases

Review hierarchy and status changes with the responsible product workstream. Provider deactivation, existing users and outstanding assignments require explicit transition rules.

Escalation evidence: module, named environment/build, actor role and workbase, subject/transaction identifier, timestamp, exact message, connectivity and known persisted result. Exclude passwords, verification codes and unnecessary customer details.
