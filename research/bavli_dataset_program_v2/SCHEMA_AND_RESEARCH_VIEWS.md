# Schema evolution and reusable research views

**Design version:** 2.0.0-design, 2026-11-25  
**Status:** Implementation target. This document does not implement a new schema, migrate records, certify annotations, or enable training exports.

## 1. Objective and inspected baseline

Build a source-anchored corpus that supports several research questions. Comparable scholar positions are one derived view of that corpus. Narrative, anonymous discussion, unresolved attribution, and questions without comparable alternatives remain useful core material.

This design was checked against the materialized PR #10 snapshot of:

- `research/bavli_sugya_corpus_v1/SCHEMA_NOTES.md`
- `research/bavli_sugya_corpus_v1/schema_v1.json`
- `research/bavli_sugya_corpus_v1/validate.py`
- `research/bavli_sugya_corpus_v1/pipeline.py`
- `research/bavli_sugya_corpus_v1/README.md`

The inspected contract is schema `1.0.0`, with strict property lists. Its eight tables are `segments`, `sugyot`, `scholars`, `statements`, `questions`, `positions`, `relations`, and `review_queue`. Semantic records require `review_status=ai_provisional` and `ml_eligible=false`. These legacy fields remain unchanged.

Existing protections should be retained: exact raw source strings; separate source and text hashes; Python Unicode code-point, half-open evidence offsets; retained authoring keys; provisional question candidates; distinct speaker/authority/transmitter fields; and explicit unresolved work.

### Baseline constraints that require deliberate evolution

| Inspected v1 behavior | Consequence | Target treatment |
| --- | --- | --- |
| Segment scope is restricted to `pilot` or `context_only`; pipeline and validator use `PILOTS` | Full-tractate production cannot honestly be enabled by changing a README | Version the production schema, driver, manifests, and coverage validator |
| Sugya completeness is fixed to `selected_claims_only` | The current record cannot claim complete extraction | Keep the original record; add explicit per-layer coverage and migrate production records |
| Statements are broad discourse units, sometimes composite | A statement count is not an atomic-claim count | Preserve statements as legacy discourse units; add utterances and claims with explicit links |
| Every position requires a question and a statement | A standalone attributed assertion does not fit without inventing a question | Allow question-independent claims and positions in schema 2; never fabricate a question for compatibility |
| Primary ownership is exactly once per entire segment | Semantic boundaries inside a source segment cannot be represented faithfully | Introduce interval ownership through an explicit schema 2 migration |
| Relation endpoints are statements, except `related_topic` between sugyot | Rich typed graphs require different endpoint rules | Add validated endpoint signatures and source evidence in schema 2 |
| Scholar identity is `textual_label_only_person_disambiguation_pending` | A textual name is not a certified historical entity | Preserve mentions; resolve identity through evidence-bearing attribution and entity-link records |
| Narrator is the constant `anonymous_talmudic_redactor` | The field is textual framing, not identified historical authorship | Preserve its documented v1 meaning; use explicit textual-voice categories in new records |
| Candidate positions are topic inventories and family IDs are provisional scaffolding | Neither answer comparability nor split independence has been established | Independently qualify these properties in task-specific derived views |

## 2. Migration policy: sidecars first, schema 2 where necessary

Do not add undeclared fields to strict v1 rows. An additive preparation stage may introduce independently versioned sidecar tables keyed by existing record IDs and record hashes:

- `runs.jsonl`
- `evidence_spans.jsonl`
- `layer_coverage.jsonl`
- `field_assertions.jsonl`
- `field_reviews.jsonl`
- `lineage_events.jsonl`
- `task_eligibility.jsonl`

These sidecars can record provenance, review, coverage, and eligibility without pretending that v1 changed. New utterance/claim proposals may likewise be stored under a separately declared proposal schema. They are not accepted schema 2 production data until migration and validation exist.

Full production requires an explicit schema 2 migration for changed meanings or invariants, including full-tractate scope, within-segment primary ownership, question-independent positions, new endpoint types, and expanded attribution structures. The implementation must supply:

