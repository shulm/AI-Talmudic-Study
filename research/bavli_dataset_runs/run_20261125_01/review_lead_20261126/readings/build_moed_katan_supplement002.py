import json, hashlib, pathlib, collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
JOB=ROOT/'jobs/bavli_moed_katan_supplement002.json'
job=json.loads(JOB.read_text(encoding='utf-8-sig'))
def digest(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert digest(job['source']['path'])==job['source']['sha256']
for x in job['common_documents']: assert digest(x['path'])==x['sha256']
src=json.loads(pathlib.Path(job['source']['path']).read_text(encoding='utf8'))
texts={f'Moed Katan {(i+2)//2}{"a" if i%2==0 else "b"}:{j+1}':s for i,a in enumerate(src['text']) for j,s in enumerate(a)}
records=[]
def ev(ref,quote=None):
 ref=ref if ref.startswith('Moed') else 'Moed Katan '+ref
 t=texts[ref]; quote=t if quote is None else quote
 start=t.index(quote)
 return {'ref':ref,'segment_id':ref,'start_char':start,'end_char':start+len(quote),'quote':quote}
def rec(layer,evidence,content,uncertainty=None,links=None,origin='source_paraphrase'):
 id=f'mk_s002.{layer}.{sum(r["layer"]==layer for r in records)+1:03}'
 records.append(dict(id=id,layer=layer,evidence=evidence,content=content,origin=origin,uncertainty=uncertainty or [],links=links or []))
 return id
claims={}; questions={}
def c(key,ref,quote,proposition,holder='anonymous discourse',conditions=None,status='asserted',chain=None,uncertainty=None):
 evidence=[ev(ref,quote)]
 cid=rec('claims',evidence,dict(proposition=proposition,conditions=conditions or [],scope='local passage',assertion_mode=status),uncertainty)
 claims[key]=cid
 rec('utterances',evidence,dict(textual_voice=holder,discourse_role='claim-bearing utterance',composition='atomic'),uncertainty,[cid])
 rec('attributions',evidence,dict(surface=holder,role='anonymous' if holder=='anonymous discourse' else 'position_holder',candidates=[holder],scope=cid,transmission_chain=chain or []),uncertainty,[cid])
 rec('positions',evidence,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=conditions or [],local_status=status+'; no later practical ruling inferred'),uncertainty,[cid])
 return cid
def q(key,ref,quote,formulation,answers=None,holder='anonymous discourse'):
 evidence=[ev(ref,quote)]; answers=answers or []
 qid=rec('questions',evidence,dict(formulation=formulation,question_origin='explicit',conditions=[],answer_set_status='partial' if answers else 'none',answer_ids=[claims[a] for a in answers],textual_voice=holder))
 questions[key]=qid
 for a in answers:
  cid=claims[a]
  for r in records:
   if r['layer']=='positions' and r['content']['claim_id']==cid:r['content']['question_id']=qid
  rec('edges',evidence,dict(source_id=cid,target_id=qid,relation='answer',explicitness='source_explicit'),links=[cid,qid])
 return qid
