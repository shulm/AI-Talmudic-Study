"""Serialize manually authored original-source readings; no semantic generation."""
import json, sys
from pathlib import Path
sys.path.insert(0, r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
base=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01')
job=base/'bavli_ketubot'
j, rows=r.load(job)
byref={x['ref'].split(' ',1)[1]:x for x in rows.values()}
records=[]
def evidence(ref, quote=None):
    s=byref[ref]; t=s['text']; q=t if quote is None else quote
    assert t.count(q)==1, (ref,q)
    a=t.index(q)
    return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(key,layer,refs,content,links=(),uncertainty=(),origin='source_paraphrase'):
    es=[evidence(*x) if isinstance(x,tuple) else evidence(x) for x in refs]
    rid='kt.open1.'+key
    records.append(dict(id=rid,layer=layer,evidence=es,content=content,origin=origin,links=['kt.open1.'+x for x in links],uncertainty=list(uncertainty)))
    return rid
def claim(key,refs,text,conditions=(),mode='asserted',scope='Local marriage timing and maintenance discussion',uncertainty=()):
    return add(key,'claims',refs,dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),uncertainty=uncertainty)
def question(key,refs,text,conditions=(),status='unreviewed_alternatives'):
    add(key,'questions',refs,dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status=status))
def position(key,refs,holder,c,conditions=(),status='asserted locally',q=None,uncertainty=()):
    add(key,'positions',refs,dict(holder_candidates=[holder] if holder else [],claim_id='kt.open1.'+c,question_id='kt.open1.'+q if q else None,conditions=list(conditions),local_status=status),links=[c]+([q] if q else []),uncertainty=uncertainty)
def attr(key,refs,surface,role,scope,chain=(),candidates=None):
    add(key,'attributions',refs,dict(surface=surface,role=role,candidates=[surface] if candidates is None else candidates,scope=scope,transmission_chain=list(chain)))
def edge(key,refs,src,target,relation,editorial=False):
    add(key,'edges',refs,dict(source_id='kt.open1.'+src,target_id='kt.open1.'+target,relation=relation,explicitness='editorial_reconstruction' if editorial else 'source_explicit'),links=[src,target],origin='editorial_inference' if editorial else 'source_paraphrase')

# Primary ownership preserves all original punctuation and markup.
add('s.mishnah','structure',['2a:1'],dict(title='Marriage weekdays and access to court',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.timing','structure',[f'2a:{i}' for i in range(2,7)],dict(title='Correcting the report: court access, feast preparation, and Sunday maintenance',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.accidents','structure',[f'2a:{i}' for i in range(7,12)]+[f'2b:{i}' for i in range(1,5)],dict(title='Illness and menstruation: alternative report, conditional inquiries, and a disputed inference',primary=True,boundary='closed',legacy_ids=[]),uncertainty=['Local maintenance subdiscussion closes; Rava introduces a linked comparison with divorce at 2b:5. The wider topic is not declared finished.'],origin='editorial_inference')
utterances=[
('u1',['2a:1'],'unnamed Mishnah','marriage rules with rationale','composite'),
('u2',['2a:2','2a:3'],'Rav Yosef reports Rav Yehuda reports Shmuel','initial report, subsequently reformulated','composite'),
('u4a',[('2a:4','אמר רב יוסף מריה דאברהם תלי תניא בדלא תניא')],'Rav Yosef','objection to initial report','atomic'),
('u4b',[('2a:4','הי תניא והי לא תניא הא תניא והא תניא אלא תלי תניא דמפרש טעמא בדתניא דלא מפרש טעמא')],'anonymous discussion correcting the objection wording','clarification','composite'),
('u5',['2a:5'],'reformulated report of Rav Yehuda in Shmuel’s name','question, court rationale, objection, feast-preparation answer','composite'),
('u6',['2a:6'],'continuation of reformulated report','maintenance consequence and embedded Mishnah quotation','composite'),
('u7',['2a:7'],'continuation of first version','extension to illness and menstruation','composite'),
('u8',['2a:8'],'anonymous alternative report','inquiry distinguishing regulatory impediment from illness','composite'),
('u9',['2a:9'],'anonymous alternative report','conditional inquiry about her illness','composite'),
('u10',['2a:10'],'anonymous alternative report','conditional inquiry about menstruation','atomic'),
('u11',['2a:11','2b:1'],'anonymous alternative report','expected-period exclusion and unexpected-period alternatives','composite'),
('ub2',['2b:2'],'Rav Achai','attempted resolution from grammatical wording','composite'),
('ub3',['2b:3'],'anonymous exposition of Rav Achai’s proof','elimination and inference','composite'),
('ub4',['2b:4'],'Rav Ashi','counterinterpretation of Mishnah wording','composite')]
for key,refs,voice,role,composition in utterances:
    add(key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition=composition))

