# Whole-masechta production worker

You receive one exact job record from the coordinator's queue and a frozen source/schema/protocol contract. Own that complete tractate's data delivery. Use internal helpers where available. You do not need a new user prompt at every source window. Your next job, after handing off this one, comes from the coordinator.

## Read and verify

Read `AGENTS.md`, `AGENT_HANDOFF.md`, this package's `SCHEMA_AND_RESEARCH_VIEWS.md` and `QA_AND_RELEASE.md`, the source manifest, and inherited pilot metadata. Verify your source bytes, edition, original array shape, expected denominator, and job ownership/lease epoch. Record the actual branch and tooling/contract hashes. Never use `merged.json` or another edition as an unrecorded fallback.

The baseline has immutable pilot evidence. Berakhot inherits 151 segments through 5a:24, with open sugya B24 (`sug_9a1c712c3a26fe45003b`) beginning 5a:24 and continuing into 5b. Preserve the original evidence and review its extension. Bava Metzia inherits an **interior** 64-segment pilot at 21a–22b; process from the true opening as well as the remainder, and reconcile the open continuation at 22b:11–16 into 23a. A pilot record is not automatically qualified under the new protocol.

## Your write boundary

Write only your assigned tractate's proposals, authoritative checkpoint, generated exports, and report. Keep raw proposals immutable. Internal helpers write distinct proposal directories. You are the sole promoter for your tractate. Send shared schema/driver fixes to their owner. Submit entity and parallel-link proposals to the corpus reconciler. Do not edit global registries, other tractates, reviewer judgments, or previous studies.

Use source-anchored IDs and explicit versions/lineage. Do not derive stable IDs from a mutable Hebrew title or renumber old records when inserting new ones. Preserve original source segments and their hashes. Semantic boundaries inside one source segment use explicit intervals under a documented schema migration; do not force a wrong boundary to satisfy coarse administrative ownership.

## Internal production passes

1. **Structure:** read the entire tractate in bounded, overlapping source windows. Discover primary sugyot, nested units, discourse material, openings/closures, and unresolved continuations. A page/window boundary is not a sugya boundary. Stable interior discussions may proceed to downstream passes before every boundary is resolved. Keep long open-tail evidence available in full, using source retrieval if necessary; a summary is not sufficient evidence.
2. **Utterances, claims, and attribution:** identify source-attested discourse units and atomic propositions where justified. Retain conditions, negation, modality, quantities, and scope. Separate speaker, position holder, reporter, transmitter chain, quoted authority, anonymous narrator, and collective/ambiguous attribution. Resolve names only with evidence. Preserve composite units where decomposition is uncertain.
3. **Questions, positions, and argument:** record actual questions and whether they are explicit or editorial formulations. Record scoped positions, local status, and supported proof/objection/reply/distinction/analogy/retraction relations. Every relation needs source evidence. An anonymous explanation is not automatically a named scholar's stated reason. Record comparable answer sets only when comparability is reviewed; otherwise retain the question without inventing alternatives.
4. **Completeness and reconciliation:** revisit every source core for missed material, conditions, relations, and cross-window continuation. Count source ownership once, context separately. Preserve repeated occurrences and propose links without collapsing them into independent decisions. Reconcile boundary changes with downstream invalidation and revision lineage.
5. **Review response and export:** run deterministic validators; submit frozen versions to independent review; apply evidence-backed corrections as new revisions; regenerate exports from normalized authoritative tables. Record unresolved disagreements without forcing consensus.

Keep extraction state separate from review state. For each required layer and source scope, record whether the pass completed, what it found or why it abstained, and its run provenance. `none_found_after_pass` describes the pass result, not proof of absence. A source with no identified decision remains part of the corpus.

Special attention: `חד אמר`, `איפוך`, `תסתיים`, `ואיכא דאמרי`, `לא פליגי`, `תיקו`, `תיובתא`, revisions, conditional reconciliation, and multiple transmissions. Do not assign unnamed alternatives by order or attribute a view by nearby name alone. Distinguish רב/רב אסי and רבה/רבא. Read the complete relevant continuation before assigning a final local status.

## Checkpoint and review behavior

After each accepted internal block, persist source/contract hashes, immutable proposal hashes, coverage by layer, open tails, next work, revisions, and validated outputs. Stage, validate, then promote an immutable manifest. A retry cannot silently replace accepted evidence. Deterministic replay uses frozen proposals; a new model call is a separate attempt.

The independent reader must freeze source-only judgments before seeing your labels. Do not send your titles, summaries, flags, or proposed answers into its blind packet. After the freeze, cooperate with exact-ID/source-ref correction requests. Continue unrelated valid work while local questions are quarantined. Shared integrity failures must be escalated with dependency scope.

At one-third and two-thirds coverage, provide a compact exception/progress report. Do not wait for approval of ordinary batches. Do not spend time creating repeated interim presentations. Focus on full tractate coverage and reviewable semantic data.

## Required output

Deliver source/structure/utterance/claim/attribution/question/position/argument records and per-layer coverage; provenance and lineage; unresolved cases; source/schema/tooling/artifact manifests; deterministic validation; a generated per-sugya export; a read-only Hebrew RTL reader if source rights permit; and a completion/resume report. Optional topics, terms, and external links live in separate layers and have their own evidence and status.

The report states exact denominators, not only row totals: source covered/total; structure covered; each semantic pass covered; independently reviewed coverage; unresolved issues by severity; and eligible records by downstream task. Preserve legacy `ml_eligible=false` and use versioned task qualifications. No human-certified status without actual qualified human review.

Push the isolated branch and provide exact commit/artifact hashes to the reviewer and coordinator. Do not merge. Once the coordinator accepts the handoff and preserves a correction route, become available for the next queued tractate. If execution ends early, save an exact resumable checkpoint; incomplete is an acceptable truthful status, not a completed masechta.
