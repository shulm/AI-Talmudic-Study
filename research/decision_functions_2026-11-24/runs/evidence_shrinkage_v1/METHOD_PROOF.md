# Conditional evidence and a bounded personalization mixture

Status: proposed method for `evidence_shrinkage_v1`, not an executed performance result. The construction below is a protocol proposal; no novelty or empirical success is attributed to its cited foundations.

## 1. Question and assumptions

For a new person, let H contain k=16 question-answer observations with fixed three-class meanings. The numerical representation z and known shared logits g are available. A shared interaction basis V is trained using other people's labels, independently of this person's responses. The individual null is

$$H_{0,s}:\quad P(Y_i=c\mid z_i,g_i,b_s)=\operatorname{softmax}_c(g_i+b_s),$$

with an arbitrary unknown constant vector b_s. Conditional on this person's parameters and the questions, the categorical responses follow the declared independent generator. Question selection is fixed independently of these responses.

The active alternative adds a question-dependent personal component:

$$P(Y_i=c\mid u,b_s)=\operatorname{softmax}_c(g_{ic}+b_{sc}+u^\top V_cz_i).$$

The same learned V serves active and inactive people. Inactivity is an evaluator label only; the learner is not supplied with the true status, true u, true b, query responses, or oracle probabilities.

The method builds on two ideas: conditional likelihood can eliminate nuisance offsets, and a normalized likelihood ratio against a simple conditional null has null expectation one. The latter is a standard e-variable construction; see Grünwald, de Heide and Koolen, *Safe testing* (2024), especially its definition and simple-null Bayes-factor identity. [Author manuscript](https://ir.cwi.nl/pub/34779/34779.pdf); [journal DOI](https://doi.org/10.1093/jrsssb/qkae011).

## 2. Condition on counts to remove the personal offset

Let n_c be the number of support answers equal to c, and let

$$\mathcal Y(n)=\{y\in\{0,1,2\}^k:\operatorname{counts}(y)=n\}.$$

For fixed u and V, define

$$Z_u(n)=\sum_{y'\in\mathcal Y(n)}\exp\!\left[\sum_i g_{i,y'_i}+u^\top\sum_i V_{y'_i}z_i\right].$$

Then the conditional support likelihood is

$$Q_u(y\mid n,g,z,V)=\frac{\exp[\sum_i g_{i,y_i}+u^\top\sum_i V_{y_i}z_i]}{Z_u(n)}.$$

To see the cancellation, write the unconditional likelihood as

$$\frac{\exp[\sum_i g_{i,y_i}+\sum_c n_cb_{sc}+u^\top\sum_i V_{y_i}z_i]}{\prod_i\sum_c\exp(g_{ic}+b_{sc}+u^\top V_cz_i)}.$$

Across assignments with the same n, both the b-dependent count term and the product of per-question denominators are constant. Conditioning removes them. Thus Q_0 is a known conditional null for every b_s.

**Do not substitute fitted B3 probabilities for Q_0.** Fitting a personal offset on the tested responses and using the fitted probabilities as a simple null would not supply this identity. Use the known g and exact conditional normalizer. Evidence calculations use stable log arithmetic without the scoring probability floor.

The assumptions matter: an estimated or misspecified g need not satisfy this conditional null (a question-independent class shift can be absorbed into b); dependence between responses or adaptive outcome-driven support selection also requires a new argument. Question-specific answer inventories cannot automatically use counts of common class labels.

## 3. A fixed training-only alternative distribution

For each shared initialization j, retain its fitted training-person coordinates u_jt, t=1,...,S, from the full saved optimizer vector. Set S=96 and define the finite symmetric prior

$$\Pi_j=\frac1{2S}\sum_{t=1}^{S}(\delta_{u_{jt}}+\delta_{-u_{jt}}).$$

Use every training vector with equal weight. Do not filter by true activity, fit quality, norm, target-person counts or target responses. Add no extra atom and tune no scale. Repeated/zero atoms retain their declared weight. Each seed's prior stays paired with that seed's V; latent coordinates from different seeds are not averaged.

For each seed,

$$E_j(y)=\int\frac{Q_u(y\mid n,g,z,V_j)}{Q_0(y\mid n,g)}\,d\Pi_j(u),\qquad E(y)=\frac13\sum_{j=1}^{3}E_j(y).$$

Conditional on the training data, questions and counts,

$$\mathbb E_0[E_j\mid n,\mathrm{train},g,z]=\sum_{y\in\mathcal Y(n)}Q_0(y)\int\frac{Q_u(y)}{Q_0(y)}d\Pi_j(u)=1.$$

Therefore the fixed arithmetic mean E also has conditional null expectation one. No independence between seed-specific statistics is needed. This averaging principle is also studied in Vovk and Wang (2021), *E-values: Calibration, combination, and applications*, [DOI](https://doi.org/10.1214/20-AOS2020), [author preprint](https://arxiv.org/abs/1912.06116). Taking the maximum, optimizing the prior on the target history, or averaging fitted latent vectors across unaligned seeds would be different procedures. Evidence from the two distinct histories must not be combined into one nominal 16-observation decision.

E is evidence against the declared null, not a posterior probability of individuality. The later mixing weight is a decision rule, not a calibrated estimate of a latent person's type.

## 4. Exact normalizers by dynamic programming

Let a_i,c(u)=g_i,c+u^T V_c z_i. Define a recursion over count vectors m:

$$Z_{u,0}(0,0,0)=1,\qquad Z_{u,t}(m)=\sum_{c:m_c>0}e^{a_{t,c}(u)}Z_{u,t-1}(m-e_c).$$

All other initial states are zero. Implement the recurrence in log space using log-sum-exp. For k=16 and three classes, there are exactly 153 feasible final count vectors. One forward table per seed/history can return every count vector simultaneously, for 192 prior atoms plus the u=0 null normalizer. The table is shared across all people observing that same question set. Per-person computation then uses its observed count vector and observed sufficient sum.

Store feasible count vectors and finite final log normalizers. Internal impossible states may use negative infinity; do not serialize them as invalid JSON or confuse them with finite final states. Do not use Monte Carlo permutations, asymptotic chi-square approximations, or target-specific optimizer fits.

Recursive conditional-likelihood calculations have an established precedent in Gail, Lubin and Rubinstein (1981), *Likelihood calculations for matched case-control studies and survival studies with tied death times*, [DOI](https://doi.org/10.1093/biomet/68.3.703). Its inspected abstract supports that historical connection; the explicit three-class recurrence above is derived directly here and must be independently checked by enumeration on small deterministic cases.

## 5. One continuous probability mixture

Let p_B and p_M be the B3 and three-seed M1 probabilities fitted on the same person's same history. Fix epsilon=0.009 nats and eta=0.9 before all scientific fitting:

$$h(E)=\min\{\epsilon(E-1)_+,-\log(1-\eta)\},$$

$$w(E)=1-e^{-h(E)},\qquad p_{\rm ES}=(1-w(E))p_B+w(E)p_M.$$

The weight is zero for E<=1, increases continuously thereafter, and never exceeds 0.9. At the cap, at least 10% of B3 remains. The cap begins at E=1+log(10)/0.009, approximately 256.8427881. These constants come from a declared risk budget and baseline floor, not a search over C/D or future outcomes.

Use log E for stable calculation: when log E<=0, set w=0; above the fixed cap threshold, set h=log(10); otherwise compute h=epsilon*expm1(log E) and w=-expm1(-h). Do not overflow exponentials, average log evidence instead of evidence, or select a favorable initialization.

## 6. Expected null loss bound

For every history, question and answer,

$$p_{\rm ES}(a)\ge(1-w)p_B(a)=e^{-h(E)}p_B(a).$$

Consequently,

$$[-\log p_{\rm ES}(a)+\log p_B(a)]_+\le h(E)\le\epsilon E.$$

The same holds for expected query log loss and its positive excess. Under the declared individual null,

$$\mathbb E_{H_s\mid H_{0,s}}[(L_{\rm ES}(H_s)-L_B(H_s))_+\mid\mathrm{train},g,z,b_s]\le\epsilon=0.009.$$

This uses the tower property over the count vector. B3 and M1 may both be fitted on the tested history; their data dependence does not invalidate the pointwise mixture inequality. The bound does not require the fitted V to equal the true interaction basis, nor the alternative prior to describe the true population. Those choices affect power.

The scoring convention clips only inside the logarithm at delta=1e-12. Since exp(-h)<=1,

$$\max\{p_{\rm ES},\delta\}\ge e^{-h}\max\{p_B,\delta\},$$

so the same inequality holds for the clipped scores. Do not renormalize clipped probability vectors; the predictions remain the original normalized mixture.

This is an expectation over possible support responses, conditional on the stated model and training/questions. It is not a guarantee for every observed history, every finite realization, every person simultaneously, or a misspecified shared predictor. It also does not imply that positive-person recovery passes. A mean over the two declared histories retains the expectation bound by linearity even when their observations overlap; combining their evidence would change the procedure.

## 7. What the experiment must distinguish

Use the same shared mixed-population V and the same .06/.6 adaptation for every compared method. B3 uses offset penalty .6. The fixed mixture p_fixed=.1*p_B+.9*p_M controls for simple dilution. Comparing evidence shrinkage with that fixed mixture isolates the contribution of history-dependent weighting more directly than comparing only against raw M1.

The primary four empirical gates remain: active expected-NLL gain>=.05, active oracle-gap recovery>=.5, active contrast NRMSE<=.5, and inactive expected-NLL degradation<=.01, separately on every fresh realization. The mathematical expectation bound does not replace these observed gates or excuse a failure. Report the entire distribution of evidence/weights, support counts, positive recovery and inactive losses.

The fixed alternative prior, shrinkage constants and model configuration cannot be adjusted after outcomes. If the method protects inactive people but loses active contrast, report the power/recovery limitation. If observed inactive loss exceeds the point gate despite the theorem assumptions and verified implementation, preserve the finite-realization failure and distinguish it from refutation of an expectation bound.

## 8. Generalization boundary

The probability-mixture loss argument applies to arbitrary answer predictors when an appropriate nonnegative null-valid evidence statistic is available. The conditional-count construction is specific to the known-base, fixed-label categorical model. Arbitrary fixed features learned without the target responses do not themselves invalidate the e-value identity; their usefulness affects power. A later text study must separately justify the null distribution when g is supplied by an estimated population predictor, and retain valid common class meanings and the response model. Neither the theorem nor synthetic success validates scholarly attributions or newly extracted corpus labels.

The source foundations are general statistical methods; the proposed four-realization experiment is one controlled application. This is the intended separation between a general modeling idea and the eventual Talmudic corpus use.
