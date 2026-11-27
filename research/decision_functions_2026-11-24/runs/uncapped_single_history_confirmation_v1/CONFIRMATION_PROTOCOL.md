# Uncapped single-history confirmation v1 — fixed protocol

Status: reviewed design and reserved seeds; **no confirmation data generated and no fits executed by this review**. The execution agent must implement this protocol in a new lab/run, complete zero-fit preflight, publish and read back its implementation freeze, and then perform I0–I4 once. This document, DESIGN.json, SEEDS.json, and NEXT_AGENT_PROMPT.md form one assignment.

## 1. Question, estimand, and scope

Does the fixed uncapped evidence mixture, with the verified personwise solver, reliably satisfy all four existing cohort-level criteria when a new person has **one designed 16-observation history**?

For each world W, H1 is its predeclared random primary history panel; H2 is secondary. The model is

\[
p_s(c\mid q,H_s)=\operatorname{softmax}_c\left[g(q)+b_s+\left(u_s^T V_c z_q\right)_{c=1}^3\right],
\]

with B3 omitting the interaction term. The primary method U mixes the B3 and arithmetic three-start M1 probability predictions using the fixed conditional evidence rule below.

Let the fixed, versioned isolated per-world procedure return a joint H1 status. Define J(W)=1 exactly when that procedure returns a verified, numerically qualified H1 joint PASS; all other terminal algorithmic outcomes lie outside the event. This defines J without conditioning on algorithmic success. Global resource/infrastructure interruptions and complete-study reporting are separate gates; never impute observed outcomes to unstarted or interrupted worlds. The primary target is **operational world reliability**:

\[
\pi=\Pr_{W\sim\mathcal P}\{J(W)=1\},\quad H_0:\pi\le .80,\quad H_1:\pi>.80.
\]

The reference scientific quantities concern exact personal minimizers conditional on the delivered shared models, evidence, histories, and computed oracle references. Numerical enclosures support that interpretation under their evaluation allowance; they are not directed-rounding proofs. Exactness of the binomial calculation does not certify real-arithmetic optimization.

The study changes the historical primary estimand prospectively from a two-history aggregate to H1 alone. It also replaces four-world all-pass reporting with one predeclared reliability target. Earlier results retain their original definitions. The new target is a bounded research criterion under this generator, not an 80% claim about individual people, arbitrary question histories, or text tasks.

## 2. Independent worlds and untouched seed reservation

Use exactly **82 worlds, U000 through U081**, in that order. SEEDS.json reserves five decimal-string uint64 seeds per world: generator, label, mask, H1_support, H2_support. Convert decimal strings directly to integers for PCG64; do not pass them through a floating-point JSON number. SEED_RESERVATION.py derives them deterministically from SHA-256 of a fixed experiment namespace. It instantiates no research RNG. SEED_RESERVATION.json binds historical seed sources and records disjointness, including PR #18's 216 reserved values.

Before generation, audit all accessible exposed/reserved seed registries and current issue #2 coordination for collisions or competing use. A collision or evidence that these worlds were already generated blocks launch; do not redraw, replace, rename, or choose a new bank automatically. No seed is selected using model outcomes. Separate reproducible PRNG streams are treated as independent draws for the simulation's statistical model; cryptographic seed derivation is not itself a theorem of stochastic independence.

Retain the PR #20 generator in `labs/decision_functions_evidence_shrinkage_v1/fixture.py` at `f18255c5fad37f704881ff1f9ad50cd113497236`, with only the explicit fresh seeds, experiment namespace, and support-schedule law changed. Freeze all copied/imported transitive dependencies. Do not call an old execution entry point.

