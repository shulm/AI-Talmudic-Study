import json,hashlib
from pathlib import Path
root=Path.cwd();job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');out=root/'research/bavli_dataset_runs/run_20261125_01/lanes/L03/kiddushin/bounded_001_20261127'
read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'));sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
assert read(job/'OWNER.json')=={'owner':'/root/lead_l01_l03','epoch':1}
assert not (job/'CURRENT.json').exists(),'Unexpected checkpoint; stop before promotion'
active=read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json'); cp=root/active['contract_path'];assert sha(cp)==active['contract_sha256'];c=read(cp)
for f,h in c['production_files'].items():assert sha(root/f)==h,f
src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Kiddushin/Hebrew/Wikisource Talmud Bavli.json');ss=Path('F:/Sefaria-Export-master/schemas/Kiddushin.json')
assert sha(src)=='daf594dcc08ac2763187d84655f905d14fe94be566b723bff6bb95e6c33f138f'
assert sha(ss)=='1b6caf35127f21fd71f7bafbd61218e6b8c9d75d6f174f94329151c74d6fe02c'
assert sha(root/'research/bavli_sugya_corpus_v1/source_manifest.json')==c['source_manifest_sha256']
# Load schema and protocol exactly as pinned, not an alternative schema.
schema=read(root/'research/bavli_production_v1/schema.json');protocol=(root/'research/bavli_production_v1/PROTOCOL.md').read_text(encoding='utf-8');assert len(schema['properties']['records']['items']['allOf'])==7
pins=dict(run_id=active['run_id'],contract_sha256=sha(cp),production_git_commit=c['production_git_commit'],schema_sha256=c['schema_sha256'],protocol_sha256=c['annotation_protocol_sha256'],source_path=str(src),source_sha256=sha(src),source_schema_path=str(ss),source_schema_sha256=sha(ss),source_manifest_sha256=c['source_manifest_sha256'],owner=read(job/'OWNER.json'),delegation='L03 lead explicitly delegated one bounded production batch under existing owner; actual agent /root/yevamot; no handoff',initial_state='No CURRENT.json; replay returned empty state, 0/2406 each layer',source_first_independence='No central Kiddushin reading or interpretations accessed before freezing this proposal.')
(out/'PINS.json').write_text(json.dumps(pins,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
w=read(job/'context_bounded001_20261127.json');seg=w['segments'];assert seg[9]['ref']=='Kiddushin 2b:5';p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['kid001.gemara'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='kid001.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Opening Mishnah and its acquisition/subject terminology discussion',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' in local source; no external normative conclusion inferred'),[c],u);return c
def q(k,inds,text):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('mishnah','structure',[0,1],dict(title='Marriage acquisition and release; money thresholds; levirate acquisition and release',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('gemara','structure',list(range(2,10)),dict(title='Opening Mishnah wording: acquisition terminology and female grammatical subject; wording discussion continues into number and דרך',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')
rec('terminology','structure',list(range(2,7)),dict(title='נקנית versus מקדש: money derivation and Torah/rabbinic terminology',primary=False,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('subject','structure',[7,8,9],dict(title='Female subject explained by self-release, death of husband and alternative consent reading',primary=False,boundary='closed',legacy_ids=[]),origin='editorial_inference')
# Explicit utterance spans separate the school statements, anonymous questions and replies.
utterances=[('u.mishnah_intro',[(0,'נקנית בשלוש דרכים וקונה את עצמה בשתי דרכים נקנית בכסף בשטר ובביאה')],'anonymous Mishnah','Enumeration of acquisition and release methods','composite'),('u.shammai',[(0,'בית שמאי אומרים בדינר ובשווה דינר')],'Beit Shammai','Money amount and equivalent value','composite'),('u.hillel',[(0,'ובית הלל אומרים בפרוטה ובשווה פרוטה')],'Beit Hillel','Alternative money amount and equivalent value','composite'),('u.pruta',[(0,'וכמה היא פרוטה אחד משמונה באיסר האיטלקי')],'anonymous Mishnah','Question and valuation answer','composite'),('u.release',[1],'anonymous Mishnah','Marriage release and levirate acquisition/release','composite')]
roles={2:'Contrast with האיש מקדש and initial money explanation',3:'Question on monetary basis and קיחה verbal analogy',4:'Acquisition terminology from Abraham’s field',5:'Alternative Jeremiah citation and wording conclusion',6:'Question about later wording; Torah/rabbinic distinction and consecration analogy',7:'Question about male subject here; coordination with self-release clause',8:'Proposal for male acquisition/release subject; death-of-husband objection',9:'Alternative explanation: acquisition requires her consent'}
for i,role in roles.items():utterances.append(('u'+str(i),[i],'anonymous Gemara',role,'composite'))
for k,inds,voice,role,comp in utterances:rec(k,'utterances',inds,dict(textual_voice=voice,discourse_role=role,composition=comp))
rec('a.mishnah','attributions',[0,1],dict(surface='מתני׳',role='anonymous',candidates=[],scope='Anonymous frame, methods, valuation and release; school-specific monetary views separately scoped',transmission_chain=[]))
for k,quote,can in [('a.shammai','בית שמאי אומרים בדינר ובשווה דינר','Beit Shammai'),('a.hillel','ובית הלל אומרים בפרוטה ובשווה פרוטה','Beit Hillel')]:rec(k,'attributions',[(0,quote)],dict(surface=quote,role='collective',candidates=[can],scope='Monetary acquisition amount and equivalent value',transmission_chain=[]))
for i,role in roles.items():rec('a'+str(i),'attributions',[i],dict(surface='anonymous Gemara',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
a=claim('three',[0],'The Mishnah lists three ways to effect the marriage acquisition.',holder='anonymous Mishnah')
b=claim('two',[0,1],'The Mishnah lists two ways for the woman to regain her independent status.',holder='anonymous Mishnah')
methods=[]
for k,quote,prop in [('money','נקנית בכסף','Marriage acquisition is effected by money.'),('document','בשטר','Marriage acquisition is effected by a document.'),('intercourse','ובביאה','Marriage acquisition is effected by intercourse.')]:
 cid=claim(k,[(0,quote)],prop,holder='anonymous Mishnah');methods.append(cid);edge(k+'.enumerates',[(0,quote)],cid,a,'qualification')
sh=claim('shammai',[(0,'בית שמאי אומרים בדינר ובשווה דינר')],'For monetary acquisition, Beit Shammai state a dinar or its equivalent value.',cond=['Money method'],holder='Beit Shammai')
hi=claim('hillel',[(0,'ובית הלל אומרים בפרוטה ובשווה פרוטה')],'For monetary acquisition, Beit Hillel state a perutah or its equivalent value.',cond=['Money method'],holder='Beit Hillel')
edge('shammai_scope',[(0,'בית שמאי אומרים בדינר ובשווה דינר')],sh,methods[0],'qualification');edge('hillel_scope',[(0,'ובית הלל אומרים בפרוטה ובשווה פרוטה')],hi,methods[0],'qualification')
qp=q('perutah_q',[(0,'וכמה היא פרוטה')],'What is the value of a perutah?')
pc=claim('perutah_value',[(0,'אחד משמונה באיסר האיטלקי')],'A perutah is one eighth of an Italian issar.',holder='anonymous Mishnah');edge('perutah_answer',[(0,'וכמה היא פרוטה אחד משמונה באיסר האיטלקי')],pc,qp,'answer')
for k,quote,prop in [('get','וקונה את עצמה בגט','She regains independent status through a get.'),('husband_death','ובמיתת הבעל','She regains independent status upon her husband’s death.')]:
 cid=claim(k,[(1,quote)],prop,holder='anonymous Mishnah');edge(k+'.enumerates',[(1,quote)],cid,b,'qualification')
yb=claim('yevamah_acquisition',[(1,'היבמה נקנית בביאה')],'The yevamah’s levirate acquisition is effected by intercourse.',holder='anonymous Mishnah')
yh=claim('yevamah_halitzah',[(1,'וקונה את עצמה בחליצה')],'The yevamah regains independent status through halitzah.',holder='anonymous Mishnah')
yd=claim('yevamah_death',[(1,'ובמיתת היבם')],'The yevamah regains independent status upon the levir’s death.',holder='anonymous Mishnah')
q1=q('why_acquisition',[(2,'מאי שנא הכא דתני האשה נקנית ומ"ש התם דתני האיש מקדש')],'Why say the woman is acquired here but the man betroths in the other Mishnah?')
c1=claim('money_word',[(2,'משום דקא בעי למתני כסף')],'The acquisition wording is chosen because this Mishnah is to teach money.');edge('why_answer',[2],c1,q1,'answer')
q2=q('money_source',[(3,'וכסף מנא לן')],'What is the source for monetary acquisition?')
c2=claim('taking_analogy',[3],'The repeated קיחה language links taking a wife with taking the money for Ephron’s field.');edge('money_answer',[3],c2,q2,'answer');edge('money_basis',[3],c2,methods[0],'support')
c3=claim('purchase_name',[4],'Taking is called acquisition, as shown by the field Abraham acquired.');edge('purchase_support',[4],c3,c1,'support')
c4=claim('jeremiah',[5],'Alternatively, שדות בכסף יקנו supplies the money/acquisition terminology, hence האישה נקנית.');edge('alternative_support',[5],c4,c1,'support')
q3=q('later_acquires',[(6,'וניתני התם האיש קונה')],'Why not use the man acquires in the later Mishnah too?')
c5=claim('two_registers',[(6,'מעיקרא תני לישנא דאורייתא ולבסוף תני לישנא דרבנן')],'The earlier Mishnah uses Torah terminology and the later Mishnah rabbinic terminology.');edge('register_answer',[6],c5,q3,'answer')
q4=q('rabbinic_meaning',[(6,'ומאי לישנא דרבנן')],'What is the meaning of that rabbinic terminology?')
c6=claim('hekdesh',[(6,'דאסר לה אכולי עלמא כהקדש')],'The term betrothal indicates that she is forbidden to everyone else like consecrated property.');edge('rabbinic_answer',[6],c6,q4,'answer')
q5=q('here_man',[(7,'וניתני הכא האיש קונה')],'Why not make the man acquires the subject here?')
c7=claim('same_subject',[(7,'משום דקא בעי למיתנא סיפא וקונה את עצמה בדידה תנא נמי רישא בדידה')],'The opening uses her as subject because the closing clause has her regaining her own status.');edge('subject_answer',[7],c7,q5,'answer')
q6=q('man_both',[(8,'וניתני האיש קונה ומקנה')],'Why not say the man acquires and releases?')
c8=claim('death_not_transfer',[(8,'משום דאיכא מיתת הבעל דלאו איהו קא מקני מן שמיא הוא דמקני לה')],'The husband’s death is among the release methods; that release comes from heaven, not from his act of transfer.');edge('death_answer',[8],c8,q6,'answer')
c9=claim('coercion_hyp',[(9,'אי תנא קונה ה"א אפילו בעל כרחה')],'Saying he acquires could be understood to include acquisition against her will.','hypothetical')
c10=claim('consent',[(9,'תנא האשה נקנית דמדעתה אין שלא מדעתה לא')],'The woman is acquired teaches acquisition with her consent, not without it.');edge('consent_alternative',[9],c10,q5,'answer');edge('coercion_corrected',[9],c10,c9,'correction')
notes={0:'Reread all acquisition methods, both counts, each school’s value/equivalent alternative, explicit valuation question and exact one-eighth ratio. No independent exchange or practical ruling invented.',1:'Marriage and levirate subjects kept distinct; get versus halitzah and husband versus levir deaths preserved.',2:'The textual contrast is with an unnamed other Mishnah; no unverified external reference supplied.',3:'קיחה analogy and the pinned source’s printed verse labels preserved exactly, without silently correcting citations.',4:'Abraham’s field quotation supports terminology, not a new independently attributed human speaker.',5:'אי נמי preserved as alternative scriptural support; continuation from prior page preserved.',6:'Both explicit questions and their separate replies retained; Torah versus rabbinic register is terminology, not validity of marriage methods.',7:'Subject-choice explanation tied to self-release; no rule inferred from author psychology.',8:'Heaven attribution describes release on death; not a human transmission chain or new named speaker.',9:'ואי בעית אימא remains alternative answer; hypothetical coercion inference is corrected, consent/negation explicit. Subsequent 2b:6 shifts to number and דרך within continuing wording discussion.'}
for i in range(10):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=notes[i]+' Read context through Kiddushin 3a:1; only the ten assigned core segments counted. '
  rationale+=('Source-based omission/reconciliation reread completed.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass with exact evidence.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
f=out/'INITIAL_PROPOSAL.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'proposal_sha256':sha(f),'records':len(p['records']),'coverage_rows':len(p['coverage']),'core_segments':10,'source_first_initial_frozen':True},indent=2))
