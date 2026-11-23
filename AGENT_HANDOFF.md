# Research handoff — updated 2026-11-23

## New active research: Abaye and Rava

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
