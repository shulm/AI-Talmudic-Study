# AI Talmudic Study

A private workspace for source-based Talmudic research with AI agents: finding sources, comparing opinions, and preparing Hebrew discussions, conclusions, and lessons.

## Latest results: Rav and Shmuel

The November 22, 2026 snapshot searches the base texts of **37 Bavli and 39 Yerushalmi tractates**, covering **94,045 nonempty source segments** in the local Sefaria export.

- [Searchable Hebrew report](rav_shmuel_results/מחלוקות_רב_ושמואל.html): download and open in a browser; search and filtering work offline. GitHub's file viewer does not run the report.
- [Plain Hebrew text](rav_shmuel_results/מחלוקות_רב_ושמואל.txt): quotations and references for copying or further study.
- [Structured index](rav_shmuel_results/rav_shmuel_index.json): the best entry point for another AI agent.
- [Coverage](rav_shmuel_results/coverage.json): all scanned tractates and source paths.

The index contains **512 source-location entries: 423 Bavli and 89 Yerushalmi**. Of these, 504 are classified as dispute/opinion-difference entries and 8 as differences discussed or reconciled in the sugya. These are **not 512 distinct disputes**. Parallel passages and repetitions remain, and one entry can contain multiple disputes.

**Research status:** this is a first-pass search and excerpt-based classification, not a critically verified exhaustive catalogue. Complete sugyot have not all been reviewed. Indirect disputes may be missing, and classifications need further checking against the full discussion. Do not treat the catalogue as a halachic ruling.

## Start here as an AI agent

Read [AGENTS.md](AGENTS.md), then [the handoff](AGENT_HANDOFF.md). Work from the structured index and preserve source references. The report and JSON include source quotations, so initial review does not require access to the original F: drive.

Suggested first task:

> Read AGENTS.md and AGENT_HANDOFF.md. Audit the Rav–Shmuel index one tractate at a time against the full source text. Distinguish genuine disputes, agreements, alternative attributions, reconciled differences, and unrelated adjacent statements. Preserve exact references and quotations; record corrections and uncertainty. Do not claim exhaustive coverage until the remaining candidates and indirect formulations have been checked.

## Repository contents

| File | Purpose |
|---|---|
| `rav_shmuel_search.py` | Broad search of the local base-text corpus; produces candidate windows and coverage |
| `classify_rav_shmuel.py` | Finds declaration pairs and joint/anonymous opinion formulations |
| `review_supplements.py`, `review_remaining.py`, `review_joint.py` | Produces review views for further filtering |
| `review_decisions.py` | Preserves first-pass inclusion/exclusion decisions using snapshot candidate IDs |
| `build_rav_shmuel_report.py` | Builds the HTML, TXT, and structured index from selected records and original sources |
| `rav_shmuel_results/strong.json` | Preserved intermediate selection from an exploratory filtering step |
| `rav_shmuel_results/candidates.json` | Broad raw search output, **not a list of confirmed disputes** |
| `rav_shmuel_results/classified_candidates.json` | Raw declaration-pair candidates, also not all disputes |
| `rav_shmuel_results/verify_report.cjs` | Checks report rendering logic, Hebrew search, and Yerushalmi filtering |

Other JSON and TXT review files preserve the investigation trail. Candidate IDs refer to this exact snapshot and must not be assumed stable after changing source data or search rules.

## Running locally

Python 3.12 and Node.js were used. The Python scripts use the standard library; the JavaScript verification uses built-in Node modules.

Original source layout:

```text
F:/Sefaria-Export-master/json/Talmud/{Bavli,Yerushalmi}/Seder */*/Hebrew/merged.json
```

To rebuild on another machine, change `ROOT` in `rav_shmuel_search.py` to the corresponding `json/Talmud` directory. Keep the original corpus read-only. Then, with the committed `selected.json` snapshot:

```sh
python -X utf8 build_rav_shmuel_report.py
node rav_shmuel_results/verify_report.cjs
```

The builder imports the search module, which reruns the broad search and rewrites candidate/coverage outputs. Back up or commit changes before rebuilding. Review scripts likewise have side effects through imports. The full exploratory workflow is not yet a single reproducible pipeline: `strong.json` is a committed intermediate artifact, and subsequent inclusion decisions are preserved in code.

## Sources and attribution

Quotations derive from the user's local Sefaria Export Hebrew `merged.json` base texts. Each index entry includes a local source path, zero-based JSON position, canonical reference, and a Sefaria link. Online versions may differ from the local snapshot. Formatting tags and Hebrew vocalization were removed for search/display; source wording was not intentionally rewritten.

The full Sefaria corpus and earlier unrelated document-extraction materials are not included. This repository does not grant a new license to underlying source editions; retain their attribution and consult the relevant edition's terms before redistribution.