claim('c.virgin',[('2a:1','בתולה</strong></big> נשאת ליום הרביעי')],'A virgin marries on Wednesday.')
claim('c.widow',[('2a:1','ואלמנה ליום החמישי')],'A widow marries on Thursday.')
claim('c.courts',[('2a:1','שפעמים בשבת בתי דינין יושבין בעיירות ביום השני וביום החמישי')],'Town courts sit twice weekly, Monday and Thursday.')
claim('c.complaint',[('2a:1','שאם היה לו טענת בתולים היה משכים לבית דין:')],'The Wednesday marriage allows prompt court attendance for a virginity complaint.',['husband has a virginity complaint'])
claim('c.deadline',[('2a:2','לפי ששנינו הגיע זמן ולא נישאו אוכלות משלו ואוכלות בתרומה')],'The quoted Mishnah provides maintenance from the betrothed man and terumah consumption when the appointed time arrives without marriage.',['appointed time arrived','marriage did not take place'],scope='Quoted Mishnah; terumah presupposes relevant priestly eligibility')
claim('c.initial_derivation',['2a:2','2a:3'],'The initial transmission explains Wednesday marriage by the rule about maintenance after the appointed time; this explanatory direction is challenged and reformulated.',mode='challenged')
claim('c.sunday_initial',['2a:3'],'In the initial report, Wednesday marriage excludes Sunday-deadline maintenance.',['appointed time is Sunday'],mode='challenged')
claim('c.both_taught',[('2a:4','הי תניא והי לא תניא הא תניא והא תניא')],'Both cited rules are taught; describing one as untaught is inaccurate.')
claim('c.direction',[('2a:4','אלא תלי תניא דמפרש טעמא בדתניא דלא מפרש טעמא')],'The objection is that a teaching with an explicit reason was made dependent on one lacking an explicit reason.')
claim('c.court_reform',[('2a:5','אמר רב יהודה אמר שמואל מפני מה אמרו בתולה נשאת ליום הרביעי שאם היה לו טענת בתולים היה משכים לב"ד')],'The reformulated Shmuel report first explains Wednesday by prompt court access for a virginity complaint.',['virgin marriage','possible virginity complaint'])
claim('c.feast',[('2a:5','שקדו חכמים על תקנת בנות ישראל שיהא טורח בסעודה שלשה ימים אחד בשבת ושני בשבת ושלישי בשבת וברביעי כונסה')],'The Sages provided for daughters of Israel: three days of feast preparation, Sunday through Tuesday, then marriage Wednesday.')
claim('c.sunday_final',['2a:6'],'Given the feast-preparation enactment, a Sunday deadline does not trigger maintenance because he cannot then marry.',['appointed time is Sunday','prevented by the described enactment'])
claim('c.ill_him',[('2a:7','לפיכך חלה הוא או שחלתה היא או שפירסה נדה אינו מעלה לה מזונות')],'In the first version, he owes no maintenance when his illness prevents marriage.',['his illness prevents marriage'],uncertainty=['The following alternative version presents this as an inquiry rather than a settled consequence.'])
claim('c.ill_her',['2a:7'],'In the first version, he owes no maintenance when her illness prevents marriage.',['her illness prevents marriage'],uncertainty=['Alternative version below leaves the case in a conditional inquiry.'])
claim('c.niddah',['2a:7'],'In the first version, he owes no maintenance when she becomes menstruant.',['menstruation prevents marriage'],uncertainty=['Alternative version distinguishes expected and unexpected onset.'])
claim('c.him_excuse',['2a:8'],'His illness may exempt maintenance by analogy to an unavoidable impediment.',['alternative version','his illness'],mode='hypothetical')
claim('c.him_distinguish',['2a:8'],'The exemption may instead be restricted to an impediment created by rabbinic enactment, not his illness.',['alternative version'],mode='hypothetical')
claim('c.her_ready',['2a:9'],'When she is ill, he may argue that he himself is ready.',['assuming his illness would not exempt him','her illness'],mode='hypothetical')
claim('c.her_misfortune',['2a:9'],'She may answer that the misfortune befell his field.',['assuming his illness would not exempt him','her illness'],mode='hypothetical',uncertainty=['Metaphorical legal argument preserved; no personal motive or general allocation rule inferred.'])
claim('c.expected',['2a:11','2b:1'],'At her expected menstrual time, she cannot invoke the argument that his field suffered the misfortune.',['onset at expected time'])
claim('c.unexpected_yes',['2b:1'],'Unexpected onset may permit her misfortune argument.',['onset outside expected time'],mode='hypothetical')
claim('c.unexpected_no',['2b:1'],'Because some women’s periods vary, unexpected onset may be treated like expected onset.',['onset outside expected time'],mode='hypothetical')
claim('c.achai_grammar',['2b:2'],'Rav Achai observes that the Mishnah says the women were not married (לא נישאו), not that the men did not marry (לא נשאו).')
claim('c.her_delay',['2b:3'],'If the women themselves delay, their maintenance and terumah entitlement would be inexplicable in this proposed reading.',mode='hypothetical')
claim('c.achai_proof',['2b:2','2b:3'],'Rav Achai’s proposed resolution reads the case as an involuntary impediment of this kind, yet retaining maintenance and terumah.',['involuntary impediment of the discussed kind'],mode='challenged',uncertainty=['Rav Ashi supplies a counterreading; this inference does not settle every conditional inquiry.'])
claim('c.ashi_exemption',['2b:4'],'Rav Ashi replies that one can still say any involuntary impediment exempts maintenance.',['involuntary impediment'],mode='hypothetical',uncertainty=['לעולם אימא לך functions as a counterreading, not an independently certified final halakhic ruling.'])
claim('c.ashi_men',['2b:4'],'Rav Ashi reads the Mishnah as the men delaying without the involuntary excuse under discussion.')
claim('c.ashi_style',['2b:4'],'Although masculine wording would fit that reading, the Mishnah uses feminine wording in the latter clause to match the opening clause.')

