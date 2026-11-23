# Continuation research plan: metric representations and scholar attribution

**Project:** AI Talmudic Study  
**Prepared:** 23 November 2026  
**Status:** PLANNED — NO ANNOTATION STUDY OR MODEL EXPERIMENT HAS BEEN RUN  
**Source revision:** 56c6abee95248b0e872655f18e1ecc147dc5965b  
**Companion files:** [source snapshot](SOURCE_SNAPSHOT.json), [next-agent assignment](NEXT_AGENT_PROMPT.md)

## 1. Decision and research objective

Continue with a bounded study of **source-grounded attribution within verified disputes**. Begin with Rav–Shmuel in Bavli, and reserve Abaye–Rava for a later supervised replication of the method. Preserve the Yerushalmi material for a distinct domain-transfer study.

The motivating question is whether a representation of a case and its alternative positions supports useful distance operations, especially nearest-neighbor retrieval, and helps recover a scholar's documented position on an unseen source family.

The first measurable question is:

> Given an anonymized problem and two verified candidate positions, does a small learned distance improve recovery of the recorded Rav–Shmuel assignment over the same encoder and nearest-neighbor rule using a fixed distance?

A second, separate question is:

> Do the retrieved neighbors share a relevant סברה or חילוק, and is the proposed correspondence between their conclusions defensible?

These questions require separate evidence. Correct attribution alone does not establish conceptual analogy. A useful neighbor does not establish that a predicted attribution is correct.

The long-term target is a conditional model of positions, P(conclusion | case, scholar), with inspectable sources. The first study supplies the alternatives; generating candidate conclusions from an unrestricted new problem is a later task.

### Current work versus planned work

Completed for this plan: repository inspection at the pinned revision, mechanical inventory counts, a check for exact primary-reference overlap, protocol design, and preparation of these documents.

Not completed: a full-sugya annotation audit, a count of eligible independent disputes, model downloads, embeddings, training, evaluation, or verification of predictive performance. The source counts below must not be reported as a supervised dataset.

## 2. Starting evidence and why the plan has changed

At the pinned revision, the repository contains the following inventories [S1–S4]:

| Inventory | Source-location entries | Corpus branch | Status for this study |
|---|---:|---|---|
| Rav–Shmuel | 512 | 423 Bavli; 89 Yerushalmi | Discovery inventory; unique eligible cases unknown |
| Abaye–Rava | 498 | Bavli, across 36 tractates | Reserved replication inventory; unique eligible cases unknown |

The Rav–Shmuel index marks 504 entries as differences and eight as reconciled. The Abaye–Rava index includes alternative explanations and proofs as well as differences in conclusions. These are inherited first-pass classifications, not gold labels.

The two indexes share two exact primary source addresses: Berakhot 44b:22 and Sukkah 18b:3. This was checked mechanically. It is only a lower-level overlap signal; parallel passages and overlapping context require a broader audit. Adding 512 and 498 does not produce an independent sample size.

The current handoff also records:

- A known reference offset in an earlier normalized Bavli corpus. Use the current export-array mapping and preserve its provenance.
- Remaining identity and attribution risks, including Rav versus longer names, and Rava versus Rabbah.
- Anonymous alternatives that must not be assigned by name order.
- Continuations that qualify, reverse, reconcile, or reject earlier statements.
- A recall gap in the unselected Abaye–Rava candidates. Unselected does not mean negative.
- Rav–Shmuel scripts with import-time side effects and an exploratory intermediate artifact that prevents claiming a complete clean rebuild from scratch.

The next stage must consume the committed indexes without importing or executing the old builders. A complete catalogue-wide recall audit is valuable separate work; it is not a prerequisite for testing a carefully described sampled subset.

## 3. Scope and hypotheses

### 3.1 Primary scope

Include a case only when:

1. It concerns one identifiable question under specified conditions.
2. The source supports two distinct positions attributed to the named pair.
3. Attribution is unambiguous in the chosen source version after reading the needed continuation.
4. A neutral problem statement and two alternatives can be prepared without supplying the attribution.
5. The record belongs to an identified source family.
6. The model input preserves the decisive conditions.

Initially permit **outcome disputes** and **interpretive alternatives**, with separate type labels and type-specific reporting. Alternative proofs of the same outcome, sequential answers to different questions, unresolved attributions, reconciled differences, and unresolved version conflicts stay in a documented excluded or exploratory set.

The target is the attributed position established under that source version, not the eventual practical ruling of the sugya.

