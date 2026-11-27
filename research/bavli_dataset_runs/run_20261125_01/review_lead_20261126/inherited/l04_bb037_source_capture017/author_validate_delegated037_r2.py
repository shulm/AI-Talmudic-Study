import json, hashlib, re, sys
from pathlib import Path
from collections import Counter
import jsonschema

OUT=Path(__file__).resolve().parent
JOB=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_bava_batra_delegated037.json')
EXPECTED='107078be4e24ffe632ce74e2b62084e784ddf0269add939bcfc5795f847d65cb'
AGENT='/root/bb_source_review037'
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
j=read(JOB); assert sha(JOB.read_bytes())==EXPECTED
bindings=[j['source'],*j['common_documents'],j['frozen_plan'],j['original_source_schema']]
for x in bindings: assert sha(Path(x['path']).read_bytes())==x['sha256'], x['path']
plan=read(j['frozen_plan']['path']); p0={k:v for k,v in plan.items() if k!='plan_sha256'}
assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(p0,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())==j['plan_sha256']==plan['plan_sha256']
block=next(b for b in plan['review_blocks'] if b['block_id']=='block_000028')
assert [x['ref'] for x in block['spans']]==j['core_refs']==j['selected_blocks'][0]['core_refs']
assert block['roles']==j['selected_blocks'][0]['roles']==['probability_sample']
src=read(j['source']['path']); schema=read(j['common_documents'][1]['path'])
def text(ref):
 m=re.fullmatch(r'Bava Batra (\d+)([ab]):(\d+)',ref); return src['text'][int(m[1])*2-2+(m[2]=='b')][int(m[3])-1]
for x in block['spans']:
 t=src['text'][x['page_index']][x['segment_index']]; assert t==text(x['ref']); assert [0,len(t)]==x['offsets_codepoints']; assert sha(t.encode())==x['span_sha256_utf8']
R=[]; names={}
def ev(ref,q=None):
 if not ref.startswith('Bava'): ref='Bava Batra '+ref
 t=text(ref); q=t if q is None else q; a=t.index(q); assert q
 return dict(segment_id=ref,start_char=a,end_char=a+len(q),quote=q)
def add(key,layer,e,content,unc=None,links=None,origin='source_paraphrase'):
 rid='bb037r2.'+key; assert key not in names; names[key]=rid
 R.append(dict(id=rid,layer=layer,evidence=e,content=content,origin=origin,uncertainty=unc or [],links=links or [])); return rid
def utt(key,ref,q,voice,role='assertion',unc=None): return add(key,'utterances',[ev(ref,q)],dict(textual_voice=voice,discourse_role=role,composition='atomic'),unc)
def attr(key,ref,q,surface,role,scope,chain=None,unc=None):
 return add(key,'attributions',[ev(ref,q)],dict(surface=surface,role=role,candidates=[surface] if role!='anonymous' else [],scope=scope,transmission_chain=chain or []),unc)
def question(key,ref,q,form,voice='anonymous',explicit=True):
 utt(key+'u',ref,q,voice,'question'); return add(key,'questions',[ev(ref,q)],dict(formulation=form,question_origin='explicit' if explicit else 'editorial_reconstruction',conditions=[],answer_set_status='partial'),origin='source_paraphrase' if explicit else 'editorial_inference')
def claim(key,ref,q,prop,holder='anonymous',cond=None,status='asserted locally; no later halakhic ruling inferred',mode='asserted',question=None,unc=None):
 e=[ev(ref,q)]; u=utt(key+'u',ref,q,holder,mode,unc)
 c=add(key,'claims',e,dict(proposition=prop,conditions=cond or [],scope='local passage '+ref,assertion_mode=mode),unc,[u])
 add(key+'p','positions',e,dict(holder_candidates=[] if holder=='anonymous' else [holder],claim_id=c,question_id=names[question] if question else None,conditions=cond or [],local_status=status),unc,[c]+([names[question]] if question else []))
 return c
