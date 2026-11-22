from pathlib import Path
import json,re,html,bisect,collections,datetime,urllib.parse
import rav_shmuel_search as s
P=Path('rav_shmuel_results')
rows=json.loads((P/'selected.json').read_text(encoding='utf-8'))
allpairs=json.loads((P/'classified_candidates.json').read_text(encoding='utf-8'))
more={190,402,827,828,1197,1378}
remove={503,1242}
rows=[r for r in rows if r['id'] not in remove]+[r for r in allpairs if r['id'] in more]
for r in rows:r.setdefault('status','dispute')
workmap={w['title']:w for w in s.works}
# Store full source units, including everything traversed by the excerpt.
for w in s.works:
 w['offsets']=[];pos=0
 for u in w['units']:w['offsets'].append(pos);pos+=len(u['text'])+1
def heb(n):
 out=''
 for v,c in [(400,'ת'),(300,'ש'),(200,'ר'),(100,'ק')]:
  while n>=v:out+=c;n-=v
 if n==15:out+='טו';n=0
 if n==16:out+='טז';n=0
 for v,c in [(90,'צ'),(80,'פ'),(70,'ע'),(60,'ס'),(50,'נ'),(40,'מ'),(30,'ל'),(20,'כ'),(10,'י'),(9,'ט'),(8,'ח'),(7,'ז'),(6,'ו'),(5,'ה'),(4,'ד'),(3,'ג'),(2,'ב'),(1,'א')]:
  if n>=v:out+=c;n-=v
 return out
def href(ref):return 'https://www.sefaria.org/'+urllib.parse.quote(ref.replace(' ','_'),safe='_:')
def heref(w,ref):
 addr=ref[len(w['title'])+1:]
 if w['branch']=='Bavli':
  m=re.match(r'(\d+)([ab]):(\d+)',addr)
  return w['he']+' '+heb(int(m[1]))+' ע״'+('א' if m[2]=='a' else 'ב')+' · קטע '+m[3]
 return w['he']+' · פרק '+heb(int(addr.split(':')[0]))+' הלכה '+heb(int(addr.split(':')[1]))+' · קטע '+addr.split(':')[2]
# Additional dialogue-form disputes whose speaker attribution is not an adjacent declaration.
for title, prefix, phrase in [
 ('Sukkah','Sukkah 11a:','צריך לנענע'),
 ('Sukkah','Sukkah 14a:','מחלוקת בנסרין'),
 ('Ketubot','Ketubot 77a:','האומר "איני זן ואיני מפרנס"'),
]:
 w=workmap[title]
 for i,u in enumerate(w['units']):
  if u['ref'].startswith(prefix) and phrase in u['text']:
   endi=min(len(w['units'])-1,i+5)
   ev='\n'.join(x['text'] for x in w['units'][i:endi+1])
   rows.append({'id':2000+len(rows),'work':title,'ref':u['ref'],'start':w['offsets'][i],'end':w['offsets'][endi]+len(w['units'][endi]['text']),'evidence':ev,'status':'dispute'})
   break

# One entry per source segment; different disputes in a segment remain in its quotation.
group={}
for r in rows:
 key=(r['work'],r['ref'])
 group.setdefault(key,[]).append(r)
entries=[]
for (title,ref),rs in group.items():
 w=workmap[title];a=min(r['start'] for r in rs);b=max(r['end'] for r in rs)
 i=bisect.bisect_right(w['offsets'],a)-1;j=bisect.bisect_right(w['offsets'],b-1)-1
 us=w['units'][max(0,i-1):min(len(w['units']),j+2)]
 main=w['units'][i]
 entry={'ref':ref,'he_ref':heref(w,ref),'work':title,'he_work':w['he'],'branch':w['branch'],
 'status':'reconciled' if all(r['status']=='reconciled' for r in rs) else 'dispute',
 'opening':main['text'][:180],'evidence':list(dict.fromkeys(r['evidence'] for r in rs)),
 'source_units':[{'ref':u['ref'],'text':u['text'],'link':href(u['ref'])} for u in us],
 'link':href(ref),'source_file':w['path'],'json_index':main['index'],'candidate_ids':[r['id'] for r in rs]}
 notes=[]
 if any('חד אמר' in r['evidence'][:100] or 'חד תני' in r['evidence'][:100] for r in rs):notes.append('לשון חד אמר: אין לייחס את הדעות לפי סדר השמות; יש לעיין אם ההמשך מזהה את בעלי הדעות.')
 if any(re.search('איפוך|מתני איפכא|איכא דאמרי|הכי איתמר|לא פליגי',r['evidence']) for r in rs):notes.append('בהמשך יש חילוף נוסח, לשון נוספת או בירור היחס בין הדעות. הציטוט הראשון לבדו אינו בהכרח המסקנה.')
 if entry['status']=='reconciled':notes.append('הבדל שנדון או יושב בסוגיה; אין למנות אוטומטית כמחלוקת מסקנתית.')
 entry['notes']=notes
 entries.append(entry)
