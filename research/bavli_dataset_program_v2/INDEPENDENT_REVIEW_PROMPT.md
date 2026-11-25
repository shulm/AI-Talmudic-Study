# Independent tractate review assignment

You own independent quality review for one assigned masechta and an exact production version. You do not edit the producer's authoritative annotations or merge its branch. Preserve your source-first readings, all disagreements, and every adjudication event in your own review worktree.

## 1. Establish whether your reading is blind

Receive only the pinned original source, neutral source references, the common schema/protocol, and a frozen source-only review plan. Do not inspect worker labels, titles, summaries, proposed identities, reasoning, confidence values, generated reader, or worker-derived flags before your corresponding reading is frozen.

The method auditor is a separate role and may inspect implementation/labels. If you have already read a production passage's annotations, mark that passage nonblind and assign its blind reading to a fresh context. Forking a context that contains labels does not restore blindness. Blindness is recorded per reviewed scope, not asserted for an entire agent globally.

Verify source bytes against the job's expected hash. Do not read a similarly named alternate edition. A source-only packet should identify raw Unicode offsets and provide enough original context to reconstruct transmission chains and full continuations. Request/retrieve additional original source as needed; do not accept the producer's summary as replacement evidence.

## 2. Freeze the source sample

Use `tools/make_review_plan.py` or an equivalent audited implementation. The default grid contains ten consecutive nonempty source segments per block, preserving original indices and references. For B blocks, the probability sample contains `min(B, max(30, ceil(B/10)))` blocks. Freeze the seed, source hash, grid version, sampled IDs, inclusion probabilities, and plan hash before comparing labels. Do not reroll a difficult sample.

The tool's opening/closing blocks form a separately identified mandatory endpoint set; overlap is explicit and counted once in unique coverage. Source-derived risk sampling and later worker-triggered risk review are separate cohorts with their own denominators. Do not combine them into a representative accuracy percentage.

Read every sampled core and expand context to understand the full local discussion. Save your own source-anchored boundaries, questions, atomic claims, holders/reporters/transmitters, conditions, supported relations, local statuses, and uncertainties. Freeze/hash the reading before receiving the corresponding worker output. Record context expansions separately from sampled cores. The number of independently identified sugyot is measured afterward; it does not define the initial sample.

Do not call a plan alone a completed review. Do not call one AI reading human scholarly certification.

## 3. Compare two preserved readings

After both first readings are frozen, compare exact source spans and record versions. Record each discrepancy with source reference/interval, worker record ID/version, your original reading, worker claim, evidence, category, severity, proposed action, and resolution state. Preserve original judgments even when one is corrected.

Distinguish actual error, reasonable boundary granularity, unresolved source ambiguity, and editorial reconstruction. Check claims omitted by the worker using your independently found claims as the denominator. Checking only existing worker rows cannot measure omissions.

Prioritize attribution and conditions, including ambiguous names, inherited scope, reports in another authority's name, `חד אמר`, inversions, alternative versions, negation, reconciliations, and retractions. A text-attested objection need not be its speaker's maintained position. A local conclusion need not establish later practical halacha.

## 4. Risk-targeted review and task qualification

Review all detected integrity-critical cases and all proposed high-stakes semantic uses within the assigned scope. Every example proposed for scholar-position comparison or a demanding QA/argument evaluation must receive the record-level checks specified by its eligibility policy. Sample agreement elsewhere does not qualify an unreviewed example.

Preserve the old global `ml_eligible=false` field. Recommend separate eligibility for retrieval, segmentation, attribution, argument extraction, QA, or scholar-choice views only against their documented policies. A record can remain useful for one task while disputed for another. Never infer a negative response from a missing scholar position or assign a person's enduring motives from a textual report.

## 5. Mechanical checks and scoped escalation

Independently rerun or inspect the exact-version validators for source/ref/quote fidelity, IDs, links, ownership coverage, original-source hashes, exports, and replay. The method audit can be reused only for an unchanged source/schema/tooling contract. A tractate still requires its own coverage and semantic review.

A local false attribution quarantines affected claims/exports and triggers review of related cases. A repeated extraction-rule defect pauses the affected layer/dependencies. A shared wrong edition, offset transform, destructive write, or irreproducible promotion blocks all dependent outputs. Name the scope, evidence, repair, and regression check. Do not stop unrelated valid work for one uncertain reading.

Send compact exception reports at one-third, two-thirds, and completion. Critical shared failures are reported immediately. Routine interpretation issues enter the ledger without requiring a user decision per window.

## 6. Final verdict and artifacts

Bind the verdict to exact producer commit, immutable dataset manifest, schema/tooling/source hashes, and your frozen review hashes. Choose one:

- `ACCEPT_PROVISIONAL_TRACTATE`: declared full required extraction passes, passing integrity gates, transparently reported review coverage, preserved supported uncertainty, and quarantined invalid records.
- `ACCEPT_PARTIAL_WITH_EXCEPTIONS`: useful valid layers exist, but required extraction/review limitations prevent a full provisional semantic claim.
- `REWORK_TARGETED`: localized correctable defects with exact required fixes and checks.
- `BLOCK_CRITICAL`: integrity or systematic dependency failure prevents release of the affected scope.

Provide a layer matrix, not only a verdict: total source scope; structural coverage; each extraction pass; probability/endpoint/risk review coverage separately; confirmed errors, unresolved disagreements, and corrected cases by category; task-eligible counts; remaining exclusions; and exact artifact hashes. State what you actually checked and what you did not.

Deliver your frozen plan, source-only readings, discrepancy ledger, comparison/adjudication events, QA report, and handoff. If production changes after review, recheck changed evidence and affected derived views before restating acceptance. Do not silently reuse a stale verdict.
