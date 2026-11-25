# Evidence and source notes

Inspection date: 2026-11-25. Links identify the actual material used for this production-design review. Requirements proposed in this package are design decisions unless attributed to a source below.

## Supplied project handoff

The user supplied `README.md`, `01_SUPERVISOR_HANDOFF(1).md`, `02_WORKER_ONE_MASECHTA_PROMPT(1).md`, `03_QA_GATE_AND_COORDINATION(1).md`, and `04_FIRST_JOB_BERAKHOT(1).json`. All five were read. They identify the production base, pilot checkpoints, whole-masechta assignment, current budget boundaries, and review expectations.

The [shared prior conversation](https://chatgpt.com/share/6b072d9a-8198-83eb-a6ce-6714c421d2dc) could not be read as conversation text through the available retrieval routes. Relevant prior project context was recovered separately. Do not describe this review as having read the full shared transcript.

## Current GitHub observations and pinned evidence

- [Repository](https://github.com/shulm/AI-Talmudic-Study): metadata confirmed public visibility on inspection.
- [PR #10](https://github.com/shulm/AI-Talmudic-Study/pull/10): open draft at `ef29310b50575ac2441ce59d0c68d58424f4b823`, head `codex/bavli-sugya-corpus-v1`, base `codex/individual-decision-followup-pr5`.
- [PR #11](https://github.com/shulm/AI-Talmudic-Study/pull/11): open draft at `9a9dfad93675b984b8223ba065732599a973f074`, head `research/bavli-sugya-corpus-v1`, base `main`.
- [Pinned repository instructions](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/AGENTS.md): preserve quotations and source corpora; do not commit full corpus copies; public visibility already chosen.
- [Pinned project handoff](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/AGENT_HANDOFF.md): broader source-index and general decision-function research context. Its historical status paragraphs are not assumed current for other active studies.
- [Corpus README](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/README.md): scope and pilot semantic limitations.
- [Source manifest](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/source_manifest.json): named edition, 37 source files, per-file hashes, TOC order and denominators. File SHA-256: `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`; Git blob SHA: `815f023e4ad42961fa175630a7f86b8b5bd47e73`; size: 63,626 bytes.
- [Progress manifest](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/progress_manifest.json): 151 Berakhot and 64 Bava Metzia pilot segments; zero completed tractates. SHA-256: `a3e1fd409ba1ed43d3f3fd5c98fbf9bdfde66b76c2fe8b57285d3942e15dc602`.
- [Pipeline](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/pipeline.py) and [validator](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/validate.py): pilot-bound execution, source-manifest creation, coverage rules, and semantic completeness limits.
- [Schema](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/schema_v1.json) and [schema notes](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/SCHEMA_NOTES.md): strict pilot contract, Unicode interval convention, broad discourse units, unvalidated answer comparability, and provisional family IDs.
- [Source attribution](https://github.com/shulm/AI-Talmudic-Study/blob/ef29310b50575ac2441ce59d0c68d58424f4b823/research/bavli_sugya_corpus_v1/SOURCE_ATTRIBUTION.md): the export records CC-BY-SA without a numeric version, and preserves a separate current-footer observation. Do not silently substitute a license version.

The selected fetched local files were verified against the corresponding Git blob hashes. This does not constitute verification of the unprovided original source-text bytes or new semantic annotations.

## Official external documentation

- [Sefaria: Copyright and Data Use](https://developers.sefaria.org/docs/usage-of-our-name-and-logo), consulted 2026-11-25. Sefaria distinguishes code, text-version licenses, and links metadata. Its links dataset is described as CC-BY with attribution and change indication.
- [Sefaria: How to Find and Understand Licensing or Copyright Information](https://help.sefaria.org/hc/en-us/articles/18490043237148-How-to-Find-and-Understand-Licensing-or-Copyright-Information), updated July 22, 2026, consulted 2026-11-25. Each language/version has its own rights information; attribution usually credits the original source rather than only the platform.
- [Sefaria versions API documentation](https://developers.sefaria.org/reference/get-versions), consulted 2026-11-25. Version metadata includes title, versionTitle, versionSource, language, status, and license. Metadata lookup does not replace pinning actual source bytes.

These sources support the license/provenance design. They do not prove that any particular full corpus redistribution has completed a rights review. The source versions recorded in the repository remain the controlling inputs for this production program.