### 3.2 Prespecified hypotheses

- **H1 — attribution:** learned-metric kNN improves complete paired-attribution accuracy over fixed-metric kNN on the same held-out families.
- **H2 — useful analogy:** learned-metric neighbors improve independently reviewed relevance and correspondence between conclusions.
- **H3 — replication:** the frozen method produces a comparable attribution advantage when fitted on Abaye–Rava support examples and evaluated on their separate test families.

H1 is the primary pilot hypothesis. H2 and H3 must be reported separately; success in one cannot substitute for failure or uncertainty in another.

The inventories were selected to find disagreements. Results therefore concern attribution conditional on a verified disagreement. Estimating agreement rates or general tendencies requires independently collected agreements and individual positions.

### 3.3 Claims reserved for later

The initial study cannot establish an unrecorded position as a source attribution, a universal strictness axis, or a distance among all scholars' approaches.

In particular, two separate pairs supply two sets of contrasts. They do not identify a common four-scholar map. A later map needs shared questions or bridging observations, broader sampling, and explicit uncertainty for unobserved positions.

## 4. Data unit, grouping, and provenance

### 4.1 Three levels of identity

Maintain distinct identifiers:

- **Occurrence:** one source location and its surrounding evidence.
- **Atomic case:** one question with its conditions and candidate positions.
- **Source family:** all occurrences or derived cases connected strongly enough to expose the same held-out information.

Split a segment containing several disputes into atomic cases. Keep their common source provenance. Group parallels, repeated discussions, relevant continuations, alternative versions, and overlapping answer-bearing text. A shared topic alone is not sufficient to merge families.

Build this grouping across both scholar-pair inventories. Do not rely solely on exact text matching or the primary reference.

For the primary endpoint, select **one focal eligible case per family** using a deterministic rule fixed before predictions: canonical source ordering, then atomic-case ordering. Preserve additional cases for exploratory work. The first main model uses focal cases only, so source-rich families cannot dominate the reference bank.

### 4.2 Required annotation record

| Field | Required content |
|---|---|
| record_id, case_id, family_id | Stable derived identifiers, with links to original entry IDs |
| scholar_pair | Canonical identities, separately from displayed candidate order |
| source_version | Repository revision, index blob, source path/index, available edition/hash |
| source_refs and evidence_spans | Exact references and text supporting the question, positions, and attribution |
| context_status | Sufficient full discussion read, or specific missing continuation |
| question_he | Neutral Hebrew question and case description |
| conditions | Conditions required to interpret the alternatives |
| candidates | Two neutral position texts with stable IDs |
| attribution | Named assignment stored separately from model inputs |
| attribution_status | Direct, established in continuation, unresolved, or version-dependent |
| discussion_status | Maintained, qualified, reconciled, retracted, rejected, or unclear |
| decision_type | Outcome, interpretation, alternative proof, sequential answer, or other |
| reasoning_provenance | Explicit source, named commentary, annotator inference, or absent |
| review | Reader identities/roles, independent decisions, disagreements, adjudication |
| eligibility | Included/excluded/pending and a specific reason |
| grouping_evidence | Parallel, continuation, overlap, or duplicate relationship |
| input_provenance | Which source spans support the neutral input; author/checking status |

Use null or an explicit unknown state for missing evidence. Do not invent a label to complete a row.

A quotation match and a correct address are mechanical checks. Neither certifies that the case is a genuine dispute or that the attribution is settled.

### 4.3 Two data views

**Evidence view:** complete source context, names, commentary provenance, attribution, and audit notes.

**Prediction view:** neutral question, conditions, and the two alternatives. Exclude names, transmission chains revealing the answer, source addresses, order markers, and answer-derived explanations.

A summary writer may read the full source to establish the record. The resulting prediction view must undergo a separate leakage check. If a rationale cannot be constructed without importing the answer, keep it in the evidence view.

Record review_level as one of ai_single, ai_independent_double, human_reviewed, or human_independent_double. AI-prepared records with independent AI review may support a provisional benchmark build and engineering experiments, with that qualification carried into every result. They do not establish independent expert validation. For a claim of expert-validated source attribution, require two independent knowledgeable human readings and adjudication for every confirmation record. Lack of human review does not prevent useful preparation or clearly labeled provisional experiments.

## 5. Phases, outputs, and stopping points

### P0 — Freeze the inventory and prepare grouping

Read repository instructions and the current handoff. Record deviations from the pinned revision before combining new data.

Produce:

