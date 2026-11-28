import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b18.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='f56e4ad0cc053ffeacf758dea51364ac14a9647be41a2634ff186025bb424632'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','18a:11','anonymous baraita','Service in overlong garments is valid.','asserted',['Overlong garments'],'Literal baraita; Rav reading later construes gathered by belt'),
('2','18a:11','anonymous baraita','Service in raised garments is valid.','asserted',['Raised garments'],'Literal baraita; manner of raising distinguished later'),
('3','18a:11','anonymous baraita','Service in worn garments is valid.','asserted',['Worn garments'],'Retained validity'),
('4','18a:11,18b:1','anonymous baraita','Service wearing two pairs of trousers is invalid.','asserted',['Two pairs of trousers'],'Excess garments'),
('5','18a:11,18b:1','anonymous baraita','Service wearing two belts is invalid.','asserted',['Two belts'],'Excess garments'),
('6','18a:11,18b:1','anonymous baraita','Service missing one required garment is invalid.','asserted',['One required garment missing'],'Deficient garments'),
('7','18a:11,18b:1','anonymous baraita','Service with one extra garment is invalid.','asserted',['One excess garment'],'Excess garments'),
('8','18a:11,18b:1','anonymous baraita','Service with a bandage over a wound underneath the garment is invalid.','asserted',['Bandage between flesh and garment'],'Interposition'),
('9','18b:1','anonymous baraita','Service in soiled garments is invalid.','asserted',['Soiled garments'],'Garment condition'),
('10','18b:1','anonymous baraita','Service in torn garments is invalid.','asserted',['Torn garments'],'Garment condition'),
('11','18b:2','Shmuel','Overlong garments are valid.','asserted',['Overlong garments'],'Rav Yehuda reports Shmuel'),
('12','18b:2','Shmuel','Short garments are invalid.','asserted',['Garments short from outset, as Rami bar Hama explains'],'Rav Yehuda reports Shmuel; initially worded raised'),
('13','18b:2','anonymous','Does the baraita not validate raised garments?','queried',['Apparent contradiction to Shmuel'],'Objection'),
('14','18b:2','Rami bar Hama','Raised by the belt differs from garments short from the outset.','asserted',['Belt gathering valid; originally short invalid'],'Reconciles baraita and Shmuel'),
('15','18b:3','Rav','Overlong garments are invalid.','asserted',['Overlong and not gathered, clarified by continuation'],'Disagrees with Shmuel'),
('16','18b:3','Rav','Short garments are invalid.','asserted',['Originally short garments'],'Agreement on invalidity of short garments'),
('17','18b:4','Rav Huna host','How can Shmuel invalidate short garments when the baraita validates raised garments?','queried',['Repeated objection while Rav Huna visits Argiza'],'Host question, not Rav Huna statement'),
('18','18b:4','Rav Huna','Set that baraita aside as an objection because Rami bar Hama already reconciled it.','asserted',['Belt gathering versus original shortness'],'Refers back to existing resolution'),
('19','18b:5','anonymous','The baraita remains difficult for Rav.','queried',['Rav invalidates overlong and short; baraita validates'],'New target of objection'),
('20','18b:5','anonymous','Even reading overlong as gathered by belt with the belt cutting off excess, the raised-garment clause remains difficult.','hypothetical',['Attempted belt interpretation of first clause'],'Partial reconciliation leaves second clause'),
('21','18b:6','Rabbi Zeira','Rav reads a single clause: overlong garments gathered by the belt are valid.','asserted',['Combined baraita reading; overlong gathered by belt'],'Resolves contradiction for Rav'),
('22','18b:7','Rav Yirmeya of Difti','Overlong garments not gathered are the subject of a tannaitic dispute.','challenged',['Ungathered overlong garments'],'Proposed analogy to corner counts rejected below'),
('23','18b:7','first corner baraita','A three-cornered garment is excluded from the tassel requirement.','asserted',['Three corners'],'Four excludes three'),
('24','18b:7','first corner baraita','A five-cornered garment is included in the tassel requirement.','asserted',['Five corners'],'Which you cover includes five; five contains four'),
('25','18b:8','second corner baraita','A three-cornered garment is excluded from the tassel requirement.','asserted',['Three corners'],'Agreement with first baraita'),
('26','18b:8','second corner baraita','A five-cornered garment is excluded from the tassel requirement.','asserted',['Five corners'],'Opposes first baraita'),
('27','18b:8','proposed anonymous explanation','The opposing corner rulings might turn on treating excess as present or absent.','rejected',['Proposed general principle from corner dispute'],'Rejected at18b9; do not transfer conclusively to garments'),
('28','18b:9','anonymous','All regard the excess as present; here Scripture specially includes it.','asserted',['Five-corner case; first baraita inclusion'],'Rejects proposed general dispute'),
('29','18b:10','anonymous','What does the other authority do with which you cover?','queried',['Second baraita; extra scriptural phrase'],'Alternative use inquiry'),
('30','18b:10','second baraita interpretation','The phrase includes the garment of a blind person in the tassel requirement.','asserted',['Blind person garment'],'Competing use of phrase'),
('31','18b:10','second baraita interpretation','You shall see it excludes night garments.','asserted',['Night garment'],'Exclusion distinct from blind person garment'),
('32','18b:11','anonymous','A blind person garment is visible to others, whereas night clothing is not visible to others.','asserted',['Reason to include blind person garment and exclude night garment'],'Comparative explanation'),
('33','18b:12','first baraita interpretation','The other authority derives that inclusion from the word which.','asserted',['Additional derivation from asher'],'Bracketed continuation retained'),
('34','18b:12','second baraita interpretation','The other authority does not expound which separately.','asserted',['No separate asher derivation'],'Bracketed continuation retained')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Garment length, belt gathering and attempted analogy to tassel corners',assertion_mode=mode),['u'+k],['Bracketed source continuation.'] if k in ['33','34'] else [])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v.startswith(('anonymous','proposed')) else [v]
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qlength' if k in ['11','15'] else (prefix+'qcorners' if k in ['24','26'] else None),conditions=conds,local_status=status),['c'+k])
rec('qlength','questions',['18b:2','18b:3'],dict(formulation='Are overlong garments not gathered by belt valid for service?',question_origin='editorial_reconstruction',conditions=['Overlong garments; not belt-gathered'],answer_set_status='partial'),origin='editorial_inference')
rec('qcorners','questions',['18b:7','18b:8'],dict(formulation='Is a five-cornered garment subject to tassels?',question_origin='editorial_reconstruction',conditions=['Five corners'],answer_set_status='partial'),origin='editorial_inference')
for k,refs,surface,cands,role,chain,links in [('shmuel',['18b:2'],'Rav Yehuda said Shmuel',['Rav Yehuda'],'transmitter',['Rav Yehuda','Shmuel'],['c11','c12']),('rami',['18b:2'],'Rami bar Hama',['Rami bar Hama'],'speaker',[],['c14']),('rav',['18b:3'],'Rav',['Rav'],'position_holder',[],['c15','c16']),('host',['18b:4'],'his host',[],'anonymous',[],['c17']),('huna',['18b:4'],'Rav Huna',['Rav Huna'],'speaker',[],['c18']),('zeira',['18b:6'],'Rabbi Zeira',['Rabbi Zeira'],'speaker',[],['c21']),('difti',['18b:7'],'Rav Yirmeya of Difti',['Rav Yirmeya of Difti'],'speaker',[],['c22'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role=role,candidates=cands,scope='Local explicit speaker or transmitter',transmission_chain=chain),links)
for a,b,rel in [('13','12','objection'),('14','13','answer'),('14','2','qualification'),('17','12','objection'),('18','17','answer'),('18','14','quotation'),('19','15','objection'),('20','19','answer'),('21','19','answer'),('21','1','qualification'),('22','15','support'),('27','22','support'),('28','27','correction'),('30','29','answer'),('31','30','distinction'),('32','30','support'),('32','31','support'),('33','30','qualification'),('34','33','distinction')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k,q in [('11','qlength'),('15','qlength'),('24','qcorners'),('26','qcorners')]:
 refs=next(x[1].split(',') for x in D if x[0]==k);rec('edispute'+k,'edges',refs,dict(source_id=prefix+'c'+k,target_id=prefix+q,relation='answer',explicitness='editorial_reconstruction'),['c'+k,q],origin='editorial_inference')
refs=['18a:11']+['18b:'+str(i) for i in range(1,13)]
rec('s1','structure',refs,dict(title='Garment conditions; Rav/Shmuel length dispute and rejected tannaitic analogy',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through18b12 and next linen discussion18b13 onward. Separate garment disqualifications, Rav from Rav Yehuda/Shmuel transmission, belt gathering reconciliation, rejected corner analogy and bracketed alternative derivations.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_18a11_18b12.json';r.immutable(path,r.encoded(p));print('Validated immutable proposal only; no promotion during hold.',r.sha(path.read_bytes()))
