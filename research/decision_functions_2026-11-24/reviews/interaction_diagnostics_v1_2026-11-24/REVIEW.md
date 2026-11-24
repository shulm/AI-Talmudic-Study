# Review: interaction recovery, null failure, and the next regularization study

Date: 2026-11-24. Reviewed delivery: `6da06a4b01bb825bcf4ad4b13c61648d6ee82220`. Pre-fit checkpoint: `5fc8cf48394b4e620a75be8e8f92054a6c02a451`.

## 1. Decision

**Accept D0–D3 as completed diagnostic work with the documented verification boundary. Preserve the overall synthetic failure. Revise D4's proposed parameterization before executing the next study.**

The new work resolves two important uncertainties from the first pilot. The head can learn a known interaction from informative numerical features, and the original DICES objective has a zero-interaction global optimum at every tested penalty. This explains the original collapse without establishing that the data lack useful person–question interactions.

The weak-penalty synthetic model also invents enough interaction under a known null to exceed the fixed degradation gate. That limitation remains a substantive result. It cannot be removed by rounding, switching retrospectively to another reported penalty, or treating successful software checks as successful scientific qualification.

No result-invalidating leakage, likelihood-scaling defect, certificate-scaling defect, or replay-arithmetic design error was found in the inspected source. This is a scoped review, not a proof that all possible defects have been excluded. The review did not access the original private arrays or matrices and did not independently reproduce their numerical contents.

## 2. What the diagnostics now establish

The pinned [diagnostic report](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/DIAGNOSTIC_REPORT.md) and [synthetic results](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/synthetic_results.json) support the following distinctions:

| Question | Current evidence | Limit |
| --- | --- | --- |
| Can saved pilot arithmetic be reproduced? | Executor ran the new verifier: 171 probability arrays, 24 paired-loss arrays, 213 comparisons, maximum reported discrepancy zero. | This review inspected code/receipts, not private arrays; replay does not regenerate predictions from weights. |
| Can the numerical head recover an interaction? | At lambda 0.001: expected-NLL gain 0.64022614, oracle-gap recovery 96.028%, contrast NRMSE 0.203964. | One generated realization with informative two-dimensional features and 96 supports. |
| Does that setting preserve the null adequately? | Expected-NLL degradation 0.01194930, versus maximum 0.01. | Gate fails; predicted null contrast RMS is 0.393161 although the oracle contrast is zero. |
| Why did original DICES M1 collapse? | All three training certificates place zero interaction at a global optimum of the specified objective. | This is not a claim about weaker penalties, new representations, or held-out interaction benefit. |

The null failure exceeds its gate by `0.0019493024944701263` NLL. This is many orders above numerical equivalence scales; it is not a floating-point near-tie. Expected NLL integrates over the known query-response distribution, so sampled query labels do not cause this metric's variation. Training and support label noise remain.

All reported penalties have a limitation under the original synthetic gates:

| Original lambda | Positive expected-NLL gain | Contrast NRMSE (maximum 0.5) | Null degradation (maximum 0.01) | All predictive gates |
| ---: | ---: | ---: | ---: | --- |
| 0.001 | 0.640226 | 0.203964 | 0.0119493 | Fail: null |
| 0.1 | 0.527291 | 0.547415 | approximately zero | Fail: contrast |
| 1 | approximately zero | approximately 1 | approximately zero | Fail: recovery |
| 10 | zero | 1 | zero | Fail: recovery |

This review recomputed the expected-gain and oracle-gap-recovery arithmetic for all 16 published rows; maximum discrepancy was zero. The probabilities underlying those rows were not available here.

## 3. D0 and D1 are meaningfully improved

The new [replay implementation](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/labs/decision_functions_diagnostics/replay.py) reads existing evidence without invoking a fitter or the historical scoring batch. It checks exact key sets, shapes, finite normalized probabilities, original public/private hashes, unchanged consumed bytes, declared metrics, and original bootstrap contrasts. The 213 comparison count reconciles with the inspected loops.

The [replay receipt](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/replay_receipt.json) correctly limits the result: arithmetic replay does not prove the historical execution used the reconstructed history permutations, regenerate predictions from weights, or recover missing development optimizer logs. The original development audit remains `RECOVERED_SELECTION_ONLY`.

The new [ledger validator](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/labs/decision_functions_diagnostics/core.py) rejects empty or incomplete evidence. Exact expected, started, and completed IDs must match, as must their configuration metadata. Optimizer fields must exist and be finite; unsuccessful termination is rejected. Immutable publication prevents a second completion from replacing the first.

