from common import *
from objective import design,penalty,value_grad_hess,independent,probability,error_bounds
from solver import solve
V=np.array([[[1,0],[0,1]],[[-1,1],[1,0]],[[0,-1],[-1,-1]]],dtype=float)
def fixture():
    out={};cycle=np.array([[1,0],[0,1],[-1,0],[0,-1]],float)
    for p in range(48):
        b,m=divmod(p,8);y=np.array([((i+b)%3 if m in (0,1,2,5) else (((i%2)+b)%3 if m==3 else ([0,1,1,2][i%4] if m==4 else b%3))) for i in range(16)])
        for tag,n in [('support',16),('query',12)]:
            i=np.arange(n);t=(2*i-(n-1))/n;z=np.zeros((n,2))
            if m in (1,5):z=cycle[i%4]
            elif m==2:z[:,0]=1
            elif m==3:z[:,0]=(-1.)**i
            elif m==4:z=8*cycle[i%4]
            elif m==7:z[:,0]=t
            c=(2*b-5)/16*np.array([1.,-1,0]);g=c[None]+[0,1/8,1/8,0,0,12,0,0][m]*t[:,None]*np.array([1.,-2,1])
            if m==0:g=np.broadcast_to(np.log(np.bincount(y,minlength=3)/16)+(2*b-5)/16,(n,3)).copy()
            out[f'{p}_{tag}_z']=z;out[f'{p}_{tag}_g']=g
        out[f'{p}_y']=y
    out['V']=V;return out
def inputs(f,p,model):
    v=None if model=='B3' else f['V'];a=design(f[f'{p}_support_z'],v);q=design(f[f'{p}_query_z'],v)
    return a,f[f'{p}_support_g'],f[f'{p}_y'].astype(int),penalty(a.shape[-1]),q,f[f'{p}_query_g']
def derivative_checks(f):
    rows=[];step=2.**-18
    for p in range(48):
        for model in ('B3','M1'):
            a,g,y,d,q,qg=inputs(f,p,model);theta=np.array([((p+3*j)%11-5)/16 for j in range(len(d))]);value,grad,hess=value_grad_hess(theta,a,g,y,d)
            scalar,ig=independent(theta,a,g,y,d);close(value,scalar);close(grad,ig)
            fd=[];fh=[]
            for j in range(len(d)):
                e=np.eye(len(d))[j]*step;vp,gp=independent(theta+e,a,g,y,d);vm,gm=independent(theta-e,a,g,y,d)
                fd.append((vp-vm)/(2*step));fh.append((gp-gm)/(2*step))
            fd=np.array(fd);fh=np.array(fh).T
            ge=float(abs(fd-grad).max()/max(1,abs(fd).max(),abs(grad).max()));he=float(abs(fh-hess).max()/max(1,abs(fh).max(),abs(hess).max()))
            sym=float(abs(hess-hess.T).max());mineig=float(np.linalg.eigvalsh(hess-np.diag(d)).min());positive=bool(np.linalg.eigvalsh(hess).min()>0)
            passed=ge<=2e-6 and he<=2e-6 and sym<=1e-12*max(1,abs(hess).max()) and mineig>=-1e-10*max(1,np.linalg.norm(hess,2)) and positive
            rows.append(dict(id=f'{p}_{model}',gradient_normalized_error=ge,hessian_normalized_error=he,symmetry_error=sym,min_likelihood_eigenvalue=mineig,positive_definite=positive,passed=bool(passed)))
    return dict(rows=rows,gradient_blocks=96,hessian_blocks=96,passed=all(r['passed'] for r in rows),optimizer_calls=0)
