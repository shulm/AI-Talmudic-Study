"""One-shot scientific executor. Starts are durable before actual optimizers."""
from common import *

def execute(out,private):
    import fixture,science,head,solver,objective,scoring
    from scipy.optimize import minimize
    freeze=frozen(out);pub=read(out/'PUBLICATION.json')
    require(pub['freeze_sha256']==sha(out/'FREEZE.json') and pub['readback_verified'] is True,'Published checkpoint required')
    require(subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==pub['commit'],'Wrong execution HEAD')
    private.mkdir(parents=True,exist_ok=False);(out/'worlds').mkdir(exist_ok=False)
    from boundary import run
    def work(progress):
        bank=read(out/'SEEDS.json')['worlds']
        for seeds in bank:
            world=seeds['id'];pr=private/world;pr.mkdir();wr=out/'worlds'/world;wr.mkdir()
            f=fixture.generate(*(int(seeds[k]) for k in ('generator','label','mask')))
            learner,support,evaluator=science.views(f,seeds)
            for name,a in [('fixture',f),('learner',learner),('support',support),('evaluator',evaluator)]:save(pr/(name+'.npz'),a)
            del f,evaluator
            inputs={n:sha(pr/(n+'.npz')) for n in ('fixture','learner','support','evaluator')}
            atomic(wr/'INPUTS.json',dict(seeds=seeds,hashes=inputs,source_freeze=sha(out/'FREEZE.json')))
            models={};personal={};bounds={}
            def start(key,kind,**metadata):
                journal(wr/'attempts.jsonl',dict(event='start',id=key,kind=kind,inputs=inputs,source=pub['commit'],time=time.time(),**metadata))
            def finish(key,public,full):
                journal(pr/'traces.jsonl',dict(id=key,**full));journal(wr/'attempts.jsonl',dict(event='complete',id=key,**public))
            for seed in SEEDS:
                key=f'{world}/shared/{seed}';start(key,'shared',seed=seed,rho=.01,lambda_b=.1,dimensions=[96,120,3,2])
                fun,unpack,sizes=head.shared_objective(learner['z'],learner['y'],learner['base'],2,.01,.1)
                rng=np.random.default_rng(seed);initial=np.r_[rng.normal(0,.05,sizes[0]+sizes[1]),np.zeros(sizes[2])];beg=time.process_time();wall=time.monotonic()
                r=minimize(fun,initial,jac=True,method='L-BFGS-B',options=dict(maxiter=1000,ftol=1e-12,gtol=1e-8,maxls=50));value,grad=fun(r.x)
                finite=bool(np.isfinite(value) and np.isfinite(r.x).all() and np.isfinite(grad).all())
                info=dict(success=bool(r.success),finite=finite,objective=float(value),iterations=int(r.nit),message=str(r.message),gradient_max=float(abs(grad).max()),person_scaled_gradient_max=float(abs(grad).max()*96),parameter_norm=float(np.linalg.norm(r.x)),cpu_seconds=time.process_time()-beg,wall_seconds=time.monotonic()-wall)
                finish(key,info,dict(parameters=r.x,gradient=grad,**info));require(finite and r.success,'Shared optimizer failure: '+key)
                v,u,b=unpack(r.x);models.update({str(seed)+'_V':v,str(seed)+'_U':u,str(seed)+'_b':b})
            save(pr/'models.npz',models)
            for h in HIST:
                for name in HEADS:
                    wid=f'{world}/{h}/{name}';journal(wr/'wrappers.jsonl',dict(event='start',id=wid,expected_people=48))
                    v=None if name=='B3' else models[name[3:]+'_V'];a=objective.design(support[h+'_z'],v);aq=objective.design(learner['query_z'],v);d=objective.penalty(a.shape[-1]);thetas=[];bs=[]
                    for i in range(48):
                        key=f'{wid}/{i:02d}';start(key,'personal',initialization='zero',penalty=d,dimensions=list(a.shape),support_ids=support[h+'_ids'],model_hash=sha(pr/'models.npz'))
                        beg=time.process_time();wall=time.monotonic();theta,info=solver.solve(a,support[h+'_base'],support[h+'_y'][i],d)
                        bound=objective.error_bounds(theta,a,support[h+'_base'],support[h+'_y'][i],d,aq);_,g2,_=objective.value_grad_hess(theta,a,support[h+'_base'],support[h+'_y'][i],d)
                        passed=bool(info['success'] and bound['R']<=1e-10 and np.isfinite(theta).all())
                        scalar=dict(success=passed,reason=info['reason'],R=bound['R'],R_used=bound['R_used'],steps=info['steps'],guarded_count=len(info['guarded']),gradient_comparison=bound['gradient_comparison'],parameter_norm=float(np.linalg.norm(theta)),cpu_seconds=time.process_time()-beg,wall_seconds=time.monotonic()-wall)
                        finish(key,scalar,dict(theta=theta,optimizer=info,bounds=bound,second_gradient=g2));require(passed,'Personal optimizer/residual failure: '+key)
                        thetas.append(theta);bs.append(bound)
                    personal[h+'_'+name]=np.array(thetas)
                    for k in bs[0]:bounds[h+'_'+name+'_'+k]=np.array([b[k] for b in bs])
                    journal(wr/'wrappers.jsonl',dict(event='complete',id=wid,people=48))
            save(pr/'personal.npz',personal);save(pr/'bounds.npz',bounds)
            pred,logs,evidence=science.predict(learner,support,models,personal);enclosures=science.log_enclosures(pred,bounds,evidence)
            for name,a in [('predictions',pred),('log_predictions',logs),('evidence',evidence),('enclosures',enclosures)]:save(pr/(name+'.npz'),a)
            manifest={p.name:sha(p) for p in pr.iterdir() if p.is_file()};atomic(wr/'PREDICTIONS_SEALED.json',dict(files=manifest,time=time.time(),evaluator_loaded_for_scoring=False))
            evaluator=load(pr/'evaluator.npz');result=scoring.score(pred,evaluator,enclosures,evidence);atomic(wr/'SCORES.json',result)
            inventory(wr/'attempts.jsonl',ids(world));inventory(wr/'wrappers.jsonl',[f'{world}/{h}/{n}' for h in HIST for n in HEADS])
            atomic(wr/'COMPLETE.json',dict(world=world,files=manifest,primary=result['gates']['H1']['joint'],time=time.time()));progress['completed']+=1
            print(json.dumps(dict(world=world,completed=progress['completed'],H1=result['gates']['H1']['joint'],values=result['gates']['H1']['values'])),flush=True)
        return dict(integrity='PENDING_VERIFICATION',numerical='PENDING_VERIFICATION',scientific='PENDING_VERIFICATION')
    run(out,dict(time=time.time(),commit=pub['commit'],freeze=sha(out/'FREEZE.json'),private_root=str(private)),work,82)