1. A checked-in target JSON Schema, migration program, and versioned validation rules.
2. A manifest identifying the exact original source and v1 dataset hashes.
3. A mapping from old IDs and versions to new records, with `equivalent`, `split`, `merged`, `superseded`, or `unmapped` relationships and reasons.
4. Preserved original records, source evidence, first model proposals, and corrections.
5. A compatibility export and an explicit loss report for target concepts that v1 cannot represent.
6. Deterministic replay of the migration and export from the same pinned inputs.

Do not label a coarse legacy container as an exact schema 2 sugya merely to obtain a lossless-looking export. Do not create fake questions, identities, or candidate answers to satisfy legacy required fields.

Existing semantic `ml_eligible=false` values remain false. A separate task-eligibility record is the only way to qualify a new research view; it does not retrospectively certify the original pilot.

## 3. Independent state dimensions

Use the following exact vocabularies in new coverage and qualification contracts. Avoid introducing near-synonymous alternatives in individual worker outputs.

| Dimension | Allowed values | Meaning |
| --- | --- | --- |
| `extraction_state` | `not_started`, `in_progress`, `completed` | Whether the declared extraction pass ran over its stated source scope |
| `extraction_result` | `records_found`, `none_found_after_pass`, `abstained_ambiguous`, `not_applicable`, `null` | The outcome of a completed pass, or no final outcome yet |
| `review_state` | `unreviewed`, `independent_ai_agreement`, `disputed`, `adjudicated_ai`, `human_reviewed` | What review actually occurred for the specified fields and record version |
| `release_state` | `valid`, `quarantined`, `superseded` | Whether this record version passes release-integrity requirements |

Enforce `extraction_result=null` if and only if `extraction_state` is not `completed`. A completed pass must have one non-null result. If a coarse scope contains both extracted findings and abstentions, use `records_found` for that scope and preserve the abstentions in child coverage records and the unresolved ledger. Do not hide them in an aggregate success value.

`completed` means the declared pass was performed; it does not prove that no claim was missed. `none_found_after_pass` requires a logged pass over the stated source scope. `not_applicable` requires a layer-specific rationale. `abstained_ambiguous` records a completed attempt with unresolved interpretation; it does not create an eligible answer or resolve an identity.

`independent_ai_agreement` requires a separately frozen source-based reading before exposure to the compared labels. A reviewer who saw the worker's answer first cannot claim this state. `adjudicated_ai` requires an adjudication record preserving both earlier readings and the reason for resolution. `human_reviewed` requires actual human review evidence and its scope; it must never be inferred from AI confidence or agreement.

`valid` means the record version satisfies declared integrity gates. It does not mean its interpretation is scholarly certainty. A disputed but accurately represented interpretation may remain valid with restricted task eligibility. Corrupted source anchors or unsupported exact quotations require quarantine.

Review and qualification are version-specific and field-specific. Changing a reviewed field invalidates its prior qualification until the changed evidence is checked. A valid attribution review does not automatically review the title, conditions, argument edges, or all other fields of the same record.

## 4. Required core layers and source coverage

Every tractate job must maintain coverage for all core layers. It is acceptable for a completed pass to find no question or named position in a passage. It is not acceptable to omit that passage from the denominator.

| Core layer | Main objects | Required content |
| --- | --- | --- |
| Source | Editions, source snapshots, source segments, evidence spans | Exact original strings, refs, indices, edition/version, hashes, attribution/license provenance, interval convention |
| Structure | Primary sugyot, nested sugyot, continuations, discourse units | Source ownership, ordered evidence, open boundaries, material type, titles/summaries as editorial fields |
| Utterances | Source-attested discourse units | Exact spans, textual voice, quoted context, discourse role, composition status |
| Claims | Propositions expressed by utterances | Faithful normalized proposition, conditions, scope, assertion mode, supporting spans, uncertainty |
| Attributions | Mentions, identity candidates, role/scope links | Speaker, position holder, transmitter, quoted authority, collective or anonymous voice; evidence for every resolution |
| Questions | Explicit questions and editorial reconstructions | Origin, exact supporting evidence, formulation, premises/conditions, links to answers when supported |
| Positions | Holder–claim relations in context | Holder or unresolved candidates, proposition, conditions, local status, transmission and optional question link |
| Edges | Directed discourse and argument relations | Typed endpoints, relation type, exact evidence, source-explicit/editorial distinction, review and local status |

