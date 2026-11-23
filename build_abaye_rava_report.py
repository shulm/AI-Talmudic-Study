"""Build the Abaye/Rava report without executing or changing the Rav/Shmuel pipeline."""
import ast
import collections
import json
import re
from pathlib import Path
from urllib.parse import quote
from abaye_rava_review_decisions import main as review

P=Path(__file__).parent/'abaye_rava_results'

def heb(n):
 out=''
 for v,c in [(400,'ת'),(300,'ש'),(200,'ר'),(100,'ק')]:
  while n>=v:out+=c;n-=v
 if n in (15,16):return out+{15:'טו',16:'טז'}[n]
 for v,c in [(90,'צ'),(80,'פ'),(70,'ע'),(60,'ס'),(50,'נ'),(40,'מ'),(30,'ל'),(20,'כ'),(10,'י'),(9,'ט'),(8,'ח'),(7,'ז'),(6,'ו'),(5,'ה'),(4,'ד'),(3,'ג'),(2,'ב'),(1,'א')]:
  if n>=v:out+=c;n-=v
 return out

def link(ref):return 'https://www.sefaria.org/'+quote(ref.replace(' ','_'),safe='_:')

def he_ref(r):
 addr=r['ref'][len(r['work'])+1:]
 if r['branch']=='Bavli':
  m=re.fullmatch(r'(\d+)([ab]):(\d+)',addr)
  return r['he_work']+' '+heb(int(m[1]))+' ע״'+('א' if m[2]=='a' else 'ב')+' · קטע '+m[3]
 return r['he_work']+' '+addr

