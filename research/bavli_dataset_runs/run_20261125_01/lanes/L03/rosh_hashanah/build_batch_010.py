"""Explicit source-read annotations: Nisan month numbering and related annual boundaries."""
from pathlib import Path
helper=Path(__file__).with_name('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_010.json').replace('rh.e3.b005.','rh.e3.b010.'),str(__file__),'exec'))
refs=['7a:'+str(i) for i in range(3,22)]+['7b:'+str(i) for i in range(1,7)]
for key,rr,title in [('s1',refs[:9],'Nisan and numbered months'),('s2',refs[9:14],'Nisan terminates intercalation'),('s3',refs[14:21],'New shekel appropriation and public offerings'),('s4',refs[21:],'House rental year')]:
 add(key,'structure',rr[0],dict(title=title,primary=True,boundary='closed',legacy_ids=[]));p['records'][-1]['evidence']=[ev(r) for r in rr]
voices=[('7a:3','anonymous baraita and unnamed alternative','Three Nisan boundaries and rental addition'),('7a:4','anonymous Gemara','Month-number source question and spring interpretation'),('7a:5','anonymous Gemara','Iyyar/Adar alternatives; majority-spring premise challenged'),('7a:6','רב חסדא','Alternative harvest-season derivation'),('7a:7','anonymous Gemara','Marheshvan/Elul alternatives and majority-harvest objection'),('7a:8','רבינא; רבה בר עולא','Named-month derivations'),('7a:9','רב כהנא; רב אחא בר יעקב; רב אשי; anonymous alternative','Four named-month proofs'),('7a:10','anonymous Gemara','Why other derivations omit direct Nisan verse'),('7a:11','anonymous Gemara','Mishnah omission explained'),('7a:12','anonymous Gemara citing baraita','Intercalation contradiction with timing restrictions'),('7a:13','רב נחמן בר יצחק quoting Mishnah','Cessation reading and whole-Adar testimony'),('7a:14','anonymous Gemara quoting teaching','Reason for Purim cutoff'),('7a:15','anonymous opposing explanation','Public understands intercalation calculations'),('7a:16','anonymous Gemara','Mishnah omission explained'),('7a:17','רבי יאשיה','New appropriation derivation'),('7a:18','anonymous Gemara','Tishrei alternative and lexical-context reply'),('7a:19','רב יהודה reporting שמואל','Preferred new funds and valid old-fund fallback'),('7a:20','anonymous supporting baraita','Repeated funding rules and individual donation'),('7a:21','anonymous Gemara','Obviousness and incomplete-dedication concern continuing across folio'),('7b:1','anonymous Gemara','Concern rejected'),('7b:2','anonymous Gemara','Nonabsolute boundary explains Mishnah omission'),('7b:3','anonymous baraita','Year versus this-year rental terms'),('7b:4','anonymous Gemara','Thirty-day practical minimum'),('7b:5','anonymous Gemara','Tishrei alternative rejected by rainy-season use'),('7b:6','anonymous explanation of first tanna and Mishnah','Nisan weather undermines absolute rental cutoff')]
for r,v,d in voices:add('u.'+r,'utterances',r,dict(textual_voice=v,discourse_role=d,composition='composite'))
for key,text,quote in [('months','Nisan 1 begins the month-numbering year.','באחד בניסן ראש השנה לחדשים'),('intercalation','Nisan 1 is the stated boundary for intercalation.','ולעיבורין'),('shekels','Nisan 1 is the boundary for the shekel appropriation.','ולתרומת שקלים')]:c(key,'7a:3',text,quote,holder='anonymous baraita',status='Lemma interpreted in following discussion')
c('rent','7a:3','An unnamed alternative also includes house rentals in the Nisan boundary.','וי"א אף לשכירות בתים',holder='unnamed alternative in baraita')
a('a.rent','7a:3','יש אומרים','anonymous','Rental addition','וי"א',candidates=[])
q('q.month','7a:4','What establishes Nisan as first of the months?','לחדשים מנלן')
c('month.first','7a:4','The Exodus passage calls the month of the Paschal lamb the first month.','החדש הזה לכם ראש חדשים ראשון הוא לכם לחדשי השנה',holder='Exodus as quoted')
c('month.spring','7a:4','The initial argument identifies the month with spring crops as Nisan and therefore first.','איזהו חדש שיש בו אביב הוי אומר זה ניסן וקרי ליה ראשון',status='Initial seasonal proof challenged in next segment')
e('e.month','7a:4',claims['month.spring'],questions['q.month'],'answer')
q('q.iyyar','7a:5','Could the first month instead be Iyyar?','ואימא אייר')
c('iyyar.no','7a:5','Iyyar fails the requirement of spring crops.','בעינא אביב וליכא')
q('q.adar','7a:5','Could it instead be Adar?','ואימא אדר')
c('adar.no','7a:5','The proposed reply requires the majority of spring crops, which Adar lacks.','בעינא רוב אביב וליכא',mode='challenged',status='Majority requirement is not stated by verse')
q('q.majority','7a:5','Does the verse say a majority of spring crops?','מידי רוב אביב כתיב')
e('e.iyyar','7a:5',claims['iyyar.no'],questions['q.iyyar'],'answer');e('e.adar','7a:5',claims['adar.no'],questions['q.adar'],'answer');e('e.majority','7a:5',questions['q.majority'],claims['adar.no'],'objection')
c('harvest','7a:6','Rav Hisda identifies Tishrei by ingathering and its designation as seventh, establishing Nisan as first.',holder='רב חסדא',status='Alternative seasonal proof challenged next')
a('a.hisda','7a:6','רב חסדא','speaker','Ingathering derivation','אמר רב חסדא')
e('e.harvest','7a:6',claims['harvest'],questions['q.month'],'answer')
q('q.heshvan','7a:7','Could Marheshvan be seventh, making Iyyar first?','ואימא מרחשון ומאי שביעי שביעי לאייר')
c('heshvan.no','7a:7','Marheshvan lacks the required ingathering.','בעינא אסיף וליכא')
q('q.elul','7a:7','Could Elul be seventh, making Adar first?','ואימא אלול ומאי שביעי שביעי לאדר')
c('elul.no','7a:7','The proposed reply requires majority ingathering, which Elul lacks.','בעינא רוב אסיף וליכא',mode='challenged',status='Majority requirement challenged as unstated')
q('q.majority2','7a:7','Does the verse say majority ingathering?','מידי רוב אסיף כתיב')
e('e.heshvan','7a:7',claims['heshvan.no'],questions['q.heshvan'],'answer');e('e.elul','7a:7',claims['elul.no'],questions['q.elul'],'answer');e('e.majority2','7a:7',questions['q.majority2'],claims['elul.no'],'objection')
c('ravina.method','7a:8','Ravina says this was not learned from the Torah of Moses but from the received scriptural writings.','דבר זה מתורת משה רבינו לא למדנו מדברי קבלה למדנו',holder='רבינא')
derivations=[('shevat','7a:8','רבינא','Shevat is named the eleventh month.','ביום עשרים וארבעה לעשתי עשר חדש הוא חדש שבט'),('tevet','7a:8','רבה בר עולא','Tevet is named the tenth month.','ותלקח אסתר אל המלך אחשורוש אל בית מלכותו בחדש העשירי הוא חדש טבת'),('kislev','7a:9','רב כהנא','Kislev is named the ninth month.','בארבעה לחדש התשיעי בכסלו'),('sivan','7a:9','רב אחא בר יעקב','Sivan is named the third month.','ויקראו סופרי המלך בעת ההיא בחדש השלישי הוא חדש סיון'),('adar','7a:9','רב אשי','Adar is named the twelfth month.','הפיל פור הוא הגורל לפני המן מיום ליום ומחדש לחדש שנים עשר הוא חדש אדר'),('nisan','7a:9','anonymous alternative','Nisan is named the first month.','בחדש הראשון הוא חדש ניסן')]
for k,r,who,text,quote in derivations:
 c('proof.'+k,r,text,quote,holder=who,status='Alternative named-month proof for Nisan first; not contrary calendar rulings');e('e.proof.'+k,r,claims['proof.'+k],questions['q.month'],'answer',quote)