def edge(a,b,rel,ref,quote=None,note=None):
 a=claims.get(a,questions.get(a,a));b=claims.get(b,questions.get(b,b))
 return rec('edges',[ev(ref,quote)],dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit',note=note),links=[a,b])

# Core Mishnah: retain distinct actions and conditions.
c('virgin','8b:7','אין נושאין נשים במועד לא בתולות','One may not marry a virgin on the festival intermediate days.','anonymous Mishnah',['במועד'])
c('widow','8b:7','ולא אלמנות','One may not marry a widow.','anonymous Mishnah',['במועד'])
c('yibbum','8b:7','ולא מייבמין','One may not perform levirate marriage.','anonymous Mishnah',['במועד'])
c('joy','8b:7','מפני ששמחה היא לו','The stated reason is that this brings him joy.','anonymous Mishnah')
c('restore','8b:7','אבל מחזיר הוא את גרושתו','He may remarry his divorced wife.','anonymous Mishnah',['במועד'])
c('adorn','8b:8','ועושה אשה תכשיטיה במועד','A woman may perform her adornment on the intermediate days.','anonymous Mishnah')
c('lime','8b:8','רבי יהודה אומר לא תסוד מפני שניוול הוא לה','A woman may not apply lime because it disfigures her.','רבי יהודה',['במועד'])
c('laysew','8b:8','ההדיוט תופר כדרכו','A layperson sews in the usual manner.','anonymous Mishnah',['במועד'])
c('prosew','8b:8','והאומן מכליב','A professional sews by מכליב.','anonymous Mishnah',['במועד'])
c('bed','8b:8','ומסרגין את המטות','One may מסרגין beds.','anonymous Mishnah',['במועד'])
c('stretch','8b:8','רבי יוסי אומר ממתחין','R. Yose permits ממתחין; the contrast is clarified by the continuation.','רבי יוסי',['במועד'])
c('mix','8b:9','אמר רב יהודה אמר שמואל וכן אמר רבי אלעזר אמר רבי אושעיא ואמרי לה אמר ר\' אלעזר אמר ר\' חנינא לפי שאין מערבין שמחה בשמחה','The marriage prohibition follows the rule against combining one joy with another.','שמואל; רבי אושעיא OR ר׳ חנינא',chain=['רב יהודה → שמואל','רבי אלעזר → רבי אושעיא OR ר׳ אלעזר → ר׳ חנינא'],uncertainty=['The second transmitted authority has two explicit versions; not two simultaneously established chains.'])
c('leave','8b:9','רבה בר [רב] הונא אמר מפני שמניח שמחת הרגל ועוסק בשמחת אשתו','He leaves festival joy and occupies himself with his wife’s joy.','רבה בר [רב] הונא')
c('asrav','8b:10','אמר ליה אביי לרב יוסף הא דרבה בר [רב] הונא דרב הוא','Abaye tells Rav Yosef that Rabbah bar [Rav] Huna’s reason is Rav’s.','אביי')
c('ravverse','8b:10','דאמר רב דניאל בר קטינא אמר רב מנין שאין נושאין נשים במועד שנאמר (דברים טז, יד) ושמחת בחגך בחגך ולא באשתך','Rav derives the prohibition from joy in your festival, excluding joy in your wife.','רב',chain=['רב דניאל בר קטינא','רב'])
c('toil','8b:11','עולא אמר מפני הטורח','Marriage is prohibited because of the exertion.','עולא')
c('procreate','8b:11','רבי יצחק נפחא אמר מפני ביטול פריה ורביה','Marriage is prohibited because of neglect of procreation.','רבי יצחק נפחא')
c('eve','9a:1','מותרין לישא ערב הרגל','Those forbidden to marry during the festival may marry on its eve.','cited baraita',['Applies to כל אלו שאמרו אסורין לישא במועד in 8b:12'])
c('onedayjoy','9a:2','לא קשיא למאן דאמר משום שמחה עיקר שמחה חד יומא הוא','The main joy lasts one day, answering the festival-eve objection to the joy rationale.','anonymous discourse',['Marriage on eve of festival'],status='reconciled')
c('onedaytoil','9a:3','למ"ד משום טירחא עיקר טירחא חד יומא הוא','The main exertion lasts one day.','anonymous discourse',['Marriage on eve of festival'],status='reconciled')
c('delay','9a:3','למ"ד משום ביטול פריה ורביה לחד יומא לא משהי איניש נפשיה','A person does not defer marriage for a single day.','anonymous discourse',['Marriage on eve of festival'],status='reconciled')
c('solomon','9a:4','דכתיב (מלכים א ח, סה) ויעש שלמה בעת ההיא את החג וכל ישראל עמו קהל גדול מלבוא חמת עד נחל מצרים [לפני ה\' אלהינו] שבעת ימים ושבעת ימים ארבעה עשר יום','Solomon’s dedication and festival celebrations are described as seven plus seven days.','scripture quoted by anonymous discourse')
c('wait','9a:4','ואם איתא דמערבין שמחה בשמחה איבעי ליה למינטר עד החג ומיעבד שבעה להכא ולהכא','If joys could be combined, Solomon should have waited for the festival and made seven days count for both.','anonymous discourse',status='hypothetical')
c('coincidence','9a:5','ודלמא מינטר לא נטרינן והיכא דאתרמי עבדינן','Perhaps one does not delay, but may combine if they coincide.','anonymous discourse',status='hypothetical')
c('leavebit','9a:5','איבעי ליה לשיורי פורתא','He should have left a small amount of construction unfinished.','anonymous discourse',status='hypothetical')
c('nodelay','9a:6','שיורי בנין בהמ"ק לא משיירינן','One does not leave Temple construction unfinished.','anonymous discourse')
c('crow','9a:6','איבעי ליה לשיורי באמה כליא עורב','He should have left the crow deterrent unfinished.','anonymous discourse',status='hypothetical')
c('crowneeded','9a:7','אמה כליא עורב צורך בנין הבית הוא','The crow deterrent is required for construction of the Temple.','anonymous discourse')
c('separate','9a:7','אלא מדמייתר קרא מכדי כתיב ארבעה עשר יום שבעת ימים ושבעת ימים למה לי שמע מינה הני לחוד והני לחוד','The redundant seven days and seven days establishes that the celebrations are separate.','anonymous discourse',status='asserted')
c('nokippur','9a:8','א"ר פרנך א"ר יוחנן אותה שנה לא עשו ישראל את יום הכפורים','Israel did not observe Yom Kippur that year.','רבי יוחנן',chain=['ר׳ פרנך','ר׳ יוחנן'])
c('fear','9a:8','והיו דואגים ואומרים שמא נתחייבו שונאיהן של ישראל כלייה','Israel feared annihilation for this conduct, using the euphemism שונאיהן של ישראל.','Israel in reported narrative',status='queried')
c('voice','9a:8','יצתה בת קול ואמרה להם כולכם מזומנין לחיי העולם הבא','A heavenly voice assured them all of life in the world to come.','בת קול within ר׳ יוחנן narrative',chain=['ר׳ פרנך','ר׳ יוחנן','בת קול'])
c('kal','9a:9','אמרו קל וחומר ומה משכן שאין קדושתו קדושת עולם וקרבן יחיד דוחה שבת דאיסור סקילה מקדש דקדושתו קדושת עולם וקרבן צבור ויום הכפורים דענוש כרת לא כ"ש','They reasoned a fortiori from the temporary Tabernacle and an individual offering overriding Sabbath with stoning liability to the permanent Temple and communal offering overriding Yom Kippur with karet.','Israel as reconstructed by anonymous discourse')
c('highlow','9a:10','התם צורך גבוה הכא צורך הדיוט','The worry reflects a distinction: there, divine need; here, human need.','anonymous discourse')
c('noeat','9a:10','הכא נמי מיעבד ליעבדו מיכל לא ניכלו ולא לישתו','Proposed alternative: perform the dedication without eating or drinking.','anonymous discourse',status='hypothetical')
c('eat','9a:10','אין שמחה בלא אכילה ושתיה','There is no joy without eating and drinking.','anonymous discourse')
c('seventh','9a:11','אילימא מדכתיב (במדבר ז, יב) ביום הראשון וביום השביעי דלמא שביעי לקרבנות','First/seventh day language might merely count the offerings, so is insufficient proof of overriding Sabbath.','anonymous discourse',status='challenged')
c('eleven','9a:11','אמר רב נחמן בר יצחק אמר קרא (במדבר ז, עב) ביום עשתי עשר יום מה יום כולו רצוף אף עשתי עשר כולן רצופין','The eleventh-day verse is read to indicate continuous days.','רב נחמן בר יצחק')
c('fit11','9a:12','ודלמא ימים הראויין','Perhaps it means eligible days.','anonymous discourse',status='hypothetical')
c('twelve','9a:12','כתיב קרא אחרינא (במדבר ז, עח) ביום שנים עשר יום מה יום כולו רצוף אף שנים עשר יום כולן רצופין','The additional twelfth-day verse indicates continuous days.','anonymous discourse')
c('fit12','9a:13','ודלמא הכא נמי ימים הראויין','Perhaps this verse too counts only eligible days.','anonymous discourse',status='hypothetical')
c('twoverses','9a:13','אם כן תרי קראי למה לי','Two verses would be unnecessary if only eligible days were meant.','anonymous discourse')
c('14days','9a:14','אילימא מדכתיב ארבעה עשר יום ודלמא ימים הראויין','Fourteen days by itself might mean only eligible days and does not suffice to show Yom Kippur was overridden.','anonymous discourse',status='challenged')
c('dayday','9a:14','גמר יום יום מהתם','Continuity for the Temple celebration is learned by יום–יום from the Tabernacle.','anonymous discourse')
c('forgiven','9a:15','דתני תחליפא (מלכים א ח, סו) ביום השמיני שלח את העם ויברכו את המלך וילכו לאהליהם שמחים וטובי לב על כל הטובה אשר עשה ה\' לדוד עבדו ולישראל עמו','Tahlifa teaches the departure verse as evidence of forgiveness.','תחליפא')
c('wives','9a:16','לאהליהם שהלכו ומצאו נשיהם בטהרה','To their tents: they found their wives in purity.','תחליפא teaching continued')
c('shekhinah','9a:16','שמחים שנהנו מזיו השכינה','Joyful: they enjoyed the radiance of the divine presence.','תחליפא teaching continued')
c('sons','9a:16','וטובי לב שכל אחד ואחד נתעברה אשתו בבן זכר','Glad of heart: each man’s wife conceived a male child.','תחליפא teaching continued')
c('good','9a:16','על כל הטובה שיצתה בת קול ואמרה להם כולכם מזומנין לחיי העולם הבא','All the good: the heavenly voice promised them life in the world to come.','תחליפא teaching continued')
c('israelforgiven','9a:17','בשלמא לישראל עמו דאחיל להו עון יום הכפורים','For Israel, the good refers to forgiveness of the Yom Kippur sin.','anonymous discourse')
c('gates','9a:18','אמר רב יהודה אמר רב בשעה שביקש שלמה להכניס ארון למקדש דבקו שערים זה לזה','When Solomon sought to bring the Ark into the Temple, the gates stuck together.','רב',chain=['רב יהודה','רב'])
c('24','9a:18','אמר שלמה עשרים וארבע רננות ולא נענה','Solomon uttered twenty-four praises and was not answered.','רב narrative',chain=['רב יהודה','רב'])
c('psalm','9a:18','פתח ואמר (תהלים כד, ז) שאו שערים ראשיכם וגו\' ולא נענה','Solomon invoked the gate psalm and was not answered.','רב narrative',chain=['רב יהודה','רב'])
c('david','9a:19','כיון שאמר (דברי הימים ב ו, מב) ה\' אלהים אל תשב פני משיחך זכרה לחסדי דוד עבדך מיד נענה','Once Solomon invoked David’s merits, he was immediately answered.','רב narrative',chain=['רב יהודה','רב'])
c('enemies','9a:19','באותה שעה נהפכו פני שונאי דוד כשולי קדירה','At that moment David’s enemies’ faces turned like the bottom of a pot.','רב narrative',chain=['רב יהודה','רב'])
c('davidforgiven','9a:19','וידעו הכל שמחל לו הקב"ה על אותו עון','Everyone knew that God had forgiven David for that sin.','רב narrative',chain=['רב יהודה','רב'],uncertainty=['The sin is not specified by name in this local text.'])
c('students','9a:20','ר\' יונתן בן עסמיי ורבי יהודה בן גרים תנו פרשת נדרים בי ר\' שמעון בן יוחי איפטור מיניה באורתא לצפרא הדור וקא מפטרי מיניה','R. Yonatan ben Asmai and R. Yehudah ben Gerim studied vows with R. Shimon ben Yohai, took leave at night, and returned to take leave in the morning.','anonymous narrator')
c('leaveagain','9a:21','אמרו ליה למדתנו רבינו תלמיד שנפטר מרבו ולן באותה העיר צריך ליפטר ממנו פעם אחרת','A student who takes leave of his teacher and stays overnight in the same city must take leave again.','ר׳ שמעון בן יוחי as recalled jointly by his students',conditions=['Previously took leave','Stayed overnight in same city'],chain=['ר׳ יונתן בן עסמיי and רבי יהודה בן גרים','ר׳ שמעון בן יוחי'])
c('dates','9a:21','שנאמר ביום השמיני שלח את העם ויברכו את המלך וכתיב (דברי הימים ב ז, י) וביום עשרים ושלשה לחדש השביעי שלח את העם','The eighth day and the twenty-third of the seventh month departure texts provide the proof.','students quoting scripture')
c('leaveagainrepeat','9a:22','אלא מכאן לתלמיד הנפטר מרבו ולן באותה העיר צריך ליפטר ממנו פעם אחרת','The repeated conclusion derives the second leave-taking requirement.','students/discourse continuation',conditions=['Previously took leave','Stayed overnight in same city'])
c('worthy','9a:23','א"ל לבריה בני אדם הללו אנשים של צורה הם זיל גביהון דליברכוך','R. Shimon calls the men worthy and tells his son to seek their blessing.','ר׳ שמעון בן יוחי in narrative')
c('weigh','9a:24','לא קשיא כאן במצוה שאפשר לעשותה ע"י אחרים','One side of the apparent weighing-paths contradiction concerns a commandment performable by others.','joint study of ר׳ יונתן בן עסמיי and רבי יהודה בן גרים',conditions=['מצוה שאפשר לעשותה ע״י אחרים'],status='reconciled',uncertainty=['The terse כאן does not expressly attach a named verse here; do not mechanically map by citation order.'])
c('cantweigh','9b:1','כאן במצוה שא"א לעשותה ע"י אחרים','The other side concerns a commandment that others cannot perform.','joint study of ר׳ יונתן בן עסמיי and רבי יהודה בן גרים',conditions=['מצוה שא״א לעשותה ע״י אחרים'],status='reconciled')
c('heavenly','9b:2','הא חפצי שמים ישוו בה','The wording all your desires suggests that heavenly obligations can equal Torah.','joint study: intermediate inference',status='hypothetical')
c('noheavenly','9b:2','דאפילו חפצי שמים לא ישוו בה','The wording all desires suggests that even heavenly obligations cannot equal Torah.','joint study: opposing textual inference',status='hypothetical')
c('others','9b:3','כאן במצוה שאפשר לעשותה ע"י אחרים','The reconciliation distinguishes a commandment performable by others.','joint study of ר׳ יונתן בן עסמיי and רבי יהודה בן גרים',conditions=['מצוה שאפשר לעשותה ע״י אחרים'],status='reconciled')
c('noothers','9b:3','כאן במצוה שאי אפשר לעשותה ע"י אחרים','The reconciliation distinguishes a commandment not performable by others.','joint study of ר׳ יונתן בן עסמיי and רבי יהודה בן גרים',conditions=['מצוה שאי אפשר לעשותה ע״י אחרים'],status='reconciled',uncertainty=['No by-name dispute between the two studying figures is stated.'])
for key,quote,meaning in [('sow','דתזרע ולא תחצד','May you sow and not reap'),('in','תעייל ולא תיפוק','May you bring in and not bring out'),('out','תיפוק ולא תעייל','May you bring out and not bring in'),('house','ליחרוב ביתך וליתוב אושפיזך','May your house be ruined and your lodging inhabited'),('table','לבלבל פתורך','May your table be disturbed'),('year','ולא תחזי שתא חדתא','May you not see a new year')]:
 c(key,'9b:4',quote,meaning+'.','ר׳ יונתן בן עסמיי and רבי יהודה בן גרים, joint blessing',status='asserted',uncertainty=['Blessing wish, not a prediction or legal rule; interpreted by father in continuation.'])
c('hurt','9b:5','לא מבעיא דברוכי לא בירכן אבל צעורי צעורן','The son complains that the men distressed rather than blessed him.','son of ר׳ שמעון בן יוחי',status='challenged')
c('allbless','9b:5','הנך כולהו ברכתא נינהו','All their words are blessings.','ר׳ שמעון בן יוחי')
c('sowmeaning','9b:5','תזרע ולא תחצד תוליד בנים ולא ימותו','Sowing without reaping means having children who do not die.','ר׳ שמעון בן יוחי')
c('inmeaning','9b:5','תעייל ולא תיפוק תעייל כלתא ולא לימותו בנך דליפקון','Bringing in without sending out means daughters-in-law enter and sons do not die, causing them to leave.','ר׳ שמעון בן יוחי')
c('outmeaning','9b:5','תיפוק ולא תעייל תוליד בנתא ולא ימותו גוברייהו וליהדרו לותיך','Sending out without bringing back means daughters marry and their husbands do not die, causing their return.','ר׳ שמעון בן יוחי')
c('housemeaning','9b:6','ליחרוב ביתך וליתוב אושפיזך דהאי עלמא אושפיזך וההיא עלמא ביתא','This world is lodging and the other world home; the apparent curse wishes continued earthly life.','ר׳ שמעון בן יוחי')
c('grave','9b:6','דכתיב (תהלים מט, יב) קרבם בתימו לעולם אל תקרי קרבם אלא קברם','The reading קברם for קרבם establishes the grave as enduring home.','ר׳ שמעון בן יוחי explanation')
c('tablemeaning','9b:7','לבלבל פתורך בבני ובנתא','The table should be disturbed by sons and daughters.','ר׳ שמעון בן יוחי')
c('yearmeaning','9b:7','ולא תיחזי שתא חדתא דלא תמות אנתך ולא תנסב אינתתא אחריתי','Not seeing a new year means the wife should not die, necessitating another marriage.','ר׳ שמעון בן יוחי')
c('departure','9b:8','ר\' שמעון בן חלפתא אפטר מיניה דרב','R. Shimon ben Halafta took leave of Rav.','anonymous narrator',uncertainty=['Preserve the printed opening; do not silently replace names to repair the narrative.'])
c('requestbless','9b:8','א"ל (אבוה) זיל לגביה דליברכך','A father/speaker tells the addressee to go obtain a blessing.','unresolved local pronoun speaker',uncertainty=['The printed parenthetical (אבוה) and unexpressed addressee leave the precise role mapping uncertain.'])
c('shame','9b:8','א"ל יהא רעוא דלא תבייש ולא תתבייש','May you neither shame nor be shamed.','unresolved local blessing speaker',uncertainty=['The local pronominal chain is not resolved by assigning from narrative name order.'])
c('trivial','9b:8','א"ל מילין בעלמא הוא דאמר לי','The recipient dismisses the blessing as mere words.','unresolved recipient reporting to father',status='challenged')
c('godbless','9b:9','א"ל ברכך ברכתא דברכן קודשא בריך הוא לישראל ותנא בה','The father explains that the blessing is one God gave Israel and repeated.','father in narrative continuation')
c('neverashamed','9b:9','דכתיב (יואל ב, כו) ואכלתם אכול ושבוע והללתם וגו\' ולא יבושו עמי לעולם וידעתם כי בקרב ישראל אני וגו\' ולא יבושו עמי לעולם','The repeated promise that My people will never be ashamed supports the blessing’s value.','scripture quoted in father’s explanation')
c('kohl','9b:10','כוחלת','Adornment includes applying kohl.','תנו רבנן',['במועד'])
c('pokeset','9b:10','ופוקסת','Adornment includes פוקסת.','תנו רבנן',['במועד'],uncertainty=['The exact technique is not glossed in this passage.'])
c('rouge','9b:10','ומעבירה (סרק) על פניה','Adornment includes applying (סרק) to her face.','תנו רבנן',['במועד'])
c('lower','9b:10','ואיכא דאמרי מעברת סרק על פניה של מטה','An alternate version places the application on פניה של מטה.','anonymous alternate report',['במועד'],uncertainty=['Preserve as a textual alternate, not a separate named disagreement.'])
c('wifeadorn','9b:11','דביתהו דרב חסדא מקשטא באנפי כלתה','Rav Hisda’s wife adorned herself in front of her daughter-in-law.','anonymous narrator')
c('young','9b:11','יתיב רב הונא בר חיננא קמיה דרב חסדא ויתיב וקאמר לא שנו אלא ילדה אבל זקנה לא','The permission was stated only for a young woman, not an old woman.','רב הונא בר חיננא',status='challenged')
c('old','9b:12','א"ל האלהים אפילו אמך ואפילו אימא דאימך ואפילו עומדת על קברה','Permission applies even to your mother, grandmother, or one standing at her grave.','רב חסדא responding',['Even very old women'])
c('proverb','9b:12','דאמרי אינשי בת שיתין כבת שית לקל טבלא רהטא','The popular saying likens a sixty-year-old to a six-year-old running to the drum.','popular saying quoted by רב חסדא')
c('limerepeat','9b:13','תניא רבי יהודה אומר אשה לא תסוד מפני שניוול הוא לה','R. Yehudah prohibits lime because it disfigures her.','רבי יהודה in baraita',['במועד'])
c('limelater','9b:13','ומודה ר\' יהודה בסיד שיכולה לקפלו במועד שטופלתו במועד שאע"פ שמצירה היא עכשיו שמחה היא לאחר זמן','R. Yehudah permits applying lime removable during the festival despite present distress because she will rejoice afterward.','רבי יהודה in baraita',['Lime can be removed during the festival'],status='conditional')
c('collect','9b:15','רבי יהודה אומר נפרעין מהן מפני שמצר','R. Yehudah permits collecting from them because collection causes distress.','רבי יהודה in cited Mishnah',uncertainty=['The foreign-festival temporal context is not given in the quoted local excerpt; do not invent a quoted condition.'])
c('collectjoy','9b:15','אמרו לו אע"פ שמצר עכשיו שמח הוא לאחר זמן','His interlocutors reply that despite present distress, the debtor rejoices later.','unnamed interlocutors of רבי יהודה')
c('moeddifferent','9b:16','אמר רב נחמן בר יצחק הנח להלכות מועד דכולהו מצר עכשיו ושמח לאחר זמן נינהו','Festival laws are different: they involve present distress followed by joy.','רב נחמן בר יצחק',status='reconciled')
c('debtalways','9b:17','רבינא אמר כותי לענין פרעון לעולם מצר','For repayment the כותי is always distressed.','רבינא',status='reconciled')
for key,quote,meaning in [('poor','עניות טופלות אותן בסיד','Poor girls are treated with lime'),('rich','עשירות טופלות אותן בסולת','Rich girls are treated with fine flour'),('royal','בנות מלכים בשמן המור','Royal daughters are treated with myrrh oil')]:
 c(key,'9b:18',quote,meaning+'.','רב יהודה',['בנות ישראל שהגיעו לפירקן ולא הגיעו לשנים'],uncertainty=['Preserve the source condition verbatim; no exact chronological ages supplied.'])
c('esther','9b:18','שנאמר (אסתר ב, יב) ששה חדשים בשמן המור','Esther’s six months in myrrh oil is cited for the royal treatment.','רב יהודה quoting scripture')
c('stacte','9b:19','רב הונא בר חייא אמר סטכת','שמן המור is סטכת.','רב הונא בר חייא')
c('olive','9b:19','רב ירמיה בר אמי אמר שמן זית שלא הביא שליש','שמן המור is olive oil whose olives have not reached a third.','רב ירמיה בר אמי')
c('anpik','9b:20','תניא רבי יהודה אומר אנפיקינון שמן זית שלא הביא שליש','אנפיקינון is olive oil whose olives have not reached a third.','רבי יהודה in baraita')
c('hair','9b:20','שמשיר את השער','This oil is used because it removes hair.','cited baraita continuation')
c('skin','9b:20','ומעדן את הבשר','This oil softens the flesh.','cited baraita continuation')
c('bibi','9b:21','רב ביבי הוה ליה ברתא טפלה אבר אבר שקל בה ד\' מאה זוזי','Rav Bibi treated his daughter limb by limb and received four hundred zuz in connection with her.','anonymous narrator',uncertainty=['The transaction is not further specified in this source sentence.'])
c('neighbor','9b:21','הוה ההוא כותי בשבבותיה דה"ל ברתא טפלה בחד זמנא ומתה','A neighboring כותי treated his daughter all at once and she died.','anonymous narrator')
c('blame','9b:21','אמר קטלא ביבי לברתי','The neighbor blames Bibi for his daughter’s death.','neighbor, reported accusation',uncertainty=['A character’s accusation is not a narrator’s causal finding.'])
c('beer','9b:21','אמר רב נחמן רב ביבי דשתי שיכרא בעיין בנתיה טפלא','Rav Nahman says Rav Bibi’s daughters require treatment because he drinks beer.','רב נחמן',['Father drinks beer'])
c('nobeer','9b:21','אנן דלא שתינן שיכרא לא בעיין בנתין טפלא','Rav Nahman says our daughters do not require treatment because we do not drink beer.','רב נחמן',['Father does not drink beer'])

# Necessary continuation for the sewing/bed clauses of the core Mishnah.
c('layneedle','10a:1','אמרי דבי רבי ינאי כל שאינו יכול להוציא מלא מחט בבת אחת','A lay sewer cannot draw a full needleful at once.','דבי רבי ינאי')
c('layhem','10a:1','רבי יוסי בר חנינא אמר כל שאינו יכול לכוין אימרא בחפת חלוקו','A lay sewer cannot align the edge at his garment’s hem.','רבי יוסי בר חנינא')
c('skip','10a:2','רבי יוחנן אמר מפסיע','מכליב means spaced stitches.','רבי יוחנן')
c('teeth','10a:2','רבה בר שמואל אמר שיני כלבתא','מכליב means dog-tooth stitching.','רבה בר שמואל')
c('bedfirst','10a:3','חד אמר מסרגין שתי וערב וממתחין שתי בלא ערב','One reported view defines מסרגין as warp and woof, ממתחין as warp alone.','unassigned אחד',chain=['רב דימי','ר׳ חייא בר אבא and ר׳ אסי','חזקיה and ר׳ יוחנן'],uncertainty=['Four names in a report do not license a unique holder mapping.'])
c('bedsecond','10a:3','וחד אמר מסרגין שתי בלא ערב וממתחין שאם היה רפוי ממתחו','The other reported view defines מסרגין as warp alone and ממתחין as tightening looseness.','unassigned אחר',status='challenged',chain=['רב דימי','ר׳ חייא בר אבא and ר׳ אסי','חזקיה and ר׳ יוחנן'])
c('norope','10a:4','והא תני רב תחליפא בר שאול ושוין שאין מפשילין חבלים לכתחלה','All agree fresh ropes may not be twisted.','baraita transmitted by רב תחליפא בר שאול')
c('bedobjection','10a:5','השתא שתי וערב אמרת לא חבלים לכתחלה מיבעיא קשיא','If warp and woof is already prohibited, the no-new-ropes agreement seems superfluous; the second account remains difficult.','anonymous discourse',status='challenged')
c('cells','10a:6','והתנן רבי מאיר אומר המטה משיסרוג בה שלשה בתים','R. Meir’s three cells definition challenges any view defining מסרגין as warp alone.','רב נחמן בר יצחק quoting רבי מאיר to רבי חייא בר אבין')
c('ravinboth','10a:7','אלא כי אתא רבין אמר במסרגין כולי עלמא לא פליגי דשתי וערב','Ravin’s report replaces the earlier account: all agree מסרגין is warp and woof.','רבין',status='asserted')
c('ravinwarp','10a:7','מר סבר ממתחין שתי בלא ערב','One unidentified view defines ממתחין as warp alone.','unassigned מר in רבין report')
c('ravintight','10a:7','ומר סבר שאם היה רפוי ממתחו','The other unidentified view defines ממתחין as tightening looseness.','unassigned מר in רבין report')
c('meirbed','10a:8','מסרגין את המטה ואין צריך לומר שממתחין דברי ר\' מאיר','R. Meir permits מסרגין and certainly ממתחין.','ר׳ מאיר')
c('yosebed','10a:8','ר\' יוסי אומר ממתחין אבל לא מסרגין','R. Yose permits ממתחין but prohibits מסרגין.','ר׳ יוסי')
c('othersbed','10a:8','וי"א אין ממתחין כל עיקר','Others prohibit ממתחין altogether.','יש אומרים')
c('fill','10a:10','אין כיון דאפשר לממלייה במאני לא טרחינן','Even mere tightening can be prohibited by the others because one can fill the bed with clothes instead of exerting effort.','anonymous discourse',['Under tightening interpretation'],status='reconciled')

q('whyjoy','8b:9','וכי שמחה היא לו מאי הוי','Why should joy prohibit marriage?',['mix','leave','ravverse','toil','procreate'])
q('eveobjection','9a:1','קשיא לכולהו','How can festival-eve marriages be allowed under these reasons?',['onedayjoy','onedaytoil','delay'])
q('mixproof','9a:4','ודאין מערבין שמחה בשמחה מנלן','What establishes that one does not combine joys?',['solomon','wait','separate'])
q('deduced','9a:9','מאי דרוש','What did Israel derive?',['kal'])
q('worried','9a:10','אלא אמאי היו דואגים','Why were they worried?',['highlow'])
q('tabernacle','9a:11','ומשכן דדחי שבת מנלן','How is it known that the Tabernacle dedication overrode Sabbath?',['eleven','twelve','twoverses'])
q('temple','9a:14','ומקדש דדוחה יום הכפורים מנלן','How is it known the Temple dedication overrode Yom Kippur?',['dayday'])
q('forgiveproof','9a:15','ומנלן דאחיל להו','What shows that they were forgiven?',['forgiven','wives','shekhinah','sons','good'])
q('davidgood','9a:17','אלא לדוד עבדו מאי היא','What was the good done for David?',['gates','24','psalm','david','enemies','davidforgiven'])
q('tookleave','9a:20','אמר להו ולאו איפטריתו מיני באורתא','Had you not already taken leave last evening?',['leaveagain','dates','leaveagainrepeat'],'ר׳ שמעון בן יוחי')
q('paths','9a:23','דקא רמו קראי אהדדי כתיב (משלי ד, כו) פלס מעגל רגלך וכל דרכיך יכונו וכתיב (משלי ה, ו) אורח חיים פן תפלס','How do the opposed path-weighing verses fit together?',['weigh','cantweigh'],'two students jointly')
q('desires','9b:2','הדר יתבי וקא מבעי להו כתיב (משלי ג, טו) יקרה היא מפנינים וכל חפציך לא ישוו בה הא חפצי שמים ישוו בה וכתיב (משלי ח, יא) כל חפצים לא ישוו בה דאפילו חפצי שמים לא ישוו בה','Do heavenly obligations equal Torah, given the differing verses?',['others','noothers'],'two students jointly')
q('whyhere','9b:4','אמרו ליה מאי בעית הכא','Why have you come?',holder='two students jointly')
c('sent','9b:4','אמר להו דאמר לי אבא זיל גבייהו דליברכוך','The son says his father sent him for their blessing.','son of ר׳ שמעון בן יוחי')
edge('sent','whyhere','answer','9b:4')
q('whatsaid','9b:5','א"ל מאי אמרו לך','What did they say to you?',['sow','in','out','house','table','year'],'ר׳ שמעון בן יוחי')
q('secondwhatsaid','9b:8','א"ל מאי אמר לך','What did he say to you?',['trivial'],'father in second narrative')
q('yehudah','9b:14','ומי אית ליה לרבי יהודה האי סברא והתנן','Does R. Yehudah accept present distress justified by later joy?',['moeddifferent','debtalways'])
q('myrrh','9b:19','מאי שמן המור','What is שמן המור?',['stacte','olive'])
q('oilpurpose','9b:20','ולמה סכין אותו','Why anoint with this oil?',['hair','skin'])
q('laydefinition','10a:1','היכי דמי הדיוט','What counts as a lay sewer?',['layneedle','layhem'])
q('makhliv','10a:2','מאי מכליב','What is מכליב?',['skip','teeth'])
q('beddefinition','10a:3','מאי מסרגין ומאי ממתחין','What are מסרגין and ממתחין?',['bedfirst','bedsecond','ravinboth','ravinwarp','ravintight'])
q('tightproblem','10a:9','אלא למאן דאמר שאם היה רפוי ממתחו ליש אומרים ממתחו נמי לא','Under the tightening definition, do the others prohibit even tightening?',['fill'])

for a,b,rel,ref in [
 ('asrav','leave','qualification','8b:10'),('ravverse','asrav','support','8b:10'),
 ('eve','joy','objection','9a:1'),('eve','mix','objection','9a:1'),('eve','leave','objection','9a:1'),('eve','toil','objection','9a:1'),('eve','procreate','objection','9a:1'),
 ('onedayjoy','mix','qualification','9a:2'),('onedayjoy','leave','qualification','9a:2'),('onedaytoil','toil','qualification','9a:3'),('delay','procreate','qualification','9a:3'),
 ('coincidence','wait','objection','9a:5'),('leavebit','coincidence','answer','9a:5'),('nodelay','leavebit','objection','9a:6'),('crow','nodelay','answer','9a:6'),('crowneeded','crow','objection','9a:7'),('separate','mix','support','9a:7'),
 ('voice','fear','answer','9a:8'),('highlow','kal','qualification','9a:10'),('eat','noeat','objection','9a:10'),('fit11','eleven','objection','9a:12'),('twelve','fit11','answer','9a:12'),('fit12','twelve','objection','9a:13'),('twoverses','fit12','answer','9a:13'),('dayday','14days','answer','9a:14'),
 ('israelforgiven','good','qualification','9a:17'),('dates','leaveagain','support','9a:21'),('leaveagainrepeat','leaveagain','continuation','9a:22'),
 ('cantweigh','weigh','distinction','9b:1'),('noothers','others','distinction','9b:3'),('allbless','hurt','correction','9b:5'),
 ('sowmeaning','sow','qualification','9b:5'),('inmeaning','in','qualification','9b:5'),('outmeaning','out','qualification','9b:5'),('housemeaning','house','qualification','9b:6'),('grave','housemeaning','support','9b:6'),('tablemeaning','table','qualification','9b:7'),('yearmeaning','year','qualification','9b:7'),
 ('godbless','trivial','correction','9b:9'),('neverashamed','godbless','support','9b:9'),('old','young','objection','9b:12'),('proverb','old','support','9b:12'),('limerepeat','lime','quotation','9b:13'),('limelater','lime','qualification','9b:13'),('collectjoy','collect','objection','9b:15'),('moeddifferent','limelater','qualification','9b:16'),('debtalways','collectjoy','objection','9b:17'),('esther','royal','support','9b:18'),
 ('bedobjection','bedsecond','objection','10a:5'),('cells','bedsecond','objection','10a:6'),('ravinboth','bedsecond','correction','10a:7'),('yosebed','stretch','qualification','10a:8'),('fill','othersbed','qualification','10a:10')]:edge(a,b,rel,ref)

# Explicit speech-layer attribution anchors supplement local paraphrases.
for ref,quote,surface,role,scope,chain in [
 ('8b:9','אמר רב יהודה אמר שמואל','רב יהודה','transmitter','mix',['רב יהודה','שמואל']),
 ('8b:9','וכן אמר רבי אלעזר אמר רבי אושעיא ואמרי לה אמר ר\' אלעזר אמר ר\' חנינא','רבי אלעזר / ר׳ אלעזר','transmitter','mix',['רבי אלעזר → רבי אושעיא OR ר׳ אלעזר → ר׳ חנינא']),
 ('8b:10','אמר ליה אביי לרב יוסף','אביי','speaker','asrav',[]),
 ('8b:10','דאמר רב דניאל בר קטינא אמר רב','רב דניאל בר קטינא','transmitter','ravverse',['רב דניאל בר קטינא','רב']),
 ('9a:8','א"ר פרנך א"ר יוחנן','ר׳ פרנך','transmitter','nokippur',['ר׳ פרנך','ר׳ יוחנן']),
 ('9a:18','אמר רב יהודה אמר רב','רב יהודה','transmitter','gates',['רב יהודה','רב']),
 ('9a:21','אמרו ליה למדתנו רבינו','two students','transmitter','leaveagain',['ר׳ יונתן בן עסמיי and רבי יהודה בן גרים','ר׳ שמעון בן יוחי']),
 ('9b:18','אמר רב יהודה','רב יהודה','speaker','poor',[])]:
 rec('attributions',[ev(ref,quote)],dict(surface=surface,role=role,candidates=[surface],scope=claims[scope],transmission_chain=chain),links=[claims[scope]])

for ref in job['core_refs']:
 rec('structure',[ev(ref)],dict(title='Original core segment; linked semantics retain cross-segment continuations',primary=True,boundary='open_both',legacy_ids=[]),origin='editorial_inference')
context=[r for r in texts if r.startswith('Moed Katan 8a:') or r.startswith('Moed Katan 10a:') or r in [f'Moed Katan 8b:{i}' for i in range(1,7)]]
coverage=[]
for ref in job['core_refs']:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in records if r['layer']==layer and any(e['ref']==ref for e in r['evidence'])]
  coverage.append(dict(ref=ref,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Direct original-source pass; repeated proof, question-only and cross-segment clauses reviewed in their local continuation.' if layer!='reconciliation' else 'Reread the original segment against independently enumerated atoms; retained narrative/quoted layers, alternative transmission, conditions and continuation corrections. No producer records consulted.'))
artifact=dict(artifact_kind='frozen_source_only_independent_reading',schema_reference='2.0.0-production; independent review envelope with ref, answer_ids and explanatory note extensions',job_id=job['job_id'],tractate=job['tractate'],core_refs=job['core_refs'],context_refs_actually_read=context,source={**job['source'],'verified_sha256':digest(job['source']['path']),'edition_metadata':{k:src.get(k) for k in ['title','versionTitle','versionSource','license']}},neutral_job={'path':str(JOB),'sha256':digest(JOB)},common_documents=[{**x,'verified_sha256':digest(x['path'])} for x in job['common_documents']],provenance={'route':'interactive_agent','agent_id':'/root/reader_moed_katan_supplement002','model_id':None,'source_only':True,'producer_outputs_read':False,'prior_reader_outputs_read':False,'lead_checkpoints_read':False,'blindness_scope':job['core_refs'],'corpus_mutated':False},records=records,coverage=coverage,limitations=['AI-provisional source-only reading, not human scholarly certification or practical halakhic ruling.','Supplemental coordinate cohort is not a probability sample.','No producer comparison performed.','Evidence uses original Python Unicode code-point offsets; source spelling and markup retained.','9b:8 printed narrative pronouns and parenthetical father are deliberately unresolved.','The two scriptural-mitzvah reconciliations preserve the textual condition alternatives; exact verse-to-condition mapping is not mechanically inferred from order.','Context was read across all 8a, 8b:1–6 and 10a; only context relevant to core sewing/bed clauses was atomically annotated.','Attribution of a speech in a narrated episode does not imply its narrator endorses each embedded assertion.','Full production schema/ownership/replay validation is outside this independent reading; envelope extensions are explicit.'],open_tails=['No extension beyond 10a read; context-only material unrelated to core is not claimed fully extracted.'],counts=dict(core_segments=len(job['core_refs']),context_segments=len(context),records_by_layer=dict(collections.Counter(r['layer'] for r in records))))
ids={r['id'] for r in records}
for r in records:
 for e in r['evidence']: assert texts[e['ref']][e['start_char']:e['end_char']]==e['quote']
 for link in r['links']:assert link in ids
out=ROOT/'readings/moed_katan_supplement002.json'
assert not out.exists(), 'Immutable additive reading already exists'
b=(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n').encode('utf8')
with out.open('xb') as f:f.write(b)
h=hashlib.sha256(b).hexdigest()
with out.with_suffix('.sha256').open('x',encoding='ascii') as f:f.write(h+'  '+out.name+'\n')
print(json.dumps({'path':str(out),'sha256':h,**artifact['counts']},ensure_ascii=False))