| Generator property | Fixed value |
|---|---|
| People | 192: 96 training, 48 unused, 48 evaluation |
| Matched pairs | Adjacent people share centered three-class bias and have opposite interaction phase |
| Activity | Whole pairs; half active in each of the three people partitions |
| Evaluation people | 24 active and 24 inactive; learner does not receive status |
| Questions | 192, in 64 rotational triplets |
| Group partitions | 40 training groups, 12 unused, 12 query groups |
| Training/query cases | 120 training, 36 query |
| Support pool | The first 32 training groups: 96 cases |
| Features / classes / rank | Unit-circle z in R² / three fixed class meanings / rank 2 |
| Population logits | Known g, scale .25 |
| Interaction scale | 2.5 |
| Bias standard deviation | .12, class-centered |

Generate one complete response array per world using its label stream. The activity mask uses the separate mask stream, balanced exactly as above. Training is repeated in every world. Shared initialization seeds 11/29/47 are fixed algorithmic starts, not world draws.

### Common random history law

For H1 and H2 separately, initialize PCG64 from that history's reserved support seed. Starting from the **sorted** 32 eligible group IDs, set `groups = rng.permutation(sorted_pool_group_ids)`, then `phases = rng.integers(0, 3, size=32)`. Pair each group with the phase at the same permutation position using `zip(groups, phases)`; phases are not indexed by the original group ID. For each such pair, list its three questions cyclically starting at that phase. Concatenate and take the first 16: five complete triplets and one question from the sixth group.

Use the same panel and order for all evaluation people and methods within a history. The empirical feature-Gram eigenvalues must be .46875 and .53125 within the inherited 1e-12 geometry allowance. H2 may overlap H1; retain overlap and reuse the original world response for the same person/question. Do not reject panels, resample responses, or filter by labels, activity, evidence, oracle values, or performance. Every prediction uses only its own sixteen labels; no H1/H2 pooling or selection.

This common outcome-blind law gives the intended identically distributed world procedure. The independent units are 82 worlds, not 164 histories or 3,936 evaluation people. Each prediction concerns new evaluation people and disjoint query groups; their support groups may also have been observed for training people.

## 3. Fixed fitted components and evidence mixture

### Shared and personal fitting

Retain the shared objective and initialization from the pinned `head.py`: rank 2, rho=.01, lambda_b=.1, starts 11/29/47, L-BFGS-B maxiter=1000, ftol=1e-12, gtol=1e-8, maxls=50, float64, one numerical thread. Save full V/U/b vectors, objective, gradients, termination data, and receipts. Require finite outputs and declared optimizer success; make no global-optimum claim. Failure is preserved and stops the study without a retry or replacement world.

Adapt each evaluation person separately from zero using the PR #27 personwise D-scaled Newton algorithm at `16ef28b105ff6c28ee3f822b1409f076fa895318`. Use 100 accepted steps maximum, 40 fixed Armijo candidates, coefficient 1e-4, and the existing narrowly specified full-step roundoff guard. Preserve the support-only residual target 1e-10. There is no algorithm, penalty, initialization, threshold, or restart search.

\[
D_{B3}=\operatorname{diag}(.6,.6,.6),\qquad
D_{M1}=\operatorname{diag}(.6,.6,.6,.06,.06).
\]

### Evidence and weights

For each shared start, use the training-only symmetric empirical prior on the 192 atoms formed from ± all 96 fitted training-person interaction coordinates. Keep the exact conditional class-count likelihood-ratio calculation and dynamic-programming normalizers from the pinned evidence implementation. The learner/evidence code receives neither activity nor query responses nor oracle probabilities. Average the three e-values arithmetically in log space; average the three M1 probability predictions arithmetically, not their logits or coordinates.

The sole primary rule is

\[
E=\tfrac13\sum_{j=1}^3E_j,\quad
h_U=.009\max(E-1,0),\quad \log\beta_U=-h_U,
\]

\[
p_U=\beta_U p_{B3}+(1-\beta_U)p_{M1}.
\]

Use the stable uncapped implementation from PR #27, including log-sum-exp/logaddexp and expm1. Preserve finite log-beta even when beta underflows. Do not derive beta by subtracting a rounded weight from one. Detect nonfinite evidence or coefficients and stop as numerical failure; do not clip to a new cap or silently set an overflowed value. Score with the existing probability floor 1e-12 and record underflow counts.