Independent, non-fitting checks during this review confirmed that valid records pass and empty, missing, incomplete, unsuccessful, and colliding records are rejected. Read-only validation of the full exported ledgers confirmed:

- 104 synthetic records: 24 shared fits and 80 adaptation batches, accounting for 1,952 personal solves.
- Three human training-intercept batches, accounting for 186 personal solves.
- Both exact expected-ID mappings agree with the predeclared protocol.

All six profiled command records report exit zero. Their fields sum to 22.109375 sampled CPU seconds and 36.421000 profiled wall seconds; the maximum sampled child RSS is 105,226,240 bytes. These are the stated process measurements, not total end-to-end resource use. Documentation/Git operations and sampling limitations remain disclosed.

## 4. The zero-interaction certificates are mathematically coherent

For fixed shared logits, the original model fits

$$
\ell_{sic}=g_{ic}+b_{sc}+u_s^\top V_c z_i
$$

with penalty

$$
\frac\lambda2\left(\|V\|_F^2+
\frac{\|U\|_F^2+\|b\|_F^2}{S}\right).
$$

Flatten $V$ into $B$ and put $W=UB$. Minimizing over factor scales induces $(\lambda/\sqrt S)\|W\|_*$. At the intercept-only optimum, zero interaction is globally optimal in the convex relaxation when

$$
\|G\|_{\mathrm{op}}\le \lambda/\sqrt S.
$$

Because zero belongs to every allowed rank class, the certificate also applies to every tested rank. Increasing rank cannot overcome this particular optimum.

The [certificate implementation](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/labs/decision_functions_diagnostics/head_v1.py) uses the correct class–feature flattening and $1/(SN)$ gradient normalization. It also uses the correct **per-person** intercept residual

$$
r_s=\frac1N\sum_i(p_{si}-e_{y_{si}})+\lambda b_s.
$$

Strong convexity and the softmax Jacobian bound yield

$$
\|\Delta G\|_{\mathrm{op}}
\le
\frac{\|Z\|_{\mathrm{op}}\|r\|_F}{2S\sqrt N\lambda},
$$

which agrees with the implementation. This residual is not the globally averaged optimizer gradient; confusing the two would introduce an erroneous person-count factor.

Independent arithmetic from the published [certificate fields](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/human_certificate.json) gives:

| Lambda | Spectral norm | Threshold | Positive margin | Margin / reported error allowance |
| ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.002618463452 | 0.012700012700 | 0.010081549248 | about 93,469 |
| 1 | 0.002545295340 | 0.127000127000 | 0.124454831661 | about 69.9 million |
| 10 | 0.002531989071 | 1.270001270002 | 1.267469280931 | about 17.55 billion |

The weakest original penalty is therefore not borderline. The floating-point allowance is heuristic, not an interval-arithmetic proof, as the report states. The large margins make the numerical conclusion persuasive conditional on the reported input matrices.

The original training-label archive did not have a historical pinned hash. The new verifier reconstructs that matrix from the pinned source CSV and checks equality. This is a coherent provenance repair without refitting; the actual private-source equality remains executor-reported in this review.

## 5. Material correction to D4: two candidates are equivalent

The proposed next objective separates personal-offset shrinkage from interaction shrinkage:

$$
J=\operatorname{CE}
+\frac{\lambda_V}{2}\|V\|_F^2
+\frac{\lambda_U}{2S}\|U\|_F^2
+\frac{\lambda_b}{2S}\|b\|_F^2.
$$

This separation is useful. However, under the proposed consistent new-person adaptation penalty, $\lambda_V$ and $\lambda_U$ do not define two independent statistical regularization strengths. For $t>0$, the transformation

$$
\lambda'_V=t\lambda_V,\quad
\lambda'_U=\lambda_U/t,\quad
V'=V/\sqrt t,\quad U'=\sqrt t\,U
$$

preserves shared logits and the full training penalty. Rescaling an adapted personal vector in the same way preserves support logits and its $\lambda_U$ penalty. At corresponding optima, adapted predictions are unchanged.

The effective interaction strength is

$$
\rho=\sqrt{\lambda_V\lambda_U},
\qquad
\text{effective penalty}=\frac\rho{\sqrt S}\|W\|_*.
$$

