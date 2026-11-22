import json,re
from pathlib import Path
p=Path('rav_shmuel_results')
a=json.loads((p/'classified_candidates.json').read_text(encoding='utf-8'))
strong={r['id'] for r in json.loads((p/'strong.json').read_text(encoding='utf-8'))}
verbs=r'(?:אמר|אומר|אוסר|אוס[רי]|מתיר|מתי[רי]|מחייב|פוטר|סבר|תני|שרי|אסר|מצלי|פסל|מכשר|מחשר|כרבי|כרבנן|כרב|מוקים|בעי|עבד|הוה)'
names=set('יהודה הונא נחמן חסדא יוסף ששת אשי פפא כהנא זביד אבהו אחא חייא יצחק דימי שמן חנן חנינא חננא חמא המנונא מרי אדא עמרם שמואל יעקב אבא עוירא גידל זירא זעירא יימר ירמיה סחורה שילא עינא אידי חנילאי חלפתא חביבא רבין אבין שבא תחליפא מלכיו חננאל מני טבי שמלאי גדא חנה מלכיא עיליש משרשיא אושעיא ביבי יכיל חיננא בריה בר ביזנא סמא יקותי אבימי אסי מתנא ענן ספרא הושעיא שרביא נתן עוקבא זוטרא מתנה עילאי שישא'.split())
pat=re.compile(r'(?<![א-ת])(?:[וד]?(?:רב|שמואל)\s+'+verbs+r'\b|(?:אמר|דאמר|בשם|משמיה ד)\s*(?:רב|שמואל)(?![א-ת]))')
out=[]
for r in a:
 if r['id'] in strong:continue
 ev=r['evidence']
 events=[]
 for m in pat.finditer(ev):
  who='שמואל' if 'שמואל' in m[0] else 'רב'
  if re.search(r'(?:רב|שמואל)$',m[0]):
   nxt=re.match(r'\s+([א-ת]+)',ev[m.end():])
   if nxt and (nxt[1] in names if who=='רב' else nxt[1] in {'בר','בן'}):continue
  if re.search(r'(?:בי|רבי)\s*$',ev[max(0,m.start()-8):m.start()]):continue
  events.append((who,m.start(),m.end()))
 if len(events)<2 or events[0][1]>5:continue
 x,y=events[:2]
 if x[0]==y[0] or y[1]>500:continue
 if re.search(r"מתני'|משנה:",ev[:y[1]]):continue
 r['review']=ev[:min(y[1],100)].replace('\n',' ')+' // '+ev[y[1]:y[1]+115].replace('\n',' ')
 out.append(r)
(p/'supplements.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(out))
for r in out[:100]:print(r['id'],r['ref'],r['review'])
