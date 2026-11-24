"""Explicit development, freeze, prediction and one-shot evaluation stages."""
import argparse
import hashlib
import json
import pickle
import time
from pathlib import Path
import numpy as np
from data_pipeline import ROOT, LOCAL, dump, digest, jsonl
from models import PopulationModel, SummaryModel, ProfileModel, CommonProbeRetrieval, participant_scores, paired_bootstrap

BUDGETS=(0,2,4,8)
SEEDS=(17,29,43)
CONFIG=dict(budgets=list(BUDGETS),primary_budget=8,population_reg=[.1,1.],summary_reg=[.1,1.],
    profile_dim=[2,4,8],profile_reg=[.1,1.],profile_seeds=list(SEEDS),epochs=100,
    adam_lr=.04,newton_training_steps=5,newton_damping=.8,quadrature_nodes=20,
    bootstrap_draws=2000,bootstrap_seed=20261124,donor_assignments=5,fit_cpu_cap=14400)

def rows(name):
    with (LOCAL/name).open(encoding='utf-8') as f:
        for line in f: yield json.loads(line)

def load(part, labels=False):
    """Learner inputs contain no target answer; only requested development labels join."""
    if labels and part=='test': raise RuntimeError('Test labels belong exclusively to score()')
    episodes={r['person_id']:r for r in rows('episode_membership.jsonl') if r['partition']==part and r['budget']==8}
    people=sorted(episodes)
    source={r['decision_id']:r for r in rows('source_observations.jsonl') if r['partition']==part}
    target={r['decision_id']:r for r in rows('target_scenarios.jsonl') if r['partition']==part}
    sx=[];sy=[];tx=[];ids=[]
    for p in people:
        s=[source[i] for i in episodes[p]['support']];t=[target[i] for i in episodes[p]['targets']]
        sx.append([r['feature_difference'] for r in s]);sy.append([r['chosen_alternative']=='later' for r in s])
        tx.append([r['feature_difference'] for r in t]);ids.append([r['decision_id'] for r in t])
    d=dict(people=people,sx=np.array(sx),sy=np.array(sy,dtype=float),tx=np.array(tx),ids=ids)
    if labels:
        lab={r['decision_id']:r['chosen_alternative']=='risky' for r in rows(f'evaluator_labels_{part}.jsonl')}
        d['ty']=np.array([[lab[i] for i in row] for row in ids],dtype=float)
    return d

def fit_args(d): return d['sx'],d['sy'],d['tx'],d['ty']
def predict(model,d,b): return model.predict(d['sx'][:,:b],d['sy'][:,:b],d['tx'])
def loss(y,p): return float(participant_scores(y,p)['nll'].mean())

def validate_data():
    partitions=json.loads((LOCAL/'person_partitions.json').read_text())
    ep=list(rows('episode_membership.jsonl')); observed={r['decision_id']:r for r in rows('canonical_observations.jsonl')}
    assert len(observed)==19300
    scenarios=list(rows('target_scenarios.jsonl'))
    assert not any('chosen_alternative' in r or 'response' in r for r in scenarios)
    for r in observed.values():
        assert r['chosen_alternative'] in [a['id'] for a in r['alternatives']]
        assert r['observed'] and not r['synthetic']
        assert not r['predecessor_dependencies'] and r['pre_choice_feedback'] is None
    for e in ep:
        assert e['partition']==partitions[e['person_id']]
        assert len(e['support'])==e['budget'] and len(set(e['support']))==e['budget']
        assert not set(e['support'])&set(e['targets'])
        assert not {observed[i]['family_id'] for i in e['support']}&{observed[i]['family_id'] for i in e['targets']}
        assert all(observed[i]['person_id']==e['person_id'] for i in e['support']+e['targets'])
    cohorts={p:{r['person_id'] for r in ep if r['partition']==p} for p in ['train','validation','test']}
    assert not cohorts['train']&cohorts['test'] and not cohorts['validation']&cohorts['test'] and not cohorts['train']&cohorts['validation']
    for p in cohorts:
        for b in BUDGETS: assert {r['person_id'] for r in ep if r['partition']==p and r['budget']==b}==cohorts[p]
    dump(ROOT/'data_validation.json',dict(passed=True,canonical_decisions=len(observed),episodes=len(ep),
        tests=['person split isolation','stable decision uniqueness','valid alternatives','evaluator fields absent from target scenarios','same cohorts across budgets','exact support charging','source-target family disjointness','no declared transitions or feedback','observed flag']))