Each `layer_coverage` record should identify the tractate, immutable source anchor or anchor set, layer, pass/run, extraction state/result, produced record IDs, explicit abstentions, and coverage-policy version. Source intervals and records must reconcile to the full pinned inventory, with context-only evidence reported separately.

Report at least three distinct denominators: source inventory units, source scope visited by each pass, and produced semantic records. A count of statements cannot substitute for a count of source passages read. Sampled review denominators are separate again.

### Source anchors and normalization

Preserve the existing evidence convention: `start_char` and `end_char` are Python Unicode code-point indices into the exact raw segment, with an exclusive end. Validate the literal slice against the recorded quote and source hashes. A multi-segment assertion uses an ordered list of such spans.

HTML removal, Unicode normalization, tokenization, and display formatting must not overwrite source strings. If normalized text is stored for search or modeling, record the transformation version and retain a mapping to original spans. An offset into normalized display text cannot be passed off as an offset into the raw source.

Source IDs are anchors, not semantic labels. Preserve the existing source IDs and enforce source-hash agreement. A different source snapshot or edition requires an explicit version and alignment policy; never retain old evidence qualification after source bytes change.

### Primary ownership inside segments

Schema 2 may partition a nonempty source segment into ordered, nonoverlapping half-open intervals whose union covers its raw string. Each interval has exactly one primary owner. Child sugyot and quoted evidence may overlap their parent by design; they do not create additional primary coverage.

The partition includes otherwise unassigned punctuation, whitespace, and markup. Empty source segments stay in the source inventory and have an explicit empty-unit accounting rule; they cannot supply nonempty quotation evidence. Report content and empty-unit counts without quietly dropping either from inventory reconciliation.

Implement and test interval coverage before using it for production. A compatibility mapping may retain coarse v1 segment ownership, but must disclose where that mapping loses semantic boundary precision.

## 5. Semantic objects and field-level provenance

### Utterance, claim, and position are distinct

An utterance is a piece of source discourse. A claim is a proposition it expresses. A position links a holder to a claim in a particular context. One utterance may express several claims; several utterances may express the same claim; attribution may remain unresolved. Repeated occurrences remain distinct evidence records.

Claims must distinguish asserted, hypothetical, queried, challenged, rejected, retracted, conditional, or reconciled uses as supported by local evidence. A maintained objection and its rejected target are separate objects with separate statuses. Later anonymous reasoning must not automatically become a named scholar's stated reasoning.

### Attribution and identity

Represent name mentions separately from resolved people. Store the surface form, source span, proposed canonical ID if any, candidate alternatives, role, scope, and the evidence supporting the link. A textual alias is not sufficient evidence that two occurrences denote the same historical person.

Workers propose local links; a designated reconciler controls the global entity registry. Preserve unresolved alternatives. Do not resolve a holder through proximity alone, or assign an anonymous statement because a familiar name occurred nearby.

Transmission chains should preserve order and quotation depth when supported. A transmitter is not automatically the holder of the transmitted position. A collective voice or anonymous voice does not need an invented personal identity.

### Questions and alternatives

Retain explicit questions, editorially reconstructed questions, open questions, and questions without a validated answer set. Record whether a candidate list is a topic inventory, a partial answer set, or a reviewed comparable alternative set. These are different concepts.

Question comparability requires matching premises, conditions, scope, and the decision being asked about. A contradiction, interpretation, qualification, and final answer are not interchangeable alternatives. A missing holder response is missing evidence, not a negative example.