def edge(key,a,b,rel,ref,q,explicit=True):
 return add(key,'edges',[ev(ref,q)],dict(source_id=names[a],target_id=names[b],relation=rel,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),links=[names[a],names[b]],origin='source_paraphrase' if explicit else 'editorial_inference')

titles=['Allocation of lodging and courtyard manure','Rav Huna: obstruction opposite doorway','Objection: graded use by five courtyards','Continuation: innermost courtyard','Tannaitic explanation and quoted baraita','Missing-text reconstruction of baraita','Reopening a blocked entrance; frame qualification','Supporting baraita: blocked house and four cubits','Impurity rules; parenthesized tomb wording preserved','Through alleys to another city; alternative road']
for ref,title in zip(j['core_refs'],titles):
 add('s'+ref.split()[-1].replace(':','_'),'structure',[ev(ref)],dict(title=title,primary=True,boundary='open_both' if ref in ['Bava Batra 11b:8','Bava Batra 11b:12','Bava Batra 12a:1','Bava Batra 12a:3'] else 'open_left' if ref in ['Bava Batra 11b:6','Bava Batra 11b:9','Bava Batra 12a:2'] else 'closed',legacy_ids=[]))

# Context dialogue anchors are not sampled cores.
utt('ctx_dialogue','11b:5',None,'Rav Huna and Rabbi Ami','question and answer context')
attr('ctx_asker','11b:5','בעא מיניה רב הונא מרבי אמי','רב הונא','speaker','questioner of continuing dialogue')
attr('ctx_answerer','11b:5','בעא מיניה רב הונא מרבי אמי','רבי אמי','speaker','respondent of continuing dialogue')
question('lodgingq','11b:6','אכסניא לפי בני אדם מתחלקת או לפי פתחים מתחלקת','Is lodging allocated by persons or doorways?','Rav Huna, inherited from preceding dialogue')
claim('lodging','11b:6','אמר ליה לפי בני אדם מתחלקת','Lodging is allocated by persons.','רבי אמי',question='lodgingq',unc=['Speaker inherited from 11b:5, not named again in this segment.'])
attr('ami','11b:6','אמר ליה','רבי אמי','speaker','lodging answer; inherited dialogue',unc=['Identification uses preceding original source, not name order.'])
attr('hunaq','11b:6','אכסניא לפי בני אדם מתחלקת או לפי פתחים מתחלקת','רב הונא','speaker','lodging question; inherited dialogue',unc=['Questioner inferred from continuous exchange at 11b:5.'])
utt('lodgingsupport','11b:6','תניא נמי הכי','anonymous','citation-introduction supporting answer')
claim('manure','11b:6','זבל שבחצר מתחלקת לפי פתחים','Courtyard manure is allocated by doorways.','anonymous baraita')
claim('lodgingbar','11b:6','תניא נמי הכי זבל שבחצר מתחלקת לפי פתחים אכסניא לפי בני אדם','Lodging is allocated by persons.','anonymous baraita')
attr('lodgingtanna','11b:6','תניא נמי הכי','anonymous baraita','quoted_authority','manure and lodging rules')
edge('lodginganswer','lodging','lodgingq','answer','11b:6','אמר ליה לפי בני אדם מתחלקת')
edge('lodgingsupp','lodgingbar','lodging','support','11b:6','תניא נמי הכי')
edge('dialoguecontinuation','ctx_dialogue','lodgingq','continuation','11b:6','אכסניא לפי בני אדם מתחלקת או לפי פתחים מתחלקת',False)

