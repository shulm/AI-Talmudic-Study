"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='a127b8cca75055de760f16fffe6824eb06eb2050717532a6a578332043206b2e';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
assert I[87]['ref']=='Yoma 5b:7' and I[107]['ref']=='Yoma 6b:3'
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='yom.s2703.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('clothes','structure',range(87,93),dict(title='סדר הלבשת אהרן ובניו: מטרת השאלה ומחלוקת באבנט',primary=True,boundary='closed',legacy_ids=[]))
s2=add('wife','structure',range(93,108),dict(title='פרישה מטומאת ביתו וזמן טבילת בועל נדה עד תיובתא',primary=True,boundary='closed',legacy_ids=[]))
e('structurelink',87,'yom.s2702.next.scope',s1,'continuation')
roles={87:'Question, historical-purpose objection, future reformulation and rejection',88:'Exegetical purpose and unnamed two-view dispute',89:'Abaye limits agreement and disagreement; rival proofs and objection',90:'Response for simultaneous-order view',91:'Objection and response for sequential-order view',92:'Extra-verse inference and clarification of simultaneity',93:'Return to separation and challenge to restating its basis',94:'Clarified house-separation question and initial baraita formulation',95:'Objection to initial formulation and corrected chronology',96:'Rabbis propose Rabbi Akiva alignment before Rav Hisda',97:'Rav Hisda temporal distinction allowing sages',98:'Rabbi Zeira daytime-immersion inference',99:'Night-immersion counterfactual and sunset argument',100:'Rav Shimi of Nehardea alternative timing rebuttal',101:'First baraita objection to night immersion',102:'Expansive reading defending night possibility',103:'Second baraita and proposed immersion interpretation with rebuttal',104:'Redundancy objection begins',105:'Cross-folio completion of proposed immersion inference',106:'Qualification from bed-and-seat impurity answers redundancy',107:'Rabbi Hiyya explicit day/night baraita and conclusive refutation'}
for i,r in roles.items():
 add('u'+str(i),'utterances',i,dict(textual_voice='Named reports and anonymous argument individually attributed below',discourse_role=r,composition='composite'))
 if i not in [97,98,100]:add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara or quoted baraita',role='anonymous',candidates=[],scope=r,transmission_chain=[]))
c={};z={}
z['clothes']=q('clothes',87,'How did he dress Aaron and his sons?', ['Past inauguration clothing order'])
z['past']=q('past',87,'Why ask about what already happened?', ['Proposed purely historical purpose of clothing-order question'])
c['future']=cl('future',87,'The initial reformulation asks how they will be dressed in the future.','Proposed purpose, rejected in same segment',mode='rejected')
c['futureanswer']=cl('futureanswer',87,'The future-purpose formulation is rejected because Aaron, his sons, and Moses will come then.','Response to proposed future practical need; do not invent an independent ruling on future clothing.')
c['purpose']=cl('purpose',88,'The question about past clothing order is asked to understand the verses.','Accepted exegetical purpose, not practical prediction')
c['seq']=cl('seq',88,'One side of the dispute says Aaron was dressed first and his sons afterward.','Initially unnamed view of the sons of Rabbi Hiyya/Rabbi Yohanan dispute; no identification by name order')
c['together']=cl('together',88,'The other says Aaron and his sons were dressed together.','Initially unnamed view; meaning and garment scope clarified below')
for k,target in [('seqholder',c['seq']),('togetherholder',c['together'])]:
 add(k,'attributions',88,dict(surface='חד אמר / וחד אמר',role='position_holder',candidates=['בני רבי חייא','רבי יוחנן'],scope='Unassigned opposing views; continuation does not identify which named party holds which.',transmission_chain=[]),[target],unc=['No assignment from name order; named pairing remains unresolved.'])
