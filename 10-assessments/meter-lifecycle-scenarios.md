# Meter Lifecycle — Practical Scenarios

Review draft, 25 September 2026. These are synthetic business/design exercises. They are not executed tests or approved procurement policies. Read the [Body of Knowledge](../01-body-of-knowledge/meter-lifecycle-body-of-knowledge.md) first.

| Scenario | Learner task | Expected explanation and evidence |
| --- | --- | --- |
| Ten ordered; nine delivered; one damaged | Reconcile the proposed stock receipt | Ten ordered, nine physically received, eight accepted for ordinary stock, one held and one outstanding; link PO, delivery and receipt |
| Supplier paid; no delivery yet | Explain meter availability | Payment evidence exists; physical stock has not been established |
| Store A dispatches five; three installed | Account for the other two | Preserve dispatch identities; record unused return, transfer or unresolved exception rather than claiming five installations |
| Meter moves between two stores | Preserve identity and custody | Link issue and receipt by transfer; retain one serial/asset identity; explain transit discrepancies |
| Existing meter discovered without records | Register honestly | Meter Discovery records observed facts; do not fabricate procurement or installation history |
| Meter in an outside shared kiosk | Identify the correct served unit | Keep actual physical position separate from premise/ERF/account association |
| Prepaid commissioning has one failed check | Distinguish acceptance from pass | A valid form can record unsuccessful commissioning; under the inspected validator FIELD remains |
| Reading blank display | Avoid a false zero | Record a supported no-reading reason with evidence; absence of a reading is not zero consumption |
| Disconnection issued but gate locked | Separate work and asset states | Instruction progress and No Access do not prove a physical disconnection |
| Replace A with B | Preserve two histories | Removal/final reading belong to A; installation/initial reading belong to B; retain replacement links and service gap |
| Removed meter held for investigation | Explain store and operational state | Physically returned is not automatically fit for issue; removal, return, retirement and disposal dates can differ |
| Previously removed meter proposed for reuse | Identify the design gap | Agree identity/service reassociation and commissioning rules; never invent another serial to bypass uniqueness |
| Submission times out after server commit | Prevent duplication | Reconcile the original attempt and its identifier before another request; local timeout is not rollback |
| QA fails paid work | Identify unresolved consequences | Preserve original evidence, define correction and approval effects, and resolve financial reconciliation; no approved automatic reversal is claimed |
| Vending payment succeeds but token response is lost | Define future recovery | Separate payment, vending and delivery outcomes; query/reconcile before charging again |

For each scenario record the actor, organisation, workbase/store, meter identity, before/after facts, transaction/document references, observation time, acceptance time, evidence and unresolved decision. A correct answer must distinguish **owner direction**, **source behaviour**, **proposed design** and **verified release**.

Publication requires product review of the proposed stages and named-environment acceptance for operational forms. No learner is instructed to perform live payments, physical meter work or irreversible disposal as part of these exercises.