def develop(smoke=False):
    start=time.process_time();tr=load('train',True);va=load('validation',True)
    if smoke:
        d={k:(v[:32] if isinstance(v,(list,np.ndarray)) else v) for k,v in tr.items()}
        t=time.process_time();m=ProfileModel(dim=2,reg=.1,seed=17,epochs=10,population_reg=.1).fit(*fit_args(d))
        prediction=predict(m,va,8)
        cpu=time.process_time()-t
        forecast=cpu*(304/32)*(100/10)*18*2 # conservative factor for grid dimensions
        dump(ROOT/'smoke.json',dict(cpu_seconds=cpu,participants=32,epochs=10,valid_probability=bool(np.isfinite(prediction).all()),
             forecast_full_grid_cpu_seconds=forecast,cap_seconds=14400,forecast_method='smoke * people ratio * epochs ratio * 18 fits * dimension safety factor 2'))
        print('Smoke CPU',cpu,'conservative full-grid forecast',forecast)
        return
    if (LOCAL/'test_predictions.npz').exists(): raise RuntimeError('Development closed after test prediction')
    prior=json.loads((ROOT/'resource_prefit.json').read_text())['prior_process_cpu_seconds_upper_bound']
    forecast=json.loads((ROOT/'resource_smoke_refined.json').read_text())['forecast_full_grid_cpu_seconds']
    if prior+forecast>CONFIG['fit_cpu_cap']: raise RuntimeError('Forecast exceeds cumulative CPU cap')
    dump(ROOT/'model_config.json',CONFIG)
    result=[];allmodels={};ledger=[]
    def record(name,config,models):
        p=np.mean([predict(m,va,8) for m in models],axis=0)
        nll=loss(va['ty'],p);cpu=sum(m.cpu_seconds for m in models)
        row=dict(model=name,configuration=config,validation_nll=nll,fit_cpu_seconds=cpu)
        result.append(row);allmodels[(name,json.dumps(config,sort_keys=True))]=models
        ledger.append(row);dump(ROOT/'development_fit_ledger.json',ledger)
        if prior+time.process_time()-start>CONFIG['fit_cpu_cap']: raise RuntimeError('Fit CPU cap reached')
        return nll
    for reg in CONFIG['population_reg']:
        record('population',dict(reg=reg),[PopulationModel(reg).fit(*fit_args(tr))])
    popbest=min([r for r in result if r['model']=='population'],key=lambda r:(r['validation_nll'],-r['configuration']['reg']))
    popreg=popbest['configuration']['reg']
    for reg in CONFIG['summary_reg']:
        record('summary',dict(reg=reg,population_reg=popreg),[SummaryModel(reg,population_reg=popreg).fit(*fit_args(tr))])
    record('retrieval',dict(reg=popreg),[CommonProbeRetrieval(popreg).fit(*fit_args(tr))])
    for dim in CONFIG['profile_dim']:
        for reg in CONFIG['profile_reg']:
            models=[]
            for seed in SEEDS:
                models.append(ProfileModel(dim,reg,seed,CONFIG['epochs'],population_reg=popreg).fit(*fit_args(tr)))
                used=time.process_time()-start
                if prior+used>CONFIG['fit_cpu_cap']: raise RuntimeError('Fit CPU cap reached')
            record('profile',dict(dim=dim,reg=reg,population_reg=popreg),models)
    selected={}
    for name in ['population','summary','retrieval','profile']:
        best=min([r for r in result if r['model']==name],key=lambda r:(r['validation_nll'],r['configuration'].get('dim',0),-r['configuration']['reg']))
        selected[name]=best
    bundle={name:allmodels[(name,json.dumps(r['configuration'],sort_keys=True))] for name,r in selected.items()}
    with (LOCAL/'fitted_models.pkl').open('wb') as f: pickle.dump(bundle,f)
    dump(ROOT/'development_results.json',dict(comparisons=result,selected=selected,total_development_process_cpu_seconds=time.process_time()-start))
    dump(ROOT/'selected_config.json',selected)
    print('Development completed; test targets untouched.')

