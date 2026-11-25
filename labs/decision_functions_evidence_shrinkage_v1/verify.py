"""Fail-closed exact verification; no optimizer calls and no output repair."""
from contracts import *
import replay
import independent_scoring as score2

def load(path):
    with np.load(path,allow_pickle=False) as z:
        ids_equal(z.files,set(z.files))
        return {k:z[k] for k in z.files}

def difference(a,b):
    if isinstance(a,dict):
        ids_equal(list(a),list(b));return max([difference(a[k],b[k]) for k in a]+[0.])
    if isinstance(a,(list,tuple)):
        if len(a)!=len(b):raise ValueError('List length mismatch')
        return max([difference(x,y) for x,y in zip(a,b)]+[0.])
    if isinstance(a,(np.ndarray,np.number,int,float)) and not isinstance(a,(bool,np.bool_)):
        x=np.asarray(a);y=np.asarray(b)
        if x.shape!=y.shape or not np.isfinite(x).all() or not np.isfinite(y).all():raise ValueError('Shape/nonfinite mismatch')
        return float(np.max(abs(x.astype(float)-y.astype(float)),initial=0))
    if a!=b:raise ValueError('Categorical mismatch')
    return 0.

class Checker:
    def __init__(self):self.results={}
    def check(self,key,a,b,tol=1e-12):
        if key in self.results:raise ValueError('Duplicate comparison')
        delta=difference(a,b)
        if delta>tol:raise ValueError(f'{key}: {delta} exceeds {tol}')
        self.results[key]=dict(max_abs=delta,tolerance=tol)

def valid_array(a,shape,probability=False):
    if list(a.shape)!=shape or not np.isfinite(a).all():raise ValueError('Missing/invalid array shape or values')
    if probability and (a.min()<0 or a.max()>1 or np.max(abs(a.sum(-1)-1))>1e-12):raise ValueError('Bad normalization')

def forward(real,arrays,private):
    l=arrays['learner'];s=arrays['support'];models={};pred={};evd={};num={}
    for seed in SEEDS:
        x=np.load(private/'parameters'/f'{real}_shared_{seed}.npy',allow_pickle=False)
        if x.shape!=(492,):raise ValueError('Wrong shared vector length')
        models.update({f'{seed}_V':x[:12].reshape(3,2,2),f'{seed}_U':x[12:204].reshape(96,2),f'{seed}_b':x[204:].reshape(96,3)})
    for h in HIST:
        for seed in SEEDS:
            ee=replay.evidence(s[f'{h}_z'],s[f'{h}_base'],s[f'{h}_y'],models[f'{seed}_V'],models[f'{seed}_U'])
            evd.update({f'{h}_{seed}_{k}':v for k,v in ee.items()})
        le,hh,w=replay.weights(np.stack([evd[f'{h}_{seed}_log_e'] for seed in SEEDS]));evd.update({f'{h}_log_e':le,f'{h}_h':hh,f'{h}_w':w})
        for m in HEADS:
            v=None if m=='B3' else models[m.split('_')[1]+'_V'];n=3 if v is None else 5
            x=np.load(private/'parameters'/f'{real}_support_{h}_{m}_48.npy',allow_pickle=False).reshape(48,n)
            pred[f'{h}_{m}']=replay.probs(l['query_z'],l['query_base'],x,v)
        counts=np.array([np.bincount(y,minlength=3) for y in s[f'{h}_y']])
        b1=(counts+4*l['training_prior'])/(16+4);pred[f'{h}_B1']=np.repeat(b1[:,None,:],36,axis=1)
        pred[f'{h}_B2']=replay.probs(l['query_z'],l['query_base'],np.zeros((48,3)),None)
        pred[f'{h}_M1']=sum(pred[f'{h}_M1_{seed}']/3 for seed in SEEDS)
        b=pred[f'{h}_B3'];m=pred[f'{h}_M1'];pred[f'{h}_FIXED_MIX']=b/10+m*9/10;pred[f'{h}_ES']=(1-w[:,None,None])*b+w[:,None,None]*m
        for m in METHODS:pred[f'{h}_{m}_donor']=np.stack([pred[f'{h}_{m}'][i+1 if i%2==0 else i-1] for i in range(48)])
    for n in (1,7):
        for m in HEADS:
            v=None if m=='B3' else models[m.split('_')[1]+'_V'];cols=3 if v is None else 5
            x=np.load(private/'parameters'/f'{real}_numerical_101_{m}_{n}.npy',allow_pickle=False).reshape(n,cols)
            num[f'{n}_{m}']=replay.probs(l['query_z'],l['query_base'],x[:1],v)
        num[f'{n}_M1']=sum(num[f'{n}_M1_{seed}']/3 for seed in SEEDS)
        b=num[f'{n}_B3'];m=num[f'{n}_M1'];w=evd['101_w'][0];num[f'{n}_FIXED_MIX']=b/10+m*9/10;num[f'{n}_ES']=(1-w)*b+w*m
    return dict(models=models,predictions=pred,numerical=num,evidence=evd)