c['agreement']=cl('agreement',89,'Abaye says all agree that for tunic and turban Aaron comes before his sons.','Shared order in both command and execution passages',cond=['Tunic and turban'],holder='אביי')
c['beltonly']=cl('beltonly',89,'Abaye locates the disagreement in the belt.','Limits scope of the initial clothing-order report',cond=['Belt'],holder='אביי')
c['seqproof']=cl('seqproof',89,'The sequential-order side cites ויחגור אותו באבנט followed by ויחגור אותם אבנט.','Proof for Aaron first and sons afterward; holder remains unnamed')
c['togetherproof']=cl('togetherproof',89,'The together-order side cites וחגרת אותם.','Proof for shared belt stage; holder remains unnamed')
z['togetherobjection']=q('togetherobjection',89,'How does the together-order side explain separate ויחגור אותו and ויחגור אותם clauses?', ['Unnamed together-order view','Belt passages'])
c['differentbelt']=cl('differentbelt',90,'That side answers that the high priest’s belt is not the same as the ordinary priest’s belt.','Response on behalf of unnamed together-order side; no name assignment',cond=['High priest versus ordinary priest belt'])
z['seqobjection']=q('seqobjection',91,'How does the sequential-order side explain וחגרת אותם אבנט?', ['Unnamed Aaron-first view','Combined plural command'])
c['samebelt']=cl('samebelt',91,'That side answers that the high priest’s belt is the same as the ordinary priest’s belt.','Response on behalf of unnamed sequential-order side',cond=['High priest versus ordinary priest belt'])
z['extraverse']=q('extraverse',92,'Why are separate ויחגור אותו and ויחגור אותם clauses then needed?', ['Combined plural command explained as belt identity'])
c['seqinference']=cl('seqinference',92,'The separate clauses establish Aaron first and his sons afterward.','Argument in defense of sequential reading, not named identification')
z['simultaneous']=q('simultaneous',92,'Is dressing them simultaneously physically possible?', ['Meaning of בבת אחת in the opposed account'])
c['advance']=cl('advance',92,'The reply says לא צריכא דאקדים, reframing the issue in terms of advancing the order rather than literal physical simultaneity.','Local clarification; exact item advanced is not explicit in this short source segment.',unc=['The terse דאקדים is retained without inventing an explicit object or identifying a named holder.'])
z['separate']=q('separate',93,'Why is the high priest separated?', ['Return to opening Mishnah'])
c['already']=cl('already',93,'The basis for separation has already been given according to Rabbi Yohanan and according to Resh Lakish.','Response rejects restating the already-addressed question; different sources not collapsed')
z['home']=q('home',94,'Why must he separate specifically from his home?', ['High-priest separation before Yom Kippur','Reformulated question concerns marital contact'])
c['initialwife']=cl('initialwife',94,'The first wording of Rabbi Yehuda ben Beteira’s baraita fears that his wife will be found a possible menstruant and he will have intercourse with her.','Initial temporal formulation challenged and corrected at6a6',cond=['Possible menstrual impurity found before intercourse in initial wording'],holder='רבי יהודה בן בתירה',mode='rejected')
z['wicked']=q('wicked',95,'Are we dealing with wicked people?', ['Initial wording would place intercourse after discovery of possible menstrual impurity'])
c['correctwife']=cl('correctwife',[94,95],'The corrected fear is that he may have intercourse with his wife and she will afterward be found a possible menstruant.','Corrected temporal formulation of the baraita; not deliberate intercourse with known impurity',cond=['Intercourse first','Possible menstrual impurity discovered afterward'],holder='רבי יהודה בן בתירה',mode='reconciled')
c['proposeakiva']=cl('proposeakiva',96,'The rabbis before Rav Hisda propose that this follows Rabbi Akiva, who says the menstruant renders her partner impure.','Tentative identification, qualified by Rav Hisda next',cond=['Retrospective discovery in the baraita'],holder='רבנן לפני רב חסדא',mode='challenged')
c['sages']=cl('sages',96,'They cite the sages’ contrary statement that the menstruant does not render her partner impure.','View cited in support of proposed Rabbi-Akiva-only reading; temporal scope restricted next',cond=['Disputed retrospective-impurity case'],holder='חכמים — במסירת הדיון')
c['hasda']=cl('hasda',97,'Rav Hisda answers that the baraita can follow the sages: they disagree with Rabbi Akiva in אחר אחר, but agree in חד אחר.','Temporal distinction preserves compatibility with sages',cond=['Distinguish source timing categories אחר אחר and חד אחר'],holder='רב חסדא',unc=['This local source gives the timing categories without numerical durations; none supplied.'])
c['zeira']=cl('zeira',98,'Rabbi Zeira infers that the partner of a menstruant is not like the menstruant herself for immersion timing and immerses by day.','Daytime-immersion inference from separation schedule',cond=['בועל נדה at end of purification period'],holder='רבי זירא')
c['nightproblem']=cl('nightproblem',99,'If the partner had to immerse at night like the menstruant, he could not serve the next day because sunset after immersion would still be required.','Counterfactual supporting Rabbi Zeira; no claim that night immersion is the final rule',cond=['Night immersion after separation period','Service the following day','Sunset still required'],mode='hypothetical')
z['nightservice']=q('nightservice',99,'How could he serve the following day after night immersion, given the requirement of sunset?', ['Counterfactual: partner immerses at night like menstruant'])
c['shimi']=cl('shimi',100,'Rav Shimi of Nehardea says the partner could still be like the menstruant if separation begins one interval before sunset.','Alternative timing undermines the inference from schedule alone; later explicitly refuted',cond=['Separation begins שעה אחת סמוך לשקיעת החמה'],holder='רב שימי מנהרדעא',mode='rejected')
c['dayrule']=cl('dayrule',101,'The first baraita says all required immersions are by day, while a menstruant and a woman after childbirth immerse at night.','First objection source; proposed extension of the exceptions follows',holder='Anonymous first baraita')
c['exclude']=cl('exclude',101,'The objection infers that the night exception names the menstruant but not her partner.','Proposed inference against partner night immersion, answered next')
c['inclusion']=cl('inclusion',102,'The defense reads “menstruant” as including everything derived by expansion of that category.','Attempt to include her partner in night exception; not final accepted rule',mode='challenged')
c['keri']=cl('keri',103,'The second baraita compares one with a seminal emission to one who touched a creeping creature.','First comparison preserved, not discarded as context',holder='Anonymous second baraita')
c['partnercorpse']=cl('partnercorpse',103,'It compares the partner of a menstruant to one impure through a corpse.','Second comparison whose scope is debated',holder='Anonymous second baraita')
z['immersioncompare']=q('immersioncompare',103,'Does the comparison concern immersion timing?', ['Partner of menstruant compared to corpse-impure person'])
c['impurityanswer']=cl('impurityanswer',103,'The first answer says the comparison concerns their impurity, not immersion timing.','Defense against the timing inference')
c['redundant']=cl('redundant',104,'Both already have seven-day impurity explicitly written, so a comparison merely about duration appears redundant.','Objection to the impurity-only explanation',cond=['Partner of menstruant and corpse-impure person both seven days'])
z['renewed']=q('renewed',[104,105],'Must the comparison therefore refer to their immersions?', ['Both impurity durations explicitly seven days','Redundancy objection crosses folio'])
c['impuritydefense']=cl('impuritydefense',106,'The reply retains impurity as the subject because the latter clause is needed.','Answer to renewed immersion inference')
c['bedseat']=cl('bedseat',106,'The partner of a menstruant is more severe in rendering bed and seat impure with a lighter impurity that contaminates foods and liquids.','Needed latter-clause distinction; preserves lighter impurity scope',cond=['Bed and seat','Transmission to foods and liquids'])
c['hiyyaday']=cl('hiyyaday',107,'Rabbi Hiyya’s baraita explicitly lists the zav, zavah, male and female persons with leprosy, partner of a menstruant, and corpse-impure person as immersing by day.','Explicit list defeats the night-immersion position',holder='רבי חייא — ברייתא')
c['hiyyanight']=cl('hiyyanight',107,'The same baraita places the menstruant and woman after childbirth in the night-immersion category.','Contrasting exception list',holder='רבי חייא — ברייתא')
c['refuted']=cl('refuted',107,'The discussion concludes תיובתא against the position allowing the partner’s immersion category to be like a menstruant’s at night.','Explicit final refutation of Rav Shimi’s contrary possibility; earlier defenses preserved')
for k,ii,a,b,r in [
 ('purpose',88,c['purpose'],z['clothes'],'answer'),('past',87,z['past'],z['clothes'],'objection'),('future',87,c['futureanswer'],c['future'],'objection'),
 ('scope1',89,c['agreement'],c['seq'],'qualification'),('scope2',89,c['beltonly'],c['together'],'qualification'),('seqproof',89,c['seqproof'],c['seq'],'support'),('togetherproof',89,c['togetherproof'],c['together'],'support'),
 ('different',90,c['differentbelt'],z['togetherobjection'],'answer'),('same',91,c['samebelt'],z['seqobjection'],'answer'),('extra',92,c['seqinference'],z['extraverse'],'answer'),('advance',92,c['advance'],z['simultaneous'],'answer'),
 ('already',93,c['already'],z['separate'],'answer'),('home',95,c['correctwife'],z['home'],'answer'),('wicked',95,z['wicked'],c['initialwife'],'objection'),('correction',95,c['correctwife'],c['initialwife'],'correction'),
 ('hasda',97,c['hasda'],c['proposeakiva'],'qualification'),('night',99,c['nightproblem'],c['zeira'],'support'),('shimi',100,c['shimi'],c['nightproblem'],'objection'),('first',101,c['exclude'],c['shimi'],'objection'),('expand',102,c['inclusion'],c['exclude'],'objection'),
 ('impurity',103,c['impurityanswer'],z['immersioncompare'],'answer'),('redundancy',104,c['redundant'],c['impurityanswer'],'objection'),('defense',106,c['impuritydefense'],z['renewed'],'answer'),('bedseat',106,c['bedseat'],c['impuritydefense'],'support'),('refute',107,c['hiyyaday'],c['shimi'],'objection'),('resolution',107,c['hiyyaday'],c['zeira'],'support'),('outcome',107,c['refuted'],c['shimi'],'local_resolution')]:e(k,ii,a,b,r)
