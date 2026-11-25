# Assignment 09 — Rolling corpus integration and final release

You are the corpus integrator for `shulm/AI-Talmudic-Study`. Assemble compatible, traceable outputs from production lanes **L01–L06** and their independent reviewers. The pinned full-Bavli scope is **37 tractates and 81,793 source segments**. Begin rolling integration as finished artifacts arrive; do not wait for all lanes to finish before discovering compatibility defects.

Read repository instructions and `research/bavli_multiplatform_launch_v1/COMMON_EXECUTION_CONTRACT.md`. Consult `research/bavli_dataset_program_v2/` for schema evolution, qualification, and release rules; its reference package commit is `5876cb9dfd40dbadecb4a79273e59631fe1f127a`. That package describes the target and supplies preparation tools; actual production readiness comes from the coordinator's execution contract.

## Resolve the authoritative run

Retrieve `research/bavli_dataset_runs/ACTIVE_RUN.json` from the coordinator's declared coordination ref. Resolve the exact run-specific `RUN_CONTRACT.json` and verify the hash recorded in the pointer. Those are future coordinator outputs, not files that this prompt claims already exist. Do not create another active-run pointer or select a different run by filename, timestamp, or apparent progress.

Pin the actual source manifest, code commit, schema, protocol, lane assignments, and ownership epoch. Use the coordinator's ledger to identify handed-off tractate versions and review results. A queued job or successful process exit is not a delivered dataset.

## Integrate immutable tractate artifacts

Accept only exact artifact manifests with verified hashes and documented source/contract compatibility. Read each tractate's coverage matrix, unresolved ledger, validation report, and exact-version review verdict. Check whether later corrections invalidate earlier qualifications. Reject stale-owner promotions and preserve superseded versions and lineage.

Keep the original named edition unchanged. Do not mix PR #11 source strings, offsets, or semantic IDs into the PR #10-based corpus. Any admitted source change requires an explicit version and alignment policy. Preserve historical pilot evidence, including Berakhot's open-tail lineage and Bava Metzia's interior-pilot distinction.

Build aggregate tables and views deterministically from the authoritative per-tractate artifacts. Do not manually edit generated aggregates or rewrite a producer's judgments during integration. Return targeted correction requests to their owner, naming exact source refs, record versions, evidence, and validation needed.

## Reconcile shared identities and relationships

Maintain the global entity registry and typed cross-tractate links using evidence-bearing proposals. Keep surface mentions, identity candidates, holder/reporting roles, and unresolved alternatives. Similar names alone do not establish identity.

Preserve every textual occurrence. Distinguish confirmed same-report repetitions, direct parallels, quotations, cross-edition counterparts, candidate similarities, and merely related topics. Do not turn every thematic link into a single equivalence family or treat repeated reports as independent decisions. Investigate unexpectedly large components and retain explicit uncertain links.

## Verify coverage and qualification

Reconcile all 37 job IDs against the pinned inventory exactly once. Verify the full 81,793-segment denominator, original indices, context exclusions, primary ownership, and explicit empty-position accounting. If a new source baseline is proposed, require coordinator versioning rather than silently changing the denominator.

For every tractate, verify completed required source, structural, utterance/claim, attribution, question/position, and argument passes with their execution evidence. Structural partition alone is insufficient. Review must meet the declared protocol with probability, endpoint, and risk cohorts reported separately.

Supported unresolved interpretations may remain in the valid provisional corpus with restricted task eligibility. Quarantine defective records and exclude their dependent examples. Systematic failures require correction of the affected layer or contract. Optional enrichment and unimplemented future benchmark adapters do not block a complete core release.

## Build reusable exports responsibly

Provide normalized core tables, per-sugya views, coverage/review matrices, task-eligibility records, unresolved cases, version manifests, and reproducibility instructions. Generate a read-only Hebrew reader where source distribution permits. Preserve source attribution and artifact-specific license metadata; follow the repository prohibition on committing full source-corpus copies.

Before a supervised task export, freeze its question, eligible population, label policy, input recipe, source cutoff, and family grouping. Group relevant repeats, overlapping evidence, and generated derivatives before splitting. Check titles, summaries, aliases, rationales, continuations, and retrieval results for outcome leakage. Record unknown model pretraining exposure separately; within-corpus splits do not resolve it.

## Deliver a truthful final release

Publish rolling provisional snapshots in your isolated integration branch and open draft PRs. Building an integration candidate does not authorize merging other PRs. Use available authorized agents for bounded reconciliation and validation, without requiring a new vendor API or inventing execution measurements.

Declare full provisional core completion only when all 37 tractates satisfy the declared required-pass and review gates, with integrity defects resolved or excluded under an explicitly qualified release scope. Report the actual included scope and all exclusions; do not describe a release with missing required source coverage as complete.

The final report gives exact source/contract/artifact hashes, tractate verdicts, per-layer coverage, independent-review coverage, unresolved and quarantined scopes, task-eligible counts, distribution/reconstruction instructions, and remaining optional work. If any required job remains unfinished, release the valid partial result with precise remaining jobs and resume instructions. Do not claim human certification or promise background continuation after the session ends.
