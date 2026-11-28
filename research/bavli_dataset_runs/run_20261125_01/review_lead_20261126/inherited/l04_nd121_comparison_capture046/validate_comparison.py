from pathlib import Path
import json,hashlib,sys,importlib.util,datetime
sys.dont_write_bytecode=True
O=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated118/comparisons'); R=O.parent
B=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research')
H='b6421aabe6cab3ce7d705b4e1dd71fa6f1dab74a7a6122db508b95ce954e8b74'
P=B/'bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/packages/nedarim'/H
J=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_nedarim_delegated118.json')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def module(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def validate():
 pins={'reading.json':'63bd309b1650a8accb9a7f0bee4e4c58e0ea0521342676a7fef9ee5c8df96714','exposure.json':'f1e9f2a8472029d53587c9fd4cbe568d65c961a05a59dec51ac2267ae22d0af7','build_reading.py':'0010b8eeeff39f8268936e0693cbf7a0a7a9b5904c16eb192bd9230da1278dcd'}
 for n,h in pins.items():assert sha(R/n)==h
 assert sha(J)=='8f07dcf5fef312f9054fb9c4937879a1375ce65fb3e7362fb77651a967cd68a1'
 job=read(J)
 for d in [job['source'],job['original_source_schema'],job['frozen_plan']]+job['common_documents']:assert sha(Path(d['path']))==d['sha256']
 for n,h in read(P/'PACKAGE.json')['files'].items():assert sha(P/n)==h,n
 rr=module(R/'build_reading.py','reader');counts=rr.validate(read(R/'reading.json'))
 run=module(B/'bavli_production_v1/runner.py','runner');j,ss=run.load(P/'job');accepted=read(P/'job/snapshots'/f'{H}.json');assert sha(P/'job/snapshots'/f'{H}.json')==H
 state=run.empty()
 for h in accepted['proposals']:
  p=P/'job/proposals'/f'{h}.json';assert sha(p)==h
  prior=state['proposals'];state=run.validate_apply(state,read(p),ss,j);state['proposals']=prior+[h]
 assert run.encoded(state)==run.encoded(accepted)
 return dict(status='PASS',at=datetime.datetime.now(datetime.timezone.utc).isoformat(),snapshot=H,accepted_proposals=len(accepted['proposals']),package_file_count=len(read(P/'PACKAGE.json')['files']),reader_counts=counts,source_segments=len(ss),production_adapter_compatible=False,method='Direct exact snapshot accepted-prefix validate_apply; no CURRENT lookup or writes to inputs'),ss,accepted
if __name__=='__main__':
 result,ss,s=validate();print(json.dumps(result))
 if '--receipt' in sys.argv:
  p=O/'presemantic_validation.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 if '--dump' in sys.argv:
  exp=read(R/'exposure.json');reader=read(R/'reading.json'); lines=[]
  for ref in exp['fully_reviewed_core_refs']+exp['fully_reviewed_context_refs']:
   sid=next(k for k,v in ss.items() if v['ref']==ref);lines+=['\n## '+ref,ss[sid]['text']]
   for label,rows,key in [('READER',reader['records'],ref),('PRODUCER',s['records'],sid)]:
    lines.append(label)
    for r in rows:
     if r['release_state']=='valid' and any(e['segment_id']==key for e in r['evidence']):lines.append(json.dumps(r,ensure_ascii=False))
  (O/'comparison_evidence.txt').write_text('\n'.join(lines),encoding='utf-8')
