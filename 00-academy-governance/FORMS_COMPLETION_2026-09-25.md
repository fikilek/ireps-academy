# Forms and meter lifecycle — preparation and verification record

Prepared 25 September 2026 on `docs/forms-and-meter-lifecycle-20260925`, based on Academy main `753f90f419322093e1b2c5756eebc546f1dda090`.

## Delivered content

- [41-family form library](../01-body-of-knowledge/forms-library.md): existing Meter Discovery plus 40 new/expanded five-component packages.
- [Meter Lifecycle — Body of Knowledge](../01-body-of-knowledge/meter-lifecycle-body-of-knowledge.md): acquisition and document flow, stores/custody, registration, operation, replacement, return and disposal; four diagrams, worked examples and open design questions.
- [iREPS Form Standards](../01-body-of-knowledge/ireps-form-standards.md): common terminology, existing UI/auth rules, proposed input contracts, validation/submission states and remaining design work.
- [Current Discovery path update](../01-body-of-knowledge/meter-discovery-path-update-2026-09-25.md): Normal Path, Sales Path, Premise Picker and source-reported capture-test status.
- [Source investigation](FORMS_INVESTIGATION_2026-09-25.md), repository/candidate inventories, source baseline, and updated navigation, content/source registers and dictionary.

## Checks completed before commit

All 41 families have a Body of Knowledge, User Manual, Field Catalogue, Error Register and Practical Examples. Six future packages are explicitly planned: procurement, check-in, check-out, return, retirement/disposal and vending.

The source review records 183 selected file fingerprints and 645 candidate surfaces including branch duplicates, shared controls, filters and historical copies. New extracted references cover 324 UI controls and 1,090 source error/message entries. These counts are evidence inventories, not a count of unique business fields, failures or passed tests.

Internal Markdown destinations/anchors, CSV source IDs/line bounds, complete content registration and dictionary uniqueness were checked. All five new diagrams rendered in the browser. The eight existing placement plates retained their SHA-256 checksums. Original Meter Discovery catalogues retain 75 field records and 110 error entries. The master dictionary preserves prior entries and adds eight explicitly qualified terms, bringing the total to 422.

## Remaining limits

Some field defaults, dynamic bindings, storage transformations, shared-component expansion, exact error stage/remedy semantics and role-specific routes remain review gaps. No runtime or Firebase test was performed. Code availability is not deployment/acceptance. No claim is made that every new package has completed the same manual field-by-field analysis as Meter Discovery.

Common offline acknowledgement/retry/retention, QA corrections/payment effects, lifecycle state modelling, procurement/stores/disposal rules, reuse, automatic billing integration and Trials retain their open/planned status. Specific source inconsistencies are recorded in the investigation and module packages.

## Integration safeguards

Only Academy Markdown/CSV changes from this task are intended for the documentation commit. The existing handover commit is preserved. Six unrelated primary-worktree video-script/field-guide edits must remain byte-for-byte unchanged across integration.

The authorised integration is a fast-forward merge and ordinary push to the existing Academy repository, followed by an independent recovery checkout and file-hash comparison. This record documents preparation checks; the actual resulting commit and remote/recovery verification are reported only after those operations succeed. No application deployment or live-data change is included.
