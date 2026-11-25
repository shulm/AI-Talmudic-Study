# Execution and Limits Ledger

## Entry 1 — 2026-11-24: Bounded Provisional Pilot (`ef29310b50575ac2441ce59d0c68d58424f4b823`, PR #10)

- Branch `codex/bavli-sugya-corpus-v1` (based on `165bd826f02c91894dc9806d5e49af119eb230a5`).
- Built 37-tractate Wikisource inventory (`81,793` segments) and extracted `215` pilot segments (`Berakhot 2a–5a`, `Bava Metzia 21a–22b`) plus `68` context segments (`29` primary sugyot, `6` sub-sugyot, `231` statement units, `52` questions, `94` positions, `59` textual scholar labels, `43` relations, `39` open review records).
- Historical semantic/ML expansion gate did **not** pass (`semantic_completeness_pass=false`, `expansion_gate_pass=false`); `0` paid API calls, `$0` spend.

## Entry 2 — 2026-11-25: Continuation Infrastructure `v1.1.0` + Block `berakhot_block_002_5b_6a`

- Isolated branch `research/bavli-sugya-continuation-pr10` branched directly from `ef29310b50575ac2441ce59d0c68d58424f4b823`. PR #11 (`research/bavli-sugya-corpus-v1`, Davidson edition) was left untouched and never merged or copied.
- Implemented configurable block input preparation (including automatic multi-page backward extension and sequential reading packets for long inherited open tails), `schema_v1_1.json`, `block_ledger.json`, append-only `revisions_ledger.jsonl`, isolated staging compilation, and atomic backup/rollback promotion (`continuation.py`, `continue_corpus.py`).
- Prepared `blocks/berakhot_5b_6a/input_packet.json` (`Berakhot 5b–6a` = `52` core segments, `27` promoted from `5b` context with unchanged IDs/hashes; `5a` preceding context; `6b` = `37` following context segments).
- Executed a context-isolated source-only second reading (`Gemini 4 Carbon` `research` subagent) frozen at `blocks/berakhot_5b_6a/independent_review_initial.json` (`SHA-256: 1249a6d49e1bcb4dd82a88a0bcf13be4cdc5b56c3376a827b91d654c658e480f`) before writing `proposal.json` into the workspace (`51 / 52` inter-segment boundary slot agreement; `6a:7 | 6a:8` disagreement preserved).
- Extended `B24` (`sug_9a1c712c3a26fe45003b`) across `5a:24–5b:3` (`provisional`), added `B25..B32` (+ sub-sugya `B31a`), leaving `B32` (`6a:17–6a:25`) `open_right` into `Berakhot 6b:1` (`וכולהו כתיבי באדרעיה:`).
- Built cumulative Berakhot per-sugya export (`exports/berakhot_sugyot_cumulative.jsonl`), compact index (`exports/berakhot_index.json`), and offline Hebrew RTL reader (`exports/berakhot_sugya_reader.html`).
- Model & cost accounting: workspace agent (`Gemini 4 Carbon`) + isolated read-only subagent on the same workspace session; external paid API calls = `0`; incremental paid API spend = `$0.00`; model training = none.
