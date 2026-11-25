# Review of the previous corpus handoff

Reviewed 2026-11-25. Scope: all five supplied handoff files; recovered relevant project context; current metadata for PRs #10/#11; and selected byte-verified implementation/schema/manifest files at PR #10's pinned commit. The shared-chat URL exposed only a generic share page in this environment, not its conversation text. No complete new semantic source review was performed.

## Overall assessment

The previous handoff has a strong foundation: named-edition pinning, exact quotes, full continuation, holder/reporter distinctions, retained ambiguity, independent readings, and separate structural/semantic/ML gates. Those protections should remain. The main changes concern throughput, richer research representation, and review design.

## Priority findings and replacements

| Finding | Evidence | Replacement |
| --- | --- | --- |
| Corpus progress remains serialized at the user level | Worker final instruction stops after Berakhot and waits for Shabbat; supplied README repeats this | One coordinator drains a whole-tractate queue; distinct tractates run concurrently |
| Every copied worker prompt could redesign shared infrastructure | Worker section 1 asks its recipient to upgrade the driver/schema | One tooling owner freezes the shared contract; workers own only assigned data |
| Actual code still extracts only two fixed pilots | `pipeline.py`: `PILOTS`, `extract`, CLI `build/show`; `validate.py`: expected set derived from `PILOTS` | Add a parameterized tractate driver, immutable source verification, persistent proposals, safe replay, and per-layer coverage |
| The build path can refresh its own source baseline | `pipeline.py`: `build` calls `inventory`, which hashes current files and writes `source_manifest.json` | Separate explicit source admission from production; production verifies approved hashes and fails on mismatch |
| Blind sample depends partly on producer-created units | Supervisor B and QA sampling specify a pre-label sample of primary sugyot / 10% of producer sugyot | Freeze source-coordinate blocks and inclusion probabilities; independently infer sugyot afterward |
| Method inspection may expose labels before a claimed blind reading | Supervisor immediate instruction says inspect PRs before freezing sample | Separate method auditor, blind reader, and later comparator; mark exposed passages nonblind |
| Exactly one semantic sugya per export segment can be too coarse | Hard coverage gates in worker/supervisor/QA | Preserve segments; support within-segment ownership intervals under explicit schema migration; retain coarse compatibility accounting |
| Extraction and review states are mixed and inconsistent | Worker uses `pending_review` alongside extraction outcomes; QA has a different vocabulary | Orthogonal extraction state/result, review state, release state, and task eligibility |
| Single global ML boolean blocks unrelated useful research views | Candidate comparability/holder/family requirements applied to all semantic records | Preserve old boolean; add separate versioned policies for retrieval, attribution, graph/QA evaluation, and choice modeling |
| Local scholarly uncertainty may halt unrelated work | Supervisor lists unjustified attribution alongside global corruption stops | Quarantine local scope; pause shared dependencies only for shared/systematic defects |
| Replay language can be mistaken for repeatable model generation | Worker incremental/reproducibility requirements | Guarantee deterministic reconstruction from frozen proposals; log fresh model attempts as distinct observations |
| A single global reviewer can become a throughput bottleneck | One worker/one supervisor model | Paired tractate review capacity plus shared infrastructure audit and separate adjudication |

## Richness beyond the original decision task

The corpus should preserve observed discourse, propositions, attribution/transmission, questions, conditions, and argument relations independently. Scholar-choice examples are derived from those records only where the question and alternatives are comparable. Narratives, anonymous reasoning, quoted reports, and unresolved passages remain useful data even when they cannot enter that view.

Add source-grounded topic and terminology layers, typed parallels, commentary links, and provenance for external enrichment. Separate explicit words of the source from editorial explanation and commentary-supported interpretation. Do not make completion of every optional enrichment layer a gate for finishing a tractate's core data.

## Specific inherited checkpoints

- Berakhot has a prefix pilot through 5a:24. B24 begins at 5a:24 and needs its continuation into 5b; preserve its original ID/evidence and record any boundary revision.
- Bava Metzia's pilot is at 21a–22b. It is **not** a processed prefix. A whole-tractate assignment must process 2a onward and the suffix, and reconcile 22b:11–16 with 23a.
- PR #10 and #11 record different editions and incompatible IDs/offsets. Similar segment counts do not establish interchangeable source text.
- Existing pair-specific indexes and behavioral/modeling experiments are separate evidence. Their scores or occurrence counts do not certify the new corpus.

## What this review verified

Live repository metadata showed the repo public and both PRs open drafts at the referenced heads. The PR #10 tree and selected fetched files were checked against their Git blob hashes. Its source and progress manifests support 37 tractates / 81,793 source segments and 215 historical pilot segments. The pilot code/schema limitations above were inspected directly.

The original full source files were not available in this execution workspace. This review did not rerun the original full-source validation, certify all source licenses, compare full PR #11 semantics, or produce new tractate annotations. Historical test/review reports remain historical claims unless explicitly rerun. New tooling validation is recorded separately in `VALIDATION_REPORT.json`.

## Recommended next production result

After the minimal common driver and migration pass their shakedown, the next lead should deliver complete provisional data for the first active tractates, with actual source reading and independent review evidence. Additional plans, access checks, and empty schemas do not count as that delivery. Continue to the queued tractates as capacity allows; give the owner a concise progress matrix and concrete exceptions.
