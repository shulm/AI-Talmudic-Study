# Bavli sugya corpus v1.1 — provisional masechet-by-masechet continuation (from PR #10)

This directory continues PR #10 (`ef29310b50575ac2441ce59d0c68d58424f4b823`) on its pinned **Wikisource Talmud Bavli** edition (`CC-BY-SA`, 37 tractates, 81,793 source segments) and existing stable IDs. PR #11 (which used a different edition and incompatible offsets) is preserved separately on its own branch and was never concatenated or copied here.

## Current Scope and Gate Truthfulness

- **Active phase:** Provisional sequential sugya segmentation (`v1.1.0`), one bounded block at a time, preserving the richer PR #10 pilot annotations (`Berakhot 2a–5a` and `Bava Metzia 21a–22b`) byte-for-byte while deferring exhaustive Q–A and comparable-position extraction to a separate phase.
- **Historical gate preserved:** PR #10's full semantic/ML readiness gate (`semantic_completeness_pass=false`, `expansion_gate_pass=false`) did **not** pass and is preserved unchanged. Every semantic record remains `ai_provisional` and `ml_eligible=false`. No masechet is complete and no model was trained.
- **Completed continuation checkpoint (`berakhot_block_002_5b_6a`):**
  - Core added: **Berakhot `5b–6a`** (`52` segments: `27` on `5b` promoted from prior `context_only` with unchanged segment IDs/hashes + `25` newly extracted on `6a`), with `5a` preceding context and `6b` (`37` segments) following context.
  - Cumulative *Berakhot* coverage: **`203 / 2,749` segments** (`2a:1–6a:25`), **`32` primary sugyot** (+ `1` sub-sugya `B31a`), last closed ref **`Berakhot 6a:16`**, active open tail **`B32` (`sug_bc413c5b52ef04c8a017`, `6a:17–6a:25` -> `6b:1`)**, next unprocessed ref **`Berakhot 6b:1`**.
  - Inherited open unit **`B24` (`sug_9a1c712c3a26fe45003b`)** was extended from `Berakhot 5a:24` through `Berakhot 5b:3` and closed (`provisional`), preserving its ID and archiving its prior `1.0.0` snapshot in `revisions_ledger.jsonl`.

## Key Files

- **Continuation architecture:** `make_schema_v1_1.py` (`schema_v1_1.json`), `continuation.py`, `continue_corpus.py`, `block_ledger.json`, `revisions_ledger.jsonl`, `test_continuation.py`.
- **Immutable block artifacts:** `blocks/berakhot_5b_6a/{input_packet.json, proposal_initial.json, proposal.json, independent_review_initial.json, comparison.json, comparison.md}`.
- **Convenient Berakhot exports & reader:** `export_reader.py`, `exports/berakhot_sugyot_cumulative.jsonl`, `exports/berakhot_index.json`, `exports/berakhot_sugya_reader.html`, and `exports/verify_reader.cjs`.
- **Preserved pilot & validation:** `pipeline.py`, `make_schema.py` (`schema_v1.json`), `annotation_initial.py`, `annotation_completion.py`, `revisions.json`, `compile_annotations.py`, `validate.py`, `test_pipeline.py`, `test_reproduction.py`, `verify_manifest.py`, [QA.md](QA.md), [HANDOFF.md](HANDOFF.md), [SCHEMA_NOTES.md](SCHEMA_NOTES.md), [REPRODUCE.md](REPRODUCE.md), and [SOURCE_ATTRIBUTION.md](SOURCE_ATTRIBUTION.md).