### Argument edges

The target edge registry should specify allowed source and target object types for each relation, including proof/support, objection, answer, qualification, distinction, analogy, quotation, correction/retraction, local resolution, and unresolved outcome. Extend the registry centrally and version it; workers must not invent inconsistent free-form relations independently.

An edge needs evidence for the relation, not merely quotations proving that both endpoint statements exist. Record who presents the reasoning only where the text supports that attribution. Keep source-explicit structure separate from editorial reconstruction. A local discourse resolution does not automatically establish a later practical ruling.

### Field assertions and reviews

For each substantive field, store its record ID/version, field path, value hash, origin, supporting spans or external source IDs, producing run, and review references. Separate literal quotations, source-based paraphrases, editorial inferences, and externally sourced enrichment.

Titles, summaries, topic labels, translated phrases, and inferred premises also require origin information. An exact source citation does not by itself prove that a generated paraphrase or inference is correct.

Use qualitative uncertainty and explicit alternatives where appropriate. A model's self-reported confidence is not a measured probability of correctness unless a separate calibration study establishes that interpretation.

## 6. Optional enrichment: useful, independently qualified, nonblocking

Topics, terminology, commentary links, and chronology belong in separately versioned enrichment layers. They must have their own evidence, coverage, run provenance, and review state. An uncompleted enrichment pass must never block a complete, valid core tractate release.

| Enrichment | Useful contents | Limits |
| --- | --- | --- |
| Topics | Coarse controlled vocabulary, source-grounded open tags, distinctions between question/topic/argument method | A shared topic does not establish the same question or evidence family |
| Terms | Surface forms, abbreviations, contextual senses, supported lemma/gloss proposals | Avoid forcing one sense across different contexts; cite external lexicons and their terms of use |
| Commentary links | Exact external work/version/ref, link type, cited explanation, disagreement with other readings | Commentary is a separate evidence layer; it must not silently replace the primary source |
| Chronology | Cited chronology or biographical metadata and uncertainty | Do not infer dates or identity from model memory alone; disagreement remains represented |
| Parallel passages | Same report, quotation, possible parallel, related discussion, cross-edition alignment | Preserve every occurrence and distinguish identity from thematic similarity |

Translations, morphology, embeddings, and reader/search indexes may be additional generated layers. Keep model/version and input hashes. None supplies independent evidence for a claim solely because it agrees with another generated layer.

## 7. Research views and task-specific eligibility

Research views are generated from the authoritative normalized records and pinned qualification policies. They are not separate editable corpora. Each view names the exact source release, schema versions, field-review versions, eligibility policy, and exclusions.

| Research view | Inputs/labels | Qualification needed | Main leakage concern |
| --- | --- | --- | --- |
| Citation retrieval and source-grounded QA | Query, source passages, supported answer/citations | Source integrity and task-appropriate answer/evidence review | Duplicate passages or parallel answers crossing partitions |
| Sugya segmentation and discourse parsing | Source spans, boundary/role labels | Reviewed structure and boundary conventions | Nearby overlapping windows or nested units split across train/test |
| Argument extraction | Claims, relations, supporting spans | Reviewed endpoint meaning, conditions, and edge evidence | Model-generated summaries or rationales exposing evaluation labels |
| Speaker/authority attribution | Source context, mentions, role and identity links | Resolved target identity and reviewed speech scope | Names, aliases, titles, quoted continuations, or registry metadata revealing the target |
| Transmission analysis | Ordered authority/transmitter relationships | Reviewed role distinctions and quoted scope | Repeated copies treated as independent observations |
| Parallel passage retrieval | Occurrences and typed parallel links | Independently qualified positive/negative relation definitions | Exact duplicates or cross-edition counterparts straddling splits |
| Uncertainty and correction analysis | Initial proposals, disputes, adjudications, evidence | Preserved independent readings and exact revision history | Testing on corrections already visible in prompts or retrieval |
| Qualified position/choice modeling | Comparable question, conditions, holder, supported position | Reviewed comparability, attribution, conditions, source families, input cutoff | Answer text, later conclusions, paraphrases, or same-report copies in inputs |

