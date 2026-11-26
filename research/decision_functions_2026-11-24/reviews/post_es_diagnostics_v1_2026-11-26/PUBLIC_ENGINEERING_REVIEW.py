"""Independent public receipt/engineering-trajectory review. No optimizer calls."""
import json, math, hashlib, argparse
from pathlib import Path
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('repo_root',type=Path)
parser.add_argument('output',type=Path)
args=parser.parse_args()
ROOT=args.repo_root.resolve()
RUN=ROOT/'research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1'
OUT=args.output.resolve()
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[];failures=[];worst={}
def require(key,passed,detail=None):
    checks.append(key)
    if not bool(passed): failures.append({'id':key,'detail':detail})
def close(key,a,b,tol=1e-11):
    a=np.asarray(a);b=np.asarray(b)
    if a.shape!=b.shape: require(key,False,'shape mismatch');return
    delta=float(np.max(np.abs(a.astype(float)-b.astype(float)),initial=0))
    require(key,np.isfinite(delta) and delta<=tol,delta)
    family=key.split('/')[0];worst[family]=max(worst.get(family,0),delta)

e=read(RUN/'EXPECTED.json')
fixture={k:np.array(v) for k,v in read(RUN/'FIXTURE.json').items()}
v=np.array([[[1,0],[0,1]],[[-1,1],[1,0]],[[0,-1],[-1,-1]]],float)
close('fixture/V',fixture['V'],v,0)
for person in range(48):
    block,motif=divmod(person,8)
    y=np.array([((i+block)%3 if motif in (0,1,2,5) else ((i%2+block)%3 if motif==3 else ([0,1,1,2][i%4] if motif==4 else block%3))) for i in range(16)])
    close(f'fixture/{person}/y',fixture[f'{person}_y'],y,0)
    for part,n in [('support',16),('query',12)]:
        z=[];g=[]
        for i in range(n):
            t=(2*i-(n-1))/n
            cardinal=[(1,0),(0,1),(-1,0),(0,-1)][i%4]
            zz=cardinal if motif in (1,5) else ((1,0) if motif==2 else (((-1)**i,0) if motif==3 else ((8*cardinal[0],8*cardinal[1]) if motif==4 else ((t,0) if motif==7 else (0,0)))))
            cc=np.array([1,-1,0],float)*((2*block-5)/16)
            gg=cc+[0,1/8,1/8,0,0,12,0,0][motif]*t*np.array([1,-2,1])
            if motif==0:gg=np.log(np.bincount(y,minlength=3)/16)+(2*block-5)/16
            z.append(zz);g.append(gg)
        close(f'fixture/{person}/{part}/z',fixture[f'{person}_{part}_z'],z)
        close(f'fixture/{person}/{part}/g',fixture[f'{person}_{part}_g'],g)

def inputs(person,model,part):
    z=fixture[f'{person}_{part}_z'];g=fixture[f'{person}_{part}_g']
    rows=[]
    for zz in z:
        f=np.array([v[c]@zz for c in range(3)])
        rows.append(np.eye(3) if model=='B3' else np.column_stack((np.eye(3),f)))
    a=np.array(rows);d=np.array([.6]*3+([] if model=='B3' else [.06]*2))
    return a,g,d
def evaluate(theta,a,g,y,d):
    values=[];gradient=np.zeros(len(theta));hessian=np.diag(d).copy();ps=[]
    for ai,gi,yi in zip(a,g,y):
        logits=np.array([float(gi[c]+np.dot(ai[c],theta)) for c in range(3)])
        top=float(max(logits));weights=np.exp(logits-top);p=weights/math.fsum(weights);ps.append(p)
        values.append(top+math.log(math.fsum(weights))-logits[int(yi)])
        gradient+=sum(((p[c]-(c==yi))*ai[c] for c in range(3)),np.zeros(len(theta)))/len(y)
        hessian+=ai.T@(np.diag(p)-np.outer(p,p))@ai/len(y)
    gradient+=d*theta
    value=math.fsum(values)/len(y)+sum(d*theta*theta)/2
    return float(value),gradient,hessian
