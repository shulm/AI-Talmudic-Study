# L03 portable checkpoint: 810 cores across each required pass

Rosh Hashanah242/1025; Yevamot218/3869; Eruvin130/3646; Kiddushin50/2406; Nazir50/1299; Arakhin50/1183; Tamid70/207. Total810/13635,12825 remain. Zero whole tractates delivered. Extraction coverage, bounded independent review, and task eligibility are distinct; task eligibility remains false.

SESSION_CHECKPOINT.json binds all seven exact snapshots, immutable accepted proposal chains, owners/epochs, original source paths/hashes, coverage, open tails, unresolved IDs and export manifests. COORDINATOR_AUDIT.json verifies actual coordinator revision6, contract Git blob, production code/schema/protocol Git blobs and both checkout files, seven exact Wikisource sources/schemas, owner equality and original source indices. The coordinator ledger explicitly records historical observed captures; newer valid lane progress is preserved. No shared implementation, source corpus or ownership change occurred.

The new package is F:/Sefaria_QA/bavli_l03_checkpoint_20261127_03.zip. ZIP SHA256:4f32396e738f8c215559c84000f3c8a07cd2df97f57bc4e29dd590d8d6611b0a. Package manifest SHA256:187d24c8239e5da52f9d88c5ca58b2b69ed0783a06d997589bee44d4537d8432. All849 manifest files and850 ZIP members were independently hash-verified. Fresh reconstruction of60 accepted proposals reproduced all7 captured snapshots exactly. all_37_reconstructed=false is expected for this seven-job lane. No full source corpus is included; separately pinned source access is required. Older390/590-core packages remain unchanged.

Reconstruct into a fresh external directory with the unchanged shared utility:

```powershell
python -X utf8 research/bavli_dataset_runs/reconstruct_release.py --release F:/Sefaria_QA/bavli_l03_checkpoint_20261127_03/run/releases/L03_checkpoint.json --source-root F:/Sefaria-Export-master --output F:/Sefaria_QA/bavli_l03_replay_20261127_03
```

The displayed output path already holds the verified reconstruction; choose a new path for a new replay. A verification copy is never a production owner. Original arrays are preserved, including Tamid’s starting[49,0] and Nazir’s empty page65.

Review entry points are continuation_wave_20261127_03/REVIEW_CLOSURE.md and continuation_wave_20261127_04/REVIEW_BINDINGS.json. Original initial candidates, source readings, targeted rework, rejected local schema candidate, corrections and exact-version rechecks remain immutable. Independent reviewers have disclosed prior source/context exposure; no fresh random cohort or complete tractate review is claimed. Review limitations—including Eruvin duplicate relation counts, ambiguous abbreviations, grouped comparative premises and pending task-specific admission—remain visible.

Captured next refs: RH10b6,YV9b9,ER5b3,KI4a12,NA4a2,AR3a16,TA28a12. After verifying live CURRENT/OWNER and exact pins, resume canonical jobs under F:/Sefaria_QA/bavli_production_run_20261125_01/L03. Reuse or immutably revise context records when they become cores; extend open primary structure without gaps/overlap. Never rerun old builders against later snapshots. The frozen next Eruvin20 source reading is preparation only; it adds no covered cores. New work may advance live pointers after capture; this package stays historical. Keep draftPR22 unmerged. No background continuation is implied if the platform interrupts execution.
