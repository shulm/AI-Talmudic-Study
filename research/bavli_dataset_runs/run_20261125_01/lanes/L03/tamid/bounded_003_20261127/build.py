import json,copy,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=runner.current(job);assert runner.sha(runner.encoded(base))=='5e6f2550823618653e9e09320c2880e8146407c46a509b4cada13217bd768b33'
j,src=runner.load(job);seg=list(src.values());assert seg[20]['ref']=='Tamid 26b:8' and seg[29]['ref']=='Tamid 27a:7'
old=json.loads((out.parent/'bounded_002_20261127/PROPOSAL.json').read_text(encoding='utf-8'));p={k:copy.deepcopy(v) for k,v in old.items() if k not in ['records','coverage','open_tails']};p.update(records=[],coverage=[],open_tails=['tam003.levites'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',sup=None):
 r=dict(id='tam003.'+k,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if sup:r['supersedes']=sup
 p['records'].append(r);return r['id']
def claim(k,inds,txt,holder='anonymous Gemara',mode='asserted',cond=None,u=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Temple watch arrangements and levitical station count; local source stage',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' in indicated source; alternative explanation retained'),[c],u);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('stones_closed','structure',[19,20],dict(title='Stone tiers: preparation before bringing stones resolves apparent hewing objection',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference',sup='tam002.stones')
for k,inds,title,bound in [('beds',[21],'Why beds are not brought for elders','closed'),('young',[22,23],'Rovim versus pirhei kehunah across folio boundary','closed'),('levites',list(range(24,30)),'Levitical stations: twenty-one versus twenty-four and twenty-two; alternative continues27a8–9','open_right')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary=bound,legacy_ids=[]),origin='editorial_inference')
roles={20:'Abaye answer about stones prepared beforehand; existing context claim reused',21:'Beds question and Abaye decorum answer',22:'Question comparing names rovîm and pirhei begins',23:'Naming question completes and eligibility distinction answers',24:'Repeated Mishnah occurrence of three priestly sites',25:'Twenty-one levitical posts enumerated',26:'Source question and alternative transmission of scriptural citation',27:'Twenty-four objection and Abaye interpretation of asuppim count',28:'Twenty-two objection and distinction of guard from companion outside',29:'Meaning of parbar and Rabbah bar Rav Shila explanation'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous discussion with separately identified named answer or quotation',discourse_role=role,composition='composite'))
 if i not in [20,24,25]:rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion frame',role='anonymous',candidates=[],scope=role+'; named statements separated',transmission_chain=[]))
for k,i,quote,name,scope in [('abaye_beds',21,'אמר אביי','Abaye','Decorum answer against bringing beds'),('abaye_count',27,'אמר אביי','Abaye','Asuppim interpreted as two'),('rabbah_shila',29,'אמר רבה בר רב שילא','Rabbah bar Rav Shila','Explanation of parbar, not Rabbah without patronymic')]:rec(k+'.a','attributions',[(i,quote)],dict(surface=quote,role='speaker',candidates=[name],scope=scope,transmission_chain=[]))
rec('quoted_mishnah.a','attributions',[24,25],dict(surface='תנן התם',role='quoted_authority',candidates=['anonymous cited Mishnah'],scope='Priestly and levitical watch locations',transmission_chain=[]))
rec('rav_yehuda.a','attributions',[(26,'אמר רב יהודה מסורא ואמרי לה במתניתא תנא')],dict(surface='אמר רב יהודה מסורא ואמרי לה במתניתא תנא',role='speaker',candidates=['Rav Yehuda of Sura','anonymous baraita (alternative transmission)'],scope='Two reported attributions for the same scriptural derivation; not Rav himself',transmission_chain=[]),u=['Alternative transmission preserved without choosing a source.'])
# Existing Abaye stone claim/position/attribution and answer edge already cover26b8.
bq=q('beds_q',[(21,'ואמאי לעיילי מטות')],'Why not bring beds for the elders?')
bc=claim('beds_answer',[(21,'אמר אביי לאו אורח ארעא לעיולי מטות לבית המקדש')],'Abaye says it is not proper decorum to bring beds into the Temple.','Abaye')
edge('beds_answer_edge',[21],bc,bq,'answer')
yq=q('young_q',[22,(23,'פרחי כהונה')],'Why call them rovîm in one place and pirhei kehunah in the other?')
young=claim('not_service',[(23,'התם דלא מטו למעבד עבודה קרי להו רובים')],'Those not yet eligible to perform service are called rovîm.')
older=claim('service',[(23,'הכא דמטו להו למעבד עבודה קרי להו פרחי')],'Those eligible to perform service are called pirhei kehunah.')
edge('young_answer',[23],young,yq,'answer');edge('older_answer',[23],older,yq,'answer');edge('age_distinction',[23],young,older,'distinction')
three=claim('three_repeat',[24],'The cited Mishnah again states that priests guard in three places: Beit Avtinas, Beit Hanitzotz and Beit Hamoked.','anonymous cited Mishnah',u=['Repeated source occurrence, not a new unique topic; named sites already individually represented in opening.'])
total=claim('twentyone',[(25,'והלוים בכ"א מקומות')],'Levites guard at twenty-one locations.','anonymous cited Mishnah')
items=[('mount_gates','ה\' על ה\' שערי הר הבית','Five guards are stationed at the five Temple Mount gates.'),('mount_corners',"ד' על ד' פנותיו מבפנים",'Four are at its four corners on the inside.'),('court_gates',"ה' על ה' שערי עזרה",'Five are at the five courtyard gates.'),('court_corners',"וד' על ד' פנותיו מבחוץ",'Four are at its four corners on the outside.'),('offering_chamber','אחד בלשכת הקרבן','One is at the offering chamber.'),('curtain_chamber','ואחד בלשכת הפרוכת','One is at the curtain chamber.'),('behind','ואחד אחורי בית הכפורת','One is behind the chamber of the ark cover.')]
for k,quote,txt in items:
 c=claim(k,[(25,quote)],txt,'anonymous cited Mishnah');edge(k+'.enumeration',[25],c,total,'qualification')
sq=q('source_q',[(26,'מנה"מ')],'What is the source for this count?')
script=claim('chronicles',[26],'The derivation cites the Chronicles enumeration of levitical stations: east six, north four, south four, asuppim two-two, west four at the road and two at parbar.','Rav Yehuda of Sura or anonymous baraita',u=['Source names are alternative reports, not joint holders; raw citation preserved.'])
edge('chronicles_answer',[26],script,sq,'answer')
ob=claim('twentyfour',[(27,'אמרי הני כ"ד הוו')],'The anonymous objection counts twenty-four in that citation.','anonymous Gemara','challenged')
edge('count_objection',[27],ob,script,'objection')
asup=claim('asuppim',[(27,'אמר אביי ה"ק לאסופים שנים (ב\')')],'Abaye reads asuppim as two, rather than treating the doubled wording as four.','Abaye',u=['Interpretation reduces count within this answer; later anonymous alternative retains literal24.'])
edge('asuppim_answer',[27],asup,ob,'answer')
still=claim('twentytwo',[(28,'אכתי עשרין ותרי הוו')],'The anonymous objection notes that twenty-two still remain.','anonymous Gemara','challenged')
edge('still_objection',[28],still,asup,'objection')
one=claim('parbar_guard',[(28,'היאך דפרבר חד הוה')],'There was one actual guard at parbar in this explanation.')
companion=claim('companion',[(28,'ואחרינא בצוותא הוא דאזיל ויתיב גביה משום דקאי אבראי')],'The other person went and sat beside him for company because the station was outside.')
edge('one_answer',[28],one,still,'answer');edge('companion_qualifies',[28],companion,one,'qualification')
pq=q('parbar_q',[(29,'מאי לפרבר')],'What does parbar mean?')
pc=claim('parbar_meaning',[(29,'אמר רבה בר רב שילא כמ"ד כלפי בר')],'Rabbah bar Rav Shila explains parbar as facing outside.','Rabbah bar Rav Shila')
edge('parbar_answer',[29],pc,pq,'answer')
# Whole relevant continuation: retain alternative rather than presenting21-reduction as exclusive.
alt=claim('literal24_context',[30],'Alternatively, retain the scriptural count of twenty-four: three are priestly stations and twenty-one levitical stations.')
edge('literal24_answer',[30],alt,ob,'answer')
alllev=q('all_levites_context',[(31,'והא הכא לוים הוא דכתיב')],'But the scriptural text here says Levites; how can it include priestly stations?')
called=claim('priests_levites_context',[31],'Rabbi Yehoshua ben Levi states that priests are called Levites in twenty-four places, with the cited Ezekiel phrase as one example.','Rabbi Yehoshua ben Levi')
edge('called_answer',[31],called,alllev,'answer');edge('called_support',[31],called,alt,'support')
rec('rybl.a','attributions',[(31,'כר\' יהושע בן לוי דאמר ריב"ל')],dict(surface='כר\' יהושע בן לוי דאמר ריב"ל',role='quoted_authority',candidates=['Rabbi Yehoshua ben Levi'],scope='Priests called Levites precedent in alternative answer',transmission_chain=[]))
for c in base['coverage']:
 if 'tam002.stones' in c['record_ids']:
  n={k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'};n['record_ids']=['tam003.stones_closed' if v=='tam002.stones' else v for v in n['record_ids']];n['rationale']+=' Stone discussion closed with already represented Abaye response26b8.';p['coverage'].append(n)
active=[r for r in base['records'] if r['release_state']=='valid' and r['id']!='tam002.stones']+p['records']
notes={20:'Existing context Abaye claim/position/attribution and answer reused without duplicate; structure closed.',21:'Bed proposal is an actual question, decorum answer belongs to Abaye.',22:'Question spans page boundary; preserve exact truncated first segment and next-page completion.',23:'Two service-eligibility groups distinguished without inventing numeric ages.',24:'Repeated Mishnah occurrence retained; occurrence versus topic count explicit.',25:'All seven location/count clauses and inner/outer contrast retained; later gate-number debates not counted here.',26:'Named Rav Yehuda of Sura versus baraita variants preserved; not Rav himself.',27:'Initial24 objection and Abaye2 reading retained with later alternative context.',28:'Remaining22 objection, one guard and companion outside kept distinct.',29:'Full patronymic preserved; lexical answer followed by alternative count interpretation in context.'}
for i in range(20,30):
 for layer in runner.LAYERS:
  ids=[r['id'] for r in active if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=notes[i]+' Actual '+layer+' pass and omission reread; continuation read through28a10. Only ten new cores counted.'))
f=out/'PROPOSAL.json';assert not f.exists();f.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'proposal_sha256':sha(f),'new_records':len(p['records']),'coverage_rows':len(p['coverage'])}))