question('q.why_initial',['2a:2'],'Why was Wednesday prescribed for a virgin?',status='partial')
question('q.sunday_pay',['2a:3'],'Could a Sunday deadline already require maintenance?',['appointed time Sunday'],status='partial')
question('q.taught',[('2a:4','הי תניא והי לא תניא')],'Which rule is taught and which is supposedly untaught?',status='partial')
question('q.why_final',['2a:5'],'Why was Wednesday prescribed for a virgin?',status='partial')
question('q.sunday_wedding',[('2a:5','ותינשא באחד בשבת שאם היה לו טענת בתולים היה משכים לבית דין')],'Why not Sunday marriage, allowing a Monday court appearance?',status='partial')
question('q.him',['2a:8'],'Does his illness exempt maintenance or is the enactment-caused impediment different?',['alternative version','his illness'])
question('q.her',['2a:9'],'If his illness does not exempt him, what is the rule when she is ill?',['if his illness entails maintenance'])
question('q.niddah',['2a:10'],'If her illness allows the misfortune argument, what if she becomes menstruant?',['if her misfortune argument is accepted'])
question('q.unexpected',['2b:1'],'For unexpected menstruation, may she invoke misfortune or is variation sufficiently expected?',['onset outside expected time'])
question('q.case',['2b:3'],'What case does the Mishnah’s feminine wording describe?',status='partial')

attr('a.mishnah',['2a:1'],'unnamed Mishnah','anonymous','Opening marriage rules',candidates=[])
chain=['רב יוסף','רב יהודה','שמואל']
attr('a.yosef_report',[('2a:2','אמר רב יוסף אמר רב יהודה אמר שמואל')],'רב יוסף','transmitter','initial report',chain)
attr('a.yehuda_report',[('2a:2','אמר רב יוסף אמר רב יהודה אמר שמואל')],'רב יהודה','transmitter','initial report',chain)
attr('a.shmuel_initial',[('2a:2','אמר רב יוסף אמר רב יהודה אמר שמואל')],'שמואל','quoted_authority','initial report subsequently reformulated',chain)
attr('a.yosef_objection',[('2a:4','אמר רב יוסף')],'רב יוסף','speaker','objection to the initial explanatory direction')
attr('a.yehuda_corrected',[('2a:5','אמר רב יהודה אמר שמואל')],'רב יהודה','transmitter','reformulated transmission',['רב יהודה','שמואל'])
attr('a.shmuel_corrected',[('2a:5','אמר רב יהודה אמר שמואל')],'שמואל','quoted_authority','reformulated transmission',['רב יהודה','שמואל'])
attr('a.sages',[('2a:5','שקדו חכמים על תקנת בנות ישראל')],'חכמים','collective','feast-preparation enactment')
attr('a.alternative',[('2a:8','ואיכא דבעי לה מיבעיא')],'ואיכא דבעי לה מיבעיא','anonymous','alternative version; no named author established',candidates=[])
attr('a.achai',[('2b:2','פשיט רב אחאי')],'רב אחאי','speaker','proposed resolution from wording')
attr('a.ashi',[('2b:4','אמר רב אשי')],'רב אשי','speaker','counterreading rejecting the necessity of Rav Achai’s inference')

