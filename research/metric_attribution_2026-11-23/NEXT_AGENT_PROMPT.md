# Next-agent assignment: source inventory and annotation feasibility

## Assignment

Continue the AI Talmudic Study project by completing **P0 and P1 only** of the companion [research plan](RESEARCH_PLAN.md).

The objective is to determine whether the existing source indexes can support a reliable experiment that recovers recorded scholar–position assignments on held-out source families. This assignment prepares source-grounded cases and a feasibility report. It does not assign model training.

Work in the private repository **shulm/AI-Talmudic-Study**. Read the repository's AGENTS.md and AGENT_HANDOFF.md, then RESEARCH_PLAN.md and SOURCE_SNAPSHOT.json in this directory.

## Starting point

The plan was prepared against commit **56c6abee95248b0e872655f18e1ecc147dc5965b**.

At that revision:

- Rav–Shmuel has 512 indexed source locations: 423 Bavli and 89 Yerushalmi.
- Abaye–Rava has 498 indexed source locations in Bavli.
- These counts are research leads, not verified independent disputes.
- Exact primary-reference overlap exists at Berakhot 44b:22 and Sukkah 18b:3. This is not a full overlap audit.

The immediate annotation pilot is Rav–Shmuel in Bavli. Inventory the Abaye–Rava files and inspect possible cross-inventory source overlap, but do not use their model results or attribution patterns to design the eventual prediction method. Abaye–Rava is reserved for later supervised replication.

## 1. Establish the working snapshot

1. Inspect current repository status and branch state.
2. Compare the current source-index hashes with SOURCE_SNAPSHOT.json.
3. If sources changed, record the differences and preserve both identities. Do not silently mix revisions.
4. Create an isolated branch for derived pilot work.
5. Read the JSON indexes directly. Do not import or run the historical builders/search modules merely to obtain an inventory; some have import-time writes.
6. Preserve the source corpora, published index IDs, existing reports, and repository visibility.

The original local corpus paths in the handoff describe the owner's machine. Check availability rather than assuming those paths exist here.

## 2. Produce a source inventory and initial family map

Separate:

- a source occurrence;
- an atomic question with its candidate positions;
- a family of linked occurrences or cases.

Propose groups using canonical references, repeated text, parallels, relevant continuations, and overlapping answer-bearing context. Preserve the evidence for each merge. Shared vocabulary or topic alone does not establish a common source family.

Detect likely cross-pair overlaps. Do not conclude that the two exact address matches exhaust them.

The map may be provisional. Mark unresolved relationships and exclude uncertain boundaries from a purportedly independent test partition. Do not invent a count of unique disputes.

## 3. Select 30 attempted pilot families

Use Rav–Shmuel Bavli records.

Aim for coverage across up to three manageable strata, initially considering:

- civil/property questions;
- Shabbat/festival questions;
- prayer/blessing questions.

Check available inventory and freeze the stratum definition before drawing the sample. Use seed **20261123**, record the sorting and selection procedure, and sample independently of which scholar holds which position.

Select 30 distinct candidate source families. If later reading merges selected families, document the merge and the next deterministic replacement. Retain every attempted candidate and exclusion in the ledger.

The goal is 30 attempted families, not 30 artificially completed labels.

## 4. Audit each selected family

Read enough of the actual discussion to establish:

- the precise question;
- the conditions;
- the two candidate positions;
- the scholar identities and attribution;
- whether the difference remains, is qualified, is reconciled, or is rejected;
- whether another passage or version affects the assignment.

If committed excerpts are insufficient, use an available original corpus or a targeted source lookup. Record edition/version differences. If needed context cannot be obtained, retain a pending record with the exact missing reference and reason.

Follow the repository's attribution rules, particularly anonymous alternatives, reversals, conclusions established in continuation, and longer names containing Rav. In cross-inventory work, distinguish Rava from Rabbah.

A source-address or quotation match does not certify the scholarly interpretation.

## 5. Prepare evidence and model-input views

