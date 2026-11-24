"""Read-only PR5 diagnostics. Never mutate, refit, or rescore original outputs."""
import argparse
import hashlib
import importlib
import json
import pickle
import sys
import time
import subprocess
from pathlib import Path
import numpy as np

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
LOCAL=ROOT/'local_data'
ORIGINAL_DEFAULT=Path(r'C:\Users\David\.codex\worktrees\individual-decision-pilot\AI Talmudic Study\research\individual_decision_model_2026-11-24')
DELIVERY='6ca2dedc547144d7279696bd5322c1e39c7f03d3'
BUDGETS=(0,2,4,8)
CANDIDATES=('item_frequency','integrated_prior','empirical_reference','legacy_population')
def sha(b):return hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
def dump(path,obj):path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def rows(path):
    with path.open(encoding='utf-8') as f:
        for l in f:yield json.loads(l)
def event(stage,cpu,**extra):
    p=ROOT/'run_ledger.json';j=read(p) if p.exists() else {'scope':'exploratory follow-up; original run preserved','events':[]}
    j['events'].append(dict(stage=stage,process_cpu_seconds=cpu,**extra));dump(p,j)
def original():return Path(read(LOCAL/'original_location.json')['path'])

def inventory(old):
    started=time.process_time()
    LOCAL.mkdir(exist_ok=True)
    if (ROOT/'diagnostic_spec_manifest.json').exists():raise RuntimeError('Inventory/spec already saved; do not overwrite')
    base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=old, text=True).strip()
    assert base==DELIVERY
    checks={}
    for manifest in ['freeze_manifest.json','split_manifest.json','prediction_artifact_manifest.json','source_manifest.json']:
        m=read(old/manifest)
        if manifest=='freeze_manifest.json': pairs=m['files'].items()
        elif manifest=='split_manifest.json':pairs=[('local_data/'+f,h) for f,h in m['artifacts'].items()]
        elif manifest=='prediction_artifact_manifest.json':pairs=[('local_data/'+f,h) for f,h in m['files'].items()]
        else:pairs=[('local_data/'+r['file'],r['sha256']) for r in m['files']]
        for f,h in pairs:
            assert (old/f).exists(),f+' missing'; actual=sha((old/f).read_bytes());assert actual==h,f+' hash mismatch'
            checks[f]=actual
    dump(LOCAL/'original_location.json',{'path':str(old)})
    dump(ROOT/'source_manifest.json',{'delivery_commit':base,'freeze_commit':'430c0ec4e74db8c265e77e1eb028b21abe6bff43','original_artifacts_available':True,
        'reconstructed_artifacts':False,'verified_original_files':checks,'additional_diagnostic_download_bytes':0})
    dump(ROOT/'diagnostic_spec_manifest.json',{'status':'declared_before_new_analysis','files':{f:sha((ROOT/f).read_bytes()) for f in ['DIAGNOSTIC_PROTOCOL.md','contrast_definitions.json']}})
    event('inventory_and_specification',time.process_time()-started,original_artifacts_verified=len(checks),outcomes_inspected=False)

def verify_original():
    old=original()
    for f,h in read(ROOT/'source_manifest.json')['verified_original_files'].items():assert sha((old/f).read_bytes())==h,f
    for f,h in read(ROOT/'diagnostic_spec_manifest.json')['files'].items():assert sha((ROOT/f).read_bytes())==h,f
    return old

def bundle(old):
    sys.path.insert(0,str(old));importlib.import_module('models')
    with (old/'local_data/fitted_models.pkl').open('rb') as f:return pickle.load(f)