The six fixed main controls are B1, B2, B3, M1, FIXED_MIX, and ES. B1 is the history count predictor `(counts + 4*training_prior)/20`; B2 is softmax(g); FIXED_MIX is .1*B3+.9*M1; **ES keeps the original capped meaning**, h=min(h_U,log(10)). No control can replace U as primary after exposure.

For each history, donor(s)=s xor 1 on evaluation rows. Transfer the entire history-derived state, including personal offset, interaction coordinates, counts, and evidence weight, within that history. Because query panels and g are shared, donor predictions equal the corresponding complete own prediction at the donor row. Verify both parameter/state reconstruction and this permutation identity. No donor fitting, donor seed-component copies, or cross-history state transfer is needed.

## 4. Fixed inventory and information boundary

| Actual work | Per world | Total |
|---|---:|---:|
| Shared fits | 3 | **246** |
| Personal wrappers: H1/H2 × four heads | 8 | **656** |
| B3 personal solves | 96 | **7,872** |
| Three M1-start personal solves | 288 | **23,616** |
| All actual personal solves | 384 | **31,488** |

Use fixed world/history/head/person IDs in the pre-fit expected manifest. A wrapper is organizational; it must call the personwise solver once for each of its 48 people. No batch1/7/48 scientific refits or new engineering optimization suite. Zero-fit preflight and saved-trace replay do not count as new fits; explicitly attest that no optimizer ran in preflight.

Save one `predictions.npz` per world with 34 float64 arrays, each [48,36,3]. Per H1/H2, the exact suffixes are seven own main methods (`B1`, `B2`, `B3`, `M1`, `FIXED_MIX`, `ES`, `ES_UNCAPPED`), three own components (`M1_11`, `M1_29`, `M1_47`), and seven main-method `_donor` counterparts. Total: **2,788 probability arrays**. Retain `ES_UNCAPPED` as the sole primary identifier.

Also retain four stable uncapped log-probability arrays per world, own/donor × H1/H2, under a distinct log-prediction role: **328 log arrays**, each [48,36,3]. These are additional numerical representations, not additional methods or probability-array count. Parameter, evidence, fixture, bound, and scoring artifacts have their own frozen shapes/keys. Save finite log-beta and evidence intermediates. Freeze the full archive/key/shape inventory before generation; no optional artifacts may be needed for qualification.

Keep generated response arrays, private model vectors, per-cell probabilities, and private caches outside Git. Publish aggregate/per-world diagnostics, exact manifests and hashes, seeds, source, receipts, and reproduction instructions. Do not upload human data or full source corpora.

Generate separate learner, support, and evaluator views. Fitting/adaptation/evidence/prediction functions accept only permitted inputs. In each world, finalize and hash all methods' probability, log-probability, evidence, and parameter artifacts **before loading the evaluator view into scoring**. Activity and oracle truth are evaluator-only. An independent verifier checks the view joins and group/person separation from saved artifacts without regenerating a world or calling an optimizer.

## 5. Primary metrics and numerical decisions

All primary losses use the oracle-expected NLL on the 36 held-out queries, with equal weights within the stated active/inactive cohort. Precisely, `L(p) = -mean_{s,q} sum_c o[s,q,c] * log(max(p[s,q,c], 1e-12))`, and `O = L(o)`. The floor is inside logarithms only; never renormalize floored probabilities. Canonical point metrics use the saved probability arrays. Stable uncapped log arrays are retained for numerical verification: compare `max(log_p, log(1e-12))` with the canonical floored log probabilities using a frozen absolute 1e-12 per-cell tolerance. Do not silently substitute a different scoring convention. Sampled-label NLL, accuracy, and Brier score are secondary. Let B, U, and O be B3, uncapped, and oracle losses. The four original thresholds are:

