# QA Report — Tractate Bava Metzia (Pilot Calibration Slice `21a:1–22b:16`)

- **Tractate:** `Bava Metzia` (`בבא מציעא`, TOC #21, *Seder Nezikin*)
- **Pinned Edition:** `William Davidson Edition - Aramaic.json` (`CC-BY-NC`)
- **Source File SHA-256:** `b1f3c0ad3cb8cf88f0ec43256faaa0b5dcb8fe27d23fb805f6c5a38892a9f631`
- **Full Tractate Ref Range & Inventory Hash:** `Bava Metzia 2a:1` – `Bava Metzia 119a:6` (`3,660` source segments; `segment_inventory_sha256 = d23bb0755f4f23c2ab34bff432ddfdcfabf29e8b12e76c91bdd1e3d99368443b`)
- **Annotated Pilot Slice:** `Bava Metzia 21a:1` – `Bava Metzia 22b:16` (`64 / 3,660` source segments = `1.75%`; `3,596` segments remain unannotated)
- **Whole-Tractate Status:** `PILOT_SLICE_PROVISIONAL_COMPLETE` (**NOT** `PROVISIONAL_TRACTATE_COMPLETE` for whole *Bava Metzia*; sampled specifically as complex multi-amora civil-law calibration slice)
- **Review Qualification:** `ai_independent_double` (**provisional AI double review — zero human expert certification claimed**)

## 1. Layer Counts and Coverage Denominators (`21a:1–22b:16`)

| Metric | Count / Rate | Notes |
|---|---:|---|
| Input segments in pilot slice | `64` | `100%` accounted for (`0` omissions, `0` duplicates, `0` gaps) |
| Unresolved segment assignments | `0` | Both slice edges (`21a:1–6` from `20b:18`; `22b:11–16` onto `23a:1–15`) explicitly flagged `window_edge_pending` |
| Top-level sugyot (`level="top"`) | `5` | Includes 40-segment multi-daf `יאוש שלא מדעת` sugya (`21a:19–22b:10`) |
| Nested sub-sugyot (`level="sub"`) | `3` | `גופא` (`21a:4–5`), Mari bar Isak `מעשה` (`22a:10–11`), `תמרי דזיקא` corollary (`22b:8–10`) |
| Uncertain / edge-pending top boundaries | `2 / 5` (`40.00%`) | Both are exact slice-edge continuations (`21a:1–6` and `22b:11–16`) |
| Statements (`statements.jsonl`) | `25` | `100%` exact substring & reversible raw-HTML alignment |
| Named authority statements | `18 / 25` (`72.00%`) | Includes strict separation of `רבה` (Rabbah) vs `רבא` (Rava) at `22b:11–14` |
| Anonymous Stam statements | `6 / 25` (`24.00%`) | Validator caught and prevented assigning Rava to Stam's `אמר לך רבא` (`22b:14:s01`) |
| Atomic questions (`questions.jsonl`) | `5` | `4` `ml_prediction_eligible = true`; `1` excluded due to explicit `תיקו` (`21a:18`) |
| Attributed positions (`positions.jsonl`) | `9` | Rava's `יאוש שלא מדעת` marked `rejected` (`תיובתא דרבא תיובתא`); Stam `הלכתא` marked `halakhic_ruling`; Rava's `סימן העשוי לידרס` kept `asserted` (deflected `תיובתא`) |
| Argument relations (`relations.jsonl`) | `6` | Explicit `qualifies`, `distinguishes`, `contradicts`, `supports`, `objects_to`, `answers` |
| Review queue items (`review_queue.jsonl`) | `4` (`4` open) | Append-only audit trail across Pass 1–3 and blind second reading |

## 2. Independent Blind Second Reading (`ai_independent_double`)

- **Inter-segment boundary slot agreement:** `62 / 63` (`98.41%`).
- **Primary internal cuts matched by blind reader:** `4 / 4` (`100.0%` precision; including catching the single-word `איתמר` at the bottom of `21a:19` as the start of `21b:1`).
- **Granularity difference (`1` cut):** Blind reader elevated `22b:8–10` (`תמרי דזיקא` post-tiyuvta dialogue) to a separate top-level sugya (`ambiguous`) whereas Pass 1 modeled it as nested sub-sugya `bm_sub_22b8_10` inside `21a:19–22b:10`; logged in `rev:bavli:bava_metzia:22b:8:v01`.
- **Attribution & rabbinic safeguard agreement:** `100%` agreement on `רבה` vs `רבא` (`22b:11–14`), `אביי` (`asserted`) vs `רבא` (`rejected` at `22b:6`), `רבא אליבא דאביי` (`conditional` at `22a:7`), `רבא` via `מר זוטרא` (`asserted` at `22a:11`), deflected `תיובתא דרבא` at `22b:13–14`, `רבי ירמיה`'s `תיקו` (`21a:14–18`), and both slice-edge continuations (`20b -> 21a:1` and `22b:16 -> 23a:1`).

## 3. Cost & Validation

- **External paid API calls / spend:** `0` calls / `$0.00 USD`.
- **Validation command:** `python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli validate` -> `PASS`.
