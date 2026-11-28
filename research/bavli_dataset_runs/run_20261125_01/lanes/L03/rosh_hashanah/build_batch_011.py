"""Source-read reconciliation of Mishnah authorities and the count of four new years."""
from pathlib import Path
helper=Path(__file__).with_name('build_batch_005.py').read_text(encoding='utf-8').split("refs=['2b:'")[0]
exec(compile(helper.replace('rh_packet_next.json','rh_packet_011.json').replace('rh.e3.b005.','rh.e3.b011.'),str(__file__),'exec'))
refs=['7b:'+str(i) for i in range(7,18)]+['8a:'+str(i) for i in range(1,4)]
add('s','structure','7b:7',dict(title='Authorities behind Mishnah clauses and interpretations of four new years',primary=True,boundary='closed',legacy_ids=[]));p['records'][-1]['evidence']=[ev(r) for r in refs]
voices=[('7b:7','anonymous Gemara citing רבי מאיר','Identification of animal-tithe clause'),('7b:8','anonymous Gemara','Mixed-authority difficulty'),('7b:9','רב יוסף','Rebbe adopts different tannaim by topic'),('7b:10','anonymous objection; רבא','Five versus four and per-authority count'),('7b:11','רב נחמן בר יצחק','Four-month count'),('7b:12','anonymous objection quoting teaching','Omer and loaves omitted'),('7b:13','רב פפא','Nightfall criterion'),('7b:14','anonymous Gemara','Festival challenge and preexisting duty'),('7b:15','anonymous Gemara quoting רבי ישמעאל בנו של רבי יוחנן בן ברוקא','Jubilee challenge and authority-specific reply'),('7b:16','רב שישא בריה דרב אידי','Act-independent criterion'),('7b:17','anonymous Gemara','Festival challenge and automatic delay prohibition'),('8a:1','anonymous Gemara','Jubilee challenge and same tannaitic view'),('8a:2','רב אשי','Four firsts of months'),('8a:3','anonymous Gemara','Beit Shammai challenge and qualified count')]
for r,v,d in voices:add('u.'+r,'utterances',r,dict(textual_voice=v,discourse_role=d,composition='composite'))
q('q1','7b:7','Whose view sets animal tithe at Elul 1?','מני')
c('c1','7b:7','The Elul animal-tithe clause follows Rabbi Meir.','רבי מאיר היא',holder='anonymous Gemara')
c('c2','7b:7','Rabbi Meir teaches Elul 1 as the animal-tithe new year.','ר"מ אומר באחד באלול ראש השנה למעשר בהמה',holder='רבי מאיר')
a('a1','7b:7','רבי מאיר','quoted_authority','Elul animal-tithe teaching','ר"מ אומר');e('e1','7b:7',claims['c1'],questions['q1'],'answer');e('e2','7b:7',claims['c2'],claims['c1'],'support')
q('q2','7b:8','Whose view is the festivals clause?','ולרגלים מני')
c('c3','7b:8','The festivals clause follows Rabbi Shimon.','רבי שמעון היא')
c('c4','7b:8','The final clause names Rabbi Elazar and Rabbi Shimon for Tishrei 1.','אימא סיפא ר\' אלעזר ור"ש אומרים באחד בתשרי',holder='quoted Mishnah')
c('c5','7b:8','The resulting difficulty is that the first and last clauses use Rabbi Shimon while the middle uses Rabbi Meir.','רישא וסיפא ר"ש ומציעתא ר"מ',status='Compositional difficulty answered next')
e('e3','7b:8',claims['c3'],questions['q2'],'answer')
c('c6','7b:9','Rav Yosef explains that Rebbe compiled the Mishnah by adopting views of different tannaim.','אמר רב יוסף רבי היא ונסיב לה אליבא דתנאי',holder='רב יוסף')
c('c7','7b:9','Rebbe adopts Rabbi Shimon for festivals.','ברגלים סבר לה כר"ש',holder='Rebbe as explained by רב יוסף')
c('c8','7b:9','Rebbe adopts Rabbi Meir for animal tithe.','ובמעשר בהמה סבר לה כר"מ',holder='Rebbe as explained by רב יוסף')
a('a2','7b:9','רב יוסף','speaker','Composite Mishnah explanation','אמר רב יוסף');e('e4','7b:9',claims['c6'],claims['c5'],'answer')
q('q3','7b:10','On this account should the count be five rather than four?','אי הכי ארבעה חמשה הוו')
c('c9','7b:10','Rava interprets four as the count for each individual opinion.','אמר רבא ארבעה לדברי הכל',holder='רבא')
c('c10','7b:10','For Rabbi Meir, omit the festival boundary to obtain four.','לר"מ ארבעה דל רגלים',holder='רבא explaining רבי מאיר')
c('c11','7b:10','For Rabbi Shimon, omit the separately dated animal-tithe boundary to obtain four.','לר"ש ארבעה דל מעשר בהמה',holder='רבא explaining רבי שמעון')
a('a3','7b:10','רבא','speaker','Per-authority count','אמר רבא');e('e5','7b:10',claims['c9'],questions['q3'],'answer')
c('c12','7b:11','Rav Nahman bar Yitzhak counts four months containing several new-year boundaries.',holder='רב נחמן בר יצחק')
a('a4','7b:11','רב נחמן בר יצחק','speaker','Four-month count','רב נחמן בר יצחק אמר');e('e6','7b:11',claims['c12'],questions['q3'],'answer')
c('c13','7b:12','Nisan 16 is the new year for the omer.','ששה עשר בניסן ראש השנה לעומר',holder='quoted teaching')
c('c14','7b:12','Sivan 6 is the new year for the two loaves.','ששה בסיון ראש השנה לשתי הלחם',holder='quoted teaching')
c('c15','7b:12','Including these would require six in Rava’s count.','לרבא ליתני ששה',status='Objection, not accepted final count')
c('c16','7b:12','Including the extra month would require five in Rav Nahman bar Yitzhak’s count.','לר"נ בר יצחק ליתני חמשה',status='Objection, not accepted final count')
e('e7','7b:12',claims['c15'],claims['c9'],'objection');e('e8','7b:12',claims['c16'],claims['c12'],'objection')
c('c17','7b:13','Rav Pappa restricts the enumeration to boundaries effective from nightfall; those not effective then are omitted.',holder='רב פפא',status='Criterion challenged and defended for festivals and jubilee')
a('a5','7b:13','רב פפא','speaker','Nightfall criterion','אמר רב פפא');e('e9','7b:13',claims['c17'],claims['c15'],'answer');e('e10','7b:13',claims['c17'],claims['c16'],'answer')
q('q4','7b:14','Festivals are counted although their offering requirement is not effective at nightfall.','והרי רגלים דלא חיילי מאורתא וקחשיב')
c('c18','7b:14','Because the person must bring, the obligation already rests on him from the outset.','כיון שצריך לאיתויי מעיקרא מיחייב וקאי')
e('e11','7b:14',questions['q4'],claims['c17'],'objection');e('e12','7b:14',claims['c18'],questions['q4'],'answer')
q('q5','7b:15','Jubilees are counted although they do not take effect at nightfall.','והרי יובלות דלא חיילי מאורתא וקחשיב')
c('c19','7b:15','The Mishnah follows Rabbi Yishmael son of Rabbi Yohanan ben Beroka, who holds that jubilee takes effect from New Year.','ר\' ישמעאל בנו של ר\' יוחנן בן ברוקא היא דאמר מראש השנה חייל יובל',holder='רבי ישמעאל בנו של רבי יוחנן בן ברוקא as applied by anonymous discussion')
a('a6','7b:15','רבי ישמעאל בנו של רבי יוחנן בן ברוקא','quoted_authority','Jubilee begins at New Year','ר\' ישמעאל בנו של ר\' יוחנן בן ברוקא');e('e13','7b:15',questions['q5'],claims['c17'],'objection');e('e14','7b:15',claims['c19'],questions['q5'],'answer')
c('c20','7b:16','Rav Shisha son of Rav Idi restricts the count to boundaries not dependent on an action.',holder='רב שישא בריה דרב אידי')
a('a7','7b:16','רב שישא בריה דרב אידי','speaker','Act-independent criterion','רב שישא בריה דרב אידי אמר');e('e15','7b:16',claims['c20'],claims['c15'],'answer');e('e16','7b:16',claims['c20'],claims['c16'],'answer')
q('q6','7b:17','Festivals depend on an act, yet are counted.','והרי רגלים מידי דתלי במעשה וקא חשיב')
c('c21','7b:17','The delay prohibition takes effect automatically.','בל תאחר ממילא חייל')
e('e17','7b:17',questions['q6'],claims['c20'],'objection');e('e18','7b:17',claims['c21'],questions['q6'],'answer')
q('q7','8a:1','What about jubilees?','והרי יובלות')
c('c22','8a:1','The reply again invokes Rabbi Yishmael son of Rabbi Yohanan ben Beroka.','ר\' ישמעאל בנו של רבי יוחנן בן ברוקה היא',holder='anonymous discussion',status='Repeated authority-specific reply to action criterion; separate occurrence')
e('e19','8a:1',questions['q7'],claims['c20'],'objection');e('e20','8a:1',claims['c22'],questions['q7'],'answer')
c('c23','8a:2','Rav Ashi counts four new years that occur on the firsts of four months.',holder='רב אשי',status='Immediately qualified for Beit Hillel’s tree date')
a('a8','8a:2','רב אשי','speaker','First-of-month enumeration','ורב אשי אמר');e('e21','8a:2',claims['c23'],questions['q3'],'answer')
q('q8','8a:3','Does Shevat 1 not follow Beit Shammai specifically?','באחד בשבט כב"ש')
c('c24','8a:3','Three are agreed by all; the Shevat 1 boundary is disputed by Beit Shammai and Beit Hillel.','ה"ק שלשה לדברי הכל באחד בשבט מחלוקת ב"ש וב"ה',status='Qualification of Rav Ashi’s count; no blanket four-distinct-dates assertion')
e('e22','8a:3',questions['q8'],claims['c23'],'objection');e('e23','8a:3',claims['c24'],questions['q8'],'answer');e('e24','8a:3',claims['c24'],claims['c23'],'qualification')
for r in p['records']:
 if r['layer']=='claims':r['content']['scope']='Mishnah attribution and count of new years, with authority-specific calendar qualifications'
for ref in refs:
 sid=segments[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  rationale='Read 7b:7–8b:12 with prior overlap; preserved alternative enumeration criteria and objection/reply sequence.'
  if layer=='reconciliation':rationale='Second source pass checked separate counts and authorities, nightfall/action criteria, repeated jubilee reply and Shevat qualification; no absolute calendar or practical-ruling inference.'
  elif not ids:rationale={'questions':'No explicit question found in this segment.','attributions':'No new named attribution; anonymous voice retained.','claims':'Question-only segment with answer in continuation.','positions':'No independent asserted position in this question segment.','edges':'No additional supported relation originating here.'}.get(layer,rationale)
  p['coverage'].append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p['open_tails']=[]
out=Path(__file__).with_name('proposal_011.json');out.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(p['records']),len(refs))