def load(old,partition):
    l=old/'local_data'
    eps={e['person_id']:e for e in rows(l/'episode_membership.jsonl') if e['partition']==partition and e['budget']==8}
    sources={r['decision_id']:r for r in rows(l/'source_observations.jsonl') if r['partition']==partition}
    targets={r['decision_id']:r for r in rows(l/'target_scenarios.jsonl') if r['partition']==partition}
    people=sorted(eps);sx=[];sy=[];tx=[];ids=[]
    for p in people:
        s=[sources[i] for i in eps[p]['support']];t=[targets[i] for i in eps[p]['targets']]
        assert len(s)==8 and len(t)==10
        sx.append([r['feature_difference'] for r in s]);sy.append([r['chosen_alternative']=='later' for r in s])
        tx.append([r['feature_difference'] for r in t]);ids.append([r['decision_id'] for r in t])
    d=dict(people=people,sx=np.array(sx),sy=np.array(sy,dtype=float),tx=np.array(tx),ids=ids)
    assert np.allclose(d['tx'],d['tx'][0]) and np.allclose(d['sx'],d['sx'][0])
    return d

def labels(old,d,partition,allow_exposed_test=False):
    if partition=='test' and not allow_exposed_test:raise RuntimeError('Exposed-test labels restricted to declared exploratory scorer')
    mapping={r['decision_id']:float(r['chosen_alternative']=='risky') for r in rows(old/'local_data'/f'evaluator_labels_{partition}.jsonl')}
    return np.array([[mapping[i] for i in row] for row in d['ids']])

def nll(y,p):
    p=np.clip(p,1e-12,1-1e-12);return (-y*np.log(p)-(1-y)*np.log1p(-p)).mean(-1)
def ci(diff):
    diff=np.asarray(diff);assert diff.ndim==1
    rng=np.random.default_rng(20261124);boot=diff[rng.integers(len(diff),size=(2000,len(diff)))].mean(1)
    return dict(estimate=float(diff.mean()),ci95=np.quantile(boot,[.025,.975]).tolist(),participants=len(diff))
def metrics(y,p):
    assert p.shape==y.shape and np.isfinite(p).all() and ((p>=0)&(p<=1)).all()
    bins=np.minimum((p*10).astype(int),9);cal=[]
    for b in range(10):
        mask=bins==b;cal.append(dict(bin=b,count=int(mask.sum()),mean_probability=float(p[mask].mean()) if mask.any() else None,observed_frequency=float(y[mask].mean()) if mask.any() else None))
    return dict(nll=float(nll(y,p).mean()),brier=float((2*(p-y)**2).mean()),accuracy=float(((p>=.5)==y).mean()),calibration=cal)

def prior_predict(models,tx):
    return np.mean([m.predict_from_posterior(tx,np.zeros(m.dim),np.eye(m.dim)) for m in models],axis=0)
def posterior_predict(models,d,b):
    if b==0:return prior_predict(models,d['tx'])
    return np.mean([m.predict(d['sx'][:,:b],d['sy'][:,:b],d['tx']) for m in models],axis=0)
def subset(d,ind):return {k:(v[ind] if isinstance(v,np.ndarray) else [v[i] for i in ind]) for k,v in d.items()}
def fixed_reference(bank_predictions,recipient_count):
    # No recipient response or identity argument exists.
    return np.broadcast_to(bank_predictions.mean(0),(recipient_count,bank_predictions.shape[1])).copy()
def folds(people):
    ordering=sorted(range(len(people)),key=lambda i:sha(f'20261124|diagnostic_fold|{people[i]}'))
    return [ordering[::2],ordering[1::2]]
def donors(recipients,bank):
    result=[]
    for p in recipients:
        assert p not in bank;idx=[]
        for a in range(5):
            i=int(sha(f'20261124|diagnostic_donor|{a}|{p}'),16)%len(bank)
            while i in idx:i=(i+1)%len(bank)
            idx.append(i)
        result.append(idx)
    return np.array(result)

def smoke():
    old=verify_original();models=bundle(old)['profile'];d=subset(load(old,'validation'),list(range(8)))
    t=time.process_time()
    for b in BUDGETS:assert np.isfinite(posterior_predict(models,d,b)).all()
    cpu=time.process_time()-t;forecast=cpu*(102/8)*3*2
    dump(ROOT/'smoke.json',dict(process_cpu_seconds=cpu,people=8,profile_fits=0,forecast_process_cpu_seconds=forecast,method='8-person four-budget inference scaled to three102-person passes with factor2 margin',cap=14400))
    assert forecast<14400;event('smoke',cpu,shared_fits=0)

