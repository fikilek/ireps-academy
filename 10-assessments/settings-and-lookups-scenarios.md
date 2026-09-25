# Settings and Lookup Administration — Practical Examples and Assessment

Module **FRM-034** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../01-body-of-knowledge/settings-and-lookups-body-of-knowledge.md) · [User Manual](../02-user-manual/mobile/settings-and-lookups-user-manual.md) · [Field catalogue](../01-body-of-knowledge/settings-and-lookups-field-catalogue.md) · [Error register](../01-body-of-knowledge/settings-and-lookups-error-register.md) · [Practical examples](settings-and-lookups-scenarios.md)

All examples use synthetic identities and are review exercises, not evidence of a passed runtime test.

## Scenario 1 — Explain the business event

An administrator adds a database reason but the current Meter Reading form uses its local shared list. The absence on the phone is a source-of-list mismatch, not a sync failure to be fixed by repeated edits.

**Learner task:** identify the subject, event, evidence and next handoff.

**Expected answer:** Settings and lookup administration maintain supported configuration records and their controlled options. Separate the submitted record from any physical, credential, work or billing outcome it does not prove.

## Scenario 2 — Wrong context

The form opens with a similarly named person, premise, meter or work item from the wrong operational context.

**Expected action:** stop before submission, verify the actual reference and authorised workbase, and use the correct route. For premise/meter tasks, inspect the individual unit and service even when the ERF or enclosure is shared. For account tasks, verify the UID and effective sign-in address.

## Scenario 3 — Conditional data

The learner changes a parent selection or attempts to submit with required information missing.

**Expected action:** use the field catalogue to identify the dependent controls, allowed values and evidence. Do not retain a now-inapplicable value simply to satisfy an unrelated validator.

**Module focus:** Lookup key/domain/field key — Normalised keys in UI; do not rename established codes without migration review.

## Scenario 4 — Uncertain outcome

The request starts, then the connection is lost before the result is displayed.

**Expected action:** retain the original identifier and evidence, establish whether the operation reached the server and follow the verified recovery route. Do not create another meter, user, charge or transaction merely because a response was late. For planned forms, specify how this must work before implementation.

## Scenario 5 — Review the implementation boundary

Map every lookup consumer before changing or retiring options. Common form standards must reference engineering rules rather than create a competing list authority.

**Expected action:** state exactly what is observed source, what is documented policy, what is proposed and what a named-environment test still needs to demonstrate.

## Assessment record

For each scenario record: actor and scope; initial record state; inputs and evidence; expected request/result; actual persisted outcome; source/build; reviewer; unresolved discrepancy. Passing requires correct identity/context, truthful outcomes, no fabricated evidence, safe reconciliation of uncertainty and clear explanation of the module-specific gap. No production pass is recorded by this document.
