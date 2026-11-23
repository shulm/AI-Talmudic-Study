"""Read-only Bavli/Yerushalmi search; aliases preserved verbatim in source quotations."""
import argparse, bisect, collections, json, re
from pathlib import Path
from abaye_rava_search import load_works, record, DEFAULT_ROOT

OUT=Path(__file__).parent/'yochanan_lakish_results'
HON=r'(?:רבי|רב|ר[\x22\x27])\s*'
Y=rf'{HON}יוחנן'
L=rf'(?:{HON}שמעון\s+בן\s+לקיש|ר[\x22\x27]ש\s*בן\s*לקיש|ריש\s+לקיש|בר\s+לקיש|רשב\x22ל|ר\x22ל)'
NAME=re.compile(rf'(?<![א-ת])(?:[ודלבכמש]?)(?P<name>{Y}|{L})(?![א-ת])')
VERB=r'(?:אמר|אומר|אומ[\x27]?|אומרים|סבר|סובר|תני|מתני|מחייב|פוטר|מתיר|אוסר|מכשיר|פוסל|שרי|אסר|פסיל|מכשר|בעי)'

def mentions(text):
 for m in NAME.finditer(text):
  name=m['name'];who='Y' if 'יוחנן' in name else 'L'
  # Exclude other Yohanan figures and patronymics. רבי יוחנן בן נורי is a tanna.
  if who=='Y' and (re.match(r'\s+(?:בן|בר|בריה)\b',text[m.end():]) or re.search(r'(?:בר|בן|בריה ד)\s*$',text[max(0,m.start()-20):m.start()])):continue
  before=text[max(0,m.start()-35):m.start()];after=text[m.end():m.end()+45]
  front=re.match(r'\s*('+VERB+r')(?![א-ת])',after)
  back=re.search(r'(?:אמר|אומר|דאמר|בשם|משום|משמיה ד)\s*$',before)
  yield {'speaker':who,'name':name,'start':m.start(),'end':m.end(),
         'decl':bool(front or back),'forward':bool(front),'verb':front[1] if front else None,
         'ambiguous_alias':name=='ר"ל'}

def scan(root=DEFAULT_ROOT):
 works=load_works(root);rows=[];broad=[];coverage=[]
 for w in works:
  text=w['text'];ms=list(mentions(text));seen=set()
  def add(a,b,kind,dest):
   r=record(w,a['start'],b['end'],kind,[a,b]);r['pair_excerpt']=text[a['start']:min(len(text),b['end']+230)]
   r['alias_warning']=a['ambiguous_alias'] or b['ambiguous_alias']
   dest.append(r)
  for a,b in zip(ms,ms[1:]):
   if a['speaker']==b['speaker'] or b['start']-a['end']>1400:continue
   i=bisect.bisect_right(w['offsets'],a['start'])-1;j=bisect.bisect_right(w['offsets'],b['start'])-1
   if (i,j) not in seen:add(a,b,'nearby_names',broad);seen.add((i,j))
  ds=[m for m in ms if m['decl']]
  for a,b in zip(ds,ds[1:]):
   if a['speaker']==b['speaker'] or b['start']-a['end']>1400:continue
   between=text[a['end']:b['start']]
   if re.search(r"מתני'|משנה:",between):continue
   add(a,b,'declaration_pair',rows)
  for a,b in zip(ms,ms[1:]):
   between=text[a['end']:b['start']]
   if a['speaker']==b['speaker'] or len(between)>18:continue
   after=text[b['end']:b['end']+110]
   if re.search(r'חד (?:אמר|אומר|תני)',after):kind='anonymous_pair'
   elif re.search(r'תרוייהו|תרויהון|תרווייהו|אמרין|אמרי',after[:45]):kind='joint_agreement_candidate'
   elif re.search(r'פליג|מחלוקת',text[max(0,a['start']-80):a['start']]+after):kind='joint_dispute_candidate'
   else:continue
   add(a,b,kind,rows)
  coverage.append({k:w[k] for k in ['work','he_work','branch','source_file','source_sha256']}|{'units':len(w['units']),'y_mentions':sum(m['speaker']=='Y' for m in ms),'l_mentions':sum(m['speaker']=='L' for m in ms),'aliases':dict(collections.Counter(m['name'] for m in ms))})
 for i,r in enumerate(rows,1):
  r['review_id']=i
  a,b=r['anchors'];pos=b['start']-r['start']
  r['review']=r['evidence'][:min(pos,125)].replace('\n',' ')+' // '+r['evidence'][pos:pos+210].replace('\n',' ')
 OUT.mkdir(exist_ok=True)
 for filename,data in [('candidates.json',rows),('broad_candidates.json',broad),('coverage.json',coverage)]:
  (OUT/filename).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'works':len(works),'segments':sum(c['units'] for c in coverage),'candidates':len(rows),'broad':len(broad),'branches':dict(collections.Counter(r['branch'] for r in rows)),'kinds':dict(collections.Counter(r['kind'] for r in rows))},ensure_ascii=False))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--corpus-root',type=Path,default=DEFAULT_ROOT);scan(p.parse_args().corpus_root)
