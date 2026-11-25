# Continuation Checkpoint Handoff — `berakhot_block_002_5b_6a`

## 1. Exact Checkpoint State

- **Base reviewed commit (PR #10):** `ef29310b50575ac2441ce59d0c68d58424f4b823`
- **Pinned edition & Berakhot source hash:** `Wikisource Talmud Bavli` (`CC-BY-SA`), `source_sha256 = dd24d48aef18159564471380f7ba200302cc9889b22380aef724d2fb086a9d38` (`source_toc_sha256 = 8023a50ed76d9d3da1a63feb7dda87fc116ca6ab184eab3cb62fb7d6bd3adcfe`).
- **Accepted block:** `berakhot_block_002_5b_6a` (`Berakhot 5b:1–6a:25`, `52` core segments; `27` promoted from `5b` context preserving exact `seg_*` IDs and hashes).
- **Berakhot coverage before -> after:** `151 / 2,749` (`2a:1–5a:24`) -> **`203 / 2,749`** (`2a:1–6a:25`); total corpus processed segments `215` -> **`267`** (`0 / 37` masechtot complete).
- **Revised IDs (with prior versions archived in `revisions_ledger.jsonl`):**
  - `sug_9a1c712c3a26fe45003b` (`B24`: extended `5a:24` -> `5a:24–5b:3`, closed `open_right` -> `provisional`)
  - `rev_77544b1ee3d5d919e5fa` (`B24` boundary review updated to span `5a:24–5b:3`)
- **New primary sugya IDs (`Berakhot 5b:4–6a:25`):**
  - `B25` (`sug_8aaf502a219414d94655`): `Berakhot 5b:4–5b:9` (`provisional`)
  - `B26` (`sug_3e781bcc10a62912f6fa`): `Berakhot 5b:10–5b:16` (`provisional`)
  - `B27` (`sug_4bddd22de96ee7dad529`): `Berakhot 5b:17–5b:20` (`provisional`)
  - `B28` (`sug_8abdf1580603d91a8e25`): `Berakhot 5b:21–5b:24` (`provisional`)
  - `B29` (`sug_d210ba50f39c0d38f613`): `Berakhot 5b:25–6a:1` (`provisional`)
  - `B30` (`sug_726a2749e243fa32b5db`): `Berakhot 6a:2–6a:6` (`provisional`)
  - `B31` (`sug_5eb00cfd65e6c6c1ae30`): `Berakhot 6a:7–6a:16` (`provisional`, `independent_source_reviewed_with_disagreement`; sub-sugya `B31a` = `sug_2854695331446c60a73d` `6a:8–6a:16`)
  - `B32` (`sug_bc413c5b52ef04c8a017`): `Berakhot 6a:17–6a:25` (**`open_right`**)
- **Last closed ref in Berakhot:** **`Berakhot 6a:16`**
- **Next unprocessed ref in Berakhot:** **`Berakhot 6b:1`**
- **Active open tails across corpus:**
  1. `Berakhot`: `B32` / `sug_bc413c5b52ef04c8a017` (`6a:17–6a:25`, `open_right`, concludes with `"וכולהו כתיבי באדרעיה:"` at `Berakhot 6b:1`).
  2. `Bava Metzia`: `M01` / `sug_d968fce424f6218db2d2` (`21a:1–21a:5`, `open_left` from `20b:18`) and `M05` / `sug_c0f6c7e3ae9d902ee487` (`22b:11–22b:16`, `open_right` into `23a:1`).

## 2. Next Block Instructions (`Berakhot 6b–7a`)

1. Run `python -X utf8 continue_corpus.py prepare --block-id berakhot_block_003_6b_7a --tractate Berakhot --core-start 6b --core-end 7a --context-before 1 --context-after 1 --out blocks/berakhot_6b_7a/input_packet.json`.
   - This automatically includes the full inherited open-tail span of `B32` (`6a:17–6a:25`), promotes the `37` existing `6b` `context_only` segments with their unchanged `seg_*` IDs, and pulls `7b` as following context.
2. Extend `B32` (`sug_bc413c5b52ef04c8a017`) to include `Berakhot 6b:1` (`וכולהו כתיבי באדרעיה:`), then partition `6b:2–7a:...` from source evidence, freeze an independent source-only review before comparison, run `continue_corpus.py apply`, regenerate `continue_corpus.py export`, and run all validation/Manifest checks before advancing.
3. Keep PR #11 (`research/bavli-sugya-corpus-v1`) separate; never mix its Davidson edition records or character offsets into this Wikisource corpus. Do not claim any masechet complete or `ml_eligible=true`.
