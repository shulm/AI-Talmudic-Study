# L01 partial production checkpoint — 2026-11-25

This is saved production data and review evidence, **not completion of the six-tractate assignment**. No tractate is delivered. Required semantic extraction and independent review remain unfinished; no source or tooling blocker has been established. The producers are inactive at this checkpoint. No background continuation is claimed.

`LANE_STATUS_AND_RESUME.json` records the exact source denominators, current tractate-local owners/epochs, accepted proposal chains, snapshot hashes, active and superseded counts, eight separate coverage counts, every missing source range, open tails, and next coordinates. `PACKAGE_HASHES.json` binds the saved files. Each tractate directory contains its authoritative snapshot, accepted immutable proposals, replay validation, and export manifest. Full typed-table/per-sugya exports remain at the recorded external paths and are included in the local companion ZIP. Source inventories and full original source files are excluded from Git.

## What ran

The immutable coordinator contract, actual production commit `15bba19d80273232b4554dfe507ceb37e97843a2`, schema/protocol, all six exact named-edition source files and source schemas, source package, and lane assignment were verified. The pre-existing inactive checkpoints were resumed. Same-lane owner transitions used the shared runner; the global assignment ledger and shared implementation were not edited. Reviewers used fresh source-only contexts and froze initial readings before comparison.

Berakhot's original151-segment pilot and later386-segment structural inheritance were preserved and checked against exact source data. This is source/structure revalidation, **not semantic completion of151 or386 segments**. The accepted B24 block already extended5a:24 into5b:3; it was revalidated and enriched after fresh independent reading. All initial and corrected judgments remain recoverable.

Independent evidence separates targeted continuation, opening endpoints, probability cores, and expanded context. Zevachim has only1 of39 probability blocks read; none of the six whole-tractate review plans is complete. Ketubot retains the two opposed Rava report versions and failed proof attempts. Condition omissions, occurrence/link omissions, and editorial boundary differences are recorded rather than erased. `review/` contains initial readings, comparisons, correction checks and reviewer provenance. These are AI reviews, not human scholarly certification. All records remain ML-ineligible.

## Resume without duplicating owners

1. Read the current coordinator `ACTIVE_RUN.json` and verify its contract and actual production files. Recheck the original source hashes and current `OWNER.json`; this saved package does not supersede a newer owner or checkpoint.
2. Run the pinned shared `runner.py replay --job-dir <external_job>` for each saved job. Compare the resulting snapshot with the resume packet. Do not regenerate accepted proposals using new model calls.
3. Resume at the recorded `next_unprocessed_by_layer`, reading sufficient original continuation. Berakhot has non-prefix coverage, so use its complete missing ranges. Complete all eight passes with actual source reading and scoped evidence.
4. Dispatch the next queued tractate only with one production owner, using the prefilled worker assignment. Sukkah and Chagigah still have zero semantic coverage. Only the coordinator transfers work across lanes.
5. Continue source-random, closing-endpoint, risk and task-specific review with fresh contexts. A reviewer exposed to producer labels is no longer blind for new readings. Keep all unresolved interpretations visible and eligibility restricted.

Commands run from a checkout containing the pinned implementation:

```powershell
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot
python -X utf8 research/bavli_production_v1/runner.py packet --job-dir <job> --start-ref '<next reference>' --end-ref '<context end>' --output <new source packet>
python -X utf8 research/bavli_production_v1/runner.py submit --job-dir <job> --proposal <immutable proposal> --owner <current owner> --epoch <current epoch>
```

The JSON snapshots and saved proposal chain also permit deterministic in-memory reconstruction via the same `runner.validate_apply` over the pinned original source. Historical proposal ownership remains in each proposal; do not rewrite it merely to fit a current epoch. Ownership handoffs affect future submissions only.

`authoring/` preserves manual serialization helpers and original attempted proposals; these are provenance, not a new shared runner or ontology. Some helpers reference the original local workspace. Use accepted immutable proposal bytes for replay, not rerunning authoring scripts against an already advanced checkpoint.

## Limits and engineering notes

The frozen schema lacks an addressee role. Ketubot3a:4 records Rav Ashi as addressee in utterance/scope prose, without falsely classifying him as a quoted authority. Any shared typed-role extension belongs to the engineering owner. Composite claims and unresolved attribution/boundary readings must be qualified before demanding evaluation views; no new eligibility policy is introduced here.

Source text is the pinned **Wikisource Talmud Bavli** edition distributed in the Sefaria export, with its **CC-BY-SA** metadata retained in each JOB file; no numeric license version is invented. Original metadata credits segmentation to the Steinsaltz Koren Gemara, courtesy of Koren Publishers. Source quotations, editorial paraphrases and inferences retain their distinct origins. Full original corpora remain outside Git. No metered external API calls or model training were used; unavailable token/cost telemetry remains unknown.

Keep this branch and any PR **draft and unmerged**. This checkpoint is useful partial evidence, not a six-tractate release.
