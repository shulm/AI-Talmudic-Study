# Schema Reference and Deterministic ID Specification (`v1.0.0`)

All JSONL layers validate against [`schemas/schema_v1.json`](schemas/schema_v1.json) (JSON Schema Draft 2020-12) plus semantic cross-layer checks in `src/bavli_corpus/validators.py`.

## 1. Deterministic Identifier Grammar and Lineage Redirects

Every identifier is derived deterministically from pinned source coordinates (`tractate_slug`, `daf`, `segment_num`), never from unstable free-form model sequence counters:

| Layer | File | Primary Key Pattern | Example |
|---|---|---|---|
| Source segments | `segments.jsonl` | `seg:bavli:<tractate>:<daf>:<seg>` | `seg:bavli:berakhot:2a:1` |
| Top-level sugya | `sugyot.jsonl` | `sugya:bavli:<tractate>:<start_daf>:<start_seg>__<end_daf>:<end_seg>` | `sugya:bavli:berakhot:2a:2__2b:10` |
| Nested sub-sugya | `sugyot.jsonl` | `subsugya:bavli:<tractate>:<start_daf>:<start_seg>__<end_daf>:<end_seg>:<tag>` | `subsugya:bavli:bava_metzia:21b:2__22b:6:yeush_shelo_midaat` |
| Scholar / collective | `scholars.jsonl` | `(scholar\|entity):<era_or_kind>:<slug>` | `scholar:amora:rava`, `scholar:amora:rabbah` |
| Statement / claim | `statements.jsonl` | `stmt:bavli:<tractate>:<daf>:<seg>:s<NN>` | `stmt:bavli:bava_metzia:21b:3:s01` |
| Atomic question | `questions.jsonl` | `q:bavli:<tractate>:<daf>:<seg>:q<NN>` | `q:bavli:bava_metzia:21b:2:q01` |
| Attributed position | `positions.jsonl` | `pos:bavli:<tractate>:<daf>:<seg>:p<NN>` | `pos:bavli:bava_metzia:21b:2:p01` |
| Argument relation | `relations.jsonl` | `rel:bavli:<tractate>:<daf>:<seg>:r<NN>` | `rel:bavli:bava_metzia:21b:4:r01` |
| Review queue item | `review_queue.jsonl` | `rev:bavli:<tractate>:<daf>:<seg>:v<NN>` | `rev:bavli:berakhot:3b:18:v01` |
| Parallel family | `parallel_family_links.jsonl` | `pfam:<slug_or_hash>` | `pfam:yeush_shelo_midaat_abaye_rava` |

### Lineage Stability After Boundary Corrections

When a subsequent review merges or splits a sugya boundary:
- The new `sugya_id` reflects the updated `<start_ref>__<end_ref>` coordinates.
- `lineage_id` preserves the founding anchor hash (`lin:<sha256[:12]>`), and `redirects_from` records all retired `sugya_id` strings so historical citations never dangle.

## 2. Anchor and Substring Grounding Contract

Every `source_spans` entry is an `anchor` object:

```json
{
  "segment_id": "seg:bavli:berakhot:2a:1",
  "start_char": 0,
  "end_char": 62,
  "quote": "מאימתי קורין את שמע בערבין משעה שהכהנים נכנסים לאכול בתרומתן",
  "quote_sha256": "a1b2...",
  "alignment_status": "exact"
}
```

**Semantic invariants enforced by `validators.py`:**
1. `segment_id` must exist in the tractate's frozen `segments.jsonl`.
2. When `alignment_status == "exact"`, `0 <= start_char < end_char <= segment.canonical_char_len`, `sha256(quote) == quote_sha256`, and (whenever the local source export/cache is available) `segment.canonical_text[start_char:end_char] == quote` character-for-character.
3. If exact substring alignment fails, `start_char` and `end_char` MUST be set to `null`, `alignment_status` MUST be `"unaligned_needs_review"`, and an open `review_queue.jsonl` record targeting the parent entity MUST exist. Pseudo-precise offsets are rejected as hard validation errors.

## 3. Enforced Cross-Layer Invariants

- **Partition completeness:** Every segment in the declared coverage scope (`full_tractate` or explicit `pilot_segment_range`) appears in `ordered_segment_ids` of **exactly one** top-level (`level == "top"`) sugya, in strictly contiguous tractate order (`ordinal_in_tractate` increments by 1 without gaps or duplicates).
- **Sub-sugya containment:** Every `level == "sub"` sugya references an existing `parent_sugya_id`, and its `ordered_segment_ids` is a contiguous subset of the parent's segments.
- **Anonymous Stam protection:** Statements with `speaker_kind == "anonymous_stam"` must have `speaker_id == null` and `attributed_to_ids == []`. `scholars.jsonl` must not contain a pseudo-scholar entry for anonymous Stam.
- **Role separation:** `reported_by_id` (transmitter) and `attributed_to_ids` (authority holding the view) are distinct fields; `scholars.jsonl` checks `distinct_from_ids` (e.g., `scholar:amora:rabbah` vs `scholar:amora:rava`).
- **`חד אמר` safeguard:** Statements with `attribution_type == "unresolved_chad_amar"` cannot populate `attributed_to_ids` with guessed named scholars and must have a corresponding `review_queue.jsonl` item.
- **Question–Position integrity:** Every `position` links to an existing `question_id` and `>= 1` `statement_ids`; if `alternative_id` is set, it must belong to `question.candidate_alternatives`; no two positions on the same question assign contradictory default/silence views to unmentioned scholars.
- **Append-only review history:** `review_queue.jsonl` requires `history` (`minItems: 1`) and prohibits `human_reviewed` / `human_independent_double` unless human reviewer attribution is explicitly present.

## 4. Schema Evolution Policy

Any future breaking or structural modification requires incrementing `schema_version` (`1.1.0` / `2.0.0`), adding a new schema file under `schemas/`, and providing a deterministic migration script with unit tests. `schema_v1.json` (`1.0.0`) remains frozen for v1 artifacts.