def engineering_checks(f,arrays,records):
    checks={};allpass=True
    for model in ('B3','M1'):
        base=arrays[f'singletons_{model}_theta'];pr=arrays[f'singletons_{model}_probabilities']
        identical=all(np.array_equal(base,arrays[f'{l}_{model}_theta']) and np.array_equal(pr,arrays[f'{l}_{model}_probabilities']) for l in ('chunks7','all48','reverse48'))
        checks[model+'_layout_bitwise']=identical;allpass &= identical
    for b in range(6):
        p=8*b;freq=np.bincount(f[f'{p}_y'].astype(int),minlength=3)/16
        for m in ('B3','M1'):
            theta=arrays[f'singletons_{m}_theta'][p];prob=arrays[f'singletons_{m}_probabilities'][p]
            passed=bool(np.array_equal(theta,np.zeros_like(theta)) and abs(prob-freq).max()<=1e-13);checks[f'{p}_{m}_zero_optimum']=passed;allpass &= passed
        for motif in (0,6,7):
            p=8*b+motif;xx=arrays['singletons_M1_theta'][p];u=float(np.linalg.norm(xx[3:]));delta=float(abs(arrays['singletons_B3_probabilities'][p]-arrays['singletons_M1_probabilities'][p]).max())
            bb=[]
            for m in ('B3','M1'):
                a,g,y,d,q,qg=inputs(f,p,m);bb.append(error_bounds(arrays[f'singletons_{m}_theta'][p],a,g,y,d,q)['probability_bound'])
            allowed=float(np.max(bb[0]+bb[1]))+1e-12;passed=u<=1e-8 and delta<=1e-8 and delta<=allowed
            checks[f'{p}_analytic']=dict(u_norm=u,probability_difference=delta,residual_bound_plus_allowance=allowed,passed=bool(passed));allpass &= passed
    return dict(checks=checks,passed=bool(allpass and all(r['engineering_pass'] for r in records.values())))
def run_suite(private,out):
    f={k:np.array(v) for k,v in read(OUT/'FIXTURE.json').items()};fhash=digest(OUT/'FIXTURE.json');arrays={};records={}
    for w in wrappers():
        atomic(out/'wrappers'/(w['id']+'.start.json'),dict(**w,fixture_hash=fhash,utc=time.time()))
        keyprefix=w['layout']+'_'+w['model'];dim=3 if w['model']=='B3' else 5
        if keyprefix+'_theta' not in arrays:arrays.update({keyprefix+'_theta':np.zeros((48,dim)),keyprefix+'_probabilities':np.zeros((48,12,3))})
        for p in w['people']:
            key=f'{w["id"]}_p{p}';spec=attempts()[key];atomic(out/'attempts'/(key+'.start.json'),dict(id=key,spec=spec,fixture_hash=fhash,source_hash=digest(LAB/'solver.py'),utc=time.time()))
            a,g,y,d,q,qg=inputs(f,p,w['model']);start=time.process_time();wall=time.monotonic()
            try:
                theta,res=solve(a,g,y,d);pb=probability(theta,q,qg);eb=error_bounds(theta,a,g,y,d,q);r=eb['R'];kr=float(eb['K'].max()*r)
                agree=abs(r-res['R'])<=1e-12*max(1,r,res['R']);passed=bool(res['success'] and r<=1e-10 and kr<=1e-8 and agree)
                rec=dict(id=key,spec=spec,**res,R_recomputed=r,residual_agreement=bool(agree),Kmax=float(eb['K'].max()),KR=kr,probability_bounds=(eb['K']*r/2).tolist(),log_probability_bounds=(np.sqrt(2)*eb['K']*r).tolist(),engineering_pass=passed,cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall)
                atomic(out/'attempts'/(key+'.complete.json'),rec);records[key]=rec
                arrays[keyprefix+'_theta'][p]=theta;arrays[keyprefix+'_probabilities'][p]=pb
            except BaseException as e:
                atomic(out/'attempts'/(key+'.failure.json'),dict(id=key,reason=repr(e),cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall));raise
        atomic(out/'wrappers'/(w['id']+'.complete.json'),dict(**w,attempts=[f'{w["id"]}_p{p}' for p in w['people']]))
    save(private/'engineering.npz',arrays);checks=engineering_checks(f,arrays,records)
    atomic(out/'engineering_checks.json',checks)
    atomic(out/'engineering_manifest.json',dict(hash=digest(private/'engineering.npz'),shapes={k:list(v.shape) for k,v in arrays.items()},attempts=len(records),wrappers=len(wrappers()),passed=checks['passed']))
    return checks
