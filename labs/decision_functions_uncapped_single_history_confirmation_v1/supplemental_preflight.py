"""Fixed synthetic arithmetic fixtures, no fitting and no research RNG."""
from common import *
import science,scoring,objective,fixture,solver,scipy.optimize,inspect,ast
def run(out,root):
    root.mkdir(parents=True,exist_ok=False);checks={}
    def forbidden(*a,**k):raise AssertionError('Forbidden optimizer/generator')
    scipy.optimize.minimize=forbidden;solver.solve=forbidden;fixture.generate=forbidden
    # Test phase indexing with deterministic RNG substitutes, never instantiate PCG64.
    generator,pcg=np.random.Generator,np.random.PCG64
    class Fake:
        def permutation(self,x):return np.array(x)[::-1]
        def integers(self,*a,**k):return np.arange(32)%3
    np.random.PCG64=lambda seed:None;np.random.Generator=lambda _:Fake()
    try:panel=science.schedule('123',np.arange(96))
    finally:np.random.Generator=generator;np.random.PCG64=pcg
    close(panel,np.array([3*g+(i%3+j)%3 for i,g in enumerate(range(31,-1,-1)) for j in range(3)][:16]));checks['support_phase_at_permutation_position']=True
    angles=np.arange(16)*2*np.pi/3;z=np.column_stack([np.cos(angles),np.sin(angles)])
    close(np.linalg.eigvalsh(z.T@z/16),[.46875,.53125],1e-12)
    q=np.column_stack([np.cos(np.arange(36)/5),np.sin(np.arange(36)/5)])
    learner=dict(query_z=q,query_base=np.zeros((36,3)),training_prior=np.array([.2,.3,.5]));support={};models={};personal={};bounds={}
    for seed in SEEDS:models.update({str(seed)+'_V':np.arange(12).reshape(3,2,2)/9,str(seed)+'_U':np.zeros((96,2))})
    for h in HIST:
        support.update({h+'_z':z,h+'_base':np.zeros((16,3)),h+'_y':(np.arange(48)[:,None]+np.arange(16)[None])%3})
        for n in HEADS:
            dim=3 if n=='B3' else 5;personal[h+'_'+n]=np.arange(48*dim).reshape(48,dim)/1000;bounds[h+'_'+n+'_log_probability_bound']=np.full((48,36),1e-10)
    p,logs,e=science.predict(learner,support,models,personal);enc=science.log_enclosures(p,bounds,e)
    exact(p,prediction_keys());exact(logs,log_keys());close(e['H1_log_e'],np.zeros(48),1e-12)
    close(p['H1_ES_UNCAPPED'],p['H1_B3'],1e-12)
    for name in METHODS:require(np.array_equal(p['H1_'+name+'_donor'],p['H1_'+name][np.arange(48)^1]),'Donor state')
    pp,ll,cc=science.stable_mix(p['H1_B3'],p['H1_M1'],np.full(48,np.log1p(1000/.009)))
    require(np.isfinite(cc['log_beta']).all() and (np.exp(cc['log_beta'])==0).all(),'Underflow log coefficient');close(np.maximum(ll,np.log(1e-12)),np.log(np.maximum(pp,1e-12)),1e-12)
    checks['archive_prediction_donor_underflow']=True
    for h in HIST:
        for n in ('B3','ES_UNCAPPED'):
            canonical=np.log(np.maximum(p[h+'_'+n],1e-12));require((enc[h+'_'+n+'_lower']<=canonical+1e-12).all() and (enc[h+'_'+n+'_upper']>=canonical-1e-12).all(),'Enclosure containment')
    require(scoring.classify({k:[0.,0.] for k in ('gain','recovery','contrast','inactive')},True)['joint']=='PASS','Exact boundary')
    oracle=np.array([.6,.3,.1]);a=np.array([.8,.1,.1]);b=np.array([.1,.8,.1]);require(abs((scoring.loss(a,oracle)+scoring.loss(b,oracle))/2-scoring.loss((a+b)/2,oracle))>.01,'Incorrect probability pooling undetected');checks['aggregation_and_margin_rules']=True
    def rejected(fn):
        try:fn()
        except (ValueError,FileExistsError,AssertionError):return
        raise AssertionError('Expected rejection')
    atomic(root/'bytes.json',{'a':1});original=sha(root/'bytes.json');(root/'bytes.json').write_text('{"a":2}')
    rejected(lambda:require(sha(root/'bytes.json')==original,'Corrupted bytes'));rejected(lambda:atomic(root/'bytes.json',{}))
    (root/'empty.jsonl').write_text('');rejected(lambda:inventory(root/'empty.jsonl',['required']))
    journal(root/'incomplete.jsonl',dict(event='start',id='required'));rejected(lambda:inventory(root/'incomplete.jsonl',['required']))
    rejected(lambda:exact({'p':1},{'p':1,'missing':2}));rejected(lambda:probabilities(np.full((48,36,3),.4)))
    require(list(inspect.signature(science.predict).parameters)==['learner','support','models','personal'],'Prediction boundary')
    require(list(inspect.signature(solver.solve).parameters)==['a','k'] or solver.solve is forbidden,'Optimizer stub')
    for file in ('reporting.py','boundary.py'):
        tree=ast.parse((LAB/file).read_text());names=[n.name for x in ast.walk(tree) if isinstance(x,(ast.Import,ast.ImportFrom)) for n in x.names]
        require(not set(names)&{'solver','fixture','execution','science'},'Recovery imports scientific execution')
    checks['corruption_inventory_information_boundary']=True
    atomic(out/'SUPPLEMENTAL_PREFLIGHT.json',dict(passed=True,checks=checks,zero_optimizer_calls=True,zero_confirmation_rng=True))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,required=True);p.add_argument('--private-root',type=Path,required=True);a=p.parse_args();run(a.output_root,a.private_root)
