# Whole-masechta assignment — Arakhin / ערכין

You are the production owner for **Arakhin only**, delegated by **L03**. Complete its full required core dataset under the shared production contract and submit exact-version evidence for independent review. This file is a prepared assignment, not proof that work has started.

Repository: https://github.com/shulm/AI-Talmudic-Study

Launch package: `research/bavli_multiplatform_launch_v1/`.
Design baseline: `research/bavli_dataset_program_v2/` at `5876cb9dfd40dbadecb4a79273e59631fe1f127a`.

## Exact job identity

- Lane: `L03`; job: `bavli_arakhin`; order within lane: 6.
- Source edition: `Wikisource Talmud Bavli`; source language: `he`.
- Complete source denominator: **1183 segments**.
- Original source-relative path: `json/Talmud/Bavli/Seder Kodashim/Arakhin/Hebrew/Wikisource Talmud Bavli.json`.
- Required original-file SHA-256: `1a25d9524ec1d35eee64749794e158a24bfa10177bc9c6db56b4fca6adbc9ed4`.
- Source schema path: `schemas/Arakhin.json`.
- Source schema SHA-256: `b7839fc28149ac6d436991936a85057d1781596bba27365a916d0112e6430804`.
- Historical source-manifest SHA-256: `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`.
- Original first nonempty reference: `Arakhin 2a:1`.

## Activate or resume

Read repository instructions and this package's `COMMON_EXECUTION_CONTRACT.md`. Retrieve the coordinator's `research/bavli_dataset_runs/ACTIVE_RUN.json` from its recorded coordination branch (default `dataset/bavli-coordination-v1`), then verify the immutable run contract, actual production commit/schema/protocol hashes, source access, your lane ownership, and assignment epoch. The old `2.0.0-design` label is not execution readiness. Keep source bytes read-only and reject any hash mismatch.

The historical baseline has no semantic pilot for this tractate. Start at Arakhin 2a:1. If the live run already has a valid checkpoint, resume it after verifying ownership and hashes instead of duplicating it.

Use the pre-existing validated checkpoint when present. You own one tractate; only the lane lead or coordinator can issue your next assignment. Do not claim other lanes' work or update global registries.

## Execute the complete tractate

1. Read all source using bounded overlapping windows; preserve full relevant continuations and open tails. Identify primary/nested sugyot and discourse structure. Source windows and pages are not semantic boundaries.
2. Extract utterances and supported atomic/composite claims, conditions, negation and scope. Separate speaker, position holder, reporter, quoted authority, transmitter chain, anonymous voice, and unresolved identity. Use evidence rather than name proximity.
3. Extract actual questions, supported positions/local statuses, and evidence-bearing directed proof/objection/reply/distinction/analogy/correction relations. Record source-explicit versus editorial interpretation. Do not invent alternatives, questions, missing responses, or psychological motives.
4. Re-read for omissions and reconcile cross-window boundaries, attribution continuations, duplication and conditions. Complete and record every required layer's pass over the full source scope; no-findings or abstention requires an actual pass.
5. Validate exact source/quotes/spans, schema, source ownership, links, lineage and per-layer coverage. Respond to independent discrepancies as explicit revisions. Generate the normalized package, per-sugya view, qualification ledger, coverage and validation reports.

Retain narratives, anonymous material and supported uncertainty. Review state and task eligibility are separate from extraction. Quarantine unsupported forced resolutions or corrupted evidence locally while completing unrelated valid units. Preserve old `ml_eligible=false`; use separate task-specific qualifications. Optional enrichment must not delay core completion.

## Checkpoints and review

Use one production writer and immutable staged proposals/checkpoints. Save accepted artifacts, source/contract hashes, per-layer progress, open continuations, revision history, and exact next work after internal batches. Replay saved proposals deterministically; a new model call is a new attempt. Do not reset source hashes or erase earlier judgments.

A fresh independent reader receives a source-only packet and common annotation instructions, not this producer packet's pilot interpretations or your outputs. Its source-first reading must be frozen before comparison. Review ordinary source cores for omissions as well as risk cases. Preserve both readings and exact-version discrepancy resolutions.

Use actual available authorized agents and truthful telemetry. Do not request a user prompt for each window. If execution is interrupted, return a verified checkpoint and precise next resume step, without claiming background continuation.

## Required result

Deliver complete required core passes for all **1183 source segments**, with source integrity, per-layer extraction, independent-review coverage and task eligibility separately reported. Deliver immutable canonical tables, per-sugya export, review/qualification ledgers, unresolved cases, manifests and replay/resume instructions. A Hebrew read-only source view may be generated where source distribution permits. Do not commit full source copies into Git history.

Push only your isolated assigned branch and open a draft PR, or deliver a hash-verified package if this platform lacks Git write access. Provide the lane lead exact commit/artifact hashes, counts, source/contract IDs, review verdict, unresolved scope and correction route. Do not merge. Do not claim a whole tractate complete with missing source or unfinished required passes.
