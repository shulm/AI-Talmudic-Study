"""Manual source reading of rain-origin controversy, 9b:10–10a:10."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','bcf272af3eb3b73fda67c2405dd64ed8b9d456650be4e6d3ea154f9a07aae6f4').replace('ta.resume008.','ta.resume018.').replace('/root/taanit_continuation_2','/root/taanit_continuation_3')
exec(compile(helper,__file__,'exec'))
def v(k,r,t,p):
 x=c(k,r,t,p,voice='biblical quotation',comp='composite');next(z for z in P['records'] if z['id']==x+'.a')['content'].update(surface='scriptural quotation',role='quoted_authority',candidates=[]);return x
A=c('ocean','9b:10',"תניא ר' אליעזר אומר כל העולם כולו ממימי אוקיינוס הוא שותה",'Rabbi Eliezer says the entire world drinks from ocean water.',who='Rabbi Eliezer',status='source cosmological teaching, not an empirical endorsement')
Av=v('mist.verse','9b:10','שנאמר (בראשית ב, ו) ואד יעלה מן הארץ והשקה את כל פני האדמה','Genesis describes mist rising from earth and watering the ground.');e('ocean.proof','9b:10','שנאמר (בראשית ב, ו) ואד יעלה מן הארץ והשקה את כל פני האדמה',Av,A)
B=c('salt.objection','9b:10','אמר לו רבי יהושע והלא מימי אוקיינוס מלוחין הן','Rabbi Yehoshua objects that ocean water is salty.',who='Rabbi Yehoshua',status='objection');e('salt.edge','9b:10','אמר לו רבי יהושע והלא מימי אוקיינוס מלוחין הן',B,A,'objection')
Bq=q('salt.q','9b:10','והלא מימי אוקיינוס מלוחין הן','How is the ocean account consistent with its salty water?',who='Rabbi Yehoshua')
C=c('sweetened','9b:10','אמר לו ממתקין בעבים','Eliezer answers that the waters are sweetened in the clouds.',who='Rabbi Eliezer',status='reply within source cosmology');e('sweetened.answer','9b:10','אמר לו ממתקין בעבים',C,Bq,'answer');e('sweetened.reply','9b:10','אמר לו ממתקין בעבים',C,B,'local_resolution')
D=c('upper.water','9b:11',"ר' יהושע אומר כל העולם כולו ממים העליונים הוא שותה",'Rabbi Yehoshua says the world drinks from the upper waters.',who='Rabbi Yehoshua',status='alternative source cosmology');e('origin.distinction','9b:11',ix['9b:11']['text'],D,A,'distinction')
Dv=v('heaven.verse','9b:11','שנאמר (דברים יא, יא) למטר השמים תשתה מים','Deuteronomy describes drinking water from heaven’s rain.');e('upper.proof','9b:11','שנאמר (דברים יא, יא) למטר השמים תשתה מים',Dv,D)
Eq=q('mist.q','9b:11','אלא מה אני מקיים ואד יעלה מן הארץ','How does Yehoshua interpret the mist rising from earth?',who='Rabbi Yehoshua')
E=c('cloud.receive','9b:11','מלמד שהעננים מתגברים ועולים לרקיע ופותחין פיהן כנוד ומקבלין מי מטר','Yehoshua explains clouds rising to the firmament, opening like a waterskin and receiving rainwater.',who='Rabbi Yehoshua',comp='composite',status='source cosmological exposition');e('mist.answer','9b:11','מלמד שהעננים מתגברים ועולים לרקיע ופותחין פיהן כנוד ומקבלין מי מטר',E,Eq,'answer')
Ev=v('receiving.verse','9b:11','שנאמר (איוב לו, כז) יזקו מטר לאדו','Job’s יזקו מטר לאדו is quoted.');e('receiving.proof','9b:11','שנאמר (איוב לו, כז) יזקו מטר לאדו',Ev,E)
F=c('sieve.clouds','9b:12','ומנוקבות הן ככברה ובאות ומחשרות מים על גבי קרקע','The continuing exposition describes clouds perforated like a sieve, discharging water onto the ground.',who='Rabbi Yehoshua',comp='composite',unc=['Inherited speaker from preceding baraita; source does not print a new name.'])
Fv=v('sieve.verse','9b:12','שנאמר (שמואל ב כב, יב) חשרת מים עבי שחקים','The proof quotes חשרת מים עבי שחקים.');e('sieve.proof','9b:12','שנאמר (שמואל ב כב, יב) חשרת מים עבי שחקים',Fv,F)
G=c('drop.spacing','9b:12','ואין בין טיפה לטיפה אלא כמלא נימא','The exposition gives a hairbreadth between one drop and another.',who='Rabbi Yehoshua',status='source cosmological image')
H=c('creation.greatness','9b:12','ללמדך שגדול יום הגשמים כיום שנבראו בו שמים וארץ','The exposition teaches that a rainy day is as great as the day heaven and earth were created.',who='Rabbi Yehoshua',comp='composite',status='homiletic comparison',unc=['Continuation of quoted exposition; no independent new named attribution.'])
Hv=v('creation.verses','9b:13',ix['9b:13']['text'],'The scriptural chain links unsearchable great deeds and rain with the eternal God’s unsearchable understanding, adding the parenthetical mountain-establishment citation.');e('creation.proof','9b:13',ix['9b:13']['text'],Hv,H)
Iq=q('upper.rooms.q','9b:14','כמאן אזלא הא דכתיב','Which view accords with the verse and Yohanan’s explanation about watering from upper chambers?')
Iv=v('rooms.verse','9b:14','(תהלים קד, יג) משקה הרים מעליותיו','The psalm describes watering mountains from upper chambers.')
I=c('rooms.yohanan','9b:14','וא"ר יוחנן מעליותיו של הקב"ה','Rabbi Yohanan identifies the chambers as God’s.',who='Rabbi Yohanan')
J=c('rooms.alignment','9b:14','כמאן כרבי יהושע','The discussion aligns this explanation with Rabbi Yehoshua.');e('rooms.answer','9b:14',ix['9b:14']['text'],J,Iq,'answer');e('rooms.support','9b:14',ix['9b:14']['text'],I,D)
K=c('eliezer.rooms','9b:15',"ור' אליעזר כיון דסלקי להתם משקה מעליותיו קרי להו",'For Rabbi Eliezer, the waters are called from upper chambers because they first rise there.',voice='anonymous explanation of Rabbi Eliezer',status='reconciliation with rival proof')
Kq=q('dust.q','9b:15','דאי לא תימא הכי (דברים כח, כד) אבק ועפר מן השמים היכי משכחת לה','Otherwise how could dust and earth come from heaven?')
L=c('dust.analogy','9b:15','אלא כיון דמדלי להתם מן השמים קרי ליה','Dust is called from heaven because it was lifted there.');e('dust.answer','9b:15','אלא כיון דמדלי להתם מן השמים קרי ליה',L,Kq,'answer')
L1=c('water.analogy','9b:15','הכא נמי כיון דסלקי להתם מעליותיו קרי ליה','Likewise, waters are called from upper chambers because they rose there.');e('water.analogy.edge','9b:15',ix['9b:15']['text'],L,L1,'analogy');e('rooms.reply','9b:15',ix['9b:15']['text'],K,J,'qualification')
Mq=q('depths.q','9b:16','כמאן אזלא [הא] דא"ר חנינא','With which view does Rabbi Hanina’s exposition accord?')
Mv=v('depths.verse','9b:16','(תהלים לג, ז) כונס כנד מי הים נותן באוצרות תהומות','The psalm describes gathering sea waters and placing depths in storehouses.')
Mqq=q('storehouses.q','9b:16','מי גרם לאוצרות שיתמלאו בר','What causes storehouses to fill with grain?',who='Rabbi Hanina')
M=c('depths.grain','9b:16','תהומות','Rabbi Hanina answers: the depths.',who='Rabbi Hanina');e('storehouses.answer','9b:16',ix['9b:16']['text'],M,Mqq,'answer')
N=c('depths.alignment','9b:16','כרבי אליעזר','The discussion aligns this exposition with Rabbi Eliezer.');e('depths.answer','9b:16',ix['9b:16']['text'],N,Mq,'answer');e('depths.support','9b:16',ix['9b:16']['text'],M,A)
O=c('creation.only','10a:1','בברייתו של עולם','For Rabbi Yehoshua the verse refers to the creation of the world.',voice='anonymous explanation of Rabbi Yehoshua',status='alternative interpretation of the depths verse');next(z for z in P['records'] if z['id']==O)['evidence'].insert(0,ev('9b:16',"ור' יהושע ההוא"));e('depths.qualification','10a:1','בברייתו של עולם',O,N,'qualification')
P1=c('israel.first','10a:2','ת"ר א"י נבראת תחילה וכל העולם כולו נברא לבסוף','A baraita says the land of Israel was created first and the rest of the world afterward.',voice='anonymous baraita',comp='composite',status='source cosmological distinction')
P1v=v('land.outside','10a:2','שנאמר (משלי ח, כו) עד לא עשה ארץ וחוצות','Proverbs pairs land and outside places.');e('creation.order.proof','10a:2','שנאמר (משלי ח, כו) עד לא עשה ארץ וחוצות',P1v,P1)
P2=c('direct.watering','10a:2','א"י משקה אותה הקב"ה בעצמו וכל העולם כולו ע"י שליח','God waters Israel directly, while the rest of the world is watered through a messenger.',voice='anonymous baraita',comp='composite')
P2v=v('giving.sending','10a:2','שנאמר (איוב ה, י) הנותן מטר על פני ארץ ושולח מים על פני חוצות','Job distinguishes giving rain over land from sending water over outside places.');e('watering.agency.proof','10a:2','שנאמר (איוב ה, י) הנותן מטר על פני ארץ ושולח מים על פני חוצות',P2v,P2)
Q=c('rain.residue','10a:3','א"י שותה מי גשמים וכל העולם כולו מתמצית','Israel drinks rainwater and the rest of the world drinks its residue.',voice='anonymous baraita',comp='composite')
Qv=v('rain.residue.verse','10a:3',"שנאמר הנותן מטר על פני ארץ וגו'",'The baraita again cites giving rain over land.');e('rain.residue.proof','10a:3',"שנאמר הנותן מטר על פני ארץ וגו'",Qv,Q)
R=c('drinks.first','10a:3','א"י שותה תחילה וכל העולם כולו לבסוף','Israel drinks first and the rest of the world afterward.',voice='anonymous baraita',comp='composite')
# The second identical printed citation remains a second occurrence with its own character offsets.
rquote="שנאמר הנותן מטר על פני ארץ וגו'";start=ix['10a:3']['text'].rindex(rquote)
Rv=v('order.verse','10a:3',rquote,'The repeated proof again cites giving rain over land.')
for z in P['records']:
 if z['id'].startswith(Rv):z['evidence']=[dict(segment_id=ix['10a:3']['id'],start_char=start,end_char=start+len(rquote),quote=rquote)]
e('drinking.order.proof','10a:3',ix['10a:3']['text'],Rv,R)
R1=c('cheese.analogy','10a:3','משל לאדם שמגבל את הגבינה נוטל את האוכל ומניח את הפסולת','The baraita likens this to making cheese, taking the food and leaving the refuse.',voice='anonymous baraita',comp='composite');e('cheese.comparison','10a:3',ix['10a:3']['text'],R1,Q,'analogy')
Sq=q('sweetening.q','10a:4','אמר מר ממתקין הן בעבים מנליה','What is the source for the stated sweetening in clouds?')
S=c('two.spellings','10a:4','דא"ר יצחק בר יוסף א"ר יוחנן כתיב (תהלים יח, יב) חשכת מים עבי שחקים וכתיב (שמואל ב כב, יב) חשרת מים עבי שחקים','Rabbi Yohanan, transmitted by Rabbi Yitzhak bar Yosef, compares the spellings חשכת and חשרת in the two verses.',who='Rabbi Yohanan',chain=['Rabbi Yitzhak bar Yosef','Rabbi Yohanan'],comp='composite')
T=c('combined.word','10a:5','שקול כף ושדי אריש וקרי ביה חכשרת','The exposition transfers the kaf to the resh and reads חכשרת.',voice='continuing letter exposition',unc=['Printed חכשרת retained exactly; no emendation supplied.']);e('sweetening.answer','10a:5',ix['10a:5']['text'],T,Sq,'answer');e('sweetening.proof','10a:5',ix['10a:5']['text'],T,C);e('spellings.support','10a:4',ix['10a:4']['text'],S,T)
Uq=q('yehoshua.spellings.q','10a:6',"ור' יהושע בהני קראי מאי דריש בהו",'How does Rabbi Yehoshua interpret these verses?')
U=c('light.clouds','10a:6','נהור ענני זעירין מוהי','The western saying reports that bright clouds have little water.',voice='western collective teaching',chain=['Rav Dimi','unnamed western teachers'],cond=['clouds bright'])
U1=c('dark.clouds','10a:6','חשוך ענני סגיין מוהי','Dark clouds have much water.',voice='western collective teaching',chain=['Rav Dimi','unnamed western teachers'],cond=['clouds dark'])
for cid in [U,U1]:
 for z in P['records']:
  if z['id']==cid+'.a':z['content'].update(surface='אמרי במערבא',role='collective');z['evidence']=[ev('10a:6')]
U2=c('yehoshua.weather','10a:6','סבר לה כי הא דכי אתא רב דימי אמר אמרי במערבא','The discussion explains Yehoshua’s view through the western saying brought by Rav Dimi.',voice='anonymous alignment',status='explanatory alignment, not direct reported quotation by Yehoshua');e('yehoshua.spellings.answer','10a:6',ix['10a:6']['text'],U2,Uq,'answer');e('weather.support','10a:6',ix['10a:6']['text'],U,U2);e('weather.support2','10a:6',ix['10a:6']['text'],U1,U2)
Vq=q('upper.fruit.q','10a:7','כמאן אזלא הא דתניא','Which view accords with the following upper-waters baraita?')
V=c('suspended','10a:7','מים העליונים במאמר הם תלוים ופירותיהן מי גשמים','The baraita says upper waters are suspended by divine utterance and their fruits are rainwater.',voice='anonymous baraita',comp='composite',status='source cosmological teaching')
Vv=v('fruit.verse','10a:7','שנאמר (תהלים קד, יג) מפרי מעשיך תשבע הארץ','The proof quotes the earth’s satisfaction from the fruit of God’s works.');e('fruit.proof','10a:7',ix['10a:7']['text'],Vv,V)
W=c('fruit.alignment','10a:7',"כמאן כר' יהושע",'The discussion aligns this with Rabbi Yehoshua.');e('fruit.answer','10a:7',"כמאן כר' יהושע",W,Vq,'answer')
X=c('eliezer.handwork','10a:7',"ור' אליעזר ההוא במעשה ידיו של הקב\"ה הוא דכתיב",'For Eliezer, the verse speaks of God’s handiwork.',voice='anonymous explanation of Rabbi Eliezer');e('handwork.qualifies','10a:7',ix['10a:7']['text'],X,W,'qualification')
Y=c('eden.residue','10a:8','אריב"ל כל העולם כולו מתמצית גן עדן הוא שותה','Rabbi Yehoshua ben Levi says the whole world drinks the residue of the Garden of Eden.',who='Rabbi Yehoshua ben Levi',status='source cosmological teaching')
Yv=v('eden.river','10a:8',"שנאמר (בראשית ב, י) ונהר יוצא מעדן וגו'",'Genesis’s river issuing from Eden is cited.');e('eden.proof','10a:8',"שנאמר (בראשית ב, י) ונהר יוצא מעדן וגו'",Yv,Y)
Z=c('kor.tarkav','10a:8','תנא מתמצית בית כור שותה תרקב:','A tanna says the residue of a beit kor waters a tarkav.',voice='anonymous tanna',status='proportional teaching; units retained without conversion')
AA=c('egypt.size','10a:9','ת"ר ארץ מצרים הויא ד\' מאות פרסה על ד\' מאות פרסה','The baraita gives Egypt’s dimensions as four hundred by four hundred parasangs.',voice='anonymous baraita',status='source geographic/cosmological magnitude, not modern measurement')
AB=c('egypt.cush','10a:9','והוא אחד מששים בכוש','Egypt is one sixtieth of Cush.',voice='anonymous baraita')
AC=c('cush.world','10a:9','וכוש אחד מששים בעולם','Cush is one sixtieth of the world.',voice='anonymous baraita')
AD=c('world.garden','10a:9','ועולם א\' מששים בגן','The world is one sixtieth of the Garden.',voice='anonymous baraita')
AE=c('garden.eden','10a:9','וגן אחד מששים לעדן','The Garden is one sixtieth of Eden.',voice='anonymous baraita')
AF=c('eden.gehenna','10a:9','ועדן אחד מס\' לגיהנם','Eden is one sixtieth of Gehenna.',voice='anonymous baraita')
AG=c('lid','10a:9','נמצא כל העולם כולו ככיסוי קדרה לגיהנם','The baraita concludes that the whole world is like a pot lid relative to Gehenna.',voice='anonymous baraita',status='source analogy');e('sizes.conclusion','10a:9',ix['10a:9']['text'],AF,AG)
AH=c('gehenna.unbounded','10a:9','וי"א גיהנם אין לה שיעור','Some say Gehenna has no measure.',voice='unnamed alternative teachers',status='alternative version')
AI=c('eden.unbounded','10a:9','וי"א עדן אין לה שיעור','Others say Eden has no measure.',voice='unnamed alternative teachers',status='alternative version');e('gehenna.alternative','10a:9',ix['10a:9']['text'],AH,AF,'qualification');e('eden.alternative','10a:9',ix['10a:9']['text'],AI,AE,'qualification')
AJq=q('babylon.verse.q','10a:10','א"ר אושעיא מאי דכתיב (ירמיהו נא, יג) שוכנת על מים רבים רבת אוצרות','Rabbi Oshaya asks the meaning of dwelling on many waters, abundant in storehouses.',who='Rabbi Oshaya')
AJq2=q('babylon.grain.q','10a:10','מי גרם לבבל שיהו אוצרותיה מליאות בר','What causes Babylonia’s storehouses to be full of grain?',who='Rabbi Oshaya')
AJ=c('many.waters','10a:10','הוי אומר מפני ששוכנת על מים רבים','Oshaya answers that it is because Babylonia dwells on many waters.',who='Rabbi Oshaya');e('waters.answer','10a:10',ix['10a:10']['text'],AJ,AJq,'answer');e('grain.answer','10a:10',ix['10a:10']['text'],AJ,AJq2,'answer')
AK=c('babylon.harvest','10a:10','אמר רב עתירה בבל דחצדא בלא מיטרא','Rav says Babylonia is wealthy because it harvests without rain.',who='Rav')
AL=c('wet.not.dry','10a:10','אמר אביי נקיטינן טובעני ולא יובשני:','Abaye gives the received maxim טובעני ולא יובשני, preferring wet conditions to dry.',who='Abaye',unc=['Compact agricultural maxim retained literally; no unprinted quantitative rule added.'])
refs=list(ix);refs=refs[refs.index('9b:10'):refs.index('10a:10')+1]
for k,title,first,last in [('origin','Ocean and upper-water rain accounts with competing scriptural interpretations','9b:10','10a:7'),('scale','Eden, proportional waters and cosmological magnitudes','10a:8','10a:9'),('babylon','Babylonia’s waters, grain and agricultural maxim','10a:10','10a:10')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'9b:10':'Eliezer ocean claim, verse, Yehoshua salinity challenge and cloud-sweetening reply retained.','9b:11':'Upper waters, verse, mist question and cloud-reception account retained.','9b:12':'Sieve account, proof, drop interval and creation comparison retained with inherited attribution qualification.','9b:13':'Full four-part scriptural proof chain including parenthetical mountain text retained.','9b:14':'Alignment question, upper-chamber verse, Yohanan interpretation and Yehoshua alignment retained.','9b:15':'Eliezer accommodation, dust-from-heaven question and ascent analogy retained.','9b:16':'Hanina question/exegesis, depths answer, Eliezer alignment and next-folio Yehoshua counterinterpretation retained.','10a:1':'Exact cross-folio creation-only interpretation retained.','10a:2':'Israel/world creation order and watering agency distinctions with separate proofs retained.','10a:3':'Rain/residue and temporal distinctions, both identical citation occurrences and cheese analogy retained.','10a:4':'Sweetening question, Yitzhak bar Yosef–Yohanan transmission and two spellings retained.','10a:5':'Exact printed combined reading retained without correction.','10a:6':'Yehoshua interpretation question, Dimi/western chain and bright/dark cloud conditions retained.','10a:7':'Upper-water baraita, proof, alignment question/answer and Eliezer alternative retained.','10a:8':'Yehoshua ben Levi Eden account, river proof and independent unit proportion retained.','10a:9':'Dimensions and every sixtieth relation retained separately; lid analogy and two unbounded alternatives retained.','10a:10':'Oshaya’s two questions and water answer, Rav’s harvest and Abaye’s lexical maxim retained.'}
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch018.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
