# Research handoff — updated 2026-11-25

## Evidence-shrinkage bounded delivery — PR20

Executed PR19 G0–G4 from assignment724be8c49808e1e1b8643d81c73267f7577439c8; pre-fit38dfff076b90d7c08387a06bd25f3cc75f15f6ae was pushed and posted/read back before fitting. Read [results](research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/RESULTS.md), [handoff](research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/NEXT_HANDOFF.md), and [resource ledger](research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/RESOURCE_USAGE_FINAL.json).

Status **INCOMPLETE / NUMERICALLY_UNRESOLVED**, qualification false. All12 shared fits,64 adaptation batches,1664 personal solves and76 optimizer records finished without retries. H batch7 probability difference1.2232536670264693e-6 exceeded the fixed1e-6 tolerance. The frozen executor stopped after H artifacts, before scientific_summary.json. The frozen verifier rejected that missing summary; it was not repaired. An explicitly post-run observer retained1158/1160 reached comparisons (max2.842170943040401e-14), unchanged private hashes, and the original exception. This is not VERIFIED_COMPLETE. Separate inventory confirms all36 archives/176 query arrays and965 historical blobs preserved.

Available ES gains are .507507/.502357/.519710/.514875 and inactive degradation9.2423362e-6/0/0/0, but contrast NRMSE .555276/.564899/.534685/.556167 fails .5 throughout E/F/G/H. Preserve these empirical failures alongside numerical invalidity; no control or expectation theorem rescues qualification. No human/text experiment, downloads, paid calls, corpus changes or merge. Stop at review. PR18's separate planning-only sweep and seed banks remain untouched; PR5/8 exposure and PR14/16 source-production tracks remain separate. Any numerical diagnosis or representation study needs a new bounded assignment; do not rerun, retune or repair this frozen execution.

## Active modeling continuation: general decision functions — 2026-11-24

The current modeling task is to learn `P(answer | problem, available answers, person's observed history)` on general corpora, then investigate the Talmudic application. This supersedes the scholar-position attribution objective in draft PR #1; retain that PR as historical context.

