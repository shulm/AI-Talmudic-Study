# Next protocol proposal — synthetic penalty separation, human confirmation blocked

Status: **PROPOSED_NOT_EXECUTED**. This document does not authorize or claim a second human evaluation. It responds to the observed null failure in diagnostics v1, while preserving its strong positive-control recovery and the DICES zero-interaction certificates.

## One immediate bounded continuation

Test whether separate personal-offset and interaction penalties preserve recovery while controlling spurious interaction under the null. Do not enlarge the encoder, feature set or rank. There is no evidence here that a more complex representation is needed before resolving this regularization tradeoff.

Use the same rank-two, three-class, 96-person/192-case rotational generator family, dimensions, balanced 96-case support design, oracle scores and informative/uninformative conditions. Fix a new synthetic generator seed `20261126` and categorical seed `2719` before fitting; retain v1's failed fixture as an exposed diagnostic, not a fresh test. People 48/24/24 and groups 40/12/12 remain disjoint. Wording variants stay within groups and are never independent observations. The middle split becomes development for this new version only.

Objective:

`mean CE + lambda_V/2 * ||V||F² + lambda_U/(2S) * ||U||F² + lambda_b/(2S) * ||b||F²`.

Fix `lambda_b=0.1`; use exactly four candidates `(lambda_V, lambda_U) = (0.001,0.01), (0.001,0.1), (0.01,0.01), (0.01,0.1)`. Apply the same lambda_b and lambda_U to new-person adaptation. Rank=2; seeds 11/29/47 form a probability ensemble. Known shared logits remain fixed; no learned feature transform. Use float64 and the v1 diagnostic optimizer settings. Compare B3 with lambda_b=0.1, B1 personal frequencies shrunk with four pseudo-observations toward training frequencies, and B2 known shared logits. Every method receives identical information and support observations.

Budget: 24 shared M1 fits (two regimes × four candidates × three seeds); at most 4,096 personal adaptations including selection, final synthetic evaluation and batch checks; one CPU-core-hour, 4 GiB, no paid calls or model/data downloads. Commit exact stage IDs and solve counts before starting; retries consume the caps.

Selection uses development only: admit candidates whose null expected-NLL degradation versus B3 is at most 0.01; among admitted candidates choose the largest positive-control expected-NLL gain. If none is admitted, stop with a failure. Treat expected-NLL differences within `1e-5` as numerical ties, choosing the larger interaction penalty product, then larger lambda_U, then declared order. B3 wins a numerical tie with M1.

Before scoring the new synthetic holdout, validate `1e-6` probability and `1e-5` NLL numerical-equivalence tolerances using fixed-person batch-size checks and repeated deterministic objective calculations on training/development fixtures. V1's maximum batch probability change was 1.672e-7; the new NLL tolerance still requires its own validation. If checks exceed the declared tolerances, stop as numerically unresolved rather than enlarging tolerances after scoring.

Freeze selection, then evaluate the new synthetic holdout once. Retain all v1 recovery gates: positive expected-NLL gain >=0.05; >=50% oracle-gap recovery; personal-contrast normalized RMSE <=0.5; null degradation <=0.01; batch difference <=1e-6. The 0.05 effect is a deliberately substantial engineering requirement, not a human practical-effect estimate. Report realized NLL, accuracy, Brier, oracle metrics, seed variation and uninformative-history failure. Report numerical audit completeness separately from predictive gates. No favorable outcome is required.

## Conditional human protocol requirements — not ready to freeze

Human confirmation remains blocked by the null-control failure and dataset admission. The concrete first candidate is **TID-8 CommitmentBank**, revision `e12b715be7582af64efc596f8402d916fb64f1e3`. The [official pinned card](https://huggingface.co/datasets/MichiganNLP/TID-8/blob/e12b715be7582af64efc596f8402d916fb64f1e3/README.md) still lists an unknown license. Its class indices 0–6 map to judgment values 0,1,2,3,-3,-1,-2. Do not interpret index distance as ordinal judgment distance or consume weak_labels as features.

The [original CommitmentBank repository](https://github.com/mcdm/CommitmentBank/tree/14ea91f56e3575b011d28fca5c37a1f5e92769b7) describes participant-level seven-point judgments, but the inspected README does not establish reuse terms; its GitHub license endpoint returned 404. This is an unresolved permission/terms record, not proof that reuse is prohibited. Before acquisition, obtain applicable constituent/distribution terms or documented owner permission. Metadata/documents only were accessed here; no candidate dataset was downloaded.

After the synthetic gate and terms are resolved, a separate admission stage must establish annotator-ID scope, genuine histories, candidate input fields, item-family relationships, and overlap with both exposed tracks. Use one canonical TID-8 constituent view, not duplicate ann/atr records. Proposed human target: seven-class probabilistic judgments, primary 16 supports, secondary 0/4/64 where a fixed eligible cohort is feasible. Preserve all categories, distinguish missing observations, never fill absent human decisions, and stop rather than change the primary endpoint when coverage fails.

The future question is whether the *method* generalizes from safety judgments to semantic commitment judgments, not whether a modern annotator's personal vector transfers to another person or to Talmudic scholars. Train domain-specific shared parameters on that corpus's training block; no transfer claim about the learned DICES profiles.

Proposed independent 60/20/20 person and item-family partitions use SHA-256 ordering with seed `20261126` and distinct namespaces. Group exact normalized duplicates, common source discourse origins and documented variants without labels. Query outcomes stay evaluator-only. Supports come only from each person's training-group observations, with nested budgets and seeds 101/211/307; hold the eligible cohort fixed. Record unresolved near-duplicates and admit at least 20 test people and 30 test groups for this proposal; otherwise return a structural limitation before modeling. Actual denominators, membership hashes and all exclusions must be frozen before any development fitting.

Keep B1/B2/B3 controls and the selected independently penalized interaction, with identical supports. A future protocol must resolve the seven-class head, training-only feature scaling, encoder revision/windowing, and exact model candidates before fitting; these remain blocked specifications until admission and synthetic results exist. Do not silently recycle the current three-class implementation as a seven-class model. No encoder is selected or downloaded under this proposal checkpoint.

Primary human estimand: macro-person NLL(B3) minus NLL(M1) at 16 supports. Retain B1/B2 comparisons, multiclass Brier, accuracy, support curves and 10 fixed deranged-history controls. Average support-draw losses per person/query before 2,000 paired independent person/family bootstrap replicates (seed 1701, within-person normalization, reject empty intersections). Declare a scientifically worthwhile NLL improvement of 0.01 separately from numerical equivalence; report the interval relative to both zero and 0.01. Add paired uncertainty for true-versus-shuffled loss contrasts rather than upgrading point differences into significance claims. All exact final comparisons and sparse-history derangement eligibility must be frozen after the coverage audit and before scoring.

## Exposure and stop conditions

DICES pilot v1 is exposed in full. PR #5's SRO Complete_02-16-2019 Kirby→Holt–Laury evaluation is exposed; a new random split of either does not provide fresh confirmation. Its Cross-Psych-101 candidate was rejected for participant-count, provenance and terms issues. Its 30 provisional scholarly families/24 usable focal cases remain a separate unvalidated source-preparation track; do not rebuild or treat them as a ready human comparison cohort.

The only immediate proposal is the small synthetic penalty-separation diagnostic above. The human sections are admission requirements and a conditional design, not a resolved preregistration. If a prerequisite remains unresolved, publish the blocker and stop. No alternative corpus substitution, source expansion, human fitting or scoring follows automatically.
