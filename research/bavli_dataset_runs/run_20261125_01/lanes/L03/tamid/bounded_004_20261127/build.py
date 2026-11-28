import copy,json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=runner.current(job);assert runner.sha(runner.encoded(base))=='eca024a2346d9a35620f5e97b60a7be3ae891cd88e9897598b3586e9da0b214f'
runner.authorize(job,'/root/lead_l01_l03',1);j,src=runner.load(job);seg=list(src.values());old={r['id']:r for r in base['records'] if r['release_state']=='valid'}
active=runner.read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json');cp=root/active['contract_path'];assert sha(cp)==active['contract_sha256'];contract=runner.read(cp)
for f,h in contract['production_files'].items():assert sha(root/f)==h
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='/root/lead_l01_l03',epoch=1,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[],coverage=[],open_tails=['tam004.emission_structure'])
replacements={}
def ev(i,q=None):
 s=seg[i];a=0 if q is None else s['text'].index(q);b=len(s['text']) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=s['text'][a:b])
def rec(k,l,inds,c,links=None,u=None,origin='source_paraphrase',supersedes=None):
 rid='tam004.'+k;r=dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links or [],uncertainty=u or [],origin=origin)
 if supersedes:r['supersedes']=supersedes;replacements[supersedes]=rid
 p['records'].append(r);return rid
def cl(k,inds,txt,holder='anonymous Gemara',cond=None,mode='asserted',u=None,supersedes=None):
 c=rec(k,'claims',inds,dict(proposition=txt,conditions=cond or [],scope='Temple guards and garment-use discussion; each local argument stage separately represented',assertion_mode=mode),u=u,supersedes=supersedes)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=cond or [],local_status=mode+' in indicated local stage; subsequent resolutions separately linked'),[c],u,supersedes=supersedes+'.p' if supersedes and supersedes+'.p' in old else None);return c
def q(k,inds,txt):return rec(k,'questions',inds,dict(formulation=txt,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,inds,a,b,rel='support'):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
# Finish the existing primary partition; original earlier evidence is retained.
oldstructure=old['tam003.levites'];r=copy.deepcopy(oldstructure)
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r.update(id='tam004.levites_closed',supersedes='tam003.levites');r['evidence'] += [ev(30),ev(31)];r['content']['boundary']='closed';r['content']['title']='Levitical station count, resolved by two alternative accounts through27a9';p['records'].append(r);replacements['tam003.levites']=r['id']
for k,inds,title,bound in [('guard_structure',[32,33,34,35],'Guard position and competing courtyard gate counts','closed'),('garment_structure',list(range(36,49)),'Garment benefit, mixed fibres and abbreviated external-use exception','closed'),('emission_structure',[49],'Seminal emission Mishnah citation; tunnel-sanctity continuation','open_right')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary=bound,legacy_ids=[]),origin='editorial_inference')
roles={30:'Alternative literal twenty-four station accounting',31:'Levites wording challenge answered by priests-called-Levites citation',32:'Watch placement quotation and inside/outside question',33:'Fatigue/seating distinction and Davidic kings exception',34:'Five versus seven courtyard gates contradiction',35:'Abaye reconciliation and Rava tannaitic disagreement proof',36:'Proposed walking/benefit inference from sleeping restriction',37:'Inference rejected through literary parallelism explanation',38:'Under-head benefit inference and opposite-head response',39:'Rav Pappa adjacent tefillin inference and risk rejection',40:'Mixed-fibres objection supports opposite-head reading',41:'Unnamed belt-composition alternatives',42:'Lying-under hypothesis rejected by rabbinic fibre-wrap prohibition',43:'Interposition hypothesis rejected by transmitted ten-covering rule',44:'Anonymous nonmixed answer and Rav Ashi stiffness answer with quoted precedent',45:'Baraita resolves garment benefit within Temple, outside restriction retained',46:'Outside restriction challenged by abbreviated Mount Gerizim narrative reference',47:'One answer uses garments suitable for priestly service',48:'Alternative exceptional-action scriptural answer',49:'Repeated Mishnah citation of seminal emission'}
for i,role in roles.items():
 rec('u'+str(i),'utterances',[i],dict(textual_voice='Gemara framing and citations, named voices separately attributed',discourse_role=role,composition='composite'))
 rec('anonymous'+str(i),'attributions',[i],dict(surface='anonymous framing',role='anonymous',candidates=[],scope='Anonymous frame only: '+role,transmission_chain=[]))