order={'Zeraim':0,'Moed':1,'Nashim':2,'Nezikin':3,'Kodashim':4,'Tahorot':5}
def sortkey(e):
 w=workmap[e['work']];sed=next((v for k,v in order.items() if 'Seder '+k in w['path']),9)
 return (0 if e['branch']=='Bavli' else 1,sed,e['he_work'],e['json_index'])
entries.sort(key=sortkey)
for i,e in enumerate(entries,1):e['id']=i
coverage=json.loads((P/'coverage.json').read_text(encoding='utf-8'))
for c in coverage:
 c['entries']=sum(e['work']==c['title'] for e in entries)
 c['dispute_entries']=sum(e['work']==c['title'] and e['status']=='dispute' for e in entries)
meta={'title':'מחלוקות רב ושמואל — מפתח מקורות בבבלי ובירושלמי','date':'2026-11-22','works':len(coverage),'units_scanned':sum(c['units'] for c in coverage),'entries':len(entries),'source_root':str(s.ROOT),
 'scope':'סריקה של כל 37 מסכתות הבבלי ו־39 מסכתות הירושלמי שבמהדורת המקור המקומית; גוף התלמוד בלבד. כולל הלכה, אגדה, פירוש ונוסח.',
 'limitations':'זהו מפתח מופעים שנמצאו בסריקה ובמיון ראשוני, ולא מהדורה ביקורתית או הבטחה למיצוי כל מחלוקת עקיפה. נבדקו ציטוטי המועמדים; לא נעשה עיון מלא בכל סוגיה מתחילתה ועד סופה. מספר הרשומות אינו מספר המחלוקות הייחודיות: סוגיה עשויה להופיע בכמה רשומות ובכמה מסכתות, ורשומה אחת עשויה לכלול יותר ממחלוקת אחת.',
 'method':'חיפוש שמות וצירופי אמירה, חד אמר, והופעות סמוכות; מיון ציטוטים והסרת הסכמות, שמות של אמוראים אחרים, ואזכורים בלתי קשורים. מראי המקום חושבו ממבנה קובצי המקור, עקב היסט במספור הדפים במאגר המנורמל. הבבלי לפי דף ועמוד; הירושלמי לפי פרק, הלכה וקטע. הוסרו תגיות עיצוב וניקוד; לא נעשה שינוי תוכני מכוון.',
 'raw_notice':'פלט הסריקה הגולמי מכיל מועמדים בלבד, לרבות הסכמות, שמות דומים וסמיכות מקרית. אין לספור אותו כרשימת מחלוקות.'}
