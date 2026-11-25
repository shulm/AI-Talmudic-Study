# Common execution contract for the multi-platform launch

This supplement defines dispatch scope for the user's request to run many agents across several platforms and complete the full inventoried Bavli. It preserves the source/semantic/review requirements of `research/bavli_dataset_program_v2/` at commit `5876cb9dfd40dbadecb4a79273e59631fe1f127a`.

**Current status: launch instructions and static assignments only. No runtime contract, active platform assignment, new annotation, or completed tractate is created by these files.**

## 1. Scope and authority

The run covers exactly the 37 base Bavli tractates in the pinned inventory, totaling 81,793 source segments. This is the complete selected Bavli Gemara inventory, not a claim to cover every tractate of Mishnah, Yerushalmi, commentary, manuscript witness, or later literature. Such enrichment has separate scope and provenance.

Only the **GLOBAL_COORDINATOR** owns the complete 37-tractate assignment map. L01–L06 leads own only their declared tractates. They must not execute the old master prompt's unrestricted "claim the next tractate" instruction outside their lanes. A worker owns one complete tractate. A fresh blind reader owns only source-first review. The integrator owns global reconciliation and release assembly.

Use available authorized platform agents without per-window or per-tractate user approval. The inherited USD 0 allowance concerns new metered external API calls, not already available agent capacity. No particular vendor or API is required. An interactive agent can generate saved structured proposals that the common tools ingest; record actual execution. Do not fabricate model/provider IDs, token counts, or runtime availability. No model training is required. Preserve draft-PR and no-auto-merge boundaries.

## 2. Shared contract, then parallel production

The coordinator prepares a real production implementation once: pinned source verification, full-tractate scope, explicit schema migration, isolated outputs, immutable proposals, safe checkpoints, deterministic replay, validators, and per-layer coverage. The design label `2.0.0-design` is not proof that this implementation exists.

The coordinator's authoritative coordination branch is proposed as `dataset/bavli-coordination-v1`. If that branch already exists, inspect its owner/run rather than replace it. Preserve any valid active continuation and record a different branch only through an explicit run handoff.

Publish `research/bavli_dataset_runs/ACTIVE_RUN.json` on the coordination branch. It identifies `run_id`, the immutable run-contract path/hash and commit, assignment revision/epoch, and the actual production code commit. Each run has `research/bavli_dataset_runs/<run_id>/RUN_CONTRACT.json`. These are future runtime outputs; the supplied template is not an active run.

The contract identifies exact source manifest and files, output schemas and hashes, annotation protocol/hash, production/tooling commit, tested command interfaces, actual supported execution routes, assignment map, branch/output conventions, and source-access descriptors. Never commit credentials or bearer/signed access URLs. Every producer verifies the same contract before canonical promotion.

Bootstrap readiness requires actual successful semantic execution on an inherited continuation and a fresh source block, plus source/replay/restart checks. It does not require a completed entire tractate or every optional enrichment adapter. Reuse the real shakedown outputs with lineage in the relevant tractate job; do not discard them as another endless pilot.

## 3. Exact source access on every platform

The public repository is not the full pinned source export. `F:/Sefaria-Export-master` is a historical local path. Each execution environment needs the actual named-edition source files for its assigned jobs and a working verification command.

The coordinator prepares source packages/access descriptors using already available authorized storage or transferable owner artifacts. Keep complete original texts outside repository Git history. Each file must match the job's expected SHA-256. A live download can be used only if it matches the pinned bytes; otherwise it is a different snapshot requiring explicit admission. Do not substitute `merged.json`, another edition, or model memory.

If source transfer cannot be completed with available access, identify the concrete missing files/location and preserve useful setup work. Work on other verified jobs may continue. Do not claim a source is present because a manifest or an online reading page exists. Independent readers need their own original-source access.

## 4. Exclusive ownership with simple coordination

`ASSIGNMENTS.json` is an immutable planned allocation. It is not a live execution ledger. The coordinator admits/resumes actual owners in the run ledger and issues assignment epochs. Existing valid jobs retain their current owner until a recorded handoff; the planned map must not overwrite live assignments.

Routine worker dispatch inside an admitted lane is delegated to that lane lead; it does not require a coordinator round trip for each tractate or batch. The global assignment revision is audit metadata. Promotion epochs are scoped to individual tractates: the lane lead records within-lane worker transitions under its delegated authority, and only the coordinator transfers ownership across lanes. An unrelated lane update does not invalidate current workers.