def predict(theta,a,g):
    out=[]
    for ai,gi in zip(a,g):
        logits=gi+ai@theta;w=np.exp(logits-max(logits));out.append(w/math.fsum(w))
    return np.array(out)

starts={p.name.removesuffix('.start.json'):read(p) for p in (RUN/'attempts').glob('*.start.json')}
records={p.name.removesuffix('.complete.json'):read(p) for p in (RUN/'attempts').glob('*.complete.json')}
require('inventory/attempt_starts',set(starts)==set(e['attempts']))
require('inventory/attempt_completions',set(records)==set(e['attempts']))
require('inventory/no_attempt_failures',not list((RUN/'attempts').glob('*.failure.json')))
final={};traces=0;transitions=0;guarded=0;max_r=0.;max_kr=0.;max_steps=0
fixture_hash=sha(RUN/'FIXTURE.json');solver_hash=sha(ROOT/'labs/decision_functions_post_es_diagnostics_v1/solver.py')
for key,spec in e['attempts'].items():
    if key not in records or key not in starts:continue
    row=records[key];start=starts[key]
    require('inventory/spec/'+key,row['spec']==start['spec']==spec)
    require('inventory/bindings/'+key,start['fixture_hash']==fixture_hash and start['source_hash']==solver_hash)
    person=spec['person'];model=spec['model'];layout=spec['layout']
    a,g,d=inputs(person,model,'support');q,qg,_=inputs(person,model,'query');y=fixture[f'{person}_y'].astype(int)
    trace=row['trace'];close('trace_initial/'+key,trace[0]['theta'],np.zeros(len(d)),0)
    require('inventory/iterations/'+key,row['steps']==len(trace)-1 and row['steps']<=100)
    for index,t in enumerate(trace):
        theta=np.array(t['theta']);value,gradient,hessian=evaluate(theta,a,g,y,d);r=float(np.linalg.norm(gradient/np.sqrt(d)))
        close('trace_value/'+key+f'/{index}',value,t['objective'])
        close('trace_residual/'+key+f'/{index}',r,t['R'])
        traces+=1
        if index+1<len(trace):
            he=hessian/np.sqrt(d)[:,None]/np.sqrt(d)[None,:];ge=gradient/np.sqrt(d)
            direction=np.linalg.solve(he,-ge)
            alpha=t['alpha'];require('trajectory/alpha/'+key+f'/{index}',alpha in [2.**-j for j in range(40)])
            predicted=theta+alpha*direction/np.sqrt(d)
            close('trajectory_next/'+key+f'/{index}',predicted,trace[index+1]['theta'],1e-10)
            require('trajectory/rule/'+key+f'/{index}',t['acceptance_rule'] in ('ARMIJO','ROUNDOFF_FULL_STEP'))
            if t['acceptance_rule']=='ARMIJO':
                rhs=value+1e-4*alpha*float(ge@direction)
                require('trajectory/armijo/'+key+f'/{index}',trace[index+1]['objective']<=rhs+1e-12)
            else:
                require('trajectory/guard_full_step/'+key+f'/{index}',alpha==1.)
            transitions+=1
    theta=np.array(trace[-1]['theta']);_,grad,_=evaluate(theta,a,g,y,d);rr=float(np.linalg.norm(grad/np.sqrt(d)))
    projector=np.eye(3)-np.ones((3,3))/3;k=np.array([np.linalg.norm(projector@aq/np.sqrt(d),2) for aq in q]);kr=float(k.max()*rr)
    close('final_residual/'+key,rr,row['R_recomputed'])
    close('final_KR/'+key,kr,row['KR'])
    require('final/criteria/'+key,row['success'] and row['engineering_pass'] and rr<=1e-10 and kr<=1e-8)
    for t in row['guarded']:
        allowance=64*2.**-52*max(1,abs(t['J_old']))
        close('guard/allowance/'+key,t['allowance'],allowance,0)
        require('guard/conditions/'+key,0<t['predicted_decrease']<=allowance and t['R_new']<t['R_old'] and t['J_new']<=t['J_old']+allowance)
    require('guard/count/'+key,len(row['guarded'])==sum(t.get('acceptance_rule')=='ROUNDOFF_FULL_STEP' for t in trace))
    guarded+=len(row['guarded']);max_r=max(max_r,rr);max_kr=max(max_kr,kr);max_steps=max(max_steps,row['steps'])
    final[(layout,model,person)]=(theta,predict(theta,q,qg))
