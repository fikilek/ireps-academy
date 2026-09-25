# Forms investigation — 25 September 2026

This pass extends the Academy from one detailed Meter Discovery module to **41 module families**, each with a Body of Knowledge, User Manual, Field Catalogue, Error Register and Practical Examples. It also adds the standalone Meter Lifecycle chapter and iREPS Form Standards. These are review drafts, not a claim of complete field-by-field release certification.

## Scope and method

The inventory searched **23 C:/dev roots**, including primary mobile/web, available mobile-auth/email/forms/work-order and web-email/forms/GMR/normalisation worktrees, rules, schemas, pipelines, Academy and website. The [repository scope](FORMS_REPOSITORY_SCOPE.csv) records branches and commits. The extension-limited search considered **5673 files** and found **645 UI/source candidates**, including repeated branch variants and historical copies. Counts are not unique application forms.

The search used routes, form/submit/input/select/textarea markers and callable/mutation references. Static JavaScript/JSX syntax parsing then extracted input bindings, option expressions, conditional context, local validation and error/message expressions. Manual review covered the core lifecycle validators, authentication rules, premise registration/account forms, commissioning, current workflow handover and shared UI rules. Supporting source selection covers **183 files** with SHA-256, commit and working-copy status.

The [candidate inventory](FORM_SOURCE_CANDIDATES.csv) separates business form/action families, shared controls, view filters, historical copies and feature variants. Additional unmatched candidates: **0**. Controls without an obvious form element can still be action-driven; manually selected onboarding screens and backend sources are in the separate source baseline. The scan is a bounded source inventory, not proof that every dynamically composed field, route or runtime permission has been exercised.

Excluded from content inspection: dependencies, build output, credentials, environment secrets, bulk customer/auth exports, fixtures and diagnostic data. No Firebase/live data were queried. Non-code document roots were listed for context; this pass did not claim a semantic review of every binary or archived document. A registered meter-number worktree outside C:/dev was noted as an additional variant; it is not silently counted as a fully scanned C:/dev root.

## What was produced

- [Form library](../01-body-of-knowledge/forms-library.md): 41 families, including the existing Meter Discovery package and 40 new/expanded packages.
- [Module inventory](FORM_MODULE_INVENTORY.csv): canonical destinations, application/content status and remaining questions.
- [Meter Lifecycle](../01-body-of-knowledge/meter-lifecycle-body-of-knowledge.md): procurement, document flow, stores/custody, registration, operation, replacement and end of service, with four diagrams and worked examples.
- [iREPS Form Standards](../01-body-of-knowledge/ireps-form-standards.md): confirmed rules, source differences and proposed common contracts, with a validation-layer diagram.
- Source controls and validation expressions are retained in per-module catalogues/CSVs. Error registers include exact codes/templates and source notifications; notification extraction is not a count of failures.

## Findings that materially affect training

| Finding | Evidence / consequence |
| --- | --- |
| Procurement, physical stores and disposal forms were not established | Six proposed packages cover procurement, check-in, check-out, return, retirement/disposal and vending; do not show invented current buttons |
| Installation registers FIELD; commissioning is separate | Dedicated commissioning checks can yield an accepted but unsuccessful result; CONNECTED requires a pass |
| Discovery is a separate lifecycle entry | Existing network assets must not acquire fictitious procurement/installation history |
| Vending is named but not implemented in the generic lifecycle service | It is absent from IMPLEMENTED_LIFECYCLE_TRN_TYPES; imported sales and commissioning confirmation are different |
| MREAD rejects prepaid/token reading in the inspected server | Phone branches alone are not a valid production manual; successful conventional readings require known and capture GPS within the inspected five-metre check |
| Phone password reset differs by branch | Primary Sign In routes to /pwdReset, but that screen is present in mobile-auth and absent from the primary tree |
| Phone verification has mismatched hook names | Screen asks for verifyPhone/resendPhoneCode; primary API exposes sendPhoneOtp/confirmPhoneOtp |
| Workbase selection conflicts with the password rule | Primary select-workbase clears mustChangePassword without performing a password change |
| Common form colours exist in dedicated feature worktrees | UI-R004's central formColors files were found in mobile-forms/web-forms, not the primary trees |
| Offline outcomes differ | Premise uses a 10-second timeout; inspection separates SAVE/SUBMIT and retains successful queued records; other screens remove successful queued items |
| Timed-out inspection wording overstates certainty | “NOT sent” does not establish non-arrival at the server |
| Disconnection accepts water but level labels describe breaker work | Water-specific instruction and evidence teaching requires product review |
| Primary web user-status saving remains disabled | A selector's presence is not implementation of the save action |
| Report email backend exists alongside older contradictory auth wording | Verify configured delivery; do not repeat “iREPS cannot send email” as a universal current fact |

## Discovery/Premise handover reconciliation

The existing Academy main commit `753f90f419322093e1b2c5756eebc546f1dda090` contains the 24 September Sales Path/Normal Path handover. This pass preserves it and links a [current training update](../01-body-of-knowledge/meter-discovery-path-update-2026-09-25.md). The rule MC-R001 subsequently reports Tests 0–7 passed on 25 September and defers 8–15; that is reported source evidence, not a test run by this Academy investigation. Ambiguous multi-meter Test 15 remains unresolved.

## Remaining depth and publication work

The new field catalogues include business definitions and extracted individual controls. Some dynamic controls, inferred storage mappings, defaults, shared component fields and server validations remain unverified. These gaps are explicit in the catalogues; they must be completed by pairing the accepted app/backend and tracing actual payloads. The error CSVs preserve triggers, but many stage-specific data-state/remedy interpretations require individual runtime review. This pass does not claim parity with all 75 manually authored Meter Discovery field records for every new module.

Use the module packages as the basis for the next discussions. Confirm product decisions; then add release-specific screenshots, full branch coverage, actual permission matrices, end-to-end recovery evidence and reviewed video demonstrations. QA, common offline handling, Trials, full billing and automated integration remain at their previously agreed statuses.

## Preservation and integration boundary

Work was prepared on `docs/forms-and-meter-lifecycle-20260925` in an isolated Academy worktree. Six pre-existing primary-worktree changes in video scripts and field-guide files remain owned by their current workstream. No application source was changed. No deployment, live data operation or outbound user communication is part of this documentation work. The final commit, remote push and recovery check are recorded in the completion record.
