# Pilot Feasibility and Error-Analysis Report — Bavli Sugya Corpus v1

## 1. Executive Summary and Gate Assessment

- **Pilot Scope:** `215` contiguous source segments across `11` amudim in two contrasting tractates:
  - **Berakhot `2a:1–5a:24`** (`151` segments: Mishnah, halakhic time-boundary dialectics, Tannaitic baraitot, `צריכותא`, aggadic narratives, liturgical exegesis, bedtime Shema, `יסורין של אהבה`).
  - **Bava Metzia `21a:1–22b:16`** (`64` segments: chapter transition, Mishnah *Elu Metziot*, `תיקו` inquiries, 40-segment multi-daf `יאוש שלא מדעת` sugya with 9+ `תא שמע` rounds, `תיובתא דרבא`, `הלכתא כוותיה דאביי`, and `רבה` vs `רבא` paired disputes).
- **Whole Tractates Completed:** **`0 / 37`** (explicitly reported: both `Berakhot` and `Bava Metzia` are `SOURCE_COMPLETE` on all `2,749` and `3,660` segments respectively, and `PILOT_SLICE_PROVISIONAL_COMPLETE` on their calibrated slices).
- **External Paid API Spend:** **`$0.00 USD`** (`0` paid external API calls; budget guard active).
- **Feasibility Gate Verdict:** **PASS FOR PROVISIONAL PIPELINE FEASIBILITY (`PROVISIONAL_AI_DOUBLE_READY_FOR_BERAKHOT_SCALE_UPON_BUDGET_AUTH`)** — ready to scale across the remaining `2,598` segments of *Berakhot* once an owner-approved API/compute budget is authorized, and ready for human Talmudic expert review on the `13` open `review_queue.jsonl` items.

## 2. Stratified Double-Review Evaluation (`24` Primary / `28` Blind Top-Level Sugyot)

To prevent self-confirmation bias, the independent second reader (`research` subagent on `Gemini 4 Carbon`, output frozen at SHA-256 `3bac6d28d1a0c9cc815a73d9998af177f4256c42f4dc524f521c18758bd6156d`) read only the raw segment files *before* any Pass 1–3 annotation files were written to the workspace.

