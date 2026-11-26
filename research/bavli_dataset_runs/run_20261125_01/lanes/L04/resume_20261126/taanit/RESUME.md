# Taanit resumable producer checkpoint — 2026-11-26

Partial: **203/895 source segments per all eight required layers**, through Taanit 8b:4. Next **Taanit 8b:5**; **692 remain per layer**. Do not mark tractate delivered.

Authoritative snapshot: `9936408e656e02d42c8df7d80f8803e7f37cc0565ec53449e03056cad69ab017`. Exact external job, export and manifest hashes are in `CHECKPOINT_014.json`. Owner remains `L04/taanit_resume_20261126`, epoch 3. Resume under authorized lane ownership only.

This session added 85 source segments in manually authored batches008–012 after reading pinned originals and rereading for omissions. Sources, common schema/runner and all previous record IDs remain preserved. No paid API calls, commits or pushes. New annotations are AI-provisional and unreviewed; no human certification is claimed.

Replay before continuing:

```powershell
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit
```

Then inspect CURRENT and OWNER and use runner.load to verify exact source bytes. Read from 8b:5 with overlap 8a:18–8b:4 and sufficient continuation. All eight passes remain required. Author scripts in this directory depend on the helper prefix of build_batch008.py and are checkpoint-bound single-use authoring records; **replay immutable accepted proposal bytes, do not rerun them against new CURRENT**. Accepted proposal data and complete exports stay external.

Correction013 adjudicates all ten findings in the frozen comparison (`f78d0ef730548b3bf0c9f2453c5a980041a772dcf8a76b8789a9fe8e9f49ee4d`). It preserves status-polarity corrections, printed כותיים, rainy-season conditions, unresolved inherited/anonymous attribution differences, canonical lexical terms, two additional scoped edges, and the exact 4a:1 boundary before ואמר רבא. See `REVIEW_CORRECTION_013.json`; 43 versions were superseded with full graph and coverage closure, no coverage inflation. No prior correction was undone.

The immutable correction review target is `1bccca4286a5288948141c490c2a66d0b3f3f32738236b66e70e2ac65145e82f`. Subsequent batch012 only appends records. Parent was asked for independent recheck; consult its receipt before claiming closure. All active links and content fields, including attribution scope strings containing IDs before punctuation, were checked for stale correction targets. Historical supersedes references intentionally remain.

Latest export includes typed tables, coverage, per-sugya views, unresolved cases, qualification and manifest. Replay and export file hashes passed. There are no open structural tails at this endpoint. Frozen source/semantic review cohorts remain separate from production coverage; the producer does not count its own reread as independent review. Previous CHECKPOINT_007 and CHECKPOINT_005 remain historical receipts.