| Metric | Gate |
|---|---|
| Active gain B−U | ≥ .05 |
| Active oracle-gap recovery (B−U)/(B−O) | ≥ .50, with positive denominator |
| Active anchored-contrast NRMSE | ≤ .50 |
| Inactive signed excess U−B | ≤ .01 |

Retain the exact legacy contrast: floor probabilities at 1e-12, form the three class log-odds pairs (0,1), (0,2), (1,2), subtract the two members of each adjacent matched pair, and subtract that pair's contrast at **the first ordered query**. Retain all 36 queries, including the anchor's zero term. Average squared errors over active pairs × queries × class pairs. Divide by the mean squared oracle contrast and take the square root. Inactive truth contrast is structurally zero; report inactive contrast RMS, not an undefined inactive NRMSE. The query ordering/anchor is frozen by the generator and never selected by outcomes.

### Conditional personal-optimization enclosures

For each actual solve retain independently expressed gradient vectors r1 and r2. Set

\[
a=10^{-12}\max(1,\|r_1\|_\infty,\|r_2\|_\infty),\quad
\|r_1-r_2\|_\infty\le a,
\]

\[
R=\|D^{-1/2}r_1\|_2\le10^{-10},\quad
R_{used}=R+a\sqrt{\sum_jD_{jj}^{-1}}.
\]

Use R_used downstream; do not inadvertently tighten the stopping rule to R_used≤1e-10. With centered query design K_q=||P A_q D^(-1/2)||_2, bound probability error by K_q R_used/2 and log-probability error by sqrt(2) K_q R_used. Record every K_q, gradient comparison, parameter binding, and bound. Query values do not affect the support-only optimizer stopping path.

Propagate component log bounds through the fixed mixtures with lower/upper log-sum-exp, apply the floor, and derive expected-loss bounds. Sum the eight absolute log-error bounds for each anchored contrast cell, bound its squared error by `[max(|e|−b,0)^2,(|e|+b)^2]`, and then average. Hold shared models, weights/evidence, and computed oracle references fixed. These enclosures address personal optimization only; they are not confidence intervals or shared-model certificates.

Let [B−,B+] and [U−,U+] be the active/inactive loss enclosures, D>0 the fixed active oracle contrast denominator, and [M−,M+] the contrast MSE enclosure. Use direct gate margins:

| Gate | Lower and upper margin |
|---|---|
| Active gain | $[B^- - U^+ - .05,\ B^+ - U^- - .05]$ |
| Active recovery | $[.5B^- - U^+ + .5O,\ .5B^+ - U^- + .5O]$ |
| Active contrast | $[.25D - M^+,\ .25D - M^-]$ |
| Inactive excess | $[.01 + B^- - U^+,\ .01 + B^+ - U^-]$ |

Before classifying recovery, require demonstrably positive `B_lower - O > 0`. If this is not established, mark the recovery gate UNRESOLVED, and report the ratio as undefined when its computed denominator is nonpositive; do not classify the transformed recovery margin outside its positive-gap domain. Other definite failed gates can still resolve the joint outcome as FAIL. Preserve point metrics as well. Treat computed oracle loss/contrast as fixed numerical reference inputs; their floating-point arithmetic is outside the personal residual enclosure, and independent scoring replay must check it.

Per gate: PASS if the lower margin is ≥0; FAIL if the upper is <0; otherwise UNRESOLVED. H1 joint PASS requires all four gates PASS and positive denominator established. A definitive failed gate makes joint FAIL, even if another gate straddles; otherwise a straddle or unresolved positive-gap check makes joint NUMERICALLY_UNRESOLVED. Nonfinite arithmetic, invalid oracle contrast denominator, invalid array semantics, or failed independent residual checks are numerical/integrity failures and halt execution. Equality passes only when the enclosure establishes it. No favorable rounding or point-estimate override.

Continue the planned sequence through scientific FAIL or endpoint UNRESOLVED without refitting. H2 endpoint straddles are reported as secondary; they do not create a fifth primary scientific gate. H2 actual solver/integrity failures still violate the execution contract.

