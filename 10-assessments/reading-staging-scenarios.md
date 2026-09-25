# Meter Reading Staging and Export — Practical Examples and Assessment

Module **FRM-032** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](../01-body-of-knowledge/reading-staging-body-of-knowledge.md) · [User Manual](../02-user-manual/web/reading-staging-user-manual.md) · [Field catalogue](../01-body-of-knowledge/reading-staging-field-catalogue.md) · [Error register](../01-body-of-knowledge/reading-staging-error-register.md) · [Practical examples](reading-staging-scenarios.md)

All examples use synthetic identities and are review exercises, not evidence of a passed runtime test.

## Scenario 1 — Explain the business event

The office generates 98 usable readings from 100 planned visits; two are No Access. The export contains reviewed readings, while the exceptions remain visible and the external billing team acknowledges its import.

**Learner task:** identify the subject, event, evidence and next handoff.

**Expected answer:** Meter Reading Staging prepares captured conventional readings for review and delivery to an external billing system. Separate the submitted record from any physical, credential, work or billing outcome it does not prove.

## Scenario 2 — Wrong context

The form opens with a similarly named person, premise, meter or work item from the wrong operational context.

**Expected action:** stop before submission, verify the actual reference and authorised workbase, and use the correct route. For premise/meter tasks, inspect the individual unit and service even when the ERF or enclosure is shared. For account tasks, verify the UID and effective sign-in address.

## Scenario 3 — Conditional data

The learner changes a parent selection or attempts to submit with required information missing.

**Expected action:** use the field catalogue to identify the dependent controls, allowed values and evidence. Do not retain a now-inapplicable value simply to satisfy an unrelated validator.

**Module focus:** Municipality/workbase — Check the active workbase and explicit municipality code.

## Scenario 4 — Uncertain outcome

The request starts, then the connection is lost before the result is displayed.

**Expected action:** retain the original identifier and evidence, establish whether the operation reached the server and follow the verified recovery route. Do not create another meter, user, charge or transaction merely because a response was late. For planned forms, specify how this must work before implementation.

## Scenario 5 — Review the implementation boundary

Owner states this module needs strengthening before production readiness. Automated billing-system integration and full customer billing remain future work. Do not invent an approval button where the page only filters or downloads.

**Expected action:** state exactly what is observed source, what is documented policy, what is proposed and what a named-environment test still needs to demonstrate.

## Assessment record

For each scenario record: actor and scope; initial record state; inputs and evidence; expected request/result; actual persisted outcome; source/build; reviewer; unresolved discrepancy. Passing requires correct identity/context, truthful outcomes, no fabricated evidence, safe reconciliation of uncertainty and clear explanation of the module-specific gap. No production pass is recorded by this document.
