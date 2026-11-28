# Resume Menachot and Beitzah — partial checkpoints

Both jobs remain incomplete and unreviewed. No tractate delivered. Owner `/root/menachot_owner`, epoch 2, under L06. Production and contract hashes were verified before dispatch; source replay re-verifies pinned source/schema files. No shared infrastructure or global ledger was edited.

- Menachot: 73/3783 source segments per required layer. Next Menachot 4a:6. Exact receipt: ../menachot_20261126/checkpoint004.json. Source context read through 4b:1; context is not coverage.
- Beitzah: 42/1151 per layer. Next Beitzah 3b:4. Exact receipt: checkpoint003_final.json. Context read through 4a:1.

External root: F:/Sefaria_QA/bavli_production_run_20261125_01/L06/. Each job retains immutable proposals, snapshots, original source manifest, inventory, ownership history and CURRENT pointer. Helpers/exports under menachot_owner_epoch2 are isolated by job.

Run the shared runner replay on each job before resuming. Do not rerun authored scripts indiscriminately: Menachot batch003 first attempt has a preserved duplicate ID; the corrected accepted proposal is separately saved. Submit exact accepted proposal bytes for idempotent recovery. Fresh semantic generation is a new attempt.

Full common-schema exports and manifests are Menachot menachot_owner_epoch2/export004 and Beitzah menachot_owner_epoch2/export003_final. Coverage, qualification, per-sugya, unresolved and core-layer files are inside each export, with exact file hashes in manifest.json. All legacy ML eligibility remains false.

Lead requested a durable handoff after Beitzah checkpoint; production is inactive after this receipt until reassigned. No background continuation or complete independent review is claimed.