for k,r,name,quote in [('ravina','7a:8','רבינא','אמר רבינא'),('rbu','7a:8','רבה בר עולא','רבה בר עולא אמר'),('kahana','7a:9','רב כהנא','רב כהנא אמר'),('aha','7a:9','רב אחא בר יעקב','רב אחא בר יעקב אמר'),('ashi','7a:9','רב אשי','רב אשי אמר')]:a('a.'+k,r,name,'speaker','Named-month derivation in own clause',quote)
q('q.direct','7a:10','Why do the other sages not use this direct first-Nisan verse?','וכולהו מאי טעמא לא אמרי מהאי')
c('direct.caution','7a:10','Perhaps “first” means first in the narrated matter, not first in the calendar.','דלמא מאי ראשון ראשון למילתיה',mode='hypothetical',status='Explains why others prefer different proof texts')
e('e.direct','7a:10',claims['direct.caution'],questions['q.direct'],'answer')
c('omit.month','7a:11','Our Mishnah concerns years rather than months.')
q('q.inter','7a:12','Does intercalation really begin with Nisan?','לעיבורין מניסן מנינן')
c('inter.before','7a:12','One may not intercalate before New Year; an attempted intercalation then is invalid.','אין מעברין השנה לפני ר"ה ואם עיברוה אינה מעוברת',holder='quoted baraita',conditions=['Before New Year'])
c('inter.pressure','7a:12','Under pressure one may intercalate immediately after New Year.','אבל מפני הדחק מעברין אותה אחר ר"ה מיד',holder='quoted baraita',conditions=['Pressing circumstances','After New Year'])
c('inter.adar','7a:12','Even then only Adar is intercalated.','ואעפ"כ אין מעברין אלא אדר',holder='quoted baraita')
e('e.inter.challenge','7a:12',claims['inter.before'],questions['q.inter'],'objection')
c('inter.stop','7a:13','Rav Nahman bar Yitzhak reads the boundary as cessation of intercalation.','אמר רב נחמן בר יצחק מאי עיבורין הפסקת עיבורין',holder='רב נחמן בר יצחק')
c('inter.testimony','7a:13','The quoted Mishnah reports testimony permitting intercalation throughout Adar.','דתנן הן העידו שמעברין השנה כל אדר',holder='unnamed witnesses in quoted Mishnah')
c('inter.purim','7a:13','The former position allowed intercalation only until Purim.','שהיו אומרים עד הפורים',holder='earlier unnamed position')
a('a.nahman','7a:13','רב נחמן בר יצחק','speaker','Cessation interpretation','אמר רב נחמן בר יצחק');e('e.inter.answer','7a:13',claims['inter.stop'],questions['q.inter'],'answer');e('e.inter.support','7a:13',claims['inter.testimony'],claims['inter.stop'],'support')
q('q.purim','7a:14','Why does the earlier position stop at Purim?','מ"ט דמאן דאמר עד הפורים')
c('passover.study','7a:14','The cited teaching calls for studying Passover laws thirty days before Passover.','שואלין בהלכות הפסח קודם לפסח שלשים יום',holder='anonymous cited teaching')
c('purim.risk','7a:14','Intercalation after that teaching begins could lead people to disregard leaven restrictions.','אתי לזלזולי בחמץ',holder='anonymous explanation of Purim cutoff',status='Source-stated concern, not independent behavioral claim')
e('e.purim','7a:14',claims['purim.risk'],questions['q.purim'],'answer')
c('inter.reply','7a:15','The opposing explanation says people know intercalation depends on calculation and will suppose the sages only now completed it.',holder='opposing explanation in anonymous discussion')
e('e.inter.reply','7a:15',claims['inter.reply'],claims['purim.risk'],'answer')
c('omit.inter','7a:16','Our Mishnah concerns beginnings, not cessations.')
q('q.shekel','7a:17','What establishes the shekel-appropriation boundary?','ולתרומת שקלים: מנלן')
c('renew','7a:17','Rabbi Yoshiyah derives a requirement to renew and bring the offering from a new appropriation.','אמרה תורה חדש והבא קרבן מתרומה חדשה',holder='רבי יאשיה')
c('renew.nisan','7a:17','The shared year terminology is learned from the Nisan passage.','וגמרי שנה שנה מניסן דכתיב (שמות יב, ב) ראשון הוא לכם לחדשי השנה',holder='רבי יאשיה')
a('a.yoshiyah','7a:17','רבי יאשיה','speaker','New appropriation derivation','א"ר יאשיה');e('e.shekel','7a:17',claims['renew.nisan'],questions['q.shekel'],'answer')
q('q.tishrei','7a:18','Why not learn year terminology from the Tishrei passage?','ולגמור שנה שנה מתשרי')
c('year.months','7a:18','A year expression accompanied by months is compared with another accompanied by months, not one without months.','דנין שנה שיש עמה חדשים משנה שיש עמה חדשים ואין דנין שנה שיש עמה חדשים משנה שאין עמה חדשים')
e('e.tishrei','7a:18',claims['year.months'],questions['q.tishrei'],'answer')
for k,r,who in [('shmuel','7a:19','שמואל'),('baraita','7a:20','supporting anonymous baraita')]:
 c(k+'.new',r,'Public offerings brought on Nisan 1 should be funded from the new appropriation.','קרבנות צבור הבאין באחד בניסן מצוה להביא מן החדש',holder=who,conditions=['Public offerings on Nisan 1'])
 c(k+'.old',r,'If funded from the old appropriation, the obligation is fulfilled but the preferred command is missed.','ואם הביא מן הישן יצא אלא שחיסר מצוה',holder=who,conditions=['Brought from old appropriation'],status='Valid fallback distinct from preferred performance')
