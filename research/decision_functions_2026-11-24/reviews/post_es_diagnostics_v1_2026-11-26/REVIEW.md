# Review of PR #27 and one fresh confirmation assignment

## Decision

Accept **H0–H4 as a completed diagnostic and engineering assignment**, including its disclosed reporting-only recovery. The saved-data ablation is informative and remains **post hoc**. Scientific qualification remains **false**. PR #20 remains **INCOMPLETE / NUMERICALLY_UNRESOLVED** at `f18255c5fad37f704881ff1f9ad50cd113497236`.

The next assignment is **uncapped_single_history_confirmation_v1, I0–I4**: implement the corrected execution boundary, freeze and publish it, then execute one fixed method on 82 untouched synthetic worlds. This review supplies the statistical design, seed reservation, finite work inventory, and executable agent instructions. It supersedes PR #27's proposal-only next-study text for this modeling continuation. It does not revise any historical endpoint or result.

This review performed no fitting, scientific world generation, human evaluation, or new policy ablation. Its new calculations concern public audit arithmetic, deterministic sample-size planning, and seed reservation only.

## Reviewed evidence

| Item | Pinned source |
|---|---|
| H0–H4 assignment, PR #25 | `2f1cae3e894bec16c9c5cd280356a4e051029031` |
| PR #27 pre-analysis | `dfc649e4557d4689c5d33556bb52faa88ec3cf03` |
| PR #27 final | `16ef28b105ff6c28ee3f822b1409f076fa895318` |
| Original PR #20 run | `f18255c5fad37f704881ff1f9ad50cd113497236` |
| Complementary PR #26 private-evidence audit | `dd636d32e084c6a2473659a9cc347fdebcd0d663` |

