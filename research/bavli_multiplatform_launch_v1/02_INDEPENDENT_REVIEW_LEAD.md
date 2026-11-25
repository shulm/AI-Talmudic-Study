# Assignment 02 — Independent review lead

You own independent review of the full Bavli dataset produced by lanes **L01–L06** in `shulm/AI-Talmudic-Study`. The pinned baseline contains **37 tractates and 81,793 source segments**. Your objective is review evidence and tractate verdicts throughout production. You do not own production annotations, global assignments, or the shared implementation.

Read repository instructions, `research/bavli_multiplatform_launch_v1/COMMON_EXECUTION_CONTRACT.md`, and the review/schema documents in `research/bavli_dataset_program_v2/`. The reference v2 package commit is `5876cb9dfd40dbadecb4a79273e59631fe1f127a`; it contains preparation tools and a design, not an already functioning full production service.

## Establish the active execution contract

Retrieve the coordinator's canonical `research/bavli_dataset_runs/ACTIVE_RUN.json` through the declared coordination ref. Follow its exact run-specific `RUN_CONTRACT.json` location and verify the contract hash recorded in the pointer. Pin the actual source, schema, protocol, tooling, ownership epoch, and output conventions. These runtime artifacts are to be created by the coordinator; do not assume they already exist or create competing replacements.

If the pointer, contract, or source is unavailable, report the precise missing artifact to the coordinator and prepare only work that does not depend on it. Never infer readiness from a design version string. Confirm access to the exact source bytes needed by each reader; a historical local filesystem path does not provide access on another platform.

## Start independent reading alongside production

Assign fresh source-only readers as tractates become available. Use the platform's supported agent dispatcher and existing authorized account access; no particular model vendor or new paid API is required. Respect the inherited allowance for new external paid calls. Record actual launches and identifiers where available, and never invent usage telemetry.

A blind reader receives the pinned source, neutral coordinates, common instructions, and schema. It must not inherit producer labels, summaries, proposed identities, conclusions, or annotated context. A full-history fork of an exposed agent is not blind. If source-only isolation is unavailable, mark the reading nonblind or use a genuinely fresh context.

You may inspect production labels for comparison only after the corresponding independent readings are frozen. Delegate those readings before exposing yourself where necessary; your own later comparison does not invalidate an already frozen independent reading. Keep method inspection and source-first judgment clearly identified.

## Freeze a reproducible source sample

Use the v2 source-only planner under the active contract. Its default grid is ten consecutive nonempty original source segments per block, with original indices preserved. For B blocks, sample `min(B, max(30, ceil(B/10)))`. Freeze the source hash, seed, grid, selected coordinates, inclusion probabilities, and plan hash before comparing labels. Do not reroll difficult samples.

Opening/closing checks and risk-targeted checks are separate cohorts. Track overlap without double-counting unique coverage. Readers expand original context enough to understand the full relevant discussion; expanded context does not inflate sampled-core coverage. A generated plan is not a completed reading. This assignment does not claim that a plan or review has already been frozen.

Each reader records boundaries, claims, questions, conditions, attribution/transmission, supported argument relations, local statuses, and uncertainty with exact source evidence. Freeze its initial output and hash before comparison.

## Compare, qualify, and correct

Measure omissions against material independently identified in source cores, not only against existing producer rows. Record both initial readings, exact record versions, supporting spans, discrepancy category, severity, proposed correction, and resolution. Preserve disagreement history.

Review all detected high-risk cases and every candidate example whose demanding task policy requires record-level verification. Random source review remains necessary for silent omissions. Report attributable-claim, condition-bearing-claim, proposed-answer-set, argument-edge, and independently found-claim denominators separately. Distinguish confirmed errors, reasonable granularity differences, unresolved ambiguity, and corrections.

Supported uncertainty may remain valid with restricted eligibility. Quarantine unsupported resolutions or corrupted evidence. A local issue restricts its dependent records; a shared edition, transform, or extraction-rule failure pauses all affected dependencies. Notify the coordinator promptly without stopping unrelated valid work.

## Deliver review evidence continuously

Write only your assigned review artifacts under the run contract's review paths. Keep production records separate. Provide compact exceptions near one-third, two-thirds, and completed tractate coverage; routine batches need no user approval.

For each exact production version, deliver the frozen plan, independent readings, discrepancy/adjudication ledger, validation observations, coverage by review cohort, task-qualification decisions, and one v2 verdict: `ACCEPT_PROVISIONAL_TRACTATE`, `ACCEPT_PARTIAL_WITH_EXCEPTIONS`, `REWORK_TARGETED`, or `BLOCK_CRITICAL`. Bind every verdict to exact source, contract, artifact, and review hashes. Changed evidence requires affected-scope rechecking.

Continue across all 37 assigned tractate reviews as execution capacity allows. Preserve checkpoints and precise resume instructions when interrupted. AI agreement is not human scholarly certification. Open draft review PRs where authorized; do not merge or promise unattended work after the session ends.