Read [the continuation entry point](research/decision_functions_2026-11-24/README.md), [the research plan](research/decision_functions_2026-11-24/RESEARCH_PLAN.md), and [the executable next-agent prompt](research/decision_functions_2026-11-24/NEXT_AGENT_PROMPT.md). Communicate and return evidence through [the coordination issue](https://github.com/shulm/AI-Talmudic-Study/issues/2) and linked draft PRs.

Status: **P0–P3 EXECUTED** on `codex/decision-functions-execution-v1`, draft PR #4. Read [the executed report](research/decision_functions_2026-11-24/runs/pilot_v1/AGENT_REPORT.md) and [concrete handoff](research/decision_functions_2026-11-24/runs/pilot_v1/NEXT_HANDOFF.md). Effective protocol freeze: `4de12a1fb300a7c9e9d927591bc4b101f0e263a2`. DICES retained 104 people/350 items, grouped into 271 input groups. Test: 22 people, 55 groups/76 items, k=16. B3 and M1 NLL both approximately 0.720449; the M1 interaction collapsed to numerical equivalence with B3. The formal sign-only primary status is positive at a delta of 1.9e-12, below optimizer tolerance; this is **not credible evidence of interaction benefit**. Correct histories improve NLL over shuffled histories by about 0.0941, and B3/M1 improve NLL over text-only B2 by about 0.0521, while accuracy is lower. Test outcomes are now exposed. Preserve results, the disclosed development optimizer-log loss, and local-only probability artifacts. Future experiments require a separate protocol and test-reuse disclosure. Existing source-index tracks below remain intact.

### Independent pilot review and next diagnostic assignment — 2026-11-24

Read [the pilot review](research/decision_functions_2026-11-24/reviews/pilot_v1_2026-11-24/REVIEW.md) and [the next-agent diagnostic prompt](research/decision_functions_2026-11-24/reviews/pilot_v1_2026-11-24/NEXT_AGENT_PROMPT.md). The review retains the completed pilot as qualified evidence of improved probabilistic prediction from personal history, with no numerically resolvable interaction gain. It independently checked 19 public integrity hashes, unchanged frozen laboratory blobs, recovered development selection, and retained test optimizer records; it did not have the private probability cache and did not replay the 171 arrays. The next assignment is bounded: reproduce saved-array verification, repair fail-open audit logging in new tooling, demonstrate planted-interaction recovery, compute the training-only regularization diagnostic where the cache is available, and propose a new protocol. Preserve `pilot_v1` and its lost-log disclosure. A new human held-out experiment and full corpus construction are outside that assignment.

### Completed interaction diagnostics and next synthetic assignment — 2026-11-24

PR #7 completed D0–D4 at `6da06a4b01bb825bcf4ad4b13c61648d6ee82220`. Read [its diagnostic report](research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/DIAGNOSTIC_REPORT.md), then [the independent diagnostic review](research/decision_functions_2026-11-24/reviews/interaction_diagnostics_v1_2026-11-24/REVIEW.md) and [the next-agent assignment](research/decision_functions_2026-11-24/reviews/interaction_diagnostics_v1_2026-11-24/NEXT_AGENT_PROMPT.md). This supersedes the earlier D0–D4 assignment as the next task. The committed verifier reproduces saved-array arithmetic on the executor's cache; this review checked code, complete public ledgers, resource arithmetic, and certificate formulas without private-cache access. The head recovers a planted interaction, but null degradation 0.0119493 fails the 0.01 gate; no original penalty passes every synthetic predictive gate. All three original DICES penalties favor zero interaction under the training objective. The revised continuation uses three distinct effective strengths `rho=sqrt(lambda_V*lambda_U)` with independent offset shrinkage, 18 selection fits and six fits on a second generated realization, within the same 24-fit cap. It is synthetic-only; no human fitting/evaluation, encoder acquisition, or corpus expansion is assigned. Preserve both completed runs and the missing historical development-log disclosure. Check parallel PRs #5 and #8 for exposure and source-preparation context before any future human or scholarly proposal.

### Completed canonical interaction diagnostic v2 — 2026-11-25

PR #12 executes PR #9's E0–E4 assignment. Pre-fit checkpoint `1ac9eaec22230d3db2b46ebdda3ada1f84f25366`; selection freeze `f830fbd989d196ebf5b44c2c862a2725da330c81`. Read [results](research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/RESULTS.md), [handoff](research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/NEXT_HANDOFF.md), and [proposal only](research/decision_functions_2026-11-24/runs/interaction_diagnostics_v2/NEXT_STUDY_PROPOSAL.md). Rho=.01, offset penalty=.1 qualifies on both independently generated held-out realizations: positive expected-NLL gains .647037/.648746; contrast NRMSE .133680/.123272; null degradation .005626/.006592 below .01. This is bounded synthetic capability with 96 supports in two dimensions, not human/text/16-support validation. Exactly24 shared fits,64 adaptation batches,1472 personal solves; zero retries/human fits/evaluations/downloads. Original pilot/v1 results and v1 null failure are unchanged. Saved-array arithmetic and supplemental audits pass; 287 historical files preserved. Final resource totals are in RESOURCE_USAGE_FINAL.json. Stop for review; future limited-history/representation work requires a separately frozen assignment. PR5/PR8 SRO exposure and TID-8/scholarly admission gates remain separate.

### Independent v2 review and next short-history assignment — 2026-11-25

Read [the v2 independent review](research/decision_functions_2026-11-24/reviews/interaction_diagnostics_v2_2026-11-25/REVIEW.md), [executable next-agent prompt](research/decision_functions_2026-11-24/reviews/interaction_diagnostics_v2_2026-11-25/NEXT_AGENT_PROMPT.md), and [machine-readable design](research/decision_functions_2026-11-24/reviews/interaction_diagnostics_v2_2026-11-25/next_short_history_design.json). This assignment supersedes v2's proposal-only handoff as the next modeling task. The review retains qualification at `40d201997ab8d79d138734b1ef116c161719c11b` and independently checked public arithmetic, all 88 records/1,472 personal solves, 225 delivery hashes, eight pre-fit source hashes, and final resource totals. Original private arrays were unavailable. The generic v2 verifier can PASS an empty run; the actual completed result has complete evidence and an exact supplemental audit. Repair that verification weakness in the new version without changing v2.

Next task: freeze and execute `short_history_v1`, primary 16 well-covered observations, secondary 4/32/96, two fresh realizations and two outcome-blind nested history schedules. Fix shared rho=.01 and lambda_b=.1; add one separately reported 16-case adaptation-scaling control (.06/.6), matched-other history permutations, and exact completeness gates. Complete design: 12 shared fits, 184 adaptation batches, 3,776 personal solves, 196 optimizer records; no retries, human evaluation, encoder acquisition, or corpus construction. A secondary success cannot rescue primary failure. Publish the new pre-fit checkpoint before optimization, then execute within the bounded assignment and return a draft PR/report through issue #2. Do not merge. Prepare the text-representation specification only as a later proposal. Parallel SRO PRs #5/#8 and provisional corpus PRs #10/#11 remain separate; consult their current handoffs and preserve their work.

### Completed short-history numerical study — 2026-11-25

Draft PR #15 executes PR #13 F0–F4 from assignment `47b19560350aa8c5d877d99f381d5b27f5b3490a`; pre-fit `89d9e0ca1b3fe3e23c3829294d3a806949943d3a`. Read [results](research/decision_functions_2026-11-24/runs/short_history_v1/RESULTS.md), [handoff](research/decision_functions_2026-11-24/runs/short_history_v1/NEXT_HANDOFF.md), and [proposal-only text specification](research/decision_functions_2026-11-24/runs/short_history_v1/TEXT_REPRESENTATION_NEXT_SPEC.md). Outcome: **COMPLETED_PRIMARY_FAILURE**, with **VERIFIED_COMPLETE** evidence. At16 well-covered observations the primary .01/.1 policy recovers planted interaction (gain .594196/.602815; contrast NRMSE .283461/.248433), but null degradation .052186/.057411 fails .01 in both C/D. Secondary .06/.6 reduces it to .009587/.010921; D still fails and no secondary rescue is permitted. D's96 anchor also fails the null, limiting extrapolation of the earlier v2 bounded result.

Exact196 optimizer records:12 shared fits,184 adaptation batches,3776 person-solves; no scientific retry. All17,038 saved-evidence comparisons pass (max3.55e-14), numerical/geometry checks pass, historical513 files and frozen scientific code preserved. The new verifier requires exact stages/archives/keys/rows/counts and explicitly conjoins completeness, numerical and predictive gates; it cannot approve an empty run. Final resource ledger includes failed pre-fit zero-fit tests and post-run audit:79.171875 accounted CPU seconds,90,120,192 bytes peak sampled RSS, with unprofiled overhead disclosed. No human models, encoder acquisition or corpus expansion. Stop for review; do not retune C/D or claim reliable primary16-case null control. PR5/8 and PR10/11 handoffs were read and their separate exposure/source tracks remain untouched.

### Independent short-history review and evidence-shrinkage assignment — 2026-11-25

Read [the short-history review](research/decision_functions_2026-11-24/reviews/short_history_v1_2026-11-25/REVIEW.md), [mathematical method and proof](research/decision_functions_2026-11-24/reviews/short_history_v1_2026-11-25/METHOD_NOTE.md), [executable next-agent prompt](research/decision_functions_2026-11-24/reviews/short_history_v1_2026-11-25/NEXT_AGENT_PROMPT.md), and [machine-readable design](research/decision_functions_2026-11-24/reviews/short_history_v1_2026-11-25/next_evidence_shrinkage_design.json). This is the next modeling assignment after PR #15's review stop. Retain `VERIFIED_COMPLETE / COMPLETED_PRIMARY_FAILURE` at `ee2b0a5a2f0916fed3dd59f720b902eb332eecc3`: primary16 null fails C/D, secondary D and D96 also fail. Independent public checks cover 1,216 scalar comparisons, all196 optimizer records,452 delivery hashes,12 pre-fit source hashes and513 preserved historical blobs; private arrays were unavailable. The empty-run verifier repair is confirmed. Add zero-optimization parameter-to-prediction forward replay in the new lab.

Next: freeze and execute `evidence_shrinkage_v1`, one fixed conditional-evidence probability mixture in four fresh mixed populations. Each has192 people (96 train/48 unused/48 test), with whole matched pairs balanced active/inactive in every partition; the SAME learned V serves both types. Use two fixed16-case histories, shared .01/.1 penalties, personal .06/.6, training-only symmetric empirical priors, and h=min(.009*(E-1)_+,log10), w=1-exp(-h), p_ES=(1-w)*B3+w*M1. Its expected null excess bound is .009 under the declared known-base model; positive recovery and each realized cohort's gates remain empirical. Complete budget:12 shared fits,64 adaptation batches,1664 person-solves,76 records. No selection, scientific retries, human/text experiment or corpus expansion. Publish the full pre-fit checkpoint before fitting, then return a draft PR and evidence through issue #2. No merge. Preserve separate SRO and corpus production/review work, including PRs #14/#16.

Coordination note: [PR #18](https://github.com/shulm/AI-Talmudic-Study/pull/18) at `49d7157e3998a20f646e9200c3e223bbbb58541f` is a separate planning-only global penalty/blend study with its own execution-authorization boundary. Its seed bank is disjoint from evidence_shrinkage_v1. Preserve that package and do not run its CLI or add its sweep under this assignment. The two plans address different estimands; this handoff recommends the bounded evidence-shrinkage experiment next without cancelling or superseding PR #18.

## Current source-index research: Rabbah and Rav Yosef

User requested all disputes of רבה and רב יוסף across Talmud, committed and pushed. Start with `rabbah_yosef_results/rabbah_yosef_index.json` and its README. Scan: 37 Bavli and 39 Yerushalmi tractates, 94,045 segments. Index: **101 source locations in 27 Bavli tractates**, grouped from 102 selected pattern candidates and 12 supplemental dialogue/continuation windows. One entry (Yevamot 45a:18) is classified as a resolved objection. No Yerushalmi entry was selected; this does not prove absence.

Review: all 207 pattern candidates and broad windows not already represented at selected opening refs received compact excerpt triage; selected supplements were read with fuller context. 47 pattern candidates are excluded as agreements and 58 remain `needs_review`. Broad windows not selected are NOT certified exclusions. Full sugyot have not all been checked. Counts preserve repeats and continuations, not unique topics.

Identity: רבה and רבא are separate. Explicit patronymics are filtered, but raw matches still include ordinary words such as מרבה and גברא רבה; do not trust raw candidates. Sotah 21a:10 attributes the objection to רבה but the alternative answer to רבא. Sanhedrin 98b:3 prints [רבה]. Bava Batra 32b uses both spellings. Preserve these readings and check textual witnesses before assigning all stages. Bava Kamma 51b has חד אמר formulations: do not assign views by order. Gittin 67a has ואיכא דאפיך להו. Menachot 39a is an attribution correction, not opposing rulings.

Narrow independent recall probe: 23 segments have literal רבה אמר/אומר and רב יוסף אמר/אומר; 22 are selected main refs. The remaining Eruvin 88a:9 gives the same ruling from different teachers. This small check is not evidence of exhaustive recall. `audit_rabbah_yosef_recall.py` reproduces it.

The builder and review script pin raw candidate SHA-256 values to prevent silent renumbering. Remap decisions by stable keys if changing retrieval. `verify_rabbah_yosef_sources.py` checks all 101 addresses and 626 context quotations directly against raw source arrays; it does not certify selection quality. UI tests and the required Rav–Shmuel test pass. A complete scan/build/audit rebuild was checked byte-for-byte. Source corpora and previous generated reports are unchanged.

Next research pass: read complete sugyot for the selected entries, resolve the 58 undecided candidates and remaining broad windows, audit indirect/anonymous formulations and name variants, and link parallel topics without deleting occurrences.

## Previous research: Rabbi Yohanan and Resh Lakish

The user requested the same research for רבי יוחנן versus רבי שמעון בן לקיש (ריש לקיש / בר לקיש / רשב״ל / ר״ל), followed by commit and push. Read `yochanan_lakish_results/yochanan_lakish_index.json` and its README first. The scan covers all 76 local tractates (94,045 segments). The selected index has **563 source locations: 338 Bavli and 225 Yerushalmi in 71 tractates (33 Bavli, 38 Yerushalmi)**. Counts include parallel occurrences and continued discussions, not unique topics.

Review: 1,409 declaration/joint candidates, of which 722 were selected, 134 excluded as pairings, and 553 left needing review. Another 17 explicit dialogue/rebuttal windows were selected from 2,109 broad windows, and 2 group statements were added manually (see the review below). Stable keys and frozen IDs are retained. Selection was based on first-pass excerpts, often compact views; it is NOT full-sugya certification. The broad appendix and unselected candidates have not been exhaustively audited. Do not estimate remaining misses without a new representative audit.

The scanner matches abbreviations and alternative names, and excludes explicit Yohanan patronymics. Ambiguous ר״ל is flagged. Other identities, variants, distant statements, anonymous pronouns and indirect disputes can still escape the patterns. Joint mentions are not automatically disputes. Zevachim 46b:4 has two pairs of amoraim and was not silently assigned to Yohanan vs Resh Lakish. In חד אמר cases the report quotes the continuation and does not assign opinions by name order. Yerushalmi Ketubot 6:1:2 is especially important: an initial attribution is replaced by a later report. Automatic warnings for inversions/retractions may concern nearby material; verify them manually.

`verify_yochanan_lakish_sources.py` independently reads raw JSON arrays and verifies every selected quotation, address, main index and source hash. UI tests are in `yochanan_lakish_results/verify_report.cjs`; also run the required `rav_shmuel_results/verify_report.cjs`. These checks do not prove classification accuracy or completeness. Original corpora and earlier reports were not modified.

Recommended next pass: review full sugyot tractate by tractate, then all unresolved candidates/proximity windows, especially dialogue forms and Yerushalmi implicit opinions. Separate practical rulings, explanations, derivations and resolved objections; link parallel topics without deleting occurrences.

Repository visibility: the user decided on 2026-11-23 that the repository should be PUBLIC, and it is now public. Do not make it private unless the user asks.

### Yohanan–Resh Lakish review — 2026-11-23

All checks passed, and a full rebuild reproduced every output byte-for-byte. A random sample of 14 entries, the Shabbat 71b–72a series and the 23 entries that depend only on ר״ל were read; all are Rabbi Yohanan vs Resh Lakish.

Independent recall check: a strict pattern (רבי יוחנן אמר … ריש לקיש אמר, either order, within one segment) hit 270 segments; 263 were already main entries. Of the other 7, two were clear misses and are now added: Eruvin 8b:11 (entry ID 562) and Menachot 54a:8 (ID 563). In both, the two amoraim stand in opposing groups with a plural verb (אמרו / אמרי), which the scanner's singular-verb patterns do not match. They are added in `build_yochanan_lakish_report.py` with fixed IDs, so all 561 earlier entries kept their IDs and content; the two new entries appear in tractate order but carry the higher IDs. The rest: Yerushalmi Kiddushin 1:4:10 (agreement) and Sotah 5:6:2 (unrelated) are correctly excluded. Borderline, left unselected: Yerushalmi Bava Metzia 10:6:2 (possibly complementary rulings), Berakhot 1:1:25 (different aggadic explanations), and Sanhedrin 7:9:8 (both are printed as saying כמחלוקת, probably a textual corruption).

Known scanner gap: רבי יוחנן הסנדלר (a tanna) is not excluded. It appears only in 5 broad proximity windows (Ketubot 58b, Kiddushin 63a, Yerushalmi Ketubot 5:5:2–3, Nedarim 11:4:2), none selected. It was not fixed in the scanner, because that would renumber `broad_candidates.json`, which the 17 supplemental selections address by index. Fix both together if the scanner is changed.

## Previous research: Abaye and Rava

The latest user request was to find all disputes between אביי and רבא across Talmud. Read `abaye_rava_results/abaye_rava_index.json` and `abaye_rava_results/README.md` for this task. The scan covered 76 tractates and 94,045 segments; the first-pass selected report has **498 source-location entries in 36 Bavli tractates**. This is not a count of unique topics or a certified exhaustive list.

Raw retrieval: 1,052 declaration/joint candidates, plus 2,455 overlapping proximity windows. Manual excerpt decisions selected 565 declaration/joint candidates; 3 broad dialogue excerpts were added. Quotations were reviewed partly through shortened views. Complete sugyot have NOT all been reviewed. Unselected candidates must not automatically be treated as rejected disputes. See stable candidate keys and reasons in `review_decisions.json` and `supplemental_decisions.json`.

No Yerushalmi pair was found by the implemented patterns. The patterns can miss distant, implicit, variant-name and dialogue-form disputes. The scanner also has an incomplete exclusion of names such as בר רבא; several known false identities were excluded during review. Preserve the frozen snapshot IDs if editing decisions. Do not silently equate רבא and רבה. Rosh Hashanah 18a has an attribution warning in the selected index.

Validation: `python -X utf8 verify_abaye_rava_sources.py` checks retained text against the normalized original source, addresses, source hashes, and six coverage probes. `node abaye_rava_results/verify_report.cjs` checks UI behavior. Neither certifies that a passage is a dispute or that the index is complete. The prior Rav–Shmuel report was not regenerated or changed.

Recommended next work: audit complete Abaye–Rava sugyot tractate by tractate; classify practical disputes vs alternative explanations and proofs; trace retractions and attribution corrections; then review remaining broad windows and deduplicate topics while preserving parallel references.

### Abaye–Rava review — 2026-11-23

An independent check re-read every entry's main segment from the raw `merged.json`; all quotations and daf addresses matched. The full pipeline reran and reproduced every output byte-for-byte. All 19 selected entries whose second speaker appears after 500 characters were read; each has differing Abaye and Rava statements in the same sugya.

Recall gap: the 362 `declaration_pair` candidates marked `not_selected` were only partly reviewed. In a random sample of 25, one was a clear miss: Megillah 8b:13 (review ID 230), where Abaye rejects Rava's derivation and gives his own. It is now selected. Chagigah 22b:10 (ID 178) is borderline: Rava's answer is refuted by the Gemara and Abaye then answers differently. Expect roughly a dozen or more further misses among the unselected declaration pairs; review them before claiming coverage.

## Current request and outcome

The user requested: “אני רוצה שתחפש בכל תלמוד כל מחלוקת בין רב ושמואל ותשמור את זה בקובץ”. The implemented scope was base Bavli and Yerushalmi in the available local Sefaria export. The current deliverable is a searchable Hebrew report plus TXT and JSON, containing 512 source-location entries (509 in the 2026-11-22 snapshot, plus 3 added on 2026-11-23; see "Review corrections" below). Full scholarly completeness has not been established.

## Useful inputs

Read `rav_shmuel_results/rav_shmuel_index.json` first:

- `metadata`: scope, counts, method, and limitations.
- `entries`: `ref`, `he_ref`, `work`, `branch`, `status`, `opening`, `evidence`, `source_units`, `notes`, `source_file`, `json_index`, and `candidate_ids`.
- `source_units`: surrounding source segments with references, quotations, and links. These can contain adjacent unrelated material as context.
- `coverage`: every scanned tractate, including those without selected entries.

Raw retrieval found 1,494 broad windows and 1,384 declaration/joint-mention candidates (1,382 in the original snapshot). Their counts do not represent disputes. The primary index groups selections by source segment. Full quotations and raw candidates are retained for auditing and recall improvement.

## Critical reference issue

The normalized corpus had an observed Bavli reference offset: the opening of Berakhot was labeled `Berakhot 3a:1` rather than `Berakhot 2a:1`. This project instead derives addresses from the original export arrays:

- Bavli: zero-based page-array index `i` maps to daf `i // 2 + 1`, with `a` for even `i`, `b` for odd `i`; segment index + 1.
- Yerushalmi: nested indices + 1 give chapter, halakha, segment. Do not invent a folio mapping.

The source corpus itself was not edited. Check unusual schemas before extending this mapping beyond the current inputs.

## Classification and known limitations

The retrieval searches name proximity and declaration patterns, followed by first-pass reading of excerpts. Some review views were abbreviated, and complete sugyot have not all been read. Selected entries are research leads with source evidence, not individually certified conclusions.

The search scripts have incomplete name-exclusion lists. Some unselected candidates are other amoraim, agreements, transmission chains, or unrelated topics. Conversely, dialogue forms and distant opinions can be missed. Three manually located dialogue/source entries were added in the builder (Sukkah 11a, Sukkah 14a, and Ketubot 77a).

`review_decisions.py` preserves selection decisions; the builder adds further selections and exclusions. `strong.json` came from an exploratory filtering step and is committed because that step is not a standalone maintained script. Do not describe the entire workflow as reproducible from scratch without addressing this gap.

Recommended next work:

1. Audit each selected entry against its complete sugya and record an explicit decision with supporting text.
2. Review excluded and remaining candidates for missed indirect disputes, while filtering names and transmission chains reliably.
3. Add topic labels and separate Rav's view from Shmuel's view only when attribution is established.
4. Group parallel occurrences into unique disputes without losing references or alternative versions.
5. Consolidate scripts into a reproducible pipeline with configurable source paths and explicit review records.

## User's local corpus locations

These paths are context for the original machine, not included repository data:

```text
F:/Sefaria_Corpus_Normalized
F:/Sefaria_Responsa_Normalized
F:/Sefaria_norm
F:/Sefaria-Export-master
F:/TORA/text_extract
```

The current scan uses only the original export's base Talmud files. Commentary and responsa research is a separate extension. An earlier project task extracted Hebrew lesson images into Word documents under `F:/TORA/text_extract/output`; those files are not part of this upload.

## Validation already performed

The report was rendered in a headless browser and visually inspected for Hebrew RTL layout. Node verification exercised rendering, Hebrew search for שמוטת גף, and filtering to the 89 Yerushalmi entries. These checks do not validate completeness or every scholarly classification.

## Review corrections — 2026-11-23

An independent review re-read every entry's segment from the original `merged.json`. All quotations matched, and every reference matched the daf mapping above. All 150 entries of an older, separate Bavli extraction (`F:/Sefaria_Corpus_Normalized/reports/rav_shmuel_bavli_disputes.json`) are present here. That older file's references are one daf too high (the normalized-corpus offset), so do not cite from it.

Changes made:

- `classify_rav_shmuel.py`: the anonymous pattern accepted only space, comma, period, or colon after רב ושמואל, so the semicolon form רב ושמואל; חד אמר was missed. A widened pattern (also semicolon and dash) now finds Gittin 68b:16, Bava Batra 91a:4, and Bava Batra 91b:7. To keep snapshot candidate IDs stable, Bava Batra 91a:4 (ID 864) is upgraded in place from `explicit_mention` to `anonymous`, and the other two are appended as IDs 1383 and 1384. No other candidate record changed.
- `build_rav_shmuel_report.py`: the three IDs are added to `more`. The manual Sukkah/Ketubot entries now use their published IDs (2529–2531) instead of a count-dependent ID. Two invalid escape sequences (future syntax errors) were fixed. Three malformed `</option value=…>` tags had hidden the Bavli, dispute, and reconciled filter options in the HTML report; the tags are fixed.
- `verify_report.cjs`: now also checks the filter-option markup.

`remaining.json` and `supplements.json` were not regenerated, so they do not list IDs 1383–1384; both were selected directly in the builder.

Entries to read in full: Eruvin 12a:8 and Avodah Zarah 57a:5 (Shmuel's view appears only indirectly, through another amora's report).
