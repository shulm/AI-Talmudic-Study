"""Explicit source readings 7b:13–8a:14. No automatic extraction."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r013');a.agent_id='/root/pesachim_continuation_2'
def c(k,ref,quote,text,**kw):
    cid=a.claim(k,ref,quote,text,**kw)
    for row in a.rows[-2:]:row['evidence']=[a.span(ref,quote)]
    return cid
def q(k,ref,quote,text):
    qid=a.question(k,ref,quote,text);a.rows[-1]['evidence']=[a.span(ref,quote)];return qid
def e(k,x,y,rel,ref):
    if rel=='answer':
        for row in a.rows:
            if row['id']==y and row['layer']=='questions':
                row['content']['answer_set_status']='partial';row['uncertainty']=['Only actually represented local answers; no exhaustive inventory or choice eligibility.']
    return a.e(k,x,y,rel,ref)
refs=['7b:'+str(i) for i in range(13,20)]+['8a:'+str(i) for i in range(1,15)]
a.structure('light',['7b:'+str(i) for i in range(13,20)]+['8a:'+str(i) for i in range(1,6)],'Candlelight search: scriptural associations, sunlight scope, and torch contrasts')
a.structure('places',['8a:'+str(i) for i in range(6,15)],'Search locations: height, access, storage supply and domestic use')
why=q('why','7b:13','מנא הני מילי','What is the source for searching by candlelight?')
hisda=c('hisda','7b:13','אמר רב חסדא למדנו מציאה ממציאה ומציאה מחיפוש וחיפוש מחיפוש וחיפוש מנרות ונרות מנר','Rav Hisda describes a chain of verbal associations from finding to searching to candles and a candle.',candidates=['רב חסדא'],composition='composite',scope='Source’s association chain; no new equivalence rule invented')
e('hisda.answer',hisda,why,'answer','7b:13')
find=c('find','7b:14',a.refs['7b:14']['text'],'The leaven verse’s finding-language is connected to finding and searching in the Benjamin narrative.',composition='composite',scope='Displayed link from Exodus 12:19 to Genesis 44:12')
lamps=c('lamps','7b:15',a.refs['7b:15']['text'],'Searching by candles in Zephaniah links to the candle of the human spirit searching inward chambers in Proverbs.',composition='composite',scope='Displayed scriptural associations, not named human claims',uncertainty=['Source prints parenthetical אלהים and bracketed ה׳ in the Proverbs citation; variant remains literal evidence.'])
e('find.support',find,hisda,'support','7b:14');e('lamps.support',lamps,hisda,'support','7b:15')
school=c('school','7b:16',a.refs['7b:16']['text'],'The school of Rabbi Ishmael teaches searching on the night of the fourteenth by candlelight, characterizing the cited verses as a reminder rather than proof.',candidates=['דבי רבי ישמעאל'],composition='composite',conditions=['night of the fourteenth'],scope='School teaching explicitly limits the force of the citations')
e('school.support',school,hisda,'support','7b:16')
extra=q('extra','7b:17','מאי ואומר','Why add the further citation?')
lenient=c('lenient','7b:18','וכי תימא האי בעת ההיא קולא הוא דקאמר רחמנא לא בדיקנא לה בירושלים בנהורא דאבוקה דנפיש נהורא טובא אלא בנהורא דשרגא דזוטר נהורא טפי דעון רבה משתכח ועון זוטר לא משתכח','One might read the Zephaniah candle passage as leniency: dimmer light finds large sins but misses small ones.',mode='hypothetical',scope='Possible limitation of that proof, not an assertion about actual divine searching')
proof=c('proof','7b:18','תא שמע נר ה\' נשמת אדם','The Proverbs candle verse answers that concern.',scope='Additional citation supporting searching thoroughness')
e('proof.answer',proof,extra,'answer','7b:18');e('proof.objection',proof,lenient,'objection','7b:18')
lights=c('lights','7b:19',a.refs['7b:19']['text'],'A baraita excludes sunlight, moonlight and torchlight and prescribes candlelight for searching.',composition='composite',scope='Four-light contrast; sunlight exceptions are explained below')
reason=c('reason','8a:1',a.refs['8a:1']['text'],'The baraita explains that candlelight suits searching and repeats the verses as a reminder rather than proof.',composition='composite',scope='Cross-page continuation of baraita, with repeated source occurrences preserved')
e('reason.support',reason,lights,'support','8a:1')
sunq=q('sunq','8a:2','האי אור החמה היכי דמי','What case does the sunlight exclusion describe?')
court=c('court','8a:2','אי נימא בחצר האמר רבא חצר אינה צריכה בדיקה מפני שהעורבין מצויין שם','Rava exempts a courtyard from searching because ravens frequent it, excluding that proposed application.',candidates=['רבא'],conditions=['courtyard frequented by ravens'],scope='Quoted rule in the case-identification argument')
porch=c('porch','8a:2','אלא באכסדרה האמר רבא אכסדרה לאורה נבדקת','Rava allows an exedra to be searched by its own light, excluding that application too.',candidates=['רבא'],conditions=['exedra'],scope='Quoted contrary case')
window=c('window','8a:3','לא צריכא לארובה דבחדר','The reply proposes a skylight in a room.',scope='Case proposal narrowed to side areas below')
where=q('where','8a:3','ודהיכא','Which area by the skylight?')
direct=c('direct','8a:3','אי לבהדי ארובה היינו אכסדרה','The area directly opposite the skylight would be like an exedra.',conditions=['directly opposite skylight'],scope='Rejected location for the sunlight prohibition')
sides=c('sides','8a:3','אלא לצדדין','The exclusion concerns the side areas.',conditions=['room side areas beside skylight'],scope='Final narrowed case of insufficient sunlight')
e('sides.answer',sides,sunq,'answer','8a:3');e('sides.where',sides,where,'answer','8a:3');e('sides.qualification',sides,lights,'qualification','8a:3')
torchq=q('torchq','8a:4','ואבוקה לא','Why exclude a torch?')
comparison=c('comparison','8a:4','והאמר רבא מאי דכתיב (חבקוק ג, ד) ונוגה כאור תהיה קרנים מידו לו ושם חביון עוזו למה צדיקים דומין בפני שכינה כנר בפני האבוקה','Rava expounds Habakkuk by comparing the righteous before the Divine Presence to a candle before a torch.',candidates=['רבא'],scope='Aggadic comparison offered in the torch-light argument')
havdala=c('havdala','8a:4','ואמר רבא אבוקה להבדלה מצוה מן המובחר','Rava states that a torch is preferable for havdala.',candidates=['רבא'],conditions=['havdala'],scope='Different ritual use; no automatic extension to leaven search')
e('havdala.objection',havdala,lights,'objection','8a:4');e('comparison.support',comparison,torchq,'support','8a:4')
nahman=c('nahman','8a:5','אמר רב נחמן בר יצחק זה יכול להכניסו לחורין ולסדקין וזה אינו יכול להכניסו לחורין ולסדקין','Rav Nahman bar Yitzhak distinguishes a candle’s access to holes and cracks from a torch’s inability to enter them.',candidates=['רב נחמן בר יצחק'],composition='composite',scope='First functional contrast')
zevid=c('zevid','8a:5','רב זביד אמר זה אורו לפניו וזה אורו לאחריו','Rav Zevid contrasts light in front with light behind.',candidates=['רב זביד'],composition='composite',scope='Second functional contrast; deictic source retained without extra optics claims')
pappa=c('pappa','8a:5','רב פפא אמר האי בעית והאי לא בעית','Rav Pappa contrasts fear or apprehension with its absence.',candidates=['רב פפא'],composition='composite',scope='Third functional contrast; no extra psychological explanation supplied')
ravina=c('ravina','8a:5','רבינא אמר האי משך נהורא והאי מיקטף איקטופי','Ravina contrasts extended steady light with interrupted light.',candidates=['רבינא'],composition='composite',scope='Fourth functional contrast')
for k,x in [('nahman',nahman),('zevid',zevid),('pappa',pappa),('ravina',ravina)]:e(k+'.answer',x,torchq,'answer','8a:5')
include=q('include','8a:6','כל מקום לאתויי מאי','What does every place in the Mishnah include?')
places=c('places','8a:6','לאתויי הא דתנו רבנן חורי בית העליונים והתחתונים וגג היציע וגג המגדל ורפת בקר ולולין ומתבן ואוצרות יין ואוצרות שמן אין צריכין בדיקה','The baraita exempts upper and lower wall holes, roof of the annex, roof of the tower, cattle shed, coops, straw store, wine stores and oil stores.',composition='composite',scope='Full source list preserved, later qualified for accessible holes and stores used for supplies')
e('places.answer',places,include,'answer','8a:6')
bed=c('bed','8a:6','רשב"ג אומר מטה החולקת בתוך הבית ומפסקת צריכה בדיקה','Shimon ben Gamliel requires searching a bed that divides and separates the house.',candidates=['רבי שמעון בן גמליאל'],scope='First bed teaching; height distinction reconciles apparent contradiction')
shared=c('shared','8a:7','ורמינהו חור שבין אדם לחבירו זה בודק עד מקום שידו מגעת וזה בודק עד מקום שידו מגעת והשאר מבטלו בלבו','For a shared hole each neighbor searches as far as his hand reaches and nullifies the rest mentally.',composition='composite',conditions=['hole between neighbors','reach limit'],scope='Baraita introduced as apparent contradiction')
bedno=c('bedno','8a:7',"ר' שמעון בן גמליאל אומר מטה החולקת בתוך הבית ועצים ואבנים סדורים תחתיה ומפסקת אינה צריכה בדיקה",'Shimon ben Gamliel exempts a dividing bed with wood and stones arranged underneath.',candidates=['רבי שמעון בן גמליאל'],conditions=['wood and stones arranged beneath dividing bed'],scope='Second bed teaching')
contr=q('contr','8a:8',a.refs['8a:8']['text'],'How can the contradictory hole rules and bed rules be reconciled?')
holes=c('holes','8a:9','חורין אחורין לא קשיא הא בעילאי ובתתאי והא במיצעי','The exempt holes are upper or lower, whereas the searched holes are at middle height.',composition='composite',conditions=['height of holes'],scope='Anonymous reconciliation')
height=c('height','8a:9','מטה אמטה לא קשיא הא דמידליא הא דמיתתאי','The bed rules differ between a raised and a low bed.',composition='composite',conditions=['raised versus low bed'],scope='Anonymous reconciliation; physical states retained without fabricated dimensions')
e('holes.answer',holes,contr,'answer','8a:9');e('height.answer',height,contr,'answer','8a:9');e('holes.qualification',holes,places,'qualification','8a:9');e('height.qualification',height,bed,'qualification','8a:9')
wineq=q('wineq','8a:10','ואוצרות יין אין צריך בדיקה והתניא אוצרות יין צריך בדיקה אוצרות שמן אין צריך בדיקה','How does the exemption for wine stores fit a baraita requiring their search but exempting oil stores?')
supply=c('supply','8a:10','הכא במאי עסקינן במסתפק','The required search concerns a store from which supplies are drawn.',conditions=['wine store used for supplies'],scope='Case qualification')
e('supply.answer',supply,wineq,'answer','8a:10')
oilq=q('oilq','8a:10','אי הכי שמן נמי','Why not also require searching the oil store used for supplies?')
fixed=c('fixed','8a:11',a.refs['8a:11']['text'],'Oil use for eating has a fixed amount, whereas wine consumption does not.',composition='composite',scope='Anonymous explanation of differing likelihood of returning for supplies')
e('fixed.answer',fixed,oilq,'answer','8a:11')
beer=c('beer','8a:12',a.refs['8a:12']['text'],'Rabbi Hiyya teaches that Babylonian beer stores used for supplies are treated like wine stores in the Land of Israel.',candidates=['רבי חייא'],conditions=['store used for supplies'],scope='Explicit regional analogy')
e('beer.analogy',beer,supply,'analogy','8a:12')
fish=c('fish','8a:13','אמר רב חסדא בי דגים אין צריך בדיקה','Rav Hisda exempts a fish store from searching.',candidates=['רב חסדא'],scope='Rule qualified by fish size below')
fishq=q('fishq','8a:13','והתניא צריכין בדיקה','How does this fit a teaching requiring search?')
fishsize=c('fishsize','8a:13','לא קשיא הא ברברבי הא בזוטרי','The rules distinguish large fish from small fish.',composition='composite',conditions=['large versus small fish'],scope='Anonymous reconciliation; context ties exemption to large and requirement to small')
e('fishsize.answer',fishsize,fishq,'answer','8a:13');e('fishsize.qualification',fishsize,fish,'qualification','8a:13')
salt=c('salt','8a:14','אמר רבה בר רב הונא בי מילחי ובי קירי צריך בדיקה','Rabba bar Rav Huna requires searching salt and wax storage places.',candidates=['רבה בר רב הונא'],composition='composite',scope='Two named storage places retained')
wood=c('wood','8a:14','אמר רב פפא בי ציבי ובי תמרי צריך בדיקה','Rav Pappa requires searching wood and date storage places.',candidates=['רב פפא'],composition='composite',scope='Two additional named storage places retained')
a.save_window(refs,'pesachim_searchscope_013.json','Read original through 9a:11, reread this scope for every list member, repeated citation, stated proof limitation, lighting distinction and storage condition. Risks and narrative material continue next batch.',expected_parent='d4f6f92c9c9da9f91cdada7903b3c70df900851734610b015e96398ee464018c')
