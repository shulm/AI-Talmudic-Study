# Results — individual decision pilot

**Qualified outcome: inconclusive.** Eight own-person source choices improved prediction relative to the declared population and simple-summary baselines, but did not improve on the matched other-person history control. The two co-primary criteria were not jointly satisfied. This experiment does not demonstrate individual-specific cross-task transfer or practical benefit.

The independently reviewed protocol and artifacts were frozen in commit `430c0ec4e74db8c265e77e1eb028b21abe6bff43` before final predictions. All declared predictions were saved before the final label join. **One final human evaluation; zero invalidated or repeated human test runs.** Earlier engineering corrections are in RUN_LOG.md.

## Data and independent counts

Admitted SRO `Complete_02-16-2019`, revision `4e6e837fb5aaca87ed5914fd9be251156f43eec9`, Kirby → Holt–Laury. Of 522 linked people, 14 incomplete target schedules were excluded before model comparisons. Split: 304 training, 102 validation, **102 held-out people**. Test: 1,020 target choices in **one target schedule family**. Each test person supplied the same eight source probes; curves use nested 0/2/4/8 budgets with the same people and targets. Three fit seeds and five donor assignments are repeated computations, not additional independent people.

Cross-Psych-101 was rejected before training: its actual 601-person release conflicts with the paper’s 591-person public cohort after opt-outs; licensing and canonical decision provenance also remain unresolved. See DATA_ADMISSION.md.

## Co-primary results at eight source choices

Positive differences favor own history. Units are natural-log loss per complete alternative, averaged within person and then equally across people. Intervals are two-sided 95% paired participant-cluster percentile bootstrap, 2,000 draws, conditional on fitted models, fixed development donor pool and these task families. The prespecified signal threshold is zero, not an application utility threshold.

| Comparison | Mean loss reduction | 95% interval |
|---|---:|---:|
| Population minus own profile (co-primary) | 0.111276 | [0.085830, 0.135950] |
| Matched other-history mixture minus own profile (co-primary) | -0.007573 | [-0.029800, 0.013568] |
| Simple summary minus own profile | 0.064917 | [0.043304, 0.086273] |
| Common-probe retrieval minus own profile | 0.093818 | [0.072019, 0.115925] |

The matched-donor mixture has slightly lower point-estimate loss than own history; its interval includes both directions. Population improvement alone is therefore insufficient evidence of person specificity. Averaging other histories and the profile model’s shared prediction behavior can produce gains without the person’s own history being necessary. This is an interpretation consistent with the controls, not an identified mechanism.

## Declared model comparisons

| Model | NLL at k=8 | Full-vector Brier | Accuracy |
|---|---:|---:|---:|
| population | 0.562996 | 0.373514 | 0.7980 |
| summary | 0.516637 | 0.333004 | 0.8078 |
| retrieval | 0.545538 | 0.356251 | 0.8235 |
| profile | 0.451720 | 0.289322 | 0.8088 |
| donor | 0.444147 | 0.276881 | 0.8235 |

Profile beats the simple summary by log loss on this test, but that does not rescue the failed own-versus-other co-primary comparison. Accuracy is a secondary measure and does not determine the declared outcome.

| Source budget | Population NLL | Summary NLL | Retrieval NLL | Own profile NLL | Other-history mixture NLL |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.562996 | 0.562996 | 0.562996 | 0.562996 | 0.562996 |
| 2 | 0.562996 | 0.514120 | 0.545742 | 0.504512 | 0.490626 |
| 4 | 0.562996 | 0.512305 | 0.545540 | 0.498116 | 0.482206 |
| 8 | 0.562996 | 0.516637 | 0.545538 | 0.451720 | 0.444147 |

All budgets’ paired contrasts and fixed-bin calibration counts/means/frequencies are in `results_summary.json`; these secondary comparisons were declared before test access. Full probability vectors, per-seed predictions, per-donor assignments and memberships are local artifacts with hashes in `prediction_artifact_manifest.json`. They are not publicly redistributed.

## Fitting and validity

Validation selected dimension eight and regularization 0.1, using the mean probabilities of seeds 17, 29 and 43. Population/summary selected regularization 0.1. Shared parameters were fitted on training people only; validation was not folded into final fitting. New-person MAP inference used only the permitted source choices. Laplace covariance plus 20-node Gaussian quadrature approximate predictive uncertainty. No encoder or personal temperature was added.

Passed: person separation, stable-decision deduplication, valid alternatives and exact raw mapping, full original task-item correspondence, no shared source/target families, physical evaluator/learner separation, exact budgets and constant cohorts, finite normalized probabilities, option-order invariance, synthetic signal recovery and no-transfer control. Independent AI review approved exact hashes before scoring. Synthetic findings are not human evidence. Tests cannot prove all real-world psychological assumptions.

Raw extraction/validation necessarily processed held-out rows mechanically; individual test answers were not printed or inspected to design the experiment. Development loaders read separate label files; the final scorer alone joined the saved test predictions with held-out outcomes. There is no claim of OS-level inaccessible labels.

## Resources and limits

Measured full development process CPU: 115.047 seconds; 23 model-fit invocations, including 18 profile fits (43 shared optimization runs counting nested population refits). Prediction CPU: 16.812 seconds. Conservative aggregate including prior engineering runs: 311.859 seconds, below 14,400. Acquired data/task artifacts: 161,196,132 bytes plus recorded small metadata/reference requests, below 2 GiB. No model weights, paid APIs or rented compute. RESOURCE_USAGE.json distinguishes exact measurements from bounds.

The claim is retrospective static prediction, not temporal forecasting. Holt–Laury items were displayed together; results are conditional on that schedule, not ten independent task families. Both tasks confound canonical alternative meaning with second/right position, so a stable position tendency cannot be separated from monetary preference here. Upstream SRO selection and historical deployment-revision uncertainty remain. A single task pair cannot establish a universal psychological signature, unseen-task transfer, live adaptive selection, or scholarly reasoning.

## Scholarly track and next experiment

The separate source track reverified 512/498/563/101 locations and attempted 30 provisional Rav–Shmuel families (32 occurrences after documented merges/replacements), yielding 24 provisionally usable focal cases. Two independently initiated AI readings and unresolved disagreements are preserved; no knowledgeable-human review or certified family independence is claimed. No scholar model was fitted and no earlier confirmation case was scored. See SCHOLAR_AUDIT.md.

**One justified next experiment:** an independently frozen replication on new participants with counterbalanced option positions and a source-blind profile-marginal population comparator, retaining the own-versus-matched-other test at eight choices. This would test whether any gain requires the individual’s own evidence rather than shared model behavior or position bias. It is proposed, not executed; the present test must not be reused as fresh confirmation.