for key,refs,holder,c,cond,status in [
('p.virgin',['2a:1'],'unnamed Mishnah','c.virgin',[],'stated'),
('p.widow',['2a:1'],'unnamed Mishnah','c.widow',[],'stated; Thursday rationale not explained in this block'),
('p.courts',['2a:1'],'unnamed Mishnah','c.courts',[],'stated institutional premise'),
('p.complaint',['2a:1'],'unnamed Mishnah','c.complaint',['virginity complaint'],'stated rationale'),
('p.deadline',['2a:2'],'quoted Mishnah','c.deadline',['appointed time arrived without marriage'],'quoted rule; application disputed below'),
('p.initial',['2a:2','2a:3'],'Shmuel as initially transmitted','c.initial_derivation',[],'challenged formulation, replaced by corrected report'),
('p.sunday_initial',['2a:3'],'Shmuel as initially transmitted','c.sunday_initial',['Sunday deadline'],'initial explanatory direction challenged'),
('p.direction',['2a:4'],'Rav Yosef objection as clarified in the discussion','c.direction',[],'objection leading to reformulation'),
('p.reform',['2a:5'],'Shmuel as reformulated through Rav Yehuda','c.court_reform',[],'corrected report'),
('p.feast',['2a:5'],'Sages in the reformulated report','c.feast',[],'enactment reported'),
('p.sunday',['2a:6'],'reformulated report attributed to Shmuel','c.sunday_final',['Sunday deadline'],'derived consequence'),
('p.him',['2a:7'],'first version continuing the report','c.ill_him',['his illness'],'asserted in first version; alternative version queries'),
('p.her',['2a:7'],'first version continuing the report','c.ill_her',['her illness'],'asserted in first version; alternative version queries'),
('p.niddah',['2a:7'],'first version continuing the report','c.niddah',['menstruation'],'asserted in first version; alternative version queries'),
('p.expected',['2a:11','2b:1'],'anonymous alternative version','c.expected',['expected menstrual time'],'not a live inquiry in this version'),
('p.achai',['2b:2','2b:3'],'רב אחאי','c.achai_proof',['involuntary impediment'],'proposed inference challenged by Rav Ashi'),
('p.ashi',['2b:4'],'רב אשי','c.ashi_exemption',['involuntary impediment'],'possible counterreading; not final adjudication'),
('p.ashi_men',['2b:4'],'רב אשי','c.ashi_men',[],'counterinterpretation'),
('p.ashi_style',['2b:4'],'רב אשי','c.ashi_style',[],'stylistic answer to grammatical inference')]:
    position(key,refs,holder,c,cond,status)
# Anonymous hypothetical alternatives retained without inventing named holders.
for c,refs,cond in [('c.him_excuse',['2a:8'],['his illness']),('c.him_distinguish',['2a:8'],['enactment versus illness']),('c.her_ready',['2a:9'],['she is ill']),('c.her_misfortune',['2a:9'],['she is ill']),('c.unexpected_yes',['2b:1'],['unexpected menstruation']),('c.unexpected_no',['2b:1'],['unexpected menstruation'])]:
    position('p.alt.'+c,refs,None,c,cond,'anonymous candidate argument; no named adoption established')

