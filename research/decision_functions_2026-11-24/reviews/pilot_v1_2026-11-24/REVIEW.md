# Independent review of the completed decision-function pilot

Review date: 2026-11-24. Reviewed final commit: `0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0`. Effective freeze: `4de12a1fb300a7c9e9d927591bc4b101f0e263a2`. This is an assessment of the completed experiment, not a replacement protocol or a new experiment.

## 1. Disposition

**Retain the pilot as a completed, qualified result. Personal history improved probabilistic prediction on this split. The experiment did not demonstrate an additional person–question interaction benefit.**

The executing agent already disclosed the numerical collapse, lower classification accuracy, and missing development optimizer logs. This review agrees with that narrow scientific interpretation. Source inspection found no evident algebraic gradient error, zero-initialization trap, test-label leakage in development, or error in the stated paired bootstrap. Those observations do not independently certify the unavailable private arrays or rule out all implementation defects.

Two validation gaps should be repaired before another human interaction experiment:

- The synthetic checks exercise valid probabilities and invariances but do not demonstrate recovery of an interaction that is known to exist.
- The recovered development log is empty, yet the freeze's convergence assertion passes on the empty list.

A third follow-up is reproducibility: commit a read-only verifier for the already-saved probability artifacts. The current final-verification JSON is an executor attestation without a committed generating script.

Keep the original literal `VALID_PILOT_POSITIVE_PRIMARY` output as historical evidence. The review's scientific assessment is **NO_RESOLVABLE_INTERACTION_GAIN**. Do not retroactively change the endpoint, replace the historical status, or present a newly chosen threshold as preregistered.

## 2. What the numbers establish

The following values are from the pinned [results summary](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/research/decision_functions_2026-11-24/runs/pilot_v1/results_summary.json). They are reported experimental results, not a replay of the original probability arrays by this reviewer.

| Model at 16 supports | NLL, lower is better | Accuracy | Multiclass Brier, lower is better |
| --- | ---: | ---: | ---: |
| B0 population frequencies | 0.782941 | 0.675837 | 0.483413 |
| B1 personal frequencies | 0.726287 | 0.648525 | 0.453094 |
| B2 shared text predictor | 0.772512 | 0.675837 | 0.474703 |
| B3 text plus personal class offsets | 0.720449 | 0.658692 | 0.444266 |
| B4 history kNN | 0.728098 | 0.661882 | 0.447894 |
| M1 text, personal offsets, and interaction | 0.720449 | 0.658692 | 0.444266 |

The reported M1-versus-B2 NLL improvement is `0.0520634350`, with paired two-way bootstrap interval `[0.0140724008, 0.0986191633]`. M1 and B3 are numerically indistinguishable on the saved-result summaries. Brier improves by approximately `0.030437`, while accuracy falls by approximately **1.71 percentage points**. Thus “improved probabilistic prediction” is the precise positive conclusion. Improvement in NLL and Brier alone does not isolate calibration from other aspects of predictive quality.

Correct histories beat shuffled histories by `0.0941414966` NLL for M1 and essentially the same amount for B3. The code averages ten fixed history derangements and three support draws. It does not report a confidence interval or randomization p-value for this contrast. Describe it as a substantial observed control contrast within this experiment, not a separately established significance result.

B1 is already close to B3: their descriptive NLL difference is only `0.0058383212`. No paired interval for this contrast is reported. This supports keeping simple personal-frequency and personal-offset models as serious baselines; it does not establish that text adds no value.

The primary M1-versus-B3 difference is `1.9145913755e-12` NLL, with reported interval `[1.6550291690e-13, 3.8049005896e-12]`. The maximum reported probability difference is `6.0072169461e-11`. The sign-only endpoint calls this positive because the interval excludes zero, but the bootstrap does not model numerical solver error. A consistent floating-point or stopping-tolerance difference can receive an interval above zero. This is not credible evidence of additional interaction.

The held-out block contains 22 people and 76 items in 55 input groups: 1,672 person–item targets. The three support draws reuse those same targets. They are not three independent samples of people. The implementation appropriately averages losses across draws at each person–item cell before bootstrap resampling.

## 3. Relation to the research question

