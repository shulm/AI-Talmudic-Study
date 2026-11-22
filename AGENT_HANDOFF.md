# Research handoff — 2026-11-22

## Current request and outcome

The user requested: “אני רוצה שתחפש בכל תלמוד כל מחלוקת בין רב ושמואל ותשמור את זה בקובץ”. The implemented scope was base Bavli and Yerushalmi in the available local Sefaria export. The current deliverable is a searchable Hebrew report plus TXT and JSON, containing 509 source-location entries. Full scholarly completeness has not been established.

## Useful inputs

Read `rav_shmuel_results/rav_shmuel_index.json` first:

- `metadata`: scope, counts, method, and limitations.
- `entries`: `ref`, `he_ref`, `work`, `branch`, `status`, `opening`, `evidence`, `source_units`, `notes`, `source_file`, `json_index`, and `candidate_ids`.
- `source_units`: surrounding source segments with references, quotations, and links. These can contain adjacent unrelated material as context.
- `coverage`: every scanned tractate, including those without selected entries.

Raw retrieval found 1,494 broad windows and 1,382 declaration/joint-mention candidates. Their counts do not represent disputes. The primary index groups selections by source segment. Full quotations and raw candidates are retained for auditing and recall improvement.

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
