"""Adjudicate frozen TF findings, preserve original versions and dependency closure."""
import copy,json,pathlib,re,sys
ROOT=pathlib.Path(__file__).resolve().parents[7];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit');j,ss=runner.load(JOB);S=runner.current(JOB)
BASE='c6590d89ec3e48fd4a2d4f9f97861045a5a45f4e57220ba657dce73e73721378'
assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']==BASE
comp=JOB.parent/'review_20261126_resume/taanit_frozen_comparison/comparison.json';assert runner.sha(comp.read_bytes())=='f78d0ef730548b3bf0c9f2453c5a980041a772dcf8a76b8789a9fe8e9f49ee4d'
active={r['id']:r for r in S['records'] if r['release_state']=='valid'};ix={s['ref'].replace('Taanit ',''):s for s in ss.values()}
def ev(ref,t=None):
 s=ix[ref];t=s['text'] if t is None else t;a=s['text'].index(t);return dict(segment_id=s['id'],start_char=a,end_char=a+len(t),quote=t)
changed={}
def edit(rid):
 if rid not in changed:changed[rid]={k:copy.deepcopy(v) for k,v in active[rid].items() if k not in ['review_state','release_state','ml_eligible']}
 return changed[rid]
def group(base):return [rid for rid in active if rid==base or rid in [base+'.a',base+'.p',base+'.u']]
for base in ['ta.resume001.yehuda.bet.reject','ta.resume002.dispersion.reject']:
 edit(base)['content']['assertion_mode']='asserted'
 edit(base+'.p')['content']['local_status']='Accepted local rejection of the proposed interpretation/identity; the negative conclusion itself is asserted.'
 edit(base+'.u')['content']['discourse_role']='asserted rejection conclusion'
 for rid in group(base):edit(rid)['uncertainty'].append('TF-STATUS correction: distinguish rejected proposal from accepted metaclaim rejecting it; prior polarity preserved in superseded record.')
for rid in group('ta.resume002.israel.winds'):
 edit(rid)['uncertainty'].append('TF-ATTR-01 unresolved source-attribution disagreement: producer reads anonymous dialectical continuation; frozen independent reader inherits Rabbi Yehoshua ben Levi from verse introduction. Neither unique attribution is certified.')
edit('ta.resume002.israel.winds.u')['content']['textual_voice']='anonymous continuation, possibly continuing Rabbi Yehoshua ben Levi; unresolved'
for rid in group('ta.resume002.mist.seed'):
 edit(rid)['uncertainty'].append('TF-ATTR-02: Rava attribution is an editorial inheritance inference from 3b:13, not a name repeated at this clause. Anonymous continuation remains possible; named attribution not independently resolved.')
edit('ta.resume002.mist.seed.a')['origin']='editorial_inference'
edit('ta.resume002.mist.seed.u')['content']['textual_voice']='likely continuing Rava, possibly anonymous; unresolved'
edit('ta.resume004.fire.water.worship')['content']['proposition']='The cited teaching depicts כותיים (as printed) worshipping fire and קדריים worshipping water; despite knowing water extinguishes fire they do not exchange gods, unlike Israel’s exchange.'
for rid in group('ta.resume004.fire.water.worship'):edit(rid)['uncertainty'].append('TF-TEXT-01: printed כותיים retained; not silently identified with preceding verse’s כתיים or normalized to Kittites.')
for rid in ['ta.resume002.negative.wind.dew','ta.resume002.negative.wind.dew.p']:edit(rid)['content']['conditions']=['rainy season','said מעביר הרוח ומפריח הטל']
edit('ta.resume002.negative.wind.dew')['content']['proposition']='In the rainy season, even saying מעביר הרוח ומפריח הטל does not require restarting.'
edit('ta.resume002.excluded.weather')['content']['proposition']='The exclusions are גילהי דליליא and שמשא דביני קרחי, retaining the source terms.'
edit('ta.resume008.nemushot.yohanan')['content']['proposition']='Rabbi Yohanan identifies נמושות as סבי דאזלי אתיגרא (elderly people who go אתיגרא).'
for base,note in [('ta.resume002.excluded.weather','Earlier English glosses night brightness / cloud breaks are provisional editorial glosses, not independently lexically verified.'),('ta.resume008.nemushot.yohanan','Earlier English gloss walking with support is editorial and unverified; אתיגרא retained for lexical review.')]:
 for rid in group(base):edit(rid)['uncertainty'].append('TF-GLOSS-01: '+note+' No demanding lexical QA qualification is claimed.')
# Exact primary partition: weather and its lexical question end immediately before ואמר רבא.
cut=ix['4a:1']['text'].index('ואמר רבא')
w=edit('ta.resume002.structure.weather.effects');w['evidence'].append(ev('4a:1',ix['4a:1']['text'][:cut]))
sch=edit('ta.resume002.structure.scholar');sch['evidence']=[ev('4a:1',ix['4a:1']['text'][cut:]) if x['segment_id']==ix['4a:1']['id'] else x for x in sch['evidence']];sch['content']['title']='Scholar likened to a seed; anger qualified by calm'
for rid in ['ta.resume002.structure.weather.effects','ta.resume002.structure.scholar']:edit(rid)['uncertainty'].append('TF-BOUNDARY-01: primary ownership partition moved to explicit ואמר רבא transition inside 4a:1; old coarse partition preserved.')
newedges=[]
def edge(key,refs,a,b,explicitness,note):
 newedges.append(dict(id='ta.review013.'+key,layer='edges',evidence=[ev(x) for x in refs],content=dict(source_id=a,target_id=b,relation='support',explicitness=explicitness),origin='source_paraphrase' if explicitness=='source_explicit' else 'editorial_inference',uncertainty=[note],links=[a,b]))
