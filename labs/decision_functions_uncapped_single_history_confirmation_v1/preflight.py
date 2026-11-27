"""Zero-fit, zero-confirmation-RNG tests, including real dispatcher and supervisor."""
from common import *
import itertools,math
from fractions import Fraction
from scipy.special import logsumexp

def run(out,mockroot):
    require(mockroot is not None,'Explicit isolated mock root required');mockroot=Path(mockroot);mockroot.mkdir(parents=True,exist_ok=False)
    import scipy.optimize,fixture,solver,objective,evidence,scoring,science,verify
    from supervise import supervise
    checks={};calls=[]
    def forbidden(*a,**k):calls.append('FORBIDDEN');raise RuntimeError('Preflight prohibits optimizer and scientific RNG')
    scipy.optimize.minimize=forbidden;solver.solve=forbidden;fixture.generate=forbidden;np.random.default_rng=forbidden;np.random.PCG64=forbidden
    a=objective.design(np.array([[1.,0.],[0.,1.],[-1.,0.],[0.,-1.]]),np.arange(12).reshape(3,2,2)/17);g=np.arange(12).reshape(4,3)/31;y=np.array([0,1,2,0]);d=objective.penalty(5);theta=np.arange(5)/23
    val,grad,hess=objective.value_grad_hess(theta,a,g,y,d);iv,ig=objective.independent(theta,a,g,y,d);close(val,iv,1e-12);close(grad,ig,1e-12)
    for j in range(5):
        delta=np.eye(5)[j]*1e-5;vp,gp,_=objective.value_grad_hess(theta+delta,a,g,y,d);vm,gm,_=objective.value_grad_hess(theta-delta,a,g,y,d);close((vp-vm)/2e-5,grad[j],1e-8);close((gp-gm)/2e-5,hess[:,j],1e-8)
    checks['derivatives_fixed_inputs']=True
    logits=np.arange(18).reshape(2,3,3)/19;counts,dp=evidence.partitions(logits);enum=[]
    for count in counts:
        sequences=[seq for seq in itertools.product(range(3),repeat=3) if np.array_equal(np.bincount(seq,minlength=3),count)]
        enum.append([logsumexp([sum(logits[atom,j,c] for j,c in enumerate(seq)) for seq in sequences]) for atom in range(2)])
    close(dp,np.array(enum).T,1e-12);close(verify.independent_partitions(logits),dp,1e-12);checks['enumerated_evidence']=True
    # Replay saved engineering numerical trajectories, without invoking solve.
    old=ROOT/'research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1';fixture_old=read(old/'FIXTURE.json')
    replay=0
    for f in sorted((old/'attempts').glob('*.complete.json')):
        r=read(f);person=r['spec']['person'];name=r['spec']['model']
        # Saved fixture arrays are read through the original deterministic accessor.
        z=np.array(fixture_old[f'{person}_support_z']);base=np.array(fixture_old[f'{person}_support_g']);labels=np.array(fixture_old[f'{person}_y']);v=None if name=='B3' else np.array(fixture_old['V'])
        aa=objective.design(z,v);dd=objective.penalty(aa.shape[-1])
        for step in r['trace']:
            vv,gg=objective.independent(np.array(step['theta']),aa,base,labels,dd);close(vv,step['objective']);close(np.linalg.norm(gg/np.sqrt(dd)),step['R']);replay+=1
    require(replay>384,'Empty engineering replay');checks['saved_engineering_trace_points']=replay
    for case in ('success','scientific','numerical','incomplete','child-failure','collision'):
        dest=mockroot/case;account=mockroot/(case+'-account');cmd=[sys.executable,str(LAB/'cli.py'),'mock','--output-root',str(dest),'--scenario',case]
        r=supervise(cmd,account);require(r['child_reaped'],'Mock child not reaped')
        if case in ('child-failure','collision'):require(r['reason'] is not None and (dest/'EXECUTION_START.json').exists() and read(dest/'EXECUTION_TERMINAL.json')['qualification'] is False,'Failure/start retention')
        else:require(r['reason'] is None,'Unexpected mock child failure');require(read(dest/'EXECUTION_TERMINAL.json')['qualification']==(case=='success'),'Mock qualification')
        checks['boundary/'+case]=True
    r=supervise(['THIS_EXECUTABLE_DOES_NOT_EXIST'],mockroot/'launch');require(r['reason'] is not None and r['child_reaped'],'Launch failure');checks['boundary/launch']=True
    for case in ('resource','interrupt'):
        dest=mockroot/case;cmd=[sys.executable,str(LAB/'cli.py'),'mock','--output-root',str(dest),'--scenario','sleep']
        r=supervise(cmd,mockroot/(case+'-account'),rss_limit=1 if case=='resource' else 4*1024**3,interrupt=dest/'EXECUTION_START.json' if case=='interrupt' else False)
        require(r['reason'] is not None and r['child_reaped'],'Termination');
        if case=='interrupt':require((dest/'EXECUTION_START.json').exists() and not (dest/'EXECUTION_TERMINAL.json').exists(),'Interrupted start must persist')
        checks['boundary/'+case]=True
    r=supervise([sys.executable,str(LAB/'cli.py'),'mock','--output-root',str(mockroot/'success'),'--scenario','success'],mockroot/'output-collision');require(r['reason'] is not None,'Output collision');checks['boundary/output_collision']=True
    for n in (0,71,72,82):
        x=scoring.inference(['PASS']*n+['FAIL']*(82-n));tail=sum(Fraction(math.comb(82,k)*4**k,5**82) for k in range(n,83));close(x['p_exact'],float(tail),1e-12);require(x['count_pass']==(n>=72),'Binomial boundary')
    close(scoring.inference(['PASS']*72+['FAIL']*10)['one_sided_95_lower'],.8019263987400118,1e-12)
    require(not scoring.inference(['PASS']*72+['FAIL']*9+['NUMERICALLY_UNRESOLVED'])['statistical_and_resolution_pass'],'Unresolved veto')
    require(scoring.classify(dict(gain=[1,2],recovery=[1,2],contrast=[1,2],inactive=[1,2]),False)['joint']=='NUMERICALLY_UNRESOLVED','Positive-gap domain')
    require(scoring.classify(dict(gain=[-2,-1],recovery=[-1,1],contrast=[1,2],inactive=[1,2]),False)['joint']=='FAIL','Definite failure precedence')
    checks['statistical_boundaries']=True
    from prepare import module,REVIEW
    plan=module('plan_arithmetic',REVIEW/'PLAN_CALCULATION.py').calculate()
    close(plan['primary_design'],read(out/'PLAN_CALCULATION.json')['primary_design'],1e-12);require(plan['minimum_search']['every_smaller_n_fails_target_power'],'Planning minimum')
    checks['exact_planning_arithmetic']=True
    def rejected(fn):
        try:fn()
        except (ValueError,FileExistsError,KeyError):return
        raise AssertionError('Failure path accepted')
    rejected(lambda:exact([],['required']));rejected(lambda:exact(['a','a'],['a']));rejected(lambda:probabilities(np.full((48,36,3),.4)));rejected(lambda:scoring.inference(['PASS']*81));rejected(lambda:terminal(completed=1,expected=1,integrity='PASS',numerical='PASS',scientific='PASS',reason='failure',qualified=True));checks['fail_closed']=True
    require(not calls,'Forbidden preflight invocation')
    atomic(out/'PREFLIGHT_FINAL.json',dict(passed=True,checks=checks,forbidden_invocations=calls,zero_confirmation_generation=True,zero_optimizer_calls=True,mock_root=str(mockroot),entrypoint_sha256=sha(LAB/'cli.py'),supervisor_sha256=sha(LAB/'supervise.py'),boundary_sha256=sha(LAB/'boundary.py'),mock_receipts={str(p.relative_to(mockroot)):dict(sha256=sha(p),record=read(p)) for p in mockroot.rglob('*.json')}))
