"""Render saved aggregate outputs only; no participant labels or scoring."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
def read(f):return json.loads((R/f).read_text(encoding='utf-8-sig'))
def write(f,s):(R/f).write_text(s,encoding='utf-8',newline='\n')
def effect(v):return f"{v['estimate']:.6f} [{v['ci95'][0]:.6f}, {v['ci95'][1]:.6f}]"

def main():
    test=read('exploratory_results.json');dev=read('development_results.json');selection=read('development_selection.json');precision=read('precision_results.json')
    s='''# Diagnostic results — exploratory, not confirmation

PR5 remains inconclusive. The stronger training-only item-frequency baseline outperformed own-history predictions in the declared reuse of102 exposed people. Single-donor replacement does not demonstrate a person-specific advantage. No independent confirmation ran.

All original35 manifested artifacts were available and hash-verified; no weights or old outputs were reconstructed or refitted. The independent AI methods signoff and diagnostic lock preceded new test probabilities. Freeze commit: dbb208f2129f356f414e9e47915f56ef40653ed9. The scorer recorded its attempt before label access and completed exactly once. This study has304 training,102 development and102 exposed-test people, eight nested source choices, ten target choices per person, one target schedule family. No exclusions changed.

## Development selection and pairing diagnostic

Fixed Beta(.5,.5) training-only item frequencies were selected by development NLL at8; there was no smoothing/calibration search. A target-context fit was unnecessary for these common ten items. Development banks were disjoint51-person opposite folds; test reference bank was all102 development people. The larger test bank is a declared design difference, not a new recipient-dependent computation. Bank posterior states use source answers only.

| Source-blind candidate | Development NLL at8 |
|---|---:|
'''
    for n,v in selection['scores'].items():s+=f'| {n} | {v:.6f} |\n'
    s+='\nDevelopment-only inference permutation-minus-own: '+effect(dev['contrasts']['inference_permutation_minus_own_8'])+''' nats. This moves intact histories, without retraining. The descriptive interval ignores cross-fold bank dependencies and original model selection; it cannot establish generalization. Development value-minus-own was '''+effect(dev['contrasts']['value_8'])+'''. Pairing sensitivity alone is insufficient when the strong source-blind comparator is better.

## Declared exposed-test contrasts

Positive values favor own prediction, except the Jensen gap which measures averaging benefit. Each interval is a2,000-draw paired participant percentile interval conditional on fitted models and fixed bank, not independent confirmation or simultaneous coverage. Zero-budget identity/mixture compare the historical fallback; coherent zero below uses the integrated prior. Tiny zero-budget values around1e-17 are floating-point noise.

| k | Strong-baseline minus own | Mean single-donor loss minus own | Donor-mixture loss minus own | Jensen gap |
|---:|---|---|---|---|
'''
    for b in [0,2,4,8]:s+=f'| {b} | '+' | '.join(effect(test['contrasts'][f'{n}_{b}']) for n in ['value','identity','mixture','jensen_gap'])+' |\n'
    s+='''
At8, the donor replacement estimate is slightly positive while the probability-mixture estimate is negative. Their0.010585-nat difference is the Jensen averaging benefit, not evidence of identity. Both specificity intervals cross zero. The item-frequency comparator beats own by0.071577 nats; this diagnoses a weak historical baseline comparison, not the absence of all personal information. The empirical-history reference also predicts well without recipient history; its at8 difference from own is '''+effect(test['contrasts']['empirical_reference_minus_own_8'])+'''.

## Coherent learning curve and all saved metrics

Own zero is the same frozen model's integrated Normal prior. The historical own-zero fallback is retained separately. Own NLL improves from0.611063 at0 to0.451720 at8, yet item frequencies achieve0.380143. A learning-curve improvement against the prior is not sufficient evidence of useful personalization.

| Saved predictor | NLL | Full-vector Brier | Accuracy |
|---|---:|---:|---:|
'''
    for n,m in test['metrics'].items():s+=f"| {n} | {m['nll']:.6f} | {m['brier']:.6f} | {m['accuracy']:.6f} |\n"
    s+='''
All other declared baseline-minus-own contrasts, all four development budgets and ten-bin calibration counts/probabilities/outcome rates for every predictor are retained in `exploratory_results.json` and `development_results.json`; no unreported endpoint was dropped. Accuracy uses positive option at p>=.5. Brier sums both alternatives, so it is twice the single-positive-option squared error. These metrics do not count ten schedule rows as independent task families.

## Feature rank and penalty audit

Source design rank4; target rank3. For each seed17/29/43, source×B rank4 and target×B rank3, with selected latent dimension8. Isotropic prior rotations B→BQ and z→Qᵀz preserve predictions, so latent axes are not named psychological traits. The source likelihood has at most four informed directions; the prior supplies remaining curvature. Frobenius norms are4.725634,4.722325,4.724885. Original penalty λ||B||²/(2FK) has coefficients0.003125,0.0015625,0.00078125 for K=2/4/8 at λ=.1,F=8. Thus dimension search also changes effective Frobenius shrinkage. The prospective rank2 and dimension-independent penalty are a separately declared future definition, never retroactively fitted here.

Fixed source-later and target-risky second positions remain confounded with semantic preference. Representation permutation checks passed but cannot establish actual counterbalancing. No trait, causal mechanism, unseen-task or temporal claim follows.

## Joint precision illustration

Development paired SDs: '''+f"{precision['development_sd'][0]:.6f}, {precision['development_sd'][1]:.6f}; correlation {precision['correlation'][0][1]:.6f}."+'''
Residuals are centered to imposed equal true advantages; observed development means are not treated as expected positive effects. Simulation preserves the two paired contrast axes, resampling people with200 outer samples and2,000 inner bootstrap draws, fixed seed20261125. Both lower endpoints must exceed0.

| Independent people | Joint success at0 | At.01 each | At.02 each | MC SE at.02 | Mean half-widths (value, identity) |
|---:|---:|---:|---:|---:|---|
'''
    for n in [100,250,500,1000,2000]:
        rr=[r for r in precision['results'] if r['n']==n];v=rr[-1]
        s+=f"| {n} | {rr[0]['joint_success_rate']:.3f} | {rr[1]['joint_success_rate']:.3f} | {v['joint_success_rate']:.3f} | {v['monte_carlo_se']:.3f} | {v['mean_half_width'][0]:.5f}, {v['mean_half_width'][1]:.5f} |\n"
    s+='''
Under this conditional approximation500 people give91.5% simulated joint success at.02 each (Monte Carlo SE1.97 percentage points). This is not an enrollment recommendation. Reported binomial SE=0 at simulated0%/100% does not mean certainty; future size selection uses a Wilson lower bound, avoiding that degeneracy. Cross-fold bank dependence, fitted-model uncertainty, counterbalancing and new-cohort variance are not captured. The future rule requires new-development residuals, the newly selected comparator and matching-layout donors, with actual candidate n100/252/500/1000/2000 and a frozen numeric n before confirmation enrollment. See `REPLICATION_PROTOCOL.md`; no human observations are created by this simulation.
'''
    write('DIAGNOSTIC_RESULTS.md',s)
    ledger=read('run_ledger.json');seconds=sum(e.get('process_cpu_seconds') or 0 for e in ledger['events'])+read('reviewer_validation.json')['process_cpu_seconds']
    write('RESOURCE_ACCOUNT.md',f'''# Resource account

Measured main analysis/test/planning process CPU plus independent diagnostic reviewer: {seconds:.6f} seconds. Per-stage values are in run_ledger.json and reviewer_validation.json. Shared model fits:0. Fixed closed-form training item estimates:10. All source adaptations are inference with saved weights. Conservative smoke forecast65.742188 seconds for bounded inference; measured inference stayed below it. Precision planning was additional development-only resampling, not fitting. No aggregate fitting budget was consumed; the4-hour cap was not approached.

Initial inventory process timing was not recorded: its original zero placeholder was corrected to null before exploratory access, with explanation. Metadata browsing, prose preparation, scholar packet creation and final integrity checks were not comprehensively CPU-timed; do not interpret the measured subtotal as all wall/CPU time in the task. No worker performed new shared model fitting.

Diagnostic downloads0. Admission direct HTTP bodies462145 bytes; browser transport sizes unavailable. Two attempted2.6MB supplementary retrievals conservatively total5.2MB plus HTML/search overhead, comfortably below2GiB. No participant response or MRI downloads; no paid services/rented compute/contact/recruitment. Participant arrays, fitted models and local linkage remain ignored and unpublished.
''')
    print('Reports rendered from saved aggregate JSON only.')
if __name__=='__main__':main()