def main():
 review()
 rows=json.loads((P/'review_candidates.json').read_text(encoding='utf-8'))
 decisions=json.loads((P/'review_decisions.json').read_text(encoding='utf-8'))
 selected={d['key'] for d in decisions if d['decision']=='selected_excerpt_review'}
 picked=[r for r in rows if r['key'] in selected]
 broad=json.loads((P/'broad_candidates.json').read_text(encoding='utf-8'))
 # Explicit rebuttals read in full from the retained broad windows.
 extra=[]
 for i in [194,315,340]:
  r=dict(broad[i]);r['review_id']='broad:'+str(i)
  r['review_note']='צורת משא ומתן: הוצגה דעה או ראיה, ונאמר עליה פירוש חלופי או דחייה. אין להסיק שזו מחלוקת שנותרה למסקנה.'
  picked.append(r)
  extra.append({'key':r['key'],'broad_index':i,'ref':r['ref'],'decision':'selected_dialogue_excerpt','reason':r['review_note']})
 (P/'supplemental_decisions.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2),encoding='utf-8')
 grouped=collections.defaultdict(list)
 for r in picked:grouped[r['ref']].append(r)
 entries=[]
 for ref,rs in grouped.items():
  r=rs[0]
  us={u['ref']:u for x in rs for u in x['source_units']}
  units=sorted(us.values(),key=lambda u:u['index'])
  mainunit=next(u for u in units if u['ref']==ref)
  context='\n'.join(u['text'] for u in units)
  notes=['סיווג ראשוני מקריאת ציטוטים; כולל גם הבדלי פירוש וראיות, שאינם בהכרח מחלוקת להלכה.']
  if re.search(r'הדר ביה|הדרו בהו|אי תניא.?תניא',context):
   notes.append('בהקשר מופיעה חזרה מדעה או קבלת ראיה; יש לברר למי היא שייכת ומה נשאר למסקנה.')
  if re.search(r'איפוך|איפכא|תסתיים|איכא דאמרי|לא פליגי|הכי איתמר',context):
   notes.append('בהקשר מופיעים חילוף ייחוס, לשון נוספת או בירור היקף המחלוקת. ההערה אוטומטית ועשויה להתייחס לדיון סמוך.')
  if any(x['review_id']==304 for x in rs):
   notes.append('נדרשת בדיקת נוסח השם: בהקשר המקומי מופיעים גם רבא וגם רבה; לא תוקן נוסח המקור.')
  notes+=list(dict.fromkeys(x['review_note'] for x in rs if 'review_note' in x))
  entries.append({'ref':ref,'he_ref':he_ref(r),'work':r['work'],'he_work':r['he_work'],'branch':r['branch'],
   'status':'dispute','review_level':'first_pass_excerpt','opening':mainunit['text'][:180],
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
  c['title']=c['work'];c['he_title']=c['he_work']
  c['entries']=sum(e['work']==c['work'] for e in entries)
 meta={
  'title':'מחלוקות אביי ורבא — מפתח מקורות', 'date':'2026-11-23',
  'works':len(coverage),'units_scanned':sum(c['units'] for c in coverage),'entries':len(entries),
  'selected_candidates':len(picked),'raw_candidates':len(rows),'broad_windows':len(broad),
  'source_root':'F:/Sefaria-Export-master/json/Talmud',
  'scope':'נסרקו 37 מסכתות הבבלי ו־39 מסכתות הירושלמי במאגר המקומי: גוף התלמוד, ללא פירושים. המפתח הנבחר כולל מופעים בבבלי; בירושלמי לא אותרו זוגות מתאימים בתבניות החיפוש, ואין זו הוכחה לשלילה מוחלטת.',
  'limitations':'מפתח מחקר בסינון ראשוני — לא רשימה סופית ומאומתת של כל המחלוקות. נקראו ציטוטי מועמדים, חלקם בתצוגה מקוצרת; לא נבדקה כל סוגיה במלואה. נכללו דעות שונות, תירוצים, דרשות וראיות חלופיות, ולא רק פסקי דין סותרים. מספר הרשומות הוא מספר מקומות במקור, ולא מספר נושאים ייחודיים: המשך דיון ומקבילות עשויים להופיע שוב. מועמדים אחרים נשמרו לבדיקה.',
  'method':'חיפוש שמות, צירופי אמירה, אזכורים משותפים וסמיכות עד 1,400 תווים; מיון ראשוני וסינון הסכמות, שמות אחרים וחיבור מקרי בין נושאים. אין להחליף בין רבא לרבה, ואין לייחס דעות חד אמר לפי סדר השמות. מראי המקום נגזרו ממערכי המקור, משום שנמצא היסט דף במאגר המנורמל. תגיות, ניקוד וריווח נורמלו; קובצי המקור לא שונו. לכל רשומה נשמרו הפניה, הקשר, נתיב מקור ו־SHA-256.',
  'raw_notice':'1,052 מועמדים בתבניות ו־2,455 חלונות סמיכות, החופפים בחלקם; אין לחבר את המספרים ואין למנות אותם כמחלוקות.'}
 data={'metadata':meta,'entries':entries,'coverage':coverage}
 (P/'abaye_rava_index.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 lines=[meta['title'],'תאריך: '+meta['date'],f"רשומות מראי מקום: {len(entries)}",meta['scope'],meta['limitations'],meta['method'],'']
 for e in entries:
  lines+=['='*70,str(e['id'])+'. '+e['he_ref'],e['ref'],e['link'],'הערות המחקר:']+e['notes']+['לשון המקור וההקשר:']
  for u in e['source_units']:lines+=['['+u['ref']+']',u['text'],'']
 (P/'מחלוקות_אביי_ורבא.txt').write_text('\n'.join(lines),encoding='utf-8-sig')
 # Read the reusable HTML literal only; importing the old builder would rerun old research.
 tree=ast.parse(Path(__file__).with_name('build_rav_shmuel_report.py').read_text(encoding='utf-8'))
 template=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='template' for t in n.targets))
 template=template.replace('רב ושמואל','אביי ורבא').replace('22 בנובמבר','23 בנובמבר').replace('classified_candidates.json','broad_candidates.json')
 template=template.replace('PAYLOAD',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
 (P/'מחלוקות_אביי_ורבא.html').write_text(template,encoding='utf-8')
 # Broad retrieval is an audit appendix, not silently promoted into the selected index.
 selected_refs={e['ref'] for e in entries}
 remaining=[r for r in broad if r['ref'] not in selected_refs]
 (P/'unreviewed_broad_windows.json').write_text(json.dumps({'notice':meta['raw_notice']+' חלונות אלה לא נבחרו למפתח; נדרשת בדיקה.', 'entries':remaining},ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'entries':len(entries),'selected_candidates':len(picked),'tractates_with_entries':len({e['work'] for e in entries}),'remaining_broad_windows':len(remaining)},ensure_ascii=False))

if __name__=='__main__':main()
