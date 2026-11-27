"""Hand-authored investigation dispute and minimum itinerant assistance rules."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r024');c=a.claim;q=a.question;e=a.e
parent='d10d149961fa28668af702db17b2d098ff687f465b32276232d5e3a4555b1877'
a.structure('investigation',['9a:6','9a:7','9a:8','9a:9'],'Rav Huna and Rav Yehuda on investigating food and clothing requests, reasons and supporting baraita')
a.structure('itinerant',['9a:10','9a:11'],'Minimum aid to a passing poor person and qualification for door-to-door solicitation')
hfood=c('huna_food','9a:6','אמר רב הונא בודקין למזונות','Rav Huna requires investigation for a food request.',candidates=['רב הונא'],conditions=['request for food assistance'])
hclothes=c('huna_clothes','9a:6','ואין בודקין לכסות','Rav Huna does not require investigation for a clothing request.',candidates=['רב הונא'],conditions=['request for clothing assistance'])
shame=c('shame','9a:7','האי קא מבזי והאי לא קא מבזי','The rational explanation prioritizes the shame of the unclothed person over the food-request case.',composition='composite',scope='Rational explanation for Rav Huna’s distinction; no external generalization about poverty')
written=c('written','9a:7','הלא פרוש לרעב לחמך בשי"ן כתיב פרוש והדר הב ליה','The scriptural explanation reads the written ש in פרוש as instructing investigation before giving bread.',scope='Source interpretation of the written form, not correction of the source spelling')
see=c('see','9a:7','כי תראה ערום וכסיתו כי תראה לאלתר','The clothing verse is read as requiring immediate covering when one sees the unclothed person.',scope='Scriptural explanation for Rav Huna’s clothing rule')
e('shame_support',shame,hclothes,'support','9a:7');e('written_support',written,hfood,'support','9a:7');e('see_support',see,hclothes,'support','9a:7')
yclothes=c('yehuda_clothes','9a:8','ורב יהודה אמר בודקין לכסות','Rav Yehuda requires investigation for clothing assistance.',candidates=['רב יהודה'],conditions=['clothing request'])
yfood=c('yehuda_food','9a:8','ואין בודקין למזונות','Rav Yehuda does not require investigation for food assistance.',candidates=['רב יהודה'],conditions=['food request'])
pain=c('pain','9a:9','האי קמצערא ליה והאי לא קמצערא ליה','The rational explanation prioritizes the suffering of hunger over the clothing-request case.',composition='composite',scope='Reason for Rav Yehuda’s contrary distinction')
read=c('read','9a:9','הלא פרוס לרעב לחמך פרוס לאלתר וכדקרינן','The scriptural explanation follows the read form פרוס and instructs immediate distribution of bread.',scope='Reading-based interpretation contrasted with the prior written-form interpretation')
check=c('check','9a:9','כי תראה ערום וכסיתו כשיראה לך','The clothing verse is read as requiring giving when the need is apparent to the assessor.',scope='Scriptural interpretation offered for investigating clothing request')
barclothes=c('baraita_clothes','9a:9','תניא כוותיה דרב יהודה אמר כסוני בודקין אחריו','A baraita supporting Rav Yehuda requires investigation of a person asking to be clothed.',conditions=['request to be clothed'],scope='Explicit source support for Rav Yehuda, not merely producer preference')
barfood=c('baraita_food','9a:9','פרנסוני אין בודקין','The same baraita requires no investigation of a request for sustenance.',conditions=['request for sustenance'])
e('clothes_contrast',yclothes,hclothes,'distinction','9a:8');e('food_contrast',yfood,hfood,'distinction','9a:8');e('pain_support',pain,yfood,'support','9a:9');e('read_support',read,yfood,'support','9a:9');e('check_support',check,yclothes,'support','9a:9');e('barclothes_support',barclothes,yclothes,'support','9a:9');e('barfood_support',barfood,yfood,'support','9a:9')
bread=c('bread','9a:10','אין פוחתין לעני העובר ממקום למקום מככר בפונדיון מארבע סאין בסלע','A passing poor person receives at least a loaf priced at a pundion when four seahs cost a sela.',conditions=['poor person passing from place to place','stated price ratio'],scope='Quoted Mishnah minimum; no modern unit conversion invented')
lodging=c('lodging','9a:10','לן נותנין לו פרנסת לינה','If he lodges overnight, he receives lodging provision.',conditions=['stays overnight'])
lodgingq=q('lodging_q','9a:10','מאי פרנסת לינה','What is lodging provision?')
bed=c('bed','9a:10','אמר רב פפא פוריא ובי סדיא','Rav Pappa identifies a bed and bedding/pillow as lodging provision.',candidates=['רב פפא'],composition='composite',uncertainty=['Printed פוריא ובי סדיא retained; material details not supplied.'])
sabbath=c('sabbath','9a:10','שבת נותנין לו מזון שלש סעודות','If he remains for Sabbath, he receives food for three meals.',conditions=['stays for Sabbath'])
beg=c('beg','9a:10','תנא אם היה מחזיר על הפתחים אין נזקקין לו','A teaching says one need not attend to someone going door to door.',conditions=['door-to-door solicitation'],scope='Initial unspecific formulation qualified in the next narrative')
e('bed_answer',bed,lodgingq,'answer','9a:10');e('bed_qualification',bed,lodging,'qualification','9a:10')
c('poor_event','9a:11','ההוא עניא דהוה מחזיר על הפתחים דאתא לקמיה דרב פפא','A poor person going door to door came to Rav Pappa.',scope='Narrative case')
refusal=c('refusal','9a:11','דאתא לקמיה דרב פפא לא מזדקיק ליה','Rav Pappa did not attend to him.',scope='Narrated initial response later challenged')
others=c('others','9a:11','א"ל רב סמא בריה דרב ייבא לרב פפא אי מר לא מזדקיק ליה אינש אחרינא לא מזדקיק ליה','Rav Sama son of Rav Yeiva warns Rav Pappa that if he does not help, others will not help either.',candidates=['רב סמא בריה דרב ייבא'],conditions=['Rav Pappa refuses assistance'])
die=q('die_q','9a:11','לימות ליה','Should he then die?',candidates=['רב סמא בריה דרב ייבא'],naming_refs=['9a:11'])
objection=c('teaching_reply','9a:11','והא תניא אם היה עני המחזיר על הפתחים אין נזקקין לו','The reply invokes the teaching that a door-to-door poor person need not be attended to.',scope='Defense of initial refusal in dialogue; no new speaker label silently supplied')
large=c('large','9a:11','אין נזקקין לו למתנה מרובה','The answer limits nonattendance to a large gift.',candidates=['רב סמא בריה דרב ייבא'],conditions=['door-to-door solicitation','large gift'],scope='Dialogue continuation resolving Rav Pappa’s citation')
small=c('small','9a:11','אבל נזקקין לו למתנה מועטת','A small gift must still be given to him.',candidates=['רב סמא בריה דרב ייבא'],conditions=['door-to-door solicitation','small gift'])
e('others_objection',others,refusal,'objection','9a:11');e('die_objection',die,refusal,'objection','9a:11');e('teaching_support',objection,refusal,'support','9a:11');e('large_qualification',large,beg,'qualification','9a:11');e('small_qualification',small,beg,'qualification','9a:11');e('small_answer',small,die,'answer','9a:11')
for row in a.rows:
    if row['layer']=='questions':
        row['content']['answer_set_status']='partial'
        row['uncertainty'].append('Source-present answer retained; neither exhaustive answer-set completeness nor task eligibility is certified.')
a.save_window(['9a:'+str(i) for i in range(6,12)],'assistance024.json','Read food/clothing dispute and itinerant/door-to-door case through9a:11 with9a:12–15 context. Preserve actual opposing rules, independent scriptural/rational supports, explicit baraita support for Rav Yehuda, conditions and small/large-gift resolution. No practical ruling beyond source status.',parent)

