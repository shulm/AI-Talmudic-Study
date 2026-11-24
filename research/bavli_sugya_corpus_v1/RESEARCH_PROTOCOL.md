# Research Protocol — Babylonian Talmud Sugya Corpus v1

## 1. Scientific Scope and Non-Goals

This track constructs a verifiable, source-grounded, multi-layer corpus of **Talmud Bavli** one *masechet* (tractate) at a time. It preserves **all** source text — halakhic, aggadic, narrative, mishnah, baraita, anonymous Stam dialectic, single-scholar statements, agreements, unresolved questions (`תיקו` / `קשיא`), textual variants, and inversions (`איפוך`) — rather than filtering for disputes or forcing passages into binary preference labels.

**Strict separation from downstream modeling:**
- Do **not** alter or reinterpret frozen results in PR #4 (`codex/decision-functions-execution-v1`) or PR #5 (`codex/individual-decision-pilot-20261124`).
- Do **not** train or fit any scholar-simulation or decision-function model in this track.
- Existing pair dispute indexes (`rav_shmuel`, `abaye_rava`, `yochanan_lakish`, `rabbah_yosef`) are used only for cross-reference recall/audit checks, never as a selection filter for corpus inclusion.

## 2. Multi-Pass Windowed Architecture

Even with long-context models, tractate-scale annotation requires deterministic, resumable partitioning:

1. **Pass 0 — Deterministic Segment Inventory (`scanner.py`):**
   - Scans `table_of_contents.json` (`37` Bavli tractates in canonical *Seder* order) and `schemas/<Tractate>.json` chapter mappings.
   - Emits frozen `manifest.json` and `segments.jsonl` (plus gitignored `local_source_cache` full text) with SHA-256 digests and reversible `offset_map`.
2. **Pass 1 — Overlapping Window Sugya Segmentation (`window_manager.py` + `reconciler.py`):**
   - Slices target ranges into bounded windows of **2 amudim central coverage** (`~25–50` segments) with **1 preceding amud and 1 following amud** of read-only context.
   - Commits boundaries only inside the central coverage region; emits `window_edge_pending` continuations when a sugya runs past the window end.
   - Global `reconciler.py` stitches cross-window and cross-daf continuations so sugyot are **never** artificially split at an amud or daf boundary, and verifies that top-level `sugyot.jsonl` forms an exact, gap-free, duplicate-free ordered partition of all frozen target segments.
3. **Pass 2 — Speech-Act and Attribution Decomposition (`statements.jsonl` + `scholars.jsonl`):**
   - Links every claim/utterance to exact `{segment_id, start_char, end_char}` anchors into `canonical_text`.
   - Enforces strict role separation: `speaker_id` (utterer), `reported_by_id` / `transmission_chain_ids` (`אמר פלוני משמיה דאלמוני`), `quoted_source_type` (Mishnah/Baraita/Scripture), and `attributed_to_ids` (holder of the view).
4. **Pass 3 — Atomic Questions, Positions, and Argument Graph (`questions.jsonl`, `positions.jsonl`, `relations.jsonl`, `review_queue.jsonl`):**
   - Extracts neutral Hebrew questions (`neutral_question_he`) and explicit conditions (`prerequisites_conditions_he`) only where supported by the sugya; narrative or non-question sugyot legitimately produce zero questions.
   - Records `positions.jsonl` with explicit `position_status` (`asserted`, `conditional`, `rejected`, `retracted`, `inverted_candidate`, `reconciled_compatible`, `halakhic_ruling`, `anonymous`, `variant`, `unresolved`).
   - Records directed `relations.jsonl` edges (`supports`, `objects_to`, `answers`, `derives_from`, `qualifies`, `contradicts`, `retracts`, `reconciles`, `distinguishes`, `quotes`, `same_topic_as`, `alternative_version_of`) grounded in explicit source spans.

## 3. Rabbinic Attribution and Reasoning Safeguards

