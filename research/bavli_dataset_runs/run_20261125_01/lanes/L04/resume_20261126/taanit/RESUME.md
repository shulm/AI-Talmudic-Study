# Taanit resumable producer checkpoint — 2026-11-26

Partial: **324/895 source segments per all eight required layers**, through **Taanit 12b:8**. Next **Taanit 12b:9**; **571 remain per layer**. Tractate delivery and full independent review remain unfinished.

Authoritative snapshot: `32bcf629046f104ec121ba829715249cb950f910fccadc3d989be9ea6592d300`. Owner remains `L04/taanit_resume_20261126`, epoch 3. The current worker `/root/taanit_continuation_3` is handing off inactive; the lane lead may dispatch the next exclusive writer under the existing lane authority. No second concurrent producer may promote Taanit.

See `CHECKPOINT_024.json` for exact contract/source hashes, accepted proposal chain, export manifest, counts and limitations. `CHECKPOINT_020.json` preserves the intermediate 279-segment state; `CHECKPOINT_014.json` preserves the previous worker's 203-segment state.

This continuation added **121 source segments and 1,956 records** in manually authored batches015–024. Current totals are **4,377 active records and 4,502 preserved record versions**. Original 203-segment-state records are unchanged. Sources and common runner/schema remain unchanged. All new annotations remain AI-provisional, unreviewed and ML-ineligible; no human certification is claimed.

Replay before continuing:

```powershell
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit
```

Verify CURRENT and OWNER and use runner.load to verify original source bytes. Read from 12b:9 with overlap 12b:5–8 and sufficient continuation. Source was read through 12b:9; later material still requires original-source reading. All eight passes remain required. Author scripts use only serialization helpers from the prefix of build_batch008.py; they are single-use checkpoint-bound authored proposals. **Replay immutable accepted proposal bytes, do not rerun these author scripts against a later CURRENT.** The accepted 016 proposal is batch016b.json; batch016.json is an unsubmitted earlier draft and does not count as production. Validation failures caught unsupported relation/role values and a duplicate local ID before accepted promotion; see attempt notes in the checkpoint.

Latest exact export is `F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit/exports/resume_20261126_324_32bcf629`, manifest SHA-256 `ce11c5cc949e71cd47c9f8c39bcd2362b8b13f99505185f9339cfe96bffdd437`. Replay, source checks, all nine production file hashes, all export-file hashes, preserved-record equivalence, active-link closure and embedded attribution-scope audit passed. No structural tails remain at this endpoint. No commits or pushes were made by this worker; parent owns packaging/publication.

Correction013 remains intact. Independent recheck `taanit_frozen_comparison/correction013_independent_recheck.json` SHA-256 `b54b1d57d15b6c63d48c1e66a0f378545d0ea82c8eb9698c4df648cc6dc88eaf` verified its seven corrections and preservation of three uncertainties against snapshot `1bccca4286a5288948141c490c2a66d0b3f3f32738236b66e70e2ac65145e82f`. That exact-version review does not admit later production. Existing review cohorts remain separate from producer rereads.

Supported uncertainty includes unnamed dialogue turns in 9a:2–4; printed רבי יוסי (בר) חנינא; compact תלמיד עושה in 10b:3–4; parenthetical judgment-scene wording; printed חסיד/[צ"ל חסד]; unassigned Hiyya/Shimon Berabbi ייסר/יאסר readings; and separate alternative Shmuel fast-deferral reports. Narrative speakers, quoted scripture, rhetorical speech, source cosmology and normative rules remain distinguished. No unprinted narrative or scientific verification was supplied.

The coordinator's additive answer-set policy 001 was read. New questions in batches022–024 explicitly state that partial means their represented local source-supported response inventory, without exhaustive alternatives or choice-task eligibility. There was no bulk relabelling of prior questions. Parent coordinates independent comparison and any exact-version corrections.