The four pairs in the [original proposal](https://github.com/shulm/AI-Talmudic-Study/blob/6da06a4b01bb825bcf4ad4b13c61648d6ee82220/research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/NEXT_PROTOCOL_PROPOSAL.md) reduce to:

| Proposed pair | Product | Effective rho |
| --- | ---: | ---: |
| (0.001, 0.01) | 0.00001 | 0.0031622776601683794 |
| (0.001, 0.1) | 0.0001 | 0.01 |
| (0.01, 0.01) | 0.0001 | 0.01 |
| (0.01, 0.1) | 0.001 | 0.03162277660168379 |

The middle two are the same regularized predictive family. Different finite-optimizer results would indicate parameterization/conditioning sensitivity, not a distinct statistical model. The original tie rule by larger $\lambda_U$ therefore has no statistical interpretation independent of factor scaling.

**Use the canonical choice $\lambda_V=\lambda_U=\rho$, keep $\lambda_b=0.1$, and test three distinct rho values.** Validate the rescaling identity with objective/logit calculations that require no fit. Do not spend a competing-candidate fit on the duplicate unless explicitly studying numerical conditioning.

The certificate for this new parameterization must also separate its arguments: use residual $r_s=\operatorname{mean}(p-y)+\lambda_b b_s$, error denominator $\lambda_b$, and threshold $\rho/\sqrt S$. Reusing a single `lam` for all three would silently undo the intended separation.

## 6. Use the saved budget for a second generated realization

V1's seeds 11, 29, and 47 initialize models on the **same** generated people, questions, supports, and labels. They are not three independent synthetic datasets. One generator seed and one categorical-label seed produced the evidence. In addition, the successful control uses 96 supports in two dimensions, versus 16 supports and 384-dimensional embeddings in DICES. The result demonstrates head capability, not natural-language representation adequacy or small-history suitability.

The revised design retains the proposed 24 shared-fit cap:

- **18 selection fits:** three distinct rho values, two regimes, three initialization seeds, on the first new realization's training/development partitions.
- Freeze a single rho using development only.
- Evaluate the selected first-realization models once on their held-out block.
- **Six independent-realization fits:** selected rho, two regimes, three initialization seeds, on a second predeclared realization; evaluate its held-out block once.

Both generator/label seed pairs and every threshold are fixed before the first fit. The second realization is materialized only after selection is frozen. Its failure cannot trigger a new rho choice, a threshold change, or another realization. Both held-out realizations must satisfy the predictive gates separately; pooling cannot hide a failed null.

This gives a stronger engineering diagnostic within the existing budget. Two realizations still do not establish universal null control or human-domain generalization.

## 7. Provenance and independent-review boundary

Public Git-tree comparisons show all 42 original pilot laboratory/run files retain their blob identities. Within the diagnostic pre-fit checkpoint, only the ledger helper and the additive line-ending rule changed among already-present files. The likelihood, fitting, synthetic generator/scorer, certificate implementation, replay code, and synthetic protocol retain their checkpoint identities.

The helper change strengthens start-record identity and required finite optimizer fields. Earlier receipts identify its earlier hash; later audit receipts identify the final hash. Exact per-file hashes are essential: the pre-fit `code_commit` alone does not identify every later verification addition.

The public protocol issue comment was posted at 21:02:00 UTC, and the earliest local synthetic ledger start is recorded at 21:02:00.863 UTC. These are different clocks with limited timestamp resolution; no independent sub-second ordering is claimed. The immutable pre-fit checkpoint and draft PR were already published. No evidence of result-dependent fitting/protocol changes was found.

This review independently inspected code and public records, recalculated scalar arithmetic, validated exported ledgers, and tested ledger failure paths without fitting. It did not access either Windows cache, reproduce the 171 original arrays, recompute the spectral norm from private training matrices, generate new model predictions, or run a new synthetic experiment. The attached receipt preserves these distinctions.

Parallel PR #8 extends PR #5 using already-exposed SRO outcomes. Its metadata was read for coordination, not an independent scientific audit. The next prompt requires checking both parallel handoffs before proposing any future fresh human confirmation or duplicate scholarly preparation.

## 8. Next action

Use the [next-agent assignment](NEXT_AGENT_PROMPT.md) and [machine-readable design](next_synthetic_design.json) to implement and freeze a new synthetic-only study. Keep the v1 null failure, the old pilot, and all private evidence unchanged. No new human fit, human evaluation, encoder acquisition, or corpus expansion is part of this assignment.

If the revised model cannot pass both recovery and null gates on the declared held-out realizations, record the failure and stop. If it passes, the next question is how well the validated head works with limited histories and learned text representations; human-corpus admission and representation experiments still need their own concrete protocol.