claim('obstruction','11b:7','אחד מבני מבוי שבקש לסתום כנגד פתחו בני מבוי מעכבין עליו','Alley residents may prevent a resident from blocking the space opposite his doorway.','רב הונא',['resident seeks to block opposite his doorway'],status='challenged at 11b:8; reconciled as tannaitic disagreement at 11b:10')
claim('distance','11b:7','שמרבה עליהן את הדרך','The proposed obstruction increases their route.','רב הונא',['obstruction opposite doorway'])
attr('huna','11b:7','אמר רב הונא','רב הונא','speaker','obstruction rule and rationale')
edge('distancerationale','distance','obstruction','support','11b:7','שמרבה עליהן את הדרך')
question('objectionq','11b:8','מיתיבי','How can the obstruction ruling stand against the baraita of graded courtyard use?',explicit=False)
attr('objector','11b:8','מיתיבי','anonymous','anonymous','baraita objection to Rav Huna')
claim('outerall','11b:8','כולן משתמשות עם החיצונה','All five courtyards use the outermost portion together.','anonymous cited baraita',['five courtyards opening to an alley'],status='cited objection; later attributed to Rabbi in reconstructed baraita')
claim('outerself','11b:8','והחיצונה משתמשת לעצמה','The outermost courtyard uses its own portion only.','anonymous cited baraita',['five courtyards opening to an alley'],status='cited objection; later attributed to Rabbi')
claim('secondall','11b:8','והשאר משתמשות עם השניה','The remaining courtyards share use with the second.','anonymous cited baraita',['five courtyards opening to an alley'])
claim('secondself','11b:8','והשניה משתמשת לעצמה','The second courtyard uses its own portion.','anonymous cited baraita',['five courtyards opening to an alley'])
claim('secondouter','11b:8','ומשתמשת עם החיצונה','The second also uses the outermost portion.','anonymous cited baraita',['five courtyards opening to an alley'])
claim('innerself','11b:9','נמצאת פנימית משתמשת לעצמה','The innermost courtyard consequently uses its own portion.','anonymous cited baraita',['five courtyards opening to an alley'])
claim('innerall','11b:9','ומשתמשת עם כל אחת ואחת','The innermost courtyard also shares use with each of the others.','anonymous cited baraita',['five courtyards opening to an alley'])
attr('baraita8','11b:8','מיתיבי חמש חצרות פתוחות למבוי','anonymous cited baraita','quoted_authority','graded use rules continued in 11b:9')
attr('baraita9','11b:9',None,'anonymous cited baraita','quoted_authority','continuation of graded courtyard use')
edge('objection','outerself','obstruction','objection','11b:8','מיתיבי')
edge('innercontinuation','innerall','outerall','continuation','11b:9','נמצאת פנימית משתמשת לעצמה ומשתמשת עם כל אחת ואחת')