The general objective remains

$$
\widehat P(a\mid q,C(q),H_s),
$$

where $q$ is a problem, $C(q)$ its available answers, and $H_s$ the observed history of person $s$. For this pilot the answer set is the same three classes for every problem.

Write $z_q=E(q)$ for the frozen text embedding and $g_c(z_q)$ for the shared B2 logit. B3 learns

$$
P_s(c\mid q,H_s)=\operatorname{softmax}_c\{g_c(z_q)+b_{s,c}(H_s)\}.
$$

Equivalently, if $p_0(c\mid q)$ is B2,

$$
P_s(c\mid q,H_s)=
\frac{p_0(c\mid q)\exp b_{s,c}}
{\sum_d p_0(d\mid q)\exp b_{s,d}}.
$$

This is a useful personalized function: people can receive different probabilities and different top answers. With three classes, the personal effect has two identifiable log-odds contrasts. However, its contribution to each class log-odds contrast is constant across questions:

$$
\log\frac{P_s(a\mid q)}{P_s(c\mid q)}
=g_a(z_q)-g_c(z_q)+b_{s,a}-b_{s,c}.
$$

M1 was intended to add

$$
\ell_{s,c}(q)=g_c(z_q)+b_{s,c}+u_s^\top V_c\tilde z_q,
\qquad \tilde z_q=z_q-\bar z_{\mathrm{train}}.
$$

A useful formal distinction is the difference in personal log-odds differences between two questions. Let $L_s^{a,c}(q)=\log(P_s(a\mid q)/P_s(c\mid q))$. Then

