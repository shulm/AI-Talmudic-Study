exec(open('review_supplements.py',encoding='utf-8-sig').read().split('out=[]')[0])
names.update('חנא חלבו פנחס שימי טובי נהילאי שיזבי חסא טביומי מנשיא ברדלא נחומי שמעיא נחמיה אויא עולא הלל מתנייה חונא חונה הושעיה מתנה מתנא אסי ענן ספרא'.split())
rows=json.loads((p/'remaining.json').read_text(encoding='utf-8'))
out=[]
for r in rows:
 ev=r['evidence'];ms=[]
 for m in pat.finditer(ev):
  who='שמואל' if 'שמואל' in m[0] else 'רב'
  nxt=re.match(r'\s+([א-ת]+)',ev[m.end():])
  if re.search(r'(?:רב|שמואל)$',m[0]) and nxt and (nxt[1] in names if who=='רב' else nxt[1] in {'בר','בן','סבא','אחוה'}):continue
  ms.append((who,m))
 if len(ms)<2 or ms[0][1].start()>5 or ms[0][0]==ms[1][0]:continue
 j=ms[1][1].start()
 r['review']=ev[:90].replace('\n',' ')+' // '+ev[j:j+110].replace('\n',' ')
 out.append(r)
(p/'remaining_filtered.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(out))
for r in out:print(r['id'],r['ref'],r['review'])
