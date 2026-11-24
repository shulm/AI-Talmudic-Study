# Execution prompt: first general decision-function pilot

## Role and assignment

Act as the implementation and research agent for **shulm/AI-Talmudic-Study**. Complete phases **P0–P3** of this directory's [RESEARCH_PLAN.md](RESEARCH_PLAN.md): acquire and audit one existing general human-judgment dataset, build the lab, run the bounded development comparison, freeze the protocol in GitHub, and perform one declared held-out evaluation if the validity checks pass.

The objective is:

$$\widehat P(a\mid q,C(q),H_s),$$

where $q$ is a textual problem, $C(q)$ its available answers, and $H_s$ contains the observed question–answer pairs of a specified decision-maker. Predict an answer from this information. Do not substitute speaker identification, population majority prediction alone, imitation of writing style, or a psychological diagnostic claim.

The primary experiment is **new decision-maker + new item group**, with **16 observed support decisions**. Talmudic source preparation is a later application. Do not build the full sugya corpus under this assignment.

**Communication channel:** https://github.com/shulm/AI-Talmudic-Study/issues/2

All durable instructions, status updates, results, and reviewer responses belong in that issue and its linked draft PR. Chat may point to those records, but must not be their only location.

## 1. Read and establish your starting point

Read, in order:

1. Repository `AGENTS.md` and `AGENT_HANDOFF.md`.
2. This directory's `README.md`, `RESEARCH_PLAN.md`, and `LITERATURE_AND_DATASETS.md`.
3. `GITHUB_WORKFLOW.md`, `SOURCE_SNAPSHOT.json`, and `protocol_template.json`.
4. The coordination issue's latest comments and any linked execution/review PRs.

This continuation explicitly supersedes the modeling objective of historical draft PR #1. Preserve that history and the existing source reports. Current repository instructions record that the repository is public; preserve its visibility.

Inspect current branches and working changes. Create your own isolated execution branch. If the plan PR is still unmerged, branch from its issue-linked commit and open a draft PR against the planning branch. If the plan has merged, branch from current main. Record the exact starting SHA and avoid overwriting another agent's work. Do not merge or close the historical PR as a side task.

Post `STARTED` with your branch, starting SHA, intended scope, and observed environment. Do not claim a GitHub comment is an atomic lock; check for an already active executor before beginning overlapping work.

## 2. Acquire and audit DICES350

Start with the official sources linked as D1 in `LITERATURE_AND_DATASETS.md`. Fetch only necessary public release files. Resolve the upstream revision and SHA-256 hashes. Use read-only source files and write derived outputs separately.

Verify the real schema and map:

- person: `rater_id`;
- item: `item_id`;
- input: `context` plus `response`;
- human outcome: `Q_overall`.

`response` is chatbot text, not the person's decision. Read the exact three-class mapping. Do not guess integer meanings, binarize the target, or discard an uncertainty answer as missing.

Document actual people/items/rows, per-person observations, overlap, exact duplicates, input groups, missingness, and author-documented quality flags. Explain exclusions and source terms. Never filter people based on disagreement with the majority or their prediction errors. An upstream advertised count is not a measured local count.

Build separate learner and evaluator views. Exclude query judgments, expert labels/reasons, demographics, other ratings of the target item, target explanations, confidence and timing from predictor inputs. Only the declared support labels may inform a held-out person's adaptation.

Audit the official TID-8 CommitmentBank and MultiPref documentation for the next task; do not download or train all candidates. If DICES is inaccessible or structurally unsuitable, document the reason and assess MultiPref `default` as the concrete next dataset. **MultiPref is audit-only in this assignment:** its candidate-aware equations, symmetric tie handling, support design and applicable baselines need a separately frozen protocol. Do not reuse DICES personal A/B intercepts or raw-label kNN for variable candidates. Do not switch datasets because a score disappoints. If no valid DICES pilot is possible, still complete the synthetic fixture, code, source audit, and concrete blocker report.

## 3. Build a reproducible small lab

Put reusable code under `labs/decision_functions/`. Use import-safe scripts and a small dependency manifest. Put derived first-run artifacts under `research/decision_functions_2026-11-24/runs/pilot_v1/`.

Provide commands for acquire, audit, prepare, synthetic checks, encode, train/develop, freeze verification, evaluate, and report. Record commands actually executed and their exit status. Examples in documentation are not evidence of successful runs.

Create the small synthetic control described in the plan: shared-factor and exception-rule regimes, two wording variants per semantic case, separate learner/evaluator records, and an ambiguous-support case. It is an engineering fixture, not a human dataset or a source for invented scholar opinions.

Implement meaningful checks for source mapping, joins, probability validity, missing/uncertainty distinction, split leakage, nested supports, evaluator-field exclusion, and consistent person-ID renaming. Use candidate-swap checks if the fallback has variable answer alternatives. Do not run historical index builders; some source scripts have import-time writes.

## 4. Construct partitions and supports

Use deterministic independent **60/20/20** partitions of people and audited item groups, seed **20261124**, following the plan's sorting/hash algorithm. Keep all exact duplicates and documented related item variants together. Record grouping uncertainty; do not advertise random unseen items as wholly new semantic topics.

- Shared fitting uses only training people × training questions.
- Development people adapt on their own training-question histories and are evaluated on development questions.
- Test people later adapt on their own designated training-question histories and are evaluated on test questions.