claim('tannaitic','11b:10','תנאי היא','The conflict reflects tannaitic disagreement.','anonymous',status='local reconciliation of objection',mode='reconciled')
claim('reroute','11b:10','אחד מבני מבוי שבקש להחזיר פתחו למבוי אחר בני מבוי מעכבין עליו','Alley residents may prevent a resident from redirecting his entrance to another alley.','רבי',['resident redirects doorway to another alley'])
claim('reopen','11b:10','היה סתום ובקש לפותחו אין בני מבוי מעכבין עליו','Residents cannot prevent reopening a blocked entrance.','רבי',['formerly blocked entrance'],status='qualified by Rava at 11b:12')
claim('shared','11b:10','ר"ש בן אלעזר אומר חמש חצרות הפתוחות למבוי כולן משתמשות במבוי זו עם זו','All five courtyards opening to the alley share use with one another.','רבי שמעון בן אלעזר',['five courtyards opening into an alley'])
attr('rabbi10','11b:10','דברי רבי','רבי','position_holder','preceding entrance rules in cited baraita')
attr('rsa10','11b:10','ר"ש בן אלעזר אומר','רבי שמעון בן אלעזר','speaker','mutual use of alley')
attr('anon10','11b:10','תנאי היא','anonymous','anonymous','tannaitic reconciliation')
edge('reconcile','tannaitic','objectionq','local_resolution','11b:10','תנאי היא')
edge('sharedsupport','shared','obstruction','support','11b:10','תנאי היא',False)
question('courtyardq','11b:11','חצרות מאן דכר שמייהו','Where were courtyards mentioned in the first part of this baraita?')
utt('reconstruction','11b:11','חסורי מחסרא והכי קתני','anonymous','missing-text reconstruction')
claim('missingtext','11b:11','חסורי מחסרא והכי קתני','The baraita is missing a clause and is to be taught with the supplied courtyard clause.','anonymous',status='textual repair proposed and used locally')
claim('rabbiouterall','11b:11','כולן משתמשות עם החיצונה','All five courtyards use the outermost portion together.','רבי',['five courtyards opening to an alley'],status='explicitly attributed in reconstructed baraita')
claim('rabbiouterself','11b:11',"והחיצונה משתמשת לעצמה וכו'",'The outermost courtyard uses its own portion only; the remaining rules are abbreviated by וכו\'.','רבי',['five courtyards opening to an alley'],status='reconstructed baraita; abbreviated continuation preserved, not filled in as literal evidence')
claim('shared11','11b:11','ר\' שמעון בן אלעזר אומר חמש חצרות הפתוחות למבוי כולן משתמשות במבוי','All five courtyards use the alley.','רבי שמעון בן אלעזר',['five courtyards opening to an alley'],status='restated in reconstructed baraita')
attr('rabbi11','11b:11','דברי רבי','רבי','position_holder','graded-use clause in reconstructed baraita')
attr('rsa11','11b:11',"ר' שמעון בן אלעזר אומר",'רבי שמעון בן אלעזר','speaker','all-courtyards alley use')
attr('anon11','11b:11','חסורי מחסרא והכי קתני','anonymous','anonymous','missing-text reconstruction')
edge('reconstructionanswer','missingtext','courtyardq','answer','11b:11','חסורי מחסרא והכי קתני')
edge('repair','missingtext','shared','correction','11b:11','חסורי מחסרא והכי קתני')
edge('rabbiattribution','rabbiouterall','outerall','quotation','11b:11','וכן חמש חצרות הפתוחות למבוי כולן משתמשות עם החיצונה')

claim('reopenquote','11b:12','אמר מר היה סתום ובקש לפותחו אין בני מבוי מעכבין עליו','The cited ruling permits reopening the blocked entrance without residents preventing it.','רבי',['blocked entrance'],status='quoted lemma immediately qualified by Rava')
claim('frameintact','11b:12','לא שנו אלא שלא פרץ את פצימיו','The non-objection rule applies only when the doorposts have not been breached.','רבא',['blocked entrance','doorposts not breached'],status='local qualification',mode='conditional')
claim('framebroken','11b:12','אבל פרץ את פצימיו בני מבוי מעכבין עליו','If he breached the doorposts, the alley residents may prevent reopening.','רבא',['doorposts breached'],status='local qualification',mode='conditional')
utt('abayesupport','11b:12','אמר ליה אביי לרבא תניא דמסייע לך','אביי','announcement of supporting baraita')
attr('rava','11b:12','אמר רבא','רבא','speaker','qualification of reopening rule')
attr('abaye','11b:12','אמר ליה אביי לרבא','אביי','speaker','introduces baraita supporting Rava')
attr('mar','11b:12','אמר מר','רבי','quoted_authority','repeated baraita lemma, attribution from 11b:10')
edge('reopenquotation','reopenquote','reopen','quotation','11b:12','אמר מר היה סתום ובקש לפותחו אין בני מבוי מעכבין עליו')
edge('qualify','frameintact','reopenquote','qualification','11b:12','לא שנו אלא שלא פרץ את פצימיו')
edge('contrast','framebroken','frameintact','distinction','11b:12','אבל פרץ את פצימיו בני מבוי מעכבין עליו')
claim('house4','12a:1',"בית סתום יש לו ד' אמות",'A closed house retains four cubits.','anonymous baraita cited by Abaye',['closed house'],status='supporting baraita, not a direct saying of Abaye')
claim('house0','12a:1',"פרץ את פצימיו אין לו ד' אמות",'If the doorposts were breached it does not retain four cubits.','anonymous baraita cited by Abaye',['doorposts breached'])
attr('baraitahouse','12a:1',None,'anonymous baraita','quoted_authority','house-space rule introduced by Abaye at 11b:12')
edge('supportframe','house4','frameintact','support','11b:12','תניא דמסייע לך')
edge('supportbroken','house0','framebroken','support','11b:12','תניא דמסייע לך')
edge('housesdistinction','house0','house4','distinction','12a:1',None)

