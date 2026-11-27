"""Manual reading of pot, oven, preserved-food and fish vow formulations."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r053.';a.OUTPUT='continuation_053.json'
c=a.c;e=a.edge;q=b.q
a.structure('pot',['51a:10','51a:11','51a:12'],'Pot versus pan and oven formulations')
a.structure('preserved',['51b:1','51b:2','51b:3'],'Definite and unqualified preserved-food formulas with unresolved prefixed forms')
a.structure('fish',['51b:'+str(i) for i in range(4,9)],'Fish sizes, processed preparations and ordinary usage')
pot=c('pot','51a:10','הנודר ממעשה קדרה אין אסור אלא ממעשה רתחתא','The repeated Mishnah limits מעשה קדרה to מעשה רתחתא.',scope='Separate repeated occurrence retained without new technical definition')
allpot=c('allpot','51a:10','אמר קונם היורד לקדרה שאני טועם אסור בכל הנעשה בקדרה','The formula היורד לקדרה prohibits all food made in a pot.',scope='Explicit broader formula')
pan=c('pan','51a:11','תניא הנודר מן היורד לקדרה אסור ביורד לאלפס שכבר ירד לקדרה קודם שיורד לאלפס','A vow against what goes into a pot includes what goes into a pan, since it previously went into a pot.',scope='Baraita’s explicit sequential-cooking rationale')
reverse=c('reverse','51a:11','מן היורד לאלפס מותר ביורד לקדרה','A vow against what goes into a pan permits what goes into a pot.',scope='Reverse direction does not imply the same inclusion')
madepot=c('madepot','51a:11','מן הנעשה בקדרה מותר בנעשה באלפס','A vow against what is made in a pot permits what is made in a pan.',scope='נעשה formula distinguished from יורד')
madepan=c('madepan','51a:11','מן הנעשה באלפס מותר בנעשה בקדרה','A vow against what is made in a pan permits what is made in a pot.',scope='Reciprocal נעשה distinction')
bread=c('bread','51a:12','הנודר מן היורד לתנור אין אסור אלא בפת','A vow against what goes into the oven prohibits only bread.',scope='Narrow ordinary usage of יורד לתנור')
oven=c('oven','51a:12','ואם אמר כל מעשה תנור עלי אסור בכל הנעשים בתנור','The formula all oven products upon me prohibits everything made in the oven.',scope='Explicit all-products broadening')
e('oven.distinction',oven,bread,'distinction','51a:12')
pickle=c('pickle','51b:1','מן הכבוש אין אסור אלא מן הכבוש של ירק','A vow against the pickled prohibits only pickled vegetables.',scope='Definite formula מן הכבוש')
pickleall=c('pickleall','51b:1','כבוש שאני טועם אסור בכל הכבושים','The formula pickled that I taste prohibits all pickled foods.',scope='Unqualified כבוש formula')
boil=c('boil','51b:1','מן השלוק אינו אסור אלא מן השלוק של בשר','A vow against the thoroughly boiled prohibits only thoroughly boiled meat.',scope='Definite formula מן השלוק')
boilall=c('boilall','51b:1','שלוק שאני טועם אסור בכל השלוקים','The formula thoroughly boiled that I taste prohibits all thoroughly boiled foods.',scope='Unqualified שלוק formula')
prefix=a.q('prefix','51b:2','אמר דכביש מאי דשליק מאי דצלי מאי דמליח מאי היכין משמע','Rav Aha son of Rav Avya asks Rav Ashi what the prefixed forms דכביש, דשליק, דצלי and דמליח imply.',voice='רב אחא בריה דרב אויא')
unresolved=c('unresolved','51b:2','תיבעי','The question of the four prefixed formulations remains unresolved.',mode='unresolved',scope='Explicit תיבעי, not an inferred prohibition or permission')
e('prefix.unresolved',unresolved,prefix,'unresolved_outcome','51b:2')
roast=c('roast','51b:3','מן הצלי אין אסור אלא מן הצלי של בשר דברי ר\' יהודה','Rabbi Yehuda limits a vow against the roasted to roasted meat.',holder="ר' יהודה",scope='Explicit named attribution of first clause')
roastall=c('roastall','51b:3','צלי שאני טועם אסור בכל הצלויים','The formula roasted that I taste prohibits all roasted foods.',scope='Following Mishnah clause; named attribution not extended beyond its explicit boundary')
salt=c('salt','51b:3','מן המליח אין אסור אלא מן המליח של דג','A vow against the salted prohibits only salted fish.',scope='Definite formula מן המליח')
saltall=c('saltall','51b:3','מליח שאני טועם אסור בכל המלוחים','The formula salted that I taste prohibits all salted foods.',scope='Unqualified מליח formula')
fish=c('fish','51b:4','דג דגים שאני טועם אסור בהן בין גדולים בין קטנים בין מלוחים בין תפלים בין חיים בין מבושלים','The printed דג דגים formula prohibits large and small fish, salted and unsalted, raw and cooked.',composition='composite',scope='All three explicit paired dimensions; printed formula not harmonized to ensuing דג דגה')
processed=c('processed','51b:4','ומותר בטרית טרופה ובציר','That fish vow permits טרית טרופה and brine.',composition='composite',scope='Two excluded processed forms')
tzahana=c('tzahana','51b:4','הנודר מן הצחנה אסור בטרית טרופה ומותר בציר ובמורייס','A vow against צחנה prohibits טרית טרופה but permits brine and muries.',composition='composite',scope='Named preserved-food category and three outcomes')
trit=c('trit','51b:4','הנודר מטרית טרופה אסור בציר ובמורייס','A vow against טרית טרופה prohibits brine and muries.',composition='composite',scope='Different origin formula changes inclusion of both liquids')
large=c('large','51b:5','תניא רבי שמעון בן אלעזר אומר דג שאני טועם אסור בגדולים ומותר בקטנים','Rabbi Shimon ben Elazar says דג prohibits large fish and permits small ones.',holder='רבי שמעון בן אלעזר',composition='composite',scope='First lexical form and two size outcomes')
small=c('small','51b:5','דגה שאני טועם אסור בקטנים ומותר בגדולים','He says דגה prohibits small fish and permits large ones.',holder='רבי שמעון בן אלעזר',composition='composite',scope='Second lexical form and two size outcomes')
both=c('both','51b:5','דג דגה שאני טועם אסור בין בגדולים בין בקטנים','He says דג דגה prohibits both large and small fish.',holder='רבי שמעון בן אלעזר',composition='composite',scope='Combined formula; printed difference from Mishnah retained')
jonahq=q('jonahq','51b:6','אמר ליה רב פפא לאביי ממאי דדג שאני טועם גדול הוא דכתיב (יונה ב, א) וימן י"י דג גדול לבלוע את יונה והכתיב (יונה ב, ב) ויתפלל יונה אל י"י אלהיו ממעי הדגה','Rav Pappa challenges Abaye: if דג means large because of Jonah’s great fish, why does Jonah also pray from the דגה?',voice='רב פפא')
possible=c('possible','51b:7','הא לא קשיא דלמא פלטיה דג גדול ובלעיה דג קטן','The first reply suggests a large fish may have expelled Jonah and a small one swallowed him.',mode='hypothetical',scope='Deflection of the Jonah objection, not asserted narrative harmonization')
nileq=q('nileq','51b:7','אלא (שמות ז, כא) והדגה אשר ביאור מתה קטנים מתו גדולים לא מתו','Does the Nile verse using דגה mean that only small fish died and large fish did not?')
usage=c('usage','51b:7','אלא דגה משמע גדולים ומשמע קטנים ובנדרים הלך אחר לשון בני אדם','The conclusion says scriptural דגה includes large and small fish, while vows follow ordinary human speech.',composition='composite',scope='Rejects scriptural size restriction without rejecting the baraita’s ordinary-usage vow distinctions')
e('possible.answer',possible,jonahq,'answer','51b:7');e('usage.answer',usage,nileq,'answer','51b:7');e('usage.qualification',usage,small,'qualification','51b:7')
tzihin=a.q('tzihin','51b:8','אמר ליה רבינא לרב אשי אמר הרי עלי ציחין מאי','Ravina asks Rav Ashi the effect of saying ציחין are upon me.',voice='רבינא')
tzun=c('tzun','51b:8','תיבעי','The ציחין wording question remains unresolved.',mode='unresolved',scope='Explicit local unresolved outcome')
e('tzihin.unresolved',tzun,tzihin,'unresolved_outcome','51b:8')
a.notes={
'51a:10':'Reread repeated Mishnah formulas and preserved distinct technical categories.',
'51a:11':'Reread all four pot/pan directional formulas and explicit prior-pot rationale; no symmetry invented.',
'51a:12':'Reread bread-only versus all oven products distinction.',
'51b:1':'Reread definite/unqualified pickle and boiled forms with all four outcomes.',
'51b:2':'Reread Aha bar Avya four prefixed forms addressed to Ashi and explicit unresolved ending.',
'51b:3':'Reread Yehuda roast-meat attribution and all remaining roast/salted formulas.',
'51b:4':'Reread printed דג דגים, all size/salt/cooking pairs, processed exclusions, tzahana and trit liquid distinctions.',
'51b:5':'Reread Shimon ben Elazar three lexical formulas and both size outcomes each; no silent correction of Mishnah wording.',
'51b:6':'Reread Pappa-to-Abaye Jonah lexical objection with both citations.',
'51b:7':'Reread hypothetical two-fish deflection, Nile objection and final scriptural breadth versus ordinary vow usage.',
'51b:8':'Reread Ravina-to-Ashi tzihin question and explicit תיבעי.'}
if __name__=='__main__':a.save()
