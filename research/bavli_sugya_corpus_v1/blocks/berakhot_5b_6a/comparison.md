# Independent Source-Only Review Comparison — `berakhot_block_002_5b_6a` (`Berakhot 5b–6a`)

- **Frozen blind initial review:** `independent_review_initial.json` (`SHA-256: 1249a6d49e1bcb4dd82a88a0bcf13be4cdc5b56c3376a827b91d654c658e480f`)
- **Frozen initial primary proposal:** `proposal_initial.json` (`SHA-256: 8c81a424917cc05b18c2635140719d7bb987d72079928396c78ba5686a63eef9`)
- **Core span audited:** `Berakhot 5b:1–6a:25` (`52` core segments), plus inherited open tail `B24` (`Berakhot 5a:24`) and following context `Berakhot 6b:1–37` (`37` segments).

## 1. Boundary & Continuation Comparison

Across the `52` inter-segment boundary slots spanning `5a:24–6a:25`, the primary proposal and the blind source-only reviewer agreed on **`51 / 52` (`98.08%`)** boundary slots and matched **8 of 9** primary units identically:

| Primary Key | Primary Span & Status | Blind Reviewer Span & Status | Match |
|---|---|---|---|
| `B24` (`sug_9a1c712c3a26fe45003b`) | `5a:24–5b:3` (`provisional`, closed) | `5a:24–5b:3` (`provisional`, closed) | Exact match |
| `B25` (`sug_8aaf502a219414d94655`) | `5b:4–5b:9` (`provisional`) | `5b:4–5b:9` (`provisional`) | Exact match |
| `B26` (`sug_3e781bcc10a62912f6fa`) | `5b:10–5b:16` (`provisional`) | `5b:10–5b:16` (`provisional`) | Exact match |
| `B27` (`sug_4bddd22de96ee7dad529`) | `5b:17–5b:20` (`provisional`) | `5b:17–5b:20` (`provisional`) | Exact match |
| `B28` (`sug_8abdf1580603d91a8e25`) | `5b:21–5b:24` (`provisional`) | `5b:21–5b:24` (`provisional`) | Exact match |
| `B29` (`sug_d210ba50f39c0d38f613`) | `5b:25–6a:1` (`provisional`, crosses daf) | `5b:25–6a:1` (`provisional`, crosses daf) | Exact match |
| `B30` (`sug_726a2749e243fa32b5db`) | `6a:2–6a:6` (`provisional`) | `6a:2–6a:6` (`provisional`) | Exact match |
| `B31` (`sug_5eb00cfd65e6c6c1ae30`) | `6a:7–6a:16` (`provisional`, with sub-sugya `B31a` `6a:8–16`) | Split `6a:7` (`#8`) + `6a:8–6a:16` (`#9`), both `ambiguous` | **Preserved disagreement** |
| `B32` (`sug_bc413c5b52ef04c8a017`) | `6a:17–6a:25` (`open_right` -> `6b:1`) | `6a:17–6a:25` (`open_right` -> `6b:1`) | Exact match |

## 2. Preserved Boundary Disagreement (`Berakhot 6a:7 | 6a:8`)

- **Primary proposal:** Groups `6a:7` (Abba Binyamin's baraita on prayer in the synagogue) with `6a:8–6a:16` (Ravin bar Rav Adda in the name of R. Yitzchak on God's presence in the synagogue and the 10/3/2/1 Shekhinah scale), while marking `6a:8–6a:16` as nested sub-sugya `B31a`.
- **Blind reviewer:** Splits `6a:7` as the concluding fourth member of the `תניא אבא בנימין אומר` series (`5b:21`, `5b:25`, `6a:2`, `6a:7`) and starts a new primary sugya at `6a:8` as the opening member of the three-part `אמר רבין/אבין בר רב אדא אמר רבי יצחק` series (`6a:8`, `6a:17`, `6b:2`), noting `6a:7–16` as an explicit alternative.
- **Handling:** Neither frozen initial file was edited. `B31` carries `span_review_status = "independent_source_reviewed_with_disagreement"` and links open review item `boundary_disagreement_preserved` (`rev_...`) with exact evidence at `6a:7` and `6a:8`.

## 3. Attribution & Textual-Label Findings Confirmed by Both Passes

- **`5b:3`:** `ההוא סבא` transmits in the name of `רבי שמעון בן יוחאי` (`משום ר' שמעון בן יוחאי`).
- **`5b:14`:** Wikisource prints `רבי אליעזר` / `ר' אליעזר` (for the Amora R. Elazar ben Pedat); preserved as textual label with open `textual_variant_or_homonym` review warning against merging with Tanna R. Eliezer.
- **`5b:17`:** Explicit `ואמרי לה` alternative between `רב יהודה אחוה דרב סלא חסידא` and `רב אדא בר אהבה`, plus anonymous `איכא דאמרי` pair at `5b:20`.
- **`5b:21`:** Explicit `ואיתימא` alternative between `רב` (transmitted via `רב יהודה`) and `רבי יהושע בן לוי` (`ריב"ל`), left unassigned in `speaker_candidates`.
- **`6a:8` vs `6a:17`:** Orthographic variant `רבין בר רב אדא` (`6a:8`, `6b:2`) vs `רבי אבין בר רב אדא` (`6a:17`) preserved verbatim as separate textual labels pending entity disambiguation.
- **`6a:25 -> 6b:1`:** `B32` ends mid-argument at `6a:25` and completes at `6b:1` (`וכולהו כתיבי באדרעיה:`), leaving `Berakhot 6a:16` as the last closed ref and `Berakhot 6b:1` as the next unprocessed ref.
