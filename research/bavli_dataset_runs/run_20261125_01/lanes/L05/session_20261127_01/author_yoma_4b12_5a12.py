"""Bounded direct source reading, Yoma 4b:12–5a:12; shared schema only."""
import json,hashlib
from pathlib import Path
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
HERE=Path(__file__).resolve().parent
inv=json.loads((J/'source_inventory.json').read_bytes());job=json.loads((J/'JOB.json').read_bytes())
old='e5376e156d6a87fa559ffcf486c81f33a6933317ea90edbfd378f5f30289574b'
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
state=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
def ev(ii):return [dict(segment_id=inv[i]['id'],start_char=0,end_char=len(inv[i]['text']),quote=inv[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 rid='yom.s2701.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,links=list(links),origin=origin,uncertainty=list(unc)));return rid
def claim(k,ii,p,cond=(),mode='asserted',scope='',holder=None,unc=()):
 if isinstance(ii,int):ii=[ii]
 c=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[c],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[c],unc=unc)
 return c
def question(k,ii,p,conds):
 if isinstance(ii,int):ii=[ii]
 return add(k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=conds,answer_set_status='partial'))
def edge(k,ii,a,b,rel):
 if isinstance(ii,int):ii=[ii]
 return add(k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s=add('mil_required','structure',range(65,80),dict(title='מילואים: זיהוי בעלי המחלוקת ונפקא מינות בעיכוב',primary=True,boundary='open_both',legacy_ids=[]),unc=['Continues prior מילואים discussion; the grounds of the all-details rule continue at5a:13–5b:6 outside this completed core.'])
edge('tail_link',65,'yom.s03.origin',s,'continuation')
roles={65:'Inference from prior exchange; initial unnamed two-view report',66:'Explicit תסתיים identification using prior objection and non-response',67:'Question about practical difference',68:'Rav Yosef: laying on hands',69:'Question and baraita: blood versus laying on hands',70:'Continuation and qualified evaluation of omitted laying on hands',71:'Rav Nahman bar Yitzhak: waving',72:'Question and baraita: blood versus waving',73:'Rav Pappa: seven-day separation',74:'Preparation-versus-separation textual proof',75:'Ravina: seven-day investiture and anointing',76:'Question and baraita proof opening',77:'Cross-segment baraita: mixed seven-day/one-day cases',78:'Question on initial seven-day anointing requirement',79:'Two alternative sources for seven-day anointing'}
for i,role in roles.items():
 add('u'+str(i),'utterances',[i],dict(textual_voice='Named reports and anonymous discussion as individually annotated',discourse_role=role,composition='composite'))
 if i not in [68,71,73,75]:add('anon'+str(i),'attributions',[i],dict(surface='Anonymous Gemara / quoted baraita',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
c={};q={}
c['inference']=claim('inference',65,'The preceding exchange implies that both disputants in that exchange accept that everything written for the inauguration rites is indispensable.',scope='Inference concerning Rabbi Yohanan and Resh Lakish in preceding exchange; not identification of the two speakers in the separate report that follows.')
c['initialall']=claim('initialall',65,'In the reported dispute between Rabbi Yohanan and Rabbi Hanina, one says every written detail is indispensable in the inauguration rites.',cond=['Inauguration rites'],scope='Initial חד אמר report; the name is not assigned at this stage.')
c['initiallimited']=claim('initiallimited',65,'The other says that a detail indispensable for later generations is indispensable in the inauguration rites, while a detail not indispensable later is not indispensable there.',cond=['Distinguish what is indispensable for later generations'],scope='Initial וחד אמר report; full positive and negative criteria retained without name-order inference.')
for k,target in [('unnamedall',c['initialall']),('unnamedlimited',c['initiallimited'])]:
 add(k,'attributions',[65],dict(surface='חד אמר / וחד אמר',role='position_holder',candidates=['רבי יוחנן','רבי חנינא'],scope='Unresolved locally at4b:12; resolved by continuation, never by listed name order.',transmission_chain=[]),[target],unc=['Initial report is unnamed.'])
c['idproof']=claim('idproof',66,'Resh Lakish had challenged Rabbi Yohanan with “if like inauguration, everything written should be indispensable,” and Rabbi Yohanan did not answer that premise; this identifies Rabbi Yohanan as the all-details view.',scope='Explicit תסתיים proof, not an inference from name order.')
c['all']=claim('all',[65,66],'Rabbi Yohanan is identified as holding every written detail indispensable in the inauguration rites.',cond=['Inauguration rites'],scope='Explicit identification at4b:13 after initially unnamed report.',holder='רבי יוחנן')
c['limited']=claim('limited',[65,66],'Rabbi Hanina is the other participant, whose view limits indispensability in the inauguration rites to details indispensable for later generations.',cond=['Detail indispensable for later generations'],scope='Remaining member of the explicitly identified two-person report, not assignment by name order.',holder='רבי חנינא',unc=['Rabbi Hanina is identified by elimination after the explicit identification of Rabbi Yohanan; his name is not repeated in the תסתיים sentence.'])
add('rl_role','attributions',[66],dict(surface='רבי שמעון בן לקיש',role='quoted_authority',candidates=['ריש לקיש'],scope='Author of prior challenge used as evidence for Rabbi Yohanan identification; not the second member of the Yohanan–Hanina report.',transmission_chain=[]),[c['idproof']])
q['difference']=question('q.difference',67,'What practical difference is there between the two views?', ['Two views on indispensability of inauguration details, now identified'])
c['semikha']=claim('semikha',68,'Rav Yosef identifies laying on hands as a difference: it is indispensable under the all-written-details view and dispensable under the later-generations criterion.',cond=['Laying on hands in inauguration rites'],scope='First proposed practical difference',holder='רב יוסף')
q['semikhasource']=question('q.semikhasource',69,'From where is laying on hands known not to be indispensable for later generations?', ['Ordinary later-generation sacrifices','Needed for Rav Yosef’s proposed difference'])
q['semikhaatonement']=question('q.semikhaatonement',69,'Does laying on hands itself effect atonement, when atonement is only through blood?', ['Interpretation of וסמך ונרצה in cited baraita'])
c['blood']=claim('blood',69,'The baraita states that atonement is only through blood, citing כי הדם הוא בנפש יכפר.',scope='Quoted baraita argument, not erasure of the command of laying on hands.')
q['semikhaverse']=question('q.semikhaverse',70,'What then does וסמך ונרצה teach?', ['Blood effects atonement; interpretation must preserve the laying-on-hands command'])
c['semikhastatus']=claim('semikhastatus',[69,70],'If a person treats laying on hands as a dispensable remainder of the command, Scripture regards him “as if he did not atone, yet he atoned” (כאילו לא כפר וכפר).',cond=['Laying on hands treated as שירי מצוה'],scope='Keep both sides of the baraita wording: deficient command fulfillment does not cancel the blood’s atonement. No permission to neglect laying on hands is asserted.')
c['waving']=claim('waving',71,'Rav Nahman bar Yitzhak identifies waving as a difference: indispensable under the all-details view, dispensable under the later-generations criterion.',cond=['Waving in inauguration rites'],scope='Alternative practical difference',holder='רב נחמן בר יצחק')
q['wavesource']=question('q.wavesource',72,'From where is waving known not to be indispensable for later generations?', ['Later-generation waving','Needed for Rav Nahman bar Yitzhak’s proposed difference'])
q['waveatonement']=question('q.waveatonement',72,'Does waving itself effect atonement, when atonement is only through blood?', ['Interpretation of לתנופה לכפר in cited baraita'])
q['waveverse']=question('q.waveverse',72,'What then does לתנופה לכפר teach?', ['Blood effects atonement; waving command must still be accounted for'])
c['waveblood']=claim('waveblood',72,'The waving baraita repeats that only blood effects atonement, citing כי הדם הוא בנפש יכפר.',scope='Separate occurrence supporting the waving argument.')
c['wavestatus']=claim('wavestatus',72,'If a person treats waving as a dispensable remainder of the command, Scripture regards him “as if he did not atone, yet he atoned.”',cond=['Waving treated as שירי מצוה'],scope='Both negative evaluation and effective atonement retained; not permission to omit waving.')
c['separation']=claim('separation',73,'Rav Pappa identifies seven-day separation as a difference: indispensable under the all-details view, dispensable under the later-generations criterion.',cond=['Seven-day separation in inauguration rites'],scope='Another practical difference',holder='רב פפא')
q['separationsource']=question('q.separationsource',74,'From where is separation known not to be indispensable for later generations?', ['Seven-day separation; substitute priest prepared for service'])
c['prepare']=claim('prepare',74,'The Mishnah says the substitute is prepared (מתקינין), rather than separated (מפרישין), providing the proof that separation is not indispensable.',cond=['Preparation of substitute priest'],scope='Proof about non-indispensability, not a denial that initial separation is prescribed.')
c['invest']=claim('invest',75,'Ravina identifies seven days of investiture in vestments and seven days of anointing as differences: indispensable under the all-details view, dispensable under the later-generations criterion.',cond=['Seven-day investiture or anointing in inauguration rites'],scope='Two duration requirements retained; not total elimination of investiture/anointing.',holder='רבינא')
q['investsource']=question('q.investsource',76,'From where are the seven-day durations known not to be indispensable for later generations?', ['Investiture and anointing durations for succeeding priest'])
q['anointverse']=question('q.anointverse',76,'What is taught by אשר ימשח אותו ואשר ימלא את ידו?', ['Baraita concerning priest succeeding his father'])
c['sevenboth']=claim('sevenboth',[76,77],'The seven-day garment verse initially establishes the case of seven days of investiture and seven days of anointing.',cond=['Successor priest','Seven days in both procedures'],scope='Starting case in the baraita, followed by expanded mixed-duration cases.')
q['mixed']=question('q.mixed',77,'From where are seven days of investiture with one day of anointing, or one day of investiture with seven days of anointing, included?', ['Successor priest','Exactly the two mixed-duration cases named by the baraita'])
c['mixed']=claim('mixed',[76,77],'אשר ימשח אותו ואשר ימלא את ידו includes the stated mixed cases: seven days of investiture with one day of anointing, and one day of investiture with seven days of anointing.',cond=['Seven-day investiture plus one-day anointing, OR one-day investiture plus seven-day anointing'],scope='Inclusion regardless of completion of both seven-day durations; does not invent an explicitly stated one-day/one-day case.')
q['initialseven']=question('q.initialseven',78,'Seven days of initial investiture have been established; from where are seven days of initial anointing derived?', ['Initial prescribed procedure, distinct from whether shortened duration invalidates'])
c['deduction']=claim('deduction',79,'One answer infers the initial seven-day anointing requirement from the need for a verse to dispense with its full duration.',cond=['First alternative derivation'],scope='Inference from special reduction verse; not cumulative with alternative analogy.')
c['analogy']=claim('analogy',79,'Alternatively, the verse juxtaposes למשחה בהם with ולמלא בם את ידם, linking anointing to investiture: as investiture lasts seven days, so does anointing.',cond=['Second alternative derivation','Initial prescribed duration'],scope='Explicit alternative source for seven-day anointing.')
for n,(ii,src,tgt,rel) in enumerate([(66,'idproof','all','support'),(68,'semikha','difference','answer'),(70,'semikhastatus','semikhasource','answer'),(69,'blood','semikhaatonement','answer'),(70,'semikhastatus','semikhaverse','answer'),(71,'waving','difference','answer'),(72,'wavestatus','wavesource','answer'),(72,'waveblood','waveatonement','answer'),(72,'wavestatus','waveverse','answer'),(73,'separation','difference','answer'),(74,'prepare','separationsource','answer'),(75,'invest','difference','answer'),(77,'mixed','investsource','answer'),(77,'mixed','anointverse','answer'),(77,'mixed','mixed','answer'),(79,'deduction','initialseven','answer'),(79,'analogy','initialseven','answer')]):
 target=c[tgt] if (src,tgt)==('idproof','all') else q[tgt]
 edge('e'+str(n),ii,c[src],target,rel)
notes={65:'Distinguished previous Yohanan/Resh Lakish exchange from separately reported Yohanan/Hanina dispute. Initial unnamed views remain unassigned locally.',66:'Read explicit תסתיים; Yohanan assigned by prior non-response, Hanina only by elimination, not name order.',67:'Explicit difference question retained.',68:'Both conditional outcomes of semikha example retained.',69:'Source question and rhetorical atonement question separate; blood proof retained.',70:'Read full prior baraita; כאילו לא כפר וכפר retains both halves and does not authorize omission.',71:'Waving difference distinct from semikha; full Rav Nahman bar Yitzhak name.',72:'Three questions, repeated blood proof and double-sided atonement formulation retained.',73:'Seven-day separation difference retains both views.',74:'Substitute preparation not equated with separation; non-indispensability not no initial duty.',75:'Both investiture and anointing durations retained; no total omission inferred.',76:'Read complete baraita through5a10; succeeding-priest scope preserved.',77:'Both mixed-duration cases explicitly enumerated; no one-day/one-day invention.',78:'לכתחלה distinguished from invalidating effect.',79:'Two alternative derivations kept distinct; subsequent rationale discussion5a13–5b6 read as context, not counted complete.'}
C=[]
for i in range(65,80):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Actual second source omission reading: ' if l=='reconciliation' else 'Direct source '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=C,open_tails=state['open_tails']+[s])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=HERE/'yoma_4b12_5a12_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(path=str(out),records=len(R),sha256=hashlib.sha256(b).hexdigest())))