# Split two previously bundled contextual claims as they become covered cores.
total=cl('count24',[30],'The alternative retains the written total of twenty-four stations.',supersedes='tam003.literal24_context',u=['Alternative to the preceding Abaye/reduced-count account.'])
priests=cl('priests3',[30],'Three of the twenty-four stations are priestly.',cond=['Alternative literal twenty-four account'])
levites=cl('levites21',[30],'Twenty-one of the twenty-four stations are levitical.',cond=['Alternative literal twenty-four account'])
called=cl('called24',[31],'Rabbi Yehoshua ben Levi states that priests are called Levites in twenty-four places.','Rabbi Yehoshua ben Levi',supersedes='tam003.priests_levites_context')
example=cl('ezekiel_example',[(31,'והכהנים הלוים בני צדוק')],'The Ezekiel phrase calling the priests Levites is one cited example.','Rabbi Yehoshua ben Levi quoting Ezekiel')
edge('example_support',[31],example,called)
for k,c in [('priests',priests),('levites',levites)]:edge(k+'_count',[30],c,total)
for k,txt in [('mount_gates','Five guards are at the five Temple Mount gates.'),('mount_corners','Four guards are at the four Temple Mount corners on the inside.'),('court_gates','Five guards are at the five courtyard gates.'),('court_corners','Four guards are at the four courtyard corners on the outside.')]:cl(k,[32],txt,'cited Mishnah')
inside=q('inside_q',[32],'Why are Temple Mount guards inside and courtyard guards outside?')
mountsit=cl('mount_sit',[33],'A tired guard at the Temple Mount can sit.',cond=['Guard becomes tired'])
courtno=cl('court_no_sit',[33],'A tired guard cannot sit in the courtyard.',cond=['Ordinary guard; Davidic kings exception separate'])
kings=cl('kings_exception',[(33,'אין ישיבה בעזרה אלא למלכי בית דוד בלבד')],'Sitting in the courtyard is restricted to kings of the House of David.','cited anonymous teaching')
mountin=cl('mount_inside',[33],'Temple Mount guarding is placed inside because a tired guard can sit there.')
courtout=cl('court_outside',[33],'Courtyard guarding is placed outside because a tired ordinary guard cannot sit inside.')
edge('sit_ground',[33],mountsit,mountin);edge('no_sit_ground',[33],courtno,courtout);edge('kings_ground',[33],kings,courtno)
edge('inside_answer',[33],mountin,inside,'answer');edge('outside_answer',[33],courtout,inside,'answer')
gatesq=q('gates_q',[34],'How can the cited five courtyard gates be reconciled with the seven-gate source?')
seven=cl('seven_gates',[34],'The opposing source counts seven courtyard gates.','cited Mishnah')
for k,txt in [('north3','Three courtyard gates are in the north.'),('south3','Three courtyard gates are in the south.'),('east1','One courtyard gate is in the east.')]:cl(k,[34],txt,'cited Mishnah')
abaye=cl('abaye_guards',[(35,'אמר אביי תרי מינייהו לא צריכי שימור')],'Abaye says two of the gates require no guarding.','Abaye')
rava=cl('rava_tannaim',[(35,'רבא אמר תנאי היא')],'Rava explains the gate counts as a tannaitic disagreement.','Rava')
edge('abaye_answer',[35],abaye,gatesq,'answer');edge('rava_answer',[35],rava,gatesq,'answer')
cl('treasurers',[(35,'אין פוחתין מי"ג גזברין')],'The cited baraita requires at least thirteen treasurers.','anonymous baraita')
cl('overseers',[(35,"ומז' אמרכלין")],'The cited baraita requires at least seven amarkalin.','anonymous baraita')
rn=cl('natan13',[(35,'ר\' נתן אומר אין פוחתין מי"ג גזברין כנגד י"ג שערים')],'Rabbi Natan requires at least thirteen treasurers corresponding to thirteen gates.','Rabbi Natan')
eight=cl('eight_inference',[(35,'דל חמשה דהר הבית פשו להו תמניא דעזרה')],'Subtracting five Temple Mount gates leaves eight courtyard gates in this account.')
edge('natan_eight',[35],rn,eight)
for n in ['eight','seven','five']:
 c=cl('tanna_'+n,[35],'A tanna holds that there are '+n+' courtyard gates.',u=['No additional unnamed-tanna identity supplied.']);edge('tanna_'+n+'_supports',[35],c,rava)
