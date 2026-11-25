# QA and Continuation Checkpoint Report (`v1.1.0`)

**Mechanical validation passes on cumulative data (`267` processed segments). The historical full-semantics/ML gate from PR #10 remains `false`; this checkpoint advances provisional sugya segmentation only (`ml_eligible=false`).**

## 1. Cumulative Coverage Before vs. After `berakhot_block_002_5b_6a`

| Metric | Baseline PR #10 (`ef29310`) | After Block `Berakhot 5b–6a` | Notes |
|---|---:|---:|---|
| Berakhot processed segments | `151` (`2a–5a`) | **`203`** (`2a–6a`) | `+52` core (`27` promoted from `5b` context with identical IDs/hashes + `25` on `6a`) |
| Bava Metzia processed segments | `64` (`21a–22b`) | `64` (`21a–22b`) | `100%` byte-for-byte unchanged |
| Total processed segments (`data/segments.jsonl`) | `215` | **`267`** | First `215` rows byte-identical |
| Context-only segments (`context/segments.jsonl`) | `68` | **`78`** | `27` `5b` promoted out; `37` `6b` added; `41` BM context untouched |
| Primary sugyot / Sub-sugyot | `29` / `6` | **`37`** (`32` BRK, `5` BM) / **`7`** | `B24` extended (`5a:24–5b:3`); `B25..B32` + `B31a` added |
| Textual scholar labels (`data/scholars.jsonl`) | `59` | **`71`** | First `59` rows byte-identical; `+12` new labels on `5b–6a` |
| Statements / Questions / Positions / Relations | `231` / `52` / `94` / `43` | **`250`** / `52` / `94` / **`44`** | Exhaustive Q–A/positions deferred (`29` core segs flagged `semantic_extraction_pending`) |
| Open review records (`data/review_queue.jsonl`) | `39` | **`80`** | Includes `6a:7\|6a:8` boundary disagreement, `5b:14` homonym, and `B32` open tail |
| Exact evidence spans verified | `688` | **`791`** | `0` substring, offset, or SHA-256 errors across all 37 pinned source files |

## 2. Continuation Safety Invariants Verified (`test_continuation.py`)

1. **Preservation of accepted work:** All `215` baseline segment rows, all `34` unaffected sugyot (`B01..B23`, `M01..M05`, `M04a..M04f`), all `59` baseline scholars, `231` baseline statements, `52` questions, `94` positions, `43` relations, and `38` unaffected review records were verified byte-for-byte identical after block application.
2. **Idempotent block replay:** Re-applying `berakhot_block_002_5b_6a` returns `already_applied_idempotent` with zero duplicate rows or byte changes.
3. **Source & conflict rejection:** Mutated `source_sha256` raises `SourceIntegrityError`; a modified proposal under an existing `block_id` or overlapping core range raises `ConflictingBlockError`.
4. **Crash / interrupted-write safety:** Simulated `IOError` mid-promotion automatically rolls back all touched files from write-ahead backup, leaving the previous checkpoint byte-identical and passing `validate.py`.
5. **Cross-block open-tail lineage & full-span reading:** `B24` retained ID `sug_9a1c712c3a26fe45003b`, closed from `open_right` to `provisional` across `5a:24–5b:3`, and archived its prior JSON record (`previous_record_sha256: 03c92488...`) in `revisions_ledger.jsonl`. Multi-page inherited open tails automatically expand `prepare_block_input` before default preceding context using bounded `<=10`-segment / `<=8,000`-char sequential reading packets.
6. **Whole-span review status enforcement:** Validator rejects `independent_source_reviewed` if any segment of an extended sugya (such as `5a:24` in `B24`) was omitted from the independent review span.

## 3. Separate Source-Only Review of `Berakhot 5b–6a`

A context-isolated reader (`blocks/berakhot_5b_6a/independent_review_initial.json`, `SHA-256: 1249a6d49e1bcb4dd82a88a0bcf13be4cdc5b56c3376a827b91d654c658e480f`) read only `input_packet.json` and `berakhot_5a_6b_reading.txt` before `proposal.json` existed in the workspace:

- Agreed on **`51 / 52` (`98.08%`)** inter-segment boundary slots, including closing `B24` at `5b:3`, crossing `5b:27 -> 6a:1` (`B29`), and leaving `B32` (`6a:17–6a:25`) `open_right` into `6b:1` (`וכולהו כתיבי באדרעיה:`).
- Differed at **`6a:7 | 6a:8`** (splitting the fourth Abba Binyamin baraita `6a:7` from `6a:8–16` vs. grouping `6a:7–16` with sub-sugya `B31a`). Both frozen files are retained untouched, and `B31` carries `independent_source_reviewed_with_disagreement` plus an open `boundary_disagreement_preserved` review item.
