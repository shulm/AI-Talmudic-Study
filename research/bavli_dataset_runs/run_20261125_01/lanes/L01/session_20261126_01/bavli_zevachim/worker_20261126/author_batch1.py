import sys,subprocess
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
repo=Path(r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study'); job=Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim'); out=job/'worker_20261126'
j,ss=r.load(job); rows={v['ref'].split(' ')[1]:v for v in ss.values()}; state=r.current(job)
active=r.read(repo/'research/bavli_dataset_runs/ACTIVE_RUN.json'); assert r.sha((repo/active['contract_path']).read_bytes())==active['contract_sha256']
for f in ['runner.py','schema.json','PROTOCOL.md']:
 b=subprocess.check_output(['git','show',active['production_git_commit']+':research/bavli_production_v1/'+f],cwd=repo); assert b==(repo/'research/bavli_production_v1'/f).read_bytes()
assert r.read(job/'OWNER.json')==dict(owner='/root/zevachim_resume',epoch=3)
assert r.sha(r.encoded(state))=='4816d1a56f623ce6377d478dd97aca7b3c62c895c55e7b3ec4d2f97246f4a83f'
r.immutable(out/'verification_before_batch1.json',r.encoded(dict(active=active,owner=r.read(job/'OWNER.json'),source=j['source_sha256'],pins=r.hashes(),replay=r.replay(job))))
R=[]; prefix='zv.20261126.b1.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,content,links=[],unc=[],origin='source_paraphrase'):
 v=dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=content,origin=origin,uncertainty=unc,links=[prefix+x for x in links]);R.append(v);return key
# Each tuple is a manually authored reading, not inferred from source patterns.
D=[
('2','5a:2','ריש לקיש','question','Why should valid offerings fail to discharge the obligation, and if they do not discharge it, why are they brought?','queried',['Offerings slaughtered not for their designated purpose'],None),
('3','5a:3','ר׳ אליעזר','analogy','Offerings brought after the owner dies are valid but do not discharge the deceased owner\'s obligation.','asserted',['Owner has died'],None),
('4','5a:4','ריש לקיש','objection','The posthumous burnt-offering example is conceded; the guilt offering, which is not brought after death, still needs a source.','challenged',['Guilt offering; unlike a burnt offering it is not brought after death'],'What establishes validity without discharge for the guilt offering?'),
('5','5a:5','ר׳ אליעזר','reply','Rabbi Eliezer\'s dissent is alongside the Mishnah: he includes the guilt offering among the exceptions.','asserted',['According to Rabbi Eliezer\'s dissent'],None),
('6','5a:6','ריש לקיש','rejection','A dissenting Rabbi Eliezer does not answer the question about the complete anonymous Mishnah.','rejected',['The target is the anonymous Mishnah, not Rabbi Eliezer\'s dissent'],None),
('7','5a:7','ריש לקיש','derivation','Resh Lakish offers his own opening from the vow/freewill distinction in מוצא שפתיך, referring to the earlier derivation.','asserted',['Fulfillment unlike what was vowed'],None),
('8','5a:8','רבי זירא ורבי יצחק בר אבא','objection','The vow/freewill verse might establish bringing without discharge only for voluntarily vowed offerings; a guilt offering might not be brought at all.','hypothetical',['Guilt offering cannot be vowed voluntarily'],'Why does the vow/freewill derivation allow bringing a guilt offering at all?'),
('9','5a:9','אביי','reply','Abaye reconstructs Resh Lakish\'s derivation: אותה limits invalidity for wrong purpose to the sin offering; other consecrated offerings are valid, while מוצא שפתיך prevents discharge.','asserted',['Slaughter not for designated purpose; non-sin offerings'],None),
('10','5a:10','anonymous','objection','Perhaps only vowed/freewill offerings fail to discharge, whereas the guilt offering also discharges.','hypothetical',['Guilt offering slaughtered not for its purpose'],'Could the guilt offering nevertheless discharge?'),
('11','5a:11','אביי','a_fortiori','The guilt offering cannot discharge: if a burnt offering, described here as not atoning, does not discharge, a guilt offering which atones should certainly not discharge.','asserted',['Both slaughtered not for designated purpose'],None),
('12','5a:12','anonymous','objection','The burnt offering has the special stringency of being entirely consumed, defeating that direct inference.','challenged',['Comparison to burnt offering'],'Does the burnt offering\'s total consumption distinguish it?'),
('13','5a:13','anonymous','reply','Peace offerings provide a counterexample to the total-consumption distinction.','asserted',['Peace offerings also slaughtered not for designated purpose'],None),
('14','5a:14','anonymous','objection','Peace offerings have their own distinguishing requirements: libations and waving the breast and thigh.','challenged',['Comparison to peace offerings'],'Do the peace offering requirements distinguish it?'),
('15','5a:15','anonymous','common_factor','Burnt and peace offerings jointly establish a common factor: both are consecrated, valid without discharge after wrong-purpose slaughter; the guilt offering is proposed for the same result.','asserted',['Wrong-purpose slaughter; proposed inference from common factor'],None),
('16','5a:16','anonymous','objection','Both examples occur as communal offerings, distinguishing them from the guilt offering.','challenged',['Comparison to burnt and peace offerings'],'Does occurrence as communal offerings distinguish the common factor?'),
('17','5a:17','anonymous','reply','The thanksgiving offering is proposed as a counterexample to the communal-offering distinction.','asserted',['Wrong-purpose slaughter; thanksgiving offering'],None),
('18','5b:1','anonymous','objection','The thanksgiving offering is distinguishable because it requires bread.','challenged',['Comparison to thanksgiving offering'],'Does the bread requirement distinguish thanksgiving?'),
('19','5b:2','anonymous','common_factor','Burnt and peace offerings counter the bread distinction; with thanksgiving the repeated common-factor argument proposes validity without discharge for the guilt offering.','asserted',['Wrong-purpose slaughter; combined common-factor inference'],None),
('20','5b:3','anonymous','objection','All these examples can be vowed or donated, unlike the guilt offering; this defeats the common-factor inference.','challenged',['Combined inference from voluntarily vowed offerings'],'Does voluntary vow/freewill availability distinguish all the examples?'),
('21','5b:4','רבא','replacement_derivation','Rava instead uses זאת התורה to juxtapose the guilt offering to peace offerings, deriving validity without discharge when slaughtered not for its purpose.','asserted',['Guilt offering slaughtered not for its purpose'],None),
('22','5b:5','anonymous','objection','Why compare the guilt offering to peace offerings rather than to the sin offering?','queried',['Competing scriptural comparisons'],'Why not compare it to the sin offering?'),
('23','5b:6','anonymous','reply','The restrictive אותה has already excluded other offerings from the sin offering\'s invalidity.','asserted',['Wrong-purpose slaughter; non-sin offerings'],None)]
for key,ref,voice,role,prop,mode,conditions,q in D:
 unc=['Surface ר׳ אליעזר is preserved; later 5b:15 reads רבי אלעזר. No normalized identity resolution imposed.'] if key in ['3','5'] else []
 rec('u'+key,'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['3','8','9','15','19'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',[ref],dict(proposition=prop,conditions=conditions,scope='Local wrong-purpose sacrifice argument; no later halachic ruling inferred',assertion_mode=mode),['u'+key],unc)
 if voice!='anonymous':rec('a'+key,'attributions',[ref],dict(surface=voice,role='speaker',candidates=[voice],scope='u'+key,transmission_chain=[]),['u'+key],unc)
 if key=='2':q=prop
 if q:rec('q'+key,'questions',[ref],dict(formulation=q,conditions=conditions,question_origin='explicit',answer_set_status='partial'),['u'+key])
 if mode=='asserted':rec('p'+key,'positions',[ref],dict(holder_candidates=[] if voice=='anonymous' else [voice],claim_id=prefix+'c'+key,question_id=None,conditions=conditions,local_status='Local proposed derivation or response; subsequent objections preserved'),['c'+key],unc)