def record_values(meta,x,l,s,models):
    # Independent objective/gradient calculation (matrix operations, no fitter).
    from scipy.special import logsumexp
    if meta['kind']=='shared':
        z,g,y=l['z'],l['base'],l['y'];v=x[:12].reshape(3,2,2);u=x[12:204].reshape(96,2);b=x[204:].reshape(96,3);n=96
    else:
        h=meta['history'];n=meta['people'];z,g,y=s[f'{h}_z'],s[f'{h}_base'],s[f'{h}_y'][:n]
        v=None if meta['model']=='B3' else models[str(meta['seed'])+'_V'];xx=x.reshape(n,3 if v is None else 5);b=xx[:,:3];u=xx[:,3:]
    rho,lb=meta['rho'],meta['lambda_b'];logits=g[None]+b[:,None]
    f=None
    if v is not None:
        f=np.stack([z@v[c].T for c in range(3)],axis=1);logits=logits+np.stack([u@f[:,c].T for c in range(3)],axis=-1)
    probs=np.exp(logits-logsumexp(logits,-1,keepdims=True));res=(probs-np.eye(3)[y])/y.size
    value=float((logsumexp(logits,-1)-np.take_along_axis(logits,y[...,None],-1)[...,0]).mean()+lb*np.sum(b*b)/(2*n)+rho*np.sum(u*u)/(2*n))
    gb=res.sum(1)+lb*b/n
    gu=np.zeros_like(u) if v is None else sum(res[:,:,c]@f[:,c] for c in range(3))+rho*u/n
    if meta['kind']=='shared':
        value+=rho*np.sum(v*v)/2;gv=np.stack([u.T@res[:,:,c]@z+rho*v[c] for c in range(3)])
        grad=np.concatenate([gv.ravel(),gu.ravel(),gb.ravel()])
    else:grad=np.concatenate([gb,gu],axis=1).ravel()
    return dict(objective=float(value),gradient_max=float(abs(grad).max()),person_scaled_gradient_max=float(abs(grad).max()*n),parameter_count=len(x),parameter_norm=float(np.linalg.norm(x)),feature_shape=list(z.shape),feature_norm=float(np.linalg.norm(z)))

def pointwise(p,e):
    worst=0.
    for h in HIST:
        b=p[f'{h}_B3'];es=p[f'{h}_ES'];hh=e[f'{h}_h'][:,None,None];w=e[f'{h}_w']
        if np.any(w<0) or np.any(w>.9):raise ValueError('Weight range')
        if np.any(w[e[f'{h}_log_e']<=0]!=0):raise ValueError('Missing fallback')
        raw=np.exp(-hh)*b-es;clipped=np.log(np.maximum(b,1e-12))-np.log(np.maximum(es,1e-12))-hh
        worst=max(worst,float(raw.max()),float(clipped.max()))
        if worst>1e-12:raise ValueError('Pointwise bound failure')
    return worst