def freeze():
    if (LOCAL/'test_predictions.npz').exists(): raise RuntimeError('Cannot refreeze after test predictions')
    review=json.loads((ROOT/'review_signoff.json').read_text())
    if not review.get('approved'): raise RuntimeError('Independent review not approved')
    for f,h in review['reviewed_files'].items():
        if digest((ROOT/f).read_bytes())!=h: raise RuntimeError('Independent review stale: '+f)
    required=['PROTOCOL.md','DATA_ADMISSION.md','DATA_CONTRACT.json','model_config.json','selected_config.json',
       'source_manifest.json','split_manifest.json','data_pipeline.py','run_lab.py','models.py','test_models.py','review_signoff.json','data_validation.json']
    hashes={f:digest((ROOT/f).read_bytes()) for f in required}
    hashes['local_data/fitted_models.pkl']=digest((LOCAL/'fitted_models.pkl').read_bytes())
    dump(ROOT/'freeze_manifest.json',dict(status='FROZEN_BEFORE_TEST_PREDICTION',files=hashes,
        split_artifacts=json.loads((ROOT/'split_manifest.json').read_text())['artifacts']))
    print('Protocol and artifacts frozen. Commit this manifest before predict.')

def check_freeze():
    manifest=json.loads((ROOT/'freeze_manifest.json').read_text())
    for f,h in manifest['files'].items(): assert digest((ROOT/f).read_bytes())==h, f+' changed after freeze'
    for f,h in manifest['split_artifacts'].items(): assert digest((LOCAL/f).read_bytes())==h, f+' changed after freeze'

def make_predictions():
    check_freeze()
    if (LOCAL/'test_predictions.npz').exists(): raise RuntimeError('Final predictions already exist; do not overwrite')
    te=load('test');donors=load('validation') # no target labels loaded
    with (LOCAL/'fitted_models.pkl').open('rb') as f: models=pickle.load(f)
    assignments=[]
    for person in te['people']:
        indexes=[]
        for a in range(5):
            i=int(digest(f'20261124|donor|{a}|{person}'),16)%len(donors['people'])
            while i in indexes:i=(i+1)%len(donors['people'])
            indexes.append(i)
        assignments.append(indexes)
    jsonl(LOCAL/'donor_assignments.jsonl',[dict(person=p,donors=[donors['people'][i] for i in ii]) for p,ii in zip(te['people'],assignments)])
    output={};predrows=[];start=time.process_time()
    for b in BUDGETS:
        for name,ensemble in models.items():
            pp=np.stack([predict(m,te,b) for m in ensemble]);output[f'{name}_{b}']=pp.mean(0)
            if name=='profile':output[f'profile_seeds_{b}']=pp
        dprobs=[]
        for a in range(5):
            ind=[ii[a] for ii in assignments];d=dict(sx=donors['sx'][ind],sy=donors['sy'][ind],tx=te['tx'])
            dprobs.append(np.mean([predict(m,d,b) for m in models['profile']],axis=0))
        output[f'donor_assignments_{b}']=np.stack(dprobs)
        output[f'donor_{b}']=np.mean(dprobs,axis=0)
        for name in ['population','summary','retrieval','profile','donor']:
            pp=output[f'{name}_{b}'];assert np.isfinite(pp).all() and ((pp>=0)&(pp<=1)).all()
            for i,p in enumerate(te['people']):
                for j,did in enumerate(te['ids'][i]):
                    predrows.append(dict(person_id=p,decision_id=did,model=name,budget=b,probabilities={'safe':float(1-pp[i,j]),'risky':float(pp[i,j])}))
    np.savez_compressed(LOCAL/'test_predictions.npz',**output)
    jsonl(LOCAL/'full_probability_predictions.jsonl',predrows)
    dump(LOCAL/'prediction_membership.json',dict(people=te['people'],decision_ids=te['ids']))
    dump(ROOT/'prediction_artifact_manifest.json',dict(prediction_cpu_seconds=time.process_time()-start,people=len(te['people']),target_decisions=len(te['people'])*10,
        files={f:digest((LOCAL/f).read_bytes()) for f in ['test_predictions.npz','full_probability_predictions.jsonl','prediction_membership.json','donor_assignments.jsonl']}))
    print('All final probabilities saved without reading test target labels.')

