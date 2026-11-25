# Actual production runner

Requires Python 3.11+ and `jsonschema` (tested 4.26.0). No metered API calls. This runner validates structured interactive-agent proposals; it does not manufacture semantic annotations. All 37 pinned tractates can be loaded in full. Core-layer completion and independent review remain separately measured.

Run from repository root, choosing an external job directory:

```powershell
python research/bavli_production_v1/runner.py init --source-root F:/Sefaria-Export-master --manifest research/bavli_sugya_corpus_v1/source_manifest.json --tractate Berakhot --job-dir F:/Sefaria_QA/production/Berakhot --owner L01-worker --epoch 1
python research/bavli_production_v1/runner.py packet --job-dir F:/Sefaria_QA/production/Berakhot --start-ref 'Berakhot 9a:29' --end-ref 'Berakhot 9b:10' --output F:/Sefaria_QA/production/reading-packet.json
python research/bavli_production_v1/runner.py migrate --job-dir F:/Sefaria_QA/production/Berakhot --owner L01-worker --epoch 1 --legacy-dir F:/Sefaria_QA/worktrees/bavli-sugya-continuation-pr10/research/bavli_sugya_corpus_v1
python research/bavli_production_v1/runner.py submit --job-dir F:/Sefaria_QA/production/Berakhot --proposal F:/Sefaria_QA/production/proposal.json --owner L01-worker --epoch 1
python research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/production/Berakhot
python -m unittest discover -s research/bavli_production_v1 -p test_runner.py -v
```

Schema and protocol SHA-256 values are returned by init and stored in JOB.json; producers bind both in each proposal. `packet` returns raw text with stable legacy source IDs. Read wider original context as needed. `open_tails` is the complete current list at that checkpoint, not an incremental list. New revisions must update affected coverage; stale coverage cannot promote. Coverage can be arbitrary non-prefix blocks, and missing earlier/later scopes remain missing. The report counts complete original source inventory separately from each semantic layer. Only recorded proposals establish execution.

Checkpoint contents: authoritative typed records, coverage matrix, immutable proposal chain, open tails, unreviewed state and ineligible task state. CURRENT.json points at an immutable content-addressed snapshot; snapshots and proposals are replay inputs. Resume by replay, inspect next_unprocessed_by_layer, read source, then submit the next proposal. `handoff --owner OLD --epoch N --new-owner NEW` increments only this job's epoch. Only the authorized coordinator or lane lead may call handoff; this CLI does not authenticate organizational authority. Do not initialize duplicate tractate jobs as concurrent producers.

`migrate` archives legacy JSONL bytes and a deterministic mapping manifest. It preserves all original IDs and first judgments but explicitly leaves legacy semantics unmapped until source-based production annotations exist. Compatibility export is byte-for-byte recovery of each `legacy/<sha256>.jsonl` to its manifest `path`; losses are recorded in the migration manifest. A later migration is a separate immutable manifest, never replacement. The legacy producer checkout is read-only.

This minimum runner does not automatically issue a tractate-delivered or independently-reviewed badge. It deliberately reports both false until separate independent review and final integration gates are implemented/recorded. No research training/evaluation view is qualified. No paid model route is implied. Existing v2 source-coordinate review planner remains the review sampler.

Generated views: `export --job-dir JOB --output NEW_DIRECTORY` writes typed core tables, coverage, qualification, unresolved cases, per-sugya segment-overlap context exports, and a hash manifest. Output is immutable; select a new directory after revisions. `compatibility-export --job-dir JOB --migration-sha256 HASH --output NEW_DIRECTORY` verifies and restores exact original JSONL bytes plus the migration loss report. Neither command grants review or eligibility.
