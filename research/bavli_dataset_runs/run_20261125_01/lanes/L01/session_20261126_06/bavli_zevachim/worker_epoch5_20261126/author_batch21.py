import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b21.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='57967a81f4896cafbbb36001920a77d66a8aba0077c5950285cd77099883f1d6'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','19a:12','Rava','Does wind entering the garment invalidate flesh contact, or is this normal wearing?','queried',['Wind between garment and flesh'],'Unresolved alternatives'),
('2','19a:13','continuing inquiry','Does a louse interpose?','queried',['Louse between garment and flesh'],'Specified next as live louse'),
('3','19a:14','anonymous','A dead louse certainly interposes.','asserted',['Dead louse'],'Settled baseline'),
('4','19a:14','continuing inquiry','Does a live louse interpose: is its movement natural growth, or does objection to it make it interpose?','queried',['Live louse'],'Unresolved alternatives'),
('5','19a:15','anonymous','Earth certainly interposes.','asserted',['Earth between flesh and garment'],'Settled baseline'),
('6','19a:15','continuing inquiry','Does fine earth dust interpose?','queried',['Fine dust'],'Unresolved specific case'),
('7','19a:16','continuing inquiry','Does armpit space interpose, or is this normal wearing despite lack of flesh contact?','queried',['Armpit space'],'Unresolved alternatives'),
('8','19a:17','continuing inquiry','Does placing his own hand inside his garment create an interposition by his own body?','queried',['Own hand inside garment'],'Unresolved'),
('9','19a:18','anonymous','An obstructing hair certainly interposes.','asserted',['Hair'],'Settled baseline'),
('10','19a:18','continuing inquiry','Does a dangling hair interpose?','queried',['Dangling hair'],'Unresolved specified case'),
('11','19a:19','Mar bar Rav Ashi','If his hair protrudes through the garment, is it like his body or not?','queried',['Hair protruding through garment'],'Unresolved classification'),
('12','19a:20','Rabbi Zeira','Do tefillin interpose?','queried',['Priestly service; tefillin'],'Qualified by nighttime-tefillin dispute'),
('13','19a:20','Rabbi Zeira inquiry','For the view that night is not tefillin time, they interpose by day too because they interpose at night.','conditional',['View night not tefillin time'],'Premise within inquiry; later arm/head distinction retained'),
('14','19a:20','Rabbi Zeira','For the view that night is tefillin time, does a bodily commandment interpose?','queried',['View night is tefillin time'],'Specific question before reply'),
('15','19a:21','Rabbi Ami','We have an established teaching that tefillin interpose.','asserted',['Report reaching Rabbi Ami'],'Qualified later as arm tefillin'),
('16','19a:22','anonymous','Does exemption imply that if worn tefillin do not interpose?','hypothetical',['Inferring permission from exemption wording'],'Rejected inference'),
('17','19a:22','anonymous','No; if worn they interpose.','asserted',['Priestly service; arm tefillin as later distinguished'],'Reply'),
('18','19a:23','anonymous','Then why say exempt instead of prohibited?','queried',['Exemption wording vs priestly interposition'],'Objection'),
('19','19a:23','anonymous','Because Levites and Israelites are included and cannot be described as prohibited, the teacher says exempt.','asserted',['Mixed list including nonpriestly roles'],'Wording explanation'),
('20','19a:24','quoted baraita','If tefillin are worn, they do not interpose.','asserted',['Qualified by following reply as head tefillin'],'Second baraita challenge'),
('21','19a:24','anonymous','Arm tefillin interpose.','asserted',['Arm tefillin'],'Resolves contradiction'),
('22','19a:24','anonymous','Head tefillin do not interpose.','asserted',['Head tefillin in exposed space between frontplate and turban'],'Resolution including continuation'),
('23','19a:25','anonymous','Arm tefillin are excluded by requiring the garment on the flesh with nothing intervening.','asserted',['Leviticus6:3; garment and flesh'],'Reason'),
('24','19a:25','anonymous','But the turban is also commanded upon his head.','queried',['Exodus29:6; objection to head tefillin'],'Question on distinction'),
('25','19a:26,19b:1','quoted teaching','Hair was visible between frontplate and turban, and tefillin were placed there.','asserted',['Exposed head space; no turban interposition'],'Full continuation across folio')]
for k,role in [('priest','Priests performing service'),('levite','Levites on platform'),('israel','Israelites at watches')]:
 for duty in ['prayer','tefillin']:D.append((k+duty,'19a:22','quoted baraita',role+' are exempt from '+duty+'.','asserted',[role,duty],'Distinct exemption outcome'))
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Unresolved interposition inquiries and tefillin arm/head resolution',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='none' if k in ['1','2','4','6','7','8','10','11'] else 'partial'),['u'+k])
 if mode not in ['queried','hypothetical']:rec('p'+k,'positions',refs,dict(holder_candidates=['Rabbi Ami'] if k=='15' else [],claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,ref,surface,links in [('rava','19a:12','Rava',['c1']),('mar','19a:19','Mar bar Rav Ashi',['c11']),('zeira','19a:20','Rabbi Zeira',['c12','c13','c14']),('ami','19a:21','Rabbi Ami',['c15'])]:rec('a'+k,'attributions',[ref],dict(surface=surface,role='speaker',candidates=[surface],scope='Explicit named inquiry or reply; unnamed continuation not forced into new named attribution',transmission_chain=[]),links)
for a,b,rel in [('3','2','qualification'),('4','2','qualification'),('5','6','distinction'),('9','10','distinction'),('13','12','qualification'),('14','12','qualification'),('15','14','answer'),('16','15','objection'),('17','16','answer'),('18','17','objection'),('19','18','answer'),('20','17','objection'),('21','15','qualification'),('22','20','qualification'),('23','21','support'),('24','22','objection'),('25','24','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['19a:'+str(i) for i in range(12,27)]+['19b:1']
rec('s1','structure',refs[:8],dict(title='Unresolved interposition inquiries with settled baseline cases',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[8:],dict(title='Tefillin interposition resolved by arm/head distinction and exposed head space',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through19b1 full head-tefillin continuation and next19b2 topic. Leave unanswered physical-interposition cases unresolved, preserve conditional nighttime premise, separate six exemption outcomes and final arm/head resolution.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding; unanswered inquiry is not a settled position.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_19a12_19b1.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch21.json',r.encoded(res));print(res)
