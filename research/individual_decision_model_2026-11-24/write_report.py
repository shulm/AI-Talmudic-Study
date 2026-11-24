"""Render aggregate results from the single completed evaluation; never fit or score."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
def read(name):return json.loads((P/name).read_text(encoding='utf-8'))
def main():
    r=read('results_summary.json');d=read('development_results.json');p=read('prediction_artifact_manifest.json');s=read('source_manifest.json')
    refs=read('references_manifest.json'); prior=read('resource_prefit.json')['prior_process_cpu_seconds_upper_bound']
    resources=dict(admitted_dataset='SRO Complete_02-16-2019',measured_acquired_artifact_bytes=s['downloaded_artifact_bytes'],
        reviewer_measured_http_bytes=refs['resource_accounting']['measured_http_body_bytes'],
        local_metadata_extra_bytes=sum(f.stat().st_size for f in (P/'local_data').glob('*tree.json'))+(P/'local_data'/'hf_metadata.json').stat().st_size,
        browser_transfer_bytes='not exposed; no large data or model weights obtained through browser',
        model_weights_bytes=0,paid_calls=0,new_rented_compute=False,
        development_measured_process_cpu_seconds=d['total_development_process_cpu_seconds'],
        development_model_fit_invocations=23,development_shared_optimization_runs=43,
        optimization_breakdown={'population_ridge_including_nested_refits':23,'summary_ridge':2,'profile_basis':18},
        development_fit_cpu_seconds=sum(x['fit_cpu_seconds'] for x in d['comparisons']),
        prediction_measured_process_cpu_seconds=p['prediction_cpu_seconds'],
        prior_engineering_cpu_seconds_conservative_bound=prior,
        cumulative_fitting_and_prediction_cpu_seconds_upper_bound=prior+d['total_development_process_cpu_seconds']+p['prediction_cpu_seconds'],
        fitting_cap_seconds=14400,download_cap_bytes=2*1024**3,
        caveat='Prior bound includes measured smoke/synthetic runs and allowance for an initially unmeasured failed synthetic run; do not describe the bound as an exact measurement.')
    (P/'RESOURCE_USAGE.json').write_text(json.dumps(resources,indent=2)+'\n',encoding='utf-8')
    lines=['# Results — individual decision pilot','',
      '**Qualified outcome: inconclusive.** Eight own-person source choices improved prediction relative to the declared population and simple-summary baselines, but did not improve on the matched other-person history control. The two co-primary criteria were not jointly satisfied. This experiment does not demonstrate individual-specific cross-task transfer or practical benefit.','',
      'The independently reviewed protocol and artifacts were frozen in commit `430c0ec4e74db8c265e77e1eb028b21abe6bff43` before final predictions. All declared predictions were saved before the final label join. **One final human evaluation; zero invalidated or repeated human test runs.** Earlier engineering corrections are in RUN_LOG.md.','',
      '## Data and independent counts','',
      'Admitted SRO `Complete_02-16-2019`, revision `4e6e837fb5aaca87ed5914fd9be251156f43eec9`, Kirby → Holt–Laury. Of 522 linked people, 14 incomplete target schedules were excluded before model comparisons. Split: 304 training, 102 validation, **102 held-out people**. Test: 1,020 target choices in **one target schedule family**. Each test person supplied the same eight source probes; curves use nested 0/2/4/8 budgets with the same people and targets. Three fit seeds and five donor assignments are repeated computations, not additional independent people.','',
      'Cross-Psych-101 was rejected before training: its actual 601-person release conflicts with the paper’s 591-person public cohort after opt-outs; licensing and canonical decision provenance also remain unresolved. See DATA_ADMISSION.md.','',
      '## Co-primary results at eight source choices','',
      'Positive differences favor own history. Units are natural-log loss per complete alternative, averaged within person and then equally across people. Intervals are two-sided 95% paired participant-cluster percentile bootstrap, 2,000 draws, conditional on fitted models, fixed development donor pool and these task families. The prespecified signal threshold is zero, not an application utility threshold.','',
      '| Comparison | Mean loss reduction | 95% interval |','|---|---:|---:|']
    for key,label in [('population','Population minus own profile (co-primary)'),('donor','Matched other-history mixture minus own profile (co-primary)'),('summary','Simple summary minus own profile'),('retrieval','Common-probe retrieval minus own profile')]:
        c=r['contrasts'][f'{key}_minus_profile_8'];lines.append(f"| {label} | {c['estimate']:.6f} | [{c['ci95'][0]:.6f}, {c['ci95'][1]:.6f}] |")
    lines += ['', 'The matched-donor mixture has slightly lower point-estimate loss than own history; its interval includes both directions. Population improvement alone is therefore insufficient evidence of person specificity. Averaging other histories and the profile model’s shared prediction behavior can produce gains without the person’s own history being necessary. This is an interpretation consistent with the controls, not an identified mechanism.','',
      '## Declared model comparisons','', '| Model | NLL at k=8 | Full-vector Brier | Accuracy |','|---|---:|---:|---:|']
    for name in ['population','summary','retrieval','profile','donor']:
        m=r['metrics'][f'{name}_8'];lines.append(f"| {name} | {m['nll']:.6f} | {m['brier']:.6f} | {m['accuracy']:.4f} |")
    lines += ['','Profile beats the simple summary by log loss on this test, but that does not rescue the failed own-versus-other co-primary comparison. Accuracy is a secondary measure and does not determine the declared outcome.','',
      '| Source budget | Population NLL | Summary NLL | Retrieval NLL | Own profile NLL | Other-history mixture NLL |','|---:|---:|---:|---:|---:|---:|']
    for b in [0,2,4,8]:lines.append('| '+str(b)+' | '+' | '.join(f"{r['metrics'][f'{n}_{b}']['nll']:.6f}" for n in ['population','summary','retrieval','profile','donor'])+' |')
    lines += ['', 'All budgets’ paired contrasts and fixed-bin calibration counts/means/frequencies are in `results_summary.json`; these secondary comparisons were declared before test access. Full probability vectors, per-seed predictions, per-donor assignments and memberships are local artifacts with hashes in `prediction_artifact_manifest.json`. They are not publicly redistributed.','',
      '## Fitting and validity','',
      'Validation selected dimension eight and regularization 0.1, using the mean probabilities of seeds 17, 29 and 43. Population/summary selected regularization 0.1. Shared parameters were fitted on training people only; validation was not folded into final fitting. New-person MAP inference used only the permitted source choices. Laplace covariance plus 20-node Gaussian quadrature approximate predictive uncertainty. No encoder or personal temperature was added.','',
      'Passed: person separation, stable-decision deduplication, valid alternatives and exact raw mapping, full original task-item correspondence, no shared source/target families, physical evaluator/learner separation, exact budgets and constant cohorts, finite normalized probabilities, option-order invariance, synthetic signal recovery and no-transfer control. Independent AI review approved exact hashes before scoring. Synthetic findings are not human evidence. Tests cannot prove all real-world psychological assumptions.','',
      'Raw extraction/validation necessarily processed held-out rows mechanically; individual test answers were not printed or inspected to design the experiment. Development loaders read separate label files; the final scorer alone joined the saved test predictions with held-out outcomes. There is no claim of OS-level inaccessible labels.','',
      '## Resources and limits','',
      f"Measured full development process CPU: {d['total_development_process_cpu_seconds']:.3f} seconds; 23 model-fit invocations, including 18 profile fits (43 shared optimization runs counting nested population refits). Prediction CPU: {p['prediction_cpu_seconds']:.3f} seconds. Conservative aggregate including prior engineering runs: {resources['cumulative_fitting_and_prediction_cpu_seconds_upper_bound']:.3f} seconds, below 14,400. Acquired data/task artifacts: {s['downloaded_artifact_bytes']:,} bytes plus recorded small metadata/reference requests, below 2 GiB. No model weights, paid APIs or rented compute. RESOURCE_USAGE.json distinguishes exact measurements from bounds.", '',
      'The claim is retrospective static prediction, not temporal forecasting. Holt–Laury items were displayed together; results are conditional on that schedule, not ten independent task families. Both tasks confound canonical alternative meaning with second/right position, so a stable position tendency cannot be separated from monetary preference here. Upstream SRO selection and historical deployment-revision uncertainty remain. A single task pair cannot establish a universal psychological signature, unseen-task transfer, live adaptive selection, or scholarly reasoning.','',
      '## Scholarly track and next experiment','',
      'The separate source track reverified 512/498/563/101 locations and attempted 30 provisional Rav–Shmuel families (32 occurrences after documented merges/replacements), yielding 24 provisionally usable focal cases. Two independently initiated AI readings and unresolved disagreements are preserved; no knowledgeable-human review or certified family independence is claimed. No scholar model was fitted and no earlier confirmation case was scored. See SCHOLAR_AUDIT.md.','',
      '**One justified next experiment:** an independently frozen replication on new participants with counterbalanced option positions and a source-blind profile-marginal population comparator, retaining the own-versus-matched-other test at eight choices. This would test whether any gain requires the individual’s own evidence rather than shared model behavior or position bias. It is proposed, not executed; the present test must not be reused as fresh confirmation.','']
    (P/'RESULTS.md').write_text('\n'.join(lines),encoding='utf-8')
if __name__=='__main__':main()
