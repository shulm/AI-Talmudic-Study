# L06 captured checkpoint09

Each exact captured snapshot was reconstructed from the complete proposal chain against original sources. Replay matched byte-for-byte. Producers continue concurrently; this capture is not a claim of latest live state.

| Tractate | Completed each pass | Next source |
|---|---:|---|
| Bava Kamma | 231/4314 | Bava Kamma 8a:11 |
| Menachot | 197/3783 | Menachot 7a:7 |
| Niddah | 215/2665 | Niddah 8b:9 |
| Megillah | 125/1213 | Megillah 5a:5 |
| Beitzah | 190/1151 | Beitzah 8a:8 |
| Meilah | 121/515 | Meilah 6b:1 |

Total 1079/13,641 per pass; 12562 remain. Historical records: 6251. Zero delivered or task-qualified tractates.

Independent source-only checkpoint005 records361 unique cores and834 context-only segments. Parent verified1373 saved evidence slices against exact sources.1720 planned cores remain. Integrity verification is not semantic comparison. The separate global51-core Niddah comparison is preserved in checkpoint07; do not double-count overlapping coordinates or transfer acceptance to later versions.

Meilah preserves pigul proof/rebuttal stages, priestly-permission alternatives, named transmission, and unresolved support-transfer/temporal questions through6a:19. First draft and inferred-speaker corrections remain available. Repeated reports and parallel arguments are proposed as typed links without collapsing occurrences.

Each jobs/<job_id> contains JOB, OWNER, captured CURRENT, full proposal chain, exact snapshot and exports. To replay, restore to a fresh external directory, supply approved source_manifest.json SHA11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c and original source_root access, then run pinned runner.py replay --job-dir <restored-job>. Verify coordinator and live owner/current before resuming; do not overwrite active jobs.

Initial commit50ce200 held production captures only after a review-manifest field-name mismatch. The subsequent completion preserves those exact captures and adds this receipt/review package. No live production checkpoint was affected.

Original sources, shared schema/protocol/runner and ledger remain unchanged. Original provenance and CC-BY-SA metadata apply. Earlier first readings/corrections remain immutable. Keep PR24 draft and unmerged.
