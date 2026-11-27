"""Deterministic manifests and source freeze; no world materialization."""
from common import *
import platform,scipy,psutil,importlib.util
REVIEW=ROOT/'research/decision_functions_2026-11-24/reviews/post_es_diagnostics_v1_2026-11-26'
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def archive_shapes():
    a={'fixture.npz':dict(z=[192,2],base=[192,3],bias=[192,3],u=[192,2],v=[3,2,2],active=[192],y=[192,192],oracle=[192,192,3],train=[120],reserved=[36],test=[36],pool=[96]),'learner.npz':dict(z=[120,2],base=[120,3],y=[96,120],query_z=[36,2],query_base=[36,3],query_ids=[36],training_prior=[3]),'evaluator.npz':dict(y=[48,36],oracle=[48,36,3],active=[48],person_ids=[48],query_ids=[36]),'support.npz':{},'models.npz':{},'personal.npz':{},'bounds.npz':{},'evidence.npz':{},'enclosures.npz':{},'predictions.npz':{k:[48,36,3] for k in prediction_keys()},'log_predictions.npz':{k:[48,36,3] for k in log_keys()}}
    for s in SEEDS:a['models.npz'].update({str(s)+'_V':[3,2,2],str(s)+'_U':[96,2],str(s)+'_b':[96,3]})
    for h in HIST:
        a['support.npz'].update({h+'_ids':[16],h+'_z':[16,2],h+'_base':[16,3],h+'_y':[48,16]})
        for n in HEADS:
            d=3 if n=='B3' else 5;a['personal.npz'][h+'_'+n]=[48,d]
            for k,shape in dict(gradient=[48,d],R=[48],R_allowance=[48],R_used=[48],gradient_comparison=[48],theta_D_norm=[48],K=[48,36],probability_bound=[48,36],log_probability_bound=[48,36]).items():a['bounds.npz'][h+'_'+n+'_'+k]=shape
        for s in SEEDS:
            for k,shape in dict(atoms=[192,2],weights=[192],count_order=[153,3],normalizers=[193,153],counts=[48,3],columns=[48],sufficient=[48,2],log_e=[48]).items():a['evidence.npz'][f'{h}_{s}_{k}']=shape
        for k in ('log_e','h','log_beta','w','capped_h'):a['evidence.npz'][h+'_'+k]=[48]
        for m in ('B3','ES_UNCAPPED'):
            for side in ('lower','upper'):a['enclosures.npz'][h+'_'+m+'_'+side]=[48,36,3]
    return a
def prepare(out):
    seed=module('seed_reservation',REVIEW/'SEED_RESERVATION.py');bank,values=seed.derive_bank();close(bank,read(out/'SEEDS.json'));require(sha(out/'SEEDS.json')=='6834495ff9525445714befbd6d0d35126aa1dd108604d79a870cb241d2169428','Seed hash')
    exports=[dict(path=p,ref=ref,content=subprocess.check_output(['git','show',ref+':'+p]).decode()) for p,(ref,h) in seed.EXPECTED_SOURCES.items()]
    atomic(out/'SEED_SOURCE_EXPORT.json',exports);audit=seed.validate_sources(out/'SEED_SOURCE_EXPORT.json',values);atomic(out/'SEED_AUDIT.json',audit)
    ver=['source_freeze','inference','historical_preservation']
    for w in WORLDS:ver+=ids(w)+[w+'/'+n for n in ('archives','views','evidence','predictions_donor','scores','hashes_after')]
    atomic(out/'EXPECTED.json',dict(attempt_ids=[i for w in WORLDS for i in ids(w)],wrapper_ids=[f'{w}/{h}/{n}' for w in WORLDS for h in HIST for n in HEADS],archives=archive_shapes(),verifier_ids=ver,counts=dict(worlds=82,shared=246,personal=31488,wrappers=656,probabilities=2788,logs=328)))
    atomic(out/'ENVIRONMENT.json',dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,psutil=psutil.__version__,platform=platform.platform(),threads=1))
    lines=subprocess.check_output(['git','ls-tree','-r',ASSIGNMENT,'labs','research/decision_functions_2026-11-24/runs'],text=True).splitlines();hist={line.split('\t')[1]:line.split()[2] for line in lines if line.split()[1]=='blob'};atomic(out/'HISTORICAL_BLOBS.json',hist)
    bindings={}
    for name,path,ref in [('head.py','labs/decision_functions_evidence_shrinkage_v1/head.py','f18255c5fad37f704881ff1f9ad50cd113497236'),('evidence.py','labs/decision_functions_evidence_shrinkage_v1/evidence.py','f18255c5fad37f704881ff1f9ad50cd113497236'),('objective.py','labs/decision_functions_post_es_diagnostics_v1/objective.py','16ef28b105ff6c28ee3f822b1409f076fa895318'),('solver.py','labs/decision_functions_post_es_diagnostics_v1/solver.py','16ef28b105ff6c28ee3f822b1409f076fa895318')]:
        raw=subprocess.check_output(['git','show',ref+':'+path]);require((LAB/name).read_bytes().replace(b'\r\n',b'\n')==raw,'Copied dependency differs');bindings[name]=dict(path=path,ref=ref,sha256=digest(raw))
    atomic(out/'DEPENDENCIES.json',bindings)
def seal(out):
    require(read(out/'PREFLIGHT_FINAL.json')['passed'],'Preflight required')
    files=list(LAB.glob('*.py'))+[out/n for n in ('CONFIRMATION_PROTOCOL.md','DESIGN.json','SEEDS.json','EXPECTED.json','ENVIRONMENT.json','HISTORICAL_BLOBS.json','DEPENDENCIES.json','GENERATOR_BINDING.json','SEED_AUDIT.json','PREFLIGHT.json','PREFLIGHT_FINAL.json','SUPPLEMENTAL_PREFLIGHT.json','PLAN_CALCULATION.json','SEED_RESERVATION.json')]+[REVIEW/n for n in ('PLAN_CALCULATION.py','SEED_RESERVATION.py')]
    atomic(out/'FREEZE.json',dict(assignment=ASSIGNMENT,files={str(p.relative_to(ROOT)).replace('\\','/'):digest(p.read_bytes().replace(b'\r\n',b'\n')) for p in files},limits=dict(cpu_seconds=3600,process_tree_rss=4*1024**3),zero_confirmation_generation=True,zero_fits=True))
