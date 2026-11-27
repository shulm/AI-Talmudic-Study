# Production run 20261125_01

**2026-11-26 coordination update:** Assignment revision 4 supersedes revision 3 for production owners and observed checkpoints. [Later-checkpoint reconciliation](releases/ownership_reconciliation_20261126.json) verified 15 within-lane epoch changes and 1,048 claim-pass source segments. These later snapshots are not yet an integrated release or completed independent review. Snapshot 004 and STATUS.json below remain historical release evidence; do not use their inactive-session statement to infer current worker activity.

Status: **PARTIAL_REQUIRED_WORK_REMAINS**, not a completed Bavli corpus. Draft [PR #17](https://github.com/shulm/AI-Talmudic-Study/pull/17) remains unmerged on `dataset/bavli-coordination-v1`.

## Immutable execution contract

- [Active pointer](../ACTIVE_RUN.json), contract commit `53bfbacb8f95d625f5036b73109eef738277e7e7`; first pointer commit `f4153e3086bfd035da02ce826eb4175cd260378f`.
- [RUN_CONTRACT.json](RUN_CONTRACT.json), SHA-256 `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174`.
- Production code commit `15bba19d80273232b4554dfe507ceb37e97843a2`.
- Schema `2.0.0-production`, SHA-256 `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa`.
- Protocol SHA-256 `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2`.
- Source manifest SHA-256 `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`.

Contract values describe bootstrap readiness, not current completion. [ASSIGNMENT_LEDGER.json](ASSIGNMENT_LEDGER.json) revision 3 records all current owners, per-tractate epochs and exact checkpoints. Earlier ledger revision 2 is preserved in `assignment_history/`. All six lanes launched actual local interactive-agent production. No paid external API calls were introduced. Model identifiers unavailable to the runtime remain null rather than guessed.

## Current evidence and limits

[Snapshot 004](releases/snapshot_004.json) contains 764 active typed records and preserves 64 superseded initial/revised records. 763 active records survive the release quarantine overlay. Eight required extraction passes each cover 82 distinct source segments; zero of 37 tractates is delivered. The 31 source-only jobs contain no invented annotation. [Exact unfinished jobs and blockers](REMAINING_WORK.md) lists all 37 next coordinates and remaining counts; the JSON snapshot lists all missing ranges separately by layer.

The real shakedown covers inherited Berakhot B24 and a fresh Rosh Hashanah block. [SHAKEDOWN.json](SHAKEDOWN.json) and `verify_shakedown.py` verify source/schema/quotes/partition, interruption recovery, idempotency, stale-owner rejection and deterministic replay. Later valid inherited structural work through Berakhot 9a:29 was preserved, not restarted or counted as complete semantic work. [Inheritance audit](../../bavli_inheritance_audit_v1/) preserves the later checkpoint and migration accounting.

Source-first initial readings and subsequent comparisons are frozen separately under `review/`. Later correction-verification artifacts explicitly disclose their exposure to those readings and producer corrections; they are not new blind readings. Targeted review is not the required full-tractate probability/endpoint/risk review. All 37 source-coordinate plans are frozen under `review_plans/`.

[Quarantine](QUARANTINE.json) excludes one unsupported Chullin attribution role. Raw producer snapshots retain it as initial evidence; their local `release_state` is not authority to bypass this integration overlay. Use the integrated release policy, not unfiltered raw exports. [Review receipt protocol](../REVIEW_RECEIPT_PROTOCOL.md) defines the separate whole-tractate admission gate. The producer runner conservatively reports review/delivery false; the integrator requires actual hash-bound review and complete passes before any delivery badge.

[Reconstruction receipt](releases/reconstruction_snapshot004.json) records a successful fresh rebuild of all 37 job states from 18 accepted frozen proposals, using the approved source and zero new model calls. Every resulting snapshot hash equals snapshot 004. This reconstructs the new production core; legacy archives remain separately preserved and hashed.

## Source access by lane

L01, L02, L03, L04, L05 and L06 have verified local source access at `F:/Sefaria-Export-master` and deterministic lane packages at `F:/Sefaria_QA/bavli_source_packages_v1/<lane>.zip`. See [source access instructions](../../bavli_source_access_v1/README.md) and contract descriptors for each exact ZIP hash. No complete source copy is stored in Git. No remote package receipt or reachable remote execution platform was established. Readiness applies to this verified local route only.

## Verify and resume

Run from this checkout with Python 3.11+ and the existing `jsonschema` dependency:

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 research/bavli_dataset_runs/run_20261125_01/verify_shakedown.py
python -X utf8 research/bavli_source_access_v1/source_packages.py --lane L01 --package F:/Sefaria_QA/bavli_source_packages_v1/L01.zip
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot
```

For other lanes use the exact job directory from the ledger. Read each current checkpoint, open tails, correction verification and original continuation before issuing the next semantic proposal. Use `runner.py packet` for the next source range and expand context to the complete relevant discussion. Submit with that job's existing owner and epoch. Keep initial judgments, all uncertainty, source offsets and rejected assumptions. Proposals belong in that lane's `proposals/` directory and are promoted by the sole authorized job writer. Save new export directories and exact-version receipts; never overwrite an earlier snapshot.

To rebuild this release on another authorized host, first obtain and verify the original source packages. Then choose a **new empty external** output path:

```powershell
python -X utf8 research/bavli_dataset_runs/reconstruct_release.py --release research/bavli_dataset_runs/run_20261125_01/releases/snapshot_004.json --source-root F:/Sefaria-Export-master --output F:/Sefaria_QA/bavli_reconstructed_checkpoint004_new
```

This is deterministic replay, not a second concurrent production owner. The coordinator must explicitly hand off ownership before a reconstructed copy can accept new proposals. Only the coordinator transfers jobs across lanes. Per-tractate epochs, not global ledger revisions, authorize writes. Existing leads may continue within their declared groups without new user approval.

For the next rolling release use `integrate_run.py --run-dir research/bavli_dataset_runs/run_20261125_01 --output NEW_IMMUTABLE_JSON`. Full-trace source passes, frozen source-first review and resolved integrity exceptions are mandatory for delivery. Keep drafts unmerged. Producer sessions are inactive at this checkpoint; there is no autonomous background service implied by the saved assignments.