- Source manifest and content hashes.
- A read-only inventory of both indexes.
- Candidate family groups with evidence and uncertainty.
- A cross-inventory overlap ledger.
- A selection manifest for the annotation pilot.

Use the frozen JSON directly. Do not rerun or import old search/build modules merely to count records.

**Completion:** every selected occurrence has traceable provenance; uncertain grouping and unavailable context are explicit. No claim of a complete corpus audit.

### P1 — Audit 30 Rav–Shmuel source families

Attempt 30 distinct Bavli families, sampled across up to three manageable subject strata. Suggested initial strata are civil/property questions, Shabbat/festival questions, and prayer/blessing questions. Confirm availability before freezing the draw.

Use a fixed sampling seed, 20261123, and record the eligible inventory, ordering, sampling procedure, and substitutions. Sample independently of the attribution direction and model output. A failed candidate remains in the attempted-sample ledger.

Read each required continuation. Prepare neutral inputs and labels, separating outcome disputes from interpretive alternatives. Independently review all 30 attempted families where a second reader is available.

Record initial agreement before adjudication, including eligibility and named assignment among cases both readers consider eligible. Keep every disagreement and its resolution.

**Operational feasibility gate:**

- At least 20 of 30 attempted families yield usable focal cases.
- All usable cases have adequate context and resolved source attribution.
- Target at least 90% initial assignment agreement among jointly eligible cases; below this, revise the annotation procedure before scaling.
- No prediction input retains an unresolved attribution leak.
- The family grouping is sufficiently clear to plan a disjoint split.

These thresholds are project management criteria, not estimates of truth or statistical power. If expert review is unavailable, complete the preparation and mark the outcome provisional. Do not manufacture review sign-off.

P1 ends with an explicit decision: READY_FOR_BENCHMARK_BUILD, REVISE_ANNOTATION, or PROVISIONAL_PENDING_REVIEW, with quantified reasons.

### P2 — Build discovery and confirmation sets

Target **80 eligible Rav–Shmuel development families**, including usable P1 families, plus **60 additional confirmation families**.

A total of 140 eligible families is a target, not a claim about the yield of the present index. If fewer are available, preserve eligibility. A smaller 60-development/40-confirmation study may proceed only as a documented feasibility version fixed before scoring; it has less precision. Below that, prioritize source and retrieval work rather than a confirmatory superiority claim.

Freeze family membership before modeling. Confirmation families must be distinct from all development evidence, parallels, and reformulations. Annotation adjudication may use labels, but the modeling workflow must not inspect confirmation labels or use confirmation source context.

This separation is procedural, not a claim that files in the private repository are technically inaccessible. Training and retrieval programs must read only the permitted inputs and reference bank.

All confirmation examples require independent review and adjudication before predictions are examined. Leave genuinely unresolved records unscored with reasons.

### P3 — Run bounded development experiments

Use the fixed input rules and model table in sections 6–7. Fit preprocessing inside each development training fold.

Use five development folds grouped by source family and approximately balanced by subject and decision type where feasible. Every case contributes one out-of-fold prediction per configuration. The same folds apply to all methods.

Model selection uses only these development folds. The resulting model rankings are exploratory; the separate confirmation set supplies the held-out comparison. There is no claim that the best development score is an unbiased estimate after selection.

Run the mandatory controls before freezing confirmation.

### P4 — Freeze and score confirmation once

Before scoring, commit:

- Final annotation and exclusion manifests.
- Source-family partitions.
- Exact input templates and candidate permutation rule.
- Encoder revision and runtime versions.
- Selected model hyperparameters and saved fitted state.
- All prespecified metrics, comparisons, uncertainty procedures, and gates.
- Confirmation input hashes and the prediction-generation command.
- A record of all development changes.

Generate predictions without source lookup or confirmation labels. Save them before evaluation. Score the paired methods on exactly the same cases.

A genuine source correction discovered later must be logged, applied consistently, and accompanied by results before and after correction. Do not remove inconvenient cases based on model errors.

### P5 — Replicate on Abaye–Rava

After the method is frozen, prepare **80 support families and 60 confirmation families** for Abaye–Rava, subject to the same feasibility rules.

Fit their own metric parameters and reference bank from their support set. Reuse the selected encoder, templates, feature dimensions, hyperparameters, optimizer recipe, and evaluation procedure. Do not retune the primary replication to its test outcomes.

The Abaye–Rava test must be disjoint from its support and all Rav–Shmuel material used for development or confirmation. Audit cross-pair parallels and shared context; the two already observed address overlaps are only starting checks.

