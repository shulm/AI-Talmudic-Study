"""Post-execution read-only delivery reconciliation; no scientific recomputation.

This supplements the frozen verifier's exact-ID checks with explicit receipt-field
bindings. It does not change a prediction, metric, tolerance, gate or source freeze.
The supplement is added after exposure and is not a new confirmatory analysis.
"""
import sys
import math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'labs/decision_functions_uncapped_single_history_confirmation_v1'))
from common import *

def audit(out,private):
    frozen(out);v=read(out/'VERIFICATION.json');require(v['integrity']=='PASS','Frozen verification required')
    pub=read(out/'PUBLICATION.json');seeds={x['id']:x for x in read(out/'SEEDS.json')['worlds']};checks={};models={};counts=dict(shared=0,personal=0,wrappers=0,probability_arrays=0,log_arrays=0);max_r=0.;max_ru=0.;guarded=0
    for world in WORLDS:
        wr=out/'worlds'/world;pr=private/world;sealed=read(wr/'PREDICTIONS_SEALED.json');complete=read(wr/'COMPLETE.json');inp=read(wr/'INPUTS.json')
        close(complete['files'],sealed['files']);close(inp['seeds'],seeds[world]);require(inp['source_freeze']==sha(out/'FREEZE.json'),'World source binding')
        exact([p.name for p in pr.iterdir()],sealed['files']);require(not sealed['evaluator_loaded_for_scoring'],'Evaluator boundary marker')
        require(sealed['time']<=complete['time'],'Seal chronology')
        for n,h in inp['hashes'].items():require(h==sealed['files'][n+'.npz']==sha(pr/(n+'.npz')),'Input hash binding')
        model_hash=sha(pr/'models.npz');models[world]=model_hash;s=load(pr/'support.npz');traces={x['id']:x for x in records(pr/'traces.jsonl')}
        rows=inventory(wr/'attempts.jsonl',ids(world));starts={x['id']:x for x in rows if x['event']=='start'};ends={x['id']:x for x in rows if x['event']=='complete'}
        for key,start in starts.items():
            require(start['source']==pub['commit'],'Attempt source binding');close(start['inputs'],inp['hashes']);end=ends[key];trace=traces[key];require(end['success'],'Failed actual attempt')
            if start['kind']=='shared':
                seed=int(key.rsplit('/',1)[1]);require(start['seed']==seed and seed in SEEDS,'Shared seed');close(start['rho'],.01);close(start['lambda_b'],.1);close(start['dimensions'],[96,120,3,2]);require(end['finite'],'Nonfinite shared')
                for k in ('success','finite','objective','iterations','message','gradient_max','person_scaled_gradient_max','parameter_norm','cpu_seconds','wall_seconds'):close(end[k],trace[k])
                counts['shared']+=1
            else:
                _,history,head,person=key.split('/');d=np.array([.6]*3+([] if head=='B3' else [.06]*2));close(start['penalty'],d);close(start['support_ids'],s[history+'_ids']);close(start['dimensions'],[16,3,len(d)])
                require(start['initialization']=='zero' and start['model_hash']==model_hash,'Personal model/initialization')
                close(trace['optimizer']['trace'][0]['theta'],np.zeros(len(d)),0);close(end['R'],trace['bounds']['R'],0);close(end['R_used'],trace['bounds']['R_used'],0)
                close(end['steps'],trace['optimizer']['steps'],0);close(end['guarded_count'],len(trace['optimizer']['guarded']),0);close(end['gradient_comparison'],trace['bounds']['gradient_comparison'],0)
                max_r=max(max_r,end['R']);max_ru=max(max_ru,end['R_used']);guarded+=end['guarded_count'];counts['personal']+=1
            checks[key]=True
        wrapper=inventory(wr/'wrappers.jsonl',[f'{world}/{h}/{head}' for h in HIST for head in HEADS]);require(all(x.get('expected_people',x.get('people'))==48 for x in wrapper),'Wrapper person count');counts['wrappers']+=8
        p=load(pr/'predictions.npz');lp=load(pr/'log_predictions.npz');exact(p,prediction_keys());exact(lp,log_keys());counts['probability_arrays']+=len(p);counts['log_arrays']+=len(lp)
        checks[world+'/public_private_bindings']=True
        require(all(sha(pr/name)==h for name,h in sealed['files'].items()),'Consumed artifact changed')
    close(counts,dict(shared=246,personal=31488,wrappers=656,probability_arrays=2788,log_arrays=328),0)
    statuses=[read(out/'worlds'/w/'SCORES.json')['gates']['H1']['joint'] for w in WORLDS];successes=statuses.count('PASS')
    exact_tail=sum((Fraction(math.comb(82,k)*4**k,5**82) for k in range(successes,83)),Fraction(0))
    lo,hi=0.,1.
    if successes:
        for _ in range(80):
            mid=(lo+hi)/2;tail=math.fsum(math.comb(82,k)*mid**k*(1-mid)**(82-k) for k in range(successes,83))
            if tail<.05:lo=mid
            else:hi=mid
        lower=(lo+hi)/2
    else:lower=0.
    close(float(exact_tail),v['inference']['p_exact'],1e-12);close(lower,v['inference']['one_sided_95_lower'],1e-12);close(successes,v['inference']['successes'],0)
    stats=dict(successes=successes,n=82,p_exact_numerator=str(exact_tail.numerator),p_exact_denominator=str(exact_tail.denominator),p_exact=float(exact_tail),one_sided_lower_by_tail_inversion=lower,comparison_absolute_tolerance=1e-12)
    checks['independent_binomial_inference']=True
    atomic(out/'DELIVERY_AUDIT.json',dict(status='PASS',designation='POST_EXECUTION_READ_ONLY_RECONCILIATION',changes_scientific_results=False,counts=counts,check_count=len(checks),checks=checks,independent_statistics=stats,model_archive_sha256=models,max_personal_R=max_r,max_personal_R_used=max_ru,guarded_full_steps=guarded,source_sha256=sha(Path(__file__)),frozen_verification_sha256=sha(out/'VERIFICATION.json')))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,required=True);p.add_argument('--private-root',type=Path,required=True);a=p.parse_args();audit(a.output_root,a.private_root)
