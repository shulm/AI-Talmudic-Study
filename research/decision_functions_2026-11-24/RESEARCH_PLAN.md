# Continuation plan: learning individual decision functions from text

Version 1.0 — 2026-11-24. **Planning document; no experimental results are claimed.**

Repository baseline: `6014a75250ce536f8d1426c7fdbfa257d404e230`. Agent coordination takes place in [the GitHub issue](https://github.com/shulm/AI-Talmudic-Study/issues/2) and linked draft pull requests.

## 1. Objective and scope correction

Learn a shared family of decision functions from textual problems and sparse repeated observations of individuals. Predict what a specified decision-maker will answer on an unobserved problem. Establish the method first on general human-judgment data; subsequently examine transfer to Talmudic cases.

The earlier [attribution proposal, PR #1](https://github.com/shulm/AI-Talmudic-Study/pull/1), remains historical. Its pair-assignment target, two-person constraints, eight metric weights, and ten-percentage-point gate do not define this experiment. Source verification practices remain useful, but source collection and individual-function prediction are distinct tracks.

Four claims must remain separate:

- **Method generality:** the same algorithm works on different datasets.
- **Representation transfer:** a text encoder remains useful in a new domain.
- **Person adaptation:** a new person's function can be inferred from limited observations.
- **Domain transfer:** shared learned decision structure transfers to another domain.

One successful pilot supports only its declared task and split. It cannot establish all four claims or identify a unique internal reasoning mechanism.

## 2. Mathematical contract

Let $Q$ contain problems with all relevant stated conditions, $S$ identify decision-makers, and $A(q)$ contain admissible decisions. Let $C(q)\subseteq A(q)$ denote supplied alternatives when the observation presents a finite menu.

$$F(q,s)=f_s(q),\qquad f_s(q)\in\Delta(A(q)).$$

The deterministic case is a point-mass distribution. A categorical distribution is a model of uncertainty and observed variation, not a requirement that the underlying person consciously randomizes.

The available evidence for person $s$ is a support history:

$$H_s=\{(q_i,C_i,a_{si})\}_{i\in I_s}.$$

The primary target is:

$$\boxed{\widehat P_\theta(a\mid q,C(q),H_s)}.$$

An unseen arbitrary person ID with an empty history supplies no individual behavioral evidence. At $|H_s|=0$, use the population predictor. If behavior changes with circumstances or time, include the observable conditioning variables in the problem definition or explicitly limit the claim to the sampled context.

### 2.1 Representation and adaptation

$$z_q=E_Q(x_q),\quad v_{q,a}=E_{QA}(x_q,x_a),\quad u_s=\operatorname{Adapt}(H_s;\theta).$$

Question retrieval and candidate compatibility are different operations. For changing answer menus, embed the actual candidate in its question context; the string 'A', 'yes', or 'option 1' is not a transferable substantive answer.

One useful family, inspired by reward factorization [L4], is:

$$R_s(q,a)=R_0(q,a)+b_s(a)+\sum_{j=1}^{K}u_{s,j}R_j(q,a).$$

The personal class intercept applies to a fixed shared answer taxonomy. For changing candidate menus, omit it or compute it from candidate features; arbitrary new answer strings do not have pre-estimated personal intercepts.

Use softmax for mutually exclusive categorical choices. Pairwise preferences may use a logistic score difference, with ties modeled explicitly. Ordered ratings need their declared order; multiple accepted labels require a set-valued or multilabel observation model. Never silently convert uncertainty, ties, or multiple judgments into a majority binary label.

Inference of a small personal vector can minimize regularized support loss. A later history encoder or probabilistic $\pi(u\mid H_s)$ can replace point adaptation [L1, L5, L6]. Low-dimensional person coefficients do not require a linear text-to-decision relationship.

### 2.2 Metrics and text reconstruction

For retrieval, start with normalized encoder vectors and Euclidean distance. A learned linear map gives $d(q,q')=\|L(E_Q(q)-E_Q(q'))\|_2$ in the projected space. Reduced projections can collapse distinct texts; relevant conditions must be tested explicitly.

Raw hidden-layer extraction is a feature source, not evidence that distance captures decision-relevant distinctions [L8, L9]. Similar wording may conceal opposite conditions. Generic embedding and retrieval benchmarks diagnose the encoder, while personal-decision prediction requires the individual-label benchmarks below.

Latent person coordinates are not uniquely interpretable: jointly transforming person vectors and basis functions can preserve predictions while changing distances. For later comparison of people, prefer a declared reference distribution $\mu$ and:

$$d_\mu(s,t)=\left[\mathbb E_{q\sim\mu}\|P_s(\cdot\mid q)-P_t(\cdot\mid q)\|_2^2\right]^{1/2}.$$

This is a pseudometric on identities, measured through behavior on common questions. Do not call a learned axis a substantive reasoning principle without independent evidence.

There is generally no unique inverse embedding-to-text map. The first lab returns a probability distribution over declared answer labels or candidates. Free-form generation and explanation fidelity are later tasks.

## 3. Research questions and planned phases

| Phase | Question and work | Reviewable output |
|---|---|---|
| P0 | Can an existing general corpus support individual-function learning? Audit sources, IDs, coverage, target semantics, and access. | Data audit and source/schema manifests |
| P1 | Does the implementation enforce person/item separation and limited support? Build adapters, synthetic controls, splits, and simple baselines. | Executable lab and checked manifests |
| P2 | Does a small personal interaction model improve held-out development predictions beyond strong baselines? | Bounded development comparisons and controls |
| P3 | Does the preselected comparison persist on new people and held-out item groups? Freeze and score once. | Saved predictions, paired results, limits, agent handoff |
| P4 | Does the method work on a second human task with different answer structure? | Independently frozen semantic-inference or candidate-choice replication |
| P5 | What domain adaptation and source representation are needed for Talmudic cases? | Audited atomic cases and a domain pilot using the general protocol |

**The next agent is assigned P0–P3.** Later phases are the roadmap, not prerequisites for completing the first assignment. Run the final pilot evaluation automatically once validity and resource conditions are met; no additional owner checkpoint is required between the assigned phases.

## 4. Data strategy

### 4.1 Primary human pilot: DICES350

Use the official DICES350 release [D1]. Documentation describes 350 conversations evaluated by 123 raters (43,050 records before quality exclusions), with repeated person and item IDs. Verify actual downloaded counts rather than copying these as executed findings.

| Our field | Source field |
|---|---|
| Person | `rater_id` |
| Item | `item_id` |
| Problem text | `context` plus `response` |
| Human target | `Q_overall` |
| Provenance | Source revision, file hash, original row ID |

`response` is the chatbot response being assessed. The human decision is `Q_overall`, a three-class field in the official schema. Read and record the exact class names and integer mapping. Keep the uncertainty category as a decision, if present in the released mapping.

Exclude demographics, expert labels/reasons, other judgments of the query item, target explanations, confidence, and timing from the learner view. This first study infers behavior from decisions rather than profile attributes.

Audit original author-documented quality flags and exclusions. Freeze the selected policy before fitting; never remove a person because they disagree with the majority or are difficult to predict. Report counts before and after each exclusion, per-person history coverage, duplicates, missingness, and connected components of the assignment graph. Preserve authentic disagreement separately from identifiable data errors.

### 4.2 Contingency audit and replication

If access or schema prevents a valid DICES pilot, complete a structural audit of **MultiPref `default`** as the concrete next candidate [D2], together with the synthetic fixture and all feasible lab preparation. **MultiPref is audit-only in P0–P3:** its different observation model is not covered by the DICES categorical experiment below. Preserve individual `evaluator` histories, ordered preference strengths and ties; do not use the majority-aggregated `human_overall_binarized` release. Select an alternative for access/structure reasons, never because a completed score disappoints.

Before a later MultiPref experiment, freeze candidate-aware model equations, the ordinal or A/tie/B likelihood, symmetric tie handling, the support design, and the applicable baselines. Group by `prompt_id` and comparison identity, score actual candidate texts, and require the full probability vector to transform correctly when candidates swap. Personal offsets may model tie/decisiveness tendencies, not arbitrary left/right class preference. A vote over neighbors' arbitrary left/right labels is not an adequate kNN. Use candidate-aware retrieval as demonstrations or omit that comparator with an explanation. Preserve role/topic assignment information in the audit, outside predictive inputs.

**TID-8 CommitmentBank** is the preferred later semantic-inference replication [D3]. Its `answer_label` indices are not the ordered numerical judgment values. Exclude `weak_labels`; inspect constituent source terms and ID scope. Existing annotator splits still require explicit support/query separation.

Additional candidates and their limitations are in [LITERATURE_AND_DATASETS.md](LITERATURE_AND_DATASETS.md). Do not download or train all shortlisted datasets in P0–P3.

### 4.3 Small synthetic engineering control

Before human training, generate a small neutral rule-based fixture, approximately 32 simulated decision-makers and 64 semantic cases, with two textual realizations per case. Keep realizations together in every split. Include one regime with shared linear factors and another with conjunctions/exceptions that violate that simple assumption.

The learner receives only text, allowed support decisions, and query metadata. The evaluator retains hidden rule parameters, latent condition vectors, and query labels. In addition, use a deliberately ambiguous support set whose compatible functions disagree on a query. This checks that the evaluation does not require impossible exact recovery from insufficient observations.

These are engineering controls, not human observations. Do not tune the human experiment until a favored synthetic score appears. PersonalLLM [D7] is a possible later larger simulation; its mixture construction must remain explicit.

## 5. Schema and boundary between learner and evaluator

Maintain separate representations, even if an evaluator process has access to both:

- **Provenance:** source revision/hash, original keys, documented transformations, outcome mapping and data-quality decisions.
- **Learner record:** neutral problem text, candidate texts or declared label inventory, opaque person key for linking histories, and the permitted support observations.
- **Evaluator record:** query outcome, quality/audit fields, group membership, target annotations and explanations, and synthetic latent rules.

Identifiers, row order, file names, selection order, source locations, and target-derived summaries must not encode outcomes into the predictive input. Use opaque keys only for joins. Split membership itself is not a feature.

Keep missing observations distinct from an explicit uncertainty response. Do not create human labels by asking an LLM to fill missing cells. Any later synthetic augmentation is a separate condition, identified at row level and evaluated against actual held-out human observations.

## 6. Person and question partitions

Use one deterministic 60/20/20 person partition and an independent 60/20/20 item-group partition, seed **20261124**, with explicit namespace separation. Sort stable canonical IDs, hash `(seed, namespace, ID)`, and assign `floor(0.6N)`, `floor(0.2N)`, and the remaining IDs. Store the algorithm and actual IDs/hashes in manifests.

Groups must unite normalized exact duplicates and documented common conversation/prompt origins. Near-duplicate relationships require a recorded decision based on input information, not outcomes. If only item identity can be established, call the test **new items**, not unseen semantic topics or verified independent question families. Unresolved similarities remain a disclosed limitation.

Write the resulting sets as $S_{tr},S_{dev},S_{te}$ and $Q_{tr},Q_{dev},Q_{te}$.

1. **Shared training:** use only $S_{tr}\times Q_{tr}$ observations.
2. **Development adaptation:** for $s\in S_{dev}$, reveal histories from that person's $Q_{tr}$ observations. Query only $Q_{dev}$.
3. **Test adaptation:** for $s\in S_{te}$, reveal the prespecified histories from $Q_{tr}$. Query only $Q_{te}$ after protocol freeze.

Fit scalers, centering, PCA, metric transformations, and calibration using the allowed training/development partitions, according to their declared role. A genuinely frozen encoder may encode held-out text; it may not be adapted on held-out labels or used to fit transductive preprocessing without declaring a different experiment.

### Support budgets and repeated histories

Use $k\in\{0,4,16,64\}$; **$k=16$ is primary**. Use support-draw seeds **101, 211, 307** and nested prefixes. For the dense dataset, use the same support-question permutation for every person in each draw. Different methods receive exactly the same histories. Never select informative supports using the query labels.

Fix eligible cohorts using observation availability, not the values of answers. Use the same eligible test people across the main support curve. If 64 supports are unavailable, record the pre-model restriction and omit that secondary budget; **the primary k=16 endpoint cannot be dropped or relabeled**. If a valid k=16 cohort cannot be formed, report a structural limitation and complete the engineering outputs. A different primary endpoint requires a new, explicitly versioned protocol before fitting. Do not manufacture observations or silently compare changing cohorts. Report all exclusions and denominators.

Treat support draws as repeated measurements, not new people. Training-person ID models that saw full histories are not equal-budget competitors to new-person adaptation.

The other three known/new-person × known/new-question quadrants are later diagnostics. They must not expand this first assignment into four full studies. The primary test is joint new-person/new-item-group prediction.

## 7. First model comparison

Use one frozen encoder for all neural-feature comparisons. The compact default is `sentence-transformers/all-MiniLM-L6-v2` [E1]. At acquisition, resolve and record its immutable revision, tokenizer, pooling, normalization, runtime, and maximum length. Download only necessary inference files.

Serialize DICES input as explicit context and assessed-response fields. Cover the entire input using deterministic non-overlapping token windows that respect the model limit, including reserved special tokens. Encode windows with the checkpoint's pooling, combine by original-token-count-weighted mean, then normalize. Freeze this rule before outcomes; report window counts and token coverage. This aggregation is a proposed baseline, not a validated preservation of reasoning. Do not silently truncate the response or a decisive condition.

Let $z_q$ be the frozen vector and $\widetilde z_q$ its training-centered version. Compare:

| ID | Model | Main purpose |
|---|---|---|
| B0 | Smoothed population class frequencies | Non-text floor |
| B1 | Personal class frequencies shrunk toward population frequencies | General response tendency from history |
| B2 | Population multinomial logistic regression on $z_q$ | Text-only prediction |
| B3 | B2 logits plus a regularized personal class intercept fitted from the same history | Text plus general personal strictness/tendency |
| B4 | Similarity-weighted kNN over the person's history, shrunk toward B2 | Local use of prior decisions |
| M1 | B2 plus a personal intercept and a shared low-rank question-dependent interaction | Individual patterns conditional on problem content |

For categorical DICES outcomes, M1 logits are:

$$\ell_{s,c}(q)=\ell_{B2,c}(q)+b_{s,c}+u_s^T V_c\widetilde z_q.$$

Freeze B2 before fitting the shared interaction matrices $V_c$ on training people. Regularize both the basis and personal parameters. Learn training-person parameters only from the training block. At new-person adaptation, hold the encoder, B2 and $V_c$ fixed and fit only $b_s,u_s$ from the allowed support set. Use zero personal parameters at $k=0$.

This is **PAL/PReF-inspired**, not an asserted reproduction of either paper. The first head is deliberately small. Later variants may learn nonlinear basis functions, a metric, or a history encoder.

### Bounded development selection

Before running development fits, save the exact grid and loss normalization. Suggested fixed grid: B2 mean-loss L2 in `{0.01, 0.1, 1}`, B1 smoothing in `{1, 4, 16}`, B3 support-mean-loss L2 in `{0.1, 1, 10}`, B4 neighbor count in `{1, 4, 8}` with shrinkage in `{1, 4}`, M1 rank in `{2, 4, 8}` and common mean-loss L2 in `{0.1, 1, 10}`. Cap neighbor count by support size.

Use M1 fit seeds **11, 29, 47** and select configurations by mean probabilities across these seeds, then macro-person development NLL at $k=16$, averaged over support draws. Keep optimizer settings, convergence tolerance, and maximum steps fixed across the grid; record them before fitting. At test time, use the same three-seed probability ensemble, report it as such, and retain individual-seed diagnostics. Do not select a lucky seed.

Select the strongest B0–B4 comparator on development NLL at $k=16$. Keep B2 and B3 results visible even when another baseline wins. Maximum **40 shared-model fits**; record support-adaptation solves separately. This is a proposed scope cap, not a measured runtime forecast.

## 8. Outcomes, controls, and interpretation

Primary contrast on new test people and held-out item groups at $k=16$:

$$\Delta=\mathrm{NLL}(B_{selected})-\mathrm{NLL}(M1).$$

Use natural logarithms and give each test person equal weight, then each observed query equal weight within that person. Retain paired per-query log losses. Report accuracy and multiclass Brier score, support curves, per-person distributions, and fixed full-cohort and disagreement-subset summaries; disagreement-subset selection is evaluator-only and cannot drive training or primary selection.

Average the loss for repeated support draws for each person/query before uncertainty estimation. For a descriptive percentile 95% paired interval, perform **2,000** resamples of people and item groups independently. Preserve the macro-person estimand: normalize query/group weights within each sampled person first, then average their means using person multiplicities. For paired loss differences $d_{sq}$, person multiplicities $w_s$, and group multiplicities $v_g$:

$$\Delta^*=\frac{\sum_s w_s\left[\frac{\sum_{q:(s,q)\in\Omega}v_{g(q)}d_{sq}}{\sum_{q:(s,q)\in\Omega}v_{g(q)}}\right]}{\sum_s w_s}.$$

Preserve all within-group records and pair model predictions in every replicate. If any sampled person has no observed query intersection after group resampling, reject and redraw the entire replicate; count these rejections. Use seed **1701**, at most **20,000** attempts to obtain 2,000 valid replicates, and report a bootstrap limitation if that fails. Do not replace this with a single ratio over all observed cells, which changes person weights on sparse data. Do not count support draws or training seeds as independent human samples.

### Required controls

- Support/query, person, and item-group separation must hold mechanically.
- Learner payloads must exclude query outcomes and all target-derived fields.
- Consistent opaque person-ID renaming must leave predictions unchanged within numeric tolerance. Renaming is an invariance test, not a negative control.
- For B3, B4 and M1, use **10 fixed derangements** of histories across held-out people, preserving support sizes and question identities in the dense case. Do not alter query owners or labels. Report the true-history advantage; no or small advantage is an interpretable scientific result, not automatically a software bug.
- Compare M1 with B3 to separate question-dependent patterns from person-level label bias.
- Preserve all outcome categories, supported probabilities, and source class mappings.
- Keep two textual versions of a synthetic case in the same partition; test deliberate evaluator-field contamination is rejected by the input adapter.

A scalar score or neighbor distance does not prove reasoning equivalence. A positive M1 contrast, evidence that the correct history matters, and performance beyond B3 are different findings; report all three separately.

## 9. Freeze and final evaluation

Push a **PROTOCOL_FROZEN** commit containing code, exact model/checkpoint identities, source revisions, schema, quality policy, split/support manifests, selected configurations, seeds, metrics, resource counters, and the ordered list of final evaluations. Record that SHA in the coordination issue before scoring held-out query outcomes.

The test harness may access held-out labels only for the declared support adaptation and evaluator scoring. The development process must not inspect test-query metrics or error examples. Commit a plan for the shuffled-history controls before the test batch.

Score the declared models, support budgets, draws, seed diagnostics, and controls in one final batch. Do not refit the shared model on the development data in this pilot. Do not modify the candidate set or select models from test performance. If a correctness bug invalidates a run, preserve it, document the exposure and cause, and version the correction; a reused test is not fresh confirmation.

## 10. Resource scope and completion decisions

This assignment uses one human corpus, one compact frozen encoder, and the small synthetic fixture. Use existing local compute, default CPU. Proposed limits: 2 GiB of dataset/weight downloads, 6 CPU-core-hours of fitting/encoding, 8 GiB peak working memory, 40 shared fits, and 2,000 bootstrap draws. Record actual counters and adaptation-solve counts. Dependency-installation costs must also be reported. These values are budget choices, not measured requirements.

Do not create paid infrastructure, make paid inference calls, or fine-tune the encoder for this assignment. If a limit is approached, finish cheaper required checks and publish a concrete resource-limited report. A missing external download need not block the synthetic fixture, code, manifests, or reports. Do not silently substitute a different encoder and label that run the specified experiment.

The first scientific outcome is completed even if the model fails to improve. Use execution status and scientific conclusions separately:

| Execution outcome | Meaning |
|---|---|
| `VALID_PILOT_POSITIVE_PRIMARY` | The paired primary interval lies above zero; report history and bias controls separately |
| `VALID_PILOT_INCONCLUSIVE` | The primary interval satisfies lower <= 0 < upper |
| `VALID_PILOT_NONPOSITIVE_PRIMARY` | The paired interval lies at or below zero; this addresses M1 versus the selected baseline only |
| `INVALID_PILOT_REQUIRES_CORRECTION` | A data boundary, scoring, or implementation defect invalidated the result |
| `DATA_ACCESS_OR_STRUCTURE_BLOCKED` | Required access, IDs, or coverage are unavailable; deliver all feasible preparation |
| `RESOURCE_LIMITED` | A measured scope limit prevents completion; report exact completed and remaining work |

Also state whether any history-based method improved on B2, whether M1 improved on B3, and whether true histories improved on shuffled ones. M1 losing to kNN does not establish that personalization is impossible. No old ten-point accuracy gate or post hoc practical threshold applies.

## 11. Deliverables and later research

Keep general lab code under `labs/decision_functions/` and first-run outputs under `research/decision_functions_2026-11-24/runs/pilot_v1/`. Required artifacts and the GitHub reporting format are specified in [NEXT_AGENT_PROMPT.md](NEXT_AGENT_PROMPT.md) and [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).

Before P4, use the actual pilot to choose the concrete representation or adaptation question that remains unresolved. Freeze a second-domain protocol independently. Domain-specific candidate models must respect answer semantics and ordering, rather than recycling categorical label voting.

Before P5, create atomic Talmudic problem–condition–candidate–scholar–decision records with source provenance, explicit uncertainty, and parallel-family links. Keep original quotations and evidence separate from neutral predictive inputs. The four source indexes are research leads, not a ready-made decision matrix. Learn scholar profiles from their own supported observations; do not transfer a modern annotator's profile to a named scholar.

The contribution sought is evidence about which representations and adaptation mechanisms generalize from sparse individual histories. It is not the claim that adding an individual embedding is new. All factual literature/dataset statements refer to [the source register](LITERATURE_AND_DATASETS.md); proposed thresholds, grids, losses, and budgets are this plan's design choices.
