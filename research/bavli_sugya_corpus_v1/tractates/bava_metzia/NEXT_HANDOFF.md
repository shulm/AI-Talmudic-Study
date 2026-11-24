# Next Handoff — Tractate Bava Metzia (`בבא מציעא`)

## Current Checkpoint

- **Source inventory (`segments.jsonl` + `manifest.json`):** Complete for all `3,660` segments (`Bava Metzia 2a:1–119a:6`).
- **Annotated & double-reviewed calibration slice:** `Bava Metzia 21a:1–22b:16` (`64` segments).
- **Pending slice edges:**
  1. `sugya:bavli:bava_metzia:21a:1__21a:6` (`rev:bavli:bava_metzia:21a:1:v01`) continues from Chapter 1's `סמפון` sugya starting at `20b:18`.
  2. `sugya:bavli:bava_metzia:22b:11__22b:16` (`rev:bavli:bava_metzia:22b:11:v01`) continues mid-sentence onto `23a:1–15` (where Rav Zvid in the name of Rava analyzes the Tannaitic dispute and states `הלכתא`).

## TOC Ordering Note

Per `RESEARCH_PROTOCOL.md`, production tractate completion proceeds strictly in pinned TOC order (`#1 Berakhot`, `#2 Shabbat`, ..., `#21 Bava Metzia`). When full-tractate processing reaches TOC #21 (`Bava Metzia`), Windows `w001..w019` (`2a–20b`) will merge seamlessly into `21a:1–6` via `redirects_from`, and Window `w022` (`23a–23b`) will complete `22b:11–16` through `23a:15`.
