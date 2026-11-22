from pathlib import Path
import json,re,html,bisect,collections
ROOT=Path('F:/Sefaria-Export-master/json/Talmud')
OUT=Path(__file__).parent/'rav_shmuel_results'
OUT.mkdir(exist_ok=True)
def plain(t):
 t=re.sub(r'<[^>]+>',' ',t);t=html.unescape(t)
 t=re.sub(r'[\u0591-\u05bd\u05bf-\u05c7]','',t).replace('־',' ').replace('״','"').replace('׳',"'")
 return re.sub(r'\s+',' ',t).strip()
def leaves(a,idx=()):
 if isinstance(a,str):
  if a.strip():yield idx,a
 elif isinstance(a,list):
  for i,x in enumerate(a):yield from leaves(x,idx+(i,))
works=[]
for branch in ['Bavli','Yerushalmi']:
 for p in sorted((ROOT/branch).glob('Seder */*/Hebrew/merged.json')):
  d=json.loads(p.read_text(encoding='utf-8'));units=[]
  for idx,t in leaves(d['text']):
   if branch=='Bavli':addr=f'{idx[0]//2+1}{"ab"[idx[0]%2]}:'+':'.join(str(x+1) for x in idx[1:])
   else:addr=':'.join(str(x+1) for x in idx)
   units.append({'ref':d['title']+' '+addr,'text':plain(t),'raw':t,'index':idx})
  works.append({'title':d['title'],'he':d['heTitle'],'branch':branch,'path':str(p),'units':units})
# Broad retrieval: every explicit joint mention, plus nearby standalone Rav and Shmuel.
joint=re.compile(r'(?<![א-ת])(?:ו?רב ושמואל|ו?שמואל ורב)(?![א-ת])')
rav=re.compile(r'(?<![א-ת])(?:[ודלבכמ]?רב)(?![א-ת])')
shm=re.compile(r'(?<![א-ת])(?:[ודלבכמ]?שמואל)(?![א-ת])')
names=set('יהודה הונא נחמן חסדא יוסף ששת אשי פפא כהנא זביד אבהו אחא חייא יצחק דימי שמן חנן חנינא חננא חמא המנונא מרי אדא עמרם שמואל יעקב אבא עוירא עוירא גידל זירא זעירא יימר ירמיה סחורה שילא שילא עינא אידי חנילאי חלפתא חביבא רבין אבין אחוה שבא תחליפא אחוה אחוה תחליפא מלכיו חננאל אחא מני טבי שמלאי גדא חנה מלכיא עיליש שמשרשיא משרשיא אושעיא חביבא ביבי יכיל חיננא אחוה בריה בר ביזנא סמא יקותי אבימי'.split())
def standalone(text,m,who):
 before=text[max(0,m.start()-18):m.start()]
 after=text[m.end():m.end()+25]
 nxt=re.match(r'\s+([א-ת]+)',after)
 if who=='rav' and nxt and nxt[1] in names:return False
 if who=='shm' and re.match(r'\s+(?:בר|בן)\s',after):return False
 if re.search(r'(?:בי|דבי|רבי|ר\')\s*$',before):return False
 return True
allrows=[];counts=[]
for w in works:
 units=w['units']; offsets=[];chunks=[];pos=0
 for u in units:offsets.append(pos);chunks.append(u['text']);pos+=len(u['text'])+1
 text='\n'.join(chunks)
 rr=[m for m in rav.finditer(text) if standalone(text,m,'rav')]
 ss=[m for m in shm.finditer(text) if standalone(text,m,'shm')]
 seeds=[]
 for m in joint.finditer(text):seeds.append((m.start(),m.end(),'joint'))
 spos=[m.start() for m in ss]
 for m in rr:
  j=bisect.bisect_left(spos,m.start())
  for k in [j-1,j]:
   if 0<=k<len(ss) and abs(ss[k].start()-m.start())<=1000:
    sm=ss[k];seeds.append((min(m.start(),sm.start()),max(m.end(),sm.end()),'near'))
 # Group overlapping pair spans, not unrelated mentions across entire pages.
 groups=[]
 for a,b,why in sorted(seeds):
  if groups and a<=groups[-1][1]:groups[-1][1]=max(b,groups[-1][1]);groups[-1][2].add(why)
  else:groups.append([a,b,{why}])
 for a,b,why in groups:
  i=bisect.bisect_right(offsets,a)-1;j=bisect.bisect_right(offsets,b-1)-1
  lo=max(0,i-1);hi=min(len(units),j+2)
  core=text[a:min(len(text),b+400)]
  row={'id':len(allrows)+1,'work':w['title'],'he_work':w['he'],'branch':w['branch'],'ref':units[i]['ref'],'end_ref':units[j]['ref'],'why':sorted(why),'snippet':core,'units':units[lo:hi],'source_path':w['path'],'hit_start':a,'hit_end':b}
  allrows.append(row)
 counts.append({'title':w['title'],'he_title':w['he'],'branch':w['branch'],'units':len(units),'chars':len(text),'candidates':sum(r['work']==w['title'] for r in allrows),'source_path':w['path']})
(OUT/'candidates.json').write_text(json.dumps(allrows,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'coverage.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2),encoding='utf-8')
print('WORKS',len(works),'UNITS',sum(c['units'] for c in counts),'CANDIDATES',len(allrows),collections.Counter(r['branch'] for r in allrows))
with (OUT/'candidate_review.txt').open('w',encoding='utf-8') as f:
 for r in allrows:f.write(f"{r['id']} | {r['ref']} | {','.join(r['why'])} | {r['snippet'][:750]}\n")
