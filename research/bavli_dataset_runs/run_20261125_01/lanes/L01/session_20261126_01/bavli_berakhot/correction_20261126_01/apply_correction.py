"""Manually adjudicated review corrections; deterministic serialization only."""
from pathlib import Path
import copy, sys
sys.path.insert(0, r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE = Path(__file__).resolve().parent
JOB = HERE.parent
BASE = '03622eb5170ef5507fa5846f93156fe872c2bd99f326f7d6c7641ade69050f1e'
meta, segments = r.load(JOB)
state = r.read(JOB/'snapshots'/f'{BASE}.json')
assert r.sha(r.encoded(state)) == BASE
review_root = Path(r'C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
review_hashes = {
 'readings/berakhot_batch001.json':'583a9532d6b54631eafbe19fd941281d222e1fa43089537645fa7c95ad3436fb',
 'comparisons/berakhot_03622eb5_batch001.json':'51067df028d991c8750c6e08387174dba22d930e10e73c827591c64edcd07ade',
 'verdicts/berakhot_03622eb5.json':'06feae36bdb143d6d6f5d229c0307852edf78686569c05c4c02108ae5e45a132'}
for path,h in review_hashes.items(): assert r.sha((review_root/path).read_bytes()) == h
active = {x['id']:x for x in state['records'] if x['release_state']=='valid'}
ids = ['bk.opening.pass1.c.duty','bk.opening.pass1.p.duty',
       'bk.opening.pass1.answer','bk.opening.pass1.general',
       'bk.watch_dispute.20261125.p10n','bk.watch_dispute.20261125.p10r',
       'bk.watch_dispute.20261125.e15','bk.watch_dispute.20261125.e16']
mapping = {old:old+'.review20261126' for old in ids}
def replace_ids(value):
    if isinstance(value,str): return mapping.get(value,value)
    if isinstance(value,list): return [replace_ids(x) for x in value]
    if isinstance(value,dict): return {k:replace_ids(v) for k,v in value.items()}
    return value
records=[]
for old in ids:
    x=copy.deepcopy(active[old])
    for key in ['ml_eligible','release_state','review_state','supersedes']: x.pop(key,None)
    x=replace_ids(x); x['supersedes']=old
    if old in ids[:2]:
        x['content']['conditions']=['The sons have not yet recited Shema','Dawn has not risen']
        if x['layer']=='claims': x['content']['proposition']='The sons, who have not yet recited Shema, remain obligated to recite if dawn has not risen.'
        sid='seg_60ee4773ccee2b2b063e'; t=segments[sid]['text']; quote='לא קרינו את שמע'
        start=t.index(quote)
        x['evidence'].append(dict(segment_id=sid,start_char=start,end_char=start+len(quote),quote=quote))
    if old in ids[4:6]:
        x['content']['question_id']=None
        x['links']=[x['content']['claim_id']]
        x['uncertainty'].append('BR-QUESTION-002: prior why-question link can represent discourse association, but is not a common comparable count-answer set. Null question_id avoids that conflation; no editorial count question is asserted here.')
    if old in ids[6:]:
        x['uncertainty'].append('BR-EDGE-003: objection to the four-watch inference and qualification of the verse interpretation are supported relation-label alternatives. Objection retained provisionally; no exact-label agreement or demanding edge-label eligibility before adjudication.')
    records.append(x)
coverage=[]
for c in state['coverage']:
    if any(x in mapping for x in c['record_ids']):
        c=copy.deepcopy(c); c.pop('proposal_execution',None)
        c['record_ids']=[mapping.get(x,x) for x in c['record_ids']]
        c['rationale']+=' Versioned review correction 20261126: explicit non-recitation condition, null count-position why-question links, and retained edge-label alternatives; original source and pass scope preserved.'
        coverage.append(c)
p=dict(schema_version=r.VERSION,tractate=meta['tractate'],owner='/root/l01_berakhot_correction',epoch=4,
       execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=state['open_tails'],
       **{k:meta[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,segments,meta)
r.immutable(HERE/'proposal.json',r.encoded(p))
cur=r.current(JOB)
assert r.sha(r.encoded(cur))==BASE or r.sha(r.encoded(p)) in cur['proposals'], 'Concurrent checkpoint changed'
result=r.submit(JOB,HERE/'proposal.json',p['owner'],p['epoch'])
r.immutable(HERE/'submit_receipt.json',r.encoded(result))
replay=r.replay(JOB); r.immutable(HERE/'replay.json',r.encoded(replay))
new=r.current(JOB)
assert all(c['content']['conditions']==['The sons have not yet recited Shema','Dawn has not risen'] for c in new['records'] if c['id'] in [mapping[x] for x in ids[:2]])
assert r.report(new,segments)['completed_by_layer']==r.report(state,segments)['completed_by_layer']
r.immutable(HERE/'resolution.json',r.encoded(dict(base_snapshot_sha256=BASE,new_snapshot_sha256=r.sha(r.encoded(new)),review_hashes=review_hashes,revision_mapping=mapping,
  findings={'BR-COND-001':'Corrected two structured conditions and evidence; dependent attribution/edge versioned.', 'BR-QUESTION-002':'Null links chosen; prior discourse-association alternative preserved in originals and uncertainty.', 'BR-EDGE-003':'Both supported labels preserved as uncertainty; no claim of confirmed initial error.'},
  scope='Eight revised records; no additional extracted source segments; independent recheck of corrected snapshot pending.',
  full_tractate_review_complete=False,human_certification=False,ml_eligible=False)))
print(r.encoded(result).decode())
