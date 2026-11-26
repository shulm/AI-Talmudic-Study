import sys
from pathlib import Path
sys.path.insert(0,'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
job=Path(__file__).resolve().parents[1]; out=Path(__file__).resolve().parent
j,segments=r.load(job); byref={x['ref'].split()[1]:x for x in segments.values()}; records=[]; prefix='kt.resume26.b1.'
def ev(ref,quote=None):
 s=byref[ref];t=s['text'];quote=t if quote is None else quote;a=t.index(quote);return dict(segment_id=s['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(key,layer,refs,content,quote=None,links=(),origin='source_paraphrase',unc=()):
 evidence=[ev(x) for x in refs] if isinstance(refs,list) else [ev(refs,quote)]
 rid=prefix+key;records.append(dict(id=rid,layer=layer,evidence=evidence,content=content,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def claim(key,ref,quote,text,conditions=(),mode='asserted',holder=('anonymous discussion',),status='Local explanation; not a later practical ruling'):
 c=add('c.'+key,'claims',ref,dict(proposition=text,conditions=list(conditions),scope='Marriage timing: Ketubot 3b local discussion',assertion_mode=mode),quote)
 add('p.'+key,'positions',ref,dict(holder_candidates=list(holder),claim_id=c,question_id=None,conditions=list(conditions),local_status=status),quote,links=[c]);return c
def q(key,ref,quote,text,conditions=()):return add('q.'+key,'questions',ref,dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status='partial'),quote)
def edge(key,ref,quote,a,b,relation):return add('e.'+key,'edges',ref,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),quote,links=[a,b])
def attr(key,ref,quote,surface,role,candidates,scope,chain=()):return add('a.'+key,'attributions',ref,dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=list(chain)),quote)
add('s.baraita','structure',['3b:1','3b:2'],dict(title='Baraita: Wednesday marriage, preparation, exceptions, and initial intercourse on Sabbath eve',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.danger','structure',['3b:3','3b:4','3b:5','3b:6'],dict(title='Meaning of danger and limits of the Tuesday concession',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('3b:1','anonymous framing and quoted baraita','question, rationale, alternative proposal, and reply'),('3b:2','quoted baraita','exceptions and restrictions'),('3b:3','anonymous discussion','question and rejected interpretation'),('3b:4','Rabbah and anonymous discussion','interpretation, objection, and answer'),('3b:5','anonymous discussion','proposal and objections'),('3b:6','anonymous discussion','proposals, policy distinction, and response')]:
 add('u.'+ref,'utterances',ref,dict(textual_voice=voice,discourse_role=role,composition='composite'))
qsh=q('shakedu','3b:1','מאי שקדו','What is the cited shakedu preparation rule?')
qwed=q('wednesday','3b:1','מפני מה אמרו בתולה נשאת ליום הרביעי','Why was marriage of a virgin assigned to Wednesday?')
cw=claim('court','3b:1','שאם היה לו טענת בתולים היה משכים לב"ד','Wednesday allows a husband with a virginity claim to go early to court.', ['Marriage of a virgin','Husband has a virginity claim'],holder=['quoted baraita'])
qs=q('sunday','3b:1','ותנשא באחד בשבת ואם היה לו טענת בתולים היה משכים לב"ד','Why not marry on Sunday, which also allows prompt court attendance?',['Virginity claim'])
cp=claim('preparation','3b:1','שקדו חכמים על תקנת בנות ישראל שיהא אדם טורח בסעודה שלשה ימים אחד בשבת ושני בשבת ושלישי בשבת וברביעי כונסה','The sages provided three days of feast preparation, Sunday through Tuesday, followed by marriage on Wednesday.',holder=['חכמים'],status='Baraita rationale')
edge('court_answer','3b:1','שאם היה לו טענת בתולים היה משכים לב"ד',cw,qwed,'answer');edge('prep_answer','3b:1','שקדו חכמים על תקנת בנות ישראל',cp,qs,'answer');edge('shakedu_answer','3b:1','שקדו חכמים על תקנת בנות ישראל',cp,qsh,'answer')
attr('sages','3b:1','שקדו חכמים','חכמים','collective',['חכמים'],'Enactment of preparation period')
ct=claim('tuesday','3b:2','ומסכנה ואילך נהגו העם לכנוס בשלישי ולא מיחו בידם חכמים','From the time of danger people practiced marriage on Tuesday and the sages did not protest.',['Danger described in the continuation'],holder=['quoted baraita'],status='Tolerated practice, not an unrestricted abolition')
cm=claim('monday','3b:2','ובשני לא יכנוס','One is not to marry on Monday.',['Ordinary application of this baraita, absent coercive exception'],holder=['quoted baraita'])
ca=claim('coercion','3b:2','ואם מחמת האונס מותר','Marriage on Monday is permitted because of coercion.',['Because of coercion; meaning discussed at 3b:7 onward'],mode='conditional',holder=['quoted baraita'])
cf=claim('friday','3b:2','ומפרישין את החתן מן הכלה לילי שבת תחלה מפני שהוא עושה חבורה','Bridegroom and bride are separated on the first Sabbath night because first intercourse makes a wound.',['Initial intercourse','Sabbath night'],holder=['quoted baraita'])
attr('nonprotest','3b:2','ולא מיחו בידם חכמים','חכמים','collective',['חכמים'],'Nonprotest at Tuesday practice')
edge('coercion_exception','3b:2','ואם מחמת האונס מותר',ca,cm,'qualification')
qd=q('danger','3b:3','מאי סכנה','What danger is meant?')
ce=claim('execution_hypothesis','3b:3','אילימא דאמרי בתולה הנשאת ליום הרביעי תיהרג','A decree to kill a virgin marrying on Wednesday is considered, then rejected as the intended danger.',['Hypothetical decree of execution'],mode='rejected',status='Rejected interpretation, not an established historical event')
qe=q('uproot_execution','3b:3','נהגו לגמרי ניעקריה','If Wednesday marriage incurred execution, why merely tolerate the custom instead of abolishing the Wednesday rule?',['Hypothetical decree of execution'])
edge('execution_rejection','3b:3','נהגו לגמרי ניעקריה',qe,ce,'objection')
cg=claim('governor','3b:4','אמר רבה דאמרי בתולה הנשאת ביום הרביעי תיבעל להגמון תחלה','Rabbah interprets the decree as requiring a virgin marrying on Wednesday to be taken first by the governor.',['Virgin marrying Wednesday'],holder=['רבה'])
attr('rabbah','3b:4','אמר רבה','רבה','speaker',['רבה'],'Interpretation of danger decree; Rabbah, not Rava')
qo=q('coercion_notdanger','3b:4','האי סכנה אונס הוא','Is this coercion rather than danger?',['Governor decree'])
cd=claim('modest_danger','3b:4','משום דאיכא צנועות דמסרן נפשייהו לקטלא ואתיין לידי סכנה','Some modest women would give their lives rather than submit, creating danger.',['Governor decree','Some modest women refuse at risk of death'])
edge('governor_answer','3b:4','אמר רבה דאמרי',cg,qd,'answer');edge('coercion_objection','3b:4','האי סכנה אונס הוא',qo,cg,'objection');edge('danger_reply','3b:4','משום דאיכא צנועות דמסרן נפשייהו לקטלא ואתיין לידי סכנה',cd,qo,'answer')
qt=q('teach','3b:5','ולידרוש להו דאונס שרי','Why not teach them that forced intercourse is permitted?',['Coercive governor decree; the question proposes teaching, not permission for voluntary intercourse'])
cl=claim('licentious','3b:5','איכא פרוצות','The presence of licentious women is one reason against the proposed public teaching.',['Proposed teaching concerning forced intercourse'])
ck=claim('priestly','3b:5','ואיכא נמי כהנות','Priestly women are an additional obstacle to that proposed teaching.',['Proposed teaching concerning forced intercourse'],status='Source says kohanot; applicability details are not expanded in the local text')
edge('licentious_answer','3b:5','איכא פרוצות',cl,qt,'answer');edge('priestly_answer','3b:5','ואיכא נמי כהנות',ck,qt,'answer')
qu=q('uproot','3b:6','וליעקריה','Why not abolish the Wednesday enactment?',['Governor decree and continuing danger'])
cr=claim('temporary','3b:6','גזירה עבידא דבטלא ותקנתא דרבנן מקמי גזירה לא עקרינן','The decree is liable to cease; a rabbinic enactment is not uprooted on account of such a decree.',['A coercive decree liable to cease'],status='Local rationale for retaining enactment while tolerating Tuesday practice')
qb=q('tuesday_governor','3b:6','אי הכי בשלישי נמי אתי ובעיל','Would the governor not also come on Tuesday?',['Tuesday practice under the decree'])
cn=claim('uncertain_arrival','3b:6','מספיקא לא עקר נפשיה','The governor does not trouble himself to come on the basis of uncertainty.',['Uncertain occurrence of Tuesday marriage'])
edge('retain_rule','3b:6','גזירה עבידא דבטלא ותקנתא דרבנן מקמי גזירה לא עקרינן',cr,qu,'answer');edge('tuesday_challenge','3b:6','אי הכי בשלישי נמי אתי ובעיל',qb,ct,'objection');edge('uncertainty_answer','3b:6','מספיקא לא עקר נפשיה',cn,qb,'answer')
core=['3b:'+str(n) for n in range(1,7)];coverage=[]
for ref in core:
 sid=byref[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Manual source pass: '+ref+'; '+('exact full-character ownership' if layer=='structure' else 'source-local findings recorded; continuation through 4b:12 read to distinguish later topics')
  if not ids:rationale='Manual '+layer+' pass: '+ref+'; '+('reread wording, conditions, questions, anonymity, Rabbah/Rava distinction, and downstream coercion/mourning continuation; no additional omitted unit identified in this core' if layer=='reconciliation' else 'no separate '+layer+' finding beyond recorded material; no named attribution invented')
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=r.current(job)['open_tails'])
r.validate_apply(r.current(job),p,segments,j)
path=out/'batch001_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'batch001_receipt.json',r.encoded(receipt));print(receipt)
