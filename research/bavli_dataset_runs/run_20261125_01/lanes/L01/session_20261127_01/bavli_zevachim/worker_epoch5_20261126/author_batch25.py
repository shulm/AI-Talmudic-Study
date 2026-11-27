import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b25.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='9a49e3dd047718ebb3def81e1839f5226192cfd941e6f3ebf8cfa40292a4da3f'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','20a:13','Rabbi Yohanan','One who sanctified hands and feet for ash removal need not sanctify the next day because he already sanctified at the start of service.','asserted',['Sanctification for ash removal; following day'],'Rule with competing interpretations'),
('2','20a:14','anonymous','To whose view does this belong: Rabbi invalidates overnight, whereas Rabbi Elazar son of Rabbi Shimon permits even ten days?','queried',['Compatibility of Yohanan rule with two overnight views'],'Interpretive inquiry'),
('3','20a:15','Abaye','It can follow Rabbi, since overnight expiration is rabbinic.','asserted',['Rabbi interpretation; rabbinic overnight expiration'],'Abaye account'),
('4','20a:15','Abaye','Rabbi concedes that the interval from cockcrow until morning does not expire sanctification.','asserted',['Cockcrow-to-morning interval'],'Explains ash-removal rule under Rabbi'),
('5','20a:16','Rava','It follows Rabbi Elazar son of Rabbi Shimon; Yohanan accepts his view at the start of service.','asserted',['Ash removal as start of service'],'Rava alternative; bracketed attribution phrase preserved'),
('6','20a:16','Rava','Yohanan does not accept that view at the end of service.','asserted',['End-of-service sanctification'],'Distinct restriction of Rava interpretation'),
('7','20a:17','quoted source','When fellow priests saw him descend, they hurried and sanctified hands and feet from the laver.','asserted',['Priests arriving after ash-removal priest descends'],'Objection source'),
('8','20b:1','anonymous','Under Abaye this can follow Rabbi and his concession from cockcrow until morning.','asserted',['Abaye account; arriving priests sanctify'],'Compatibility analysis'),
('9','20b:2','anonymous','Under Rava, how can this fit either Rabbi, who expires sanctification by morning, or Rabbi Elazar son of Rabbi Shimon, who needs none even for ten days?','queried',['Rava account; timing of priests sanctification'],'Objection'),
('10','20b:3','anonymous','It follows Rabbi Elazar son of Rabbi Shimon and concerns fresh priests.','asserted',['New priests not yet sanctified for this service'],'Answers objection without changing underlying overnight rule')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Ash-removal sanctification: Abaye and Rava interpretations',assertion_mode=mode),['u'+k],['Source brackets Yohanan acceptance phrase.'] if k=='5' else [])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':rec('p'+k,'positions',refs,dict(holder_candidates=[] if v in ['anonymous','quoted source'] else [v],claim_id=prefix+'c'+k,question_id=prefix+'q2' if k in ['3','4','5','6'] else None,conditions=conds,local_status=status),['c'+k])
for k,ref,surface,links in [('yohanan','20a:13','Rabbi Yohanan',['c1']),('abaye','20a:15','Abaye',['c3','c4']),('rava','20a:16','Rava',['c5','c6'])]:rec('a'+k,'attributions',[ref],dict(surface=surface,role='speaker',candidates=[surface],scope='Explicit source speaker or interpreter',transmission_chain=[]),links)
for a,b,rel in [('2','1','qualification'),('3','2','answer'),('4','3','support'),('5','2','answer'),('6','5','qualification'),('7','1','objection'),('8','7','answer'),('9','5','objection'),('10','9','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['20a:'+str(i) for i in range(13,18)]+['20b:1','20b:2','20b:3']
rec('s1','structure',refs,dict(title='Ash-removal sanctification: competing interpretations and fresh-priests reply',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through20b3 and new exit inquiry20b4 onward. Keep Abaye and Rava interpretations distinct, cockcrow exception, start/end service difference and fresh-priests answer.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_20a13_20b3.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch25.json',r.encoded(res));print(res)