$$
D_{s,t}^{a,c}(q,q')=
\{L_s^{a,c}(q)-L_t^{a,c}(q)\}
-\{L_s^{a,c}(q')-L_t^{a,c}(q')\}.
$$

B3 forces $D=0$. M1 permits

$$
D_{s,t}^{a,c}(q,q')
=(u_s-u_t)^\top(V_a-V_c)(z_q-z_{q'}).
$$

The stronger research objective is to estimate such nonconstant personal responses to question content and improve held-out prediction. The pilot establishes useful personal offsets; it has not demonstrated that stronger capability. The result also does not refute its existence: shrinkage, limited supports, representation, signal size, and optimization are not yet distinguished.

## 4. Finding A: the synthetic pass is not a recovery test

The pinned [checks.py](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/checks.py) creates meaningful six-condition cases and person-specific rules. The subsequent model exercise uses random eight-dimensional features unrelated to those conditions or their text:

```python
z = rng.normal(size=(24,8))
y = shared[:8,:24]
```

The assertions test normalized finite probabilities, person-renaming invariance, zero-support fallback, derivatives, and some evaluation boundaries. They do not require recovery of planted personal interactions on new people and questions. A model that always becomes B3 can pass.

**Next requirement:** first test the learning head using informative numerical features generated with a known nonzero low-rank interaction. Include an intercept-only null condition, sufficiently informative supports, held-out people/questions, an oracle predictor, and explicit recovery criteria. Control person class frequencies so a personal class prior cannot by itself satisfy the intended recovery criterion. Use predictive recovery, not raw factor alignment: factor coordinates are not unique, including under orthogonal rotations. Only after the head works should the text-to-embedding path be tested separately.

This is also a correction to the original planning requirements: an operational smoke test and a learning positive control must be separate acceptance gates.

## 5. Finding B: missing optimizer records pass the freeze gate

The recovered [development_results.json](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/research/decision_functions_2026-11-24/runs/pilot_v1/development_results.json) contains `optimizations: []`, while reporting 30 shared fits and 1,800 development adaptation person-solves. The [freeze check](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/freeze.py) uses:

```python
assert all(o['success'] for o in dev['optimizations'])
```

This succeeds for an empty list. In [models.py](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/models.py), the optimizer wrapper records unsuccessful termination but raises only for nonfinite loss. Without the development records, convergence of every candidate cannot be independently verified.

The selection recovery is corroborated: all 25 configuration records and selected settings exactly match the separately saved `DEV_RESULTS.md`, and the chosen settings follow the recorded development minima. The 165 retained test optimization records all report success. These checks do not restore the lost development convergence evidence.

**Next requirement:** use append-only, uniquely identified stage records, atomic summaries, expected counts and configuration identities, and an explicit convergence policy. Missing records must produce an incomplete audit state. Keep the old recovery attestation; do not manufacture replacement logs by rerunning the completed experiment.

## 6. Finding C: reproduce verification without rerunning the test

The pinned [final_verification.json](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/research/decision_functions_2026-11-24/runs/pilot_v1/final_verification.json) reports checks of 171 probability arrays and 24 paired-loss arrays. No committed script generating that verification report was found in the inspected laboratory/run files.

The regeneration command in the prediction manifest calls [evaluate.py](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/evaluate.py), whose historical gate requires both local HEAD and the execution branch remote to equal the freeze SHA. The execution branch has advanced to the final report, so that command cannot run unchanged now.

Preserve the historical gate. A new read-only verifier should load existing arrays, check source and artifact hashes, recompute only the already-declared metrics/contrasts, and compare them to the published outputs. It must not train, generate new predictions, reset the remote branch, or overwrite `pilot_v1`. Verification should report disagreements and stop; it should never repair the evidence silently.

## 7. A diagnostic that can explain interaction collapse

The source gradients match the specified objectives on analytic inspection. Both training factors receive random initialization, so the code does not have a both-factors-zero initialization trap. The regularization is a more informative next diagnostic than immediately increasing model size.

For $S$ training people, $N$ training questions, and centered features, the implemented objective is

$$
J(U,V,b)=\frac1{SN}\sum_{s,i}\operatorname{CE}(\ell_{si},y_{si})
+\frac\lambda2\left(\|V\|_F^2+
\frac{\|U\|_F^2+\|b\|_F^2}{S}\right).
$$

Flatten $V$ to $B\in\mathbb R^{r\times 3d}$ and define $W=UB$. For any $W$ representable at that rank,

$$
\min_{UB=W}\frac\lambda2
\left(\|B\|_F^2+\frac{\|U\|_F^2}{S}\right)
=\frac\lambda{\sqrt S}\|W\|_*.
$$

Here $\|W\|_*$ is the nuclear norm. To see the scaling, put $A=U/\sqrt S$, so $AB=W/\sqrt S$, and minimize the balanced factor penalty. The singular-value factorization achieves the nuclear-norm value. Thus the factor model is a rank-constrained nuclear-norm-regularized residual classifier, with a separate quadratic personal-intercept penalty.

Keep the saved B2 logits fixed and optimize training-person intercepts $b^{(0)}$ with $W=0$ and the same $\lambda$. Define

$$
p^{(0)}_{sic}=\operatorname{softmax}_c(g_i+b_s^{(0)}),
\qquad
G_{s,(c,j)}=\frac1{SN}\sum_i
\left(p^{(0)}_{sic}-\mathbf1[y_{si}=c]\right)\tilde z_{ij}.
$$

The convex relaxation has a zero-interaction global optimum precisely when

$$
\boxed{\|G\|_{\mathrm{op}}\le\lambda/\sqrt S.}
$$

This follows from the nuclear norm's subgradient at zero and the zero intercept gradient at $b^{(0)}$. If the inequality holds, the zero interaction is also optimal at every allowed rank. If it fails, the leading singular vectors give a rank-one descent direction, so zero interaction is not optimal even at rank one.

For this pilot, $S=62$ and the selected $\lambda=0.1$ give threshold approximately `0.0127000`. **The actual gradient spectral norm has not been computed in this review. The condition has not been shown to hold.**

Compute it only on the training block, using the same feature center, frozen B2 parameters, and objective. Record intercept optimality residuals and the signed spectral margin; allow a borderline/uncertain outcome when numerical error could change the inequality. These are new diagnostic training-intercept solves and must be separately counted. They do not replace lost original logs.

If future penalties are separated as $\lambda_V\|V\|^2/2+\lambda_U\|U\|^2/(2S)+\lambda_b\|b\|^2/(2S)$, the corresponding interaction threshold is $\sqrt{\lambda_V\lambda_U/S}$. This offers a principled way to separate interaction shrinkage from personal-offset shrinkage. It is a proposed future model change, not a result of the pilot.

## 8. Evaluation strengths and remaining limits

Inspection of [prepare.py](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/prepare.py), [develop.py](https://github.com/shulm/AI-Talmudic-Study/blob/0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0/labs/decision_functions/develop.py), and `evaluate.py` supports the following design properties:

- People and input groups are separately partitioned. Support questions come only from training groups; models receive identical nested history question schedules.
- Development opens training/development outcomes, not test-query outcomes. B3, B4, and M1 share the selected B2 model. Seed probabilities are ensembled instead of selecting a favorable seed.
- M1 feature centering uses training questions. B4 uses the original normalized vectors for cosine similarity.
- History derangements preserve query ownership and question identities while replacing the person's support labels.
- The bootstrap resamples people and input groups, computes the declared macro-person contrast, and averages repeated-support losses before resampling.

The grouping rule detects normalized duplicate inputs and identical nonempty contexts, not every semantic paraphrase or shared topic. The result concerns held-out input groups, not certified new semantic topics. The interval is conditional on this split, selected model and representation, and fitted parameters; it does not cover arbitrary retraining or transfer to another decision domain.

Batch-averaged adaptation has mathematically separable personal objectives but globally applied solver tolerances. Numerical behavior can therefore depend on batch size. Future diagnostics should check this, without treating it as an established explanation of the observed history gain.

## 9. What this review independently checked

The accompanying [receipt](public_review_receipt.json) records the verification boundary. Public-source inspection and consistency checks established:

- All 19 protocol integrity-file SHA-256 values match the exported files.
- All 13 laboratory files have identical Git blob IDs at freeze and final commit; protocol, split/support manifests, development results, model manifest, and other frozen run files also retain their blob identities.
- The recovered 25-row development table and selected settings exactly match the independent Markdown table and recorded minima.
- All 165 retained test optimization records report success; the reported test adaptation count is 3,630 person-solves.
- The declared batch accounts for 171 prediction arrays: 72 model/budget/draw arrays, nine individual-seed arrays, and 90 shuffled-history arrays.

The original source membership files, embeddings, weights, and probability arrays were unavailable in this review environment. Consequently, this review did **not** independently check actual participant memberships, reconstruct predictions from weights, recompute reported confidence intervals from original losses, or verify the 171 private arrays. The executing agent's attestation remains distinct from this public review. No new human fits, predictions, or scores were produced here.

## 10. Continuation decision

Proceed with the bounded [diagnostic assignment](NEXT_AGENT_PROMPT.md). Preserve B3 as a strong baseline. Require a meaningful synthetic recovery gate, fail-closed audit records, and a numerical-equivalence policy distinct from a minimum worthwhile scientific effect before a new human experiment.

The sign-only primary rule was a weakness in the original plan as well as in its implementation. For a future protocol, declare both numerical resolution and scientific relevance before scoring. Do not retroactively declare a new practical threshold for this pilot.

All DICES pilot outcomes are exposed. Additional work on that corpus is development or exploratory follow-up, even if the split changes. Confirmation should use an independent corpus or demonstrably untouched units with a new frozen protocol and explicit overlap audit. This review assigns diagnostics and protocol preparation; it does not launch P4, a larger encoder search, full Talmudic corpus construction, or a new held-out human experiment.

### Parallel track discovered during publication

[PR #5](https://github.com/shulm/AI-Talmudic-Study/pull/5), delivery `6ca2dedc547144d7279696bd5322c1e39c7f03d3`, reports a separate SRO cross-task pilot and provisional scholarly-source preparation. Its [handoff](https://github.com/shulm/AI-Talmudic-Study/blob/6ca2dedc547144d7279696bd5322c1e39c7f03d3/research/individual_decision_model_2026-11-24/HANDOFF.md) records an inconclusive individual-specific transfer result and already-exposed test outcomes. Only its PR metadata and handoff were read for coordination; its code, arrays, and scientific conclusions were not audited in this review. The next agent should reconcile both branches' exposure histories before selecting a new confirmation dataset or repeating source preparation. The DICES numerical findings above remain a separate experiment.
