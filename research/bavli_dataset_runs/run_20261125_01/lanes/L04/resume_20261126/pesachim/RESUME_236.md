# Pesachim continuation handoff — 236 segments

Authoritative job: `F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_pesachim`.
Owner remains `L04/pesachim_resume_20261126`, epoch 3. This worker is handing back production to the lane lead; do not launch overlapping writers.

Current snapshot: `ecb3dc24813b3635bbd1b9c61c96b44acafd94ed133d5cd8641d001b1efb36e5`.
All eight required passes cover 236/3519 segments through Pesachim 9b:9. Next: **9b:10**. Read context through 10b:20, but none beyond 9b:9 is counted as produced. Complete the uncertainty analogies through 10b:12 before closing that source unit. Read beyond 10b:20 before processing the later Mishnah dispute.

This worker added 165 segments (4b:8–9b:9) in accepted proposals 008–015. Fifteen total accepted proposals; 2541 active records, 2547 preserved versions. Common replay passes and two independently generated exports match all 36 file hashes. Exact source/schema and all nine frozen production files verified. See `CHECKPOINT_236_ecb3dc24813b.json` for hashes and full replay/coverage receipt.

Export: `F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_pesachim/exports/resume_20261126_236_ecb3dc24813b`.

Author scripts 008–015 are explicit readings, not extractors. They are stateful proposal generators and must not be rerun against a later CURRENT. The common runner, original sources, schema and protocol were not changed. Rejected proposal009 is retained externally: semantic continuation edges are disallowed by the common schema. Accepted009b replaced repeated-citation linkage with quotation and relies on contiguous primary structure for cross-page continuation.

New material is independently unreviewed and ML-ineligible. No tractate completion or choice eligibility is claimed. Composite lists are marked composite, not atomic claim counts. Question partial status is assigned only with represented linked local answers, with a nonexhaustiveness qualification; older statuses were not bulk relabeled. Known review-risk areas include literal biblical citation variants (6b:6), conflicting reports of Rava's blessing wording (7a:16), deictic light contrasts (8a:5), and source-based candidate interpretations of animal-removal certainty (9b:2–4). Named transmitter chains, anonymous voices, source-explicit retractions, narratives and uncertainty remain distinct.

Reproduce with the unchanged common runner's `replay --job-dir` and `export --job-dir ... --output <new immutable directory>` commands. Lane lead owns package capture, reviews and commits. This worker has made no commits or source edits.
