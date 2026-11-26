# Next agent assignment: post_es_diagnostics_v1

## Objective and authorization

Continue AI-Talmudic-Study through H0–H4 below. Read root AGENTS.md and AGENT_HANDOFF.md, then the adjacent REVIEW.md, METHOD_NOTE.md, ENGINEERING_SPEC.md and next_post_es_design.json.

Preserve PR #20 at f18255c5fad37f704881ff1f9ad50cd113497236 as **INCOMPLETE / NUMERICALLY_UNRESOLVED**, qualification false. Its scientific pre-fit is 38dfff076b90d7c08387a06bd25f3cc75f15f6ae; its assignment was PR #19 at 724be8c49808e1e1b8643d81c73267f7577439c8.

Answer two precise questions:

1. How much numerical uncertainty remains in the saved personal predictions, and can it bridge the recorded contrast gaps when shared models and evidence are fixed?
2. What changes in those same saved predictions when only the imposed 90% mixture cap is removed?

Also deliver a reusable personwise solver and complete terminal reporting for future studies. This is a diagnostic and engineering assignment. It authorizes **zero new scientific fits, zero historical refits, zero fresh scientific worlds, and exactly 384 scheduled engineering personal solve attempts** on the deterministic suite. No optimizer may consume E/F/G/H data under this assignment.

The original private cache is identified in PR #20's handoff. It is read-only input. If it is unavailable, complete the engineering and proposal work, mark the private diagnosis unavailable, and report the exact missing evidence. Do not reconstruct substitutes for missing fitted parameters or invent verification results.

## H0 — Isolate and freeze the diagnostic

Base a new branch on the reviewed PR #20 delivery with this review package included. Preserve every historical lab/run file and source corpus. Use new paths:

- Laboratory: labs/decision_functions_post_es_diagnostics_v1/
- Public artifacts: research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/
- Derived private artifacts: a new directory outside the original evidence_shrinkage_v1 cache.

Read the current PR #18 handoff for coordination only. Its original planning revision is 49d7157e3998a20f646e9200c3e223bbbb58541f; the current engineering-repair head observed in this review is cdcafb41726820265bd4e1dea5272702f2663aae. That repair is already closed by its separate supervisory review and does not authorize scientific execution. Do not run its CLI, use its seed bank, alter its files, or count this assignment as its execution authorization. Refresh the corpus-production PR metadata only to avoid overlap; no corpus task is assigned.

Before any new engineering solve or private ablation calculation, publish a pre-analysis checkpoint and read it back in issue #2. Freeze:

- diagnostic code, scalar formulas, error-bound implementation and tolerances;
- sole uncapped rule, scoring and aggregation;
- all deterministic engineering fixture arrays, exact IDs, hashes and schedule;
- exact 384-attempt/114-wrapper inventory, stop paths and immutable algorithm;
- input bindings to all 36 historical archives and 76 full optimizer vectors;
- expected output keys, shapes, rows and comparison IDs;
- environment, single-thread configuration and resource accounting.

Pure objective/derivative evaluations, source review and code corrections before the checkpoint are permitted. They must be recorded; there are no undeclared development optimizer calls. The first formal engineering solve starts the fixed 384-attempt budget. Do not change the solver algorithm, fixtures, penalties, targets or numerical thresholds after that point.

This is a pre-analysis freeze on already exposed scientific data, not preregistered confirmation. Do not use that terminology to imply that E/F/G/H have become unexposed.

## H1 — Read-only numerical diagnosis

Verify historical public/input hashes before reading the model data, and again after all analysis. Check the 112 private artifact bytes against their public bindings where the cache is present. Reject absent, changed, duplicated or incomplete inputs.

Use the unchanged saved data and an independently expressed forward calculation to verify parameter slices, seed-specific V/U alignment, old query predictions, evidence and mixtures. The original frozen replay functions may be used as a comparison. Deterministic reconstruction of the already exposed E/F/G/H fixtures is permitted solely for verification; no new seed/world may be materialized.

Do not recreate scientific_summary.json, overwrite the historical verifier receipt, or run the old executor. Preserve the original missing-summary exception and the distinction between 1,158 successful comparisons and two unreached IDs. A new diagnostic can have complete evidence even though the historical scientific run remains incomplete.

