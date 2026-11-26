import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b5.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['10b:32'],'רבי עקיבא','quoted_rule','All blood brought into the Sanctuary to atone is invalid according to Rabbi Akiva.','asserted',['Blood brought into Sanctuary for atonement'],'Quoted general invalidity'),
('2',['10b:32'],'חכמים','quoted_rule','The sages restrict this invalidity to sin-offering blood.','asserted',['Blood brought into Sanctuary for atonement; sin offering only'],'Quoted restricted invalidity'),
('3',['10b:32'],'רבי אליעזר','quoted_rule','Rabbi Eliezer also includes guilt-offering blood, from כחטאת כאשם.','asserted',['Guilt-offering blood brought into Sanctuary for atonement'],'Quoted additional category'),
('4',['10b:33'],'anonymous','question','Rabbi Eliezer\'s reason is stated; what is the sages\' reason?','queried',['Sages exclude guilt offering from invalidity'],'Question on sages\' source'),
('5',['10b:34','11a:1'],'רבא','a_fortiori','The guilt offering cannot be invalidated by bringing its blood inside: wholly burned burnt offering remains valid in that case, all the more a guilt offering not wholly burned.','asserted',['Blood brought inside; burnt/guilt comparison'],'Initial proof challenged below'),
('6',['11a:2'],'anonymous','objection','The burnt offering differs because it does not atone as described here.','challenged',['Burnt-offering premise'],'Distinguishing feature'),
('7',['11a:3'],'anonymous','counterexample','The sinner\'s meal offering provides the counterexample.','asserted',['Atoning sinner\'s meal offering'],'Response to lack-of-atonement distinction'),
('8',['11a:4'],'anonymous','question_answer','Why not use bird sin offering? Its inward-blood case is Rabbi Avin\'s unresolved inquiry.','unresolved',['Bird sin offering blood taken inside'],'Unavailable settled counterexample'),
('9',['11a:5'],'anonymous','objection','The sinner\'s meal offering is not a slaughtered animal offering.','challenged',['Meal offering versus animal offering'],'Counterexample distinguished'),
('10',['11a:6'],'anonymous','common_factor','Burnt and sinner\'s meal offerings share most-holy status and remain valid when their pertinent material enters inside; infer guilt offering too remains valid.','asserted',['Most-holy combined comparison; inward entry'],'Proposed common-factor proof'),
('11',['11a:7'],'רבא מברניש','objection','The two examples lack fixed monetary valuation, unlike the guilt offering.','challenged',['Common-factor comparison; guilt fixed amount'],'Rava of Barnish addresses Rav Ashi'),
('12',['11a:8'],'anonymous','replacement_derivation','The sages instead derive from דמה: blood of this offering, not another.','asserted',['Sin-offering-specific blood exclusion'],'Replacement proof'),
('13',['11a:9'],'anonymous other side','interpretation','The other side reads דמה as blood, not flesh.','asserted',['Alternative use of same word'],'Unnamed side retained'),
('14',['11a:10'],'anonymous other side','reply','The reply draws meaning from the additional form דם דמה.','asserted',['Extra possessive form'],'Unnamed side retained'),
('15',['11a:11'],'anonymous other side','reply','The other side does not expound דם דמה.','asserted',['Rejection of additional possessive inference'],'Unnamed side retained'),
('16',['11a:12'],'anonymous','framing','For the sages who validate wrong-purpose guilt offering, the separate meal-offering comparisons to sin and guilt offerings are understandable.','asserted',['Sages\' guilt-offering view'],'Transition to use of juxtaposition'),
('17',['11a:13'],'רבי שמעון','quoted_rule','The sinner\'s meal offering is like a sin offering, so a handful taken not for its purpose is invalid.','asserted',['Sinner\'s meal offering; wrong-purpose handful'],'Quoted rule'),
('18',['11a:13'],'רבי שמעון','quoted_rule','The voluntary meal offering is like a guilt offering, so a handful taken not for its purpose is valid.','asserted',['Voluntary meal offering; wrong-purpose handful'],'Quoted rule'),
('19',['11a:14'],'anonymous','question','For Rabbi Eliezer, what is the purpose of comparing the meal offering separately to sin and guilt offerings?','queried',['Rabbi Eliezer invalidates wrong-purpose guilt offering'],'Question about apparent redundant comparison'),
('20',['11a:15'],'anonymous','answer','It is used for the other Rabbi Shimon teaching about service without a sacred vessel.','asserted',['Alternative purpose of juxtaposition'],'Answer using another teaching'),
('21',['11a:15'],'anonymous Mishnah','quoted_rule','Service without a sacred vessel is invalid in the anonymous Mishnah.','asserted',['Meal-offering service without sacred vessel'],'Quoted anonymous view'),
('22',['11a:15'],'רבי שמעון','quoted_rule','Rabbi Shimon validates service without a sacred vessel.','asserted',['Meal-offering service without sacred vessel'],'Quoted dissent'),
('23',['11a:16'],'רב יהודה בריה דרבי חייא','explanation','If performed by hand it is performed with the right hand like a sin offering.','asserted',['Rabbi Shimon interpretation; by hand'],'Explanation of Rabbi Shimon, not independent new dissent'),
('24',['11a:16'],'רב יהודה בריה דרבי חייא','explanation','If performed in a vessel it can be performed with the left hand like a guilt offering.','asserted',['Rabbi Shimon interpretation; using vessel'],'Alternative performance condition'),
('25',['11a:17'],'anonymous','question','Does Rabbi Shimon use this same verse for both teachings?','queried',['Two uses of same juxtaposition verse'],'Apparent competing derivations'),
('26',['11a:18'],'anonymous','answer','The verse primarily serves Rav Yehuda son of Rabbi Hiyya\'s explanation of performance.','asserted',['Allocation of juxtaposition verse'],'Primary use assigned'),
('27',['11a:18'],'anonymous','answer','Wrong-purpose sinner\'s meal offering is invalid because it too contains היא, as does the sin offering.','asserted',['Sinner\'s meal offering; wrong-purpose handful'],'Separate source for invalidity'),
('28',['11a:19'],'anonymous','question_answer','For the sages, the guilt/sin juxtaposition teaches that a guilt offering requires laying on hands like a sin offering.','asserted',['Guilt offering; laying on hands; sages\' reading'],'Local alternative use of juxtaposition')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['Source parenthetical דמן retained; meal offering has no animal blood, so comparison paraphrase describes pertinent material rather than asserting meal-offering blood.'] if key=='10' else []
 if key=='27':unc=['Bracketed טעמא אחרינא הוא retained in evidence.']
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['5','8','10','28'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Inward-entry invalidity and sin/guilt/meal-offering juxtaposition',assertion_mode=mode),['u'+key],unc)
 if mode=='queried' or key in ['8','28']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key],unc)
 if mode!='queried':
  holder=[] if voice.startswith('anonymous') else [voice]
  if key in ['23','24']:holder=['רבי שמעון']
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if not voice.startswith('anonymous'):rec('a'+key,'attributions',refs,dict(surface=voice,role='collective' if voice=='חכמים' else 'speaker',candidates=[voice],scope='Local '+role,transmission_chain=[]),['c'+key])
rec('a8','attributions',['11a:4'],dict(surface='רבי אבין',role='quoted_authority',candidates=['רבי אבין'],scope='Bird sin-offering inward-blood inquiry',transmission_chain=[]),['c8'])
for a,b,rel in [('5','4','answer'),('6','5','objection'),('7','6','answer'),('8','7','qualification'),('9','7','objection'),('10','9','answer'),('11','10','objection'),('12','4','answer'),('13','12','objection'),('14','13','answer'),('15','14','objection'),('17','16','support'),('18','16','support'),('20','19','answer'),('23','22','support'),('24','22','support'),('25','20','objection'),('26','25','answer'),('27','17','support')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['10b:'+str(i) for i in range(32,35)]+['11a:'+str(i) for i in range(1,20)]
rec('s1','structure',refs[:14],dict(title='Blood brought inward: Akiva, sages and Eliezer; failed analogy and exclusive pronoun',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[14:],dict(title='Meal-offering comparisons: wrong purpose, hand/vessel service, laying on hands',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through11a19 and following11a20 heading. Preserve three inward-blood views, unresolved bird case, unnamed other-side replies, performance hand/vessel conditions, separate meal-offering validity outcomes and source-use reconciliation.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' finding; discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_10b32_11a19.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch5.json',r.encoded(res));print(res)