claim('tombclosed','12a:2','קבר שפתחו סתום אינו מטמא כל סביביו','A tomb with a closed opening does not impart impurity all around.','anonymous baraita',['tomb opening closed'],unc=['Parenthesized wording in this edition; not silently substituted for the following house wording.'])
claim('tombbroken','12a:2','פרץ את פצימיו וסתמו מטמא כל סביביו','If its doorposts were breached and it was sealed, the tomb imparts impurity all around.','anonymous baraita',['doorposts breached','then sealed'],unc=['Parenthesized textual formulation; source gives no named variant authority.'])
claim('impurityhouse','12a:2','בית סתום אינו מטמא כל סביביו','A closed house does not impart impurity all around.','anonymous baraita',['closed house'],unc=['The relevant corpse/impurity setting is implicit; source does not spell it out here.'])
claim('impuritybroken','12a:2','פרץ את פצימיו מטמא כל סביביו','If its doorposts were breached it imparts impurity all around.','anonymous baraita',['doorposts breached'],unc=['Unparenthesized house wording does not repeat וסתמו.'])
attr('impuritybaraita','12a:2',None,'anonymous baraita','quoted_authority','continued baraita; parenthesized and unparenthesized impurity formulations')
edge('tombdistinction','tombbroken','tombclosed','distinction','12a:2','פרץ את פצימיו וסתמו מטמא כל סביביו')
edge('impuritydistinction','impuritybroken','impurityhouse','distinction','12a:2','פרץ את פצימיו מטמא כל סביביו')
edge('impurityanalogy','impurityhouse','house4','analogy','12a:2',None,False)

claim('othercity','12a:3','מבואות המפולשות לעיר אחרת ובקשו בני העיר לסותמן בני אותה העיר מעכבין עליהן','Residents of the other city may prevent blocking through alleys leading to their city.','רבי יוחנן',['through alleys leading to another city','local residents seek to block them'])
claim('noroute','12a:3','לא מיבעי כי ליכא דרכא אחרינא דמעכבי','They may prevent closure when there is no other route.','רבי יוחנן',['no alternative route'],status='easy case in explanatory expansion; not separately marked as a new named statement',unc=['The scope of the named report versus anonymous explanation is not explicitly delimited.'])
claim('withroute','12a:3','אלא אפילו כי איכא דרכא אחרינא נמי מעכבי','They may prevent closure even when there is another route.','רבי יוחנן',['alternative route exists'],status='stronger case in explanatory expansion',unc=['The scope of the named report versus anonymous explanation is not explicitly delimited.'])
attr('rbbh','12a:3','אמר רבה בר בר חנה א"ר יוחנן','רבה בר בר חנה','transmitter','through-alley ruling',['רבה בר בר חנה','רבי יוחנן'])
attr('yohanan','12a:3','א"ר יוחנן','רבי יוחנן','position_holder','through-alley ruling',['רבה בר בר חנה','רבי יוחנן'])
edge('evenalternative','withroute','noroute','qualification','12a:3','אלא אפילו כי איכא דרכא אחרינא נמי מעכבי')
claim('publicroute','12a:4','מצר שהחזיקו בו רבים אסור לקלקלו','A boundary route held by the public may not be damaged.','רב',['public have established possession/use'],status='context-only rationale for through-alley ruling')
attr('yehuda','12a:4','דרב יהודה אמר רב','רב יהודה','transmitter','public-route rule',['רב יהודה','רב'])
attr('rav','12a:4','דרב יהודה אמר רב','רב','position_holder','public-route rule',['רב יהודה','רב'])
claim('giddel','12a:4','רבים שבררו דרך לעצמן מה שבררו בררו','A route selected by the public remains their selected route.','רב גידל',['public select a route'],status='parenthesized context formulation; not conflated with Rav report',unc=['Parenthesized text retained without deciding its textual history.'])
attr('giddelattr','12a:4','דא"ר גידל','רב גידל','quoted_authority','parenthesized public-route rationale')
edge('routerationale','publicroute','withroute','support','12a:4','משום דרב יהודה אמר רב')
edge('giddelrationale','giddel','withroute','support','12a:4','כדרב גידל',False)

