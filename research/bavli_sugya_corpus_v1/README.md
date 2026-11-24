# Bavli sugya corpus v1 — bounded provisional pilot

This builds a reproducible source-grounded pilot, **not a completed Bavli corpus or a training-ready dataset**. The inventory covers all37 base tractates in the actual source TOC, in that order. Semantic processing is limited to Berakhot2a–5a and Bava Metzia21a–22b, with adjacent context read. No masechet is complete and no model was trained. Earlier experiments and source indexes are unchanged.

The requested Gemini runtime and schema attachment were unavailable. The user explicitly authorized the current model for provisional pilot annotation and a newly defined provisional schema. These substitutions are recorded, not attributed to Gemini. No paid API calls were made. See SCHEMA_NOTES.md, RUN_LEDGER.md and annotation_manifest.json.

Start with [the QA summary](QA.md), [progress manifest](progress_manifest.json), [mapping review](mapping_review.md), [independent comparison](review/comparison.md), and [reproduction commands](REPRODUCE.md). Each record validates against schema_v1.json. Exact Hebrew/Aramaic strings, including markup, punctuation and whitespace, are retained in segments; derived prose is explicitly editorial.

## Dataset design

- `segments`:215 pilot source units, plus68 clearly separate context-only units in context/segments.jsonl. No source segment is silently rewritten or discarded.
- `sugyot`:29 primary units and6 nested units. Boundaries follow discussion, not page breaks; three primary units are explicitly open at pilot edges. Primary coverage is exactly once per pilot segment; children are not extra independent examples.
- `scholars`:textual name labels with evidence, not a certified authority catalog. Repeated names may refer to different historical people; external identity remains unresolved. Rav, Rabbah, Rava and named patronymics are not collapsed by substring matching.
- `statements`:curated source-unit claims, questions, arguments, narratives and structural markers. Some units remain composite. Direct named authority, transmitter chain, quoted authority and anonymous narrator are distinct fields. Unassigned alternatives retain candidate names without assignment.
- `questions` and `positions`:multiple questions/claims are allowed; statuses preserve assertions, conditions, rejection, reconciliation and uncertainty. Candidate-position lists are **topic inventories, not certified mutually exclusive or comparable answers**. They cannot yet be exported as an ML answer menu.
- `relations`:source-supported argument edges and four within-pilot related-topic links. Related topics do not automatically form one parallel family. No claim of exhaustive graph or corpus-wide parallel detection.
- `review_queue`:open boundary/family/atomic-decomposition and attribution work. Every semantic record is `ai_provisional`, with `ml_eligible=false`.

`annotation_initial.py` and the independently frozen initial BM review preserve first readings. `annotation_completion.py` is a second author pass over previously unrepresented source units. `revisions.json` applies documented corrections without replacing those initial decisions. `compile_annotations.py` serializes them deterministically; it does not make semantic judgments by regex or fabricate missing scholar positions.

## Future use and limits

`examples.py` reconstructs a sugya using the original source strings or retrieves a named scholar label's documented provisional positions with quotations. Missing records mean missing evidence, never negative answers. A reported action, biblical narrative, interpretation or transmitted ruling is not automatically an observed psychological decision.

Before any learned distance, Q–A or scholar-history experiment: finish atomic question/condition extraction; disambiguate entities and transmissions; neutralize candidate alternatives without removing conditions; review full continuations and semantic parallels; form adjudicated source families; then freeze family-level partitions. Do not randomly split these occurrences or related sub-sugyot. No synthetic scholar decision is represented as historical evidence.

The local source edition is Wikisource Talmud Bavli as exported by Sefaria, pinned by file hashes. Source text retains the recorded CC-BY-SA attribution/terms; see SOURCE_ATTRIBUTION.md. Public files contain only the bounded pilot/context evidence, not full corpus copies. Subsequent tractate extraction must use a separate authorized execution budget and the recorded expansion gates.