edge('e.complaint',['2a:1'],'c.complaint','c.virgin','support')
edge('e.courts',['2a:1'],'c.courts','c.complaint','support')
edge('e.initial',['2a:2','2a:3'],'c.initial_derivation','q.why_initial','answer')
edge('e.suninitial',['2a:3'],'c.sunday_initial','q.sunday_pay','answer')
edge('e.taught',['2a:4'],'c.both_taught','q.taught','answer')
edge('e.direction',['2a:4'],'c.direction','c.initial_derivation','objection')
edge('e.correction',['2a:5'],'c.court_reform','c.initial_derivation','correction')
edge('e.whyfinal',['2a:5'],'c.court_reform','q.why_final','answer')
edge('e.sundaychallenge',['2a:5'],'q.sunday_wedding','c.court_reform','objection')
edge('e.feast',['2a:5'],'c.feast','q.sunday_wedding','answer')
edge('e.maintenance',['2a:6'],'c.feast','c.sunday_final','support')
for c in ['c.ill_him','c.ill_her','c.niddah']:
    edge('e.consequence.'+c,['2a:7'],'c.sunday_final',c,'analogy')
edge('e.version',['2a:8'],'q.him','c.ill_him','unresolved_outcome')
edge('e.himexcuse',['2a:8'],'c.him_excuse','q.him','answer')
edge('e.himdistinguish',['2a:8'],'c.him_distinguish','c.him_excuse','distinction')
edge('e.herready',['2a:9'],'c.her_ready','q.her','answer')
edge('e.hermisfortune',['2a:9'],'c.her_misfortune','c.her_ready','objection')
edge('e.expected',['2a:11','2b:1'],'c.expected','q.niddah','qualification')
edge('e.unexpectedyes',['2b:1'],'c.unexpected_yes','q.unexpected','answer')
edge('e.unexpectedno',['2b:1'],'c.unexpected_no','c.unexpected_yes','objection')
edge('e.achaisupport',['2b:2','2b:3'],'c.achai_grammar','c.achai_proof','support')
edge('e.achairesolve',['2b:2','2b:3'],'c.achai_proof','q.unexpected','answer',editorial=True)
edge('e.ashireject',['2b:4'],'c.ashi_exemption','c.achai_proof','objection')
edge('e.ashistyle',['2b:4'],'c.ashi_style','c.achai_grammar','distinction')
edge('e.ashimen',['2b:4'],'c.ashi_men','q.case','answer')

core=[f'2a:{i}' for i in range(1,12)]+[f'2b:{i}' for i in range(1,5)]
coverage=[]
checks={
'2a:1':'Re-read virgin and widow schedules, court days and complaint rationale; no reason for widow Thursday invented.',
'2a:2':'Preserved three-person transmission and embedded deadline/terumah rule; initial explanation marked challenged after continuation.',
'2a:3':'Retained Sunday hypothetical and initial conclusion; correction at 2a:5 read.',
'2a:4':'Separated Rav Yosef objection from anonymous correction of its wording; neither statement treated as final report.',
'2a:5':'Re-read question, court argument, Sunday counterexample, and three preparation days; report reformulation explicit.',
'2a:6':'Both maintenance and terumah in quoted rule retained; Sunday exception derived in correct direction.',
'2a:7':'Separate illness of man, illness of woman and menstruation; alternative version retained, not harmonized into final ruling.',
'2a:8':'Re-read alternative report and enactment-versus-illness distinction; no final answer imposed.',
'2a:9':'Preserved if-you-say premise and both litigant arguments; no named holder or motive invented.',
'2a:10':'Conditional menstruation question remains linked to preceding premise and next-page distinction.',
'2a:11':'Read across page boundary into 2b:1; expected-time exclusion not isolated from its explanation.',
'2b:1':'Retained expected and unexpected timing and variable-cycle counterargument.',
'2b:2':'Preserved Rav Achai and masculine/feminine wording difference; not assigned to Rav Ashi.',
'2b:3':'Kept hypothetical voluntary delay distinct from inferred involuntary case and both entitlements.',
'2b:4':'Re-read Rav Ashi counterinterpretation and stylistic explanation; no final halakhic conclusion forced; 2b:5 onward read as linked context.'}
for ref in core:
    sid=byref[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=checks[ref]+(' Source-based omission reconciliation performed after layer drafting; no additional unrepresented claim found in this reading.' if layer=='reconciliation' else ' Reviewed '+layer+' in original source and continuation; '+('listed evidence-bearing records.' if ids else 'no additional independent object of this layer found.'))))
p=dict(schema_version=r.VERSION,tractate='Ketubot',owner='/root/l01_ketubot',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
r.validate_apply(r.current(job),p,rows,j)
out=base/'ketubot_proposals'/'opening_001.json'
r.immutable(out,r.encoded(p))
print(json.dumps(dict(path=str(out),sha256=r.sha(out.read_bytes()),records=len(records),core_segments=len(core))))