def score():
    check_freeze()
    if (ROOT/'results_summary.json').exists():raise RuntimeError('Final evaluation already scored; preserve it')
    predmanifest=json.loads((ROOT/'prediction_artifact_manifest.json').read_text())
    for f,h in predmanifest['files'].items():assert digest((LOCAL/f).read_bytes())==h
    membership=json.loads((LOCAL/'prediction_membership.json').read_text())
    # This is the sole final test-label join. No fitted object is present here.
    labels={r['decision_id']:r['chosen_alternative']=='risky' for r in rows('evaluator_labels_test.jsonl')}
    y=np.array([[labels[i] for i in row] for row in membership['decision_ids']],dtype=float)
    predictions=np.load(LOCAL/'test_predictions.npz');results={};contrasts={}
    for b in BUDGETS:
        scores={}
        for name in ['population','summary','retrieval','profile','donor']:
            p=predictions[f'{name}_{b}'];s=participant_scores(y,p);scores[name]=s
            calibration=[]
            bins=np.minimum((p*10).astype(int),9)
            for v in range(10):
                mask=bins==v
                calibration.append(dict(bin=v,count=int(mask.sum()),mean_probability=float(p[mask].mean()) if mask.any() else None,observed_frequency=float(y[mask].mean()) if mask.any() else None))
            results[f'{name}_{b}']={**{k:float(v.mean()) for k,v in s.items()},'calibration':calibration}
        for name in ['population','donor','summary','retrieval']:
            contrasts[f'{name}_minus_profile_{b}']=paired_bootstrap(scores[name]['nll'],scores['profile']['nll'])
    a=contrasts['population_minus_profile_8'];b=contrasts['donor_minus_profile_8'];s=contrasts['summary_minus_profile_8']
    if a['ci95'][0]>0 and b['ci95'][0]>0:
        outcome='positive individual signal' if s['ci95'][0]>0 else 'simpler model sufficient'
    elif a['ci95'][1]<=0 or b['ci95'][1]<=0:outcome='extension not supported'
    else:outcome='inconclusive'
    dump(ROOT/'results_summary.json',dict(outcome=outcome,people=len(y),target_decisions=int(y.size),target_families=1,metrics=results,contrasts=contrasts,
        uncertainty='95% paired participant bootstrap; conditional on fitted models, fixed validation donor pool and these task families',practical_threshold=0,
        final_evaluation_count=1))
    print('Final evaluation completed:',outcome)

if __name__=='__main__':
    arg=argparse.ArgumentParser();arg.add_argument('stage',choices=['validate','smoke','develop','freeze','predict','score']);a=arg.parse_args()
    {'validate':validate_data,'smoke':lambda:develop(True),'develop':develop,'freeze':freeze,'predict':make_predictions,'score':score}[a.stage]()
