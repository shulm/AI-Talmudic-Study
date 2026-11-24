# QA Report — Tractate Berakhot (Pilot Calibration Slice `2a:1–5a:24`)

- **Tractate:** `Berakhot` (`ברכות`, TOC #1, *Seder Zeraim*)
- **Pinned Edition:** `William Davidson Edition - Aramaic.json` (`CC-BY-NC`)
- **Source File SHA-256:** `034c03e8259d3b4ce21a900b6baacde4398464d153b60bc3b880c5224ac69771`
- **Full Tractate Ref Range & Inventory Hash:** `Berakhot 2a:1` – `Berakhot 64a:15` (`2,749` source segments; `segment_inventory_sha256 = 7f3a0db56d2e3ef9b299c193d18db8781d4d640630798f3d62ac90784ce5d190`)
- **Annotated Pilot Slice:** `Berakhot 2a:1` – `Berakhot 5a:24` (`151 / 2,749` source segments = `5.49%`; `2,598` segments remain unannotated)
- **Whole-Tractate Status:** `PILOT_SLICE_PROVISIONAL_COMPLETE` (**NOT** `PROVISIONAL_TRACTATE_COMPLETE` for whole *Berakhot*; awaiting owner budget sign-off to scale across `5b:1–64a:15`)
- **Review Qualification:** `ai_independent_double` (**provisional AI double review — zero human expert certification claimed**)

## 1. Layer Counts and Coverage Denominators (`2a:1–5a:24`)

| Metric | Count / Rate | Notes |
|---|---:|---|
| Input segments in pilot slice | `151` | `100%` accounted for (`0` omissions, `0` duplicates, `0` gaps) |
| Unresolved segment assignments | `0` | `5a:24` (`1` segment) marked `window_edge_pending` continuing onto `5b:1–3` |
| Top-level sugyot (`level="top"`) | `19` | `6` cross-amud sugyot; `3` cross-daf sugyot |
| Nested sub-sugyot (`level="sub"`) | `3` | `2b:17–3a:3`, `3b:29–4a:3`, `4a:14–4a:18` |
| Uncertain / edge-pending top boundaries | `3 / 19` (`15.79%`) | `3b:20–4a:7`, `4b:27–5a:5`, `5a:24` (pilot slice edge) |
| Statements (`statements.jsonl`) | `52` | `100%` exact substring & reversible raw-HTML alignment (`0` unaligned) |
| Named/collective authority statements | `35 / 52` (`67.31%`) | Transmitters separated from holders (`3a:11`, `3b:14`, `3b:17`, `4b:16`, `5a:11`, `5a:16`) |
| Anonymous Stam statements | `10 / 52` (`19.23%`) | Zero false named-scholar assignments |
| Ambiguous / variant / `חד אמר` statements | `8 / 52` (`15.38%`) | Unresolved `חד אמר` (`4a:8–9`, `5a:14–15`), `איכא דאמרי` (`3b:18–19`), `ואמרי לה` (`2b:13`), `ואיתימא` (`5a:9`) |
| Atomic questions (`questions.jsonl`) | `6` | `4` `ml_prediction_eligible = true`; `2` excluded due to unresolved `חד אמר` |
| Attributed positions (`positions.jsonl`) | `15` | `0` silence-imputed views |
| Argument relations (`relations.jsonl`) | `9` | All grounded in explicit spans |
| Review queue items (`review_queue.jsonl`) | `9` (`9` open) | Append-only history preserving Pass 1–3 and blind second reading |

## 2. Independent Blind Second Reading (`ai_independent_double`)

Frozen blind second pass (`model_outputs/independent_second_pass/blind_second_reading_v1.json`, SHA-256 `3bac6d28d1a0c9cc815a73d9998af177f4256c42f4dc524f521c18758bd6156d`):

- **Inter-segment boundary slot agreement:** `147 / 150` (`98.00%`).
- **Primary internal cuts matched by blind reader:** `18 / 18` (`100.0%` precision; `17 / 19` exact top-level span matches).
- **Granularity differences (`3` extra cuts in blind pass):** Blind reader split `4b:27–5a:5` into `4b:27–5a:1`, `5a:2–5a:3`, and `5a:4–5a:5`, and split `5a:6–5a:19` at `5a:9` (`5a:6–8` vs `5a:9–19`). Both passes independently flagged these exact regions as `ambiguous` with matching alternative notes; logged in `rev:bavli:berakhot:4b:27:v01` and `rev:bavli:berakhot:5a:6:v01`.
- **Attribution & rabbinic hazard agreement:** `100%` agreement on both unresolved `חד אמר` pairs (`4a:8–9`, `5a:14–15`), opposite `איכא דאמרי` versions (`3b:18–19`), cross-daf sentence break (`4b:28 -> 5a:1`), slice-end continuation (`5a:24 -> 5b:1`), and multi-link transmission chains.
- **Preserved semantic disagreement (`1` item):** At `Berakhot 5a:16–17`, Pass 3 modeled R. Yohanan's `אלו ואלו יסורין של אהבה הן` as inclusive harmonization (`reconciled_compatible`), whereas the blind second reader noted the Rashi reading that R. Yohanan *rejects* restricting `יסורין של אהבה` even when Torah or prayer is interrupted (explaining why `5a:17` re-expounds `ומתורתך תלמדנו`). Logged in `rev:bavli:berakhot:5a:14:v01` for human expert adjudication.

## 3. Cost & Validation

- **External paid API calls / spend:** `0` calls / `$0.00 USD`.
- **Validation command:** `python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli validate` -> `PASS`.
