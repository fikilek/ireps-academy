# Meter reading and billing handoff

Status: owner-confirmed module purpose; functionality needs strengthening before production. Detailed operating instructions and export acceptance remain to be verified.

iREPS supports fieldworkers manually reading conventional electricity and water meters using mobile devices rather than paper. The worker locates the meter, including its GPS position, accesses it, captures the reading and evidence, and submits the reading to iREPS. The software digitises the work; it does not imply automated remote meter reading.

Readings must follow a consistent cycle. iREPS prepares the readings, and an authorised role initiates the final file for the external billing system. The role, file format, validation, exception handling and dispatch/receipt controls need confirmation for each utility and deployment.

Future backend integration should exchange readings without people carrying files between systems. That automated integration and a full iREPS customer-billing module are future work. Do not label reading staging or file preparation as full customer billing.

The complete lesson must cover the prior/current reading interval, electricity and water differences, No Access/No Reading, quality checks, duplicates/corrections, staging, export and billing-system acknowledgement. QA correction policy remains open.

See [DEC-011 and DEC-012](../../00-academy-governance/OWNER_DECISIONS.md).
