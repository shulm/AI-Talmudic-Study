"""Saved-artifact verification only: never import generator or solver."""
from common import *
import objective,science,scoring
from scipy.special import logsumexp

def independent_partitions(logits):
    # Dense two-count recurrence, independent from evidence.py's sparse tuple lookup.
    n,k,_=logits.shape;t=np.full((n,k+1,k+1),-np.inf);t[:,0,0]=0
    for j in range(k):
        u=t+logits[:,j,2,None,None]
        u[:,1:,:]=np.logaddexp(u[:,1:,:],t[:,:-1,:]+logits[:,j,0,None,None])
        u[:,:,1:]=np.logaddexp(u[:,:,1:],t[:,:,:-1]+logits[:,j,1,None,None]);t=u
    return np.stack([t[:,a,b] for a in range(k+1) for b in range(k-a+1)],axis=1)

def verify_world(out,private,world,checks):
    wr=out/'worlds'/world;pr=private/world;manifest=read(wr/'PREDICTIONS_SEALED.json')['files'];expected=read(out/'EXPECTED.json')
    exact(manifest,list(expected['archives'])+['traces.jsonl'])
    before={n:sha(pr/n) for n in manifest};close(before,manifest)
    arrays={n:load(pr/n) for n in expected['archives']}
    for name,keys in expected['archives'].items():
        exact(arrays[name],keys)
        for k,shape in keys.items():require(list(arrays[name][k].shape)==shape,'Wrong archive shape '+name+'/'+k);require(np.isfinite(arrays[name][k]).all(),'Nonfinite saved array')
    checks[world+'/archives']=True
    f,l,s,ev=[arrays[n+'.npz'] for n in ('fixture','learner','support','evaluator')];models=arrays['models.npz'];pers=arrays['personal.npz'];bounds=arrays['bounds.npz'];pred=arrays['predictions.npz'];e=arrays['evidence.npz'];enc=arrays['enclosures.npz']
    close(l['y'],f['y'][:96][:,f['train']]);close(l['z'],f['z'][f['train']]);close(l['base'],f['base'][f['train']]);close(l['query_z'],f['z'][f['test']]);close(l['query_base'],f['base'][f['test']]);close(l['training_prior'],np.bincount(l['y'].ravel(),minlength=3)/l['y'].size)
    require(not(set(f['train'])&set(f['test'])),'Query/train overlap');require(len(set(f['test']//3))==12,'Query groups');require(set(f['pool'])<=set(f['train']),'Support pool')
    close(ev['oracle'],f['oracle'][144:][:,f['test']]);close(ev['y'],f['y'][144:][:,f['test']]);close(ev['active'],f['active'][144:]);close(ev['person_ids'],np.arange(144,192));close(ev['query_ids'],f['test']);close(l['query_ids'],f['test'])
    require(int(ev['active'].sum())==24 and np.array_equal(ev['active'][::2],ev['active'][1::2]),'Pair/status preservation')
    close(f['bias'][::2],f['bias'][1::2],1e-12);close(f['u'][::2],-f['u'][1::2],1e-12);close(f['bias'].sum(1),np.zeros(192),1e-12)
    for lo,hi in ((0,96),(96,144),(144,192)):require(int(f['active'][lo:hi].sum())==(hi-lo)//2,'Balanced activity partition')
    from scipy.special import softmax
    oracle=softmax(f['base'][None]+f['bias'][:,None]+np.einsum('sr,crd,nd->snc',f['u']*f['active'][:,None],f['v'],f['z']),axis=-1);close(oracle,f['oracle'],1e-12)
    seedrow=next(x for x in read(out/'SEEDS.json')['worlds'] if x['id']==world)
    for h in HIST:
        ix=s[h+'_ids'];require(len(set(ix))==16 and set(ix)<=set(f['pool']),'Support boundaries')
        close(ix,science.schedule(seedrow[h+'_support'],f['pool']))
        close(s[h+'_y'],f['y'][144:][:,ix]);close(s[h+'_z'],f['z'][ix]);close(s[h+'_base'],f['base'][ix]);close(np.linalg.eigvalsh(s[h+'_z'].T@s[h+'_z']/16),[.46875,.53125],1e-12)
    checks[world+'/views']=True
    rows=inventory(wr/'attempts.jsonl',ids(world));ends={r['id']:r for r in rows if r['event']=='complete'}
    traces=records(pr/'traces.jsonl');exact([r['id'] for r in traces],ids(world));traces={r['id']:r for r in traces}
    inventory(wr/'wrappers.jsonl',[f'{world}/{h}/{n}' for h in HIST for n in HEADS])
    import head
    for seed in SEEDS:
        key=f'{world}/shared/{seed}';t=traces[key];require(ends[key]['success'] and ends[key]['finite'],'Shared failure')
        fun,unpack,_=head.shared_objective(l['z'],l['y'],l['base'],2,.01,.1);val,g=fun(np.array(t['parameters']));close(g,t['gradient']);close(val,t['objective'])
        v,u,b=unpack(np.array(t['parameters']));close(v,models[str(seed)+'_V']);close(u,models[str(seed)+'_U']);close(b,models[str(seed)+'_b']);checks[key]=True
    for h in HIST:
        for name in HEADS:
            v=None if name=='B3' else models[name[3:]+'_V'];a=objective.design(s[h+'_z'],v);aq=objective.design(l['query_z'],v);d=objective.penalty(a.shape[-1])
            for i,theta in enumerate(pers[h+'_'+name]):
                key=f'{world}/{h}/{name}/{i:02d}';t=traces[key];require(ends[key]['success'],'Personal failure');close(theta,t['theta'])
                b=objective.error_bounds(theta,a,s[h+'_base'],s[h+'_y'][i],d,aq);require(b['R']<=1e-10,'Independent residual failure')
                close(b,t['bounds']);close(objective.value_grad_hess(theta,a,s[h+'_base'],s[h+'_y'][i],d)[1],t['second_gradient'])
                for k,x in b.items():close(x,bounds[h+'_'+name+'_'+k][i])
                close(objective.probability(theta,aq,l['query_base']),pred[h+'_'+name][i],1e-12)
                require(len(t['optimizer']['trace'])==t['optimizer']['steps']+1,'Trace length')
                for step in t['optimizer']['trace']:
                    value,grad=objective.independent(np.array(step['theta']),a,s[h+'_base'],s[h+'_y'][i],d);close(value,step['objective']);close(float(np.linalg.norm(grad/np.sqrt(d))),step['R'])
                checks[key]=True
        for seed in SEEDS:
            prefix=f'{h}_{seed}_';atoms=e[prefix+'atoms'];allatoms=np.vstack([atoms,np.zeros((1,2))]);feature=np.einsum('crd,nd->ncr',models[str(seed)+'_V'],s[h+'_z'])
            logits=s[h+'_base'][None]+np.einsum('ar,ncr->anc',allatoms,feature);normal=independent_partitions(logits);close(normal,e[prefix+'normalizers'])
            close(atoms,np.concatenate([models[str(seed)+'_U'],-models[str(seed)+'_U']]))
            observed=np.stack([(s[h+'_y']==c).sum(1) for c in range(3)],1);close(observed,e[prefix+'counts']);cols=e[prefix+'columns'];ll=[]
            for i,y in enumerate(s[h+'_y']):
                numerator=np.array([sum(float(feature[j,y[j]]@atom) for j in range(16)) for atom in atoms]);ll.append(logsumexp(numerator-normal[:-1,cols[i]]+normal[-1,cols[i]])-np.log(192))
            close(ll,e[prefix+'log_e'])
    checks[world+'/evidence']=True
    pp,lp,ee=science.predict(l,s,models,pers);close(pp,pred,1e-12);close(lp,arrays['log_predictions.npz'],1e-12);close(ee,e);close(science.log_enclosures(pred,bounds,e),enc)
    donor=np.arange(48)^1
    for h in HIST:
        for m in METHODS:require(np.array_equal(pred[h+'_'+m+'_donor'],pred[h+'_'+m][donor]),'Donor permutation')
        for name in HEADS:
            v=None if name=='B3' else models[name[3:]+'_V'];a=objective.design(l['query_z'],v)
            dp=np.stack([objective.probability(t,a,l['query_base']) for t in pers[h+'_'+name][donor]])
            close(dp,pred[h+'_'+name][donor],1e-12)
    checks[world+'/predictions_donor']=True
    score=read(wr/'SCORES.json');close(scoring.score(pred,ev,enc,e),score)
    for row in score['rows']:
        ix=ev['active']==(row['stratum']=='active');p=pred[row['history']+'_'+row['method']][ix];o=ev['oracle'][ix];y=ev['y'][ix]
        expected=sum(float(o[i,j,c])*np.log(max(float(p[i,j,c]),1e-12)) for i in range(24) for j in range(36) for c in range(3))/-864
        close(expected,row['metrics']['expected_nll'])
        # Independent anchored contrast using explicit person/class loops.
        def con(x):
            return np.array([[[np.log(max(x[i,j,a],1e-12)/max(x[i,j,b],1e-12))-np.log(max(x[i+1,j,a],1e-12)/max(x[i+1,j,b],1e-12))-np.log(max(x[i,0,a],1e-12)/max(x[i,0,b],1e-12))+np.log(max(x[i+1,0,a],1e-12)/max(x[i+1,0,b],1e-12)) for a,b in ((0,1),(0,2),(1,2))] for j in range(36)] for i in range(0,24,2)])
        close(float(((con(p)-con(o))**2).mean()),row['contrast_mse'])
    checks[world+'/scores']=True
    close(before,{n:sha(pr/n) for n in manifest});checks[world+'/hashes_after']=True
    return score

def verify(out,private,receipt):
    require(not receipt.exists(),'Fresh verification receipt required');checks={}
    try:
        frozen(out);checks['source_freeze']=True;expected=read(out/'EXPECTED.json');scores=[]
        exact([p.name for p in (out/'worlds').iterdir()],WORLDS);exact([p.name for p in private.iterdir()],WORLDS)
        for w in WORLDS:
            require((out/'worlds'/w/'COMPLETE.json').exists(),'Incomplete world');scores.append(verify_world(out,private,w,checks));print('verified '+w,flush=True)
        inf=scoring.inference([s['gates']['H1']['joint'] for s in scores]);checks['inference']=True
        hist=read(out/'HISTORICAL_BLOBS.json');actual=subprocess.check_output(['git','hash-object','--stdin-paths'],input='\n'.join(hist)+'\n',text=True,cwd=ROOT).splitlines();close(dict(zip(hist,actual)),hist);checks['historical_preservation']=True
        exact(checks,expected['verifier_ids']);atomic(receipt,dict(integrity='PASS',completed_worlds=82,checks=checks,inference=inf,historical_blobs=len(hist),qualification_pending_resource_report=True))
    except BaseException as e:atomic(receipt,dict(integrity='FAIL',checks=checks,error=repr(e),qualification=False));raise