For all **1,664 personal row instances in 64 saved personal parameter vectors**, recompute the gradient of the individual objective without dividing by batch size. The other 12 optimizer vectors are shared fits and are not covered by personal strong-convexity claims.

Use the bounds in METHOD_NOTE.md:

\[
R_s=\|D^{-1/2}\nabla J_s(\hat\theta_s)\|_2,\quad
K_q=\|(I-\mathbf1\mathbf1^\top/3)A_qD^{-1/2}\|_2.
\]

Save per-row residuals, norms, prediction/log-probability bounds and exact identities. Report the first-person and first-seven-person comparisons for every original realization, seed and B3 head, not only the largest H discrepancy. Batch 48 is a comparison reference, not an exact solution.

Hold shared V, training priors, evidence and weights fixed. Propagate log-probability bounds through the seed ensemble and mixtures, then through the original eight-term anchored contrasts. Report deterministic lower/upper NRMSE enclosures for M1, FIXED_MIX and original ES; apply the same saved component bounds to the uncapped ablation after H2 creates it. Use the same support histories, paired people, class-pairs, query ordering and oracle denominator as the original definition. Also bound their expected-NLL changes.

A lower contrast bound above .5 supports the conditional statement that personal optimization error cannot bridge that recorded gap. An enclosure crossing .5 is uninformative. Do not refit, widen a tolerance, or infer the exact optimum would pass. Separate these optimization-error enclosures from confidence intervals and from sampling uncertainty.

Independently evaluate residuals and document floating-point comparison allowances. Unless directed-rounding interval machinery is actually implemented and checked, describe these as analytic bounds evaluated numerically, not machine-rigorous certificates.

## H2 — Exactly one cap-removal ablation

From the original B3, seed-ensemble M1 and arithmetic-mean scalar evidence, calculate only:

\[
h_\infty=.009(E-1)_+,\qquad
p_\infty=e^{-h_\infty}p_{B3}+(1-e^{-h_\infty})p_{M1}.
\]

Do not change .009, priors, shared/personal penalties, fitted parameters, evidence definitions, histories, seed averaging, baseline, score floor, or thresholds. No cap grid, new shrinkage rule, alternate prior, seed selection or support-size curve.

Produce **eight new primary prediction arrays**, one per realization/history, each 48 people by 36 queries by three classes. Keep their log mixture coefficients, per-person weights and input hashes. Preserve baseline coefficients directly in log space; do not calculate them as one minus a rounded weight. Record coefficient underflow and use stable logaddexp. Do not introduce a numerical replacement cap or renormalize clipped probabilities.

For each row on which the cap was inactive, independently verify the calculated mixture against the old ES row within 1e-12, then retain the original row exactly. The published evidence implies that all 192 inactive person-history rows must remain unchanged and that 153 active rows have changed weight. Check this rather than assuming it.

The new scientific-description output contains 16 stratum/history rows and eight stratum aggregates. Compare original B3, M1, FIXED_MIX and ES with the uncapped arm, using:

- expected and sampled NLL, accuracy and Brier score;
- active gain and oracle-gap recovery;
- contrast numerator, denominator, MSE and NRMSE;
- inactive expected excess and positive-part excess;
- per-person changes, cap activation and numerical-error enclosures.

Average losses and squared errors across histories; do not pool their probabilities. Report ordered changes in contrast MSE as well as NRMSE. The repeated histories are not independent people.

No additional donor arm or bootstrap resampling is required for this explanatory ablation. Do not select a favorable confidence procedure or count the old bootstrap as uncertainty for the new rule.

Every new table must be labelled **POST_HOC_EXPOSED_DIAGNOSTIC**. Former thresholds may be displayed as descriptive reference lines, but qualification remains false. Even if all descriptive thresholds are met, the result is a candidate for independent confirmation, not a rescue of PR #20.

## H3 — Personwise solver and failure-complete reporting

Implement the exact fixed individual objective in a new module. Each person's trajectory, line search and stopping condition must depend only on that person's support data, the fixed basis and fixed penalties. Wrapper batching may change packaging only.

