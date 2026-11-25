# Lead-agent assignment: build the reusable Bavli research dataset

You own **actual dataset production and delivery** for `shulm/AI-Talmudic-Study`. Use available authorized agents actively. The user wants deep, rich, reusable data and faster progress, with one accountable whole-masechta job per producer and independent review. Coordinate the work yourself; do not require the user to manage small windows or continually assign the next tractate.

Read this package, the repository's `AGENTS.md` and `AGENT_HANDOFF.md`, and the current source/annotation manifests before modifying anything. Preserve the user's instructions and frozen prior studies. Work in isolated branches/worktrees. This mission concerns dataset construction; model training is a separate research assignment.

## 1. Establish the real baseline and start production

The inspected historical production base is PR #10, commit `ef29310b50575ac2441ce59d0c68d58424f4b823`, using **Wikisource Talmud Bavli**. Recheck current refs and active worker ownership so you do not duplicate a production job already in progress. Reuse a later accepted continuation if its source, schema migration, pilot lineage, and review evidence are valid; otherwise preserve the pinned baseline.

PR #11 at `9a9dfad93675b984b8223ba065732599a973f074` uses a different edition. It is a separate method reference. Do not transplant its annotations or assume its offsets match.

Resolve the source root on the execution machine. The historical path is `F:/Sefaria-Export-master`, not a universal path. Verify all needed source hashes before annotation. If the exact snapshot is absent, obtain an authorized copy or report the exact missing artifact; never silently substitute a live edition. Other jobs with available validated inputs may proceed. Preserve original source bytes read-only.

Give shared driver/schema/replay work to **one tooling owner**. Its brief is `ENGINEERING_NEXT.md`. The current supplied tools build a job queue and source-only review plans; they are not an annotation executor. Implement the smallest working production path over available agent execution. Demonstrate real semantic work, not only a model-access check, by extending a pilot continuation and processing one fresh source block. Preserve outputs and invocation provenance. Verify safe staging, deterministic replay, restart, and long open-sugya handling.

This shakedown is a dependency check, not a new open-ended pilot project. Once the production path works, proceed directly to whole-tractate production in this assignment. Do not finish with another plan-only report.

## 2. Dispatch whole-masechta jobs concurrently

Use the static `jobs.json`. The delivered builder reproduces the exact historical baseline only; track accepted continuations in the separate runtime ledger. A changed source baseline requires an explicit queue/tool version update, not resetting current work by rerunning the baseline builder. It currently represents all 37 tractates and 81,793 source segments. **Queued is not running.** Actual launch, worker identity, branch, checkpoint, and evidence belong in the runtime ledger, not invented into the static queue.

Start available production/review pairs in this order: **Berakhot, Bava Metzia, Rosh Hashanah, Taanit**. This is a practical first wave that reuses both pilots and tests fresh tractates. Then drain the remaining inventory in pinned TOC order, adjusting assignment order only with a recorded operational reason. No need to wait until every Berakhot uncertainty is resolved before other tractates proceed.

Use one owner per tractate. Give it `TRACTATE_WORKER_PROMPT.md` and the exact job record. Give its independent reviewer `INDEPENDENT_REVIEW_PROMPT.md` and source-only access. Each producer stops writing a completed tractate after its exact-version handoff; the coordinator may assign it the next queued job without a new user prompt. Review and targeted corrections continue on the delivered version.

For twelve actual simultaneous slots, a starting allocation is one lead/integrator, one tooling owner, four tractate producers, four independent reviewers, one adjudicator, and one enrichment/link worker. Adapt to actual available slots. With fewer slots, time-share compatible roles while keeping blind reading contexts independent. With more slots, add producer/reviewer pairs and independent second extraction of important layers. Log launches only after the platform confirms them.

Keep sufficient review capacity. If review backlog grows faster than it is cleared, assign the next free agents to review before adding producers. Do not promise a completion date from agent count alone; measure a full completed tractate's annotation and review throughput first.

## 3. Freeze a common contract and isolate writers

Pin the source manifest, schema, annotation protocol, tooling version, and accepted pilot lineage in each job. Tractate producers do not independently redesign shared schemas or append to global JSONL tables. Propose changes to the tooling owner; a changed contract receives a new version and an explicit impact/migration record.

Use separate production and review worktrees. Internal helpers write immutable proposals to unique job directories. The tractate lead is the sole promoter of its authoritative checkpoint. The corpus integrator alone updates global entity, family, and release manifests. A small single-dispatcher ledger is sufficient initially; do not build a distributed service without an operational need.

The runtime ledger must record job ID, worker/reviewer identities, source/schema/protocol hashes, branch, lease epoch, expiry/heartbeat when supported, state, current checkpoint, and blockers. Claim updates must be atomic in the dispatcher's authoritative state. If an expired job is reassigned, increment the epoch and reject stale promotions. Do not call a GitHub comment or a concurrently edited JSON file an atomic lock.

Use the sequence **immutable proposal → staged validation → explicit revision/adjudication → checkpoint promotion**. A checkpoint identifies immutable files and hashes; old checkpoints remain recoverable. Retries for technical failures are bounded and logged. A fresh model response is a new proposal, never a replacement that erases disagreement.

## 4. Produce rich core data before optional enrichment

Follow `SCHEMA_AND_RESEARCH_VIEWS.md`. Required core layers cover exact sources; primary/nested structure and continuation; discourse units and atomic claims; mentions and attribution/transmission; questions and scoped positions; evidence-bearing argument edges; per-layer extraction coverage; and review/provenance/lineage.

