"""Explicit source reading, Moed Katan 2b:3–3a:11; no automatic inference."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from author_remaining_openings_001 import Reading,r
a=Reading('moed_katan','Moed Katan','mk.r004')
assert r.sha(r.encoded(r.current(a.job)))=='0213d8f3ab29abf7830ecf383f1bbb89b6fa5b05f518fd25d47cc3ded6712bdc'

def narrow(ref,quote):
    s=a.refs[ref];assert s['text'].count(quote)==1,(ref,quote)
    start=s['text'].index(quote);return dict(segment_id=s['id'],start_char=start,end_char=start+len(quote),quote=quote)
def voice(key,ref,quote,holder=None,role='speaker',composition='atomic',act='assertion'):
    u=a.add(key+'.u','utterances',dict(textual_voice=holder or 'anonymous discussion',discourse_role=act,composition=composition),[ref])
    a.rows[-1]['evidence']=[narrow(ref,quote)]
    at=a.add(key+'.a','attributions',dict(surface=holder or '',role=role if holder else 'anonymous',candidates=[holder] if holder else [],scope=u,transmission_chain=[]),[ref],[u])
    a.rows[-1]['evidence']=[narrow(ref,quote)]
    if holder and quote!=a.refs[ref]['text']:a.rows[-1]['evidence'].append(a.evidence(ref))
    return u
def c(key,ref,quote,text,holder=None,mode='asserted',conditions=(),role='speaker',composition='atomic',scope='Local Sabbath/sabbatical classification argument; not a later practical ruling',uncertainty=()):
    if composition=='composite':uncertainty=list(uncertainty)+['This source list or paired formulation is retained together; not certified as a single atomic claim.']
    u=voice(key,ref,quote,holder,role,composition,mode)
    cid=a.add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),[ref],[u],uncertainty)
    a.add(key+'.p','positions',dict(holder_candidates=[holder] if holder else [],claim_id=cid,question_id=None,conditions=list(conditions),local_status=mode+' in this local argument'),[ref],[cid],uncertainty)
    return cid
def q(key,ref,quote,text,holder=None,composition='atomic'):
    u=voice(key,ref,quote,holder,composition=composition,act='explicit question')
    return a.add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='none'),[ref],[u])
def e(key,src,dst,rel,ref):return a.e(key,src,dst,rel,ref)

a.structure('sabbath',['2b:'+str(i) for i in range(3,8)],'Weeding and irrigation: Sabbath classification and the unresolved double-liability objection')
a.structure('kilayim',['2b:'+str(i) for i in range(8,15)],'Mixed-species objection and reinterpretation as Rabbi Akiva’s maintenance rule')
a.structure('sabbatical',['2b:'+str(i) for i in range(15,20)]+['3a:'+str(i) for i in range(1,12)],'Sabbatical irrigation: alternative explanations, specified derivatives and rabbinic restrictions')
ask=q('warning','2b:3','המנכש והמשקה מים לזרעים בשבת משום מאי מתרינן ביה','For which labor is a person warned when weeding or watering seeds on the Sabbath?')
rabbah=c('rabbah','2b:3','רבה אמר משום חורש','Rabbah classifies the warning as plowing.','רבה',mode='challenged',conditions=['weeding or watering seeds on Sabbath'])
yosef=c('yosef','2b:3','רב יוסף אמר משום זורע','Rav Yosef classifies the warning as sowing.','רב יוסף',mode='challenged',conditions=['weeding or watering seeds on Sabbath'])
e('rabbah_answer',rabbah,ask,'answer','2b:3');e('yosef_answer',yosef,ask,'answer','2b:3')
soft=c('soft','2b:4','אמר רבה כוותי דידי מסתברא מה דרכו של חורש לרפויי ארעא האי נמי מרפויי ארעא','Rabbah reasons that the activity loosens the earth as plowing does.','רבה')
growth=c('growth','2b:4','אמר רב יוסף כוותי דידי מסתברא מה דרכו של זורע לצמוחי פירא הכא נמי מצמח פירא','Rav Yosef reasons that the activity promotes produce growth as sowing does.','רב יוסף')
e('soft_support',soft,rabbah,'support','2b:4');e('growth_support',growth,yosef,'support','2b:4')
qa=q('abaye_rabbah','2b:5','לדידך קשיא משום חורש אין משום זורע לא','Abaye asks why Rabbah would impose the plowing category but not sowing.','אביי')
qb=q('abaye_yosef','2b:5','לרב יוסף קשיא משום זורע אין משום חורש לא','Abaye asks why Rav Yosef would impose sowing but not plowing.','אביי')
e('abaye_rabbah_objection',qa,rabbah,'objection','2b:5');e('abaye_yosef_objection',qb,yosef,'objection','2b:5')
one=c('one','2b:6','וכי תימא כל היכא דאיכא תרתי לא מיחייב אלא חדא','A proposed defense would allow only one liability where two classifications apply.',mode='rejected')
two=c('two','2b:6','והאמר רב כהנא זומר וצריך לעצים חייב שתים אחת משום נוטע ואחת משום קוצר','Rav Kahana states that pruning while needing the wood incurs two liabilities, planting and harvesting.','רב כהנא',conditions=['pruning','needs the wood'],role='quoted_authority',composition='composite')
e('two_objection',two,one,'objection','2b:6')
hard=c('hard','2b:7','קשיא','The double-liability difficulty is left standing.',mode='unresolved',scope='Local unresolved objection; neither original speaker is silently retracted')
e('hard_rabbah',hard,rabbah,'objection','2b:7');e('hard_yosef',hard,yosef,'objection','2b:7')
kil=c('kil','2b:8','המנכש והמחפה לכלאים לוקה','The cited teaching imposes lashes for weeding or covering in a mixed-species setting.',role='quoted_authority',conditions=['mixed-species setting'])
ak=c('akiva','2b:8','רבי עקיבא אומר אף המקיים','Rabbi Akiva adds one who maintains the mixed species.','רבי עקיבא',role='quoted_authority',conditions=['maintenance of mixed species'])
kilq=q('kilquestion','2b:9','אלא לדידך דאמרת משום חורש חרישה בכלאים מי אסירא','Rav Yosef objects that the mixed-species prohibition fits sowing, but how does it fit Rabbah’s plowing classification?','רב יוסף')
e('kil_challenge',kilq,rabbah,'objection','2b:9');e('kil_evidence',kil,kilq,'support','2b:8')
maint=c('maint','2b:10','אמר ליה משום מקיים','Rabbah answers that the mixed-species liability is for maintaining it.','רבה',conditions=['the cited mixed-species teaching'],uncertainty=['Speaker recovered from the explicit Rav Yosef-to-Rabbah exchange, not named in this answer segment.'])
e('maint_answer',maint,kilq,'answer','2b:10')
suffix=q('suffix','2b:11','והא מדקתני סיפא ר"ע אומר אף המקיים מכלל דתנא קמא לאו משום מקיים הוא','Does Rabbi Akiva’s appended maintenance clause not imply the first tanna uses a different basis?')
e('suffix_objection',suffix,maint,'objection','2b:11')
whole=c('whole','2b:12','כולה ר\' עקיבא היא ומאי טעם קאמר מאי טעם המנכש והמחפה בכלאים לוקה משום מקיים שר"ע אומר אף המקיים','The reply reads the whole teaching as Rabbi Akiva: the maintenance clause explains why weeding and covering incur lashes.',mode='reconciled',composition='composite',scope='Anonymous reinterpretation of this cited teaching, not deletion of its initial contrasting presentation')
e('whole_answer',whole,suffix,'answer','2b:12');e('whole_support',whole,maint,'support','2b:12')
akq=q('akwhy','2b:13','מאי טעמא דר\' עקיבא','What is Rabbi Akiva’s basis?')
proofq=q('proofwhy','2b:13','אין לי אלא זורע מקיים מניין','The cited derivation asks how maintenance is included beyond the explicitly stated sowing.')
proof=c('proof','2b:14','תלמוד לומר כלאים שדך לא','The cited derivation rereads the verse’s words as כלאים שדך לא to include maintenance.',scope='Scriptural derivation in the cited teaching; do not treat its book as a named human holder')
e('proof_answer',proof,proofq,'answer','2b:14');e('akwhy_answer',proof,akq,'answer','2b:14')
mish=c('mish','2b:15','תנן משקין בית השלחין במועד ובשביעית','The Mishnah permits irrigating a dependent field during the festival and sabbatical year.',conditions=['בית השלחין'],composition='composite',scope='Quoted opening Mishnah, retained again as argument evidence')
festival=c('festival','2b:16','בשלמא מועד משום טירחא הוא ובמקום פסידא שרו רבנן','The question accepts that festival restrictions concern effort and that the sages permit work to avoid loss.',conditions=['festival','loss prevention'])
shevq=q('shevquestion','2b:16','אלא שביעית בין למאן דאמר משום זורע ובין למאן דאמר משום חורש זריעה וחרישה בשביעית מי שרי','How can irrigation be permitted in the sabbatical year under either the sowing or plowing classification?')
e('shev_objection',shevq,mish,'objection','2b:16')
ab=c('abaye','2b:17','אמר אביי בשביעית בזמן הזה ורבי היא','Abaye explains the permission as present-era sabbatical observance following Rabbi.','אביי',conditions=['sabbatical year in the era under discussion','Rabbi’s view'])
rabbi=c('rabbi','2b:17','דתניא רבי אומר (דברים טו, ב) וזה דבר השמטה שמוט בשתי שמיטות הכתוב מדבר אחת שמיטת קרקע ואחת שמיטת כספים','Rabbi interprets the verse as speaking of land release and monetary release.','רבי',role='quoted_authority',composition='composite')
dep=c('release_dependence','2b:18','בזמן שאתה משמט קרקע אתה משמט כספים ובזמן שאי אתה משמט קרקע אי אתה משמט כספים','In Rabbi’s cited teaching, monetary release applies when land release applies and does not apply when land release does not.','רבי',role='quoted_authority',composition='composite',scope='Continuation of Rabbi’s quotation; categories retained without importing a later practical ruling')
e('abaye_answer',ab,shevq,'answer','2b:17');e('rabbi_support',rabbi,ab,'support','2b:17');e('dependence_support',dep,ab,'support','2b:18')
ra=c('rava','2b:19','רבא אמר אפילו תימא רבנן אבות אסר רחמנא','Rava says the explanation can follow the sages: the Torah prohibited principal labor categories.','רבא')
der=c('derivatives','3a:1','תולדות לא אסר רחמנא','Rava’s explanation continues that derivatives were not prohibited by the Torah, subsequently qualified by the explicitly named derivatives.','רבא',scope='Rava’s cross-page continuation; qualified at3a:2–3, with rabbinic restrictions retained at3a:9')
e('rava_answer',ra,shevq,'answer','2b:19');e('der_rava',der,ra,'qualification','3a:1')
specified=q('specified','3a:2','מכדי זמירה בכלל זריעה ובצירה בכלל קצירה למאי הלכתא כתבינהו רחמנא','Why name pruning and grape harvesting separately when included in sowing and harvesting?')
only=c('only','3a:3','למימרא דאהני תולדות מיחייב אאחרנייתא לא מיחייב','The explicit naming limits liability to these specified derivatives rather than other derivatives.',scope='Explanation of Torah liability in this argument; does not deny rabbinic restrictions')
e('only_answer',only,specified,'answer','3a:3');e('only_qualifies',only,der,'qualification','3a:3')
barq=q('baraita','3a:4','ולא והתניא','Does the following teaching not contradict the exclusion of other derivatives?')
e('baraita_objection',barq,der,'objection','3a:4')
bar=c('fieldworks','3a:4','מנין לניכוש ולעידור ולכיסוח ת"ל שדך לא כרמך לא לא כל מלאכה שבשדך ולא כל מלאכה שבכרמך','The teaching derives restrictions on ניכוש, עידור and כיסוח from the field/vineyard wording.',composition='composite',scope='Quoted teaching; later classified as rabbinic with scriptural support at3a:9')
b5=c('treeworks','3a:5','מנין שאין מקרסמין ואין מזרדין ואין מפסגין באילן ת"ל שדך לא כרמך לא לא כל מלאכה שבשדך ולא כל מלאכה שבכרמך','The teaching similarly restricts מקרסמין, מזרדין and מפסגין in a tree.',composition='composite',scope='Technical source terms retained; later rabbinic classification at3a:9')
b6=c('treecare','3a:6','מנין שאין מזבלין ואין מפרקין ואין מאבקין ואין מעשנין באילן ת"ל שדך לא כרמך לא כל מלאכה שבשדך לא וכל מלאכה שבכרמך לא','The teaching similarly restricts מזבלין, מפרקין, מאבקין and מעשנין in a tree.',composition='composite',scope='Technical source terms retained; later rabbinic classification at3a:9')
for key,ref,quote,text,target in [
    ('field_derivation','3a:4','מנין לניכוש ולעידור ולכיסוח','What is the source for restrictions on ניכוש, עידור and כיסוח?',bar),
    ('tree_derivation','3a:5','מנין שאין מקרסמין ואין מזרדין ואין מפסגין באילן','What is the source for restricting מקרסמין, מזרדין and מפסגין in a tree?',b5),
    ('care_derivation','3a:6','מנין שאין מזבלין ואין מפרקין ואין מאבקין ואין מעשנין באילן','What is the source for restricting מזבלין, מפרקין, מאבקין and מעשנין in a tree?',b6)]:
    question=q(key,ref,quote,text,composition='composite');e(key+'_answer',target,question,'answer',ref)
for i,target in enumerate([bar,b5,b6]):e('bar_support'+str(i),target,barq,'support',['3a:4','3a:5','3a:6'][i])
exclude=q('exclude','3a:7','יכול לא יקשקש תחת הזיתים ולא יעדר תחת הגפנים ולא ימלא נקעים מים ולא יעשה עוגיות לגפנים','Could the restriction also prohibit קשקוש beneath olives, digging beneath vines, filling hollows with water, and making vine basins?',composition='composite')
analogy=c('analogy','3a:8','זריעה בכלל היתה ולמה יצתה להקיש אליה לומר לך מה זריעה מיוחדת עבודה שבשדה ושבכרם אף כל שהיא עבודה שבשדה ושבכרם','The teaching uses sowing as the model for the class of field/vineyard work, distinguishing the proposed exclusions.',composition='composite',scope='Quoted derivation’s own formulation; detailed technical meanings not invented')
e('analogy_answer',analogy,exclude,'answer','3a:8')
rabbinic=c('rabbinic','3a:9','מדרבנן וקרא אסמכתא בעלמא','The reply classifies these additional restrictions as rabbinic and the verse as an asmachta.',mode='reconciled',scope='Resolution of the cited baraita objection; no reclassification of the expressly stated Torah prohibitions')
e('rabbinic_answer',rabbinic,barq,'answer','3a:9')
for i,target in enumerate([bar,b5,b6]):e('rabbinic_qualifies'+str(i),rabbinic,target,'qualification','3a:9')
kq=q('kashkush','3a:10','וקשקוש בשביעית מי שרי','Is קשקוש in the sabbatical year permitted?')
ban=c('ban','3a:10','תשמטנה מלקשקש ונטשתה מלסקל','A cited verse exposition reads תשמטנה as refraining from קשקוש and ונטשתה as refraining from stone removal.',composition='composite',scope='Quoted challenge; קשקוש distinguished in the next answer')
e('ban_support',ban,kq,'support','3a:10')
dist=c('distinction','3a:11','אמר רב עוקבא בר חמא תרי קשקושי הוו חד אברויי אילני וחד סתומי פילי','Rav Ukva bar Hama distinguishes two kinds of קשקוש: improving trees and closing cracks.','רב עוקבא בר חמא',composition='composite')
forbid=c('forbid','3a:11','אברויי אילן אסור','Improving the tree by that activity is forbidden.','רב עוקבא בר חמא',conditions=['אברויי אילן'])
permit=c('permit','3a:11','סתומי פילי שרי','Closing cracks is permitted.','רב עוקבא בר חמא',conditions=['סתומי פילי'])
e('distinction_answer',dist,kq,'answer','3a:11');e('forbid_qualifies',forbid,dist,'qualification','3a:11');e('permit_qualifies',permit,dist,'qualification','3a:11')

# Cross-segment quotation/dialogue attribution uses its actual naming context.
for key,ref in [('kilquestion','2b:8'),('maint','2b:8'),('release_dependence','2b:17'),('derivatives','2b:19')]:
    row=next(x for x in a.rows if x['id']=='mk.r004.'+key+'.a')
    row['evidence'].append(a.evidence(ref))
    row['uncertainty'].append('Attribution follows the cited continuous speech/dialogue; the naming context is included as separate evidence.')

refs=['2b:'+str(i) for i in range(3,20)]+['3a:'+str(i) for i in range(1,12)]
cov=[]
for ref in refs:
    sid=a.refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in a.rows if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Direct original-source reread with context through4a:11; retained local challenges, unresolved double liability, quoted teachings, alternative Abaye/Rava explanations and Torah/rabbinic distinctions. '+layer+' pass: '+('supported records retained.' if ids else 'no additional independent object found in this segment.')))
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.rows,coverage=cov,open_tails=[])
out=a.job/'staging'/'classification_004.json';r.immutable(out,r.encoded(p));print(out)