Follow ENGINEERING_SPEC.md without substitutions:

- 48 toy people, eight motifs, 16 supports and 12 query-design rows;
- B3 and M1; fixed unlearned V and penalties;
- four layouts: singletons, chunks of seven, all 48, reverse 48;
- 384 actual individual solve attempts and 114 wrapper calls;
- zero initialization, D-scaled coordinates, fixed damped Newton;
- support-only residual target 1e-10, finite iteration/backtracking limits;
- independently checked derivatives, analytic motifs, residuals and query-error bounds.

Do not cache one solution and call its reuse another solve. Count every actual optimization invocation, including failures. If a finite isolated formal case fails, preserve it and complete the remaining declared cases; abort on corrupted inputs, nonfinite arithmetic or a resource limit. No formal-case retry or alternate optimizer.

Derivative/value-only checks do not use an optimizer, but their resources still count. These engineering cases measure implementation behavior, not predictive performance on people.

Build a small reusable terminal-reporting utility for future studies. Consult PR #18's repaired attempt accounting and repeat-verification pattern as a reference; do not reopen or duplicate its completed repair task. On success, numerical failure, scientific failure, incomplete evidence, or resource stop, it must write the completed/expected inventory, failure reason, scientific status, numerical status, integrity status and qualification=false unless all required axes pass. Test these paths with static mock inputs and corruption/missing-file examples. A terminal receipt alone must never establish integrity.

Do not retrofit that utility into PR #20, create its missing summary, or change any old verdict.

## H4 — Deliver a decision and concrete next proposal

Publish a draft PR and an issue #2 report with:

- input/pre-analysis/final commits and all historical preservation hashes;
- exact diagnosis, ablation and engineering counts, including attempted failures;
- per-person residual findings and contrast-error enclosures;
- the five-arm descriptive comparison and unchanged-inactive checks;
- solver source, immutable fixtures, independent checks and complete receipts;
- terminal-reporting examples and fail-closed checks;
- CPU, wall-time and sampled-memory accounting, including unsuccessful commands;
- a concrete handoff and exactly one recommended next scientific question.

Report separate axes:

1. Historical status: INCOMPLETE / NUMERICALLY_UNRESOLVED, unchanged.
2. Diagnostic evidence: complete, incomplete, or private artifacts unavailable.
3. Solver engineering: pass, fail, or incomplete.
4. Cap ablation: descriptive complete or unavailable.
5. Scientific qualification: false; no new confirmatory experiment ran.

Decision rules:

| Finding | Next proposal |
|---|---|
| Missing or inconsistent private artifacts | State the exact evidence gap; finish independent engineering; no reconstructed substitutes |
| Solver engineering fails | Specify the unresolved implementation/algorithm issue; no scientific launch |
| Uncapped descriptive recovery still fails, or numerical enclosure is uninformative | State which uncertainty remains; do not start a cap/penalty search |
| Solver passes and uncapped descriptive recovery meets all former criteria | Propose one fresh confirmation with untouched seeds and fully stated endpoints; do not execute it here |

The next proposal must also explain how it advances text-based decision-function modeling. Distinguish empirical text prediction without the .009 guarantee from transporting that guarantee to an estimated g. Independence from target people does not prove that the conditional null is correct. Cite the current population-predictor limitation and propose an identifiable control, not an automatic encoder download.

DICES and completed SRO tests remain exposed. Any future human dataset needs its own provenance, admission and split review. Corpus production continues independently; this assignment does not produce or certify scholarly records.

Stop after the complete diagnostic/engineering handoff. No fresh scientific fit, human evaluation, data/model download, paid call, PR #18 execution, corpus edit, historical repair or merge.

## Resource ceiling

At most 600 accounted CPU seconds and 1 GiB sampled peak RSS for this new task, including all attempted engineering cases, replay, diagnostics and tests. Use one computational thread. Retain failed-command and stop receipts; explain sampled-memory and unprofiled-overhead limits. Stop cleanly rather than enlarging the budget.

The formal scientific optimization budget is zero. The formal engineering budget is 384 individual solve attempts; it is not a promise that all attempts will succeed.