## 6. Exact world-level decision

At complete execution let S be the number of operational H1 PASS worlds among all 82. Compute

\[
p_{exact}=\Pr\{\operatorname{Binomial}(82,.8)\ge S\},\quad
L_{95}=\operatorname{Beta}^{-1}(.05;S,83-S)
\]

for S>0, with L95=0 for S=0. Use the one-sided `greater` binomial test and one-sided 95% exact Clopper–Pearson lower bound. Do not accidentally substitute a two-sided 95% interval. Critical success count is **72**; L95(72)=.8019263987400118. PLAN_CALCULATION.json gives exact rational planning tails and the sample-size minimum. Its .8057064 power and n=82 minimum concern the binomial count component only. Additional completion, numerical-resolution, integrity and resource requirements can reduce overall qualification probability; overall qualification power is not established. The inference has the declared fixed-world-law interpretation, not a conditional guarantee selected on successful completion.

Final scientific qualification requires **all** of:

1. All 82 worlds and all required artifacts/attempts verified complete.
2. All declared numerical, integrity, source-freeze, and resource contracts met.
3. Every H1 joint outcome numerically resolved.
4. S≥72 and the independently reproduced exact test/lower bound agrees.

Resolved S<72 is **VERIFIED_COMPLETE / PRIMARY_FAILURE**. Any unresolved H1 joint outcome makes qualification false and numerical resolution unresolved, even if S≥72 from other worlds. Report operational PASS/FAIL/UNRESOLVED counts; do not drop unresolved worlds from n. When all data are complete the operational success indicator is still defined, but its count cannot override this additional qualification gate. Any incomplete execution/evidence is **INCOMPLETE**, with no confirmation conclusion from partial counts.

No early stop based on a high/low success count; no extra worlds, replacement seeds, optional extension, hyperparameter selection, or scientific retry. Halt actual execution on a genuine solver, integrity, nonfinite, or resource failure, preserve the unreached inventory, and report the obstruction.

## 7. Prespecified descriptive analyses

Report H2's same four metrics/statuses; joint success for both histories; and the old two-history aggregate computed from average losses and average squared errors, never averaged predictions or averaged NRMSEs. Report the count of aggregate successes hiding an H1/H2 failure, and the count of H1/H2 disagreements. Secondary unresolved statuses remain visible.

For all fixed main controls, report paired per-world differences against U, by history and active/inactive stratum. Include sampled NLL, accuracy, Brier score, inactive signed expected excess, mean positive part of per-person expected excess, and per-person excess min/median/q90/q95/q99/max using NumPy's `linear` quantile definition. Include evidence/weight distributions, fractions at zero and above the historical .9 weight, beta underflow counts, finite log-beta range, and complete own/donor comparisons. Keep all declared methods and worlds in the tables.

Across worlds, report mean, sample standard deviation (ddof=1), min/median/q10/q90/max and all 82 values for each primary metric and fixed paired comparison. These empirical summaries are descriptive, without secondary significance claims. No person-level or question-level bootstrap is used in this protocol. The primary whole-world design already varies people, groups, labels, support panels, and shared retraining; counting individual people/histories as independent would be incorrect. This explicitly replaces the older four-world conditional person/group bootstrap for the new primary inference. No unplanned comparison, favorable secondary rate, or pooled mean rescues primary failure.

## 8. Preflight, execution, accounting, and reporting

Use new paths `labs/decision_functions_uncapped_single_history_confirmation_v1/` and `research/decision_functions_2026-11-24/runs/uncapped_single_history_confirmation_v1/`. Preserve all historical files and statuses. Implement one canonical terminal composition function; protected status fields cannot be duplicated or overridden. Non-null failure_reason is incompatible with qualification=true.

