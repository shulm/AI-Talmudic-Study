"""Manual semantic specifications, Eruvin 2b:2-3a:11; preserve older proposals."""
import copy
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
j,ss=runner.load(JOB); byref={r['ref'].removeprefix('Eruvin '):r for r in ss.values()}
state=runner.current(JOB);records=[]
def add(key,layer,refs,content,links=(),uncertainty=(),origin='source_paraphrase',supersedes=None):
    rid='er.objections.001.'+layer+'.'+key
    evidence=[dict(segment_id=byref[r]['id'],start_char=0,end_char=len(byref[r]['text']),quote=byref[r]['text']) for r in refs]
    row=dict(id=rid,layer=layer,evidence=evidence,content=content,links=list(links),uncertainty=list(uncertainty),origin=origin)
    if supersedes:row['supersedes']=supersedes
    records.append(row);return rid
def claim(key,ref,text,mode='asserted',conditions=(),scope='Temple-opening derivation: sequential local argument'):
    return add(key,'claims',[ref],dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode))
def question(key,refs,text,conditions=()):
    return add(key,'questions',refs,dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status='unreviewed_alternatives'))
def edge(key,refs,source,target,relation):
    return add(key,'edges',refs,dict(source_id=source,target_id=target,relation=relation,explicitness='source_explicit'),[source,target])
def attr(key,ref,surface,role,persons,scope,chain=()):
    return add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=persons,scope=scope,transmission_chain=list(chain)))
def pos(key,ref,holder,cid,conditions=(),status='Reported local position'):
    return add(key,'positions',[ref],dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(conditions),local_status=status),[cid])