This is supervised replication with new scholar-specific evidence. It is not zero-shot attribution from an unfamiliar scholar ID.

If the samples overlap in permitted support material, report global unique-family counts separately rather than adding pair-specific sample counts.

### P6 — Expand only after the bounded study

Possible extensions, selected according to observed errors:

- Yerushalmi transfer, with a separately audited source/interpretation protocol.
- Additional scholars and shared cases that connect the pair-specific comparisons.
- Independently sampled agreements and individual statements.
- More than two candidate positions.
- Reviewed concept features.
- Domain adaptation when errors concentrate in the original language.
- Predictions for unresolved passages, explicitly labeled as research hypotheses.
- Candidate generation for new problems, evaluated as a separate task.

Each extension gets a new frozen protocol. Larger models are not the default response to weak data or leakage.

## 6. Fixed inputs and encoder

Use concise, source-checked Hebrew as the primary prediction view. Preserve an attribution-masked original Hebrew/Aramaic view as a predeclared diagnostic where the same information can be retained. Do not search over many paraphrases to obtain a favorable result.

The initial encoder is **intfloat/multilingual-e5-base**, revision **d128750597153bb5987e10b1c3493a34e5a4502a**. The official card documents 768-dimensional vectors and requires prefixes; use the literal English prefix **query: ** for both sides of these symmetric comparisons [T1].

Use the documented masked mean pooling and normalization. The sentence-model input limit is 512 tokenizer tokens, including the template. Count tokens and preserve all decisive conditions; do not silently truncate a sugya. If checked compression cannot retain them, mark that view unusable [T1].

The encoder is a fixed practical starting point, not a claim of validated Aramaic reasoning. Run frozen, in evaluation mode, with CPU float32 as the initial execution setting. Record actual installed versions and measured resource use.

Use one problem template and one candidate template:

~~~
query: שאלה: {neutral_question}
תנאים: {conditions}
~~~

~~~
query: שאלה: {neutral_question}
תנאים: {conditions}
עמדה מוצעת: {candidate_text}
~~~

Both candidates use the same template without A/B labels. Store presentation order separately; choose it deterministically from a fixed seed and stable case/candidate IDs, independently of the label.

Cache by input hash, preprocessing version, model/tokenizer revision, prefix, pooling, normalization, runtime, and dtype. Fit no corpus-level statistics on confirmation inputs.

## 7. Models and the controlled distance-learning experiment

### 7.1 Representations and paired target

For a focal case i, let q_i be the problem, a_i and b_i the displayed alternatives, and y_i=+1 when the first canonical scholar selects a_i and the second selects b_i. Use y_i=-1 for the reversed assignment.

Canonical first scholars are Rav for the primary study and Abaye for replication. These are label conventions, not learned universal coordinates.

Let h_i be the normalized problem embedding. Let normalized candidate embeddings be e(q_i,a_i) and e(q_i,b_i). Define:

$$
\Delta_i=e(q_i,a_i)-e(q_i,b_i), \qquad
z_i=\Delta_i/\|\Delta_i\|_2.
$$

Use an epsilon of 10^-8. A smaller norm is a representation failure: assign a neutral score, flag it, and retain it in the primary accuracy denominator. Do not silently discard difficult evaluation cases. Exclude failed training representations from semantic fitting, SVD, and both semantic reference banks, recording IDs and counts. Fixed and learned kNN must use the identical valid bank. If fewer than six valid training families remain in any required training split, halt that semantic comparison and report it as unavailable instead of changing k.

Do not center differences. Swapping the alternatives gives (h_i,z_i,y_i) -> (h_i,-z_i,-y_i).

### 7.2 Oriented nearest neighbors

For each training family j, compare both orientations:

$$
D_{j,\sigma}^{2}
=\tfrac12\|h-h_j\|_2^2
+\tfrac12(z-\sigma z_j)^\top M(z-\sigma z_j),
\quad \sigma\in\{-1,+1\}.
$$

Take d_j^2=min_sigma D_{j,sigma}^2, and select the five nearest distinct training families. Resolve equal neighbor distances by stable family ID.

Restore the orientation using sigma_j=sign(z^T M z_j). An orientation tie within 10^-12 gives sigma_j=0 and neutral evidence. Each family casts one vote v_j=sigma_j y_j, weighted by w_j=exp(-d_j^2/0.5).

$$
m=\frac{\sum_j w_jv_j}{\sum_j w_j}, \qquad p=(1+m)/2.
$$