data={'metadata':meta,'entries':entries,'coverage':coverage}
(P/'rav_shmuel_index.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
lines=[meta['title'],'תאריך: '+meta['date'],meta['scope'],meta['limitations'],meta['method'],'']
for e in entries:
 lines+=['='*70,str(e['id'])+'. '+e['he_ref'],e['ref'],e['link']]
 lines+=e['notes']
 lines+=['לשון הגמרא וההקשר:']
 for u in e['source_units']:lines+=['['+u['ref']+']',u['text'],'']
(P/'מחלוקות_רב_ושמואל.txt').write_text('\n'.join(lines),encoding='utf-8-sig')
payload=json.dumps(data,ensure_ascii=False).replace('</','<\/')
template='''<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>מחלוקות רב ושמואל</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f4f1e9;color:#242a30;font:18px/1.75 Arial,sans-serif}header,main{max-width:1100px;margin:auto;padding:24px}header{padding-top:44px}h1{font-size:36px;margin:0}h2{font-size:23px;margin:0 0 10px}p{margin:10px 0}.muted{color:#5c6268;font-size:15px}.stats{display:flex;gap:16px;flex-wrap:wrap}.stat{background:#fff;padding:12px 22px;border:1px solid #d9d4c7;border-radius:8px}.stat strong{font-size:27px;color:#225c58}.filters{position:sticky;top:0;background:#f4f1e9f5;padding:14px 0;z-index:2;display:flex;flex-wrap:wrap;gap:10px}input,select,button{font:inherit;border:1px solid #aaa;border-radius:5px;padding:9px;background:white}input{flex:1;min-width:240px}button{cursor:pointer;color:#225c58}article{background:white;border:1px solid #d9d4c7;border-right:5px solid #39716b;padding:22px;margin:18px 0;border-radius:6px}a{color:#225c58}.quote{font-family:"Times New Roman",serif;font-size:23px;white-space:pre-wrap;line-height:1.9}.tag{display:inline-block;background:#e9efeb;color:#225c58;padding:2px 10px;border-radius:5px;font-size:14px}.note{background:#fcf6de;padding:8px 14px;font-size:16px}summary{cursor:pointer;font-weight:bold}details{margin:12px 0}table{border-collapse:collapse;width:100%;font-size:16px}td,th{padding:6px;border-bottom:1px solid #ddd;text-align:right}.page{display:flex;align-items:center;gap:12px;margin:20px 0}code{font-size:13px;word-break:break-all}.source{padding-top:14px;border-top:1px solid #eee;margin-top:14px}footer{margin:28px 0;font-size:15px}@media print{.filters,.page,button{display:none}article{break-inside:avoid}header,main{max-width:none;padding:8px}body{background:white}}
</style><header><p class="muted">ספריית מקורות ללימוד • 22 בנובמבר 2026</p><h1>מחלוקות רב ושמואל</h1><p>מפתח מקורות בתלמוד הבבלי ובתלמוד הירושלמי</p><div class="stats" id="stats"></div><p id="scope"></p><p class="note" id="limits"></p><details><summary>היקף החיפוש ושיטת העבודה</summary><p id="method"></p><p>לצד מחלוקות בדין נכללו הבדלי פירוש, אגדה ונוסח. נשמרו מקבילות וחזרות, וכן חילופי ייחוס המופיעים בגמרא. הציטוטים כוללים הקשר ולעיתים גם נושאים סמוכים.</p><p>המקור: קובצי Hebrew/merged.json המקומיים של Sefaria Export. ההפניות המקוונות ניתנות לעיון, ואין הכרח שהמהדורה באתר תהיה זהה לקובץ המקומי.</p><p>לצורך ביקורת נוספת נשמרו באותה תיקייה candidates.json ו־classified_candidates.json. אלו פלטי חיפוש גולמיים, ולא רשימות מחלוקות מאומתות.</p></details><details><summary>כיסוי המסכתות</summary><table><thead><tr><th>תלמוד</th><th>מסכת</th><th>קטעי מקור שנסרקו</th><th>רשומות במפתח</th></tr></thead><tbody id="coverage"></tbody></table><p class="muted">אפס רשומות פירושו שלא סווג מופע למפתח זה; אינו הוכחה שאין מחלוקת במסכת.</p></details></header>
<main><div class="filters"><input id="q" aria-label="חיפוש" placeholder="חיפוש בציטוטים או במראי המקום"><select id="branch" aria-label="תלמוד"><option value="">שני התלמודים</option value="Bavli">בבלי</option><option value="Yerushalmi">ירושלמי</option></select><select id="work" aria-label="מסכת"><option value="">כל המסכתות</option></select><select id="status" aria-label="סוג"><option value="">כל סוגי הרשומות</option value="dispute">מופעי מחלוקת והבדלי דעות</option value="reconciled">בירור או יישוב ההבדל</option></select></div><p class="muted" id="count"></p><div class="page"><button id="prev">הקודם</button><span id="page"></span><button id="next">הבא</button><button id="all">הצג הכל / הדפסה</button></div><div id="results"></div><footer>קובץ מקומי עצמאי: החיפוש פועל ללא אינטרנט. קישורי המקורות נפתחים באתר ספריא.</footer></main>
<script id="data" type="application/json">PAYLOAD</script><script>
const D=JSON.parse(document.querySelector('#data').textContent),$=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
$('scope').textContent=D.metadata.scope;$('limits').textContent=D.metadata.limitations;$('method').textContent=D.metadata.method;
$('stats').innerHTML=[['מסכתות שנסרקו',D.metadata.works],['קטעי מקור',D.metadata.units_scanned.toLocaleString('he')],['רשומות במפתח',D.entries.length]].map(([t,n])=>'<div class="stat"><strong>'+n+'</strong><br>'+t+'</div>').join('');
$('coverage').innerHTML=D.coverage.map(c=>'<tr><td>'+(c.branch==='Bavli'?'בבלי':'ירושלמי')+'</td><td>'+esc(c.he_title)+'</td><td>'+c.units+'</td><td>'+c.entries+'</td></tr>').join('');
const works=[...new Map(D.entries.map(e=>[e.work,e.he_work])).entries()];
$('work').innerHTML+=[...works].sort((a,b)=>a[1].localeCompare(b[1],'he')).map(([v,t])=>'<option value="'+esc(v)+'">'+esc(t)+'</option>').join('');
const clean=s=>s.toLowerCase().replace(/[\u0591-\u05c7"׳״']/g,'');
D.entries.forEach(e=>e.search=clean(e.he_ref+' '+e.ref+' '+e.source_units.map(u=>u.text).join(' ')));
let page=0,size=25,filtered=[];
function render(reset=false){if(reset)page=0;const q=clean($('q').value.trim());filtered=D.entries.filter(e=>(!q||q.split(/\s+/).every(t=>e.search.includes(t)))&&(!$('branch').value||e.branch===$('branch').value)&&(!$('work').value||e.work===$('work').value)&&(!$('status').value||e.status===$('status').value));const pages=Math.max(1,Math.ceil(filtered.length/size));page=Math.max(0,Math.min(page,pages-1));$('count').textContent=filtered.length+' רשומות תואמות מתוך '+D.entries.length;$('page').textContent='עמוד '+(page+1)+' מתוך '+pages;$('prev').disabled=page===0;$('next').disabled=page>=pages-1;
$('results').innerHTML=filtered.slice(page*size,(page+1)*size).map(e=>'<article><span class="tag">'+(e.branch==='Bavli'?'בבלי':'ירושלמי')+' · רשומה '+e.id+'</span><h2><a href="'+esc(e.link)+'" target="_blank" rel="noopener">'+esc(e.he_ref)+'</a></h2><p class="muted" dir="ltr" style="text-align:right">'+esc(e.ref)+'</p>'+e.notes.map(n=>'<p class="note">'+esc(n)+'</p>').join('')+'<p><strong>פתיחת קטע המקור:</strong> '+esc(e.opening)+'…</p><div class="quote">'+esc(e.evidence[0])+'</div><details><summary>הצג את קטעי המקור המלאים וההקשר</summary>'+e.source_units.map(u=>'<div class="source"><a href="'+esc(u.link)+'" target="_blank" rel="noopener" dir="ltr">'+esc(u.ref)+'</a><div class="quote">'+esc(u.text)+'</div></div>').join('')+'</details><details><summary>פרטי המקור המקומי</summary><code dir="ltr">'+esc(e.source_file)+'</code><p class="muted">כתובת במערך המקור, בסיס אפס: '+esc(e.json_index.join(' / '))+'</p></details></article>').join('');}
['q','branch','work','status'].forEach(id=>$(id).addEventListener(id==='q'?'input':'change',()=>render(true)));
$('prev').onclick=()=>{page--;render()};$('next').onclick=()=>{page++;render()};$('all').onclick=()=>{size=D.entries.length;render(true)};render();
</script></html>'''
(P/'מחלוקות_רב_ושמואל.html').write_text(template.replace('PAYLOAD',payload),encoding='utf-8')
print(json.dumps({'entries':len(entries),'branches':dict(collections.Counter(e['branch'] for e in entries)),'statuses':dict(collections.Counter(e['status'] for e in entries))},ensure_ascii=False))
