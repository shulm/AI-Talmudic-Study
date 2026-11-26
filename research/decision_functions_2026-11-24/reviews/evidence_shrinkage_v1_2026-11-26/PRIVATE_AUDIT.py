"""Saved-evidence supplement: no optimizer, generator, new policy, or input writes.

Run from repository root; outputs must be a new directory. Original verifier's
pure forward/record helpers are reused, never its generate-calling verify().
"""
import argparse, hashlib, json, os, subprocess, sys, time
from pathlib import Path
os.environ.update(OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1', OMP_NUM_THREADS='1')
sys.dont_write_bytecode = True
import numpy as np
from scipy.special import logsumexp
import scipy.optimize
import psutil

PIN = 'f18255c5fad37f704881ff1f9ad50cd113497236'
ROOT = Path(__file__).resolve().parents[4]
RUN = ROOT/'research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1'
sys.path.insert(0, str(ROOT/'labs/decision_functions_evidence_shrinkage_v1'))
import verify as old
import contracts as ct
import fixture

def forbidden(*a, **k):
    raise RuntimeError('Optimization and world generation forbidden in this audit')
scipy.optimize.minimize = forbidden
fixture.generate = forbidden

def read(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(p): return {x.relative_to(p).as_posix():sha(x) for x in p.rglob('*') if x.is_file()}
def write(p, data):
    with p.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, indent=2, sort_keys=True, allow_nan=False); f.write('\n')
def loss(p,o): return -(o*np.log(np.maximum(p,1e-12))).sum(-1)
def contrast(p):
    lp=np.log(np.maximum(p,1e-12))
    ratios=np.stack([lp[:,:,a]-lp[:,:,b] for a,b in ((0,1),(0,2),(1,2))],-1)
    pair=ratios[::2]-ratios[1::2]
    return pair-pair[:,:1]

def personal(x,z,g,y,v,rho,lb):
    n=len(y); x=x.reshape(n,3 if v is None else 5)
    A=np.broadcast_to(np.eye(3),(len(z),3,3)).copy()
    if v is not None: A=np.concatenate([A,np.einsum('crd,nd->ncr',v,z)],-1)
    logits=g[None]+np.einsum('ncd,sd->snc',A,x)
    p=np.exp(logits-logsumexp(logits,axis=-1,keepdims=True))
    penalty=np.r_[np.full(3,lb), np.full(x.shape[1]-3,rho)]
    residual=np.einsum('snc,ncd->sd',p-np.eye(3)[y],A)/len(z)+x*penalty
    obj=float((logsumexp(logits,-1)-np.take_along_axis(logits,y[...,None],-1)[...,0]).mean()+np.sum(x*x*penalty)/(2*n))
    return obj,residual,A

def main(private,dest):
    start=time.process_time(); wall=time.monotonic(); samples=[]
    dest=dest.resolve()
    if dest.exists(): raise FileExistsError(dest)
    # Only additive output under this review; never an input or historical path.
    if not dest.is_relative_to(Path(__file__).resolve().parent): raise ValueError('Output must be under review directory')
    dest.mkdir()
    checks={}; failures=[]; missing=[]; stats=[]; pairs=[]; bounds=[]; weights=[]; details=[]
    def check(k,a,b,tol=1e-12):
        try:
            delta=old.difference(a,b)
            checks[k]={'max_abs':delta,'tolerance':tol,'passed':delta<=tol}
            if delta>tol: failures.append(k)
        except Exception as e:
            checks[k]={'passed':False,'error':str(e)}; failures.append(k)
    tracked=subprocess.check_output(['git','ls-tree','-rz','--name-only',PIN],cwd=ROOT).decode('utf-8').strip('\0').split('\0')
    public_before={p:sha(ROOT/p) for p in tracked}
    # Git-normalized content comparison allows Windows checkout newlines.
    tree=subprocess.check_output(['git','ls-tree','-rz',PIN],cwd=ROOT).decode('utf-8').strip('\0').split('\0')
    expected_blobs={row.split('\t',1)[1]:row.split()[2] for row in tree}
    actual_blobs=subprocess.run(['git','hash-object','--stdin-paths'],input='\n'.join(tracked)+'\n',cwd=ROOT,text=True,encoding='utf-8',capture_output=True,check=True).stdout.splitlines()
    for p,actual in zip(tracked,actual_blobs):
        expected=expected_blobs[p]
        if actual!=expected: failures.append('pinned_blob/'+p)
    private_before=inventory(private) if private.exists() else {}
    inputs={'public_sha256':public_before,'private_sha256':private_before,'base_commit':PIN,'script_sha256':sha(Path(__file__))}
    for r in 'EFGH':
        samples.append(psutil.Process().memory_info().rss)
        root=private/r; manifest=read(RUN/(r+'_manifest.json'))
        if not root.exists(): missing.append(r+'/private_cache'); continue
        check(r+'/manifest',inventory(root),manifest['private_files'])
        if r+'/manifest' in failures: continue
        arrays={role:old.load(root/(role+'.npz')) for role in ct.ROLES}
        l,s,ev,models,pred=[arrays[k] for k in ('learner','support','evaluator','models','predictions')]
        f=arrays['fixture']; ids=ev['person_ids']; q=ev['query_ids']
        check(r+'/people',ids,np.arange(144,192)); check(r+'/query_ids',q,l['query_ids'])
        for name in ('z','base'): check(r+'/query_'+name,l['query_'+name],f[name][q])
        check(r+'/oracle',ev['oracle'],f['oracle'][ids][:,q])
        check(r+'/active',ev['active'],f['active'][ids])
        for h in ct.HIST:
            ix=s[f'{h}_ids']
            for name in ('z','base'): check(f'{r}/{h}/{name}',s[f'{h}_{name}'],f[name][ix])
            check(f'{r}/{h}/labels',s[f'{h}_y'],f['y'][ids][:,ix])
            check(f'{r}/{h}/schedule',ix,read(RUN/(r+'_schedules.json'))[str(h)]['ids'])
        fw=old.forward(r,arrays,root)
        for role in fw:
            for k,v in fw[role].items(): check(r+'/forward/'+role+'/'+k,v,arrays[role][k],1e-10 if role=='evidence' else 1e-12)
        residuals={}; logbounds={}; params={}
        for stage in ct.STAGES:
            for key,meta in ct.expected(r,stage).items():
                rec=read(RUN/'records'/f'{r}_{stage}'/(key+'.complete.json'))
                x=np.load(root/'parameters'/(key+'.npy'),allow_pickle=False)
                vals=old.record_values(meta,x,l,s,models)
                check(key+'/record',vals,{k:rec[k] for k in vals})
                if stage=='shared': continue
                h,n,m=meta['history'],meta['people'],meta['model']
                v=None if m=='B3' else models[str(meta['seed'])+'_V']
                obj,res,A=personal(x,s[f'{h}_z'],s[f'{h}_base'],s[f'{h}_y'][:n],v,meta['rho'],meta['lambda_b'])
                check(key+'/objective',obj,rec['objective'])
                check(key+'/gradient',float(abs(res).max()/n),rec['gradient_max'])
                mu=meta['lambda_b'] if v is None else min(meta['rho'],meta['lambda_b'])
                radius=np.linalg.norm(res,axis=1)/mu
                AQ=np.broadcast_to(np.eye(3),(len(q),3,3)).copy()
                if v is not None: AQ=np.concatenate([AQ,np.einsum('crd,nd->ncr',v,l['query_z'])],-1)
                # Each log p_c has gradient A_c - sum_d p_d A_d.
                L=np.linalg.norm(AQ[:,:,None,:]-AQ[:,None,:,:],axis=-1).max((1,2))
                eps=radius[:,None]*L[None,:]
                residuals[h,m,n]=res; params[h,m,n]=x.reshape(n,-1)
                if n==48: logbounds[h,m]=eps
                stats.append(dict(record=key,batch=n,history=h,model=m,message=rec['message'],iterations=rec['iterations'],gradient_max=rec['gradient_max'],person_scaled_gradient_max=float(abs(res).max()),first_person_residual_l2=float(np.linalg.norm(res[0])),first_person_parameter_radius=float(radius[0]),max_parameter_radius=float(radius.max()),max_query_log_probability_bound=float(eps.max()),mu=mu))
        for n in (1,7):
            for m in ct.HEADS+('M1','FIXED_MIX','ES'):
                a=arrays['numerical'][f'{n}_{m}']; b=pred['101_'+m][:1]
                delta=abs(a-b); at=np.unravel_index(np.argmax(delta),delta.shape)
                row=dict(world=r,batch=n,model=m,max_probability_difference=float(delta[at]),expected_nll_difference=float(abs(loss(a,ev['oracle'][:1]).mean()-loss(b,ev['oracle'][:1]).mean())),coordinate={'person_index':int(at[0]),'query_index':int(at[1]),'class_index':int(at[2])})
                saved=read(RUN/(r+'_numerical.json'))['comparisons'][f'{n}_{m}']
                check(f'{r}/numerical/{n}/{m}',[row['max_probability_difference'],row['expected_nll_difference']],[saved['probability_max'],saved['expected_nll_difference']])
                if m in ct.HEADS:
                    mu=.6 if m=='B3' else .06
                    row.update(parameter_difference_l2=float(np.linalg.norm(params[101,m,n][0]-params[101,m,48][0])),parameter_difference_bound=float((np.linalg.norm(residuals[101,m,n][0])+np.linalg.norm(residuals[101,m,48][0]))/mu))
                    check(f'{r}/parameter_bound/{n}/{m}',max(0,row['parameter_difference_l2']-row['parameter_difference_bound']),0)
                details.append(row)
        public=read(RUN/(r+'_scores.json'))
        for h in ct.HIST:
            logbounds[h,'M1']=np.maximum.reduce([logbounds[h,'M1_'+str(seed)] for seed in ct.SEEDS])
            for m in ('FIXED_MIX','ES'): logbounds[h,m]=np.maximum(logbounds[h,'B3'],logbounds[h,'M1'])
            w=arrays['evidence'][f'{h}_w']; hh=arrays['evidence'][f'{h}_h']
            for activity in (True,False):
                ix=ev['active']==activity; label='active' if activity else 'inactive'
                ww=w[ix]
                wr=dict(world=r,history=h,stratum=label,count=int(ix.sum()),zero_count=int((ww==0).sum()),cap_count=int((hh[ix]==np.log(10)).sum()),mean=float(ww.mean()),min=float(ww.min()),max=float(ww.max()),median=float(np.median(ww)),q10=float(np.quantile(ww,.1)),q90=float(np.quantile(ww,.9)))
                weights.append(wr)
                recorded=read(RUN/(r+'_evidence.json'))['summaries'][f'{h}_{label}']
                check(f'{r}/{h}/{label}/weights',{k:wr[k] for k in ('min','max','mean','median','q10','q90')},recorded['weight'])
                check(f'{r}/{h}/{label}/counts',[wr['zero_count']/wr['count'],wr['cap_count']/wr['count']],[recorded['fraction_zero'],recorded['fraction_cap']])
                truth=contrast(ev['oracle'][ix]); den=float(np.mean(truth**2))
                base_loss=loss(pred[f'{h}_B3'][ix],ev['oracle'][ix]).mean()
                for m in ('B3','M1','FIXED_MIX','ES'):
                    pp=pred[f'{h}_{m}'][ix]; err=contrast(pp)-truth
                    row=dict(world=r,history=h,stratum=label,method=m,gain=float(base_loss-loss(pp,ev['oracle'][ix]).mean()),contrast_mse=float(np.mean(err**2)),contrast_den=den,gap=float(base_loss-loss(ev['oracle'][ix],ev['oracle'][ix]).mean()))
                    saved=next(x for x in public['rows'] if x['id']==f'{h}_{label}_{m}')
                    check(f'{r}/{h}/{label}/{m}/metrics',{k:row[k] for k in ('gain','contrast_mse','contrast_den','gap')},{k:saved[k] for k in ('gain','contrast_mse','contrast_den','gap')})
                    bounds.append(row)
                    if activity:
                        eps=logbounds[h,m][ix]
                        # A contrast contains two log odds at query and anchor.
                        pair=2*(eps[::2]+eps[1::2]); cb=pair+pair[:,:1]
                        rad=float(np.sqrt(np.mean(cb**2)/den)); observed=float(np.sqrt(row['contrast_mse']/den))
                        row.update(contrast_nrmse=observed,numerical_nrmse_radius=rad,nrmse_lower=max(0,observed-rad),nrmse_upper=observed+rad)
                for src,dst in (('M1','FIXED_MIX'),('FIXED_MIX','ES')):
                    a=contrast(pred[f'{h}_{src}'][ix]); b=contrast(pred[f'{h}_{dst}'][ix]); d=b-a
                    square=float(np.mean(d*d)); cross=float(2*np.mean((a-truth)*d)); change=float(np.mean((b-truth)**2)-np.mean((a-truth)**2))
                    check(f'{r}/{h}/{label}/{src}_to_{dst}/identity',change,square+cross)
                    pairs.append(dict(world=r,history=h,stratum=label,source=src,target=dst,contrast_mse_change=change,prediction_change_square=square,error_cross_term=cross,expected_nll_change=float((loss(pred[f'{h}_{dst}'][ix],ev['oracle'][ix])-loss(pred[f'{h}_{src}'][ix],ev['oracle'][ix])).mean())))
        samples.append(psutil.Process().memory_info().rss)
    aggregates=[]
    for r in 'EFGH':
        for m in ('B3','M1','FIXED_MIX','ES'):
            aa=[x for x in bounds if x['world']==r and x['method']==m and x['stratum']=='active']
            ii=[x for x in bounds if x['world']==r and x['method']==m and x['stratum']=='inactive']
            if len(aa)!=2 or len(ii)!=2: continue
            mean=lambda k:float(np.mean([x[k] for x in aa]))
            row=dict(world=r,method=m,active_gain=mean('gain'),recovery=mean('gain')/mean('gap'),contrast_nrmse=float(np.sqrt(mean('contrast_mse')/mean('contrast_den'))),inactive_degradation=-float(np.mean([x['gain'] for x in ii])))
            row['nrmse_radius']=float(np.sqrt(np.mean([x['numerical_nrmse_radius']**2 for x in aa])))
            row['nrmse_lower']=max(0,row['contrast_nrmse']-row['nrmse_radius'])
            aggregates.append(row)
    check('private_preservation',inventory(private) if private.exists() else {},private_before)
    check('public_preservation',{p:sha(ROOT/p) for p in tracked},public_before)
    check('missing_summary_preserved',(RUN/'scientific_summary.json').exists(),False)
    result=dict(aggregates=aggregates,per_history=bounds,paired_changes=pairs,weights=weights,optimizer_diagnostics=stats,batch_comparisons=details)
    write(dest/'analysis.json',result); write(dest/'inputs.json',inputs)
    write(dest/'receipt.json',dict(status='PASS' if not failures and not missing else 'PARTIAL_OR_FAILED',scope='Supplemental saved-evidence audit, not complete-run verification',original_status='INCOMPLETE / NUMERICALLY_UNRESOLVED',qualification=False,historical_replay='1158/1160 partial',checks=checks,failures=failures,unavailable=missing,resources=dict(cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall,sampled_peak_rss=max(samples,default=0),sampling='RSS sampled at world boundaries; transient peaks and orchestration overhead not measured'),counts=dict(optimization=0,world_generation=0,new_policies=0,downloads=0,paid_calls=0),outputs={p.name:sha(p) for p in dest.iterdir() if p.is_file()}))
    print(json.dumps({'failures':failures,'unavailable':missing,'checks':len(checks),'aggregates':aggregates},indent=2))
    return bool(failures or missing)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--private-root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    started=time.process_time(); started_wall=time.monotonic()
    try: code=main(a.private_root,a.output)
    except Exception as e:
        if a.output.exists() and not (a.output/'receipt.json').exists():
            write(a.output/'receipt.json',dict(status='FAILED_AUDIT',error=repr(e),cpu_seconds=time.process_time()-started,wall_seconds=time.monotonic()-started_wall,optimization=0,world_generation=0))
        raise
    sys.exit(code)