Calculate weights stably. The raw p is a vote-based assignment score, not an established calibrated probability.

Two orientations are alternative representations of one training example. They do not create extra observations, extra votes, or a larger sample count.

A candidate exchange leaves neighbor identities and distances unchanged and reverses votes. Thus p(q,b,a)=1-p(q,a,b). Check this numerically to tolerance 10^-6.

For primary forced-choice accuracy, a score exactly 0.5 uses a stable, label-independent candidate-ID tie-break. Keep a separate unresolved flag. The same substantive candidate must win an exact tie when display order changes. Report tie counts and selective coverage separately.

### 7.3 Fixed and learned metrics

The fixed reference uses M=I.

The proposed model learns only eight bounded metric weights:

$$
M_\theta=I+P^\top\operatorname{diag}(\theta)P,
\qquad 0\le\theta_\ell\le1.
$$

P has orthonormal rows: the first r=min(8, training-rank) uncentered SVD directions of training z vectors. It is fitted inside each training fold. Original dimensions outside those directions remain in the identity term.

The eigenvalues of M stay between 1 and 2. Consequently the update cannot collapse distinct vectors or arbitrarily stretch the representation. At theta=0 it exactly equals the fixed metric. Normalize only before applying the metric, never after.

This is a proposed small-data model. Its learned directions are attribution-predictive directions; they are not automatically named Talmudic concepts.

### 7.4 Training objective

Use one loss per training family. For query family i, exclude itself and every linked occurrence. For all other training families j and orientations sigma, define:

$$
K_{ij,\sigma}=\exp(-D_{ij,\sigma}^{2}/0.5).
$$

$$
p_i(y_i)=
\frac{\sum_{j,\sigma}K_{ij,\sigma}\mathbf{1}[\sigma y_j=y_i]}
{\sum_{j,\sigma}K_{ij,\sigma}}.
$$

Minimize mean negative log p_i plus lambda times mean(theta^2), using stable log-sum-exp calculations.

Fix projected gradient descent: theta starts at zero; learning rate 0.1; 200 full-batch steps; clip weights to [0,1] after each step. Use float64 for these small optimization calculations. Select lambda from {0.01,0.1} using development folds only. Record training loss, final weights, and bound saturation. Numerical failure triggers an implementation investigation, not a silent new optimizer search.

The smooth all-neighbor objective is a training surrogate. The scientific endpoint is performance of the predeclared hard five-family rule on held-out data.

### 7.5 Model table and search budget

| Model | Definition | Development configurations |
|---|---|---:|
| Chance/order diagnostics | Uniform chance and fixed presentation choice | No trained model |
| Metadata diagnostic | Signed candidate-length contrast interacted with source/topic indicators; diagnostic only | One fixed regularized model |
| Lexical preference | Character TF-IDF 3–5 grams, candidate difference, L2 logistic model without intercept | C in {0.1,1,10} |
| Frozen semantic preference | Same z as above, L2 logistic model without intercept | C in {0.1,1,10} |
| Fixed semantic kNN | Same h, z, k=5, weights, M=I | Fixed |
| Learned semantic kNN | Same inference rule with M_theta | Two lambda values |

TF-IDF vocabulary and IDF are learned on each training fold. Fit linear comparators with both sign orientations, each weighted one-half, without treating them as independent cases. Use no intercept so predictions preserve candidate-swap symmetry. The metadata diagnostic uses the contrast (len(a)-len(b))/(1+len(a)+len(b)), multiplied by an all-ones indicator and training-only tractate/topic one-hot indicators, with unseen categories encoded as all-zero, no intercept, and fixed C=1. All its features therefore reverse under candidate exchange. Pure source/topic features are not included as additive terms.

Select hyperparameters by development assignment accuracy, breaking ties by lower Brier score and then stronger regularization. Keep exact tie-break conventions fixed.

Eight trained configurations across five folds require 40 main development fits, followed by three final refits. Allow up to 50 shuffled-label control fits and five metadata-diagnostic fits: at most 98 shallow fits for this stage. Frozen encoding is cached once per input view. Additional searches require a documented new exploratory version.

The primary estimand is:

$$
\Delta_{\rm metric}
=\operatorname{Accuracy}(\text{learned kNN})
-\operatorname{Accuracy}(\text{fixed kNN}).
$$

The encoder, data, candidate order, reference-bank size, and kNN rule remain identical. Comparisons with lexical and linear methods assess practical usefulness but cannot replace this controlled metric comparison.

