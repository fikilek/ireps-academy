# Meter Vending — Practical Examples and Assessment

Module **FRM-040** · Baseline **25 September 2026** · Application: **Planned; no implemented form found**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../01-body-of-knowledge/meter-vending-body-of-knowledge.md) · [User Manual](../02-user-manual/shared/meter-vending-user-manual.md) · [Field catalogue](../01-body-of-knowledge/meter-vending-field-catalogue.md) · [Error register](../01-body-of-knowledge/meter-vending-error-register.md) · [Practical examples](meter-vending-scenarios.md)

All examples use synthetic identities and are review exercises, not evidence of a passed runtime test.

## Scenario 1 — Explain the business event

Payment succeeds but the token response times out. A future design must query/reconcile that purchase rather than charging again or generating a duplicate transaction.

**Learner task:** identify the subject, event, evidence and next handoff.

**Expected answer:** Meter Vending will record a prepaid purchase and its transaction outcome against the correct meter and customer context. Separate the submitted record from any physical, credential, work or billing outcome it does not prove.

## Scenario 2 — Wrong context

The form opens with a similarly named person, premise, meter or work item from the wrong operational context.

**Expected action:** stop before submission, verify the actual reference and authorised workbase, and use the correct route. For premise/meter tasks, inspect the individual unit and service even when the ERF or enclosure is shared. For account tasks, verify the UID and effective sign-in address.

## Scenario 3 — Conditional data

The learner changes a parent selection or attempts to submit with required information missing.

**Expected action:** use the field catalogue to identify the dependent controls, allowed values and evidence. Do not retain a now-inapplicable value simply to satisfy an unrelated validator.

**Module focus:** Meter/account — Proposed; validate eligibility and identity.

## Scenario 4 — Uncertain outcome

The request starts, then the connection is lost before the result is displayed.

**Expected action:** retain the original identifier and evidence, establish whether the operation reached the server and follow the verified recovery route. Do not create another meter, user, charge or transaction merely because a response was late. For planned forms, specify how this must work before implementation.

## Scenario 5 — Review the implementation boundary

Agree state transitions, permissions, custody/financial audit, duplicate handling and evidence requirements. METER_VENDING is recognised by name but is excluded from the implemented generic lifecycle list; it returns LCT_TYPE_NOT_IMPLEMENTED there.

**Expected action:** state exactly what is observed source, what is documented policy, what is proposed and what a named-environment test still needs to demonstrate.

## Assessment record

For each scenario record: actor and scope; initial record state; inputs and evidence; expected request/result; actual persisted outcome; source/build; reviewer; unresolved discrepancy. Passing requires correct identity/context, truthful outcomes, no fabricated evidence, safe reconciliation of uncertainty and clear explanation of the module-specific gap. No production pass is recorded by this document.
