"""Build the selected Hebrew research index; no changes to previous projects."""
import ast
import collections
import json
import re
from pathlib import Path
from build_abaye_rava_report import he_ref, link
from yochanan_lakish_review import main as review

P=Path(__file__).parent/'yochanan_lakish_results'
def save(name,value):
 (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def main():
 review()
 rows=json.loads((P/'candidates.json').read_text(encoding='utf-8'))
 decisions={d['key']:d for d in json.loads((P/'review_decisions.json').read_text(encoding='utf-8'))}
 picked=[r for r in rows if decisions[r['key']]['decision']=='selected_excerpt_review']
 broad=json.loads((P/'broad_candidates.json').read_text(encoding='utf-8'))
 # Explicit objections / alternative interpretations missed by paired-declaration syntax.
 supplemental=[]
 for i in [81,166,240,516,541,549,647,739,855,859,1036,1041,1069,1140,1142,1198,1235]:
  r=dict(broad[i]);r['review_id']='broad:'+str(i)
  decision={'key':r['key'],'broad_index':i,'ref':r['ref'],'decision':'selected_dialogue_excerpt',
   'reason':'נקרא ציטוט המשא ומתן: דחייה או פירוש חלופי; אין זו קביעה שהמחלוקת נותרה למסקנה.','reconciled':False}
  decisions[r['key']]=decision;supplemental.append(decision);picked.append(r)
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
 meta={'title':'מחלוקות רבי יוחנן וריש לקיש — מפתח מקורות','date':'2026-11-23',
  'works':len(coverage),'units_scanned':sum(c['units'] for c in coverage),'entries':len(entries),
  'selected_candidates':len(picked),'raw_candidates':len(rows),'broad_windows':2109,
  'branch_counts':dict(collections.Counter(e['branch'] for e in entries)),
  'scope':'נסרקו 37 מסכתות הבבלי ו־39 מסכתות הירושלמי במאגר המקומי: גוף התלמוד, ללא פירושים. ההפניות בירושלמי הן לפי פרק, הלכה וקטע במהדורת המאגר.',
  'limitations':'מפתח מחקר בבדיקה ראשונית, לא רשימה סופית ומאומתת של כל המחלוקות. נקראו ציטוטי מועמדים, חלקם בתצוגות מקוצרות; לא נבדקה כל סוגיה במלואה. נכללו הבדלי דעות, דרשות, תירוצים וראיות. מספר הרשומות הוא מספר מקומות במקור, ולא מספר מחלוקות ייחודיות: המשך דיון ומקבילות נשמרו. הצעות שלא נבחרו וחלונות סמיכות דורשים המשך בדיקה.',
  'method':'חיפוש רבי יוחנן מול רבי שמעון בן לקיש, ריש לקיש, בר לקיש, רשב״ל, ר״ל ור״ש בן לקיש; כינויי ר׳ וכתיב גרש נכללו לאחר נרמול. ר״ל הוא גם קיצור דו־משמעי, ולכן אינו הוכחה לזהות בפני עצמו. צימוד אמירות וסמיכות עד 1,400 תווים, ולאחר מכן סינון ראשוני של הסכמות ומעברים בין נושאים. אין לייחס חד אמר לפי סדר השמות. נשמרו נתיב מקור, SHA-256 ואינדקס מערך; תגיות, ניקוד וריווח נורמלו. קובצי המקור לא שונו.',
  'raw_notice':'1,409 מועמדי תבניות ו־2,109 חלונות סמיכות חופפים בחלקם: אין לחבר את המספרים או למנותם כמחלוקות.'}
 data={'metadata':meta,'entries':entries,'coverage':coverage};save('yochanan_lakish_index.json',data)
 lines=[meta['title'],'תאריך: '+meta['date'],f'רשומות מראי מקום: {len(entries)}',meta['scope'],meta['limitations'],meta['method'],'']
 for e in entries:
  lines+=['='*70,str(e['id'])+'. '+e['he_ref'],e['ref'],e['link'],'הערות המחקר:']+e['notes']+['לשון המקור וההקשר:']
  for u in e['source_units']:lines+=['['+u['ref']+']',u['text'],'']
 (P/'מחלוקות_רבי_יוחנן_וריש_לקיש.txt').write_text('\n'.join(lines),encoding='utf-8-sig')
 tree=ast.parse(Path(__file__).with_name('build_rav_shmuel_report.py').read_text(encoding='utf-8'))
 template=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='template' for t in n.targets))
 template=template.replace('רב ושמואל','רבי יוחנן וריש לקיש').replace('22 בנובמבר','23 בנובמבר').replace('classified_candidates.json','broad_candidates.json')
 template=template.replace('PAYLOAD',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
 (P/'מחלוקות_רבי_יוחנן_וריש_לקיש.html').write_text(template,encoding='utf-8')
 print(json.dumps(meta|{'tractates_with_entries':len({e['work'] for e in entries})},ensure_ascii=False))

if __name__=='__main__':main()