notes={
'11b:6':'Checked allocation alternatives, inherited dialogue speakers, both baraita rules, and explicit support. No named dispute manufactured from the question alternatives.',
'11b:7':'Checked actor, requested obstruction, residents\' objection power, and route-length rationale. Objection and tannaitic resolution preserved in following cores.',
'11b:8':'Checked five courtyards, outer and second courtyard rights separately; objection is not an enduring anonymous position against Rav Huna. The implicit objection question is labeled editorial reconstruction.',
'11b:9':'Checked both innermost rights as continuation of preceding cited baraita, not a new named speaker or additional dispute.',
'11b:10':'Checked reconciliation, both entrance cases, Rabbi attribution, and R. Shimon b. Elazar\'s shared-use position; repair follows, so initial incomplete formulation is retained as an occurrence.',
'11b:11':'Checked explicit question, missing-text repair, Rabbi\'s added courtyard clause, וכו abbreviation and repeated R. Shimon clause. No silent expansion of abbreviation into literal quotation.',
'11b:12':'Checked quoted lemma, Rava\'s two conditional branches, Abaye\'s supporting introduction and continuation. Abaye is not made the author of the baraita.',
'12a:1':'Checked retained/lost four-cubit claims with doorpost condition and prior Abaye support. No independently explicit question in this segment.',
'12a:2':'Checked every impurity clause; preserved parenthesized tomb formulation including וסתמו and following house wording separately. No invented named textual witnesses or automatic identity of conditions.',
'12a:3':'Checked reporter versus holder, city roles, both route cases, rationale in 12a:4 and distinction from subsequent Shmuel report. Named-report boundary uncertainty retained; no Rav–Shmuel dispute inferred.'}
coverage=[]
for ref in j['core_refs']:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if r['layer']==layer and any(e['segment_id']==ref for e in r['evidence'])]
  rationale=notes[ref.split()[-1]] if layer=='reconciliation' else ('Source-based pass found the listed records.' if ids else 'Source-based pass found no separate '+layer+' record here; '+notes[ref.split()[-1]])
  coverage.append(dict(segment_id=ref,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
proposal=dict(schema_version='2.0.0-production',tractate='Bava Batra',owner=AGENT,epoch=1,source_sha256=j['source']['sha256'],protocol_sha256=j['common_documents'][0]['sha256'],schema_sha256=j['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id=AGENT,model_id=None),records=R,coverage=coverage,open_tails=[])
artifact=dict(artifact_kind='frozen_independent_source_only_reading',supersedes_artifact_sha256='b8f404704770c73b6bdd7cd3126b3b59ef8292bd18e8a8dbf9c34b82c598508f',revision_reason='Before comparison, source-only audit corrected lodging baraita evidence from repeated opening-question substring to the full explicit supporting citation. Original artifact retained immutable. Provenance wording clarified to avoid any implication of human authorship.',job_id=j['job_id'],job_sha256=EXPECTED,agent_id=AGENT,model_id=None,provenance='Fresh independent agent context; semantic inventory manually composed by interactive AI reviewer encoded by deterministic helper; no paid API calls, producer annotations, comparisons, previous readings, lane handoffs or production pins accessed.',blindness=dict(scope=j['core_refs'],source_only=True,frozen_before_comparison=True),release_scope='Additive next-release evidence only; no release015 mutation, production admission, full tractate review or task eligibility.',ml_eligible=False,source_metadata={k:v for k,v in src.items() if k!='text'},bindings=bindings,plan_sha256=j['plan_sha256'],block_id='block_000028',core_refs=j['core_refs'],sampled_core_count=10,context=dict(evidence_refs=['Bava Batra 11b:5','Bava Batra 12a:4'],read_refs=['Bava Batra 11b:'+str(i) for i in range(1,6)]+['Bava Batra 12a:'+str(i) for i in range(4,16)],note='Read surrounding original page segments for boundaries; only 11b:5 and 12a:4 needed for evidence. Context never counted as sampled cores. Subsequent Shmuel/public-domain discussion is separate.'),coordinate_contract='Original source array coordinates; segment_id is original canonical reference; Python Unicode codepoint half-open offsets including all markup/parentheses.',original_spans=block['spans'],proposal=proposal,limitations=['AI provisional source-only reading; no human certification.','No producer comparison/adjudication performed.','Mechanical validation establishes fidelity/schema/coverage, not scholarly correctness.','Owner/epoch fields identify isolated review container only and confer no production ownership.'])

def validate(a):
 p=a['proposal']; jsonschema.Draft202012Validator(schema).validate(p)
 ids={r['id'] for r in p['records']}; assert len(ids)==len(p['records'])
 evidence_count=0
 for r in p['records']:
  for e in r['evidence']:
   assert text(e['segment_id'])[e['start_char']:e['end_char']]==e['quote']; evidence_count+=1
  assert set(r['links'])<=ids
  for k in ['source_id','target_id','claim_id','question_id']:
   if r['content'].get(k) is not None: assert r['content'][k] in ids
 for ref in j['core_refs']:
  intervals=sorted((e['start_char'],e['end_char']) for r in p['records'] if r['layer']=='structure' and r['content']['primary'] for e in r['evidence'] if e['segment_id']==ref)
  cursor=0
  for start,end in intervals: assert start==cursor; cursor=end
  assert cursor==len(text(ref))
 assert len(p['coverage'])==80 and len({(c['segment_id'],c['layer']) for c in p['coverage']})==80
 for c in p['coverage']:
  assert c['rationale']; assert set(c['record_ids'])<=ids
  assert set(c['record_ids'])=={r['id'] for r in p['records'] if r['layer']==c['layer'] and any(e['segment_id']==c['segment_id'] for e in r['evidence'])}
 return dict(result='PASS',records=len(p['records']),counts_by_layer=dict(Counter(r['layer'] for r in p['records'])),evidence_spans=evidence_count,core_segments=10,context_evidence_segments=2,coverage_rows=80,reconciliation_rows=10,primary_partitions=10,descriptor_file_hash_checks=7,canonical_plan_hash_verified=True,selected_span_hash_checks=10,unique_ids=True,internal_links=True,unicode_exact_quotes=True,json_schema_valid=True,comparison_performed=False,ml_eligible=False)

payload=json.dumps(artifact,ensure_ascii=False,indent=2).encode('utf-8')+b'\n'
dest=OUT/'bava_batra_delegated037.r2.json'
if '--verify' in sys.argv:
 assert dest.read_bytes()==payload
else:
 with dest.open('xb') as f:f.write(payload)
receipt=validate(read(dest)); receipt.update(artifact_path=str(dest),artifact_sha256=sha(dest.read_bytes()),helper_path=str(Path(__file__).resolve()),helper_sha256=sha(Path(__file__).read_bytes()),validator='Python jsonschema Draft202012Validator plus explicit source/plan/offset/partition/link/coverage assertions',agent_id=AGENT)
if '--verify' not in sys.argv:
 (OUT/'bava_batra_delegated037.r2.json.sha256').write_text(sha(payload)+'  bava_batra_delegated037.r2.json\n',encoding='ascii')
 with (OUT/'validation_delegated037.r2.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2); f.write('\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