refs=['2b:'+str(i) for i in range(2,17)]+['3a:'+str(i) for i in range(1,12)]
oldid='er.derivation.002.structure.structure'
oldrefs=['2a:'+str(i) for i in range(6,15)]+['2b:1']
sid=add('completed.derivation','structure',oldrefs+refs,dict(title='מקור מגבלות המבוי: פתחי המקדש, קשיים וקריאת היכר',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference',supersedes=oldid)

# These are authored semantic readings, not labels generated from source patterns.
specs=[
 ('court.dimensions','2b:2','The cited courtyard passages give length 100, width 50, height 5 and curtains of 15 on each side of the gate.'),
 ('court.proposal','2b:2','The question proposes deriving an opening five cubits high and twenty wide from the courtyard gate.','queried'),
 ('court.name','2b:3','That entrance is called פתח שער החצר, not an unqualified פתח.'),
 ('court.alt.height','2b:4','The alternative reads fifteen cubits at the side as the curtains’ height.'),
 ('court.five','2b:5','The objection cites the explicit five-cubit height.','challenged'),
 ('court.altar','2b:5','The answer reads the five cubits as measured above the altar edge.'),
 ('width.unopposed','2b:6','The objection observes no explicit Rabbi Yehuda dissent in the mishnah’s ten-cubit width clause.','challenged'),
 ('width.baraita','2b:7','Abaye answers that Rabbi Yehuda does dissent in a baraita.'),
 ('width.baraita.reduce','2b:7','The baraita first requires reducing width above ten cubits.'),
 ('width.baraita.yehuda','2b:7','In that baraita Rabbi Yehuda says width above ten cubits need not be reduced.'),
 ('width.implicit','2b:8','The answer takes Rabbi Yehuda’s stated height dissent as also applying to width.'),
 ('height.baraita','2b:9','A baraita requires reducing mavoi height above twenty cubits.'),
 ('height.yehuda','2b:9','The baraita reports Rabbi Yehuda permitting forty and fifty cubits.'),
 ('height.kappara','2b:9','Bar Kappara teaches a version permitting up to one hundred cubits.'),
 ('height.hundred','2b:10','The argument can read Bar Kappara’s one hundred as exaggeration, but still asks why fifty appears alongside the derivable forty.','hypothetical'),
 ('hisda.mistake','2b:11','Rav Hisda says a baraita misled Rav into inferring Rabbi Yehuda’s Ulam derivation from the Rabbis’ Heikhal derivation.'),
 ('hisda.baraita','2b:11','The cited baraita associates a mavoi above twenty cubits with exceeding the Heikhal entrance.'),
 ('hisda.royal','2b:11','Rav Hisda instead explains Rabbi Yehuda as learning from royal entrances.'),
 ('doors.bsh','2b:12','The cited mishnah reports Beit Shammai requiring both a sidepost and a beam.'),
 ('doors.bh','2b:12','The cited mishnah reports Beit Hillel allowing a sidepost or a beam.'),
 ('doors.privacy','2b:13','The answer treats the Heikhal doors as made only for privacy.'),
 ('form.heikhal','2b:14','The objection observes that the Heikhal has a doorway form yet its width is ten cubits.'),
 ('form.mishnah','2b:14','The quoted mishnah exempts a mavoi with doorway form from width reduction even above ten cubits.'),
 ('form.rav.correction','2b:15','When Rav Yehuda taught Hiyya bar Rav the wording אינו צריך למעט before Rav, Rav instructed him to teach צריך למעט.'),
 ('amaltara.heikhal','3a:1','The objection invokes five ornamental beams of milah wood one above another over the entrance, while the Heikhal height remains twenty.'),
 ('amaltara.ulam.possible','3a:2','A counter-question suggests the baraita about ornamental beams may refer to the Ulam.','hypothetical'),
 ('amaltara.similar.possible','3a:3','A reply suggests the Heikhal may have the same design as the Ulam.','hypothetical'),
 ('rav.beam.width','3a:4','Rabbi Ila’a reports Rav: a beam four handbreadths wide is acceptable even if not strong.'),
 ('rav.amaltara','3a:4','In the same report Rav permits an entrance above twenty cubits when it has amaltara.'),
 ('yosef.baraita','3a:5','Rav Yosef says the amaltara teaching is a baraita.'),
 ('abaye.teacher','3a:6','Abaye names Hama son of Rabbah bar Avuha as its teacher.'),
 ('baraita.still','3a:6','The argument says that even treating it as a baraita would still leave a difficulty for Rav.','challenged'),
 ('rav.tannaim','3a:7','The anonymous reply formulated on Rav’s behalf argues that the baraitot conflict even without him; a tannaitic dispute can explain them and his view.'),
 ('rnby.heker','3a:8','Rav Nahman bar Yitzhak says that without Rav’s interpretation the baraitot need not conflict: the Rabbis require the beam for recognition.'),
 ('rnby.sign','3a:8','Rav Nahman bar Yitzhak reads יתר מפתחו של היכל merely as a mnemonic measure, not the derivation of the law.'),
 ('rabbah.awareness','3a:9','Rabbah expounds למען ידעו דורותיכם: up to twenty cubits one is aware of dwelling in a sukkah; above that one is not, since the eye does not notice it.'),
 ('sukkah.parallel','3a:10','On that explanation, the sukkah dispute also concerns recognition.','conditional'),
 ('necessity.sukkah','3a:11','If only sukkah were taught, one could suppose Rabbi Yehuda permits it because sitting makes it noticeable but concedes a mavoi used for walking.','hypothetical'),
 ('necessity.mavoi','3a:11','If only mavoi were taught, one could suppose the Rabbis require recognition there but concede the sukkah case to Rabbi Yehuda.','hypothetical'),
 ('necessity.both','3a:11','The argument therefore requires both the sukkah and mavoi disputes.')]
cs={}
for row in specs:
    key,ref,text,*mode=row
    cond=[]
    if key=='width.baraita.reduce' or key=='width.baraita.yehuda':cond=['mavoi width exceeds ten cubits']
    if key=='rav.beam.width':cond=['beam width is four handbreadths']
    if key=='rav.amaltara':cond=['presence of amaltara','height exceeds twenty cubits']
    if key=='sukkah.parallel':cond=['Rav Nahman bar Yitzhak accepts Rabbah’s explanation']
    cs[key]=claim(key,ref,text,mode[0] if mode else 'asserted',cond)
qs={}
for key,rr,text,conditions in [
 ('court',['2b:2'],'Why do both sides not derive five cubits height and twenty width from the courtyard gate?',[]),
 ('height.five',['2b:5'],'How can the curtain height be fifteen if the verse says five?',[]),
 ('width',['2b:6'],'If Rabbi Yehuda derives from the Ulam, why does the mishnah not record his width dissent?',[]),
 ('width.mishnah',['2b:8'],'Why not state the width dispute in the mishnah?',[]),
 ('forty.fifty',['2b:9','2b:10'],'How can an Ulam derivation explain the reported permission of fifty or one hundred cubits?',[]),
 ('doors',['2b:12'],'If the Rabbis derive from the Heikhal opening, why are doors not required?',[]),
 ('doorway.form',['2b:14'],'Why does doorway form permit extra width if the Heikhal itself has doorway form and is only ten cubits wide?',[]),
 ('amaltara',['2b:16','3a:1'],'Should amaltara fail to permit extra height since the Heikhal also had it and was twenty cubits high?',[]),
 ('amaltara.ulam',['3a:2'],'Could the ornamental-beam teaching concern the Ulam instead?',[]),
 ('amaltara.design',['3a:3'],'Could the Heikhal share the Ulam’s design?',[]),
 ('amaltara.rav',['3a:4'],'How does the Heikhal derivation fit Rav’s reported permission with amaltara?',[]),
 ('baraita.teacher',['3a:5'],'Who teaches the amaltara baraita?',[]),
 ('baraita.rav',['3a:6'],'Even if this is a baraita, does it not still challenge Rav?',[]),
 ('baraita.conflict',['3a:7'],'Do the baraitot not conflict even if Rav is set aside?',[]),
 ('recognition.parallel',['3a:9','3a:10'],'If Rav Nahman bar Yitzhak accepts Rabbah, why state the recognition dispute twice?', ['Acceptance of Rabbah’s sukkah explanation'])]:
    qs[key]=question(key,rr,text,conditions)
voices={
'2b:2':'anonymous challenge citing courtyard verses','2b:3':'anonymous answer','2b:4':'anonymous alternative answer','2b:5':'anonymous objection and answer','2b:6':'anonymous challenge','2b:7':'Abaye quoting a baraita','2b:8':'anonymous question and answer','2b:9':'anonymous challenge quoting baraita and Bar Kappara','2b:10':'anonymous numerical objection','2b:11':'Rav Hisda explaining Rav’s inference and contesting it','2b:12':'anonymous challenge quoting Beit Shammai and Beit Hillel','2b:13':'anonymous answer','2b:14':'anonymous challenge quoting mishnah','2b:15':'anonymous answer narrating Rav’s teaching correction','2b:16':'anonymous objection continued on following page','3a:1':'anonymous objection citing ornamental beams','3a:2':'anonymous counter-question','3a:3':'anonymous counter-question','3a:4':'Rabbi Ila’a reporting Rav inside objection','3a:5':'Rav Yosef followed by anonymous question','3a:6':'Abaye followed by anonymous continuing objection','3a:7':'anonymous hypothetical answer on Rav’s behalf','3a:8':'Rav Nahman bar Yitzhak alternative explanation','3a:9':'anonymous conditional objection quoting Rabbah','3a:10':'anonymous continuation question','3a:11':'anonymous necessity resolution'}
for ref,voice in voices.items():
    add('u.'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=voice,composition='composite'),origin='editorial_inference')
    # Anonymous framing is explicit textual framing, not historical author identification.
    if ref not in ['2b:7','2b:11','3a:8']:
        attr('anonymous.'+ref.replace(':','_'),ref,'anonymous discourse framing','anonymous',[],'Question/answer or quotation framing; named quoted voices recorded separately')
for key,ref,surface,role,persons,scope,chain in [
 ('abaye','2b:7','אמר אביי','speaker',['אביי'],'Locates Rabbi Yehuda width dissent in baraita',[]),
 ('baraita.yehuda','2b:7',"ר' יהודה אומר",'quoted_authority',['רבי יהודה'],'No reduction above ten cubits',[]),
 ('height.yehuda','2b:9','ורבי יהודה מכשיר','quoted_authority',['רבי יהודה'],'Forty/fifty height permission',[]),
 ('kappara','2b:9','ותני בר קפרא','transmitter',['בר קפרא'],'Version teaching עד מאה; not automatically its position holder',[]),
 ('hisda','2b:11','א"ר חסדא','speaker',['רב חסדא'],'Critique of Rav’s inferred Ulam derivation',[]),
 ('rav.inference','2b:11','אטעיתיה לרב','quoted_authority',['רב'],'Inference attributed to Rav by Rav Hisda',[]),
 ('royal.yehuda','2b:11',"ר' יהודה",'position_holder',['רבי יהודה'],'Royal-entrance derivation according to Rav Hisda',[]),
 ('bsh','2b:12','ב"ש אומרים','collective',['בית שמאי'],'Both sidepost and beam',[]),
 ('bh','2b:12','וב"ה אומרים','collective',['בית הלל'],'Sidepost or beam',[]),
 ('ravyehuda.teacher','2b:15','מתני ליה רב יהודה','transmitter',['רב יהודה'],'Teaching אינו צריך למעט before correction',[]),
 ('rav.correction','2b:15','וא"ל אתנייה צריך למעט','speaker',['רב'],'Instructs replacement teaching; Hiyya bar Rav is recipient, not asserted authority',[]),
 ('ilaa','3a:4','אמר רבי אילעא אמר רב','transmitter',['רבי אילעא'],'Beam strength and amaltara report',['רבי אילעא','רב']),
 ('rav.amaltara','3a:4','אמר רב','quoted_authority',['רב'],'Beam width/strength and amaltara allowance',['רבי אילעא','רב']),
 ('yosef','3a:5','אמר רב יוסף','speaker',['רב יוסף'],'Classifies amaltara as baraita',[]),
 ('abaye.teacher','3a:6','אמר אביי','speaker',['אביי'],'Names teacher of baraita',[]),
 ('hama','3a:6','חמא בריה דרבה בר אבוה קתני לה','transmitter',['חמא בריה דרבה בר אבוה'],'Teacher of baraita, not a fabricated original ruling holder',[]),
 ('rav.hypothetical','3a:7','אמר לך רב','quoted_authority',['רב'],'Anonymous answer formulated on Rav’s behalf; not direct historical speech',[]),
 ('rnby','3a:8','רב נחמן בר יצחק אמר','speaker',['רב נחמן בר יצחק'],'Recognition explanation and mnemonic Heikhal reference',[]),
 ('rabbah','3a:9','דאמר רבה','quoted_authority',['רבה'],'Sukkah awareness explanation; distinguish from רבא',[])]:
    attr(key,ref,surface,role,persons,scope,chain)
for key,ref,holder,cid,status in [
 ('abaye','2b:7','אביי','width.baraita','Reply to supposed absence of width dissent'),
 ('yehuda.width','2b:7','רבי יהודה','width.baraita.yehuda','Position quoted from baraita'),
 ('yehuda.height','2b:9','רבי יהודה','height.yehuda','Height allowance as quoted, challenged as to derivation'),
 ('hisda.error','2b:11','רב חסדא','hisda.mistake','Critique; does not establish Rav himself retracted'),
 ('hisda.royal','2b:11','רב חסדא','hisda.royal','Explanation attributed to Rav Hisda'),
 ('bsh','2b:12','בית שמאי','doors.bsh','Quoted rule'),
 ('bh','2b:12','בית הלל','doors.bh','Quoted rule'),
 ('rav.form','2b:15','רב','form.rav.correction','Reported textual correction of teaching'),
 ('rav.width','3a:4','רב','rav.beam.width','Report through Rabbi Ila’a'),
 ('rav.amaltara','3a:4','רב','rav.amaltara','Report through Rabbi Ila’a; competing source framing at 3a:5'),
 ('yosef','3a:5','רב יוסף','yosef.baraita','Classifies source as baraita'),
 ('abaye.teacher','3a:6','אביי','abaye.teacher','Identifies teacher'),
 ('rav.hypothetical','3a:7','רב','rav.tannaim','Anonymous hypothetical defense, not attested self-retraction'),
 ('rnby.recognition','3a:8','רב נחמן בר יצחק','rnby.heker','Alternative explanatory account'),
 ('rnby.sign','3a:8','רב נחמן בר יצחק','rnby.sign','Heikhal phrase as mnemonic'),
 ('rabbah','3a:9','רבה','rabbah.awareness','Quoted interpretation')]:
    cond=next(r['content']['conditions'] for r in records if r['id']==cs[cid])
    pos(key,ref,holder,cs[cid],cond,status)
for key,ref,src,tgt,relation in [
 ('court.answer','2b:3','court.name','court','answer'),
 ('court.alternative','2b:4','court.alt.height','court','answer'),
 ('court.height.answer','2b:5','court.altar','height.five','answer'),
 ('width.answer','2b:7','width.baraita','width','answer'),
 ('width.mishnah.answer','2b:8','width.implicit','width.mishnah','answer'),
 ('height.answer','2b:11','hisda.royal','forty.fifty','answer'),
 ('doors.answer','2b:13','doors.privacy','doors','answer'),
 ('form.answer','2b:15','form.rav.correction','doorway.form','answer'),
 ('teacher.answer','3a:6','abaye.teacher','baraita.teacher','answer'),
 ('rav.defense','3a:7','rav.tannaim','baraita.rav','answer'),
 ('recognition.answer','3a:11','necessity.both','recognition.parallel','answer')]:
    edge(key,[ref],cs[src],qs[tgt],relation)
edge('width.support',['2b:7'],cs['width.baraita.yehuda'],cs['width.baraita'],'support')
edge('hisda.challenge',['2b:11'],cs['hisda.royal'],'er.derivation.002.claims.rav.yehuda','correction')
edge('heikhal.rationale',['3a:8'],cs['rnby.heker'],cs['rnby.sign'],'support')
edge('recognition.challenge',['3a:9','3a:10'],qs['recognition.parallel'],cs['rnby.heker'],'objection')
edge('necessity.sukkah',['3a:11'],cs['necessity.sukkah'],cs['necessity.both'],'support')
edge('necessity.mavoi',['3a:11'],cs['necessity.mavoi'],cs['necessity.both'],'support')
# The source-role schema cannot encode Hiyya bar Rav as addressee; do not mislabel him.
# Preserve him in the narrative claim and record the modeling limitation locally.
next(r for r in records if r['id']==cs['form.rav.correction'])['uncertainty']=['Hiyya bar Rav is the recipient in this teaching scene; schema has no addressee role, so no false quoted_authority attribution is emitted.']
next(r for r in records if r['id']==cs['height.hundred'])['uncertainty']=['The raw string at 2b:10 reads לרב יהודה in one clause; do not silently normalize that occurrence into a new Rav Yehuda position. Context discusses Rabbi Yehuda and Rav’s derivation.']
coverage=[]
# Replace only coverage references to the superseded structure, preserving all other records.
for cov in state['coverage']:
    if oldid in cov['record_ids']:
        new={k:copy.deepcopy(v) for k,v in cov.items() if k!='proposal_execution'}
        new['record_ids']=[sid if x==oldid else x for x in new['record_ids']]
        new['rationale']='Previously read structure extended through the inspected completion at 3a:11; earlier semantic judgments preserved.'
        coverage.append(new)
for ref in refs:
    sourceid=byref[ref]['id']
    for layer in runner.LAYERS:
        ids=[r['id'] for r in records if (layer=='reconciliation' or layer==r['layer']) and any(x['segment_id']==sourceid for x in r['evidence'])]
        coverage.append(dict(segment_id=sourceid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Manual complete source pass and omission reread: arguments, alternatives, hypothetical defenses, quoted voices, numerical objections, and conditions retained. 2b:16 continues into 3a:1, not a page-based boundary.' if ids else 'Actual source pass found no additional '+layer+' object here; question-only or continuation-only material retained in its applicable layers.'))
proposal=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=Path(__file__).with_name('eruvin_objections_001.json');runner.immutable(out,runner.encoded(proposal))
print(runner.submit(JOB,out,'L03/eruvin',2));print(runner.replay(JOB))
