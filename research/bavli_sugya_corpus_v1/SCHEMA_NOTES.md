# Schema and Operational Migration Notes (`1.0.0` -> `1.1.0`)

## 1. Backward-Compatible Operational Contract (`schema_v1_1.json`)

`schema_v1.json` (`1.0.0`) is retained byte-for-byte intact so the original bounded pilot (`ef29310`) remains documented as frozen. `make_schema_v1_1.py` generates `schema_v1_1.json` (`urn:ai-talmudic-study:bavli-sugya:1.1.0`) for cumulative pilot + block-continuation validation:

- **Unaffected `1.0.0` records stay untouched:** All `215` pilot segments (`scope="pilot"`), `34` unaffected sugyot (`B01..B23`, `M01..M05`, `M04a..M04f`), `59` scholars, `231` statements, `52` questions, `94` positions, `43` relations, and `38` unaffected review items keep their exact `1.0.0` bytes.
- **Core continuation segments (`1.1.0`):** Carry `scope="core"`, `block_id`, and `promoted_from_context` (`true` when promoted from prior `context/segments.jsonl`, retaining identical `seg_*` IDs and hashes).
- **Minimal useful sugya layer (`sugyot` `1.1.0`):** Every new or extended sugya records:
  - Stable `id` (`sug_*`, preserved across open-tail extension) and exact contiguous `segment_ids` / `start_ref` / `end_ref`;
  - `title_he` and `summary_he` (`summary_origin="editorial_paraphrase"`);
  - `boundary_status`, `boundary_rationale`, `evidence`, and structured `pending_continuation` (`is_open`, `direction`, `next_unprocessed_ref`, `context_preview_refs`, `note_he`);
  - `name_mentions` with exact raw-segment substring `evidence`, `scholar_id`, `transmitter_ids`, `candidate_ids` (never assigned by name order in `חד אמר`, `ואמרי לה`, or `ואיתימא`), `role`, and `attribution_status`;
  - Three explicit separate statuses: `construction_status`, `extraction_status`, and `span_review_status` (verified mechanically against the full segment span covered by `independent_review_initial.json`);
  - `uncertainty_notes_he`, `review_item_ids`, and `lineage` (`origin_block_id`, `updated_in_block_id`, `previous_record_sha256`, `supersedes_ids`).
- **Fail-closed ML gate:** `ml_eligible` remains `const: false` and `review_status` remains `const: "ai_provisional"` across all records.

## 2. Ledger and Append-Only Revision History

- `block_ledger.json` records each accepted block's input packet SHA-256, proposal SHA-256, independent review SHA-256, added/promoted segment counts, revised IDs, new sugya IDs, `last_closed_ref`, `next_unprocessed_ref`, and active open tails.
- `revisions_ledger.jsonl` stores the complete pre-revision JSON record and SHA-256 for every intentional cross-block update (such as extending `B24` from `5a:24` to `5a:24–5b:3`). Any mutation of a previously accepted record not accompanied by a matching `revisions_ledger.jsonl` entry fails staging validation.
