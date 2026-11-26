import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b14.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='0eaf7c4f78fa5ead9a887396cf082132e58b4e76d77c8e36d7f0a19c2d81e4d5'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('left','15b:10','anonymous Mishnah','Receiving blood with the left hand invalidates.','asserted',['Left hand reception'],'Opposed by Rabbi Shimon'),
('shimon','15b:10','Rabbi Shimon','Receiving blood with the left hand is valid.','asserted',['Left hand reception'],'Explicit opposing view'),
('q','15b:11','anonymous','What is the source for invalidity of nonpriest service?','queried',['Nonpriest reception'],'Derivation inquiry'),
('levi','15b:11','Levi','Levi teaches from the command to Aaron and his sons to separate from the sacred things of Israel.','asserted',['Leviticus22:2; nonpriest service derivation'],'Verse interpretation examined'),
('women','15b:11','anonymous','Does children of Israel exclude women, permitting their offerings in impurity?','challenged',['Proposed exclusion of women offerings'],'Rhetorical rejection'),
('gentile','15b:12','anonymous','Could children of Israel exclude gentile offerings, allowing impurity even though the frontplate does not effect acceptance?','challenged',['Gentile offerings; impurity'],'Rhetorical rejection'),
('tzitz','15b:12','quoted authority','The frontplate does not effect acceptance for gentile offerings in impurity even when inadvertent.','asserted',['Gentile offering; inadvertent impurity'],'Cited premise'),
('tzitz2','15b:12','quoted authority','The frontplate does not effect acceptance for gentile offerings in impurity when deliberate.','asserted',['Gentile offering; deliberate impurity'],'Cited premise'),
('verse','15b:13','anonymous','Read the verse as requiring separation from the sacred things of Israel so that they not profane them.','asserted',['Nonpriest service; not exclusion of women or gentile offerings'],'Concluding reading of Levi derivation'),
('ishmael','15b:14,16a:1','school of Rabbi Ishmael','If a blemished priest who may eat profanes by service, a nonpriest who cannot eat should certainly profane.','asserted',['Nonpriest compared with blemished priest'],'Initial a-fortiori proof challenged'),
('blemish','16a:2','anonymous','Blemish is stronger because it disqualifies the offered as well as the offerer.','asserted',['Animal as well as priest blemish'],'Objection to simple inference'),
('impure','16a:3','anonymous','The impure person supplies a counterexample.','asserted',['Impurity as proof partner for blemish'],'Reply to blemish distinction'),
('contagion','16a:3','anonymous','Impurity is stronger because it transmits impurity.','asserted',['Impure performer'],'Objection to impure proof partner'),
('common','16a:4','anonymous','Blemish and impurity together establish that persons warned against service profane by serving, including the nonpriest.','asserted',['Common-factor proof; warned performers'],'Two-source proof challenged subsequently'),
('warning','16a:5','anonymous','Where is the nonpriest warned, without already deriving profanation from the same verse?','queried',['Need independent warning for common-factor inference'],'Vinazzeru would already state profanation'),
('warninganswer','16a:5','anonymous','The warning is that a stranger shall not approach you.','asserted',['Numbers18:4'],'Answer to warning source question'),
('bamah','16a:6','anonymous','The proof partners are stricter because they were not permitted at a private altar.','asserted',['Blemished and impure; bamah restriction'],'Objection to common factor'),
('onen','16a:7','anonymous','Replace impurity with an onen as the proof partner.','asserted',['Blemished priest plus onen'],'Revised common-factor proof'),
('maaser','16a:7','anonymous','An onen is stricter because he may not eat the tithe.','asserted',['Onen; tithe restriction'],'Objection to onen proof partner'),
('pair','16a:7,16a:8','anonymous','Blemish counters that objection; their common warning and profanation support the nonpriest conclusion.','asserted',['Blemished priest and onen'],'Bracketed blemish witness retained'),
('bamah2','16a:9','anonymous','Can the same private-altar objection be made against the revised pair?','queried',['Assuming onen forbidden at private altar'],'Objection questioned by Rav Sama'),
('sama','16a:9','Rav Sama son of Rava','Who establishes that an onen is forbidden at a private altar? Perhaps he is permitted.','queried',['Onen service at bamah'],'Possibility, not categorical permit'),
('mesh','16a:10','Rav Mesharshiya','A seated priest may eat yet profanes by serving, so a nonpriest who may not eat should certainly profane.','asserted',['Seated priest compared with nonpriest'],'Alternative a-fortiori proof'),
('testimony','16a:11','anonymous','Seated posture is stricter because it disqualifies testimony.','asserted',['Seated witness'],'Objection to seated proof'),
('scholar','16a:11','anonymous','Use a seated Torah scholar as the proof case.','asserted',['Scholar may testify seated but priestly service remains invalid seated'],'Reply to testimony objection'),
('category','16a:12','anonymous','Could the whole category of sitting be challenged for its testimony disqualification?','queried',['Category-level rather than individual comparison'],'Further objection'),
('categoryanswer','16a:12','anonymous','The category of sitting is not a valid objection.','asserted',['Category-level comparison'],'First reply'),
('fallback','16a:12','anonymous','Even if that objection is allowed, combine the seated case with one of the earlier cases.','conditional',['Assume category-level objection accepted'],'Alternative two-source proof'),
('standingq','16a:13','anonymous','How is seated service known to be valid at a private altar?','queried',['Seated priest; bamah'],'Source inquiry'),
('standing','16a:13','anonymous','Standing is required before the Lord, excluding a private altar.','asserted',['Deuteronomy10:8; bamah excluded from standing requirement'],'Concluding source proof')]
# Separate every Mishnah disqualifying condition; no composite counted again as a normative claim.
for k,condition in [('nonpriest','nonpriest'),('onen','onen'),('immersed','immersed today before sunset'),('atonement','missing required atonement offering'),('garments','missing priestly garments'),('washing','hands and feet not washed'),('uncircumcised','uncircumcised'),('impure','impure'),('seated','seated'),('vessels','standing on vessels'),('animal','standing on animal'),('feet','standing on fellow person feet')]:
 D.append(('m_'+k,'15b:9','anonymous Mishnah','Reception of sacrificial blood in this condition invalidates.','asserted',[condition,'Blood reception'],'Mishnah disqualification; later derivations remain separate'))
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_derivation',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Opening disqualifications and nonpriest derivations',assertion_mode=mode),['u'+k])
 if mode=='queried' or k in ['women','gentile']:rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':
  holder=[] if v.startswith('anonymous') else [v]
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qleft_dispute' if k in ['left','shimon'] else None,conditions=conds,local_status=status),['c'+k])
rec('qleft_dispute','questions',['15b:10'],dict(formulation='Is reception with the left hand valid?',question_origin='editorial_reconstruction',conditions=['Blood reception; left hand'],answer_set_status='partial'),origin='editorial_inference')
for k,ref,surface,cands,role,links in [('shimon','15b:10','Rabbi Shimon',['Rabbi Shimon'],'position_holder',['cshimon']),('levi','15b:11','Levi teaches',['Levi'],'quoted_authority',['clevi']),('ishmael','15b:14','school of Rabbi Ishmael',['school of Rabbi Ishmael'],'collective',['cishmael']),('sama','16a:9','Rav Sama son of Rava',['Rav Sama son of Rava'],'speaker',['csama']),('mesh','16a:10','Rav Mesharshiya',['Rav Mesharshiya'],'speaker',['cmesh'])]:rec('a'+k,'attributions',[ref],dict(surface=surface,role=role,candidates=cands,scope='Explicit named local attribution',transmission_chain=[]),links)
for a,b,rel in [('levi','q','answer'),('women','levi','objection'),('gentile','levi','objection'),('tzitz','gentile','support'),('tzitz2','gentile','support'),('verse','levi','qualification'),('ishmael','q','answer'),('blemish','ishmael','objection'),('impure','blemish','answer'),('contagion','impure','objection'),('common','contagion','answer'),('warning','common','objection'),('warninganswer','warning','answer'),('bamah','common','objection'),('onen','bamah','answer'),('maaser','onen','objection'),('pair','maaser','answer'),('bamah2','pair','objection'),('sama','bamah2','objection'),('mesh','q','answer'),('testimony','mesh','objection'),('scholar','testimony','answer'),('category','scholar','objection'),('categoryanswer','category','answer'),('fallback','category','answer'),('standing','standingq','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k in ['left','shimon']:rec('edispute'+k,'edges',['15b:10'],dict(source_id=prefix+'c'+k,target_id=prefix+'qleft_dispute',relation='answer',explicitness='editorial_reconstruction'),['c'+k,'qleft_dispute'],origin='editorial_inference')
refs=['15b:'+str(i) for i in range(9,15)]+['16a:'+str(i) for i in range(1,14)]
rec('s1','structure',refs[:2],dict(title='Mishnah: disqualified reception and left-hand dispute',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[2:],dict(title='Nonpriest service: verse and common-factor derivations',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through16a13 and next onen derivation16a14 onward. Separate every Mishnah status, preserve left-hand dispute, rejected exclusion readings, bamah caveat as possibility and alternate proof chains.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_15b9_16a13.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch14.json',r.encoded(res));print(res)
