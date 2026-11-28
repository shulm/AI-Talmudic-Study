"""Add omitted explicit questions and distinguish quoted Akiva rule from meta-inference."""
import copy,json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
old='f851c9b375713b38304ecf608a397ea529aa63992ecbfca1d40759d05b3354a6'
S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes());M=json.loads((J/'JOB.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
def evidence(i,quote=None):
 t=I[i]['text'];quote=t if quote is None else quote;a=t.index(quote)
 return dict(segment_id=I[i]['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(k,l,ev,c,links=()):
 rid='yom.s2703.fix.'+k;R.append(dict(id=rid,layer=l,evidence=ev,content=c,origin='source_paraphrase',uncertainty=[],links=list(links)));return rid
future=add('q_future','questions',[evidence(87,'לעתיד לבוא נמי לכשיבואו אהרן ובניו ומשה עמהם')],dict(formulation='Why ask even about the future, when Aaron and his sons will come with Moses?',question_origin='explicit',conditions=['Challenge to the temporary future-practical-purpose reformulation','Future inauguration clothing order could be addressed when Aaron, his sons and Moses arrive; the discussion next supplies an exegetical purpose'],answer_set_status='partial'))
alignment=add('q_akiva','questions',[evidence(96)],dict(formulation='According to whom does the baraita about separation from his wife follow—Rabbi Akiva?',question_origin='explicit',conditions=['Intercourse precedes subsequent discovery of possible menstrual impurity, in corrected baraita wording','Question of alignment with Rabbi Akiva versus the sages; Rav Hisda qualifies the inference by timing next'],answer_set_status='partial'))
rule=add('akiva_rule','claims',[evidence(95),evidence(96),evidence(97)],dict(proposition='Rabbi Akiva holds that the menstruant renders her partner impure in the retrospective-discovery case discussed here.',conditions=['Menstrual impurity discovered after intercourse','The dispute is scoped by Rav Hisda to אחר אחר; in חד אחר the sages agree'],scope='Quoted legal view within the rabbis’ argument, separately represented from their tentative inference that the baraita must follow Rabbi Akiva. No universal retrospective rule or numerical interval invented.',assertion_mode='asserted'))
add('akiva_rule.a','attributions',[evidence(96,'כרבי עקיבא דאמר נדה מטמאה את בועלה')],dict(surface='רבי עקיבא',role='position_holder',candidates=['רבי עקיבא'],scope='Quoted retrospective-impurity rule; not speaker of the rabbis-before-Rav-Hisda meta-inference.',transmission_chain=[]),[rule])
add('akiva_rule.p','positions',[evidence(95),evidence(96),evidence(97)],dict(holder_candidates=['רבי עקיבא'],claim_id=rule,question_id=None,conditions=['Retrospective-discovery case','Timing distinction אחר אחר versus חד אחר retained'],local_status='Quoted view; the inference that the baraita exclusively follows it is separately challenged by Rav Hisda.'),[rule])
for k,ii,src,dst,rel in [('future_challenge',[87],future,'yom.s2703.future','objection'),('future_purpose_answer',[88],'yom.s2703.purpose',future,'answer'),('alignment_proposal',[96],'yom.s2703.proposeakiva',alignment,'answer'),('alignment_qualification',[97],'yom.s2703.hasda',alignment,'answer'),('akiva_support',[96],rule,'yom.s2703.proposeakiva','support')]:
 add(k,'edges',[evidence(i) for i in ii],dict(source_id=src,target_id=dst,relation=rel,explicitness='source_explicit'),[src,dst])
C=[]
for oldc in S['coverage']:
 ids=[r['id'] for r in R if (oldc['layer']=='reconciliation' or oldc['layer']==r['layer']) and any(e['segment_id']==oldc['segment_id'] for e in r['evidence'])]
 if not ids:continue
 c={k:copy.deepcopy(v) for k,v in oldc.items() if k!='proposal_execution'};c['record_ids']+=ids;c['extraction_result']='records_found'
 c['rationale']+=' Bounded review correction: explicit future-purpose and authority-alignment questions added with conditions and answer links; Rabbi Akiva cited rule separated from rabbis’ meta-inference. Original claims, holders and evidence preserved; no new completed segment.'
 C.append(c)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=C,open_tails=S['open_tails'])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_questions_akiva_correction_v2.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),sha256=hashlib.sha256(b).hexdigest(),new_completed_segments=0)))