1. **`חד אמר ... וחד אמר`:** Never assign named scholars by mention order. Unless an explicit continuation (`תסתיים דרב פלוני הוא דאמר...`) resolves the pairing — and even then recording whether the resolution is itself challenged — leave `holder_kind = "unresolved_chad_amar"`, `attributed_to_ids = []`, and log an open item in `review_queue.jsonl`.
2. **Dialectical reversals and qualifications (`איפוך`, `איכא דאפיך`, `תיובתא`, `קשיא`, `לא פליגי`, `לא צריכא`, `הדר ביה`):** Read the full continuation before labeling `interpretation_status` and `position_status`. Refuted (`תיובתא`) or retracted (`הדר ביה`) statements remain historical statements with `position_status = "rejected"` or `"retracted"`, never accepted final views. `לא פליגי` / `כאן ב... כאן ב...` reconciliations mark positions `reconciled_compatible` / `conditional` with explicit `conditions_he`.
3. **Transmission chains (`אמר רב יהודה אמר רב`, `אמר רבה בר בר חנה אמר רבי יוחנן`, `משמיה ד...`):** Separate transmitter (`reported_by_id`) from original authority (`attributed_to_ids`).
4. **Anonymous Stam:** Redactional questions, objections (`מתיבי`, `ומי אמר ... והאמר`), forced explanations (`דוחקא`), and anonymous conclusions belong to `speaker_kind = "anonymous_stam"` (`speaker_id = null`, `attributed_to_ids = []`), never to the nearest mentioned Amora.
5. **Practical *Hilkheta* (`הלכתא`):** Editorial rulings (`והלכתא כוותיה ד...`) are recorded separately from individual scholars' personal positions.
6. **Homonym and orthography disambiguation:** Strictly separate `רבה` (Rabbah bar Nachmani) from `רבא` (Rava); standalone `רב` (Abba Arikha) from compound names (`רב יהודה`, `רב אסי`, `רב הונא`, `רב חסדא`, `רב נחמן`, `רב ששת`, `רב פפא`, `רב זביד`, `רב אשי`); Amora `רבי יוחנן` from Tanna `רבי יוחנן הסנדלר`; Tanna `רבי יהודה` from Amora `רב יהודה`.
7. **No negative imputation from silence:** Never create a negative or default position for an unmentioned scholar.

## 4. Three Completeness Tiers and Pilot Feasibility Gate

1. **`SOURCE_COMPLETE`:** Every segment in the tractate is mapped from the pinned export with verified `raw_array_index`, chapter, daf, SHA-256 hashes, and reversible `offset_map`.
2. **`PROVISIONAL_TRACTATE_COMPLETE`:** 100% of tractate segments belong to a reconciled primary sugya (or documented unresolved boundary), all layers pass `validators.py`, and uncertainties remain in `review_queue.jsonl`. Pilot slices are labeled `PILOT_SLICE_PROVISIONAL_COMPLETE` — never misrepresented as whole-tractate completion.
3. **`SCHOLARLY_CONFIRMED`:** Requires independent human expert review and adjudication under a declared agreement protocol. **AI-only passes (`ai_single` or `ai_independent_double`) are never labeled `scholarly_confirmed`.**

### Pilot Calibration Gate (Before Scaling to Full Berakhot & Subsequent Tractates)

- Annotate **Berakhot 2a–5a** (`151` segments, `7` amudim: Mishnah, halakhic time-boundary dialectic, tannaitic baraitot, aggadic night-watches/David narratives, scriptural juxtaposition, suffering-of-love `יסורין של אהבה` series, Kriyat Shema al ha-Mitah) and **Bava Metzia 21a–22b** (`64` segments, `4` amudim: opening Mishnah of *Elu Metziot*, multi-generation Amoraic disputes on `יאוש שלא מדעת` between Abaye and Rava, `איפוך` proposal and rejection, Rav Zvid vs. Rav Papa alternative reconstructions, conditional `לא צריכא` distinctions, cross-amud and cross-daf argument trajectories).
- Run a genuinely independent second AI reading (`ai_independent_double`) across `>= 20` proposed sugyot without exposing Pass 1–3 labels.
- Measure and report exact agreement denominators on: (a) sugya boundary spans, (b) named speaker/authority attribution, (c) exact source-span alignment (`100%` required), (d) question/alternative decomposition, and (e) position status (`asserted` vs `rejected`/`conditional`/`reconciled`).
- Pause for owner budget authorization before incurring any paid external API spend for Bavli-wide bulk passes.