# Keep the garment benefit proof stages separate, including rejected inferences.
walk=cl('walking_hyp',[36],'The initial inference permits walking in the priestly garments although sleeping is excluded.',mode='hypothetical')
benefit1=cl('benefit_hyp',[36],'The initial inference would establish that priestly garments were given for benefit.',mode='hypothetical')
edge('walking_inference',[36],walk,benefit1)
nowalk=cl('no_walking',[37],'The response says walking is also excluded at this explanatory stage.',mode='asserted',u=['This response blocks the initial inference; later27b5 independently permits Temple use.'])
literary=cl('literary',[37],'The opening uses the sleeping wording to match the following stripping, folding and placement clause.')
edge('walk_rejected',[37],nowalk,walk,'correction');edge('literary_support',[37],literary,nowalk)
placementbenefit=cl('placement_benefit',[38],'Literal under-head placement would imply permission to benefit from priestly garments.',mode='hypothetical')
edge('placement_blocks',[38],'tam001.opposite_context',placementbenefit,'objection')
tefillin=cl('tefillin_side',[(39,'שמע מינה תפילין מן הצד שריין')],'Rav Pappa infers that tefillin may be placed at the side.','Rav Pappa',cond=['Placement beside one’s sleeping position'])
roll=cl('no_roll_concern',[(39,'ולא חיישינן דלמא מיגנדר ונפיל עלייהו')],'Rav Pappa does not impose concern that one might roll onto them.','Rav Pappa',cond=['Tefillin at the side'])
edge('side_inference',[38,39],'tam001.opposite_context',tefillin);edge('roll_ground',[39],roll,tefillin)
mix=cl('mixed_objection',[40],'Even assuming benefit is permitted, mixed-fibre prohibition obstructs literal under-head placement.',mode='challenged',cond=['Garments containing prohibited mixed fibres'])
edge('mixed_opposite',[40],mix,'tam001.opposite_context')
beltq=q('belt_q',[41],'What can be said according to the view that the ordinary priest’s belt is the same as the high priest’s?')
cl('belt_different',[41],'One cited view distinguishes the high priest’s belt from the ordinary priest’s belt.',None,u=['Unnamed view remains unnamed.'])
cl('belt_same',[41],'The other cited view equates the ordinary priest’s belt with the high priest’s belt.',None,u=['Unnamed view remains unnamed.'])
lie=cl('lying_hyp',[42],'Perhaps the mixed-fibre ban applies to wearing or placing on oneself, while lying beneath oneself is permitted.',mode='hypothetical')
torah=cl('torah_under',[42],'The baraita reads the verse as allowing one to spread the material beneath oneself.','cited baraita',cond=['Verse-level rule, rabbinic restriction follows'])
rabbinic=cl('rabbinic_under',[42],'The sages nevertheless prohibit this spreading beneath oneself.','sages in cited baraita',cond=['Concern that one thread may wrap onto the flesh'])
thread=cl('thread_reason',[42],'A thread may wrap onto one’s flesh.','sages in cited baraita',mode='hypothetical')
edge('thread_ground',[42],thread,rabbinic);edge('rabbinic_qualifies',[42],rabbinic,torah,'qualification');edge('lying_rejected',[42],rabbinic,lie,'objection')
barrier=cl('barrier_hyp',[43],'Perhaps an intervening material separates the sleeper from the mixed fibres.',mode='hypothetical')
ten=cl('ten_coverings',[43],'Sleeping is prohibited even when ten coverings lie above the mixed fibres.','sacred congregation in Jerusalem (reported)',cond=['Ten coverings above mixed fibres'])
edge('barrier_rejected',[43],ten,barrier,'objection');edge('ten_opposite',[43],ten,'tam001.opposite_context')
rec('transmission','attributions',[(43,'ר"ש א"ר יהושע בן לוי א"ר יוסי בן שאול משום קהלא קדישא שבירושלים')],dict(surface='ר"ש א"ר יהושע בן לוי א"ר יוסי בן שאול משום קהלא קדישא שבירושלים',role='transmitter',candidates=['ר"ש (unexpanded in this witness)'],scope='Ten-covering prohibition; preserve actual local witness, not a silently substituted parallel',transmission_chain=['ר"ש (unexpanded)','Rabbi Yehoshua ben Levi','Rabbi Yose ben Shaul','sacred congregation in Jerusalem']),u=['Initial abbreviation ר"ש not disambiguated from this source alone.'])
# Existing27b4 alternative claims, positions, attributions and edges reused verbatim.
outside=cl('outside_forbidden',[45],'Going out in priestly garments to the province is prohibited.','cited baraita',cond=['Outside the Temple'])
service=cl('temple_service',[45],'Use of priestly garments within the Temple during service is permitted.','cited baraita',cond=['Within Temple','During service'])
noservice=cl('temple_no_service',[45],'Use of priestly garments within the Temple outside service time is permitted.','cited baraita',cond=['Within Temple','Outside service time'])
benefit=cl('benefit_resolved',[45],'The baraita establishes that priestly garments were given for benefit in this Temple-use context.','cited baraita',cond=['Temple-use context; provincial restriction separately retained'])
edge('benefit_service',[45],benefit,service);edge('benefit_nonservice',[45],benefit,noservice)
edge('benefit_resolution',[36,45],benefit,benefit1,'local_resolution');edge('walking_scope',[37,45],noservice,nowalk,'qualification')
externalq=q('outside_q',[46],'How does the provincial prohibition accord with the cited Mount Gerizim episode?')
gerizim=cl('gerizim_no_eulogy',[(46,'בכ"א בו יום הר גריזים דלא למיספד')],'The cited passage identifies the twenty-first as Mount Gerizim day, on which eulogizing is forbidden.','cited baraita',u=['Month and narrative omitted in local abbreviated text; do not infer them from this segment alone.'])
rec('yoma_reference','attributions',[46,47],dict(surface='כדאיתא ביומא פרק בא לו כ"ג ... עד',role='quoted_authority',candidates=['Yoma, chapter Ba Lo Kohen Gadol (explicit cross-reference)'],scope='Local text abbreviates the narrative; no imported parallel text treated as local quotation',transmission_chain=[]),u=['Narrative actors and events are not spelled out in this local witness; source-first parallel review is a separate evidence item.'])
suitable=cl('suitable',[47],'One answer treats the garments as suitable for priestly garments.',cond=['Abbreviated Mount Gerizim objection'],u=['Local source omits the intervening narrative. Do not infer actual sanctified status from suitability.'])
emergency=cl('exception',[48],'Another answer invokes the verse עת לעשות לה\' הפרו תורתך for the exceptional action.',cond=['Abbreviated Mount Gerizim objection'],u=['Exceptional response, not unrestricted provincial permission.'])
edge('suitable_answer',[47],suitable,externalq,'answer');edge('exception_answer',[48],emergency,externalq,'answer');edge('outside_exception',[46,48],emergency,outside,'qualification')
rec('emission_citation','attributions',[49],dict(surface='אירע קרי באחד מהן [וכו\']',role='quoted_authority',candidates=['opening Mishnah'],scope='Repeated incipit, continuation follows27b10',transmission_chain=[]))
emission=cl('emission_repeat',[49],'The discussion returns to the Mishnah’s case of a priest experiencing seminal emission.','cited Mishnah')
tunnels=cl('tunnels_context',[50],'Rabbi Yohanan states that the tunnels were not sanctified.','Rabbi Yohanan')
expel=cl('two_camps_context',[50],'A person with seminal emission is sent outside two camps.','anonymous Gemara',cond=['Person with seminal emission'])
edge('route_support',[49,50],'tam001.route',tunnels)
for k,i,surface,name in [('abaye',35,'אמר אביי','Abaye'),('rava',35,'רבא אמר','Rava'),('natan',35,"ר' נתן אומר",'Rabbi Natan'),('pappa',39,'אמר רב פפא','Rav Pappa'),('yohanan_context',50,"לר' יוחנן דאמר",'Rabbi Yohanan')]:rec(k+'.a','attributions',[(i,surface)],dict(surface=surface,role='speaker',candidates=[name],scope='Only the named local speech; adjacent anonymous clauses kept separate',transmission_chain=[]))
# Keep superseded contextual dependencies live through new immutable versions.
def remap(v):
 if isinstance(v,str):return replacements.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
