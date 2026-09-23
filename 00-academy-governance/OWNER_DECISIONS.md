# Owner decisions and open questions

Source: the owner's Academy conversation and approved consolidation proposal, 23 September 2026. This register distinguishes decisions from proposals; source code observations do not silently resolve policy.

| ID | Topic | Status | Direction |
| --- | --- | --- | --- |
| DEC-001 | Academy ownership | Confirmed | This Codex Academy task owns structure, dictionary and training content. Other agents contribute through a coordinated handover. |
| DEC-002 | SPU | Confirmed | The exact name is **Super User**. |
| DEC-003 | Guest | Confirmed for current catalogue | Exclude Guest/GST from current roles. Preserve historical mentions only in clearly marked source evidence. No runtime-role change is authorised here. |
| DEC-004 | Permission inheritance | Open | Do not assert automatic inheritance. An action-by-action model by organisation, role, workbase and assignment still needs discussion. |
| DEC-005 | Common offline system | Accepted direction; design incomplete | Every server-bound submission should first be stored locally. Attempt transmission when online. Retain local data if offline or unresolved. Existing behaviour is not yet a complete implementation of this model. |
| DEC-006 | 15-second attempt | Proposed target within offline design | Stop waiting on a submission attempt after 15 seconds and retain the local record. Timeout does not prove non-arrival at the server; acknowledgement, duplicate-safe retry and late-response handling need design. |
| DEC-007 | Offline retention | Open | Automatic retry rules, successful acknowledgement, local deletion/retention, device loss and storage management are not settled. Do not promise deletion or automatic transmission for every form. |
| DEC-008 | QA | Planned; not implemented as a module | Mainly web review of transactions submitted through mobile, with pass/fail and correction handling. Submitted evidence must remain trustworthy for payment, salaries and invoices. |
| DEC-009 | QA correction approach | Proposal only | Linked immutable correction submissions could preserve the original while enabling rework. This is not an approved implementation. Identity, uniqueness, idempotency, approval and financial consequences remain open. |
| DEC-010 | Environments and Trials | Confirmed | Current servers are DEV, TEST and LIVE. Trials has not started; configuration labels do not establish a working service. Planned journey: signup, approval, selected wards, time-limited trial, contract and transition to LIVE. |
| DEC-011 | Manual meter reading | Existing, needs strengthening | Fieldworkers use mobile devices and GPS to capture electricity/water readings. Readings are prepared for an authorised export to the billing system. Production readiness still needs work. |
| DEC-012 | Billing integration | Future | Automated backend exchange with billing systems is future work. Full iREPS customer billing is also a roadmap item. |
| DEC-013 | Feature availability | Evidence required | A placeholder may coexist with completed code on another branch. Record implementation, environment deployment and acceptance separately. |
| DEC-014 | Initial learning priorities | Agreed | Foundations/onboarding; fieldworker guides; supervisor/manager guides; web manual; electricity and water revenue courses. |
| DEC-015 | Consolidation and backup | Approved | Preserve existing Academy work, establish governance, consolidate learning material, verify references, commit, merge, push and verify GitHub. This does not approve application or data deployment. |
| DEC-016 | Module knowledge standard | Owner direction, 23 September 2026 | Every module has a comprehensive Body of Knowledge and a separate User Manual. Include diagrams, full field definitions, prerequisites, validations, errors, routes and all-role/customer explanations. Start with Meter Discover; existing application term Meter Discovery remains an alias. |

## Questions to resolve with product workstreams

1. Which actions may each organisation/role perform, and which are inherited, delegated or assignment-specific?
2. How does the server acknowledge a durable submission, and how does the device reconcile a timed-out attempt before retrying?
3. Which local records can be removed, when, and with what recovery and audit requirements?
4. Does QA rejection create a correction request, a new transaction/revision or a return visit? Which data become operationally effective at each stage?
5. How do meter-number corrections preserve unique identity and handle collisions with real existing meters?
6. How do QA outcomes and corrected submissions affect already calculated, approved or paid work?
7. What evidence marks a workflow production-ready, and which release should each guide teach?

These questions are documentation requirements, not implementation instructions. Pending answers remain open rather than being filled by guesses.
