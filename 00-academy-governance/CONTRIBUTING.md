# Contributing to Academy

## Handover from a development workstream

Supply the affected task, user-facing change, source repository/branch/commit, intended environment/release, role and organisation conditions, screenshots or synthetic examples when available, field validations, error messages, offline behaviour and remaining placeholders. State separately what was implemented, deployed and accepted.

Propose dictionary and learning changes in Academy. This Academy workstream reconciles them with owner decisions, reviews the material and records the decision. Do not create a second active glossary or manual in an application repository. Keep a link to Academy instead. Do not remove another contributor's unmerged branch files or change their current checkout.

## Required information for a task guide

- Stable topic ID, title, purpose and audience.
- Platform, organisation/role conditions and prerequisites.
- Applicable application revision and verified environment/release.
- Steps, fields, decision points and expected result.
- Evidence requirements, exceptions, Error Register and escalation.
- Save, submit, retry and acknowledgement behaviour for that specific workflow.
- Related dictionary terms, demonstrations and assessment.
- Source evidence, review date and content status.

## Two independent status tracks

Application: planned; in development; awaiting deployment; deployed to a named environment; accepted for production; unknown/unverified. A code inspection alone proves neither deployment nor acceptance.

Content: source material; draft; under review; approved; published; superseded. Approval of repository organisation is not approval of every imported instruction. Published content needs a verified release and review record. Historical originals remain source material and are excluded from learner navigation.

## Integration and checks

Use a dedicated documentation branch from main, preserve unrelated work, and review the exact diff before merging. For this approved consolidation, documentation-only changes may be integrated and backed up; no Firebase promotion is involved. Verify links, imported source checksums, role terminology and open-decision notices. When an application consumes Academy-owned help text, record the consumed revision and coordinate the runtime update with its developer.

Feature worktrees can still contain historical copies until their owners integrate the documentation commit. Do not switch or rewrite those worktrees to make a folder search look clean.