while True:
 changed=False
 for rid,r in old.items():
  if rid in replacements:continue
  if remap(r['links'])!=r['links'] or remap(r['content'])!=r['content']:
   n={k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']};n.update(id='tam004.dep.'+rid,supersedes=rid);n['links']=remap(n['links']);n['content']=remap(n['content']);replacements[rid]=n['id'];p['records'].append(n);changed=True
 if not changed:break
for r in p['records']:r['links']=remap(r['links']);r['content']=remap(r['content'])
live={rid:r for rid,r in old.items() if rid not in replacements};live.update({r['id']:r for r in p['records']})
for c in base['coverage']:
 if any(rid in replacements for rid in c['record_ids']):
  n={k:copy.deepcopy(v) for k,v in c.items() if k!='proposal_execution'};n['record_ids']=remap(n['record_ids']);p['coverage'].append(n)
for i in range(30,50):
 for layer in runner.LAYERS:
  ids=[rid for rid,r in live.items() if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=roles[i]+'. Actual '+layer+' pass and omission reread; all initial/rejected/alternative explanations retained; earlier contextual rows reused. Continuation27b10 read, context uncounted. Abbreviated narrative not expanded into source evidence.'))
runner.validate_apply(base,p,src,j)
runner.immutable(out/'PROPOSAL.json',runner.encoded(p))
runner.immutable(out/'PINS.json',runner.encoded(dict(base_snapshot=runner.sha(runner.encoded(base)),contract_sha256=sha(cp),production_git_commit=contract['production_git_commit'],source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],owner=runner.read(job/'OWNER.json'),core_refs=[seg[30]['ref'],seg[49]['ref']],core_indices=[seg[30]['source_index'],seg[49]['source_index']],next_ref=seg[50]['ref'],context_through='Tamid 27b:10',independence='Root producer has not opened independent Tamid004 reading or findings; prior opening review exposure disclosed.',new_rows=len(p['records']),replacements=replacements)))
print(json.dumps(dict(proposal_sha256=sha(out/'PROPOSAL.json'),new_rows=len(p['records']),superseded=len(replacements),new_cores=20)))