## 8. Evaluation and statistical interpretation

### 8.1 Primary endpoint

Use complete paired assignment on one focal case per independent confirmation family. Two correct scholar labels in one case count as one correct assignment.

Report:

- Accuracy, correct/total, and an interval for each method.
- Paired accuracy difference and a 95% interval.
- The number correct only for the proposed model and only for the fixed baseline.
- Performance by subject and decision type, with denominators.
- Ties, representation failures, and exclusions.
- Exact test sample and prediction hashes.

Use 95% Wilson intervals for individual accuracies. For the paired difference, use a conservative finite-sample interval for the decision gates. Let b count learned-only wins and c count fixed-only wins among n independent families, so the estimated difference is (b-c)/n. Construct two-sided 97.5% Clopper–Pearson binomial intervals [Lb,Ub] for b/n and [Lc,Uc] for c/n. Report [Lb-Uc, Ub-Lc] as a conservative 95% interval for the population difference. Bonferroni coverage of the two marginal events justifies this construction without assuming that the directional discordance counts are independent. Record that it is conservative, especially with small n.

Also report a descriptive sensitivity interval using the 2.5th and 97.5th percentiles of 10,000 paired bootstrap resamples of whole families, seed 20261123. Do not use that bootstrap interval to trigger a go/stop decision: with rare discordances it can be too narrow.

Report an exact two-sided McNemar comparison: condition on b+c and use a Binomial(b+c, 0.5) null. If there are no discordant outcomes, set p=1. These procedures and intervals are fixed before confirmation; do not choose the most favorable method afterward.

The primary comparison is learned versus fixed kNN at alpha=0.05. Other model comparisons are descriptive unless a separate multiplicity-controlled confirmatory specification is frozen in advance.

Family grouping is an explicit attempt to control dependence, not proof that all subject-level dependence vanishes. Folds, paraphrases, repeated occurrences, and orientations do not increase the effective n.

A 60-family confirmation set is intended to detect a substantial effect. It does not guarantee power for a modest effect. There is no promised accuracy target.

### 8.2 Confidence and selective output

Report the Brier score of the vote score as a diagnostic of its quality. Do not label raw cosine similarity or vote strength a calibrated confidence level.

Use confidence statistic c=|2p-1|. Representation failures and exact neutral scores always abstain in the selective analysis. On development out-of-fold predictions only, choose the highest cutoff that retains at least 80% of all development families, including every score tied at the boundary. If 80% is unattainable after mandatory abstentions, retain every otherwise eligible case and report the achieved coverage. Freeze the numerical cutoff and boundary rule. Report actual confirmation coverage and error without adjusting the cutoff to force a target coverage. These small samples do not support a guaranteed error-rate claim.

### 8.3 Pretraining exposure

A pretrained encoder may already have encountered source passages. Name masking, paraphrasing, and family splitting reduce specific shortcuts but do not establish absence from pretraining.

Describe the result as held-out attribution under the stated protocol. Do not claim independent recovery of unknown positions or uncontaminated historical prediction.

## 9. Independent test of useful neighbors

Use a separate fully judged retrieval challenge to address H2.

Before seeing confirmation outputs, select 30 query families from the confirmation set, stratified by the frozen types where possible. For each, define a pool of ten development families, including candidate analogues and difficult same-topic alternatives. No candidate may be a parallel or answer-bearing continuation of the query.

The query and candidates contain neutral case descriptions and alternatives, so this evaluates decision-structure retrieval. Pure question-only retrieval is a separately labeled capability; the proposed contrast representation requires the alternatives.

Judge all ten candidates for each query, rather than assuming unjudged passages are irrelevant. Use grades:

- 0: no useful connection.
- 1: same topic or vocabulary only.
- 2: a relevant issue with a material limitation.
- 3: a useful operative distinction and a defensible correspondence of positions.

Record the proposed correspondence and decisive differences. Hide model identity, distance score, and attribution correctness from reviewers. Two readers adjudicate disagreements where possible.

Report nDCG@5 within this pool, precision@3 for grades 2–3, and the number of queries with no positively judged candidate. If using Recall@k, label it explicitly as recall within the fully judged pool. It is not exhaustive corpus recall.

Rank the same pools with fixed and learned distances. Correct attribution without better independently reviewed neighbors supports only H1. A positive H2 result is needed for a claim about useful conceptual geometry.

Additional full-bank neighbor examples may illustrate errors and uses, but they do not replace the controlled judged-pool comparison.

## 10. Mandatory controls

