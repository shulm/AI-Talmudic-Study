"""Build the selected Hebrew research index; no changes to previous projects."""
import ast
import hashlib
import collections
import json
import re
from pathlib import Path
from build_abaye_rava_report import he_ref, link
from rabbah_yosef_review import main as review
from rabbah_yosef_search import mentions
from abaye_rava_search import load_works, record

P=Path(__file__).parent/'rabbah_yosef_results'
def save(name,value):
 (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def main():
 review()
 rows=json.loads((P/'candidates.json').read_text(encoding='utf-8'))
 decisions={d['key']:d for d in json.loads((P/'review_decisions.json').read_text(encoding='utf-8'))}
 picked=[r for r in rows if decisions[r['key']]['decision']=='selected_excerpt_review']
 broad_raw=(P/'broad_candidates.json').read_bytes()
 assert hashlib.sha256(broad_raw).hexdigest()=='02e0f8aec452aa184875c3d780d77069ad4abd2accaa0b53132745e6fa19e34d', 'Broad snapshot changed; remap supplements by stable keys'
 broad=json.loads(broad_raw)
 # Explicit objections / alternative interpretations missed by paired-declaration syntax.
 supplemental=[]
 supplements={
 46:'חילוף ייחוס במסירת מימרה: רבה מוסר בשם רב, ורב יוסף מתקן לשמואל; אין זו מחלוקת בדין עצמו.',
 62:'רב יוסף משיג; שלחו מתם הלכתא כרב יוסף. בסוף הקטע הגמרא מעמידה את דברי רבה ורב חסדא בשמנים. יש להבחין בין השלבים.',
 84:'רב יוסף דוחה את הצעת רבה להסבר מחלוקת בית שמאי ובית הלל.',
 110:'רבה מסכים בהנהון לפירוש רב ששת; רב יוסף דוחה את הפירוש.',
 147:'המשך המחלוקת במועד קטן ב ע״ב: רב יוסף מקשה על טעמו של רבה. אין זו סוגיה ייחודית נוספת.',
 333:'הנוסח מייחס את הקושיה לרבה, ואילו את התירוץ החלופי לרבא. אין לייחס את תירוצו של רבא לרבה ללא בירור נוסח.',
 341:'רב יוסף מקשה על תשובת רבה ממסורת רב יהודה; הסתירה מתיישבת בהבחנה בין המצבים. אין להציג כמחלוקת שנשארה למסקנה.',
 353:'רב יוסף מנסח ראיה כנגד רבה; הסיום תיובתא דרבה תיובתא. צורף גם תחילת הדיון.',
 367:'מקרה ראשון בכפייה על מידת סדום; ההמשך דן במקרה נוסף. נפסק בקטע כרב יוסף.',
 425:'המשך מחלוקת יאוש ושינוי: לאחר עשרים ושתיים שנה רב יוסף מתרץ את הקושיה על שיטתו. אינו נושא ייחודי נוסף.',
 440:'רבה דוחה את הצעת רב יוסף בניהול כספי יתומים ומציע דרך אחרת; בהמשך רב אשי משלים את ההצעה.',
 457:'הבדל עמדות באגדה על ביאת המשיח. רבה מופיע בסוגריים מרובעים בנוסח המאגר; נשמר ללא תיקון.'
 }
 assert len(broad)==477,'Remap supplemental indexes if the snapshot changes'
 for i,note in supplements.items():
  r=dict(broad[i]);r['review_id']='broad:'+str(i)
  decision={'key':r['key'],'broad_index':i,'ref':r['ref'],'decision':'selected_dialogue_excerpt',
   'reason':'נקרא ציטוט המשא ומתן; לא נבדקה כל הסוגיה.','note':note,'reconciled':i==341}
  decisions[r['key']]=decision;supplemental.append(decision);picked.append(r)
 works={w['work']:w for w in load_works()}
 # Extend the resolved objection and late rebuttal to retain their premises and conclusion.
 for r in picked:
  if r['ref'] in {'Yevamot 110b:8','Yevamot 45a:18','Bava Kamma 66b:14'}:
   w=works[r['work']]; k=next(j for j,u in enumerate(w['units']) if u['ref']==r['ref'])
   r['source_units']=w['units'][max(0,k-8):k+12]
 save('supplemental_decisions.json',supplemental)
 grouped=collections.defaultdict(list)
 for r in picked:grouped[r['ref']].append(r)
 entries=[]
 for ref,rs in grouped.items():
  r=rs[0]; us={u['ref']:u for x in rs for u in x['source_units']}
  units=sorted(us.values(),key=lambda u:u['index'])
  mainunit=next(u for u in units if u['ref']==ref)
  context='\n'.join(u['text'] for u in units)
  notes=['סיווג ראשוני מקריאת ציטוטים; כולל הבדלי פירוש, דרשות וראיות, ולא רק מחלוקת מעשית. ההקשר כולל לעיתים דיונים סמוכים.']
  if any(x['kind']=='anonymous_pair' for x in rs):
   notes.append('לשון חד אמר: אין לייחס דעה לפי סדר השמות. יש לקרוא את המשך המקור; לעיתים הייחוס מתפרש או משתנה בהמשך. לא נוסף כאן ייחוס שאינו במקור.')
  if re.search(r'הדר ביה|חזר ב|חזר בה|חזרו|הדרו בהו',context):
   notes.append('זוהתה בהקשר לשון חזרה; סימון אוטומטי, ויש לבדוק למי היא מתייחסת ומה נותר למסקנה.')
  if re.search(r'איפוך|איפכא|תסתיים|איכא דאמרי|לא פליג|מחלף|מיחלף|מוחלף|מחלפה|הכי איתמר',context):
   notes.append('זוהו בהקשר חילוף ייחוס, לשון נוספת או בירור היקף המחלוקת; סימון אוטומטי שעשוי להתייחס גם לדיון סמוך.')
  notes.extend(dict.fromkeys(decisions[x['key']]['note'] for x in rs if decisions[x['key']].get('note')))
  label=he_ref(r)
  if r['branch']=='Yerushalmi':
   addr=ref[len(r['work'])+1:].split(':')
   label=r['he_work']+' · פרק '+addr[0]+' הלכה '+addr[1]+' קטע '+addr[2]
  entries.append({'ref':ref,'he_ref':label,'work':r['work'],'he_work':r['he_work'],'branch':r['branch'],
   'status':'reconciled' if any(decisions[x['key']]['reconciled'] for x in rs) else 'dispute',
   'review_level':'first_pass_excerpt','opening':mainunit['text'][:180],
   'evidence':list(dict.fromkeys(x['evidence'] for x in rs)),
   'source_units':[{'ref':u['ref'],'text':u['text'],'link':link(u['ref'])} for u in units],
   'link':link(ref),'source_file':r['source_file'],'source_sha256':r['source_sha256'],
   'json_index':r['json_index'],'candidate_ids':[x['review_id'] for x in rs],
   'candidate_keys':[x['key'] for x in rs],'notes':notes})
 seder={'Zeraim':0,'Moed':1,'Nashim':2,'Nezikin':3,'Kodashim':4,'Tahorot':5}
 entries.sort(key=lambda e:(e['branch']!='Bavli',next((v for k,v in seder.items() if 'Seder '+k in e['source_file']),9),e['he_work'],e['json_index']))
 for i,e in enumerate(entries,1):e['id']=i
 coverage=json.loads((P/'coverage.json').read_text(encoding='utf-8'))
 for c in coverage:
  c['title']=c['work'];c['he_title']=c['he_work'];c['entries']=sum(e['work']==c['work'] for e in entries)
 meta={'title':'מחלוקות רבה ורב יוסף — מפתח מקורות','date':'2026-11-23',
  'works':len(coverage),'units_scanned':sum(c['units'] for c in coverage),'entries':len(entries),
  'selected_candidates':len(picked),'raw_candidates':len(rows),'broad_windows':len(broad),
  'branch_counts':dict(collections.Counter(e['branch'] for e in entries)),
  'scope':'נסרקו 37 מסכתות הבבלי ו־39 מסכתות הירושלמי במאגר המקומי: גוף התלמוד, ללא פירושים. ההפניות בירושלמי הן לפי פרק, הלכה וקטע במהדורת המאגר.',
  'limitations':'מפתח מחקר בבדיקה ראשונית, לא רשימה סופית ומאומתת של כל המחלוקות. נקראו ציטוטי מועמדים, חלקם בתצוגות מקוצרות; לא נבדקה כל סוגיה במלואה. נכללו הבדלי דעות, דרשות, תירוצים וראיות. מספר הרשומות הוא מספר מקומות במקור, ולא מספר מחלוקות ייחודיות: המשך דיון ומקבילות נשמרו. הצעות שלא נבחרו וחלונות סמיכות דורשים המשך בדיקה.',
  'method':'חיפוש רבה ורב יוסף, כולל רבה בר נחמני, תחיליות ופעלי אמירה ברבים. רבה ורבא אינם מאוחדים. צימוד אמירות וסמיכות עד 1,400 תווים, או בתוך אותו קטע, ולאחר מכן קריאת ציטוטים וסינון ראשוני. אין לייחס חד אמר לפי סדר השמות. נשמרו נתיב מקור, SHA-256 ואינדקס מערך; תגיות, ניקוד וריווח נורמלו. קובצי המקור לא שונו. לא נבחרה תוצאה בירושלמי; אין בכך הוכחה להעדר מוחלט.',
  'raw_notice':'207 מועמדי תבניות ו־477 חלונות סמיכות חופפים בחלקם: אין לחבר את המספרים או למנותם כמחלוקות.'}
 data={'metadata':meta,'entries':entries,'coverage':coverage};save('rabbah_yosef_index.json',data)
 lines=[meta['title'],'תאריך: '+meta['date'],f'רשומות מראי מקום: {len(entries)}',meta['scope'],meta['limitations'],meta['method'],'']
 for e in entries:
  lines+=['='*70,str(e['id'])+'. '+e['he_ref'],e['ref'],e['link'],'הערות המחקר:']+e['notes']+['לשון המקור וההקשר:']
  for u in e['source_units']:lines+=['['+u['ref']+']',u['text'],'']
 (P/'מחלוקות_רבה_ורב_יוסף.txt').write_text('\n'.join(lines),encoding='utf-8-sig')
 tree=ast.parse(Path(__file__).with_name('build_rav_shmuel_report.py').read_text(encoding='utf-8'))
 template=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='template' for t in n.targets))
 template=template.replace('רב ושמואל','רבה ורב יוסף').replace('22 בנובמבר','23 בנובמבר').replace('classified_candidates.json','broad_candidates.json')
 template=template.replace('PAYLOAD',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
 (P/'מחלוקות_רבה_ורב_יוסף.html').write_text(template,encoding='utf-8')
 print(json.dumps(meta|{'tractates_with_entries':len({e['work'] for e in entries})},ensure_ascii=False))

if __name__=='__main__':main()
