# Meter Discovery — Path and Premise Update

Review draft, 25 September 2026. This update qualifies the 23 September detailed Meter Discovery baseline. It reconciles the committed [24 September handover](../00-academy-governance/HANDOVER-2026-09-24-sales-path-and-normal-path.md) with the newer source-rule report; it is not a production acceptance certificate.

## Sales Path and the Premise Picker

From My Work Orders, a row with **Premise 0** opens the **Premise Picker**, showing premises on that ERF with their unit/business details and existing joins. An empty ERF can proceed straight to New premise. New premise and Copy a premise are distinct creation choices. A premise joined to another row in the same batch is unavailable for reuse by that row.

**Premise 1** opens the associated premise; the AST action opens Meter Discovery with the expected meter number. Check the actual equipment before accepting that prefilled value. A shared ERF does not make every premise interchangeable. Commercial and Industrial premise names use the Business Name label in the current work.

Cross-batch association is a known edge: a premise may appear Not joined in the picker but still be refused by the server because of another batch. Do not work around the refusal by creating duplicate premises. A backend association-correction capability does not establish a phone correction interface.

## Normal Path and an available Sales row

The worker begins from the actual premise. If no applicable row is found, Meter Discovery opens through the Normal Path. If an applicable row is found, the path dialog offers **Sales Path**, **Normal Path** and Cancel. Choosing Sales Path carries row context and the expected number; choosing Normal Path does not carry that row context or prefill that expected number.

If a known row cannot be worked, the dialog explains why and offers Normal Path or Cancel. If the check fails because availability could not be established, the handover retains both path choices and tells the worker to check connectivity. These UI choices do not bypass server assignment/ERF/meter checks.

The source handover describes a ten-second path-check wait and a repeated-click message, “Still checking the previous premise”. Do not confuse this navigation check with the proposed universal fifteen-second submission policy.

## Which row is completed?

The captured meter and served premise must determine the appropriate row outcome. Expected Sales meter and actual discovered meter are separate facts. Normal Path work can still be correlated by the server, but it must not silently complete unrelated premises on a multi-meter ERF.

MC-R001 describes sixteen combinations of one/many expected meters, premise origin, meter origin and same/different expected meter. Its 25 September revision reports Tests 0–7 passed and defers 8–15. Earlier handover reports and newer source-rule reports are date-specific. This Academy pass did not reproduce those tests. Test 15—an ambiguous unlinked premise and unlisted meter on a multi-meter ERF—still needs an agreed rule.

## Review exercises

1. One ERF, four flats: join only the row's actual premise and verify its meter identity.
2. A premise already joined to another same-batch row: explain why it is unavailable and do not duplicate it.
3. Normal Path sees a valid Sales row: explain the carried context and prefilled-number difference for each offered path.
4. Row-check timeout: distinguish unknown availability from a confirmed allocation refusal; preserve server checks.
5. A different meter is found: keep expected and discovered serials distinct and verify the single appropriate row outcome.
6. Multi-meter ambiguity: record the unresolved case rather than declaring whole-ERF closure correct.

Use [Premise Registration](premise-registration-body-of-knowledge.md), [My Work Orders](work-order-acceptance-body-of-knowledge.md) and the [original Meter Discovery catalogue](meter-discover-field-catalogue.md) together. The original field/error source fingerprints remain historical evidence; they were not silently rewritten to pretend the newer branch was their original baseline.