| Control | Purpose and interpretation |
|---|---|
| Candidate exchange | Predicted correspondence must exchange; numerical tolerance 10^-6 |
| Within-family assignment randomization | Independently shuffle each training family's assignment; preserve all its linked occurrences |
| Metadata/length diagnostic | Identify source, topic, ordering, or formatting shortcuts |
| Family and parallel audit | Prevent a test assignment from appearing in training under another location |
| Retrieval access audit | Confirmation sources, labels, and answer-bearing continuations cannot enter the reference bank |
| Neutral-summary/source-view comparison | Test dependence on normalization; never silently change information content |
| Fixed paraphrase subset | One independently checked paraphrase for a prespecified 20 development families; no iterative prompt search |
| Same-topic hard negatives | Test whether neighbors distinguish the operative condition |

For randomization controls, use ten fixed shuffles and the five development folds for the selected metric configuration: 50 fits. Sample assignment flips independently for families in each training partition. Keep evaluation labels true. Chance-like performance is judged with finite-sample variability; an unexpectedly high mean requires investigating leakage. Source-view and paraphrase diagnostics reuse the selected models for inference on fixed alternative views of development validation inputs; they add no tuning or refitting and are not claims about a separately optimized source-view model.

A global exchange of the two scholar names only renames the labels and is not a negative control.

Do not use a nominal "scholar identity removed" ablation in the first pair-only classifier: pair identity is constant there. Such an ablation becomes meaningful only in a broader model that actually receives varying scholar identities.

Do not treat a counterfactual invented case as an observed position of a named scholar. Counterfactuals can test input sensitivity, with an explicitly different kind of ground truth.

## 11. Go, hold, revise, and stop rules

Freeze these operational rules before confirmation. Check data validity first. For H1's statistical decision, apply GO first; if GO is unmet, apply STOP only when the conservative interval's upper endpoint is below the practical threshold; otherwise HOLD. The other rows describe separate data, interpretation, and replication outcomes.

| Outcome | Decision |
|---|---|
| Attribution or context cannot be established for enough cases | DATA_LIMITED: improve source preparation; no model claim |
| Annotation disagreement or leakage persists | REVISE_DATA: correct the process before scaling |
| Learned metric gain >=10 percentage points, conservative paired 95% interval above zero, exact paired p<=0.05, controls pass | GO_TO_REPLICATION for H1 |
| GO is unmet and the conservative upper limit still permits a 10-point gain | HOLD: report inconclusive; add genuinely independent evidence under a new version |
| Metric improves over fixed kNN but falls behind a simple linear model | Record metric evidence and practical limitation; no best-model claim |
| Neighbors match topic but fail the operative distinction | REVISE_REPRESENTATION for H2 |
| Replication supports the prespecified advantage with its own uncertainty | Support method transfer across the two studied pairs |
| Replication differs substantially | Report both results; investigate domain/support differences without retuning the completed tests |
| GO is unmet, the conservative upper confidence limit is below a 10-point gain, and controls are valid | STOP_THIS_METRIC_VERSION; this does not reject every possible representation |
| Gains depend on leakage, repeated passages, or order | Reject the affected result; repair before further modeling |

Ten percentage points is a deliberately substantial pilot investment threshold. Smaller improvements can be useful but do not automatically justify a larger training program.

If development reveals a near-ceiling baseline, amend the challenge before confirmation is opened. Do not reduce the required gain after viewing confirmation results.

Do not repeatedly extend the same test until significance appears. A later study receives new independent families and a new frozen protocol. Preserve all completed results.

## 12. Resources, roles, and deliverables

### Resources

The first assigned task is P0–P1 only. It needs source reading and modest scripts, not model weights or a GPU.

Later phases use one local frozen encoder, exact nearest-neighbor search, and the bounded shallow-fit budget above. Do not start a new cloud instance or incur paid API charges as part of this plan. If existing local CPU resources are insufficient, first measure and report the concrete limitation.

Record actual memory, elapsed time, embedding throughput, and fit counts when executed. No wall-time or GPU-hour claim has been measured. Specialist reading and annotation are expected to be the principal uncertain workload.

### Roles

- **Source/annotation owner:** case boundaries, full context, identities, source evidence.
- **Independent reviewer:** attribution and input checks, without model predictions.
- **Modeling owner:** controlled inputs, train-only preprocessing, deterministic experiments.
- **Evaluation owner:** frozen predictions, scoring, family-level uncertainty, and final claim limits.