Use nested support budgets **0, 4, 16, 64**, support-draw seeds **101, 211, 307**, and **16** as the primary endpoint. In the dense dataset, use the same support questions across people for each draw. Keep the same eligible cohort for the support curve. The secondary 64-support budget may be omitted for documented structural reasons before fitting, but the primary 16-support endpoint cannot silently change. If it is infeasible, report the structural limitation and complete the engineering outputs. Store support and split manifests before fitting.

Keep query outcomes inaccessible to development/model selection. Labels may be read mechanically by the data adapter and evaluator, but must not be exposed in development reports or supplied to the learner. Do not use target labels to group cases, choose supports, tune text transformations, or exclude difficult records.

## 5. Run the declared model comparison

Use one frozen compact encoder, default **sentence-transformers/all-MiniLM-L6-v2**, with an immutable revision resolved and recorded at download. Follow the plan's deterministic full-token-coverage windowing and aggregation. Record serialization, token/window coverage, pooling, normalization, library versions, and hardware. Do not silently truncate or substitute another encoder.

Implement B0–B4 and M1 from the plan:

1. Population class frequencies.
2. Smoothed personal class frequencies.
3. Text-only multinomial logistic regression.
4. Text plus a support-fitted personal class intercept.
5. History kNN shrunk toward the text model.
6. A small shared low-rank interaction, with only the new person's intercept/vector fitted from their support.

The personal-intercept baseline is required: it tests whether improvement is merely a general label tendency. Call the interaction model PAL/PReF-inspired unless you actually reproduce a published method and evaluation.

Freeze the exact development grid, optimizer settings, convergence criteria and normalization before fitting. Use the plan's bounded grid and seeds; select the primary baseline and M1 configuration only by development NLL at 16 supports. Do not report the best random seed as the method. Save all attempted configurations, failures, and resource counters.

Execute shuffled-history controls without relabeling query owners. Keep all models' support observations identical. A weak history effect is a possible scientific finding, not grounds to search indefinitely for a favorable result.

## 6. Freeze, then score once

Complete a resolved `experiment_protocol.json` from the template. Required unknowns include upstream/checkpoint revisions, actual class mapping, quality policy, schema, grouping rule, cohort counts, paths/hashes for manifests, optimizer settings, selected configurations, and the final batch of evaluations. No unresolved required fields may remain.

Push code, manifests and protocol as a **PROTOCOL_FROZEN** commit. Post its SHA and the declared evaluation list to the coordination issue. Then proceed to scoring without waiting for an additional owner reply, provided correctness checks pass and resources remain within scope.

Evaluate declared methods, support sizes, support draws, training-seed diagnostics and fixed shuffled-history controls in one final batch. Do not refit shared parameters on development data. Save probabilities before aggregation. Keep raw third-party text and person histories out of Git; persist local prediction artifacts with checksums and reproducible regeneration commands, and publish compact aggregate summaries.

Primary contrast: macro-person NLL of the development-selected B0–B4 baseline minus M1 NLL, at 16 supports, on new test people and held-out item groups. Report B2/B3 comparisons and true-versus-shuffled-history differences separately. Use accuracy, multiclass Brier score and support curves as secondary results. Average repeated support-draw losses at the person/query level before the paired two-way person/group bootstrap described in the plan.

Do not change the model after inspecting test errors. If a correctness bug is discovered, preserve the invalid attempt, explain the exposure, version the correction, and qualify reuse of the test. Never describe a reused test as fresh confirmation.

## 7. Resource limits and autonomous completion

Default to existing local CPU resources, one human dataset and one frozen encoder. Scope limits: **2 GiB dataset/weight downloads, 6 CPU-core-hours for encoding/fitting, 8 GiB working memory, 40 shared-model fits**. Record adaptation solves separately. No new paid infrastructure, paid inference API, encoder fine-tuning, or open-ended search is assigned.

These are proposed limits, not prior measured requirements. Measure and report actual usage. If access or a resource bound prevents a step, finish all remaining feasible preparation and deliver a precise partial-execution report. Routine implementation, existing-source access, read-only audits, fixes, commits and draft PR creation within this assignment do not require another permission request.

## 8. Required return package

Create actual completed outputs; mark unavailable artifacts and explain why. At minimum:

- `DATA_AUDIT.md`, `source_manifest.json`, `dataset_schema.json`;
- `split_manifest.json`, `support_manifest.json` or reproducible hash manifests with locally retained detailed memberships;
- `EXPERIMENT_PROTOCOL.md`, resolved `experiment_protocol.json`;
- executable lab code, dependency versions, and meaningful validation results;
- `DEV_RESULTS.md`, `TEST_RESULTS.md` if the test ran;
- `results_summary.json`, probability/prediction artifact manifest, and paired-loss summaries;
- `RESOURCE_USAGE.json`, including failed attempts;
- `AGENT_REPORT.md`, `NEXT_HANDOFF.md`.

Reports must separate measured findings, mathematical interpretation, proposed next experiments, and unavailable evidence. State the exact source/checkpoint revisions, eligible cohort, number of independent people/item groups, support sizes, baseline selection, primary contrast and interval, control results, limitations and run status. Preserve unfavorable findings.

Open or update your execution draft PR, link it from the coordination issue, and post the final report using `GITHUB_WORKFLOW.md`. Include the exact final commit, freeze commit, commands, changed paths, outcome and next recommendation. Do not merge, change repository visibility, rebuild existing source indexes, or start P4/P5 as an unreported extension.

Finish with a valid pilot result, an explicitly invalid result requiring correction, or a concrete access/structure/resource limitation. Do not stop with another generic plan when the assigned experiment is executable.
