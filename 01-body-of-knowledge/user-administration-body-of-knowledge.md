# User Authorisation and Role Management — Body of Knowledge

Module **FRM-022** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-administration-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/user-administration-user-manual.md) · [Field catalogue](user-administration-field-catalogue.md) · [Error register](user-administration-error-register.md) · [Practical examples](../10-assessments/user-administration-scenarios.md)

## Meaning and purpose

User administration associates an authenticated identity with the approved organisation, role and operational access.

Fieldworker authorisation and web role editing are separate actions. A visible status dropdown is not proof that status saving is enabled. The catalogue excludes Guest; SPU means Super User. There is no approved blanket inheritance rule.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Locate the intended user and check their provider and current approval state.
2. Choose the specific action supported in that release: authorise, role change or another implemented action.
3. Review the target role/workbase and the actor’s authority.
4. Confirm and submit; do not treat changing a selector as saving.
5. Reload the user record and verify only the intended changes.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Target user | Existing person being administered. | Verify UID, email and provider; names can duplicate. |
| Role | Functional role of this identity. | Use permitted current roles; Super User is SPU; Guest excluded from current catalogue. |
| Status | User availability/approval status. | Primary web status save remains disabled; do not teach it as working. |
| Workbase | Approved operating areas. | Only assign within the administrator’s actual scope. |

The [field catalogue](user-administration-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](user-administration-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

An office user changes the status selection but Save is disabled. The account has not changed; training must not instruct the learner to proceed as if approval succeeded.

## Exceptions, maturity and unresolved decisions

Capture action-level permissions in a tested matrix. Role labels alone are not authority. Review the current branch against other user-management feature worktrees.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-183:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/users/UsersPage.jsx#L1) | `ireps-web/src/pages/users/UsersPage.jsx` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-019:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/[uid].js#L1) | `ireps-mobile/app/(tabs)/admin/users/[uid].js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-088:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L1) | `ireps-web/functions/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-151:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/helpers.js#L1) | `ireps-web/functions/users/helpers.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-152:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/index.js#L1) | `ireps-web/functions/users/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-153:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/users/updateUserCallable.js#L1) | `ireps-web/functions/users/updateUserCallable.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
