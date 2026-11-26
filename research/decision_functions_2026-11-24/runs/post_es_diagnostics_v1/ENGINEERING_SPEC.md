# Fixed personal-solver engineering suite

This specification is part of the H0â€“H4 assignment. No fixture was solved while preparing it. Scientific fitting is not authorized.

## Constants and identities

There are 48 people, indexed `p=8*b+m`, where `b=0..5` and motif `m=0..7`. Each person has 16 support rows and 12 query rows. Classes are indexed 0,1,2. M1 has rank 2 and the fixed, unlearned basis:

```json
{
  "V": [[[1,0],[0,1]],[[-1,1],[1,0]],[[0,-1],[-1,-1]]],
  "D_B3": [0.6,0.6,0.6],
  "D_M1": [0.6,0.6,0.6,0.06,0.06],
  "support_rows": 16,
  "query_rows": 12,
  "people": 48,
  "models": ["B3", "M1"],
  "layouts": ["singletons", "chunks7", "all48", "reverse48"],
  "formal_person_solve_attempts": 384,
  "wrapper_calls": 114,
  "scientific_fits": 0,
  "learned_shared_fits": 0
}
```

For a row index `i=0..n-1`, set `t=(2*i-(n-1))/n` and let `v_i` cycle through `[(1,0),(0,1),(-1,0),(0,-1)]` by `i mod 4`. Define `c_b=((2*b-5)/16)*(1,-1,0)` and `d=(1,-2,1)`. All label calculations below use support indices only; query labels do not exist. For every motif except 0, set `g_i=c_b+a_m*t*d`, with coefficients `a=[0,1/8,1/8,0,0,12,0,0]`. Query geometry/base use the same formulas with `n=12`; support geometry/base use `n=16`.

| Motif | Features z_i | Support labels y_i | Purpose |
|---|---|---|---|
| 0 | (0,0) | (i+b) mod3 | Exact known zero optimum; base override below |
| 1 | v_i | (i+b) mod3 | Unit features and approximately balanced hard labels |
| 2 | (1,0) | (i+b) mod3 | Constant, rank-deficient design |
| 3 | ((-1)^i,0) | ((i mod2)+b) mod3 | Collinear, separated labels |
| 4 | 8*v_i | (0,1,1,2)[i mod4] | High-scale separated features |
| 5 | v_i | (i+b) mod3 | Large opposing known-base logits |
| 6 | (0,0) | b mod3 | Single observed class and no interaction features |
| 7 | (t,0) | b mod3 | Symmetric collinear features with one observed class |

For motif 0 only, let `f_c` be the exact fraction of its 16 support labels equal to c. Set every support and query base row to `g_c=log(f_c)+(2*b-5)/16`. The additive final term is the same for all three classes. Thus theta=0 is the exact mathematical optimum for both heads despite the nonuniform counts (6,5,5 up to permutation). Blocks alter the class permutation and common logit shift without changing that identity.

Motifs 0 and 6 have interaction optimum u=0 because all features vanish. Motif 7 also has u=0 at the unique optimum: the fixed base is constant across support rows, the label is constant, and the support features sum to zero. Consequently its exact B3 and M1 query predictions coincide. These analytic identities are independent of the Newton implementation.

## Objective and sole algorithm

Keep the existing individual objective, averaged over that person's support rows, with the stated ridge matrix D. Do not divide gradients or Hessians by the number of people in a wrapper call. Use float64 and stable log-sum-exp/softmax. Work in `eta=D^(1/2)*theta` coordinates. Initialize eta=0 for every solve. At each iteration compute value, `g_eta=D^(-1/2)*grad_theta` and `H_eta=D^(-1/2)*H_theta*D^(-1/2)`.

Stop successfully only when `R=norm2(g_eta)<=1e-10`, checked on the current iterate. This stopping rule uses support data and fixed D only. Query features, labels, losses, and certificates are not solver inputs.

Otherwise solve `H_eta*direction=-g_eta` by Cholesky, without diagonal jitter. Check a finite descent direction. Backtracking candidates are exactly `alpha=2^(-j)` for j=0..39; accept the first candidate satisfying the ordinary Armijo condition `J(eta+alpha*direction)<=J(eta)+1e-4*alpha*dot(g_eta,direction)`. Define `eps64=2^-52`. One fixed roundoff safeguard applies to the full-step candidate only: when the predicted decrease `-dot(g_eta,direction)` is at most `64*eps64*max(1,abs(J))`, the full step may also be accepted if its independently recomputed residual strictly decreases and its objective is at most `J+64*eps64*max(1,abs(J))`. For every guarded acceptance, record old/new objective, old/new residual, positive predicted decrease, numerical allowance and the acceptance rule used. This safeguard handles objective differences below floating-point resolution; it never declares convergence or changes the residual target. No other acceptance allowance is permitted. At most 100 accepted Newton steps are allowed; after step 100, evaluate the residual once and accept only if the same residual criterion holds. No L-BFGS, gradient-descent, precision-switch, warm-start, or alternative-tolerance fallback is permitted.