Agents can parallelize inventories, script work, and independent review preparation. Never claim human review when only agents participated. Models and annotators should not share confirmation outcomes during development.

### Planned execution outputs

These are future outputs, not files claimed to exist now:

- inventory and source manifest;
- occurrence-to-case-to-family map and overlap ledger;
- pilot selection, attempted-sample and eligibility ledgers;
- audited evidence records and neutral prediction inputs;
- annotation disagreement report;
- source-family partitions and frozen protocol;
- embedding cache manifest;
- development results and negative controls;
- saved confirmation predictions and paired results;
- fully judged retrieval pools and grades;
- a source-linked error analysis;
- final decision and next-stage handoff.

Persist derived work in this private repository, with large reproducible caches kept out of Git. Preserve the original source corpora and their references.

### Immediate next assignment

Execute P0 and P1 using [NEXT_AGENT_PROMPT.md](NEXT_AGENT_PROMPT.md). End with a concrete source/annotation feasibility report. The scoped stopping point is intentional: this prompt does not assign model downloads, training, confirmation scoring, or the replication phase.

## 13. What a useful eventual output should show

For one user-supplied case with candidate positions, display:

1. The problem and conditions the system understood.
2. The predicted assignment or an explicit unresolved result.
3. The comparable recorded cases actually used.
4. The proposed correspondence between positions.
5. Material differences and conflicting examples.
6. Separate labels for source attribution, model prediction, and explanatory hypothesis.

Proximity does not establish entailment. A supporting, qualifying, or refuting relationship should be represented explicitly when available; a symmetric distance alone cannot encode the direction of those relationships.

The final research claim should match the evidence. A successful initial study would support improved source-grounded attribution using a constrained learned distance on the studied families. A broader claim about a geometry of סברות requires the separate analogy evidence and successful transfer.

## 14. References and source boundaries

### Repository evidence, pinned to the source snapshot

- **S1:** [Repository README](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/README.md).
- **S2:** [Agent instructions](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/AGENTS.md) and [handoff](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/AGENT_HANDOFF.md).
- **S3:** [Rav–Shmuel index](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/rav_shmuel_results/rav_shmuel_index.json).
- **S4:** [Abaye–Rava index](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/abaye_rava_results/abaye_rava_index.json) and [procedure](https://github.com/shulm/AI-Talmudic-Study/blob/56c6abee95248b0e872655f18e1ecc147dc5965b/abaye_rava_results/README.md).
- Exact blob identifiers, byte sizes, and mechanical observations are in [SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json).

### Technical foundations

- **T1:** [Official multilingual-e5-base model card](https://huggingface.co/intfloat/multilingual-e5-base), [pinned repository revision](https://huggingface.co/intfloat/multilingual-e5-base/commit/d128750597153bb5987e10b1c3493a34e5a4502a), and [sentence configuration](https://huggingface.co/intfloat/multilingual-e5-base/blob/main/sentence_bert_config.json). Supports encoder conventions, not validation on this research task.
- **T2:** Weinberger and Saul, [Distance Metric Learning for Large Margin Nearest Neighbor Classification](https://jmlr.org/papers/v10/weinberger09a.html), 2009. Technical foundation for learning distances; the bounded eight-weight model above is this plan's proposal.
- **T3:** Reimers and Gurevych, [Sentence-BERT](https://aclanthology.org/D19-1410/), 2019. Sentence representations for similarity operations.
- **T4:** Shmidman et al., [Introducing BEREL](https://arxiv.org/abs/2208.01875), 2022. Rabbinic-language representation research; its homograph results do not establish a ready-made sentence-analogy metric.
- **T5:** [Sefaria Rabbinic Hebrew/Aramaic–English pairs](https://huggingface.co/datasets/Sefaria/Rabbinic-Hebrew-English-Pairs/blob/main/README.md). Translation-retrieval benchmark, not a scholar-attribution benchmark.
- **T6:** Koh et al., [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a.html), 2020. A basis for later reviewed concept representations.
- **T7:** [Technion dispute-extraction project](https://sipl.ece.technion.ac.il/projects/project-details/?prj_id=11461). Related work on structured opinions and attribution chains in Tur and Beit Yosef; a different evaluation task.
- **T8:** Park et al., [Preference Completion](https://arxiv.org/abs/1507.04457), 2015. A possible foundation for later multi-scholar conditional scoring.

This document is a research protocol proposal. Its thresholds, sampling targets, bounded metric, and execution budget are design choices, not published findings about Talmudic reasoning.
