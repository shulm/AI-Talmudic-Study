import json, hashlib
from pathlib import Path
root=Path.cwd(); job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid'); out=Path(__file__).resolve().parent
read=lambda f:json.loads(f.read_text(encoding='utf-8-sig'))
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
assert read(job/'OWNER.json')=={'owner':'/root/lead_l01_l03','epoch':1}
assert not (job/'CURRENT.json').exists()
active=read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json'); cp=root/active['contract_path']; assert sha(cp)==active['contract_sha256']; contract=read(cp)
for f,h in contract['production_files'].items(): assert sha(root/f)==h,f
src=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Kodashim/Tamid/Hebrew/Wikisource Talmud Bavli.json'); ss=Path('F:/Sefaria-Export-master/schemas/Tamid.json')
assert sha(src)=='d37fab6314d84a21da855c5b5d8b91f8bfc594b336817e13393e383ffdcd453d'
assert sha(ss)=='22f679c21fa0c12eab0e3a686a4069b0a628415290b7204e57ac92d368de60f9'
assert sha(root/'research/bavli_sugya_corpus_v1/source_manifest.json')==contract['source_manifest_sha256']
w=read(job/'context_bounded001_full_20261127.json'); seg=w['segments']; assert seg[0]['source_index']==[49,0] and seg[9]['ref']=='Tamid 26a:7'
byref={s['ref']:i for i,s in enumerate(seg)}
p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='/root/lead_l01_l03',epoch=1,execution={'route':'interactive_agent','agent_id':'/root','model_id':None},records=[],coverage=[],open_tails=['tam001.guard_derivation'])
def ev(i,q=None):
 s=seg[i]; t=s['text']; a=0 if q is None else t.index(q); b=len(t) if q is None else a+len(q)
 return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase'):
 rid='tam001.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin));return rid