notes={87:'Historical and future-purpose suggestions separated; future objection preserved.',88:'Purpose is exegesis; both unnamed opinions retained, names not assigned by order.',89:'Shared tunic/turban order distinguished from belt dispute; both proofs and objection retained.',90:'Different-belt response remains attached to unnamed side.',91:'Same-belt answer remains attached to other unnamed side.',92:'Extra-verse inference and physical-simultaneity question retained; terse דאקדים marked uncertain rather than expanded from memory.',93:'Return to separation distinguished from already-given Yohanan/Resh Lakish derivations.',94:'Initial baraita chronology preserved as rejected; corrected wording read next.',95:'Intercourse precedes discovery in corrected wording; no deliberate-wrongdoing attribution.',96:'Rabbis’ proposed alignment not final; sages’ statement restricted by next response.',97:'Rav Hisda compatibility and both timing categories retained without invented durations.',98:'Rabbi Zeira daytime inference explicit.',99:'Counterfactual night schedule and sunset requirement retained.',100:'Rav Shimi name and pre-sunset condition preserved; later refutation reflected in status.',101:'General day rule, two named exceptions, and exclusion inference distinguished.',102:'Expansive defense preserved without overriding final baraita.',103:'Both comparisons, timing question and impurity answer retained.',104:'Two explicit seven-day durations form redundancy objection.',105:'Read full cross-folio objection; not an independent final ruling.',106:'Impurity-only defense and light bed/seat impurity to foods/liquids retained.',107:'Complete Rabbi Hiyya day list and night exceptions, explicit תיובתא and target retained; next corpse-impurity topic read through6b9 as context only.'}
C=[]
for i in range(87,108):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==I[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Actual source omission reread: ' if l=='reconciliation' else 'Direct '+l+' source pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=C,open_tails=S['open_tails'])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'yoma_5b7_6b3_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=21,sha256=hashlib.sha256(b).hexdigest())))
