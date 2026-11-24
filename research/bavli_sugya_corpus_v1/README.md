# Babylonian Talmud Sugya Corpus v1 (`research/bavli_sugya_corpus_v1`)

A verifiable, source-grounded, multi-layer structured corpus pipeline for **Talmud Bavli**, built tractate-by-tractate from a single pinned Hebrew/Aramaic Sefaria edition (`William Davidson Edition - Aramaic.json`, `CC-BY-NC`, `37/37` tractates, `81,793` segments).

> **Current Status:** Infrastructure complete + Pilot calibration (`Berakhot 2a–5a` = `151` segments; `Bava Metzia 21a–22b` = `64` segments) annotated, validated, and double-reviewed (`ai_independent_double`). **Zero whole tractates are claimed complete yet** (`Berakhot` pilot covers `151 / 2,749` segments; `Bava Metzia` pilot covers `64 / 3,660` segments). All AI annotations are labeled **provisional** (`provisional_ai_double`), never `scholarly_confirmed`.

## Directory Layout

- [`SOURCE_POLICY.md`](SOURCE_POLICY.md) — Audit of all 37 Bavli tractates, why `William Davidson Edition - Aramaic.json` was pinned over mixed `merged.json`, solution to the normalized one-daf offset bug, `Tamid 25b` / `Nazir 33b` pagination verification, and `CC-BY-NC` local-only full-text protection.
- [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) — Multi-pass windowed segmentation architecture, rabbinic attribution safeguards (`חד אמר`, `איפוך`, `תיובתא`, `לא פליגי`, `משמיה ד...`, anonymous Stam, `רבה` vs `רבא`), and three completeness tiers.
- [`SCHEMA.md`](SCHEMA.md) & [`schemas/schema_v1.json`](schemas/schema_v1.json) — Versioned JSON Schema (`1.0.0`), deterministic ID grammar, lineage redirects, and exact substring offset contracts.
- [`MODEL_LOG.md`](MODEL_LOG.md) — Model configuration (`Gemini 4 Carbon` default), prompt audit paths, and `$0.00` paid external API guard.
- `src/bavli_corpus/` — Executable Python package:
  - `scanner.py` — Deterministic 37-tractate TOC scanner, `Talmud` daf/amud reference builder, chapter mapper, SHA-256 hasher, and reversible HTML-to-canonical `offset_map` generator.
  - `window_manager.py` — Bounded overlapping amud window slicer (`central` + preceding/following context) with deterministic window manifests.
  - `reconciler.py` — Global cross-window and cross-daf sugya boundary reconciler and lineage-redirect tracker.
  - `annotation_runner.py` — Idempotent, checkpointed runner supporting `offline_frozen` replay, `dry_run`, `smoke`, and budget-guarded `gemini_api` structured JSON execution.
  - `validators.py` — JSON Schema Draft 2020-12 + cross-layer semantic & rabbinic invariant validator.
  - `queries.py` — Reference query & export helpers: reconstruct any sugya from local segments, retrieve all justified statements of a scholar across processed tractates, and derive leakage-checked ML Q–A views with explicit caveats.
- `tests/` — Automated pytest suite including adversarial rabbinic fixtures (`רבה`/`רבא`, `חד אמר`, `איפוך`, `לא פליגי`, `משמיה ד...` transmission, cross-daf sugya continuity, anonymous Stam, offset misalignment rejection).
- `scholars.jsonl` — Global canonical scholar & collective registry with homonym disambiguation rules.
- `tractate_progress.json` & `source_version_manifest.json` — Global 37-tractate completion and SHA-256 source manifest.
- `parallel_family_links.jsonl` — Cross-tractate and intra-tractate parallel sugya/dispute family links for leakage-safe downstream splitting.
- `tractates/berakhot/` & `tractates/bava_metzia/` — Pilot tractate directories (`manifest.json`, `segments.jsonl`, `sugyot.jsonl`, `statements.jsonl`, `questions.jsonl`, `positions.jsonl`, `relations.jsonl`, `review_queue.jsonl`, `QA_REPORT.md`, `NEXT_HANDOFF.md`).
- `FEASIBILITY_REPORT.md` — Pilot double-review comparison (`ai_independent_double`), agreement denominators, error analysis, and scoped next step for full *Berakhot* production.

## Reproducible Commands

Run from the repository root (with Python 3.12+):

```powershell
# 1. Scan 37-tractate TOC and freeze local full-text cache + repo hash manifests
python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli scan --corpus-root "F:/Sefaria-Export-master" --tractates "Berakhot" "Bava Metzia"

# 2. Materialize pilot corpus from audited window outputs (idempotent, $0 API cost)
python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli build-pilot --corpus-root "F:/Sefaria-Export-master"

# 3. Validate all schemas, exact character spans, coverage invariants, and rabbinic rules
python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli validate --corpus-root "F:/Sefaria-Export-master"

# 4. Run full unit + adversarial rabbinic QA test suite
python -X utf8 -m pytest research/bavli_sugya_corpus_v1/tests -q

# 5. Demonstrate sugya reconstruction, scholar statement lookup, and caveated Q-A derivation
python -X utf8 -m research.bavli_sugya_corpus_v1.src.bavli_corpus.cli demo-queries --corpus-root "F:/Sefaria-Export-master"
```
