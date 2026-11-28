import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b12.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['14a:19'],'אביי','question','Abaye asks Rav Hisda\'s interpreter to ask Rav Hisda about carrying by a nonpriest.','queried',['Blood carrying by nonpriest'],'Question transmitted via interpreter'),
('2',['14a:20'],'רב חסדא reported','answer','Rav Hisda validates nonpriest carrying and cites priests sprinkling blood from their hands while Levites flayed.','rejected',['Blood carrying by nonpriest'],'Ruling rejected by explicit refutation at14b1'),
('3',['14a:21','14b:1'],'רב ששת quoting baraita','objection','Rav Sheshet cites invalid service by disqualified persons, including carrying, and the text marks a refutation.','asserted',['Cited receiving/carrying/sprinkling restrictions'],'Refutation of Rav Hisda'),
('4',['14b:2'],'anonymous','question','But Rav Hisda cited a verse.','queried',['Scriptural support for rejected ruling'],'Question on unused textual support'),
('5',['14b:3'],'anonymous','answer','They acted only as a platform.','asserted',['Nonpriests in Rav Hisda\'s cited verse'],'Passive support does not establish valid nonpriest carrying'),
('6',['14b:4'],'רבה ורב יוסף','interpretation','Rabbah and Rav Yosef jointly assign nonpriest carrying to the Rabbi Shimon/sages dispute.','challenged',['Whether avoidable carrying is a service'],'Joint report, not a Rabbah–Rav Yosef dispute; challenged below'),
('7',['14b:4'],'רבה ורב יוסף reporting רבי שמעון','inferred_rule','Their reading permits nonpriest carrying for Rabbi Shimon because avoidable service is not service.','challenged',['Rabbi Shimon as interpreted by Rabbah/Rav Yosef'],'Later contrary report at14b13 retained'),
('8',['14b:4'],'רבה ורב יוסף reporting רבנן','inferred_rule','Their reading invalidates nonpriest carrying for the sages.','asserted',['Sages\' carrying view in joint report'],'Contrasting attributed outcome'),
('9',['14b:5'],'אביי','objection','Slaughter cannot be avoided yet is valid by a nonpriest.','challenged',['Counterexample to indispensability implying priestly service'],'Abaye objection'),
('10',['14b:5'],'anonymous reply','answer','Slaughter is not classified as service for this argument.','asserted',['Slaughter; priestly-service classification'],'Reply, not denial that slaughter is necessary'),
('11',['14b:6'],'anonymous citing רבי זירא אמר רב','objection','Rav says slaughter of the red cow by a nonpriest is invalid, from Eleazar and statute wording.','asserted',['Red cow slaughter; nonpriest'],'Counterexample to service classification'),
('12',['14b:7'],'anonymous','distinction','The red cow differs because it has Temple-maintenance sanctity.','asserted',['Red cow category'],'Initial distinction challenged next'),
('13',['14b:8'],'anonymous','objection','If Temple-maintenance sanctity requires service, all the more altar sanctity should.','hypothetical',['A-fortiori against sanctity distinction'],'Counterargument, not final new requirement'),
('14',['14b:9'],'רב שישא בריה דרב אידי','analogy','It is like examination of skin lesions: not classified as service yet requiring priesthood.','asserted',['Priesthood requirement without service classification'],'Answers red-cow objection'),
('15',['14b:10'],'anonymous','objection','Carrying limbs to the ramp is avoidable yet invalid by a nonpriest, as והקריב הכהן describes that carrying.','asserted',['Carrying limbs to ramp; avoidable but requires priest'],'Counterexample to joint report inference'),
('16',['14b:11'],'anonymous','answer','Where Scripture disclosed a requirement it applies; where not disclosed it does not.','asserted',['Explicit priest requirement for limb carrying'],'Attempted distinction'),
('17',['14b:12'],'anonymous','objection','If limb carrying not indispensable for atonement needs a priest, all the more blood carrying indispensable for atonement.','asserted',['Blood carrying compared with limb carrying'],'A-fortiori undermines attempted distinction'),
('18',['14b:13'],'עולא אמר רבי אלעזר','reported_rule','Ulla reports Rabbi Elazar that carrying by a nonpriest is invalid even for Rabbi Shimon.','asserted',['Blood carrying by nonpriest; includes Rabbi Shimon'],'Contrary report supporting stricter outcome')]
for key,refs,voice,role,prop,mode,cond,status in D:
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['2','3','6','11'] else 'atomic'))
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Nonpriest carrying, avoidable service and priesthood requirement',assertion_mode=mode),['u'+key])
 if mode=='queried' or key in ['9','13','15','17']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 if mode not in ['queried','hypothetical']:
  holder=[] if voice.startswith('anonymous') else [voice]
  if key=='2':holder=['רב חסדא']
  if key=='7':holder=['רבי שמעון']
  if key=='8':holder=['רבנן']
  if key=='11':holder=['רב']
  if key=='18':holder=['רבי אלעזר']
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key])
# Distinct disqualifying statuses in the cited baraita, not merely a bundled list.
for key,status,refs in [('nonpriest','nonpriest',['14a:21','14b:1']),('onen','onen',['14a:21','14b:1']),('drunk','intoxicated priest',['14b:1']),('blemish','blemished priest',['14b:1']),('seated','seated performer',['14b:1']),('left','left-hand performance',['14b:1'])]:
 cond=['Receiving, carrying or sprinkling',status]
 rec('cbar_'+key,'claims',refs,dict(proposition='The cited baraita invalidates this performance.',conditions=cond,scope='Rav Sheshet\'s quoted disqualification baraita',assertion_mode='asserted'))
 rec('pbar_'+key,'positions',refs,dict(holder_candidates=['quoted baraita'],claim_id=prefix+'cbar_'+key,question_id=None,conditions=cond,local_status='Quoted counterevidence; explicit refutation'),['cbar_'+key])