for person in range(48):
    for model in ('B3','M1'):
        base=final.get(('singletons',model,person))
        if base is None:continue
        for layout in ('chunks7','all48','reverse48'):
            candidate=final.get((layout,model,person))
            require('layout/'+layout+'/'+model+f'/{person}',candidate is not None and np.array_equal(base[0],candidate[0]) and np.array_equal(base[1],candidate[1]))

wrappers=e['wrappers'];ws=list((RUN/'wrappers').glob('*.start.json'));wc=list((RUN/'wrappers').glob('*.complete.json'))
require('inventory/wrapper_starts',{p.name.removesuffix('.start.json') for p in ws}=={w['id'] for w in wrappers})
require('inventory/wrapper_completions',{p.name.removesuffix('.complete.json') for p in wc}=={w['id'] for w in wrappers})
for w in wrappers:
    p=RUN/'wrappers'/(w['id']+'.complete.json')
    if p.exists():require('inventory/wrapper/'+w['id'],read(p)==dict(**w,attempts=[w['id']+f'_p{p}' for p in w['people']]))
verification=read(RUN/'VERIFICATION.json')
require('verification/ids',set(verification['checks'])==set(e['comparison_ids']) and len(verification['checks'])==395)
require('verification/zeros',all(v==0 for v in verification['checks'].values()))
require('verification/qualification_false',verification['scientific_qualification'] is False)
bindings=read(RUN/'INPUT_BINDINGS.json');input_receipt=read(RUN/'INPUT_HASH_RECEIPT.json')
require('private_bindings',bindings['private_files']==input_receipt['before']==input_receipt['after'])
resources=read(RUN/'RESOURCE_USAGE_FINAL.json');commands=[read(RUN/p) for p in resources['command_receipts']]
close('resources/cpu',sum(c['cpu_seconds_sampled'] for c in commands),resources['cpu_seconds_sampled'],0)
close('resources/wall',sum(c['wall_seconds'] for c in commands),resources['wall_seconds_profiled'],1e-10)
close('resources/rss',max(c['peak_rss_bytes_sampled'] for c in commands),resources['peak_rss_bytes_sampled'],0)
require('resources/commands',len(commands)==6 and sum(c['exit_code']!=0 for c in commands)==1)
manifest=read(RUN/'DELIVERY_MANIFEST.json');missing=[];bad_hashes=[]
for p,h in manifest['files'].items():
    path=ROOT/p
    if not path.exists():missing.append(p)
    elif sha(path)!=h:bad_hashes.append(p)
require('delivery_hashes/no_mismatch',not bad_hashes,bad_hashes)
require('delivery_hashes/no_missing',not missing,missing)
receipt=dict(status='PASS' if not failures else 'INCOMPLETE_OR_FAIL',checks=len(checks),failures=failures,worst_differences=worst,
 engineering_attempts=len(records),wrapper_calls=len(wc),trace_points=traces,transitions_replayed=transitions,guarded_acceptances=guarded,
 maximum_independent_R=max_r,maximum_independent_KR=max_kr,maximum_steps=max_steps,
 delivery_manifest_files=len(manifest['files']),delivery_missing=missing,delivery_hash_mismatch=bad_hashes,
 public_private_hash_bindings=len(bindings['private_files']),resources=resources,
 limitations='No original or derived private archive bytes available. Public engineering parameter traces and mathematical values/updates replayed independently; no optimizer, new scientific fixture or new model fit invoked. Guarded/Armijo checks include stated numeric comparison allowance.',
 optimizer_calls=0)
OUT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('resources','failures','worst_differences')},indent=2))
print(json.dumps({'failures':failures[:10],'worst_differences':worst},indent=2))