def verify(private,out):
    private=Path(private);out=Path(out);c=Checker();gates={};numerical=True;all_hashes={}
    ids_equal([x.name for x in (out/'records').iterdir()],[f'{r}_{s}' for r in REAL for s in STAGES])
    for r in REAL:
        root=private/r;manifest=read(out/(r+'_manifest.json'));before={p.relative_to(root).as_posix():file_hash(p) for p in root.rglob('*') if p.is_file()};all_hashes[r]=before
        required={role+'.npz' for role in ROLES}|{'parameters/'+key+'.npy' for st in STAGES for key in expected(r,st)}
        ids_equal(list(before),required);c.check(r+'/manifest',before,manifest['private_files'])
        if manifest['archives']!={role:shapes(role) for role in ROLES} or manifest['seeds']!=REAL[r]:raise ValueError('Manifest contract mismatch')
        arrays={role:load(root/(role+'.npz')) for role in ROLES}
        for role,a in arrays.items():
            ids_equal(list(a),shapes(role))
            for k,v in a.items():
                valid_array(v,shapes(role)[k],role in ('predictions','numerical'))
                c.check(f'{r}/archive/{role}/{k}',list(v.shape),shapes(role)[k])
        for st in STAGES:
            path=out/'records'/f'{r}_{st}';ee=expected(r,st);validate_records(path,ee)
            if read(path/'expected.json')!=ee:raise ValueError('Wrong declared stage')
            binding=read(path/'binding.json')
            ids_equal(list(binding),['input_hashes','code_hashes','environment'])
            ids_equal(list(binding['input_hashes']),binding_paths(r,st))
            if binding['code_hashes']!={n:file_hash(Path(__file__).parent/n) for n in SOURCE_NAMES}:raise ValueError('Code binding mismatch')
            if binding['environment']!=read(out/'environment.json'):raise ValueError('Environment binding mismatch')
            for p,h in binding['input_hashes'].items():
                if before[p]!=h:raise ValueError('Stage input changed')
            for key in ee:
                if read(path/(key+'.start.json'))['binding_hash']!=file_hash(path/'binding.json'):raise ValueError('Start binding mismatch')
                x=np.load(root/'parameters'/(key+'.npy'),allow_pickle=False);rec=read(path/(key+'.complete.json'))
                vals=record_values(ee[key],x,arrays['learner'],arrays['support'],arrays['models'])
                c.check(f'{r}/record/{key}',{k:rec[k] for k in vals},vals)
        from fixture import generate,views
        f=generate(**REAL[r]);ll,ss,ev,orders=views(f,r)
        c.check(r+'/fixture_join',dict(fixture=f,learner=ll,support=ss,evaluator=ev),{k:arrays[k] for k in ('fixture','learner','support','evaluator')})
        c.check(r+'/support_geometry',read(out/(r+'_schedules.json')),orders)
        ff=forward(r,arrays,root)
        boot,interval=score2.bootstrap(arrays['predictions'],arrays['evaluator']);ff['bootstrap']=boot
        for role,a in ff.items():
            ids_equal(list(a),shapes(role))
            for k,v in a.items():c.check(f'{r}/forward/{role}/{k}',arrays[role][k],v,1e-10 if role=='evidence' and k.endswith(('normalizers','log_e')) else 1e-12)
        scores=score2.score(arrays['predictions'],arrays['evaluator']);c.check(r+'/scores',read(out/(r+'_scores.json')),scores)
        c.check(r+'/evidence_summary',read(out/(r+'_evidence.json')),score2.evidence_summary(arrays['evidence'],arrays['evaluator']))
        c.check(r+'/bootstrap_summary',read(out/(r+'_bootstrap.json')),interval)
        nr=score2.numerical_summary(arrays['predictions'],arrays['numerical'],arrays['evaluator']);c.check(r+'/numerical_summary',read(out/(r+'_numerical.json')),nr)
        c.check(r+'/pointwise',pointwise(arrays['predictions'],arrays['evidence']),0.)
        gates[r]=scores['gates']['ES']['passed'];numerical=bool(numerical and nr['passed'])
        after={p.relative_to(root).as_posix():file_hash(p) for p in root.rglob('*') if p.is_file()}
        if before!=after:raise ValueError('Private bytes changed during verification')
    frozen=read(out/'prefit_sources.json');ids_equal(list(frozen['files']),source_paths());c.check('frozen_sources',{p:file_hash(ROOT/p) for p in frozen['files']},frozen['files'])
    hist=read(out/'historical_blobs.json');truth=historical()
    if hist!=truth:raise ValueError('Incomplete historical manifest')
    hashes=subprocess.run(['git','hash-object','--stdin-paths'],input='\n'.join(hist)+'\n',cwd=ROOT,text=True,capture_output=True,check=True).stdout.splitlines()
    actual=dict(zip(hist,hashes))
    c.check('historical_blobs',actual,hist)
    q=qualification('VERIFIED_COMPLETE',numerical,gates);c.check('qualification',read(out/'scientific_summary.json'),dict(gates=gates,numerical_pass=numerical,predictive_qualified=all(all(v.values()) for v in gates.values())))
    c.check('resource_contract',dict(shared_fits=sum(len(expected(r,'shared')) for r in REAL),adaptation_batches=sum(len(expected(r,st)) for r in REAL for st in ('support','numerical')),person_solves=sum(v['person_solves'] for r in REAL for st in STAGES for v in expected(r,st).values()),optimizer_records=sum(len(expected(r,st)) for r in REAL for st in STAGES)),dict(shared_fits=12,adaptation_batches=64,person_solves=1664,optimizer_records=76))
    ids_equal(list(c.results),comparison_ids())
    return dict(state='VERIFIED_COMPLETE',qualification=q,numerical_pass=numerical,gates=gates,comparisons=len(c.results),checks=c.results,max_abs=max(x['max_abs'] for x in c.results.values()),private_hashes_before_after=all_hashes,hashes_unchanged=True)

def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    if a.receipt.exists():raise FileExistsError('Receipt collision')
    try:r=verify(a.private_root,a.output_root)
    except Exception as e:r=dict(state='INCOMPLETE',qualification=False,error=repr(e));atomic(a.receipt,r);raise
    atomic(a.receipt,r)
if __name__=='__main__':main()
