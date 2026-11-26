# Mathematical diagnosis and next method boundary

This note derives the proposed diagnostics. It does not report a new fitted model or qualified scientific result.

## 1. Personal optimization is a small strongly convex problem

For one person and a fixed shared basis, let

\[
\theta=(b,u),\quad A_i=[I_3\ F_i],\quad F_i[c,:]=V_cz_i.
\]

The personal objective is

\[
J_s(\theta)=\frac1k\sum_i
\left[\log\sum_c\exp(g_{ic}+(A_i\theta)_c)
-g_{i,y_i}-(A_i\theta)_{y_i}\right]
+\frac12\theta^\top D\theta.
\]

For M1, \(D=\operatorname{diag}(.6,.6,.6,.06,.06)\). B3 has only the first three coordinates. Its Hessian is

\[
\nabla^2J_s(\theta)=
\frac1k\sum_i A_i^\top
\{\operatorname{diag}(p_i)-p_ip_i^\top\}A_i+D
\succeq D\succ0.
\]

Consequently each personal objective has a unique minimizer. The existing batch objective,

\[
J_S(\theta_1,\ldots,\theta_S)=S^{-1}\sum_sJ_s(\theta_s),
\]

has the same individual minimizers but gradients divided by S. Batch-mean stopping is not an invariant personal accuracy criterion.

This is a standard strongly convex optimization setting; see Boyd and Vandenberghe, [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), chapters 9.1 and 9.5, for the general framework. The weighted bounds below are derived here for the laboratory's objective.

## 2. Residual-to-prediction bounds

Write \(r_s=\nabla J_s(\hat\theta_s)\), using the unaveraged personal objective, and

\[
R_s=\|D^{-1/2}r_s\|_2.
\]

Strong monotonicity gives

\[
(\hat\theta_s-\theta_s^\star)^\top r_s
\ge\|D^{1/2}(\hat\theta_s-\theta_s^\star)\|_2^2.
\]

Apply weighted Cauchyâ€“Schwarz to obtain

\[
\boxed{\|D^{1/2}(\hat\theta_s-\theta_s^\star)\|_2\le R_s.}
\]

Set \(P=I_3-\mathbf1\mathbf1^\top/3\) and

\[
K_q=\|P A_qD^{-1/2}\|_2.
\]

The centering removes a common logit shift, to which softmax is invariant. Its Jacobian has spectral norm at most 1/2: each absolute row sum is \(2p_c(1-p_c)\le1/2\), and the Jacobian is symmetric. Therefore

\[
\|\hat p_q-p_q^\star\|_\infty
\le\|\hat p_q-p_q^\star\|_2
\le\tfrac12K_qR_s.
\]

The gradient of one log probability has Euclidean norm at most \(\sqrt2\), giving

\[
|\log\hat p_q(c)-\log p_q^\star(c)|
\le\sqrt2K_qR_s.
\]

For two computed solutions to the same personal objective, add their bounds through the common optimum. The batch-48 solution is not assumed exact.

A sharper class-pair statement uses the log-odds linearity:

\[
|\Delta\log(p_c/p_d)|
\le \|(A_q[c,:]-A_q[d,:])D^{-1/2}\|_2R_s.
\]

For ensembles or probability mixtures, use the component log-probability bounds. If component j has \(|\Delta\log p_j(c)|\le\epsilon_j(c)\), a mixture with fixed nonnegative coefficients has lower and upper log probabilities

\[
\log\sum_j w_j\hat p_j(c)e^{-\epsilon_j(c)}
\quad\text{and}\quad
\log\sum_j w_j\hat p_j(c)e^{+\epsilon_j(c)}.
\]

The coarser bound \(\max_j\epsilon_j(c)\) is also valid. Compute the sums in log space and use the original floor inside scoring logarithms. Clipping a log probability below at \(\log(10^{-12})\) is nonexpansive.

These are deterministic optimization-error enclosures, not confidence or credible intervals. Each anchored pair contrast contains eight signed log-probability terms. Sum their error bounds to obtain \(B_{\rm cell}\). If the recorded contrast error is \(e_{\rm cell}\), its squared error at exact personal minima lies in

\[
\left[
(\max\{|e_{\rm cell}|-B_{\rm cell},0\})^2,\ 
(|e_{\rm cell}|+B_{\rm cell})^2
\right].
\]

Average the interval endpoints over the originally declared cells and histories, divide by the unchanged oracle contrast denominator, and take square roots. A lower NRMSE bound above .5 establishes, conditional on the saved shared models and evidence, that personal optimization error cannot bridge the recorded contrast failure. A bound straddling .5 is uninformative; do not refit to shrink it or infer that the exact optimum would pass.

These bounds condition on the fitted V, fixed evidence and saved histories. They do not certify shared global optimality, statistical estimation, oracle correctness, or a true person's decision function. Evaluating residuals in float64 is not automatically an interval-arithmetic proof. Record the numerical evaluation allowance and distinguish analytic bounds from machine-rigorous certificates.

## 3. The 90% cap is extra to the expectation argument

The original rule was

\[
h_{\mathrm{cap}}(E)=\min\{\alpha(E-1)_+,\log10\},\quad
\alpha=.009,\quad
p_{\mathrm{cap}}=e^{-h_{\mathrm{cap}}}p_B+
(1-e^{-h_{\mathrm{cap}}})p_M.
\]

The proposed single diagnostic removes only the cap:

\[
\boxed{
h_\infty(E)=.009(E-1)_+,\qquad
p_\infty=e^{-h_\infty}p_B+(1-e^{-h_\infty})p_M.
}
\]

