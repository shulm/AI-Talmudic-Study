import rav_shmuel_search as search
from rav_shmuel_search import *
# Extraction independent of broad candidate grouping: a separate record for each declaration pair.
decl_verbs=r'(?:אמר|אומר|אוסר|אוס[רי]|מתיר|מתי[רי]|מחייב|פוטר|סבר|תני|שרי|אסר|מצלי|פסל|מכשר|מחשר|כרבי|כרבנן|כרב|מוקים|תני|בעי|עבד|הוה)'
rd=re.compile(r'(?<![א-ת])(?:[וד]?רב\s+'+decl_verbs+r'\b|(?:אמר|דאמר|בשם|משמיה ד)\s*רב(?![א-ת]))')
sd=re.compile(r'(?<![א-ת])(?:[וד]?שמואל\s+'+decl_verbs+r'\b|(?:אמר|דאמר|בשם|משמיה ד)\s*שמואל(?![א-ת]))')
records=[]
for w in works:
 units=w['units'];offsets=[];pos=0
 for u in units:offsets.append(pos);pos+=len(u['text'])+1
 text='\n'.join(u['text'] for u in units)
 events=[]
 for who,pattern in [('רב',rd),('שמואל',sd)]:
  for m in pattern.finditer(text):
   end=text[m.end():m.end()+30]
   if who=='רב' and re.search(r'רב$',m[0]) and re.match(r'\s+(?:'+'|'.join(names)+r')(?:\s|[,.:])',end):continue
   if who=='שמואל' and re.search(r'שמואל$',m[0]) and re.match(r'\s+(?:בר|בן)\s',end):continue
   events.append((m.start(),m.end(),who))
 events.sort()
 hits=[]
 for a,b in zip(events,events[1:]):
  if a[2]!=b[2] and b[0]-a[1]<=850:
   hits.append((a[0],b[1],'paired',a[2],b[2]))
 for m in joint.finditer(text):
  aft=text[m.end():m.end()+160]
  if re.match(r'[\s,.:]*(?:חד (?:אמר|תני)|רב (?:אמר|כרבי|כרבנן)|שמואל אמר)',aft):
   hits.append((m.start(),m.end(),'anonymous','',''))
  elif re.search(r'(?:פליג|נחלק|אתפלג|איתפלג)',text[max(0,m.start()-55):m.start()]):
   hits.append((m.start(),m.end(),'explicit_mention','',''))
 for a,b,kind,first,second in sorted(hits):
  i=bisect.bisect_right(offsets,a)-1;j=bisect.bisect_right(offsets,b-1)-1
  # Main evidence includes full second statement and any same-unit continuation.
  lo=max(0,i-1);hi=min(len(units),j+2)
  evend=max(offsets[j]+len(units[j]['text']),min(len(text),b+280))
  if kind=='anonymous':evend=min(len(text),max(evend,a+700))
  evidence=text[a:evend]
  # Prevent overlapping records for the very same statements, but retain different topics.
  if records and records[-1]['work']==w['title'] and records[-1]['start']==a:continue
  records.append({'id':len(records)+1,'work':w['title'],'he_work':w['he'],'branch':w['branch'],'ref':units[i]['ref'],'end_ref':units[j]['ref'],'kind':kind,'first':first,'second':second,'start':a,'end':evend,'evidence':evidence,'context':[{'ref':u['ref'],'text':u['text']} for u in units[lo:hi]],'source_path':w['path'],'json_index':units[i]['index']})
(OUT/'classified_candidates.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('PAIRS',len(records),collections.Counter(r['kind'] for r in records))
for r in records:
 s=r['evidence'].replace('\n',' ')
 print(r['id'],r['ref'],r['kind'],s[:200])
