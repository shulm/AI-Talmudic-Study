# L03 production checkpoint — 2026-11-25

> Historical checkpoint: the counts and package hashes below describe the frozen 2026-11-25 package. The later bounded Rosh Hashanah correction is in [review_correction_20261126](../rosh_hashanah/review_correction_20261126/RESUME.md). Its response binds the exact comparison, reader, verdict and revised snapshot. Independent correction verification remains pending; coverage and zero-of-seven delivery status are unchanged. Resume new source production only under the coordinator’s next-wave dispatch instructions.

**PARTIAL_REQUIRED_WORK_REMAINS. Zero of seven tractates delivered.**

The user-appointed L03 lead verified the immutable active contract, production commit, every frozen production-file hash, output schema/protocol, all seven exact named-edition sources and schemas, the 13,635-segment inventory, source-package hash, original indices, historical owners and checkpoints. The coordinator's revision 3 records prior producers inactive. The user authorizes this lane only; no cross-lane reassignment occurred.

| Tractate | Complete source denominator | Each of eight passes | Next source | Current owner / epoch |
|---|---:|---:|---|---|
| Rosh Hashanah | 1,025 | 144 | 7a:3 | L03/rosh_hashanah / 3 |
| Yevamot | 3,869 | 158 | 8a:9 | L03/yevamot / 2 |
| Eruvin | 3,646 | 88 | 4a:10 | L03/eruvin / 2 |
| Kiddushin | 2,406 | 0 | 2a:1 | /root/lead_l01_l03 / 1 |
| Nazir | 1,299 | 0 | 2a:1 | /root/lead_l01_l03 / 1 |
| Arakhin | 1,183 | 0 | 2a:1 | /root/lead_l01_l03 / 1 |
| Tamid | 207 | 0 | 25b:1 | /root/lead_l01_l03 / 1 |

390/13,635 unique source segments have recorded completed passes at this checkpoint, including 14 inherited Rosh Hashanah segments. 376 were newly processed in this session. Each required pass has 13,245 remaining segments. The three active jobs contain 2,559 retained records, 2,543 active and 16 superseded. Counts measure recorded execution, not certified scholarly accuracy. No task-qualified ML records are claimed.

Rosh Hashanah and Yevamot had separate production agents. The lead produced Eruvin. A fresh non-forked reviewer read only source/common methodology before freezing its findings. Three production owners were active concurrently while the independent review slot was reserved. All are now checkpointed inactive; no background continuation is implied. The last four tractates remain queued and were not dispatched. The full assignment was not completed within this session's execution capacity; there is no source/access blocker.

## Immutable contract

- Run: `run_20261125_01`; coordinator branch: `dataset/bavli-coordination-v1`.
- Contract commit: `53bfbacb8f95d625f5036b73109eef738277e7e7`.
- Contract SHA-256: `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174`.
- Production commit: `15bba19d80273232b4554dfe507ceb37e97843a2`.
- Schema SHA-256: `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa`.
- Protocol SHA-256: `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2`.
- Source manifest SHA-256: `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`.
- L03 source ZIP SHA-256: `820487dce3d741f6009979eb2b2c8d399951471ba4d2978ebc2be50c2a9605d3`.

`ADMISSION_AND_DISPATCH_001.json` preserves all seven source paths/hashes, starting/ending coordinates, empty-page indices, inventory equality and preproduction checkpoints. Tamid begins at original page index 49 (25b); Nazir has an empty page at index 65. No empty source strings occur in these seven pinned files. Empty pages remain in the index map. Source corpora were not edited or copied into Git.

Authorized same-lane handoffs used the shared runner: Rosh Hashanah epoch 2→3, Yevamot and Eruvin epoch 1→2, from `/root/lead_l01_l03` to their above owners. The global ledger was not edited; the coordinator should incorporate this receipt. Historical proposals and owner histories remain intact.

## Review and unresolved work

Rosh Hashanah's frozen probability/endpoint **initial reading** is complete: 32 blocks, 315 cores, 397 substantive findings, 37,277 core codepoints. Probability sample: 300; endpoint addition: 15; overlap: zero. The reader separately logged 469 context-only segments. All 1,305 saved evidence/context spans and plan/source/receipt hashes were checked. Manifest SHA-256: `4c536471e8b8a1b66e720a20dc82307dcd811419db7d13c02ae29c354a2fecc2`.

No comparison, source-first omission comparison against production, complete risk review, demanding-task qualification, or integration acceptance was performed. All other tractates' source-first cohorts remain unstarted. Do not turn the completed reading sample into a whole-tractate review badge. Some independent findings group several atomic points; split those explicitly when constructing a comparison denominator.

Preserved risks include variant attribution, alternative versions, rejected proofs, partial continuations, and uncertain identities. Eruvin retains both reversed Rabbah transmissions with their separate Rava-of-Parzakya/Ravina explanations. Yevamot has five recorded open structural tails, requiring reconciliation from their original source, not deletion to obtain closure. Rosh Hashanah preserves names/versions and a fiscal proof rejected by its continuation. Worker handoffs contain exact IDs and source scope.

The first Eruvin derivation proposal failed duplicate-ID validation and remains saved as `eruvin_derivation_001.json`; accepted version 002 adds the layer to record IDs without changing its interpretations. Rosh Hashanah also preserves a rejected open-tail serialization attempt. Neither rejected attempt counts as accepted coverage. The authored scripts document initial generation; **replay uses immutable proposal bytes**, not rerunning author scripts against later state.

## Replay and resume

Run from the isolated L03 checkout. The current job directories are under `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/`.

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 research/bavli_source_access_v1/source_packages.py --lane L03 --package F:/Sefaria_QA/bavli_source_packages_v1/L03.zip
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin
```

Inspect the new coordinator pointer and actual `OWNER.json` before resumption. If the recorded owner remains current and inactive, the admitted lead may issue another explicit within-lane handoff and save its receipt. Do not run two promoters. Resume exact next coordinates above with overlapping original-source context and all eight passes. Keep independent source-first contexts separate. Start the remaining queue in its stated order as production capacity becomes available; whole-tractate delivery remains the goal.

`SESSION_CHECKPOINT.json` binds the complete seven-job snapshot matrix, accepted proposal chains, layer coverage, unresolved IDs, local epochs, package and ZIP hashes. The external package includes all accepted proposals, typed exports, coverage, per-sugya views, qualifications, unresolved records, independent readings and initial/rejected provenance. It contains no full source corpus.

For a fresh deterministic reconstruction use the existing shared command, the package's lane release, verified original sources, and a **new external destination**:

```powershell
python -X utf8 research/bavli_dataset_runs/reconstruct_release.py --release F:/Sefaria_QA/bavli_l03_checkpoint_20261125_01/run/releases/L03_checkpoint.json --source-root F:/Sefaria-Export-master --output F:/Sefaria_QA/bavli_l03_replay_20261125_01
```

The reconstruction utility's `all_37_reconstructed=false` is expected for this seven-job lane package; inspect all seven matching job hashes. A reconstructed directory is a verification copy, not a new production owner. New semantic generation is a new attempt, never deterministic replay.

No shared implementation or ontology was changed. Global proposals belong to the coordinator/integrator and engineering owner; see worker routing notes and `SHARED_OWNER_PROPOSALS.json`. No metered external APIs were used. Token/cost telemetry is unavailable. Keep this draft unmerged.
