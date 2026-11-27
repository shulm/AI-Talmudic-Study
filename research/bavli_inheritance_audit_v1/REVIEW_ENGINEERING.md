# Independent minimum-runner engineering review

Status: **minimum engineering path approved at the file hashes below**, subject to coordinator freezing the same implementation and separately verifying actual semantic shakedown outputs. This is not semantic coverage certification or full tractate delivery approval.

Reviewed source binding, isolated ownership epochs, immutable proposals/checkpoints, interruption recovery, replay, migration, typed layers and coverage checks. Review was conducted independently of implementation; only engineering owner changed production code.

## Findings corrected before approval

1. Unknown open tails and silent dropping of inherited tails were accepted. Runner now requires exact equality with active open structure IDs.
2. Revisions could leave active positions/edges/links referencing superseded records. Runner now rechecks all active dependency references.
3. Multiple competing successors could supersede the same record. Runner now rejects ambiguous or stale revision successors.
4. Initial JOB publication preceded required files and could strand a crashed initialization. JOB is now published last and an identical initialized job resumes.
5. Migration previously lacked epoch authorization. It now checks expected owner/epoch.
6. JOB source metadata now must match freshly verified pinned manifest source hash/count.
7. Reports now expose extraction outcomes separately, including abstention. A completed extraction pass does not imply resolved interpretation or independent review.

Initial findings 1–3 were reproduced with synthetic fixtures; see engineering_initial_probes.json. Subsequent regression suite passed all 15 tests independently, including source quote/Unicode offset integrity, partition gaps/overlap, schema/contract rejection, immutable proposal replay corruption, stale ownership, interrupted checkpoint promotion, idempotency, graph revisions and tails.

Additional isolated tests used actual pinned Berakhot bytes: all 2749 source segments load, init interruption before JOB publication recovers, init resumes, stale migration owner rejects, actual inherited migration preserves 8 table files/1327 mappings, and an empty semantic chain replays without claiming extraction. See engineering_source_checks.json. These checks create no real semantic production records.

## Limits and remaining production obligations

The runner supports full-tractate source loading and incremental structured proposals; it does not independently generate or certify their interpretation. Schema checks cannot certify that a zero-record pass, generic rationale, or purported reconciliation reflects real source reading. Blind source review and omission testing remain necessary. Reconciliation is a coverage pass rather than an independent semantic table. Review completion and tractate delivery remain explicitly false; implementing their admission gates and delivery artifacts is still required before any finished-tractate claim.

The OS lock and per-job epoch prevent accidental concurrent/stale promotion. They do not authenticate organizational identity or protect against an adversary with filesystem write authority; handoff authority remains coordinator/lane policy. Production commit/run-contract verification occurs before dispatch outside this runner.

Legacy migration archives table bytes and explicit unmapped semantic records; it does not convert old selected semantics into completed new layers. The separate inherited snapshot preserves context, proposals, revisions and other non-table lineage files as well. The coordinator must retain that snapshot and its manifest.

All semantic records stay unreviewed and ML-ineligible. This review does not approve full semantic coverage through generic markers. Actual inherited/fresh source shakedown annotation review is separate.

## Reviewed file SHA-256 values

- `.gitignore`: `32dae3052f331ee34d628ef535709b301259a45df7c7522c4d35dcf49873f00b`
- `PROTOCOL.md`: `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2`
- `README.md`: `a10fcf9c60fa1b6d2009300ed9675fd0d29122a45773d2cc741a617fd3a1a77c`
- `runner.py`: `c93f53ac423eed853f375e1316f29242ec242ed730c44deb6f13879d8d18b9d0`
- `schema.json`: `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa`
- `test_runner.py`: `200767dcf0dde2d6df49b353d3643084be93c03f8059d290f01c7885d9da32e3`

## Final export and portability addendum

Minimum engineering approval extends to final runner SHA-256 `b929c6bb529eb27c306d925bc234cfa051ea199fd7dcbce4be0a3be4673f8dc0`. All **17 tests passed** independently. Export binds immutable tables, coverage, qualification and per-sugya contextual views to a checkpoint hash; views explicitly claim only source-segment overlap, not semantic containment. Compatibility export checks migration and original-file hashes and preserves bytes. Use a fresh output directory per checkpoint: export artifacts are immutable, and existing differing files correctly fail. This reviewer found no material blocker in the additions.

Source-package portability reviewed at SHA-256 `46ecd53e5d5699602fc4419d3d5f2a8477d8d068fbab7adeb0c800262a0690a8`: only ASSIGNMENTS metadata line endings are normalized against the pinned LF hash, then serialized to fixed historical CRLF package metadata. Source/schema/TOC bytes are never normalized. An isolated simulated LF checkout produced identical inventory/package metadata; all six existing ZIPs verified successfully, and the source-root audit passed 37 tractates/81,793 segments. This establishes local package integrity and portability, not delivery to remote platforms.

Coordinator SHAKEDOWN.json was inspected as method evidence: actual saved proposals cover four source segments in each of Berakhot and Rosh Hashanah with source/schema/restart/replay checks and explicitly incomplete whole-tractate status. This inspection is not blind semantic review and does not upgrade coverage claims. Detailed final checks and hashes are in engineering_final_checks.json.
