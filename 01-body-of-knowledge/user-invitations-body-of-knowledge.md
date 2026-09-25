# User Invitations — Body of Knowledge

Module **FRM-021** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](user-invitations-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/invite-a-user.md) · [Field catalogue](user-invitations-field-catalogue.md) · [Error register](user-invitations-error-register.md) · [Practical examples](../10-assessments/user-invitations-scenarios.md)

## Meaning and purpose

User Invitations creates an account for a manager, supervisor or administrator through the authorised office workflow.

Separate screens implement each invited role. Their provider selection and permitted inviter differ. The authentication rule describes a generated, once-displayed initial password and mandatory password change; verify the source variant and delivery method before publishing a task guide.

## Place in the iREPS system

[The meter lifecycle](meter-lifecycle-body-of-knowledge.md) connects business events, custody, field operations and end-of-service decisions. [iREPS Form Standards](ireps-form-standards.md) governs the shared form vocabulary and presentation rules. [The master dictionary](../15-dictionary/iREPS_Master_Dictionary.md) owns terminology.

Administrative actions can affect many people or records. Their scope, actor and result need explicit verification. A filter changing what is visible is different from a mutation changing stored information. Do not infer completion from a modal closing or a row disappearing from a filtered list.

## Actors, prerequisites and handoffs

The learner must identify the person performing the action, the organisation they represent, the active workbase and the specific subject of the action. Fieldworker, supervisor, manager, administrator and Super User responsibilities depend on the action. The Academy does not assert that a higher role inherits every lower-role action.

For this module, the entry and handoff sequence is:

1. Choose the specific role invitation screen.
2. Confirm the person’s identity and email.
3. Select the provider context required for that role.
4. Review and submit once.
5. Pass the invitation result through the organisation’s approved channel and verify pending/onboarding state without publishing the initial credential.

## Data and evidence

| Information | Meaning | Requirement / interpretation |
| --- | --- | --- |
| Name and surname | Invited person’s identity. | Required identity fields in the role-specific form. |
| Email | New account sign-in identifier. | Valid email and server uniqueness; do not invite an existing account to bypass approval. |
| Service Provider | Organisation association where required. | Choices depend on inviter and role; server must recheck permission. |

The [field catalogue](user-invitations-field-catalogue.md) distinguishes business definitions from extracted UI bindings and validation expressions. A keyboard hint, placeholder or displayed value does not prove the server data type. The [error register](user-invitations-error-register.md) distinguishes validation refusal, network uncertainty and partial success.

## Worked explanation

A manager invites a supervisor for the correct provider. The supervisor changes the initial password, then checks the assigned workbase. Being invited does not create an accepted work order.

## Exceptions, maturity and unresolved decisions

Do not publish fixed-password examples from historical code. Verify the once-displayed password behaviour in the target build; invitations and re-invitations can have partial success.

Offline-first submission, acknowledgement, retry and successful-local-record retention are not one completed platform-wide system. QA rejection and financial consequences remain open. Do not turn these gaps into an invented promise of automatic retry, automatic deletion or editable submitted evidence.

## Publication evidence still required

A reviewer must pair mobile and backend revisions, demonstrate the applicable branches with synthetic records, verify the intended role/workbase, inspect persisted outcomes and reconcile exceptions. Retain test evidence under the owning development workstream. This documentation investigation did not run live forms, send communications or modify Firebase records.

## Source evidence

| Source | File | Branch / commit | Working copy |
| --- | --- | --- | --- |
| [FS-022:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-supervisor.js#L1) | `ireps-mobile/app/(tabs)/admin/users/create-supervisor.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-021:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-manager.js#L1) | `ireps-mobile/app/(tabs)/admin/users/create-manager.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-020:1](https://github.com/fikilek/ireps-mobile/blob/74a9497dd162e1168bd96878e2a5fd93da315121/app/(tabs)/admin/users/create-admin.js#L1) | `ireps-mobile/app/(tabs)/admin/users/create-admin.js` | feature/meter-normalisation-v1 / `74a9497dd162` | clean |
| [FS-088:1](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/functions/index.js#L1) | `ireps-web/functions/index.js` | feature/sales-targeted-batch-v3 / `ddd3121e2e82` | clean |
| [FS-059:1](https://github.com/fikilek/ireps-rules/blob/f5dc84e44c9f612fa22f708dcbd2da6fbaafdd1b/auth/auth-rules.md#L1) | `ireps-rules/auth/auth-rules.md` | main / `f5dc84e44c9f` | clean |
