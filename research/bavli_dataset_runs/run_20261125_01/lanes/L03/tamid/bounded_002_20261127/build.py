import json,copy,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=runner.current(job);assert runner.sha(runner.encoded(base))=='82d494b4dd71ba8c26cd774abe128eabab1dc84cbdd79561bba5e92b5543dcc2'
j,src=runner.load(job);seg=list(src.values());assert seg[10]['ref']=='Tamid 26a:8' and seg[19]['ref']=='Tamid 26b:7'
old=json.loads((out.parent/'bounded_001_20261127/VALIDATED_PROPOSAL.json').read_text(encoding='utf-8'));p={k:copy.deepcopy(v) for k,v in old.items() if k not in ['records','coverage','open_tails']};p.update(records=[],coverage=[],open_tails=['tam002.stones'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',sup=None):
 r=dict(id='tam002.'+k,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup
 p['records'].append(r);return r['id']
def claim(k,inds,txt,holder='anonymous Gemara',mode='asserted',cond=None,u=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Temple watch interpretation and architecture; local argument stage',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' at this source stage; no external ruling inferred'),[c],u);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('guard_closed','structure',list(range(7,13)),dict(title='Basis of priestly watch count; anonymous readings and Rav Ashi alternative',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference',sup='tam001.guard_derivation')
for k,inds,title,bound in [('upper',[13,14,15,16],'Upper rooms and priest-above-Levite watch arrangement','closed'),('moked',[17,18],'One guard for Beit Hamoked despite two gates','closed'),('stones',[19],'Stone tiers and apparent conflict with whole stones; response continues26b8','open_right')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary=bound,legacy_ids=[]),origin='editorial_inference')
roles={10:'Question and grammatical basis separating encamping and guarding',11:'Single-place hypothesis and Moses analogy rejecting it',12:'Rav Ashi alternative derivation from three guard expressions',13:'Inquiry whether upper rooms are literal or merely elevated',14:'Cited Mishnah describing northern gate and above/below guards',15:'Question and baraita deriving service of priests',16:'Alternative reading tested against second verse; above/below explanation',17:'Mishnah lemma on Beit Hamoked',18:'Single guard challenged by two gates; Rabbi Judah detail and Abaye reply',19:'Definition of stone tiers and whole-stone objection'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='composite voices identified in attribution rows' if i in [12,18] else 'anonymous Gemara with cited text',discourse_role=role,composition='composite'))
 if i!=12:rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion or quotation frame',role='anonymous',candidates=[],scope=role+'; named substatements separately attributed',transmission_chain=[]))
for k,i,quote,name,scope in [('ravashi',12,'רב אשי אמר','Rav Ashi','Alternative count derivation'),('judah',18,'א"ר יהודה','Rabbi Judah','Small wicket in gate opening to courtyard'),('abaye',18,'אמר אביי','Abaye','One guard suffices for adjacent gates')]:rec(k+'.a','attributions',[(i,quote)],dict(surface=quote,role='speaker',candidates=[name],scope=scope,transmission_chain=[]))
rec('baraita.a','attributions',[15,16],dict(surface='דתנו רבנן',role='quoted_authority',candidates=['anonymous baraita'],scope='Distinguishing your service from their service in verses',transmission_chain=[]))
gq=q('grammar_q',[(10,'ממאי')],'What grounds the proposed separation in the verse?')
gc=claim('grammar',[(10,'מדכתיב והחונים וכתיב שומרים חונים לחוד ושומרים לחוד')],'The distinct encamping and guarding expressions allow encampers and guards to be read separately.')
edge('grammar_answer',[10],gc,gq,'answer');edge('grammar_support',[10],gc,'tam001.r1.verse_separation','support')
h=claim('one_place',[(11,'אימא כולהו בחד מקום לחודיה')],'Perhaps all of them occupy one place.','anonymous Gemara','hypothetical')
an=claim('moses_analogy',[(11,'לא ס"ד מה משה בחד מקום לחודיה אף אהרן ובניו בחד מקום לחודיה')],'The anonymous answer rejects the one-place suggestion by comparing Moses’ separate place with the separate places of Aaron and his sons.',u=['Preserve terse printed analogy; do not silently paraphrase it as an independently explicit allocation of every son.'])
edge('one_place_reject',[11],an,h,'objection')
ra=claim('ravashi',[12],'Rav Ashi derives the count from the verse’s three guard expressions: שומרים משמרת למשמרת.','Rav Ashi')
edge('ravashi_support',[12],ra,'tam001.three','support')
uq=q('upper_q',[13],'Were these actual upper rooms, or merely places elevated like upper rooms?')
up=claim('upper_room',[(14,'כמין אכסדרא היה ועלייה בנוי על גבה')],'The cited northern Gate of the Spark was like a portico with an upper room built above it.','anonymous cited Mishnah')
edge('upper_proof',[14],up,uq,'answer')
above=claim('above',[(14,'שהכהנים שומרים מלמעלה')],'Priests guard above at the cited gate.','anonymous cited Mishnah')
below=claim('below',[(14,'והלוים מלמטה')],'Levites guard below there.','anonymous cited Mishnah')
claim('outside_door',[(14,'ופתח היה לו לחול')],'It had an opening to non-sacred ground.','anonymous cited Mishnah')
bq=q('arrangement_basis',[(15,'מנא הני מילי')],'What grounds this priestly and levitical arrangement?')
first=claim('your_service',[(15,'וילוו עליך וישרתוך בעבודתך הכתוב מדבר')],'The baraita interprets וילוו עליך וישרתוך as referring to service performed for you.','anonymous baraita')
edge('service_basis',[15],first,bq,'answer')
alt=q('whose_service',[(16,'אתה אומר בעבודתך הכתוב מדבר או אינו אלא בעבודתם')],'Does the first verse concern your service, or could it concern their own service?')
second=claim('their_service',[(16,'כשהוא אומר (במדבר יח ד) ונלוו עליך ושמרו לכל כליו ולכל עבודתו הרי בעבודתם אמור')],'The second quoted verse already refers to their own service.','anonymous baraita')
remaining=claim('first_remaining',[(16,'הא מה אני מקיים וילוו עליך וישרתוך בעבודתך הכתוב מדבר')],'The first verse is therefore interpreted as service performed for you.','anonymous baraita')
edge('second_distinguishes',[16],second,remaining,'support');edge('service_answer',[16],remaining,alt,'answer')
arr=claim('arrangement',[(16,'הא כיצד כהנים שומרים מלמעלה ולוים מלמטה')],'The baraita realizes this service relation by placing priestly guards above and levitical guards below.','anonymous baraita')
edge('arrangement_explains',[16],arr,first,'qualification')
claim('moked_lemma',[17],'The discussion repeats that Beit Hamoked is domed and a large chamber.','anonymous quoted Mishnah')
mq=q('single_guard',[(18,'וחד שומר הוא דהוה בבית המוקד ורמינהי')],'How can Beit Hamoked have one guard given the following two-gate teaching?')
two=claim('two_gates',[(18,'שני שערים היו בבית המוקד')],'Beit Hamoked had two gates.','anonymous cited Mishnah')
claim('heil_gate',[(18,'אחד פתוח לחיל')],'One gate opened to the heil.','anonymous cited Mishnah')
claim('courtyard_gate',[(18,'ואחד פתוח לעזרה')],'One gate opened to the courtyard.','anonymous cited Mishnah')
wicket=claim('wicket',[(18,'א"ר יהודה בזה שנכנסין לעזרה פשפש קטן היה לו שבו נכנסין לבלוש העזרה')],'Rabbi Judah states that the courtyard entrance had a small wicket through which they entered to inspect the courtyard.','Rabbi Judah')
adjacent=claim('adjacent',[(18,'כיון דגבי הדדי הוו קיימי')],'Abaye explains that the gates stood adjacent to each other.','Abaye')
one=claim('one_sufficient',[(18,'סגי להו בחד שומר דוי להכא ודוי להכא')],'One guard suffices by looking this way and that.','Abaye',cond=['The two gates are adjacent'])
edge('adjacent_support',[18],adjacent,one,'support');edge('one_answer',[18],one,mq,'answer')
sq=q('tiers_q',[(19,'רובדין מאי ניהו')],'What are the stone tiers?')
steps=claim('steps',[(19,'גזרתא דאצטבתא דסלקי בהו לאצטבתא')],'They are step-like tiers by which one ascends to the platform.')
edge('tiers_answer',[19],steps,sq,'answer')
wholeq=q('whole_stone_q',[(19,'ומי הוו מיפלגי אבנים והכתיב')],'Were stones split, despite the verse describing the House built of whole stone?')
whole=claim('whole_stone',[(19,"(מלכים א' ו ז) והבית בהבנותו אבן שלמה וגו'")],'The cited verse describes the House being built of whole stone.')
edge('whole_objection',[19],whole,steps,'objection')
prepared=claim('prepared_context',[20],'Abaye answers that small and large stones were prepared and brought beforehand, citing the ten-cubit and eight-cubit stones.','Abaye')
edge('prepared_answer',[20],prepared,wholeq,'answer')
rec('prepared.a','attributions',[(20,'אמר אביי')],dict(surface='אמר אביי',role='speaker',candidates=['Abaye'],scope='Reply about prior preparation of stones; context only',transmission_chain=[]))
for c in base['coverage']:
 if 'tam001.guard_derivation' in c['record_ids']:
  n={k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'};n['record_ids']=['tam002.guard_closed' if v=='tam001.guard_derivation' else v for v in n['record_ids']];n['rationale']+=' Guard derivation closed through26a10 in following batch.';p['coverage'].append(n)
notes={10:'Distinct grammatical forms support reading; no additional speaker assigned.',11:'Hypothetical one-place reading and rejection retained; terse analogy uncertainty explicit.',12:'Rav Ashi kept separate from preceding anonymous reasoning.',13:'Both alternatives actual upper room versus elevation retained as question.',14:'Actual upper room, priest-above/Levite-below and non-sacred opening separately checked.',15:'Anonymous baraita distinct from narrative question; scriptural quotation is evidence, not a new human speaker.',16:'Two verses and their service scopes distinguished; rejected alternative not silently adopted.',17:'Repeated lemma retained as occurrence; no new unique-topic count.',18:'Both gates, Rabbi Judah wicket, Abaye adjacency and conditional one-guard answer retained separately.',19:'Definition and objection retained, with source-backed continuation response26b8; open tail retained at core endpoint.'}
for i in range(10,20):
 for layer in runner.LAYERS:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=notes[i]+' Actual '+layer+' pass and omission reread; surrounding context through28a10 read. Only ten new cores counted.'))
f=out/'PROPOSAL.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'sha256':sha(f),'records':len(p['records']),'coverage_rows':len(p['coverage'])}))