| Evaluation Dimension | Denominator | Agreement | Findings & Error Analysis |
|---|---:|---:|---|
| Exact character-offset & raw-HTML reversible alignment | `77` statements + `54` boundary cues | **`100.0%`** (`131 / 131`) | Deterministic Python `build_anchor` + `offset_map` eliminated hallucinated quotes and offset drift completely |
| Inter-segment sugya boundary slots | `213` slots (`150` BRK + `63` BM) | **`98.12%`** (`209 / 213`) | `22 / 22` (`100%`) of Primary Pass 1 internal cuts were independently placed at the exact same segments by the blind reader |
| Exact top-level sugya span identity | `24` primary top-level sugyot | **`87.50%`** (`21 / 24`) | The `3` non-identical spans (`BRK 4b:27–5a:5`, `BRK 5a:6–19`, `BM 21a:19–22b:10`) differed solely in sub-sugya vs top-sugya granularity, and **both** readers independently flagged all 3 as `ambiguous` |
| Cross-amud / cross-daf / slice-edge continuations | `4` slice edges + `7` internal amud breaks | **`100.0%`** (`11 / 11`) | Both passes caught `21a:19 ('איתמר') -> 21b:1`, `4b:28 ('אמר רב נחמן') -> 5a:1`, `20b:26 -> 21a:1`, `5a:24 -> 5b:1`, and `22b:16 -> 23a:1` |
| Named scholar, transmitter, & homonym attribution | `11` focal questions / `53` named statements | **`100.0%`** | Zero `רבה`/`רבא` confusions (`BM 22b:11–14`); zero compound-`רב` confusions; `100%` separation of transmitters (`משמיה דרב`, `רבי זריקא -> רבי אמי -> ריב״ל`, `רבא -> רב סחורה -> רב הונא`, `רבי יוחנן משום רבי ישמעאל בן יהוצדק`) |
| `חד אמר`, `תיקו`, and `תיובתא` decision status | `2` `חד אמר` pairs, `1` `תיקו`, `2` `תיובתא` tokens | **`100.0%`** | Both `חד אמר` pairs (`BRK 4a:8–9`, `5a:14–15`) left unassigned; `BM 21a:18` marked `unresolved`; `BM 22b:6` marked Rava `rejected`, while deflected `תיובתא דרבא` at `BM 22b:13–14` kept Rava `asserted` |
| Semantic scope interpretation | `24` sugyot | **`95.83%`** (`23 / 24`) | `1` genuine interpretive difference at `BRK 5a:16–17` (`אלו ואלו יסורין של אהבה הן`: inclusive reconciliation vs Rashi's reading that R. Yohanan rejects both `ביטול תורה` and `ביטול תפלה` restrictions); preserved in `rev:bavli:berakhot:5a:14:v01` |

## 3. Validator-Caught Pre-Release Defects (Preserved Audit Lesson)

During compilation of Pass 2–3 before final sign-off, `validators.py` automatically caught and blocked two instructive failure modes:
1. **Hypothetical Stam defense (`אמר לך רבא` at `BM 22b:14:s01`):** Initial Pass 2 attached `attributed_to_ids: ["scholar:amora:rava"]` while setting `speaker_kind: "anonymous_stam"`. `validators.py` (`[rabbinic:stam]`) rejected mixing anonymous Stam redactional voice with named attribution, enforcing clean separation between the Stam defense (`22b:14:s01`) and Rava's actual cited memra (`22b:14:s03`).
2. **Per-branch `חד אמר` review coverage (`BRK 4a:9:s01`, `5a:15:s01`):** `validators.py` (`[rabbinic:chad_amar]`) required every individual `unresolved_chad_amar` statement branch — not only the opening branch — to be linked in `review_queue.jsonl`.

## 4. Comparison With Existing Disagreement-Selected Pair Indexes

Across all `215` pilot segments (`Berakhot 2a–5a` and `Bava Metzia 21a–22b`), the four existing repository pair-dispute indexes (`rav_shmuel`, `abaye_rava`, `yochanan_lakish`, `rabbah_yosef`) cover only **`4` segment refs** (`Berakhot 5a:6`, `Bava Metzia 21b:1`, `21b:4`, `21b:11` — missing `Bava Metzia 22b:11–14` where `רבה` and `רבא` dispute directly because Rabbah–Rava is not one of the four pair indexes, and omitting the other `210` segments of Mishnah, baraita, Stam dialectic, single-scholar rulings, `תיקו`, and aggadah). All `4` indexed refs are present and grounded in our pilot corpus.

## 5. Scoped Next Step and Estimated Budget for Full *Berakhot*

1. **Immediate human review target:** Adjudicate the `13` open items in `tractates/{berakhot,bava_metzia}/review_queue.jsonl` (especially associative aggadic sugya granularity on `Berakhot 4b:27–5a:19` and the `אלו ואלו` interpretation at `Berakhot 5a:16–17`) to establish the first `human_reviewed` gold anchor set.
2. **Completing *Berakhot* (`5b:1–64a:15`, `2,598` remaining segments across `61` overlapping 2-amud windows):**
   - Estimated structured-JSON token volume (`Pass 1` + `Pass 2` + `Pass 3` on `Gemini 4 Carbon`): `~1.1M` input tokens and `~0.45M` output tokens across the `61` windows.
   - Once owner budget authorization is granted (`--authorized-budget-usd`), run `cli` across Windows `w005..w065` of *Berakhot*, verify 100% `2,749 / 2,749` segment partition coverage via `cli validate`, mark *Berakhot* `PROVISIONAL_TRACTATE_COMPLETE`, and proceed in TOC order to `#2 Shabbat`.