def claim(k,inds,prop,cond=None,holder='anonymous Mishnah',mode='asserted',u=None):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond or [],scope='Opening Temple watch, overnight arrangements and ash-removal procedure; local textual stage',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' at indicated source stage; continuation qualifications preserved separately'),[c],u);return c
def q(k,inds,txt): return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel,ex='source_explicit'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness=ex),[a,b])
rec('mishnah','structure',list(range(7)),dict(title='Temple priestly watches, sleep and impurity arrangements, ash-removal preparation and lottery',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('guard_derivation','structure',[7,8,9],dict(title='Scriptural basis for priestly and levitical watches; numerical interpretation continues through26a10',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')
for k,inds,title in [('watch',[0,1],'Watch locations and Beit Hamoked'),('night',[2,3,4],'Sleeping garments and route after seminal emission'),('lottery',[5,6],'Preparation and ash-removal lottery')]:rec(k,'structure',inds,dict(title=title,primary=False,boundary='closed',legacy_ids=[]),origin='editorial_inference')
roles=['Three priestly watch stations and youths in upper rooms','Architecture, elders and courtyard keys','Priestly sleep and clothing; emission case begins','Underground route, lights, immersion room and latrine privacy','Immersion, drying, warming, waiting and departure','Preparation before supervisor and variable arrival time','Supervisor summons immersed priests to lottery','Question of scriptural basis and Abaye citation','Anonymous objection: generic duty insufficient for distinct counts','Anonymous reading separating Moses, Aaron and sons']
for i,role in enumerate(roles):
 voice='anonymous Mishnah' if i<7 else ('anonymous question and Abaye answer' if i==7 else 'anonymous Gemara')
 rec('u'+str(i),'utterances',[i],dict(textual_voice=voice,discourse_role=role,composition='composite'))
 if i!=7:rec('a'+str(i),'attributions',[i],dict(surface='מתני׳' if i<7 else 'אמרי',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
rec('a.abaye','attributions',[(7,'אמר אביי')],dict(surface='אמר אביי',role='speaker',candidates=['Abaye'],scope='Scriptural answer at26a5 only; following anonymous objections/answers not automatically his',transmission_chain=[]))
rec('a.question','attributions',[(7,'מנא ה"מ')],dict(surface='מנא ה"מ',role='anonymous',candidates=[],scope='Question of basis for watches',transmission_chain=[]))
rec('a.supervisor','attributions',[(6,'אמר להן מי שטבל יבא ויפיס')],dict(surface='הממונה',role='speaker',candidates=['the supervisor (unnamed role)'],scope='Invitation to immersed priests to participate in lottery, quoted within Mishnah',transmission_chain=[]))
count=claim('three',[(0,'בשלשה</strong></big> מקומות הכהנים שומרים בבית המקדש')],'Priests keep watch at three locations in the Temple.')
for k,quote in [('avtinas','בית אבטינס'),('nitzotz','בית הניצוץ'),('moked','בית המוקד')]:
 c=claim(k,[(0,quote)],'One priestly watch location is '+quote+'.');edge(k+'.location',[0],c,count,'qualification')
claim('upper',[(0,'בבית אבטינס ובבית הניצוץ היו עליות')],'Beit Avtinas and Beit Hanitzotz had upper rooms; the later inquiry distinguishes actual rooms from mere elevation.',u=['Precise architectural interpretation examined in26b1–2, beyond core.'])
claim('young',[(0,'הרובים שומרים שם')],'The rovîm keep watch there.',u=['27a1 explains these as those not yet eligible for service, distinguished from pirhei kehunah; do not equate both groups.'])
claim('dome',[(1,'בית המוקד כיפה')],'Beit Hamoked is domed.')
claim('large',[(1,'ובית הגדול היה מוקף רובדין של אבן')],'The large chamber was surrounded by stone tiers.')
claim('elders',[(1,'זקני בית אב ישנים שם')],'The elders of the paternal priestly house sleep there.')
claim('keys',[(1,'ומפתחות העזרה בידם')],'The courtyard keys are held by those elders.')
claim('ground',[(2,'פרחי כהונה איש כסותו בארץ')],'Each of the young priests has his own covering on the ground.')
claim('not_sleep',[(2,'לא היו ישנים בבגדי קדש')],'They did not sleep wearing sacred garments.',u=['This negation alone does not settle permission for other benefit; discussion27a14–27b8 retained as context.'])
placement=claim('placement',[(2,'אלא היו פושטין ומניחין אותן תחת ראשיהם')],'The Mishnah literally describes removing the sacred garments and placing them under their heads.',u=['Initial wording, not a final resolved rule:27a16/27b3 propose opposite their heads;27b4 preserves alternatives involving garments without mixed fibres or stiff priestly garments.'])
claim('own_cover',[(2,'ומתכסין בכסות עצמן')],'They cover themselves with their own clothing.')
em=claim('emission',[(2,'אירע קרי לאחד מהן יוצא והולך לו')],'One who experiences a seminal emission leaves by the route continued on26a1.',cond=['Seminal emission in one of the priests'])
route=claim('route',[3],'The route runs beneath the bira, with lights on both sides, to the immersion chamber.',cond=['Priest leaving after seminal emission'])
edge('route_continues',[2,3],route,em,'continuation')
claim('fire',[(3,'ומדורה היתה שם')],'A fire was present there.')
claim('latrine',[(3,'ובית הכסא של כבוד')],'A latrine preserving privacy was present.')
claim('locked',[(3,'מצאו נעול יודע שיש שם אדם')],'A locked door indicates a person is inside.',cond=['Latrine found locked'])
claim('open',[(3,'פתוח בידוע שאין שם אדם')],'An open door indicates nobody is inside.',cond=['Latrine found open'])
for k,quote,prop in [('immerse','ירד וטבל','He descends and immerses.'),('dry','עלה ונסתפג','He ascends and dries himself.'),('warm','ונתחמם כנגד המדורה','He warms himself before the fire.'),('wait','בא וישב לו אצל אחיו הכהנים עד שהיו שערים נפתחים','He returns and sits beside his fellow priests until the gates open.'),('depart','יוצא והולך לו','He then departs.')]:claim(k,[(4,quote)],prop,cond=['Priest who experienced seminal emission; stage in stated sequence'])
prep=claim('prepare',[(5,'מי שהוא רוצה לתרום את המזבח משכים וטובל עד שלא יבא הממונה')],'One wishing to remove ashes from the altar rises early and immerses before the supervisor arrives.',cond=['Wishes to perform ash removal'],u=['28a5–10 discusses relation to lottery: Abaye distinguishes before/after enactment; Rava reads both clauses after enactment. No temporal harmonization chosen here.'])
tq=q('time_q',[(5,'וכי באיזה שעה בא הממונה')],'At what time does the supervisor arrive?')
tc=claim('time',[(5,'לא כל העתים שוות פעמים שהוא בא מקרות הגבר או סמוך לו מלפניו או מאחריו')],'His arrival time varies: at keriat hagever or shortly before or after it.',u=['קרות הגבר left as printed temporal marker; no unprovided identification of crier versus cock chosen.'])
edge('time_answer',[5],tc,tq,'answer')
claim('knock',[(6,'הממונה בא ודפק עליהן והן פתחו לו')],'The supervisor comes and knocks, and they open for him.')
lot=claim('invite',[(6,'מי שטבל יבא ויפיס')],'Those who immersed are invited to come and participate in the lottery.',cond=['Has immersed'],holder='the supervisor (unnamed role)')
claim('winner',[(6,'הפיסו מי שזכה זכה בו')],'They conduct the lottery, and its winner obtains the task.')
gq=q('basis',[7],'What is the scriptural basis for these watches?')
gc=claim('abaye_basis',[7],'Abaye cites Numbers3:38, describing Moses, Aaron and his sons guarding the sanctuary, as the basis.',holder='Abaye')
edge('abaye_answer',[7],gc,gq,'answer')
ob=claim('insufficient',[8],'The citation establishes that priests and Levites guard, but does not yet distinguish the Mishnah’s three priestly locations from twenty-one levitical locations, since both groups occur together in the verse.',holder='anonymous Gemara',mode='challenged')
edge('objection',[8],ob,gc,'objection')
lc=claim('levites21',[(8,"והלוים בעשרים וא' מקום")],'The cited Mishnah assigns Levites twenty-one locations.',holder='anonymous Gemara quoting Mishnah')
ans=claim('separate',[9],'The anonymous response separates Moses from Aaron and his sons: Aaron at one location and his sons at two.',holder='anonymous Gemara',u=['Argument remains open at core endpoint;26a8–10 supplies further grounds, objection and Rav Ashi alternative.'])
edge('response',[9],ans,ob,'answer');edge('three_basis',[9],ans,count,'support')
# Continuation qualification records carry exact non-core evidence; no extra coverage claimed.
ci=byref['Tamid 27a:16']; opposite=claim('opposite_context',[ci],'The anonymous response proposes reading the garment placement as opposite their heads.',holder='anonymous Gemara',mode='asserted',u=['Not exclusive:27b4 retains further alternatives.'])
edge('placement_correction',[ci],opposite,placement,'correction')
ci=byref['Tamid 27b:4']; alternatives=claim('garment_alternatives',[ci],'An alternative invokes garments without mixed fibres; Rav Ashi alternatively invokes the stiffness of priestly garments, citing Rav Huna son of Rav Yehoshua on the felt of Narsh.',holder='anonymous alternative and Rav Ashi',u=['Composite record preserves distinct voices; not a single jointly held ruling.'])
edge('placement_alternatives',[ci],alternatives,placement,'qualification')
rec('garment_transmission','attributions',[ci],dict(surface='רב אשי אמר ... דאמר רב הונא בריה דרב יהושע',role='quoted_authority',candidates=['Rav Huna son of Rav Yehoshua'],scope='Rav Ashi cites felt precedent for stiffness answer; not Rav Huna himself',transmission_chain=['Rav Ashi','Rav Huna son of Rav Yehoshua']))
ca=byref['Tamid 28a:6']; cr=byref['Tamid 28a:10']
a=claim('lottery_abaye',[ca],'Abaye resolves the preparation/lottery tension by distinguishing before and after the enactment.',holder='Abaye')
r=claim('lottery_rava',[cr],'Rava reads both clauses after the enactment: one wishing to enter the lottery rises early and immerses.',holder='Rava')
edge('abaye_prep',[ca],a,prep,'qualification');edge('rava_prep',[cr],r,prep,'qualification')
for k,i,name in [('abaye_lottery',ca,'Abaye'),('rava_lottery',cr,'Rava')]:rec(k+'.a','attributions',[i],dict(surface=seg[i]['text'].split(' ')[0]+' '+seg[i]['text'].split(' ')[1],role='speaker',candidates=[name],scope='Alternative explanation of ash-removal preparation and lottery',transmission_chain=[]))
notes=['Three sites, upper rooms and rovîm retained; no equation with service-age young priests.','Dome, stone tiers, elders and keys separately checked.','All clothing clauses and emission transition retained; later placement alternatives explicitly qualified.','Cross-folio route preserved, lights/fire/privacy and opposite locked/open conditions checked.','Five ordered stages reread, with impurity case carried from preceding page.','Preparation, explicit time question, variability and before/after alternatives preserved; later lottery explanations represented.','Knock/open, conditional invitation and lottery result retained; supervisor speech separated from narrator.','Abaye citation distinct from anonymous question and subsequent voices.','Generic duty and count mismatch retained, including levitical21.','Anonymous response not attributed to Abaye by proximity; further numerical derivation remains open.']
for i in range(10):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=notes[i]+' Source and continuation reread through28a10; only10 core segments counted. '+('Omission reconciliation completed.' if layer=='reconciliation' else ('Completed evidence-based '+layer+' pass.' if ids else 'No separate '+layer+' item after actual pass.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
pins=dict(run_id=active['run_id'],contract_sha256=sha(cp),production_git_commit=contract['production_git_commit'],source_sha256=sha(src),source_schema_sha256=sha(ss),schema_sha256=contract['schema_sha256'],protocol_sha256=contract['annotation_protocol_sha256'],source_manifest_sha256=contract['source_manifest_sha256'],owner=read(job/'OWNER.json'),executor='/root',source_start_index=[49,0],independence='Producer has not viewed central Tamid reader labels. Existing source-first reader frozen separately; comparator is /root/rosh_hashanah.',context_last='Tamid 28a:10',core_segments=10)
for name,value in [('PINS.json',pins),('INITIAL_PROPOSAL.json',p)]:
 f=out/name;assert not f.exists();f.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(proposal_sha256=sha(out/'INITIAL_PROPOSAL.json'),records=len(p['records']),core_segments=10)))