def develop():
    old=verify_original()
    if (ROOT/'development_selection.json').exists():raise RuntimeError('Development already completed')
    assert read(ROOT/'smoke.json')['forecast_process_cpu_seconds']<14400
    t=time.process_time();models=bundle(old);tr=load(old,'train');va=load(old,'validation')
    ty=labels(old,tr,'train');vy=labels(old,va,'validation')
    freq=(ty.sum(0)+.5)/(len(ty)+1)
    fold=folds(va['people']);pred={};own={};assign=[]
    for recipients in fold:
        bank=sorted(set(range(len(vy)))-set(recipients),key=lambda i:va['people'][i])
        assert not set(recipients)&set(bank)
        assign.append((recipients,bank,donors([va['people'][i] for i in recipients],[va['people'][i] for i in bank])))
    for b in BUDGETS:
        own[b]=posterior_predict(models['profile'],va,b);pred[f'own_{b}']=own[b]
        pred[f'item_frequency_{b}']=np.broadcast_to(freq,vy.shape).copy()
        pred[f'integrated_prior_{b}']=prior_predict(models['profile'],va['tx'])
        pred[f'legacy_population_{b}']=models['population'][0].predict(va['sx'][:,:b],va['sy'][:,:b],va['tx'])
        empirical=np.zeros_like(vy);single=np.zeros((5,*vy.shape))
        for recipients,bank,di in assign:
            empirical[recipients]=fixed_reference(own[b][bank],len(recipients))
            single[:,recipients,:]=own[b][np.array(bank)[di]].transpose(1,0,2)
        pred[f'empirical_reference_{b}']=empirical;pred[f'donor_single_{b}']=single;pred[f'donor_mixture_{b}']=single.mean(0)
    permutation=[]
    for shift in [1,5,11,17,23]:
        pp=np.zeros_like(vy)
        for ind in fold:pp[ind]=own[8][np.roll(ind,shift)]
        permutation.append(pp)
    pred['permutation_single_8']=np.stack(permutation)
    measures={k:metrics(vy,p) for k,p in pred.items() if p.ndim==2}
    minimum=min(measures[n+'_8']['nll'] for n in CANDIDATES)
    best=next(n for n in CANDIDATES if measures[n+'_8']['nll']<=minimum+1e-12)
    result=summarize(vy,pred,best,validation=True)
    rank=dict(source_design=int(np.linalg.matrix_rank(va['sx'][0])),target_design=int(np.linalg.matrix_rank(va['tx'][0])),bases=[])
    for m in models['profile']:
        rank['bases'].append(dict(seed=m.seed,dimension=m.dim,source_likelihood_rank=int(np.linalg.matrix_rank(va['sx'][0]@m.B)),target_design_rank=int(np.linalg.matrix_rank(va['tx'][0]@m.B)),frobenius_norm=float(np.linalg.norm(m.B)),penalty_coefficient=m.reg/(2*m.B.size)))
    rank['grid_penalty_coefficients']={str(k):.1/(2*8*k) for k in [2,4,8]}
    np.savez_compressed(LOCAL/'development_probabilities.npz',**pred)
    np.savez_compressed(LOCAL/'reference_probabilities.npz',**{f'budget_{b}':own[b] for b in BUDGETS},item_frequency=freq)
    dump(LOCAL/'development_membership.json',dict(people=va['people'],folds=fold,banks=[b for _,b,_ in assign],donor_indexes=[di.tolist() for _,_,di in assign],ids=va['ids']))
    dump(ROOT/'rank_penalty_audit.json',rank)
    dump(ROOT/'development_results.json',result)
    dump(ROOT/'development_selection.json',dict(selected=best,criterion='minimum cross-fold validation participant NLL at8; fixed candidate order ties1e-12',scores={n:measures[n+'_8']['nll'] for n in CANDIDATES},validation_people=len(vy),source_only_bank_per_fold=51,
        artifacts={f:sha((LOCAL/f).read_bytes()) for f in ['development_probabilities.npz','reference_probabilities.npz','development_membership.json']}))
    event('development',time.process_time()-t,shared_fits=0,closed_form_item_frequency_estimates=10,validation_people=102)

