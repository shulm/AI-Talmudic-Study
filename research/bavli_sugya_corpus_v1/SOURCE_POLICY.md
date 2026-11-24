# Source, Edition, and Licensing Policy — Bavli Sugya Corpus v1

## 1. Local Sefaria Export Audit and Edition Selection

Before constructing any references or annotations, all 37 tractates of Talmud Bavli in the immutable local Sefaria Export (`F:/Sefaria-Export-master`, export timestamp `2025-03-18T05:02:42.863984`) were audited across all available Hebrew/Aramaic JSON files:

| File in `Hebrew/` | Tractates covered | Non-empty segments | License field | Edition uniformity finding |
|---|---:|---:|---|---|
| `William Davidson Edition - Aramaic.json` | 37 / 37 | 81,793 | `CC-BY-NC` (all 37) | **100% uniform single unvocalized Aramaic/Hebrew edition across all 37 tractates** |
| `Wikisource Talmud Bavli.json` | 37 / 37 | 81,793 | `CC-BY-SA` (all 37) | Uniform `CC-BY-SA` edition, identical `[page_idx, seg_idx]` segment grid (`shape_eq=True` on 37/37) |
| `merged.json` | 37 / 37 | 81,793 | `None` (missing) | **Mixed edition**: uses `William Davidson Edition - Vocalized Aramaic` in 33 tractates, but silently switches to `Wikisource Talmud Bavli` in *Zevachim*, *Menachot*, *Chullin*, and *Niddah* |

### Pinned Canonical Edition (`source_version_id`)

We pin **`William Davidson Edition - Aramaic.json`** (`source_version_id = "sefaria-export-2025-03-18:bavli:william-davidson-aramaic:v1"`) as the single, internally consistent primary Hebrew/Aramaic base text across all 37 Bavli tractates:

1. **No silent edition mixing:** Unlike `merged.json`, `William Davidson Edition - Aramaic.json` never switches underlying editions in *Kodashim* or *Tahorot*.
2. **1-to-1 coordinate compatibility:** Its 2D array structure `text[page_idx][seg_idx]` matches `merged.json` and `Wikisource Talmud Bavli.json` across every single tractate (`81,793` non-empty segments total), so existing repository dispute-index addresses (`rav_shmuel`, `abaye_rava`, `yochanan_lakish`, `rabbah_yosef`) join cleanly by `(tractate, raw_array_index)` and canonical `ref`.
3. **Immutability:** `F:/Sefaria-Export-master` is accessed strictly read-only; SHA-256 digests of every source file and every segment are frozen in `source_version_manifest.json` and per-tractate `manifest.json`.

## 2. Reference Construction and the One-Daf Offset Hazard

Prior normalized Bavli files (`F:/Sefaria_Corpus_Normalized`) suffered from an off-by-one folio bug that labeled the opening Mishnah of *Berakhot* (`מאימתי קורין את שמע בערבין`) as `Berakhot 3a:1` instead of `Berakhot 2a:1`.

**Strict rule:** This pipeline never reads `F:/Sefaria_Corpus_Normalized` and never uses guessed folio arithmetic. Every reference is derived directly from the Sefaria `Talmud` schema (`addressTypes: ["Talmud", "Integer"]`) on the raw 0-based `text[page_idx][seg_idx]` array:

- `folio_num = page_idx // 2 + 1`
- `amud = "a" if page_idx % 2 == 0 else "b"`
- `daf = f"{folio_num}{amud}"`
- `segment_num = seg_idx + 1`
- `ref = f"{tractate} {daf}:{segment_num}"`

### Verified Structural Pagination Edge Cases Across All 37 Tractates

- **Berakhot opening anchor:** `page_idx = 2, seg_idx = 0` -> `Berakhot 2a:1` (`מאימתי קורין את שמע בערבין...`). Indices `0` and `1` (`1a`, `1b`) are empty title-page slots across standard tractates.
- **Tamid start boundary:** `text[0..48]` are empty; first non-empty page is `page_idx = 49` -> `49 // 2 + 1 = 25`, odd -> **`Tamid 25b:1`**, ending at `Tamid 33b:12` (`207` segments), matching traditional Vilna pagination.
- **Nazir internal empty amud:** **`Nazir 33b`** (`page_idx = 65`) has `0` base-text segments in the Vilna layout (printed page carries commentary wrap only), resuming at `Nazir 34a:1` (`page_idx = 66`). Our scanner iterates actual array indices rather than assuming contiguous non-empty amudim, preserving exact fidelity across `Nazir 33a -> 34a`.
- **Zero empty segments inside non-empty amudim:** Verified across all `81,793` segments of all 37 tractates.

## 3. Redistribution and Public-Repository Safety (`CC-BY-NC`)

Because `William Davidson Edition - Aramaic.json` carries a `CC-BY-NC` license and `shulm/AI-Talmudic-Study` is a **public** repository:

1. **Full source text stays local-only:** Full `raw_text` and `canonical_text` strings for `segments.jsonl` are materialized only in `.gitignore`d `research/bavli_sugya_corpus_v1/local_source_cache/<tractate_slug>/segments.local_fulltext.jsonl`.
2. **Repository-facing `segments.jsonl`:** Stores `raw_text: null` and `canonical_text: null`, while publishing deterministic `segment_id`, `ref`, `he_ref`, `chapter_num`, `raw_array_index`, `source_file_sha256`, `raw_sha256`, `canonical_sha256`, `raw_char_len`, `canonical_char_len`, and the exact reversible `offset_map` (`[[canon_start, canon_end, raw_start, raw_end], ...]`).
3. **Short evidence snippets:** `statements.jsonl` and `anchor` objects store only bounded scholarly quotation snippets (`source_quote` / `quote`) needed to ground claims and argument edges, together with exact `{segment_id, start_char, end_char}` character offsets into `canonical_text` and `quote_sha256`.
4. **Dual-mode verification:** When `F:/Sefaria-Export-master` (or `local_source_cache`) is present, `validators.py` verifies every `raw_sha256`, `canonical_sha256`, reversible `offset_map`, and exact substring `canonical_text[start_char:end_char] == quote`. When running in an environment without the local Sefaria export, `validators.py` still verifies schema conformance, referential integrity, partition coverage, `quote_sha256 == sha256(quote)`, span bounds `0 <= start_char < end_char <= canonical_char_len`, and all rabbinic attribution invariants.

## 4. Reversible Canonical Text Normalization (`canon_strip_html_collapse_ws_v1`)

To make character offsets deterministic, human-auditable, and reversible back to the raw JSON string:

1. HTML tags (`<big>`, `<strong>`, `<i>`, `<small>`, `<br>`, etc.) are stripped; every character outside HTML tags retains its exact raw index.
2. Runs of whitespace are collapsed to a single ASCII space (`U+0020`), and leading/trailing whitespace is trimmed.
3. No Hebrew/Aramaic letters, matres lectionis, brackets, or punctuation in `William Davidson Edition - Aramaic.json` are deleted or rewritten.
4. Every contiguous run of surviving characters is recorded in `offset_map` as `[canon_start, canon_end, raw_start, raw_end]`, guaranteeing exact character-level projection back into `raw_text`.