for key,refs,voice,role,cand,chain,links in [('abaye',['14a:19'],'אביי','speaker',['אביי'],[],['c1']),('hisda',['14a:19','14a:20'],'רב חסדא','quoted_authority',['רב חסדא'],[],['c2']),('interpreter',['14a:19'],'אמוריה דרב חסדא','transmitter',[],[],['c1']),('sheshet',['14a:21'],'רב ששת','speaker',['רב ששת'],[],['c3']),('joint',['14b:4'],'רבה ורב יוסף דאמרי תרוייהו','collective',['רבה','רב יוסף'],[],['c6','c7','c8']),('rav',['14b:6'],'רבי זירא אמר רב','transmitter',['רבי זירא'],['רבי זירא','רב'],['c11']),('shisha',['14b:9'],'רב שישא בריה דרב אידי','speaker',['רב שישא בריה דרב אידי'],[],['c14']),('ulla',['14b:13'],'עולא א״ר אלעזר','transmitter',['עולא'],['עולא','רבי אלעזר'],['c18'])]:rec('a'+key,'attributions',refs,dict(surface=voice,role=role,candidates=cand,scope='Specified local speaker/reporting role',transmission_chain=chain),links)
for a,b,rel in [('2','1','answer'),('3','2','objection'),('4','3','objection'),('5','4','answer'),('9','7','objection'),('10','9','answer'),('11','10','objection'),('12','11','answer'),('13','12','objection'),('14','13','answer'),('15','7','objection'),('16','15','answer'),('17','16','objection'),('18','17','support')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['14a:'+str(i) for i in range(19,22)]+['14b:'+str(i) for i in range(1,14)]
rec('s1','structure',refs,dict(title='Nonpriest carrying: Rav Hisda refuted, joint Shimon attribution challenged, contrary Elazar report',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual reread through14b13 and14b14 next inquiry. Preserve Rav Hisda explicit refutation, interpreter role, Rabbah/Rav Yosef joint rather than disputed report, separate unfit categories, red-cow/lesions analogy and contrary Ulla/Elazar report.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding; source discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_14a19_14b13.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch12.json',r.encoded(res));print(res)