def summarize(y,pred,best,validation=False):
    out={'status':'development diagnostic' if validation else 'single post hoc reuse of exposed original test; not confirmation','people':len(y),'target_choices':y.size,'target_families':1,'metrics':{},'contrasts':{}}
    for name,p in pred.items():
        if p.ndim==2:out['metrics'][name]=metrics(y,p)
    for b in BUDGETS:
        ownloss=nll(y,pred[f'own_{b}']);singleloss=np.mean([nll(y,p) for p in pred[f'donor_single_{b}']],0);mixloss=nll(y,pred[f'donor_mixture_{b}'])
        # Saved zero-budget donors belong to the legacy fallback, not prior.
        donor_own=nll(y,pred['historical_own_0']) if b==0 and not validation else ownloss
        out['contrasts'][f'value_{b}']=ci(nll(y,pred[f'{best}_{b}'])-ownloss)
        out['contrasts'][f'identity_{b}']=ci(singleloss-donor_own)
        out['contrasts'][f'mixture_{b}']=ci(mixloss-donor_own)
        out['contrasts'][f'jensen_gap_{b}']=ci(singleloss-mixloss)
        assert np.all(singleloss>=mixloss-1e-12)
        for n in CANDIDATES:out['contrasts'][f'{n}_minus_own_{b}']=ci(nll(y,pred[f'{n}_{b}'])-ownloss)
    if validation:
        perm_loss=np.mean([nll(y,p) for p in pred['permutation_single_8']],0)
        out['contrasts']['inference_permutation_minus_own_8']=ci(perm_loss-nll(y,pred['own_8']))
        out['interval_qualification']='descriptive conditional bootstrap; cross-fold bank/recipient dependencies not modeled; no confirmation coverage claim'
    else:out['interval_qualification']='paired participant bootstrap conditional on fixed disjoint development bank, fitted models, one schedule family; exploratory test reuse'
    return out

def lock():
    verify_original();review=read(ROOT/'diagnostic_review_signoff.json');assert review['approved']
    for f,h in review['reviewed_files'].items():assert sha((ROOT/f).read_bytes())==h,f
    assert not (LOCAL/'exploratory_test_probabilities.npz').exists()
    files=['DIAGNOSTIC_PROTOCOL.md','contrast_definitions.json','diagnostics.py','test_diagnostics.py','development_selection.json','rank_penalty_audit.json','diagnostic_review_signoff.json']
    dump(ROOT/'diagnostic_lock.json',dict(status='locked_before_exploratory_test_pass',files={f:sha((ROOT/f).read_bytes()) for f in files}))
def check_lock():
    verify_original()
    for f,h in read(ROOT/'diagnostic_lock.json')['files'].items():assert sha((ROOT/f).read_bytes())==h,f
    for f,h in read(ROOT/'development_selection.json')['artifacts'].items():assert sha((LOCAL/f).read_bytes())==h,f