One platform lead may own several lanes, or several lane leads may run on one platform. One current producer owns each tractate. More helpers work under that producer or lead, not as uncoordinated second owners. Reassignment must preserve the last checkpoint and advance the assignment epoch; stale owners cannot promote output.

Each tractate has an isolated branch/output directory and one checkpoint promoter. Internal helpers write separate immutable proposal directories. Review outputs are separate. Lane leads write lane status/receipts, never append concurrently to global corpus files. The coordinator is the sole writer of global assignments and integration indexes. Use actual branch/version checks; a comment or uncontrolled shared JSON edit is not a lock. Static allocation avoids a distributed scheduler requirement.

If a platform cannot push to GitHub, preserve a hash-verified artifact package with the same paths and a delivery receipt for the coordinator. Do not mark it pushed. A receipt identifies run/contract/assignment epoch, tractate, artifact hashes, producing version, review version, coverage, and next work.

## 5. Required richness and complete passes

For every assigned source scope, complete structure/continuation; utterance and claim extraction; attribution/transmission; questions and conditions; scoped positions and local status; supported directed argument edges; and a source-based omission/reconciliation pass. Preserve exact evidence and distinguish original text, paraphrase, inference, and external commentary.

Keep anonymous discussion, narratives, unresolved questions, composite units, and missing positions. Do not invent binary choices, historical decisions, speakers, or personal motives. A transmitter is not automatically a position holder. Read full relevant continuations for reversals, alternative versions, distinctions, and retractions.

Track extraction state/result, review state, release integrity, and task eligibility separately under the common schema. Source ownership alone does not establish semantic extraction. Supported unresolved alternatives remain useful records with restricted task eligibility; unsupported resolutions and invalid evidence are quarantined. Ordinary uncertainty does not stop unrelated tractates.

Optional topics, terminology, commentary links, global authority-catalogue enrichment, and additional research adapters proceed separately. They do not block a core tractate release. Preserve the legacy `ml_eligible=false` and use separately versioned eligibility policies for new views.

## 6. Independent review without inherited labels

Use fresh source-only reviewer contexts. A child agent inheriting the producer's conversation is not blind to that conversation's annotations. Different platform/model names do not establish independence. A comparison agent may see both readings only after the source-first reading is frozen.

Use the v2 source-coordinate sampler: fixed blocks of ten raw nonempty source segments, sample `min(B, max(30, ceil(B/10)))`, freeze seed/source/grid before comparison, and track endpoints separately. Original-source context can expand to complete discussions without inflating sampled-core counts. Report random, endpoint, risk, and task-qualification cohorts separately.

Review detected high-risk cases and all rows proposed for demanding evaluation/choice views under their policies. Inspect omissions using independently found claims in sampled source cores, not only existing worker rows. Preserve initial readings, errors, disagreements, and corrections. AI review is not human scholarly certification.

## 7. Checkpoints and truthfulness

After internal batches, save immutable proposals, exact evidence/contract hashes, coverage by layer, open tails, accepted artifacts, revision lineage, and next-unprocessed work. Replay reconstructs from saved proposals; fresh model calls are new attempts. Never overwrite initial judgments to obtain apparent agreement.

Start the next assigned tractate automatically when a production slot becomes available and the previous handoff is durable. Reviewer corrections can proceed against exact versions. At session limits, save a resume packet; do not claim background continuation after the platform stops.

Minimum tractate delivery: authoritative core tables, per-sugya export, coverage matrix, qualification ledger, frozen review/comparison artifacts, unresolved cases, validation, manifests, and replay/resume instructions. Public source views obey source distribution rules; retain full original bytes in the appropriate source package. A reader/search view may be generated where permitted without becoming a second editable corpus.

## 8. Final completion condition

Full provisional core completion requires all 37 jobs, exact source accounting against the 81,793-segment baseline, complete declared required extraction passes, passing integrity gates, and declared independent-review requirements for each tractate. Source bookkeeping, full extraction, sampled AI review, and task eligibility remain separately reported.

Valid unresolved interpretations can remain explicitly recorded. Missing source/passes, unfinished review, and quarantined invalid scope must be reported and cannot be hidden by a whole-corpus completion badge. No requirement of 100% human certification or complete optional enrichment is introduced. The integrator releases useful partial snapshots while closing genuine gaps.
