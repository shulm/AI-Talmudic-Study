import author_yoma_opening as a
import json,hashlib
from pathlib import Path
a.R=[]
add,claim,question,edge=a.add,a.claim,a.question,a.edge
# Distinct attempt namespace without changing the shared schema or validator.
original_add=add
def add(k,*args,**kw): return original_add('derivation.'+k,*args,**kw)
a.add=add
S=add('structure','structure',list(range(7,39)),dict(title='מקור הפרישה ממילואים: דרשות, חלופות ותיקון מסירת רבי יוחנן',primary=True,boundary='open_right',legacy_ids=[]),unc=['Discussion continues with Resh Lakish challenge at Yoma 3b:12; no global conclusion recorded.'])
for i in range(7,39):add('u'+str(i),'utterances',[i],dict(textual_voice='anonymous discussion with named reports preserved in attribution records',discourse_role='derivation, challenge, distinction or reported alternative',composition='composite' if i!=22 else 'atomic'))
q7=question('q7',7,'מניין פרישת הפרה ויום הכיפורים?',q='מנא הני מילי')
c7a=claim('c7a',7,'לעשות נדרש למעשי פרה בדיווח רבי מניומי בר חלקיה בשם רבי מחסיא בר אידי בשם רבי יוחנן.',holder='רבי יוחנן — ייחוס ראשוני למסירה',unc=['Yoma 3b:11 identifies this as his teacher’s teaching, reported in Rabbi Yishmael’s name; not an unqualified personal ruling.'])
c7b=claim('c7b',7,'לכפר נדרש למעשי יום הכיפורים באותה מסירה.',holder='רבי יוחנן — במסירה המצוטטת')
for k,name in [('m','רבי מניומי בר חלקיה'),('h','רבי מחסיא בר אידי')]:add('report7'+k,'attributions',[7],dict(surface=name,role='transmitter',candidates=[name],scope='לעשות אלו מעשי פרה לכפר אלו מעשי יום הכפורים',transmission_chain=['רבי מניומי בר חלקיה','רבי מחסיא בר אידי','רבי יוחנן']),[c7a,c7b])
edge('e7a',7,c7a,q7,'answer');edge('e7b',7,c7b,q7,'answer')
c8=claim('c8',8,'העמדת כל הפסוק בפרה נדחית מכיוון שכתוב לכפר והפרה אינה בת כפרה.');q8=question('q8',8,'מדוע לא להעמיד את כל הפסוק ביום הכיפורים?')
c9a=claim('c9a',9,'גזירת צוה צוה קושרת את הפסוק לפרה.');c9b=claim('c9b',9,'מאותה השוואה מועברת חובת פרישה מכאן לפרה.');edge('e9',9,c9a,q8,'answer');edge('e9b',9,c9a,c9b,'support')
q10=question('q10',10,'מדוע לא ללמוד מצוה שנאמר ביום הכיפורים?');c10=claim('c10',10,'דנים ציווי שלפני עשייה מציווי שלפני עשייה, ולא מציווי המסופר לאחר עשייה.',cond=['השוואת מיקום הציווי ביחס לעשייה']);edge('e10',10,c10,q10,'answer')
q11=question('q11',11,'מדוע לא ללמוד מציווי הקרבנות ביום צותו?');c11=claim('c11',11,'מעדיפים צוה מצוה ולא צותו מצוה.');edge('e11',11,c11,q11,'answer')
q12=question('q12',12,'מה חשיבות ההבדל הלשוני, והרי דבי רבי ישמעאל מקשרים ושב ובא?');c12=claim('c12',12,'תנא דבי רבי ישמעאל מלמד זו היא שיבה זו היא ביאה.',holder='תנא דבי רבי ישמעאל');edge('e12',12,c12,c11,'objection')
c13=claim('c13',13,'לימוד מלשונות שונות אפשרי כשאין לשון דומה, אך כשיש דומה לומדים ממנה.',cond=['ליכא דדמי ליה לעומת איכא דדמי ליה']);edge('e13',13,c13,q12,'answer');edge('e13b',13,c13,c12,'qualification')
c14=claim('c14',14,'הדיון חוזר לדרשת לכפר על יום הכיפורים.');q14=question('q14',14,'מדוע לכפר אינו כפרת קרבנות?')
q15a=question('q15a',15,'האם ידוע מראש איזה כהן יזדמן לקרבן כדי להפרישו?');c15a=claim('c15a',15,'מוצעת פרישה לכל משמרת בית אב כתשובה לבעיית זיהוי הכהן.',mode='hypothetical');c15b=claim('c15b',15,'דנים דבר שקבוע לו זמן מדבר שקבוע לו זמן ומוציאים קרבנות הקיימים בכל יום.');edge('e15a',15,c15a,q15a,'answer');edge('e15b',15,c15b,q14,'answer')
q16=question('q16',16,'מדוע לא רגלים?');c16=claim('c16',16,'משווים דבר הנוהג פעם בשנה לדבר הנוהג פעם בשנה, שלא כרגלים.');edge('e16',16,c16,q16,'answer')
q17=question('q17',17,'מדוע לא רגל אחד, פסח או סוכות?');c17a=claim('c17a',17,'לפסח מוצע יתרון משום שהכתוב פתח בו תחילה.',mode='hypothetical');c17b=claim('c17b',17,'לסוכות מוצע יתרון משום שמצוותו מרובה.',mode='hypothetical');edge('e17a',17,c17a,q17,'support');edge('e17b',17,c17b,q17,'support')
c18=claim('c18',18,'משווים פרישת שבעה ליום אחד, ולא פרישת שבעה לשבעה.');edge('e18',18,c18,q17,'answer')
q19=question('q19',19,'מדוע לא שמיני עצרת, שהוא יום אחד?');c19=claim('c19',19,'משווים דבר שאין קדושה לפניו, ולא דבר שיש קדושה לפניו.');edge('e19',19,c19,q19,'answer')
q20=question('q20',20,'האם קל וחומר אינו מחייב פרישה דווקא כשקדושה לפניו?');c20=claim('c20',20,'רב משרשיא דוחה: הזה כתיב, כזה, ולכן נדרשת דמיון.',holder='רב משרשיא');edge('e20',20,c20,q20,'answer');edge('e20b',20,q20,c19,'objection')
c21=claim('c21',21,'רב אשי שולל חיוב פרישה לטפל כשעיקר הרגל אינו טעון פרישה.',holder='רב אשי');q21=question('q21',21,'האם ייתכן שעיקר הרגל אינו טעון פרישה וטפלו טעון?');edge('e21',21,c21,q19,'answer')
c22=claim('c22',22,'שמיני עצרת נחשב רגל בפני עצמו לענייני פז״ר קש״ב; זוהי המשכה של הגבלה מן הקטע הקודם.',holder='רב אשי — המשך דבריו',cond=['גם למאן דאמר שמיני רגל בפני עצמו'],unc=['Acronym retained without adding expanded meanings absent from this segment.'])
c23a=claim('c23a',23,'לעניין תשלומין שמיני עצרת הוא תשלומי הראשון.',holder='רב אשי — המשך דבריו');c23b=claim('c23b',23,'מי שלא חג ביום טוב הראשון חוגג כל הרגל וגם ביום טוב האחרון.',holder='משנה מצוטטת',cond=['מי שלא חג ביום טוב הראשון']);edge('e23a',23,c23b,c23a,'support');edge('e23b',23,c23a,c22,'qualification')
q24=question('q24',24,'מדוע לא עצרת, שיש בה פרישת שבעה ליום אחד?');c24=claim('c24',24,'רבי אבא מבחין בין פר אחד ואיל אחד לבין שני אילי עצרת.',holder='רבי אבא');edge('e24',24,c24,q24,'answer')
q25=question('q25',25,'מה התשובה למאן דאמר שביום הכיפורים שני אילים?');c25a=claim('c25a',25,'רבי אומר שאיל ויקרא ואיל חומש הפקודים הם אחד.',holder='רבי');c25b=claim('c25b',25,'רבי אליעזר ברבי שמעון אומר ששני אילים הם, אחד בכל פרשה.',holder='רבי אליעזר ברבי שמעון');edge('e25',25,c25b,c24,'objection')
c26=claim('c26',26,'גם לשני אילים ביום הכיפורים אחד לחובת היום ואחד למוספין, בעוד שני אילי עצרת לחובת היום.',cond=['אפילו לרבי אליעזר ברבי שמעון']);edge('e26',26,c26,q25,'answer')
q27=question('q27',27,'מדוע לא ראש השנה שגם בו יום אחד?');c27=claim('c27',27,'רבי אבהו משווה פר ואיל פרטיים, ומוציא עצרת וראש השנה שקרבנותיהם ציבוריים.',holder='רבי אבהו');edge('e27',27,c27,q27,'answer')
q28=add('q28','questions',[27,28],dict(formulation='כיצד תעמוד ההבחנה לשיטה שקח לך ועשה לך משל ציבור?',question_origin='explicit',conditions=['למאן דאמר משל ציבור'],answer_set_status='partial'));edge('e28',28,q28,c27,'objection')
c29a=claim('c29a',29,'רבי יאשיה דורש קח לך ועשה לך משלך, ויקחו אליך משל ציבור.',holder='רבי יאשיה');c29b=claim('c29b',29,'רבי יונתן סובר שגם קח לך וגם ויקחו אליך משל ציבור.',holder='רבי יונתן');c29c=claim('c29c',29,'לרבי יונתן קח לך מבטא כביכול רצון בשלך יותר מבשלהם.',holder='רבי יונתן');edge('e29',29,c29b,q28,'support')
q30=question('q30',30,'כיצד ליישב ועשית לך ארון עץ עם ועשו ארון עצי שטים?');c30=claim('c30',30,'אבא חנן בשם רבי אלעזר מבחין בין זמן שישראל עושים רצונו של מקום לזמן שאין עושים; אין כאן שיוך מפורש של כל פסוק בנפרד.',holder='רבי אלעזר',unc=['The text lists two states without explicitly matching each verse; no order-based mapping asserted.']);add('a30','attributions',[30],dict(surface='אבא חנן',role='transmitter',candidates=['אבא חנן'],scope='יישוב פסוקי עשיית הארון',transmission_chain=['אבא חנן','רבי אלעזר']),[c30]);edge('e30',30,c30,q30,'answer')
c31a=claim('c31a',31,'המחלוקת האמורה מוגבלת לקיחות ועשיות כלליות, כגון סמים וחצוצרות.');c31b=claim('c31b',31,'במילואים ההבחנה בין קחו של ישראל לקח לך של אהרן מפרשת שמדובר בשל אהרן.');edge('e31a',31,c31a,c29b,'qualification');edge('e31b',31,c31b,q28,'answer')
c32=claim('c32',32,'ביום הכיפורים אשר לו, נוסף על קרבנות העדה, מפרש שהפר משלו.');edge('e32',32,c32,q28,'answer')
c33=claim('c33',33,'רב אשי משווה פר לחטאת ואיל לעולה, ומוציא ראש השנה ועצרת שפרם ואילם עולות.',holder='רב אשי');edge('e33',33,c33,q27,'answer');edge('e33b',33,c33,q24,'answer')
c34=claim('c34',34,'רבינא משווה עבודה בכהן גדול לעבודה בכהן גדול ומוציא את חלופות הקושיות.',holder='רבינא',unc=['First reported version, not merged with following איכא דאמרי.']);edge('e34',34,c34,q27,'answer')
c35a=claim('c35a',35,'לפי איכא דאמרי רבינא משווה עבודה תחילה לעבודה תחילה.',holder='רבינא — איכא דאמרי');q35=question('q35',35,'מה פירוש תחילה?');c35b=claim('c35b',35,'פירוש תחילה בכהן גדול אינו חלופה חדשה, שכן הוא זהה לגרסה הקודמת.',mode='rejected');c35c=claim('c35c',35,'הגרסה החלופית מתפרשת כעבודה תחילה במקום.');edge('e35',35,c35c,q35,'answer');edge('e35b',35,c35b,c35a,'qualification')
c36a=claim('c36a',36,'רב דימי מוסר שרבי יוחנן שנה דרשה אחת, לעשות לכפר על יום הכיפורים.',holder='רבי יוחנן',unc=['This is Rav Dimi’s report of the personal teaching, distinct from the teacher-attributed report.']);c36b=claim('c36b',36,'רב דימי מוסר שרבי יהושע בן לוי שנה שתיים: לעשות לפרה ולכפר ליום הכיפורים.',holder='[רבי יהושע בן לוי]',unc=['Bracketed source reading preserved; identity normalized only provisionally.']);add('a36','attributions',[36],dict(surface='רב דימי',role='transmitter',candidates=['רב דימי'],scope='רבי יוחנן מתני חדא וריב״ל מתני תרתי',transmission_chain=['רב דימי']),[c36a,c36b])
q37=question('q37',37,'כיצד רבי יוחנן שנה רק אחת כאשר נשנתה פרישה גם לפרה?');c37=claim('c37',37,'פרישת הפרה מוסברת כמעלה בעלמא לפי מסירת רבי יוחנן האישית.');edge('e37',37,c37,q37,'answer');edge('e37b',37,c37,c36a,'qualification')
q38=question('q38',38,'כיצד ליישב את המסירה בשם רבי יוחנן הדורשת גם פרה?');c38a=claim('c38a',38,'המסירה הדורשת שתיים היא של רבו של רבי יוחנן.');c38b=claim('c38b',38,'רבין מוסר רבי יוחנן משום רבי ישמעאל: לעשות לפרה ולכפר ליום הכיפורים.',holder='רבי ישמעאל');add('a38','attributions',[38],dict(surface='רבין',role='transmitter',candidates=['רבין'],scope='לעשות אלו מעשה פרה לכפר אלו מעשה יום הכפורים',transmission_chain=['רבין','רבי יוחנן','רבי ישמעאל']),[c38b]);add('a38j','attributions',[38],dict(surface='רבי יוחנן',role='transmitter',candidates=['רבי יוחנן'],scope='דרשת רבו רבי ישמעאל',transmission_chain=['רבי יוחנן','רבי ישמעאל']),[c38b]);edge('e38',38,c38a,q38,'answer');edge('e38b',38,c38b,c7a,'correction');edge('e38c',38,c38b,c36a,'distinction')
C=[]
for i in range(7,39):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  note='Actual source rereading: preserve proposed alternatives as questions, conditional distinctions, cross-segment clauses at 3a:1 and 3b:1, two Ravina versions and 3b:11 attribution correction. Later Resh Lakish challenge remains open and unprocessed.'
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+(' No distinct explicit record in this layer found for this segment.' if not ids else '')))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=[S])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=Path(__file__).parent/'yoma_derivation_002.json'
if path.exists():assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(a.R))))