The main delivery is [PR #27](https://github.com/shulm/AI-Talmudic-Study/pull/27). Its pinned [results](https://github.com/shulm/AI-Talmudic-Study/blob/16ef28b105ff6c28ee3f822b1409f076fa895318/research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/RESULTS.md), [residual analysis](https://github.com/shulm/AI-Talmudic-Study/blob/16ef28b105ff6c28ee3f822b1409f076fa895318/research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/RESIDUALS.json), [ablation](https://github.com/shulm/AI-Talmudic-Study/blob/16ef28b105ff6c28ee3f822b1409f076fa895318/research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/ABLATION.json), [verification](https://github.com/shulm/AI-Talmudic-Study/blob/16ef28b105ff6c28ee3f822b1409f076fa895318/research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/VERIFICATION.json), and [reporting recovery](https://github.com/shulm/AI-Talmudic-Study/blob/16ef28b105ff6c28ee3f822b1409f076fa895318/research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1/REPORTING_RECOVERY.json) were inspected. Public audit evidence for this review is in the adjacent JSON receipts and portable scripts.

### Independent verification and its boundary

The public scientific checker performed **161,386 scalar assertions**, covering published scores, contrasts, residual-bound relationships, evidence averages, history aggregation, and historical scalar preservation. The engineering reviewer independently evaluated **1,704 saved trace points** and replayed **1,320 Newton transitions** without invoking an optimizer. All 384 attempt identities, 114 wrapper identities, 395 declared verifier-group identities, 1,055 delivery hashes, and 13 frozen scientific-source hashes reconciled. These counts describe arithmetic and audit operations, not independent experiments.

The largest independently recomputed final engineering residual was `9.840073629366365e-11`; the largest update discrepancy was `2.4424906541753444e-15`. Final saved parameters and independently replayed probabilities were bitwise identical across the four packaging layouts. The 36 guarded full-step acceptances obeyed the declared rule.

The review did **not** have the original or derived private cache bytes. It checked 112 public before/after private-file hash bindings, not the underlying files. It did not independently reconstruct private gradients, oracle arrays, or all private probability cells. PR #26 supplies complementary executor-run private-evidence checks; those are not relabeled as a second private replay here.

Git tree comparison confirmed all 1,215 historical blobs at the assignment, pre-analysis, and final revisions, all 13 frozen scientific sources, and all 12 frozen artifacts. No files were deleted. Unedited GitHub publication comments at 19:47:12Z and 19:47:13Z precede the recorded execution start at 19:47:28.294767Z on 2026-11-26. Host clock synchronization was not independently attested. See [CHRONOLOGY_PRESERVATION.json](CHRONOLOGY_PRESERVATION.json).

## Scientific interpretation

### Numerical error cannot explain the original recovery failure

For fixed shared parameters and a personal objective with positive penalty matrix D,

\[
J_s(\theta)=\frac1k\sum_i \mathrm{CE}(g_i+A_i\theta,y_i)+\frac12\theta^T D\theta,
\qquad \nabla^2J_s\succeq D,
\]

the residual gives

\[
\|\widehat\theta_s-\theta_s^\star\|_D
\le \|D^{-1/2}\nabla J_s(\widehat\theta_s)\|_2.
\]

PR #27 correctly propagates this conditional personal-optimization bound through centered logits, softmax, the fixed probability mixtures, and the eight-term anchored contrast. Its enclosures are analytic expressions evaluated in float64 with an allowance. They are not directed-rounding certificates, sampling confidence intervals, or certificates of a shared-model global optimum.

All four original capped-ES aggregate contrast lower bounds exceed .53. Improving only the saved personal solutions cannot bridge the original .50 threshold within the declared conditional scope. The H batch discrepancy remains real and remains part of the historical failure.

### Removing the cap helps, but the history-level failure matters

| Exposed world | Uncapped aggregate contrast NRMSE | Conditional optimization enclosure | Original capped-ES lower bound |
|---|---:|---|---:|
| E | .4821921035 | [.4821898423, .4821943646] | .5552739114 |
| F | .4828266020 | [.4828243509, .4828288532] | .5648972347 |
| G | .4388665439 | [.4388632228, .4388698651] | .5346817868 |
| H | .4759287818 | [.4759255264, .4759320373] | .5561640887 |

The uncapped expected-NLL gains over B3 are .531137, .528202, .547532, and .539463; oracle-gap recoveries are about .7965, .7915, .8207, and .8074. Removing the cap reduces expected NLL relative to capped ES by approximately .0236–.0278. This supports the proposed attenuation mechanism in these saved predictions.

However, **E/history101 has contrast NRMSE .5165570103**, with lower optimization enclosure .5165552180. Its failure survives the numerical-error allowance. The two-history aggregate combines losses and squared contrast errors; it does not show that each available 16-observation history works.

The next study therefore makes an explicit prospective change: **one randomly drawn, predeclared H1 is primary**. H2, the old two-history aggregate, and the requirement that both histories pass are secondary. H2 cannot rescue H1, and no prediction may combine the two histories into 32 observations. The historical studies retain their original aggregate endpoint.

### Null behavior still needs fresh evidence

All 192 inactive person-history predictions were unchanged in this ablation; 190 already used B3 exactly. Therefore the small reported inactive losses add no empirical information about what uncapping does on rare null histories with unusually large evidence.

The fixed rule is

\[
h(E)=.009(E-1)_+,\qquad
p_U=e^{-h(E)}p_{B3}+(1-e^{-h(E)})p_{M1}.
\]

Under the declared correct conditional null, the evidence construction gives an expectation argument, and the mixture bounds the positive excess loss by h. This is not a guarantee for each history or each finite inactive cohort. The next study retains the signed mean inactive-loss gate and separately reports positive-part and upper-tail loss, large weights, and coefficient underflow. No new tail endpoint is silently added as a fifth scientific gate.

## Engineering recovery is acceptable; its defect must not migrate

The frozen executor's final composition duplicates the `qualification` keyword and raises a `TypeError` after the substantive work. That defect remains in the historical frozen source. The separately hashed reporting-only adapter reads retained results, invokes no solver or prediction function, rejects conflicting terminal fields, and preserves the failed command. Accept that recovery without pretending the original invocation succeeded.

The fresh implementation must test the **actual executor → supervisor → terminal** path. Mock launch failure, child failure, resource termination, supervisor interruption, missing evidence, scientific failure, numerical failure, successful completion, and serialization collision. A terminal helper test alone would not have caught the observed integration defect. A supervisor must terminate and wait for a child on its own failure, retain unfinished starts, and prevent an automatic scientific retry.

Recorded run resources sum to **41.140625 sampled CPU seconds**, **104.031 profiled wall seconds**, and **107,982,848 bytes sampled peak RSS**, across six commands including the failure. Startup/exit CPU, transient peaks, authoring, and orchestration are not comprehensively measured. These remain sampled command totals.

## Why 82 worlds and what success would mean

Let J be the fixed implementation's numerically qualified, four-gate result for primary history H1 in a fresh world. The operational target is

\[
\pi=\Pr(J=1),\qquad H_0:\pi\le .80.
\]

The single one-sided exact binomial test uses **82 independent worlds** and requires **at least 72 primary successes**. At that boundary, size at .80 is .0458481011, nominal count-test power at the planning alternative .90 is .8057063960, and the one-sided 95% Clopper–Pearson lower bound is .8019263987. The adjacent [planning script](PLAN_CALCULATION.py) proves that 82 is the smallest fixed n meeting the 80% power requirement for that binomial count test, using exact rational tails and independent SciPy agreement. Additional completion, no-unresolved-outcome, numerical, and integrity gates can reduce overall qualification power; **overall qualification power has not been established**. They cannot enlarge the count test's rejection event. The .90 alternative is a planning assumption, not an estimate established by four exposed worlds. The .80 reliability target is a new bounded research criterion, not a deployment requirement or a retrospective relaxation of earlier studies.

The exact statistical statement concerns the frozen operational procedure under an independent, identically distributed world law. Its conditional optimization enclosures remain numerically evaluated bounds with the stated allowance. This distinction prevents the word “exact” in binomial inference from being transferred to real-arithmetic optimization or model truth. Official method references are [SciPy binomtest](https://docs.scipy.org/doc/scipy-1.15.1/reference/generated/scipy.stats.binomtest.html) and [Clopper–Pearson proportion_ci](https://docs.scipy.org/doc/scipy-1.15.1/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html).

The protocol repeats shared training in every world, fixes the method throughout, and uses the same random balanced-history law in each world. It requires 246 shared fits and 31,488 personal solves. Complete verification and numerical integrity are necessary in addition to the statistical result. An incomplete run cannot qualify from a favorable partial count.

## Relation to the original text-to-decision objective

The broader object remains

\[
x\in X\longmapsto q\in Q\longmapsto z=\phi(q),
\qquad f_s(q\mid H_s)\in\Delta(A(q)).
\]

This experiment supplies z, common answer-class meanings, and population logits g. It tests adaptation to a person's history in a known two-dimensional geometry. It does not learn a useful language metric, resolve answer alignment between questions, identify scholarly positions from source text, or establish transfer to unseen text domains.

After this single confirmation, end this oracle-generator sequence regardless of its result. The next handoff should propose one empirical representation/population-predictor study with grouped questions, held-out people, equal support budgets, B1/B2/B3 controls, and explicit outcome-blind data admission. An empirical study can proceed without claiming the .009 theorem. Transferring that theorem to estimated g requires a separate conditional-null argument; training on different people alone is insufficient.

## Coordination

PR #26's complementary audit is already accepted through issue #2 and remains independent. PR #18 is an **open draft, scientifically unexecuted planning package** at `cdcafb41726820265bd4e1dea5272702f2663aae`; its engineering repair is closed, not the PR. Its reserved seeds and CLI remain outside this assignment. Corpus production and reviews, including PRs #17 and #21–#24/#28/#29 observed during coordination, continue on their separate track. No merge or visibility change is part of this review or its continuation prompt.

Read [CONFIRMATION_PROTOCOL.md](CONFIRMATION_PROTOCOL.md), [NEXT_AGENT_PROMPT.md](NEXT_AGENT_PROMPT.md), [DESIGN.json](DESIGN.json), and [SEEDS.json](SEEDS.json) as one assignment. The next agent must publish and read back its own pre-fit implementation freeze before generating any confirmation world.