def predict_exposed():
    check_lock();old=original();t=time.process_time()
    if (LOCAL/'exploratory_test_probabilities.npz').exists():raise RuntimeError('Exploratory prediction pass already saved')
    te=load(old,'test');va=load(old,'validation');assert not set(te['people'])&set(va['people'])
    saved=np.load(old/'local_data/test_predictions.npz');ref=np.load(LOCAL/'reference_probabilities.npz');models=bundle(old)
    membership=read(old/'local_data/prediction_membership.json');assert membership==dict(people=te['people'],decision_ids=te['ids'])
    assignments=list(rows(old/'local_data/donor_assignments.jsonl'))
    assert [a['person'] for a in assignments]==te['people']
    for a in assignments:
        assert len(a['donors'])==len(set(a['donors']))==5
        assert set(a['donors'])<=set(va['people']) and a['person'] not in a['donors']
    pred={}
    for b in BUDGETS:
        assert saved[f'donor_assignments_{b}'].shape==(5,102,10)
        assert saved[f'profile_seeds_{b}'].shape==(3,102,10)
        assert np.allclose(saved[f'profile_{b}'],saved[f'profile_seeds_{b}'].mean(0))
        pred[f'own_{b}']=prior_predict(models['profile'],te['tx']) if b==0 else saved[f'profile_{b}']
        pred[f'integrated_prior_{b}']=prior_predict(models['profile'],te['tx'])
        pred[f'item_frequency_{b}']=np.broadcast_to(ref['item_frequency'],te['tx'].shape[:2]).copy()
        pred[f'empirical_reference_{b}']=fixed_reference(ref[f'budget_{b}'],len(te['people']))
        pred[f'legacy_population_{b}']=saved[f'population_{b}'];pred[f'historical_summary_{b}']=saved[f'summary_{b}']
        pred[f'donor_single_{b}']=saved[f'donor_assignments_{b}'];pred[f'donor_mixture_{b}']=saved[f'donor_{b}']
        assert np.allclose(pred[f'donor_mixture_{b}'],pred[f'donor_single_{b}'].mean(0))
        for name in CANDIDATES:assert np.allclose(pred[f'{name}_{b}'],pred[f'{name}_{b}'][0])
    pred['historical_own_0']=saved['profile_0']
    np.savez_compressed(LOCAL/'exploratory_test_probabilities.npz',**pred)
    dump(LOCAL/'exploratory_membership.json',dict(people=te['people'],ids=te['ids']))
    dump(ROOT/'probability_manifest.json',dict(status='saved_before_exposed_label_join; exploratory not new confirmation',files={f:sha((LOCAL/f).read_bytes()) for f in ['exploratory_test_probabilities.npz','exploratory_membership.json']}))
    event('exploratory_predictions',time.process_time()-t,test_labels_loaded=False,shared_fits=0)

def score_exposed():
    check_lock();t=time.process_time()
    if (ROOT/'exploratory_results.json').exists():raise RuntimeError('Declared exploratory pass already scored')
    attempt=ROOT/'exploratory_score_attempt.json'
    if attempt.exists():raise RuntimeError('Prior scoring attempt exists; preserve it and document any correction separately')
    for f,h in read(ROOT/'probability_manifest.json')['files'].items():assert sha((LOCAL/f).read_bytes())==h
    dump(attempt,dict(status='started_before_exposed_label_join',attempt=1,new_confirmation=False))
    try:
        old=original();d=read(LOCAL/'exploratory_membership.json');y=labels(old,d,'test',True)
        pred=dict(np.load(LOCAL/'exploratory_test_probabilities.npz'));best=read(ROOT/'development_selection.json')['selected']
        result=summarize(y,pred,best)
        result['selected_source_blind']=best;result['original_verdict_preserved']='inconclusive';result['exploratory_pass_count']=1
        dump(ROOT/'exploratory_results.json',result)
        dump(attempt,dict(status='completed',attempt=1,new_confirmation=False))
        event('single_exploratory_score',time.process_time()-t,people=102,new_confirmation=False)
    except Exception as exc:
        dump(attempt,dict(status='failed_after_attempt_started',attempt=1,error=repr(exc),new_confirmation=False))
        event('failed_exploratory_score',time.process_time()-t,error=repr(exc))
        raise

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['inventory','smoke','develop','lock','predict','score']);p.add_argument('--original',type=Path,default=ORIGINAL_DEFAULT);a=p.parse_args()
    if a.stage=='inventory':inventory(a.original)
    else:{'smoke':smoke,'develop':develop,'lock':lock,'predict':predict_exposed,'score':score_exposed}[a.stage]()