For each usable atomic case, write the fields required by section 4 of the plan.

The **evidence view** contains exact sources, names, assignment, discussion status, and review notes.

The **prediction view** contains only a neutral Hebrew question, required conditions, and two neutral alternatives. It must not expose the answer through names, transmission chains, source locations, candidate order, or an explanation derived from the true assignment.

Keep candidate IDs stable and presentation order separate. Do not attach A/B labels to the candidate text itself.

Record whether each reasoning statement is explicit in the source, from a named commentary, or an annotator's inference. Do not turn an inferred explanation into source fact.

Retain cases that fail eligibility with specific reasons. Preserve alternative explanations/proofs and unresolved attributions in appropriate non-primary categories.

## 6. Review independently and preserve uncertainty

Arrange an independent second reading of the attempted families where available. Preserve both initial decisions before reconciliation.

Record review_level explicitly as ai_single, ai_independent_double, human_reviewed, or human_independent_double. Independent AI passes can identify problems and support a provisional benchmark build and engineering experiments; carry that qualification into results. Do not claim expert review when no knowledgeable human reader participated. Expert-validated confirmation later requires two independent knowledgeable human readings per confirmation record. Human-review availability does not prevent completing this assignment's useful preparation.

Report initial agreement on:

- eligibility;
- question and conditions;
- candidate-position alignment;
- named assignment among jointly eligible cases.

Resolve disagreements from evidence. If unresolved, leave the record pending or excluded. Do not manufacture consensus.

## 7. Deliverables

Create derived outputs under a pilot subdirectory of this research directory. Suggested files:

- INVENTORY_REPORT.md
- source_manifest.json
- occurrence_family_map.jsonl
- family_relationships.jsonl
- cross_inventory_overlap.jsonl
- pilot_selection.json
- attempted_families.jsonl
- evidence_records.jsonl
- prediction_inputs.jsonl
- review_disagreements.jsonl
- PILOT_FEASIBILITY_REPORT.md
- NEXT_HANDOFF.md

Use a small documented schema. If a file is legitimately empty, explain why. Never fill it with invented findings.

Implement only lightweight read-only inventory, schema, selection, and consistency helpers needed for these outputs. Keep script imports side-effect free. Validate meaningful invariants: unique IDs, valid links between records, source provenance, family membership, candidate consistency, and absence of obvious names/addresses in prediction inputs. Automated checks supplement source reading.

The report must include:

- attempted and usable family counts;
- included types and subject coverage;
- exclusions by reason;
- initial review agreement and unresolved cases;
- context availability;
- known grouping/overlap limitations;
- whether the operational feasibility gate is met;
- the exact branch, commit, and reproducible commands;
- a realistic next task based on the observed yield.

## 8. Completion decision

Use one of:

- **READY_FOR_BENCHMARK_BUILD:** enough source-grounded cases, clear grouping, usable inputs, and the specified review status.
- **REVISE_ANNOTATION:** eligibility, attribution, or input construction needs revision.
- **PROVISIONAL_PENDING_REVIEW:** useful preparation is complete, but independent knowledgeable review or necessary source context remains outstanding.

The plan's operational target is at least 20 usable families from 30 attempted, with resolved attribution for each usable case and at least 90% initial assignment agreement among jointly eligible cases where independent review was possible. Explain the denominators. These thresholds are workflow choices, not proof of annotation correctness.

If context or review is unavailable, complete all useful preparation and document the precise gap. Do not leave an inventory or source manifest unfinished merely because the later scholarly gate is pending.

## 9. Scope endpoint

Stop this assignment after P0–P1 and its feasibility handoff. Do not download encoder weights, generate embeddings, fit models, score a confirmation set, start cloud compute, or incur paid API charges under this assignment.

Save the work on the research branch, open or update a draft PR, and summarize source-backed findings and remaining uncertainty. Do not merge unrelated research, regenerate the published indexes, or describe planned experiments as completed.

The next assignment will be selected from the actual P1 evidence. The current endpoint is a reviewable data-feasibility package.