Nonfinite values, a failed Cholesky factorization, a non-descent direction, exhaustion of 40 backtracking candidates, or failure of the residual criterion after 100 accepted steps is an engineering failure. Save its receipt. Do not count it as success because a library optimizer reports success. Continue remaining declared formal cases only if the failure is isolated and all computations remain finite; do not rerun the failed case. Abort the suite on corrupted inputs or nonfinite arithmetic. The expected complete inventory is384 attempts, not an entitlement to manufacture successful receipts.

## Layouts and exact accounting

Process layouts in the stated order, then heads B3,M1 within each layout. Canonical people are p=0..47. `singletons` submits each person separately; `chunks7` submits consecutive chunks with sizes7,7,7,7,7,7,6; `all48` submits all48; `reverse48` submits47..0. The wrapper must call the same single-person routine independently and reassemble outputs. Counts: 96+14+2+2=114 wrapper calls; 4*2*48=384 individual solver attempts. Every attempt starts at zero and has its own receipt. No response to another person may enter an individual's computation.

Before any formal solver invocation, freeze the exact fixture-array hash, derivative-check specifications, algorithm, tolerances, and schedule. The suite contains no scientific RNG seed, model selection, or learned shared fit. Derivative/value evaluations are not optimizer calls; account for them separately. No hidden development optimizer invocations are permitted under the stated384-call budget.

## Independent checks

1. Independently evaluate the scalar objective using a small loop-based implementation. At deterministic test point `theta_j=((p+3*j) mod11-5)/16`, compare the analytic gradient with central finite differences of that scalar objective, using coordinate step `2^-18`. Compare analytic Hessian columns with central finite differences of the already-checked gradient at the same step. Require normalized maximum discrepancies `max_abs_difference/max(1,max_abs_left,max_abs_right)<=2e-6`. There are exactly96 gradient and96 Hessian comparison blocks. None invokes an optimizer.
2. Require Hessian symmetry error <=`1e-12*max(1,max_abs_H)` and minimum eigenvalue of `H-D` >=`-1e-10*max(1,norm2(H))` at each of the96 test points. Require the full Hessian to be positive definite. These checks complement the analytic PSD proof; finite differences alone do not prove convexity.
3. After solving, recompute each residual independently of the solver's cached gradient. Record R and the comparison with the logged residual. Require discrepancy <=`1e-12*max(1,R_logged,R_recomputed)` and independently recomputed R<=1e-10. State that these are float64 numerical checks, not directed-rounding interval certificates.
4. For query design A=[I,F], P=I-11'/3 and K=norm2(P*A*D^(-1/2)), report `Kmax*R`. Require <=1e-8 as a post-solve engineering criterion, never a stopping input. The largest suite geometry has Kmax=sqrt(3*8^2/.06+1/.6)=sqrt(3201.6666666666665)<57, so the chosen support residual target gives substantial margin. Report probability error bounds K*R/2 and class log-probability bounds sqrt(2)*K*R.
5. After canonical reordering, require bitwise identical parameter and probability arrays for each person's four packaging layouts. This checks the wrapper's promised independence, not numerical truth; residual bounds, derivatives, and analytic motifs provide separate evidence.
6. Motif0: require theta exactly zero as initialized and predictions within1e-13 of its empirical-frequency vector. Motifs6/7: require interaction-coordinate norm<=1e-8 and B3/M1 query differences<=1e-8; also verify the observed differences lie within the sums of their residual-derived probability bounds plus a fixed1e-12 numerical comparison allowance. No theoretical threshold is expanded if any check fails.

The fixed derivative tolerances are engineering checks, not criteria for deciding scientific success. Do not choose new steps, fixtures, scales or tolerances after formal-suite outcomes. Report failures and stop for review.

## Historical contrast-uncertainty calculation without refits

For each saved personal head, compute its unscaled individual gradient and D-weighted residual at the saved parameters. Shared V, training-person prior atoms, scalar evidence, histories, and mixture weights stay fixed. Compute query probability/log-probability intervals using the analytic residual bounds. For an ensemble or mixture, combine component probability bounds with the original fixed nonnegative weights. Alternatively, a common maximum component log-probability error gives valid multiplicative bounds on the mixture. Clip only inside the subsequent log at the original1e-12 floor.

The map log(p) -> max(log(p),log(1e-12)) is nonexpansive, so the same log error bounds remain valid after clipping. Every anchored pair/class contrast uses eight signed log-probability terms. Sum the eight individual error bounds to obtain B_cell. If e_cell is the recorded contrast minus oracle contrast, exact-personal-minimum squared error lies between `max(abs(e_cell)-B_cell,0)^2` and `(abs(e_cell)+B_cell)^2`. Average in the original history/pair/query/class-pair order, divide by the original positive oracle contrast denominator, and take square roots.

If the resulting lower NRMSE bound exceeds0.5, report that optimization error in the personal heads cannot bridge the recorded contrast gap conditional on the frozen shared models/prior/evidence. If it overlaps0.5, report the bound as uninformative. Do not refit to tighten it. This does not certify shared global optimality or the true generative model, and it does not repair PR20's historical numerical status.
