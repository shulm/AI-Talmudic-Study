"""No fitting: failure paths, objective equivalence, gradients, spectral examples."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import importlib.util
import tempfile
from core import *
from replay import validate_archive,verify_hash,compare,bootstrap
from head_v1 import shared_objective,personal_objective,certificate,ce
from scipy.optimize import check_grad
from scipy.special import softmax,logsumexp

def rejects(fn):
    try: fn()
    except (ValueError,FileExistsError): return
    raise AssertionError('Invalid evidence accepted')

def main():
    passed=[]
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp); f=root/'bytes'; f.write_bytes(b'a'); h=file_hash(f); f.write_bytes(b'b'); rejects(lambda:verify_hash(f,h)); passed.append('changed_bytes')
        p=np.full((2,3,3),1/3); rejects(lambda:validate_archive({}, {'required'},p.shape)); passed.append('missing_array')
        rejects(lambda:validate_archive({'required':p*2},{'required'},p.shape)); passed.append('bad_normalization')
        rejects(lambda:compare([.1,.2],[.1,.3])); passed.append('wrong_loss_aggregation')
        rejects(lambda:validate_records(root,{})); passed.append('empty_log')
        expected={'a':meta('toy',.1,people=2),'b':meta('toy',.1,people=2)}
        ledger=Ledger('toy',expected,root); ledger.start('a',expected['a']); ledger.complete('a',dict(success=True,finite=True))
        rejects(ledger.validate); passed.append('missing_configuration')
        ledger.start('b',expected['b']); rejects(ledger.validate); passed.append('interrupted_run')
        ledger.complete('b',dict(success=False,finite=True)); rejects(ledger.validate); passed.append('nonconvergence')
        rejects(lambda:ledger.complete('a',dict(success=True,finite=True))); passed.append('output_collision')
        rejects(lambda:ledger.start('unexpected',{})); passed.append('unexpected_configuration')
    # Capture frozen objective closures without invoking any optimizer.
    module_path=ROOT/'labs/decision_functions/models.py'
    assert module_path.read_bytes().replace(b'\r\n',b'\n')==git_bytes(FREEZE,'labs/decision_functions/models.py')
    spec=importlib.util.spec_from_file_location('frozen_head',module_path); old=importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
    rng=np.random.default_rng(123); z=rng.normal(size=(7,2)); y=rng.integers(0,3,size=(4,7)); base=rng.normal(size=(7,3)); errors=[]
    def capture(fun,x,kind):
        old.captured=fun; old.OPT_LOG.append({}); return x.ravel()
    old.solve=capture
    old.fit_m1(z,y,base,2,.1,11)
    new,_,sizes=shared_objective(z,y,base,2,.1); probe=rng.normal(0,.2,sum(sizes))
    errors.extend([compare(old.captured(probe)[0],new(probe)[0]),compare(old.captured(probe)[1],new(probe)[1])])
    gradient_errors=[float(check_grad(lambda x:new(x)[0],lambda x:new(x)[1],probe))]
    v=rng.normal(size=(3,2,2)); old.adapt(base,base,z,z,y,.1,v)
    new,shape=personal_objective(z,y,base,.1,v); probe=rng.normal(0,.2,np.prod(shape))
    errors.extend([compare(old.captured(probe)[0],new(probe)[0]),compare(old.captured(probe)[1],new(probe)[1])])
    gradient_errors.append(float(check_grad(lambda x:new(x)[0],lambda x:new(x)[1],probe)))
    assert max(gradient_errors)<1e-5
    passed+=['objective_gradient_equivalence','finite_difference_gradients']
    # Balanced labels make zero intercept exactly stationary for all lambdas.
    z=np.array([[-1.], [0.], [1.]]); y=np.array([[0,1,2],[2,1,0]]); base=np.zeros((3,3)); b=np.zeros((2,3))
    yes=certificate(z,y,base,b,10.); no=certificate(z,y,base,b,.001)
    assert yes['status']=='ZERO_INTERACTION_OPTIMAL' and no['status']=='NONZERO_DESCENT_AVAILABLE'
    g=np.einsum('snc,nd->scd',softmax(base[None]+b[:,None],-1)-np.eye(3)[y],z).reshape(2,-1)/6
    u,s,vt=np.linalg.svd(g,full_matrices=False); direction=-np.outer(u[:,0],vt[0]); step=1e-4; w=step*direction
    logits=np.einsum('scd,nd->snc',w.reshape(2,3,1),z)
    value=ce(logits,y)[0]+.001/np.sqrt(2)*np.linalg.svd(w,compute_uv=False).sum()
    initial=ce(np.zeros((2,3,3)),y)[0]; assert value<initial
    passed+=['spectral_satisfied','spectral_violated','rank_one_descent']
    constant=bootstrap(np.full((3,4),.123),['a','a','b','c']); assert np.allclose(constant['interval95'],[.123,.123],atol=1e-15,rtol=0)
    passed.append('group_bootstrap_known_constant')
    receipt('engineering_checks.json',dict(status='PASS',tests=passed,equivalence_max_error=max(errors),gradient_errors=gradient_errors,spectral_examples=[yes,no],rank_one_objective_decrease=float(initial-value),optimizer_fits=0,person_solves=0))
    print('PASS',len(passed))

if __name__=='__main__': main()