For every answer and support history,

\[
p_\infty(a)\ge e^{-h_\infty}p_B(a),
\qquad
[\ell_\infty(a)-\ell_B(a)]_+\le h_\infty(E)\le.009E.
\]

Under the original conditional-count null, \(\mathbb E_0[E]=1\), so

\[
\mathbb E_{H_s}[(L_\infty(H_s)-L_B(H_s))_+]\le.009.
\]

The arithmetic averaging of seed e-values requires no independence. For the general e-value framework and averaging property, see Vovk and Wang (2021), [E-values: Calibration, combination, and applications](https://doi.org/10.1214/20-AOS2020), [author manuscript](https://arxiv.org/abs/1912.06116).

The cap was a further bound on how far a single history could move from B3. Removing it preserves the stated expectation argument but allows larger realized losses on rare histories. No per-person, finite-cohort, or high-probability guarantee follows. The coefficient \(\alpha=.009\), evidence, prior, shared basis, penalties, histories and seed aggregation all remain fixed in the diagnostic.

This new rule is post hoc and uses exposed, numerically unqualified predictions. Even if its observed metrics pass every former threshold, it cannot qualify PR #20 or serve as fresh confirmation.

## 4. What the saved evidence permits

The cap begins at

\[
E=1+\log(10)/.009\approx256.8428.
\]

There are 153 capped active rows among 192 active person-history rows, and zero capped inactive rows among 192 inactive rows. Thus the uncapped rule changes only active rows in these particular saved histories. Every observed inactive prediction is unchanged algebraically.

The count is not a prediction about future inactive histories. In particular, 190 observed inactive rows fell back exactly to B3, so their zero excess loss is not a comprehensive test of the rare-event expectation bound.

Use the original scalar log evidence. Compute h with expm1 when log evidence is positive, retain \(\log\beta=-h\), and compute

\[
\log p_\infty(c)=
\operatorname{logaddexp}
(-h+\log p_B(c),\ \log(1-e^{-h})+\log p_M(c)).
\]

For h=0 return B3 exactly. Compute \(\log(1-e^{-h})\) stably. Do not obtain the baseline coefficient by subtracting a rounded weight from one. The largest observed h is approximately 1133, so its exponent may underflow in float64; retain the finite log coefficient and report underflow explicitly. Do not add a replacement cap, tune a floor, or renormalize clipped prediction vectors. The historical scoring floor remains 1e-12 inside logarithms only.

For rows where the cap was inactive, check the independently calculated mixture against the saved ES prediction and preserve that saved row exactly in the derived prediction artifact. This makes unchanged inactive predictions transparent without hiding discrepancies.

## 5. Why contrast and NLL differ

For probabilities \(p_M=(.99,.005,.005)\) and \(p_B=(1/3,1/3,1/3)\), their fixed .9 mixture has first-class probability about .9243 and second-class probability about .03783. The first-to-second log-odds falls from \(\log198\approx5.288\) to approximately 3.196. This is an algebraic illustration, not a fitted result.

A modest probability floor can substantially shrink extreme log-odds while retaining a useful probability assigned to the dominant answer. The laboratory's loss and contrast therefore measure distinct properties. Preserve both original metrics; do not relax the contrast threshold because a different loss looks favorable.

Report ordered differences in contrast mean-squared error as well as NRMSE. The controls M1, FIXED_MIX, ES and the uncapped ablation help describe which transformation changes the saved predictions. They do not identify a unique causal decomposition of unknown future-person performance.

## 6. Returning to text and embeddings

The broader target remains

\[
z=\phi(q,C(q)),\qquad
p_s(a\mid q,C(q),H_s)
=\operatorname{softmax}_a\{g(q,C(q))+b_s+F(q,C(q))u_s\}.
\]

Numerical adaptation, representation quality and the population predictor g are separate questions. A useful text baseline can be evaluated empirically without claiming the .009 theorem. The theorem should not become an indefinite prerequisite for every text experiment.

If that theorem is transported to an estimated \(\hat g\), training on other people establishes an information boundary but does not establish a correct conditional null. Conditional on training and support questions, suppose one justified C applies uniformly to every feasible count vector n and every ordered response assignment with those counts:

\[
\sup_y Q_0^{\mathrm{true}}(y\mid n)/\widehat Q_0(y\mid n)\le C.
\]

Then any e-value valid under \(\widehat Q_0\) has true-null expectation at most C. The uncorrected expected-loss bound becomes .009C; using \(\widehat E/C\) can retain the original budget when C is justified independently. If instead a known C(n) varies with the observed count vector, the conditional bound is .009C(n), the unconditional bound is .009 times the true-null expectation of C(N), and \(\widehat E/C(n)\) is still conditionally valid.

For example, if remaining logit errors after removing one question-independent vector of class offsets and question-wise common shifts obey \(\|\Delta g_i\|_\infty\le\delta_i\), every assignment's score error is at most \(\sum_i\delta_i\). Its conditional normalizer has the same bound, so a conservative result is

\[
C\le\exp(2\sum_i\delta_i).
\]

This is a sufficient bound derived here, not a claimed available calibration guarantee. At limited history it can be very conservative. Any future claim must specify common answer meanings, independent-response assumptions, outcome-blind support selection, and how error in g is controlled.

The next handoff must distinguish an empirical text-prediction route from a theorem-preserving route. Neither an attractive embedding plot nor k-nearest-neighbor behavior establishes either route's predictive validity.
