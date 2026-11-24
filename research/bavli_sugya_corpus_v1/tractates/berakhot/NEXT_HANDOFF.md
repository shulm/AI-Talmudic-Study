# Next Handoff — Tractate Berakhot (`ברכות`)

## Current Checkpoint

- **Source inventory (`segments.jsonl` + `manifest.json`):** Complete for all `2,749` segments (`Berakhot 2a:1–64a:15`).
- **Annotated & double-reviewed pilot slice:** `Berakhot 2a:1–5a:24` (`151` segments across Windows `w001..w004`).
- **Pending boundary at slice edge:** `sugya:bavli:berakhot:5a:24__5a:24` (`boundary_status = "window_edge_pending"`, `rev:bavli:berakhot:5a:24:v01`) continues mid-sentence onto `Berakhot 5b:1–3` (`וקובר את בניו מוחלין לו על כל עונותיו...`).

## Scoped Next Step (Upon Budget Authorization)

1. Resume `annotation_runner` starting at Window `w005` (`central_dafs = ["5b", "6a"]`, `preceding_context_dafs = ["5a"]`, `following_context_dafs = ["6b"]`).
2. Reconcile `5a:24` with `5b:1–3` (`continues_from_prev_window = true`), recording a `redirects_from: ["sugya:bavli:berakhot:5a:24__5a:24"]` lineage redirect on the merged sugya.
3. Proceed in 2-amud overlapping windows through `Berakhot 64a:15` (`125` non-empty amudim total -> `61` remaining windows), run `cli validate` after every checkpoint, and only then upgrade `tractate_completion_status` to `PROVISIONAL_TRACTATE_COMPLETE` before moving to TOC #2 (`Shabbat`).
