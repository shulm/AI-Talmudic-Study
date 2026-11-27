import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b23.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='05d913cad3e3a8e37ffb903964d40f33699e3070d67979676de570299920cbc7'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','19b:16','Rabbi','If hands and feet were sanctified by day, they need not be sanctified again at night.','asserted',['Day sanctification; ensuing night'],'First baraita'),
('2','19b:16','Rabbi','If sanctified at night, they must be sanctified again by day.','asserted',['Night sanctification; ensuing day'],'Overnight expiration'),
('3','19b:16','Rabbi','Overnight passage affects sanctification of hands and feet.','asserted',['Passage through night'],'Underlying principle'),
('4','19b:16','Rabbi Elazar son of Rabbi Shimon','Overnight passage does not affect sanctification of hands and feet.','asserted',['Passage through night'],'Opposing principle'),
('5','19b:17','Rabbi','One who stood offering on the altar all night must sanctify hands and feet at daylight.','asserted',['Continuous all-night offering; daylight'],'Second baraita explicit continuous-work case'),
('6','19b:17','Rabbi Elazar son of Rabbi Shimon','Once sanctified at the start of service, he need not sanctify again even for ten days.','asserted',['Sanctified at service start; continued service'],'Second baraita opposing outcome'),
('7','19b:18','anonymous','The first teaching alone might allow Rabbi to concede where service never stopped.','hypothetical',['First teaching read as work interruption; second as continuous'],'Rejected limitation explains need for second teaching'),
('8','19b:18','anonymous','The continuous-work teaching alone might allow Rabbi Elazar son of Rabbi Shimon to concede when service stopped.','hypothetical',['Second teaching continuous; first includes interruption'],'Rejected limitation explains need for first teaching'),
('9','19b:18','anonymous','Both teachings are necessary.','asserted',['Continuous and interrupted cases'],'Both disputed scopes preserved'),
('10','19b:19','anonymous','What is Rabbi reason?','queried',['Overnight expiration view'],'Source inquiry'),
('11','19b:19','Rabbi textual basis','When they approach supplies Rabbi basis.','asserted',['Exodus30:20; begishtam'],'Scriptural basis'),
('12','19b:19','anonymous','What is Rabbi Elazar son of Rabbi Shimon reason?','queried',['No overnight expiration view'],'Source inquiry'),
('13','19b:19','Rabbi Elazar son of Rabbi Shimon textual basis','When they enter supplies his basis.','asserted',['Exodus30:20; bevoam'],'Scriptural basis'),
('14','19b:20','anonymous','But when they enter is also written for Rabbi.','queried',['Rabbi must account for other phrase'],'Objection'),
('15','19b:20','Rabbi explanation','Without when they enter, one might require sanctification for every approach.','asserted',['Both approach and entry wording'],'Entry wording limits repeated requirement'),
('16','19b:21','anonymous','But when they approach is also written for the other authority.','queried',['Rabbi Elazar son of Rabbi Shimon must account for approach wording'],'Objection'),
('17','19b:21','proposed anonymous explanation','Without approach wording one might require sanctification even for an empty entry.','rejected',['Entry not for service'],'Rejected next because to serve already written'),
('18','19b:22','anonymous','Empty entry is already excluded by to serve.','asserted',['Levitical service context of washing command'],'Objection to proposed explanation'),
('19','19b:22','Rav Aha bar Yaakov','All agree that at the second sanctification he sanctifies while dressed.','asserted',['Second sanctification; already dressed'],'Approach wording applies to one lacking only approach, not dressing plus approach'),
('20','19b:23','anonymous','What is to burn a fire-offering needed for?','queried',['Extra phrase in washing command'],'Additional scope inquiry'),
('21','20a:1','anonymous','It includes service that does not prevent atonement, which might otherwise have been excluded.','asserted',['Service not indispensable to atonement'],'Concluding extension of sanctification scope')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Overnight sanctification dispute and scriptural scope',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v.startswith(('anonymous','proposed')) else (['Rabbi'] if v.startswith('Rabbi textual') or v=='Rabbi explanation' else (['Rabbi Elazar son of Rabbi Shimon'] if v.endswith('textual basis') else [v]))
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qovernight' if k in ['3','4'] else (prefix+'qcontinuous' if k in ['5','6'] else None),conditions=conds,local_status=status),['c'+k])
rec('qovernight','questions',['19b:16'],dict(formulation='Does overnight passage expire sanctification of hands and feet?',question_origin='editorial_reconstruction',conditions=['Night passes'],answer_set_status='partial'),origin='editorial_inference')
rec('qcontinuous','questions',['19b:17'],dict(formulation='Must a priest continuously serving overnight sanctify again at daylight?',question_origin='editorial_reconstruction',conditions=['Continuous overnight service'],answer_set_status='partial'),origin='editorial_inference')
for k,refs,surface,cands,links in [('rabbi',['19b:16','19b:17'],'Rabbi',['Rabbi'],['c1','c2','c3','c5']),('elazar',['19b:16','19b:17'],'Rabbi Elazar son of Rabbi Shimon',['Rabbi Elazar son of Rabbi Shimon'],['c4','c6']),('aha',['19b:22'],'Rav Aha bar Yaakov',['Rav Aha bar Yaakov'],['c19'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='position_holder',candidates=cands,scope='Explicit local rule attribution',transmission_chain=[]),links)
for a,b,rel in [('3','2','support'),('9','7','qualification'),('9','8','qualification'),('11','10','answer'),('13','12','answer'),('15','14','answer'),('17','16','answer'),('18','17','objection'),('19','16','answer'),('21','20','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k,q in [('3','qovernight'),('4','qovernight'),('5','qcontinuous'),('6','qcontinuous')]:
 refs=next(x[1].split(',') for x in D if x[0]==k);rec('edispute'+k,'edges',refs,dict(source_id=prefix+'c'+k,target_id=prefix+q,relation='answer',explicitness='editorial_reconstruction'),['c'+k,q],origin='editorial_inference')
refs=['19b:'+str(i) for i in range(16,24)]+['20a:1']
rec('s1','structure',refs,dict(title='Overnight expiration of sanctification: two baraitot and scriptural derivations',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through20a1 and next laver-water inquiry20a2 onward. Preserve day/night direction, continuous/interrupted work distinction, rejected empty-entry explanation and second-sanctification dressed condition.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_19b16_20a1.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch23.json',r.encoded(res));print(res)
