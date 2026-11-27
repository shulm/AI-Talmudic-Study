import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b19.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='f56e4ad0cc053ffeacf758dea51364ac14a9647be41a2634ff186025bb424632'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','18b:13','anonymous baraita','The garments described as bad must be linen.','asserted',['Priestly linen garments'],'Required material'),
('2','18b:13','anonymous baraita','They should be new.','asserted',['Priestly linen garments'],'Ideal requirement, worn garments valid per continuation'),
('3','18b:13','anonymous baraita','Their threads should be twisted.','asserted',['Priestly linen garments'],'Requirement listed; degree of indispensability not individually assigned here'),
('4','18b:13','anonymous baraita','Each thread should be sixfold.','asserted',['Priestly linen garments'],'Requirement listed'),
('5','18b:13','anonymous baraita','Ordinary garments must not be worn together with them.','asserted',['Priestly garments plus ordinary garments'],'Additional clothing prohibited'),
('6','18b:14','Abaye','Linen excludes other materials, but does new exclude worn garments despite the baraita validating worn garments?','queried',['Newness versus validity of worn garments'],'Question to Rav Yosef'),
('7','18b:15','Rav Yosef','On that reading, bad suggests a single thread, conflicting with sixfold thread.','asserted',['Literal reading of bad; sixfold requirement'],'Counterquestion to Abaye literal exposition'),
('8','18b:15','Rav Yosef','The teaching lists properties required of garments called bad; some are ideal requirements and some indispensable.','asserted',['Listed linen, new, twisted and sixfold requirements'],'Resolves newness difficulty without assigning each item individually'),
('9','18b:16','anonymous','How is bad known to mean flax?','queried',['Meaning of garment material term'],'Material derivation inquiry'),
('10','18b:16','Rabbi Yosef son of Rabbi Hanina','It means that which grows from the ground singly.','asserted',['Flax stalk growth'],'Etymological explanation'),
('11','18b:17','anonymous','Could the material instead be wool?','queried',['Alternative material identification'],'Objection'),
('12','18b:17','anonymous','Wool branches.','asserted',['Wool growth distinction'],'Reply'),
('13','18b:17','anonymous','Flax also branches.','challenged',['Apparent counterexample to growth distinction'],'Objection'),
('14','18b:17','anonymous','Flax branching occurs because of damage.','asserted',['Abnormal damaged flax growth'],'Distinguishes ordinary growth'),
('15','18b:18','Ravina','Ezekiel linen headwear and trousers supply the textual support.','asserted',['Ezekiel44:18; explicit linen'],'Alternative scriptural support; bracketed continuation retained'),
('16','18b:19','Rav Ashi','Before Ezekiel arrived, how was this known?','queried',['Earlier basis for linen requirement'],'Question to Ravina'),
('17','18b:19','Rav Hisda quoted','The exclusion of an alien uncircumcised in heart or flesh was not learned from Moses Torah but from Ezekiel.','asserted',['Ezekiel44:9; admission to sanctuary service'],'Counterexample used to clarify role of prophetic support'),
('18','18b:19','anonymous respondent','The rule was received by tradition and Ezekiel attached it to a verse.','asserted',['Prior received law; later prophetic textual support'],'Applies to quoted exclusion and linen rule; no claim Ezekiel invented law'),
('19','18b:20','anonymous','What does not gird in sweat mean?','queried',['Ezekiel44:18'],'Verse interpretation'),
('20','18b:20','Abaye','Do not gird at places where one sweats.','asserted',['Belt placement'],'Explanation'),
('21','18b:20','quoted baraita','Do not gird below the waist.','asserted',['Priestly belt below waist'],'Placement excluded'),
('22','18b:20','quoted baraita','Do not gird above the elbows.','asserted',['Priestly belt above elbow level'],'Placement excluded'),
('23','18b:20,19a:1','quoted baraita','Gird opposite the elbows.','asserted',['Priestly belt at elbow level'],'Required placement'),
('24','19a:2','Huna bar Natan','While standing before King Izgadar with his belt high, the king lowered it and cited kingdom of priests and holy nation.','asserted',['Court encounter; belt placement'],'Personal report transmitted by Rav Ashi; narrative not independent garment rule'),
('25','19a:2','Amemar','Kings shall be your nurturers was fulfilled in that event.','asserted',['Huna bar Natan report to Amemar'],'Interpretation of court narrative')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else ('narrative' if k in ['24','25'] else 'rule_or_argument'),composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Linen garment properties, traditional law and belt placement',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried' and k!='24':
  holder=[] if v.startswith(('anonymous','quoted')) else (['Rav Hisda'] if k=='17' else [v])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,refs,surface,cands,role,chain,links in [('abaye',['18b:14'],'Abaye to Rav Yosef',['Abaye'],'speaker',[],['c6']),('yosef',['18b:15'],'he said to him',['Rav Yosef'],'speaker',[],['c7','c8']),('hanina',['18b:16'],'Rabbi Yosef son of Rabbi Hanina',['Rabbi Yosef son of Rabbi Hanina'],'speaker',[],['c10']),('ravina',['18b:18'],'Ravina',['Ravina'],'speaker',[],['c15']),('ashi',['18b:19'],'Rav Ashi to Ravina',['Rav Ashi'],'speaker',[],['c16']),('hisda',['18b:19'],'Rav Hisda',['Rav Hisda'],'quoted_authority',[],['c17']),('abaye2',['18b:20'],'Abaye',['Abaye'],'speaker',[],['c20']),('huna',['19a:2'],'Rav Ashi said Huna bar Natan told me',['Rav Ashi'],'transmitter',['Rav Ashi','Huna bar Natan'],['c24']),('king',['19a:2'],'Izgadar the king',['King Izgadar'],'speaker',[],['c24']),('amemar',['19a:2'],'Amemar said to me',['Amemar'],'speaker',[],['c25'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role=role,candidates=cands,scope='Named local speaker/reporting role',transmission_chain=chain),links)
for a,b,rel in [('6','2','objection'),('7','6','objection'),('8','6','answer'),('8','2','qualification'),('10','9','answer'),('11','10','objection'),('12','11','answer'),('13','12','objection'),('14','13','answer'),('15','9','answer'),('16','15','objection'),('17','16','analogy'),('18','16','answer'),('18','15','qualification'),('20','19','answer'),('21','20','support'),('22','20','support'),('23','20','support'),('25','24','qualification')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['18b:'+str(i) for i in range(13,21)]+['19a:1','19a:2']
rec('s1','structure',refs,dict(title='Linen garment requirements, prophetic support and belt placement narrative',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through19a2 and new bandage/interposition source19a3 onward. Separate each garment property, preserve ideal/indispensable distinction without unsupported allocation, preexisting tradition vs prophetic support, and court narrative attribution.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_18b13_19a2.json';r.immutable(path,r.encoded(p));print('Validated immutable proposal only; no promotion during hold.',r.sha(path.read_bytes()))