edge('dew.restoration.support',['3a:14','3b:1'],'ta.resume002.rain.restore','ta.resume002.dew.notwithheld','source_explicit','TF-EDGE-01: this evidence supports the dew component only; wind has its own proof. Existing question-mediated relation retained.')
edge('aging.dilemma.support',['5b:4','5b:5','5b:6'],'ta.resume004.dilemma.conditions','ta.resume004.aging.sudden','editorial_reconstruction','TF-EDGE-02: direct explanatory summary of the existing dilemma/solution path; independent granularity disagreement preserved, not counted as an omitted narrative claim.')
# Close over exact ID tokens in every active content field, including scope strings before semicolons.
def strings(x):
 if isinstance(x,str):yield x
 elif isinstance(x,list):
  for v in x:yield from strings(v)
 elif isinstance(x,dict):
  for v in x.values():yield from strings(v)
def regex(ids):return re.compile(r'(?<![A-Za-z0-9_.:-])(?:'+'|'.join(re.escape(i) for i in sorted(ids,key=len,reverse=True))+r')(?![A-Za-z0-9_.:-])')
while True:
 pat=regex(changed);more=[rid for rid,r in active.items() if rid not in changed and any(pat.search(t) for t in strings([r['links'],r['content']]))]
 if not more:break
 for rid in more:edit(rid)
mapping={rid:rid+'.tf013' for rid in changed};pat=regex(mapping)
def replace(x):
 if isinstance(x,str):return pat.sub(lambda m:mapping[m.group()],x)
 if isinstance(x,list):return [replace(v) for v in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
records=[]
for rid,r in changed.items():
 r['id']=mapping[rid];r['supersedes']=rid;r['content']=replace(r['content']);r['links']=replace(r['links']);records.append(r)
for r in newedges:r['content']=replace(r['content']);r['links']=replace(r['links']);records.append(r)
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_2',model_id=None),records=records,coverage=[],open_tails=replace(S['open_tails']))
# Refresh existing coverage only. No source completion count is added by correction.
for cov in S['coverage']:
 affected=any(rid in mapping for rid in cov['record_ids']) or any(r['layer']==cov['layer'] and any(e['segment_id']==cov['segment_id'] for e in r['evidence']) for r in records)
 if not affected:continue
 cc={k:copy.deepcopy(v) for k,v in cov.items() if k!='proposal_execution'};cc['record_ids']=replace(cc['record_ids'])
 for r in records:
  if r['layer']==cc['layer'] and any(e['segment_id']==cc['segment_id'] for e in r['evidence']) and r['id'] not in cc['record_ids']:cc['record_ids'].append(r['id'])
 if cc['record_ids']:cc['extraction_result']='records_found'
 cc['rationale']+=' TF review correction013: source reread, field adjudication and dependency/partition closure; coverage denominator unchanged.';P['coverage'].append(cc)
N=runner.validate_apply(S,P,ss,j)
assert runner.report(S,ss)['completed_by_layer']==runner.report(N,ss)['completed_by_layer']
for r in N['records']:
 if r['release_state']=='valid':assert not any(pat.search(t) for t in strings([r['links'],r['content']])),r['id']
decisions=[
 ('TF-STATUS-01','corrected','Negative identity conclusion asserted; proposed identity rejected, not the metaclaim.'),
 ('TF-STATUS-02','corrected','Negative interpretation conclusion asserted; rejection polarity no longer inverted.'),
 ('TF-ATTR-01','unresolved_disagreement_preserved','Both anonymous and inherited Yehoshua ben Levi readings recorded. No unique attribution qualification.'),
 ('TF-ATTR-02','uncertainty_added','Rava remains a candidate by inheritance only; anonymous continuation possible.'),
 ('TF-TEXT-01','corrected','Exact ethnonym כותיים retained, no silent harmonization.'),
 ('TF-COND-01','corrected','Rainy-season condition restored to claim and position.'),
 ('TF-GLOSS-01','unresolved_gloss_preserved','Canonical terms restored; English glosses explicitly editorial/unverified.'),
 ('TF-EDGE-01','added_scoped_direct_support','Restoration omission supports dew component of joint claim; prior question path preserved.'),
 ('TF-EDGE-02','added_editorial_summary_edge','Narrative contains reason already; added direct summary edge preserves independent granularity finding.'),
 ('TF-BOUNDARY-01','corrected','Exact nonoverlapping 4a:1 split before ואמר רבא moves preceding weather/lexical text to weather unit.')]
out=JOB/'staging_resume_20261126'/'review_correction013.json';runner.immutable(out,runner.encoded(P))
receipt=dict(status='PRODUCER_ADJUDICATION_PENDING_INDEPENDENT_RECHECK',base_snapshot_sha256=BASE,comparison_sha256=runner.sha(comp.read_bytes()),proposal_sha256=runner.sha(out.read_bytes()),proposal_path=str(out),findings=[dict(id=a,decision=b,rationale=c) for a,b,c in decisions],supersession_map=mapping,new_edge_ids=[r['id'] for r in newedges],coverage_inflation=0,all_active_pointer_fields_checked=True,independent_review_claimed=False)
runner.immutable(pathlib.Path(__file__).with_name('REVIEW_CORRECTION_013.json'),runner.encoded(receipt));print(json.dumps(dict(proposal=str(out),revised=len(mapping),new_edges=len(newedges),total_records=len(records)),indent=2))