Before generating a world, run the actual executor/supervisor/terminal boundary using tiny deterministic mocks and an optimizer stub that raises if called. Cover success, primary scientific failure, numerical failure, missing/incomplete evidence, command-launch exception, child nonzero exit, resource kill, supervisor interruption, terminal collision, and frozen-output collision. Use isolated mock output roots and mock IDs, never the real scientific start/journal namespace. Verify child cleanup and durable unmatched start retention. Replay saved PR #27 engineering trajectories without solving again, and check independent derivatives on fixed toy inputs without optimization. Verify evidence arithmetic on small fixed enumerated label cases. Bind the frozen real entry point, not merely a helper.

Publish source, method/protocol, seed-bank hash, environment/library versions, transitive dependency hashes, exact attempts/archives/verifier-group identities, resource ceiling, preflight receipts, and historical preservation manifest in a new draft PR. Post the pre-fit commit to issue #2 and the PR; read back both before any world materialization. Bind execution to that exact published source revision. Any implementation correction before generation requires another pre-fit freeze/readback; it must not use confirmation outcomes.

Resource ceiling for this complete assignment: **3,600 accounted CPU seconds**, **4 GiB sampled peak process-tree RSS**, one numerical thread, zero GPU/paid calls/downloads. This is a conservative workload budget, not a runtime prediction. Historical runs used tens of CPU seconds for four worlds; the new inventory and individual solving justify a larger explicit ceiling. Include preflight, failures, execution, verification, and reporting commands in the cumulative ledger. Do not double count internal fit CPU on top of process totals. Record sampling interval, startup/exit gaps, measurement scope, and unprofiled overhead. Missing required-command accounting or unexplained work remains unresolved and blocks verified compliance. Disclosed sampling gaps remain limitations of the accounted/sampled metric, rather than automatically making every sampled run incomplete. Do not call this an exact process-lifetime hard bound; that would require stronger OS accounting/enforcement.

Maintain durable attempt starts before any fit/solve and completion/failure records afterward, with exclusive output creation, input/source/environment bindings, fixed IDs, stop reasons and saved parameters. JSONL journals per world are permitted to avoid tens of thousands of tiny files; enforce unique identities, flush durable starts, and finalize immutable hashes. Unlike PR #27's public toy traces, the new parameter/gradient/accepted-step vectors remain private; publish their hashes and scalar/status receipts. The supervisor must terminate and wait for its child on failure/interruption and preserve unmatched starts even if the child never reaches `finally`. No automatic resume or retry after a scientific start; a later continuation would require a separately reviewed assignment for only unstarted identities.

The independent final verifier must read saved artifacts, reconstruct predictions/evidence/metrics without fitting or generating a world, check every actual personal residual and all declared identities, and reject missing/extra/duplicate keys. Freeze and test tolerances before generation; retain the legacy 1e-12 probability and 1e-10 scalar replay tolerances unless a specifically justified arithmetic expression requires a separately stated pre-fit tolerance. No tolerance is chosen from confirmation outcomes. Repeated read-only verification writes a fresh receipt or checks the existing immutable one; it must not overwrite evidence.

Prepare a one-shot reporting-only recovery path before freeze. It may serialize already saved verified evidence and must never import/call fitting or prediction-generation entry points. Preserve the original failed command and its resources. Missing scientific evidence cannot be manufactured by reporting recovery.

## 9. Exit and next handoff

Return one new draft PR, issue #2 report read back from GitHub, exact pre-fit/final/source/model revisions, aggregate tables, independent verification, all failures, resource limitations, and concrete NEXT_HANDOFF.md. Do not merge. Preserve PR #20's incomplete status and PR #27's descriptive status regardless of this fresh result.

After this study, **do not automatically start another synthetic cap/penalty rescue loop**. Propose one next text-representation or estimated-g admission study, with its own data provenance, grouped splits, identity/response semantics, support coverage, and fixed B1/B2/B3 controls. Distinguish empirical predictive evaluation from any claim that the conditional .009 bound transports to estimated g. Corpus production, scholarly certification, and PR #18 remain separate workstreams.
