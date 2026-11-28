import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b10.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['13b:5'],'רבי יהודה בריה דרבי חייא','received_rule','Rabbi Yehuda son of Rabbi Hiyya reports hearing that finger dipping creates piggul in an inner sin offering.','asserted',['Inner sin offering; piggul intent during finger dipping'],'Received teaching'),
('2',['13b:6'],'אילפא','transmission_event','Ilfa heard the statement and presented it before Rav Pada.','asserted',['Transmission of finger-dipping teaching'],'Reporter distinct from response holder'),
('3',['13b:6'],'רב פדא','objection','Rav Pada argues from peace offerings: since finger dipping does not create piggul there, it should not in sin offerings either.','asserted',['Peace-offering analogy applied to sin offering'],'Contested inference'),
('4',['13b:7'],'anonymous','counterargument','An unrestricted peace-offering analogy would also leave a sin offering\'s piggul intact despite wrong-purpose intent, as in peace offerings.','hypothetical',['Wrong-purpose intent in sin offering compared with peace offering'],'Counterexample, not accepted sin-offering ruling'),
('5',['13b:8'],'anonymous','answer','Additional scriptural inclusions supply the rule rather than deriving everything from peace offerings.','asserted',['Response to unrestricted analogy'],'Inclusive-text answer; variant wording retained'),
('6',['13b:9'],'רבי יהושע בן לוי','received_rule','Rabbi Yehoshua ben Levi reports hearing in this upper room that finger dipping creates piggul.','asserted',['Finger-dipping teaching; location of received report'],'Parallel source occurrence kept separate'),
('7',['13b:9'],'ריש לקיש','objection','Resh Lakish questions it by the peace-offering analogy in which finger dipping does not create piggul.','asserted',['Peace-offering model for piggul'],'Parallel objection, not merged with Rav Pada'),
('8',['13b:10'],'anonymous','counterargument','Again, an unrestricted analogy would imply that wrong-purpose sin-offering intent does not remove piggul.','hypothetical',['Parallel counterargument to peace-offering analogy'],'Repeated occurrence preserved'),
('9',['13b:11'],'רבי יוסי ברבי חנינא','analogy','Not everything is learned from peace offerings: wrong-purpose intent invalidates sin offering, so like out-of-place intent invalidating peace offering it removes piggul.','asserted',['Invalidating wrong-purpose sin intent compared with out-of-place peace intent'],'Proposed analogy'),
('10',['13b:12'],'רבי ירמיה','objection','Out-of-place invalidity applies to all sacrifices, whereas wrong-purpose invalidity applies only to Paschal and sin offerings.','challenged',['Breadth difference in compared invalidities'],'Objection to proposed analogy'),
('11',['13b:13'],'anonymous','principle','What invalidates the offering removes it from piggul.','asserted',['Relevant offering\'s invalidating factor'],'General principle in reply'),
('12',['13b:13'],'anonymous','principle','What is indispensable for that offering can bring it to piggul.','asserted',['Indispensable service of relevant offering'],'Separate positive principle'),
('13',['13b:14'],'anonymous','application','The same offering-specific invalidating and indispensable-service principles apply here.','asserted',['Sin offering finger dipping; local application'],'Application, not independent universal expansion'),
('14',['13b:15'],'רב מרי','support_attempt','Rav Mari cites the list: taking a handful, placing it in a vessel, carrying and burning.','asserted',['Meal-offering piggul services'],'Proposed supporting parallel'),
('15',['13b:16'],'anonymous','question','Handful-taking, carrying and burning have animal-service parallels; what corresponds to placing in a vessel?','queried',['Meal-offering placement in vessel'],'Question on fourth operation'),
('16',['13b:17'],'anonymous','objection','Receiving blood happens of itself, whereas the priest actively takes and places the handful.','challenged',['Compare receiving with placing in vessel'],'Initial distinction'),
('17',['13b:18'],'anonymous','inference','Indispensable placement is an important service; likewise indispensable finger dipping is treated as carrying.','asserted',['Indispensability of placement/dipping'],'Proposed support subsequently deflected'),
('18',['13b:19'],'anonymous','rejection','Placement can still correspond to receiving: both put into a vessel, whether passive flow or active placement.','asserted',['Both are vessel placement despite different mechanics'],'Rejects necessity of proof without rejecting original dipping rule'),
('19',['13b:20'],'anonymous','question','One baraita says dipping creates piggul, another says it neither creates nor is made piggul; is this a tannaitic disagreement?','queried',['Two conflicting baraitot about finger dipping'],'Proposed disagreement'),
('20',['13b:21'],'anonymous','initial_answer','Initially the baraitot are assigned to the sages and Rabbi Shimon.','rejected',['Initial allocation of two baraitot'],'Allocation rejected by next objection'),
('21',['13b:22','14a:1'],'anonymous','objection','Rabbi Shimon denies piggul for anything not on the outer altar like peace offerings; then singling out finger dipping would be unnecessary.','challenged',['Rabbi Shimon general inner-offering rule'],'Objection to initial allocation'),
('22',['14a:2'],'anonymous','replacement_answer','Both baraitot follow the sages, distinguished by outer and inner sin offerings.','asserted',['Outer versus inner sin offerings'],'Replacement reconciliation'),
('23',['14a:3'],'anonymous','question','Outer sin offerings seem obvious, since וטבל is not written for them.','queried',['No written dipping requirement in outer sin offering'],'Question about needed teaching'),
('24',['14a:4'],'anonymous','hypothesis','Because ולקח requires the priest to take the blood again if a monkey placed it on his hand, one might treat the requirement as equivalent to וטבל.','hypothetical',['Outer sin offering; taking requirement; monkey places blood on hand'],'Rejected equivalence hypothesis'),
('25',['14a:5'],'anonymous','answer','The omission of וטבל permits either mode; it does not impose the distinct dipping requirement.','asserted',['Outer sin offering; ולקח without וטבל'],'Final textual distinction')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['Bracketed source variant preserved without harmonization.'] if key in ['5','25'] else []
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['9','13','19','24'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Finger dipping as indispensable piggul service; repeated reports and baraita reconciliation',assertion_mode=mode),['u'+key],unc)
 if mode=='queried' or key in ['4','8','10','21']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key],unc)
 if mode not in ['queried','hypothetical']:rec('p'+key,'positions',refs,dict(holder_candidates=[] if voice=='anonymous' or key=='2' else [voice],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if voice!='anonymous':rec('a'+key,'attributions',refs,dict(surface=voice,role='transmitter' if key=='2' else 'speaker',candidates=[voice],scope='Local '+role,transmission_chain=[]),['c'+key])
# Explicit outcomes from the two-baraita reconciliation, separate from attribution discourse.
for key,prop,cond in [('inner','Finger dipping creates piggul in inner sin offerings.',['Inner sin offering; sages\' baraita']),('outer','Finger dipping does not create piggul in outer sin offerings.',['Outer sin offering; sages\' baraita']),('outer_target','Finger dipping is not itself made piggul in the outer sin-offering baraita.',['Outer sin offering; second baraita formulation'])]:
 rec('c'+key,'claims',['13b:20','14a:2'],dict(proposition=prop,conditions=cond,scope='Two baraitot reconciled by inner/outer offering',assertion_mode='reconciled'))
 rec('p'+key,'positions',['13b:20','14a:2'],dict(holder_candidates=['רבנן'],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status='Local replacement reconciliation, not Rabbi Shimon assignment'),['c'+key])
for a,b,rel in [('3','1','objection'),('4','3','objection'),('5','4','answer'),('7','6','objection'),('8','7','objection'),('9','8','answer'),('10','9','objection'),('11','10','answer'),('12','10','answer'),('13','6','support'),('14','6','support'),('16','15','objection'),('17','15','answer'),('18','17','objection'),('20','19','answer'),('21','20','objection'),('22','20','correction'),('23','22','objection'),('24','23','answer'),('25','24','objection')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['13b:'+str(i) for i in range(5,23)]+['14a:'+str(i) for i in range(1,6)]
rec('s1','structure',refs,dict(title='Finger dipping: two reported debates, indispensability principle and inner/outer reconciliation',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread13b5–14a5 and next14a6 lemma. Preserve two report occurrences, failed vessel-placement proof, rejected sages/Shimon allocation and final inner/outer reconciliation; separately encode positive/negative dipping outcomes and general principle directions.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' item after inspection; anonymous discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_13b5_14a5.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch10.json',r.encoded(res));print(res)
