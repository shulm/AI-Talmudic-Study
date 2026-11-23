# AI Talmudic Study

A public workspace for source-based Talmudic research with AI agents: finding sources, comparing opinions, and preparing Hebrew discussions, conclusions, and lessons.

## Latest results: Rabbah and Rav Yosef — November 23, 2026

Scanned **76 tractates / 94,045 nonempty segments**. The first-pass index contains **101 source locations in 27 Bavli tractates**, including one objection resolved by distinguishing cases. These are occurrences, not 101 unique disputes or a certified exhaustive catalogue. No Yerushalmi entry was selected.

- [Searchable Hebrew report](rabbah_yosef_results/מחלוקות_רבה_ורב_יוסף.html)
- [Hebrew quotations and context](rabbah_yosef_results/מחלוקות_רבה_ורב_יוסף.txt)
- [Structured index for another agent](rabbah_yosef_results/rabbah_yosef_index.json)
- [Method, limitations and rebuild commands](rabbah_yosef_results/README.md)

The search distinguishes רבה from רבא. It retains 207 pattern candidates, 477 overlapping proximity windows, and explicit review decisions. Read the attribution and conclusion notes before preparing a lesson.

## Rabbi Yohanan and Resh Lakish — November 23, 2026

Scanned **76 tractates / 94,045 nonempty segments**. The first-pass index contains **563 source locations: 338 Bavli and 225 Yerushalmi, across 71 tractates**. These are source occurrences, not unique-topic counts or a certified exhaustive list.

- [Searchable Hebrew report](yochanan_lakish_results/מחלוקות_רבי_יוחנן_וריש_לקיש.html)
- [Hebrew quotations and context](yochanan_lakish_results/מחלוקות_רבי_יוחנן_וריש_לקיש.txt)
- [Structured index for another agent](yochanan_lakish_results/yochanan_lakish_index.json)
- [Method, limitations and rebuild commands](yochanan_lakish_results/README.md)

Aliases include רבי שמעון בן לקיש, ריש לקיש, בר לקיש, רשב״ל and ר״ל. The pipeline retains 1,409 pattern candidates and 2,109 overlapping proximity windows for further audit. Read the limitations before using the index to prepare a lesson.

## Abaye and Rava — November 23, 2026

The new scan covers the same **76 tractates / 94,045 nonempty segments** of Bavli and Yerushalmi. The selected index has **498 source-location entries in 36 Bavli tractates**, grouped from 568 selected candidate occurrences. These are not 498 distinct disputes: alternative explanations, repeated reasoning, and parallel passages remain.

- [Searchable Hebrew report](abaye_rava_results/מחלוקות_אביי_ורבא.html)
- [Hebrew text with source context](abaye_rava_results/מחלוקות_אביי_ורבא.txt)
- [Structured index for another agent](abaye_rava_results/abaye_rava_index.json)
- [Research procedure and limitations](abaye_rava_results/README.md)

**First-pass excerpt review only.** The scan retrieved 1,052 declaration/joint-mention candidates and 2,455 overlapping name-proximity windows. They are not counts of disputes. No paired candidates were retrieved in Yerushalmi with these patterns; this is not proof of absence. The selected index still needs full-sugya checking and broader recall review.

## Rav and Shmuel

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
