"""Bounded next-release source reading; no frozen assembly mutation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r035');c=a.claim;q=a.question;e=a.e
parent='6c1f1a43e1e07f0772cd625422949e0673e777a153dde1e6bfc081211cc96833'
refs=['12b:'+str(i) for i in range(9,15)]+['13a:1']
a.structure('inheritance',['12b:9','12b:10'],'Contiguous firstborn shares and the levir’s inherited share')
a.structure('adjacency',['12b:11','12b:12'],'Request for an allotment adjoining purchased land')
a.structure('two_channels',['12b:13'],'Two fields supplied by two channels')
a.structure('one_channel',['12b:14'],'Two fields supplied by one channel')
a.structure('river_channel',['13a:1'],'Division where one side has a channel and the other a river')
firstborn=c('firstborn','12b:9','פשיטא חלק בכור וחלק פשוט יהבינן ליה אחד מצרא','Rav Huna son of Rav Yehoshua treats it as obvious that the firstborn’s extra and ordinary shares are allotted along one boundary.',candidates=['רב הונא בריה דרב יהושע'],conditions=['firstborn receiving extra and ordinary shares'],scope='Contiguous allotment in the stated inheritance setting')
levirq=q('levir_q','12b:9','יבם מאי','Rav Huna son of Rav Yehoshua asks whether the same applies to the levir.',candidates=['רב הונא בריה דרב יהושע'],uncertainty=['Question concerns contiguous allocation in the preceding inheritance context; no unprinted family case supplied.'])
abaye=c('abaye','12b:10','אמר אביי היא היא','Abaye applies the same contiguous-allotment rule to the levir.',candidates=['אביי'],conditions=['levir’s allocation in this inheritance setting'])
whyq=q('why_q','12b:10','מאי טעמא','What is the reason for applying the same rule?',uncertainty=['Reason-question embedded after Abaye’s answer; no independent named questioner asserted.'])
called=c('called','12b:10','בכור קרייה רחמנא','The explanation is that Scripture calls him a firstborn.',candidates=['אביי'],scope='Reason attached to Abaye’s stated answer')
rava=c('rava','12b:10','רבא אמר אמר קרא (דברים כה, ו) והיה הבכור הוייתו כבכור ואין חלוקתו כבכור','Rava reads והיה הבכור as making his status like a firstborn but not his allocation like a firstborn’s.',candidates=['רבא'],conditions=['levir’s inherited allocation'],composition='composite',scope='Explicit distinction concerning inheritance allocation; no final ruling printed for this dispute in the window')
e('abaye_answer',abaye,levirq,'answer','12b:10');e('reason_answer',called,whyq,'answer','12b:10');e('called_support',called,abaye,'support','12b:10');e('rava_answer',rava,levirq,'answer','12b:10');e('rava_distinction',rava,abaye,'distinction','12b:10')
purchase=c('purchase','12b:11','ההוא דזבן ארעא אמצרא דבי נשיה','The narrative introduces a man who bought land adjoining property of בי נשיה.',scope='Narrative setting; source relational phrase retained without adding an unstated inheritance genealogy')
request=c('request','12b:11','כי קא פלגו אמר להו פליגו לי אמצראי','At division he requests an allotment adjoining his existing boundary.',conditions=['division of the jointly held property'],scope='Quoted request in the narrative')
rabbah=c('rabbah','12b:11','אמר רבה כגון זה כופין על מדת סדום','Rabbah says that in such a case one compels against middat Sedom.',candidates=['רבה'],conditions=['request for adjoining allotment in the described case'],mode='challenged',scope='Proposed compulsion challenged by Rav Yosef; רבה not conflated with רבא')
yosef=c('yosef','12b:12','אמרי ליה אחי מעלינן ליה עלויא כי נכסי דבי בר מריון','Rav Yosef objects that the brothers can demand a higher valuation for it, like the property of the house of bar Maryon.',candidates=['רב יוסף'],conditions=['brothers respond to the requested adjoining allotment'],scope='Their available counterargument as stated by Rav Yosef; no fabricated exact price')
ruling=c('ruling','12b:12','והלכתא כרב יוסף','The anonymous ruling follows Rav Yosef in this case.',scope='Explicit local source ruling; not a ruling on the preceding levir dispute')
e('rabbah_request',rabbah,request,'answer','12b:11');e('yosef_objection',yosef,rabbah,'objection','12b:12');e('ruling_resolution',ruling,yosef,'local_resolution','12b:12')
two=c('two','12b:13','תרי ארעתא אתרי נגרי','The next case concerns two fields on two channels.',conditions=['two fields','two distinct channels'],scope='Case premise, not an independently attributed legal position')
tworabbah=c('two_rabbah','12b:13','אמר רבה כגון זה כופין על מדת סדום','Rabbah again allows compulsion against middat Sedom in this case.',candidates=['רבה'],conditions=['two fields on two channels'],mode='challenged')
twoyosef=c('two_yosef','12b:13','מתקיף לה רב יוסף זמנין דהאי מדויל והאי לא מדויל','Rav Yosef objects that one may supply irrigation while the other does not.',candidates=['רב יוסף'],conditions=['two different channels may differ in irrigation availability'],scope='Potential relevant difference, not a claim that one channel presently failed')
tworuling=c('two_ruling','12b:13','והלכתא כרב יוסף','The anonymous ruling follows Rav Yosef in the two-channel case.',conditions=['two-channel case'],scope='Separate occurrence of an explicit local ruling')
e('two_objection',twoyosef,tworabbah,'objection','12b:13');e('two_resolution',tworuling,twoyosef,'local_resolution','12b:13')
one=c('one','12b:14','תרתי אחד נגרא','The next case concerns two fields on one channel.',conditions=['two fields','one channel'],scope='Changed case premise')
oneyosef=c('one_yosef','12b:14','א"ר יוסף כגון זה כופין על מדת סדום','Rav Yosef allows compulsion against middat Sedom in the single-channel case.',candidates=['רב יוסף'],conditions=['two fields on one channel'])
abayeob=c('abaye_objection','12b:14','מתקיף לה אביי מצי אמר בעינא דאפיש אריסי','Abaye objects that a party can say he wants to increase his tenant-farmers.',candidates=['אביי'],conditions=['one-channel allocation case'],mode='challenged',scope='Possible counterargument, not an asserted actual desire of a named party')
oneruling=c('one_ruling','12b:14','והלכתא כרב יוסף','The anonymous ruling follows Rav Yosef in the single-channel case.',conditions=['two fields on one channel'])
notreason=c('not_reason','12b:14','אפושי לאו מילתא היא','Increasing the tenant-farmers is dismissed as not a sufficient consideration here.',conditions=['this proposed objection in the single-channel case'],scope='Accepted rejection of the objection; assertion mode remains asserted, not rejected')
e('one_distinction',oneyosef,twoyosef,'distinction','12b:14');e('abaye_objection_edge',abayeob,oneyosef,'objection','12b:14');e('one_resolution',oneruling,oneyosef,'local_resolution','12b:14');e('not_reason_correction',notreason,abayeob,'correction','12b:14');e('not_reason_support',notreason,oneruling,'support','12b:14')
corner=c('corner','13a:1','חד גיסא נגרא וחד גיסא נהרא פלגין לה בקרנא זול','With a channel on one side and a river on the other, the property is divided בקרנא זול, diagonally.',conditions=['channel on one side','river on other side'],scope='Anonymous allocation rule; no unprinted dimensional plan or additional rationale supplied',uncertainty=['Printed technical expression בקרנא זול retained alongside the diagonal gloss.'])
for row in a.rows:
 if row['layer']=='questions':
  row['content']['answer_set_status']='partial'
  row['uncertainty'].append('Source-present answers for this exact question are represented; no exhaustive choice inventory or task qualification established.')
# Serialize only explicit authored objects and the eight completed source passes.
state=r.current(a.job);assert r.sha(r.encoded(state))==parent
active=[x for x in state['records'] if x['release_state']=='valid']+a.rows
cov=[]
for ref in refs:
 sid=a.refs[ref]['id']
 for layer in r.LAYERS:
  ids=[x['id'] for x in active if x['layer']==layer and any(v['segment_id']==sid for v in x['evidence'])]
  cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read original12b:1–13b:12 and reread12b:9–13a:1. Completed bounded contiguous-allocation discussion before next buyout topic. Preserve narrative requests, levir dispute without invented resolution, distinct water conditions, three explicit local rulings, rejection polarity, names רבה versus רבא, and anonymous final rule. '+layer+' pass: '+('supported objects retained.' if ids else 'no additional independent object found.')))
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/bava_batra_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/bava_batra_continuation_2',model_id=None),records=a.rows,coverage=cov,open_tails=state['open_tails'])
# Validate against the frozen common implementation before immutable staging.
r.validate_apply(state,p,a.source,a.meta)
out=a.job/'staging'/'next_release_20261127_contiguous035.json';r.immutable(out,r.encoded(p));print(out)