Retain anonymous, narrative, nondecision, unresolved, and apparently negative material. An absent scholar response is missing data. Do not force every question into binary alternatives or every passage into a decision. Record source-attested positions separately from editorial explanations and from later practical rulings.

Each producer performs a complete pass for every required layer across its entire source scope. A layer may legitimately return no findings, but that outcome requires a completed pass and evidence of the scope read. A generic summary and a coverage partition are not substitutes for extracting claims, conditions, and relations.

Keep optional enrichment in separately versioned layers: topics, technical terms, external authority-catalogue enrichment, commentary/quotation links, cross-tractate parallels, and later linguistic features. Source mentions, attribution roles, identity candidates, and task-relevant disambiguation remain core responsibilities. Begin useful enrichment as stable core units arrive; it must not block source and core semantic completion. Commentary-supported interpretations must retain their external evidence and must not appear as explicit words of the base Gemara.

## 5. Review independently and continuously

The method auditor may inspect code and existing annotations. A blind reader must receive only source, neutral coordinates, common instructions, and the schema. If exposed to worker labels, titles, summaries, or suggested answers, mark that reading nonblind or use a fresh reader.

Freeze a source-only sampling grid and sample before comparing labels. `tools/make_review_plan.py` provides the default: blocks of ten consecutive nonempty source segments; sample `min(B, max(30, ceil(B/10)))` blocks, where B is the grid size. The sample seed and source hash are frozen. Mandatory opening/closing checks and risk-targeted review are reported separately. Readers expand original-source context as needed to understand complete discussions; context does not inflate sampled-core counts.

With available resources, independently read all high-risk attribution cases and every record proposed for demanding decision/QA evaluation views. Random source reading must still test omissions in ordinary material. Preserve both initial readings, evidence, discrepancy classifications, corrections, and unresolved alternatives. Agreement by two agents is AI review, not human certification.

Report compact milestone exceptions at approximately one-third, two-thirds, and complete source coverage. Normal processing does not wait for a user or supervisor prompt at each window. Bind final review to exact artifact/commit hashes. Changed evidence requires review of the affected portion before the verdict is reused.

## 6. Scope blockers and release usable data

A supported unresolved attribution remains valid corpus material with disputed/unresolved status and restricted task eligibility. Quarantine unsupported forced resolutions, corrupted evidence, and the downstream examples depending on them. A repeated shared attribution bug pauses the affected pass/dependencies. A corrupted source snapshot or destructive-write defect stops all dependent promotions. Unrelated valid jobs continue. Every blocker names its scope, evidence, correction, and proof of recovery.

Use `QA_AND_RELEASE.md`. Mechanical integrity is checked on all released artifacts. Semantic coverage and independent review coverage are separate. Preserve the legacy `ml_eligible=false`; add task-specific eligibility records with versioned policies. Source retrieval, segmentation, attribution, argument extraction, QA, and scholar-position modeling have different requirements.

A reviewer issues a tractate verdict with layer-by-layer coverage and exclusions. Assemble provisional releases as tractates finish. Do not wait for the entire corpus or optional enrichment to publish a useful reviewed snapshot. Do not advertise a whole-corpus semantic accuracy percentage from an AI sample.

Create task-specific leakage controls before supervised exports: group confirmed repeats/parallels and all derivatives, preserve occurrence-level records, and remove outcome-bearing text/metadata from prediction inputs. A source's order in the Talmud is not evidence of the historical order of an individual's decisions. Modeling conclusions remain outside the core annotations.

## 7. Resource and publication authority

Use the available authorized agent resources without repeatedly asking for ordinary internal work. The user's abundant-agent instruction does not define a new metered vendor API budget; keep new paid external calls at the inherited USD 0 allowance unless a later explicit amount is provided. Existing included agent usage may proceed. Log actual service/model IDs and observed usage; use null plus a reason when telemetry is unavailable. Do not describe a provider as used without execution evidence.

The repository is already public. Preserve its visibility and keep credentials, full source-corpus copies, and unrelated personal material out of commits. Respect each edition's actual recorded terms. Separate source, links, commentary, generated annotations, and code rights; public visibility is not a license grant. Build portable source acquisition instructions and manifests so full texts need not be copied into Git history.

Push your isolated branches and open draft PRs for concrete completed artifacts. Do not merge existing or new drafts without an owner instruction. Do not modify frozen behavioral studies or claim their results validate this dataset.

## 8. Required deliverable and continuation

For each completed tractate, provide authoritative normalized core tables, a generated per-sugya view, an eligibility ledger, exact manifests, per-layer coverage, independent readings/discrepancies, validation, unresolved cases, and replay/resume instructions. Provide the read-only Hebrew RTL reader where source display is permitted. Zero eligible examples for a demanding task is a legitimate reported result. Implementing every proposed benchmark adapter is not required before core delivery; add task exports as their records and policies become ready.

The corpus report must state: queued/running/checkpointed/completed jobs; source and semantic coverage separately; independently read coverage; task-eligible records; blockers; measured time and available token/cost telemetry; exact branch/commit/artifact hashes; and next job.

Continue draining available jobs in this authorized mission while the execution environment allows it. If a platform limit interrupts you, save a verified checkpoint and a single precise resume instruction. Mark unfinished jobs honestly. Do not promise autonomous background work after the session ends. A source or runtime block should identify the concrete missing input and the completed useful work, not trigger a request to approve routine windows.
