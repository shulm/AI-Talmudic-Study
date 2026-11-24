# Execution and limits

Date:2026-11-24. Isolated branch codex/bavli-sugya-corpus-v1, based on PR8 delivery165bd826f02c91894dc9806d5e49af119eb230a5, which contains the preserved PR5 sources. This new directory is the only intended diff. No unrelated work, old results, corpora, IDs or repository visibility were changed.

1. Read assignment, AGENTS.md, AGENT_HANDOFF.md, existing dispute-index metadata, research plan and PR5 results. Located original export and named edition; confirmed the schema attachment was missing.
2. User authorized current-model provisional annotations and a provisional schema. No Gemini execution is claimed.
3. Built37-tractate TOC inventory and extracted215 pilot/68 context segments. Read source sequentially in overlapping batches, preserving page continuations.
4. Separate reviewer read BM20b–23a before seeing the primary annotation and saved its initial decisions. It independently checked11 explicitly addressed amudim/215 segments against live named-version Sefaria responses, plus Wikisource page anchors.
5. Authored128 first-pass claims,29 primary units and6 children. Mechanical validation exposed96 pilot source units without a selected claim. These were not filled by regex or fabricated anonymous decisions: a second manual pass added96 source-unit summaries and7 positions, with structural markers labeled.
6. Separate comparison preserved initial disagreements and recommended C01–C04; subsequent review found paraphrase/status errors C05–C07. Applied corrections only via revisions.json; initial files remain intact. Added context evidence and related-topic links without collapsing source occurrences.
7. Validated exact source text, references, primary coverage, IDs, schema, evidence spans and relationships. Ran eight adversarial corruption tests and an isolated byte-for-byte rebuild. See machine-readable QA/tests/reproduction records for exact final counts and measured rebuild wall time.

Model execution: current interactive Codex session and its separately tasked AI reviewer. Exact API model identifier, sampling settings and per-task token counts are not exposed by this interface; they are recorded as unavailable, not guessed and not zero. Incremental paid API calls0; incremental paid API spend0; no rented compute or training. Source processing is deterministic local Python. API address verification used public read-only HTTP; no paid model provider or credentials were used. No all-Bavli semantic run occurred.

No user execution budget for finishing Berakhot or the other tractates has been authorized. This pilot's semantic completeness/family-comparability gate also remains false. The assignment itself requires both a passed pilot criterion and authorized expansion budget before full-masechet execution. Delivering this checkpoint does not imply either gate has passed.