a('a.yehuda','7a:19','רב יהודה','transmitter','Public funding rule','אמר רב יהודה אמר שמואל',chain=['רב יהודה','שמואל']);a('a.shmuel','7a:19','שמואל','quoted_authority','Public funding rule','אמר שמואל',chain=['רב יהודה','שמואל'])
e('e.support.new','7a:20',claims['baraita.new'],claims['shmuel.new'],'support');e('e.support.old','7a:20',claims['baraita.old'],claims['shmuel.old'],'support')
c('donation','7a:20','An individual’s donated offerings are valid provided he transfers them to the public.','ויחיד שהתנדב משלו כשרין בלבד שימסרם לצבור',holder='supporting anonymous baraita',conditions=['Transferred to public'])
q('q.obvious','7a:21','Is the validity of such a donation not obvious?','פשיטא')
c('donation.concern','7a:21','One might be concerned that the donor will not transfer ownership fully to the public.','מהו דתימא ליחוש שמא',mode='rejected',status='Concern completed and rejected at 7b:1')
p['records'][-2]['evidence'].append(ev('7b:1'));p['records'][-1]['evidence'].append(ev('7b:1'))
c('donation.reply','7b:1','The teaching declines to invalidate the gift because of the proposed concern about incomplete transfer.',status='Does not dispense with the actual transfer condition')
e('e.donation','7b:1',claims['donation.reply'],claims['donation.concern'],'correction')
c('omit.shekel','7b:2','Our Mishnah omits this boundary because old funds still fulfill the obligation, so it is not absolute.')
c('rental.year','7b:3','Renting a house for a year means twelve months counted from day to day.','המשכיר בית לחבירו לשנה מונה שנים עשר חודש מיום ליום',holder='anonymous baraita',conditions=['Lease says for a year'])
c('rental.this','7b:3','If the lease says this year, starting even on Adar 1, the arrival of Nisan 1 completes that rental year.','ואם אמר לשנה זו אפילו לא עמד אלא באחד באדר כיון שהגיע יום אחד בניסן עלתה לו שנה',holder='anonymous baraita',conditions=['Lease says this year','Starts as late as Adar 1'])
c('rental.minimum','7b:4','Even for the view counting one day as a year, a house renter does not undertake the trouble for less than thirty days.',conditions=['House-rental context'],status='Distinguishes rental usage from general one-day counting')
q('q.rental','7b:5','Why not make Tishrei the rental boundary?','ואימא תשרי')
c('rental.rains','7b:5','An ordinary renter rents for the whole rainy season.','סתם כי אגר איניש ביתא לכולהו ימות הגשמים אגר')
e('e.rental','7b:5',claims['rental.rains'],questions['q.rental'],'answer')
c('rental.other','7b:6','The baraita’s first tanna and our Mishnah recognize that unsettled weather can occur in Nisan too.',holder='anonymous explanation of first tanna and Mishnah',status='Reason for not making this rental boundary absolute',uncertainty=['קיטרי retained as weather rationale without a more precise meteorological expansion.'])
e('e.rental.other','7b:6',claims['rental.other'],claims['rental.rains'],'qualification')
for r in p['records']:
 if r['layer']=='claims':r['content']['scope']='Nisan numbered months, intercalation cessation, public funding and rental year; local source reasoning only'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  rationale='Source read in overlapping 7a:1–8a:6 window; distinctions and proof alternatives preserved without inventing disputes.'
  if layer=='reconciliation':rationale='Second source-based omission check retained each seasonal challenge, named-month proof, intercalation exception, funding repeat, transfer condition and rental qualification. Full independent review remains pending.'
  elif not ids:rationale={'questions':'No explicit question in this segment after continuation reading.','attributions':'Anonymous continuation or already specified baraita voice; no additional named role.','claims':'Question-only or continuation connective; substantive claim preserved at answer.','positions':'No separate asserted holder position in this question/connective segment.','edges':'No additional explicit directed relation originating in this segment.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal_010.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(p['records']),len(refs))
