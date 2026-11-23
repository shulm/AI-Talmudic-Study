"""Independent raw-array address and quotation checks, not scholarly certification."""
import hashlib
import html
import json
import re
from pathlib import Path
P=Path(__file__).parent/'yochanan_lakish_results'
def clean(s):
 s=html.unescape(re.sub('<[^>]+>',' ',s))
 s=re.sub('[\u0591-\u05bd\u05bf-\u05c7]','',s)
 return ' '.join(s.replace('־',' ').replace('״','"').replace('׳',"'").split())
def address(ref,title,branch):
 a=ref[len(title)+1:]
 if branch=='Bavli':
  m=re.fullmatch(r'(\d+)([ab]):(\d+)',a)
  return [(int(m[1])-1)*2+(m[2]=='b'),int(m[3])-1]
 return [int(i)-1 for i in a.split(':')]
def leaf(tree,idx):
 for i in idx:tree=tree[i]
 return clean(tree)
def main():
 d=json.loads((P/'yochanan_lakish_index.json').read_text(encoding='utf-8'))
 sources={};checked=0
 for e in d['entries']:
  p=e['source_file']
  if p not in sources:
   raw=Path(p).read_bytes();sources[p]=(json.loads(raw),hashlib.sha256(raw).hexdigest())
  raw,digest=sources[p]
  assert raw['title']==e['work'] and digest==e['source_sha256'],e['ref']
  assert address(e['ref'],e['work'],e['branch'])==e['json_index'],e['ref']
  main=leaf(raw['text'],e['json_index'])
  assert e['opening']==main[:180],e['ref']
  for u in e['source_units']:
   assert leaf(raw['text'],address(u['ref'],e['work'],e['branch']))==u['text'],u['ref']
   checked+=1
  combined='\n'.join(u['text'] for u in e['source_units'])
  for evidence in e['evidence']:assert evidence in combined,e['ref']
 assert len({e['ref'] for e in d['entries']})==len(d['entries'])==d['metadata']['entries']
 assert len(d['coverage'])==76 and sum(c['units'] for c in d['coverage'])==94045
 # Niddah 3b contrasts Hezekiah with Yohanan, not Resh Lakish.
 assert not any(e['ref'].startswith('Niddah 3b:') for e in d['entries'])
 for probe in ['Yoma 74a','Bava Kamma 22a','Bava Metzia 47b','Gittin 47b','Niddah 24a','Jerusalem Talmud Nedarim 11:1','Eruvin 8b','Menachot 54a']:
  assert any(e['ref'].startswith(probe+':') for e in d['entries']),probe
 print(f'PASS: {len(d["entries"])} entries, {checked} context quotations, raw-array references, hashes and coverage probes. Not a completeness or dispute-classification check.')
if __name__=='__main__':main()
