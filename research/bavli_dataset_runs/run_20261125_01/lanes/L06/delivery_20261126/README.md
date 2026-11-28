# L06 partial execution checkpoint — 2026-11-26

**Incomplete: zero of six tractates delivered.** This package preserves actual annotation work, independent first readings, revisions and reproducible checkpoints. It does not fulfill the all-six completion request.

| Tractate | Completed source segments in each of eight required passes | Denominator | Next source |
|---|---:|---:|---|
| Bava Kamma | 80 | 4,314 | 4a:10 |
| Menachot | 73 | 3,783 | 4a:6 |
| Niddah | 35 | 2,665 | 3a:12 |
| Megillah | 29 | 1,213 | 2b:6 |
| Beitzah | 42 | 1,151 | 3b:4 |
| Meilah | 41 | 515 | 3b:8 |

Total: 300/13,641 source segments per required pass; 13,341 remain. Twelve Bava Kamma segments were inherited. There are 1,817 historical records, including superseded versions. Counts are source occurrences, not unique topics or independently established decisions. Completed passes are provisional agent reading/extraction assertions, not scholarly completeness certification.

All six exact named-edition sources, their source schemas, package, immutable run contract, production implementation, output schema and protocol were checked. The initial assignment-file hash check exposed CRLF checkout conversion; the exact Git blob matches the pinned contract, and normalization was verified without changing the file. Both initial and resolved audit results are retained in the sibling verification directory. Coordinator revision 4 was rechecked; contract and production commit were unchanged. The global ledger is not edited here.

Production used the pinned common runner. All six final checkpoints pass deterministic replay. `LANE_RECEIPT.json` records exact snapshot, proposal, source, export-manifest and contract hashes; each job contains authoritative exported tables, per-sugya overlap views, coverage, qualification and unresolved records. Source inventories and full source files are excluded from this package. Proposals and snapshots contain bounded original evidence, including preserved rejected attempts and first readings.

Independent source-only readings were created in a fresh agent context before exposure to producer labels. Six opening cores and five Menachot probability blocks are frozen: 110 unique core segments, 417 context-only segments, 600 validated evidence slices including repeated context. Plans are not completed review. Another 1,971 planned core segments, all closing endpoints, risk review and qualification work remain. The separate global review lead has overlapping Bava Kamma readings; do not add these counts without source-coordinate deduplication.

The independent Bava Kamma comparison found a missing horn-elimination edge. The new `bk06_e_horn_elimination` revision adds it while retaining the original omission. The exact corrected snapshot is in the receipt; the global reviewer independently verified the targeted correction at this snapshot. Its original comparison, rework verdict and correction receipt are preserved under `global_review_comparisons`; the intervening new records and full tractate are not thereby admitted. Niddah's producer comparison preserved a scope correction from the frozen independent reading: Hillel's retrospective statement concerns pure objects, not retroactive marital prohibition. Self-corrections also preserve the initially omitted explicit כיצד question and split Meilah's named Rabbi Yohanan report from the anonymous inference about rabbinic meilah. No record is ML-qualified; no human scholarly review is claimed.

Typed parallel proposals remain proposals for the integrator. Repeated mikveh quotations, repeated attributed reports and related passages have not been collapsed. Open structural tails and uncertainty arrays remain explicit; consolidation and cross-window reconciliation must continue with the next sources.

## Replay and resume

1. Read the current coordinator `ACTIVE_RUN.json`, immutable contract, current ledger and live job `OWNER.json` before any mutation. All six jobs in this delivery are checkpointed inactive at epoch 2. Do not assume an unchanged owner merely from this package.
2. Use production commit `15bba19d80273232b4554dfe507ceb37e97843a2` and the pinned source edition. Verify the actual source bytes against each job's source manifest. The original source path is `F:/Sefaria-Export-master`; it is local storage, not a transferable URL.
3. Existing authoritative jobs are under `F:/Sefaria_QA/bavli_production_run_20261125_01/L06/<job_id>`. Resume these, not duplicate active writers. For archive replay only, copy a packaged `jobs/<job_id>` directory to a fresh external directory; retain its immutable bytes and provide the exact source root required by `JOB.json`.
4. Run `python -X utf8 research/bavli_production_v1/runner.py replay --job-dir <job-directory>`. Compare the resulting snapshot hash with `LANE_RECEIPT.json`. Replay needs the accepted proposal chain, current snapshot, original source and manifests; a new model reading is not replay.
5. An authorized lane lead transfers each job with `handoff --job-dir <job> --owner <current-owner> --epoch <current-epoch> --new-owner <new-owner>`. Preserve and record the incremented local epoch; do not edit the coordinator's global ledger.
6. Read original overlapping context around the next reference in the table, inspect open tails and prior revisions, and continue all eight passes. Freeze proposals, submit through the shared runner, replay, and export to a new immutable directory after each batch. Do not restart from the beginning or erase rejected proposals.
7. Keep source-first review separate, preserve first readings before comparison, and complete the frozen sample, endpoints, risks and task-specific requirements. Review plans alone do not establish review coverage.

All producers and the local reviewer stopped at this durable checkpoint. No background continuation is claimed. No source/access blocker was found; required extraction and review are unfinished. The remaining task is substantive annotation and review, not another planning phase. New paid external API calls: zero. Unavailable token/cost telemetry remains unknown.

## Provenance and distribution

Source edition: Wikisource Talmud Bavli, Hebrew, via the pinned Sefaria export. Original metadata records `CC-BY-SA`; no numeric license version is invented. Exact source attribution and version metadata remain in every `JOB.json`. Text-bearing annotations retain these source obligations; this delivery does not assign a blanket new license to code or annotations. Full source files and inventories remain outside Git.

Draft only. Do not merge or label any tractate complete on the basis of this checkpoint.
