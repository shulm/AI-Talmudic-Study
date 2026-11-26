"""Hand-authored BB-WINDOW and BB-KINYAN adjudication; immutable dependency closure."""
import copy,json,sys,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.review016')
state=r.current(a.job)
parent='f82c4e3f725e0eac9e92ce05eeb4070e085b2aa370f3e27d64445236f3c97077'
assert r.sha(r.encoded(state))==parent
root=Path(__file__).resolve().parents[7]
contract=root/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
assert hashlib.sha256(contract.read_bytes()).hexdigest()=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for path,digest in json.loads(contract.read_text())['production_files'].items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
assert hashlib.sha256(Path('F:/Sefaria-Export-master/schemas/Bava_Batra.json').read_bytes()).hexdigest()=='83a4a3dab261bad3302a89620da14e49d69a10b09b64d3c45d147d6854b837b2'
assert json.loads((a.job/'OWNER.json').read_text())==dict(owner='L04/bava_batra_resume_20261126',epoch=3)
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
obligations={}
for key,word,meaning in [('above','מלמעלה','above'),('below','מלמטה','below'),('opposite','מכנגדן','opposite')]:
    obligations[key]=a.claim(key,'2b:15',"החלונות בין מלמעלה בין מלמטה ובין מכנגדן ד' אמות",f'The quoted window rule requires a distance of four cubits {meaning} the window.',conditions=[f'adjacency {meaning} the window'],scope='One component of the anonymous quoted window-distance rule; reasons are separately linked.')
    for row in a.rows[-4:]:
        if row['layer']=='utterances':row['content']['textual_voice']='anonymous quoted Mishnah'
        if row['layer']=='attributions':row['content']['surface']='anonymous quoted Mishnah'
premise=a.claim('words_premise','3a:14','קנין דברים בעלמא הוא','An acquisition merely of the verbal division agreement does not bind the parties in the proposed case.',conditions=['courtyard lacks the required area for compulsory division','parties consent to divide','acquisition understood as only the verbal agreement'],scope='Anonymous objection premise to the unqualified acquisition answer; property-specific acquisition and possession are subsequent solutions.')
a.e('words_premise.objection',premise,'bb.alternative003.acquisition.c','objection','3a:14')
a.e('words_premise.support',premise,'bb.alternative003.words.q','support','3a:14')
a.e('directions.qualification','bb.alternative003.directions.c',premise,'qualification','3a:14')
a.e('possession.qualification','bb.alternative003.possession.c',premise,'qualification','3a:14')
a.e('below.challenge',obligations['below'],'bb.opening001.noharm.c','objection','2b:15')
a.e('below.home','bb.visual002.home.c',obligations['below'],'distinction','2b:16')
targets={'bb.visual002.windows.u','bb.visual002.windows.challenge','bb.visual002.home.distinction'}|{'bb.visual002.'+k+'.reason' for k in obligations}
def deps(row):
    c=row['content'];out=list(row['links'])
    out += [c[k] for k in ['claim_id','question_id','source_id','target_id'] if c.get(k)]
    if row['layer']=='attributions':out += [c.get('scope','').split(';')[0].strip()]
    return out
affected=set(targets)
while True:
    more={k for k,v in active.items() if any(d in affected for d in deps(v))}-affected
    if not more:break
    affected|=more
mapping={k:k+'.review016' for k in affected}
for old in sorted(affected):
    row=copy.deepcopy(active[old]);row.update(id=mapping[old],supersedes=old)
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row['links']=[mapping.get(k,k) for k in row['links']]
    for k in ['claim_id','question_id','source_id','target_id']:
        if k in row['content']:row['content'][k]=mapping.get(row['content'][k],row['content'][k])
    if row['layer']=='attributions':
        scope=row['content']['scope']
        for before,after in mapping.items():
            if scope==before or scope.startswith(before+';'):scope=after+scope[len(before):]
        row['content']['scope']=scope
    if old=='bb.visual002.windows.u':row['content']['composition']='composite'
    if old=='bb.visual002.windows.c':row['uncertainty'].append('Composite quotation retained as aggregate; the three obligations have separate claim nodes. Not an atomic training unit.')
    if old=='bb.visual002.windows.challenge':row['content']['source_id']=obligations['above']
    if old=='bb.visual002.home.distinction':row['content']['target_id']=obligations['above']
    for key in obligations:
        if old=='bb.visual002.'+key+'.reason':row['content']['target_id']=obligations[key]
    if row['layer']=='edges':row['links']=[row['content']['source_id'],row['content']['target_id']]
    a.rows.append(row)
remaining=[v for k,v in active.items() if k not in affected]+a.rows
touched={e['segment_id'] for x in a.rows for e in x['evidence']}
coverage=[]
for old in state['coverage']:
    if old['segment_id'] not in touched and not any(x in affected for x in old['record_ids']):continue
    item=copy.deepcopy(old);item.pop('proposal_execution',None)
    item['record_ids']=[x['id'] for x in remaining if x['layer']==item['layer'] and any(e['segment_id']==item['segment_id'] for e in x['evidence'])]
    item['extraction_result']='records_found' if item['record_ids'] else 'none_found_after_pass'
    item['rationale']+=' Source reread for independent BB-WINDOW/BB-KINYAN: separate three obligations and reasons; privacy argument excludes light obstruction; extract scoped verbal-acquisition objection premise. Preserve source attribution at3a:17.'
    coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/bava_batra_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/bava_batra_review_repair',model_id=None),records=a.rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'review016.json';r.immutable(out,r.encoded(p));print(out);print('new',len(a.rows),'superseded',len(affected))
