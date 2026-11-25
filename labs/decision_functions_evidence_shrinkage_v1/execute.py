"""One-shot bounded scientific execution. Publication guard precedes materialization."""
from contracts import *
import head as model
from evidence import seed_evidence,mixture_weights,mixtures

def save(path,arrays):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:np.savez_compressed(stream,**arrays)
def load(path):
    with np.load(path,allow_pickle=False) as a:return {k:a[k] for k in a.files}

class RunLedger(Ledger):
    def __init__(self,real,stage,private,out):
        super().__init__(real+'_'+stage,expected(real,stage),out);self.parameter_root=private/'parameters'
        self.binding=dict(input_hashes={p.relative_to(private).as_posix():file_hash(p) for p in private.rglob('*') if p.is_file()},code_hashes={p.name:file_hash(p) for p in Path(__file__).parent.glob('*.py')},environment=environment())
        atomic(self.path/'binding.json',self.binding)
    def start(self,key,meta):
        if key not in self.expected or meta!=self.expected[key]:raise ValueError('Unexpected configuration')
        atomic(self.path/(key+'.start.json'),dict(id=key,meta=meta,utc=time.time(),binding_hash=file_hash(self.path/'binding.json')))

def run(real,private,out):
    from fixture import generate,views
    private=Path(private)/real;private.mkdir(parents=True,exist_ok=False)
    f=generate(**REAL[real]);learner,support,evaluator,orders=views(f,real)
    for role,a in [('fixture',f),('learner',learner),('support',support),('evaluator',evaluator)]:save(private/(role+'.npz'),a)
    atomic(out/(real+'_schedules.json'),orders)
    # Deliberately release generator and evaluator data before fitting/prediction.
    del f,evaluator
    shared=RunLedger(real,'shared',private,out);models={}
    for key,meta in shared.expected.items():
        seed=meta['seed'];v=model.fit(learner['z'],learner['y'],learner['base'],2,.01,.1,seed,shared,key)
        x=np.load(private/'parameters'/(key+'.npy'),allow_pickle=False)
        _,unpack,_=model.shared_objective(learner['z'],learner['y'],learner['base'],2,.01,.1)
        vv,u,b=unpack(x)
        models.update({f'{seed}_V':vv,f'{seed}_U':u,f'{seed}_b':b})
    shared.validate();save(private/'models.npz',models)
    personal=RunLedger(real,'support',private,out);pred={};evd={}
    for h in HIST:
        z,g,y=(support[f'{h}_{k}'] for k in ('z','base','y'))
        for s in SEEDS:
            e=seed_evidence(z,g,y,models[f'{s}_V'],models[f'{s}_U'])
            evd.update({f'{h}_{s}_{k}':value for k,value in e.items()})
        logs,hh,w=mixture_weights(np.array([evd[f'{h}_{s}_log_e'] for s in SEEDS]))
        evd.update({f'{h}_log_e':logs,f'{h}_h':hh,f'{h}_w':w})
        for m in HEADS:
            v=None if m=='B3' else models[m.split('_')[1]+'_V'];key=f'{real}_support_{h}_{m}_48'
            x=model.adapt(z,y,g,.06,.6,v,personal,key)
            pred[f'{h}_{m}']=model.probabilities(learner['query_z'],learner['query_base'],x,v)
        counts=np.stack([(y==c).sum(1) for c in range(3)],-1)
        pred[f'{h}_B1']=np.broadcast_to(((counts+4*learner['training_prior'])/20)[:,None],(48,36,3)).copy()
        pred[f'{h}_B2']=np.broadcast_to(model.softmax(learner['query_base'],-1),(48,36,3)).copy()
        pred[f'{h}_M1']=np.mean([pred[f'{h}_M1_{s}'] for s in SEEDS],axis=0)
        pred[f'{h}_FIXED_MIX'],pred[f'{h}_ES']=mixtures(pred[f'{h}_B3'],pred[f'{h}_M1'],w)
        for m in METHODS:pred[f'{h}_{m}_donor']=pred[f'{h}_{m}'][np.arange(48)^1]
    personal.validate();save(private/'evidence.npz',evd);save(private/'predictions.npz',pred)
    numerical=RunLedger(real,'numerical',private,out);num={}
    for n in (1,7):
        for m in HEADS:
            v=None if m=='B3' else models[m.split('_')[1]+'_V'];key=f'{real}_numerical_101_{m}_{n}'
            x=model.adapt(support['101_z'],support['101_y'][:n],support['101_base'],.06,.6,v,numerical,key)
            num[f'{n}_{m}']=model.probabilities(learner['query_z'],learner['query_base'],x[:1],v)
        num[f'{n}_M1']=np.mean([num[f'{n}_M1_{s}'] for s in SEEDS],axis=0)
        num[f'{n}_FIXED_MIX'],num[f'{n}_ES']=mixtures(num[f'{n}_B3'],num[f'{n}_M1'],evd['101_w'][:1])
    numerical.validate();save(private/'numerical.npz',num)
    # All probabilities and evidence are now saved, before query labels/status load.
    from scoring import score,evidence_summary,bootstrap,numerical_summary
    evaluator=load(private/'evaluator.npz')
    scores=score(pred,evaluator);boot,intervals=bootstrap(pred,evaluator);save(private/'bootstrap.npz',boot)
    atomic(out/(real+'_scores.json'),scores);atomic(out/(real+'_evidence.json'),evidence_summary(evd,evaluator))
    atomic(out/(real+'_bootstrap.json'),intervals);atomic(out/(real+'_numerical.json'),numerical_summary(pred,num,evaluator))
    files={p.relative_to(private).as_posix():file_hash(p) for p in private.rglob('*') if p.is_file()}
    atomic(out/(real+'_manifest.json'),dict(private_files=files,archives={role:{k:list(v.shape) for k,v in load(private/(role+'.npz')).items()} for role in ROLES},source_commit=head(),seeds=REAL[real],information_boundary='evaluator loaded only after prediction/evidence/numerical publication',model_hash=file_hash(private/'models.npz')))
    if not read(out/(real+'_numerical.json'))['passed']:raise RuntimeError('Numerical invalidity: stop without retry')

def scientific_summary(out):
    return dict(gates={r:read(out/(r+'_scores.json'))['gates']['ES']['passed'] for r in REAL},numerical_pass=all(read(out/(r+'_numerical.json'))['passed'] for r in REAL),predictive_qualified=all(all(read(out/(r+'_scores.json'))['gates']['ES']['passed'].values()) for r in REAL))

def guard(private,out,publication):
    pub=read(publication)
    if not pub.get('verified') or pub['commit']!=head():raise ValueError('Publication checkpoint not verified/current')
    frozen=read(out/'prefit_sources.json')
    ids_equal(list(frozen['files']),source_paths())
    if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')):raise ValueError('Single-thread runtime required')
    for p,h in frozen['files'].items():
        if file_hash(ROOT/p)!=h:raise ValueError('Frozen scientific source changed: '+p)
    if Path(private).exists():raise FileExistsError('Fresh private root required')
    if list((out/'records').glob('*')):raise FileExistsError('Scientific attempts already exist')
    atomic(out/'scientific_attempt.json',dict(prefit=pub['commit'],utc=time.time(),private_root=str(private),expected=contract()['totals']))

def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--publication',type=Path,required=True);a=p.parse_args()
    guard(a.private_root,a.output_root,a.publication)
    for r in REAL:run(r,a.private_root,a.output_root)
    atomic(a.output_root/'scientific_summary.json',scientific_summary(a.output_root))
if __name__=='__main__':main()