Eligibility records must include `task_id`, policy version, source release, record IDs and versions, field dependencies, eligibility boolean, reasons, and the evidence/review versions that justify the decision. Eligibility can be revoked or superseded after a correction. It is never inferred from tractate completion alone.

Different tasks may legitimately qualify different records. An unresolved speaker can prevent attribution training while leaving a source passage usable for citation retrieval. Narrative remains valid corpus material even if it supplies no comparable decision.

## 8. Split and leakage policy

Create splits only after the task definition and eligible record population are frozen. Each split manifest must specify input construction, labels, grouping relation types, generation version, and exact members.

1. Preserve occurrence identity separately from report identity. Repeated quotations or versions of the same report are not automatically independent observations.
2. Group verified same-report occurrences, near duplicates, and cross-edition counterparts according to the task. Keep overlapping source windows and nested units together where their overlap reveals labels.
3. Do not automatically union every related-topic edge into a family. Report component sizes and inspect unexpectedly large components.
4. Distinguish confirmed parallel links from candidate links. Unresolved duplicate risk can require a conservative grouping or exclusion for a particular benchmark.
5. Define the prediction-time source cutoff. If predicting a later answer, do not include the answer, its later discussion, a revealing title, an editorial summary, a rationale, or a retrieved parallel that discloses it.
6. Audit all input channels, including metadata, aliases, cached embeddings, generated translations, retrieval indexes, and examples embedded in prompts. Removing one answer field is insufficient.
7. Keep calibration, threshold selection, and adjudication policy development separate from held-out evaluation. Version any changed benchmark.
8. Report detectable within-corpus leakage and acknowledge unknown model pretraining exposure. A family split cannot prove that a foundation model has never seen the underlying source.

An identity-prediction task and a position-prediction task may require different masking. Do not remove a conditioning variable that the task intentionally supplies, and do not retain the variable the task asks the model to predict.

## 9. Interpretation and release limits

The corpus stores text-attested material, supported interpretations, uncertainty, and review history. It can support carefully defined comparisons of positions or reasoning patterns. It does not, by itself, establish psychological traits, hidden motives, stable personal preferences, historical authorship of anonymous material, or causal explanations of a person's decisions.

AI agreement is a review outcome. It is not expert scholarly certification. Multiple occurrences are not independent corroboration when they preserve one report. Missing evidence remains missing. No synthetic scholar decision may be presented as historical evidence.

Publish a per-tractate matrix of core extraction, unresolved cases, field-review coverage, integrity state, and eligible task counts. Optional enrichment gets separate columns. Publish unresolved material with precise qualification where licensing permits; do not improve reported quality by silently deleting difficult cases.

Reproducibility means that frozen inputs, proposals, revisions, and deterministic reconciliation reproduce the release. A fresh model call may produce different annotations. Record actual runs and model identifiers where available; never claim execution, token counts, or model identities that were not observed.

## 10. Implementation acceptance checks

Before this target is declared implemented, demonstrate:

- Strict schemas and compatible version handling; no silent extra fields in v1.
- Exact source hash, raw quote, offset, and referential-integrity checks.
- Full-tractate source inventory reconciliation and per-core-layer coverage.
- Interval partition validation and documented empty-source-unit handling for schema 2 ownership.
- A migration of the pinned pilot that preserves originals, IDs or explicit mappings, evidence, and correction lineage.
- Compatibility export losses reported without fabricated records.
- Field-review and task-eligibility invalidation when a dependent field changes.
- Correct exclusion of quarantined or superseded records from qualified views.
- Idempotent replay from frozen proposals and safe recovery from an interrupted promotion.
- A documented example of task-specific qualification and a leakage audit on its generated inputs.

These checks establish the implementation contract and integrity behavior. Semantic review remains a separate measured activity with its own denominator and unresolved findings.