# Separately retain each postpartum Mishnah condition and the reporting roles.
for key,prop,cond in [('3a','Heirs bring her burnt offering after she brought her sin offering and died.',['Woman brought her sin offering, then died']),('3b','Heirs do not bring her sin offering after she brought her burnt offering and died.',['Woman brought her burnt offering, then died'])]:
 rec('c'+key,'claims',['5a:3'],dict(proposition=prop,conditions=cond,scope='Quoted postpartum Mishnah',assertion_mode='conditional'),['u3'])
 rec('p'+key,'positions',['5a:3'],dict(holder_candidates=['quoted Mishnah'],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status='Quoted rule used as evidence'),['c'+key])
rec('a3quote','attributions',['5a:3'],dict(surface='דתנן',role='quoted_authority',candidates=['Mishnah'],scope='Postpartum offerings quotation',transmission_chain=['ר׳ אליעזר','Mishnah']),['c3a','c3b'])
rec('a5quote','attributions',['5a:5'],dict(surface='רבי אליעזר אומר',role='quoted_authority',candidates=['רבי אליעזר'],scope='Dissent includes guilt offering',transmission_chain=[]),['c5'],['Quoted authority distinguished from dialogue respondent; surface names do not prove identity.'])
rec('a9report','attributions',['5a:9'],dict(surface='ריש לקיש מהכא פתח',role='quoted_authority',candidates=['ריש לקיש'],scope='Derivation as reconstructed by Abaye',transmission_chain=['אביי','ריש לקיש']),['c9'])
# Explicit argument sequence; endpoints are claims or actual questions.
for a,b,rel in [('3','2','answer'),('3a','3','support'),('4','3','objection'),('5','4','answer'),('6','5','objection'),('7','2','answer'),('8','7','objection'),('9','8','answer'),('10','9','objection'),('11','10','answer'),('12','11','objection'),('13','12','answer'),('14','13','objection'),('15','14','answer'),('16','15','objection'),('17','16','answer'),('18','17','objection'),('19','18','answer'),('20','19','objection'),('21','20','answer'),('22','21','objection'),('23','22','answer')]:
 ref=next(x[1] for x in D if x[0]==a) if a!='3a' else '5a:3'
 rec('e'+a+'_'+b,'edges',[ref],dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=[x[1] for x in D]
rec('s1','structure',refs[:6],dict(title='Resh Lakish: validity without discharge and the guilt-offering challenge',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[6:],dict(title='Reconstructing the guilt-offering derivation: Abaye and Rava',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  rationale='Source reread against claims, conditions, voices, questions and linked objections; continuation read through 6a:4. Later retrospective discussion begins 5b:8 and is not covered here.' if layer=='reconciliation' else 'Manually read local source and complete 5a:2–5b:6 argument; '+('listed source-supported records.' if ids else 'no separate '+layer+' item found in this segment after pass; anonymous voice retained in utterance where applicable.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=3,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j); path=out/'proposal_5a2_5b6.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch1.json',r.encoded(res));print(res)
