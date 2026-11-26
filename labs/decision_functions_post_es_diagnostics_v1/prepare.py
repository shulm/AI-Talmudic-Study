"""Freeze source, deterministic arrays and historical byte bindings, without solving."""
from common import *
from suite import fixture
def prepare(private):
    review=ROOT/'research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26'
    for source,dest in [('next_post_es_design.json','PROTOCOL.json'),('METHOD_NOTE.md','METHOD_NOTE.md'),('ENGINEERING_SPEC.md','ENGINEERING_SPEC.md')]:
        p=OUT/dest
        with p.open('x',encoding='utf-8',newline='\n') as f:f.write((review/source).read_text())
    atomic(OUT/'FIXTURE.json',{k:v.tolist() for k,v in fixture().items()});atomic(OUT/'EXPECTED.json',expected());atomic(OUT/'ENVIRONMENT.json',environment())
    checks=read(OUT/'PREFLIGHT_01.json')
    if not checks['passed']:raise ValueError('Preflight failed')
    atomic(OUT/'DERIVATIVES.json',checks['derivatives'])
    import terminal
    atomic(OUT/'TERMINAL_TESTS.json',terminal.tests())
    public={}
    raw=subprocess.check_output(['git','ls-tree','-r','--name-only',HISTORICAL,'--','labs/decision_functions_evidence_shrinkage_v1','research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1'],cwd=ROOT,text=True)
    for p in raw.splitlines():
        pinned=git(HISTORICAL,p);h=sha(pinned)
        if sha((ROOT/p).read_bytes().replace(b'\r\n',b'\n'))!=h:raise ValueError('Historical public bytes mismatch')
        public[p]=h
    files={}
    for r in REAL:
        man=json.loads(git(HISTORICAL,(OLD/(r+'_manifest.json')).relative_to(ROOT).as_posix()))
        for p,h in man['private_files'].items():files[r+'/'+p]=h
    assert len(files)==112
    availability='AVAILABLE' if private.exists() else 'UNAVAILABLE'
    if availability=='AVAILABLE':close(hashes(private),files)
    atomic(OUT/'INPUT_BINDINGS.json',dict(historical_commit=HISTORICAL,private_root=str(private),availability=availability,private_files=files,public_files=public))
    raw=subprocess.check_output(['git','ls-tree','-r',BASE,'--','labs','research/decision_functions_2026-11-24/runs'],cwd=ROOT,text=True)
    atomic(OUT/'HISTORICAL_BLOBS.json',{l.split('\t')[1]:l.split()[2] for l in raw.splitlines()})
    artifacts=['PROTOCOL.json','METHOD_NOTE.md','ENGINEERING_SPEC.md','FIXTURE.json','EXPECTED.json','ENVIRONMENT.json','INPUT_BINDINGS.json','HISTORICAL_BLOBS.json','PREFLIGHT_01.json','DERIVATIVES.json','TERMINAL_TESTS.json']
    atomic(OUT/'FREEZE.json',dict(assignment=BASE,historical=HISTORICAL,source={n:digest(LAB/n) for n in NAMES},artifacts={n:digest(OUT/n) for n in artifacts},scientific_fits=0,optimizer_calls_before_freeze=0,comparison_count=len(expected()['comparison_ids'])))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);a=p.parse_args();prepare(a.private_root)
