"""Deterministic source handling. Semantic decisions are separately authored, never inferred by regex."""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
DEFAULT=Path('F:/Sefaria-Export-master')
VERSION='Wikisource Talmud Bavli'
PILOTS={'Berakhot':(2,8),'Bava Metzia':(40,43)} # inclusive zero-based pages
TABLES=('segments','sugyot','scholars','statements','questions','positions','relations','review_queue')
def sha(data):return hashlib.sha256(data).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def jsonl(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows),encoding='utf-8',newline='\n')
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()]
def stable(kind,*parts):return kind+'_'+sha('|'.join(parts).encode())[:20]
def address(work,i,j):return f'{work} {i//2+1}{"a" if i%2==0 else "b"}:{j+1}'
def plain(s):return html.unescape(re.sub('<[^>]*>','',s)) # display only; original is untouched
def toc_leaves(nodes):
    for n in nodes:
        if 'contents' in n:yield from toc_leaves(n['contents'])
        elif n.get('categories',[])[:2]==['Talmud','Bavli'] and len(n['categories'])==3 and n['categories'][2].startswith('Seder '):yield n
def inventory(root):
    toc=root/'table_of_contents.json';tractates=[]
    for ordinal,n in enumerate(toc_leaves(read(toc)),1):
        rel=Path('json').joinpath(*n['categories'],n['title'],'Hebrew',VERSION+'.json');p=root/rel
        if not p.exists():raise FileNotFoundError(f'Named edition absent: {p}; no silent merged fallback')
        d=read(p);assert d['title']==n['title'] and d['language']=='he'
        assert all(isinstance(page,list) and all(isinstance(s,str) for s in page) for page in d['text'])
        schema_rel=Path('schemas')/(n['title'].replace(' ','_')+'.json');sp=root/schema_rel
        schema=read(sp);assert schema['schema']['addressTypes']==['Talmud','Integer']
        tractates.append(dict(ordinal=ordinal,title=n['title'],he_title=n.get('heTitle'),categories=n['categories'],source_path=rel.as_posix(),source_sha256=sha(p.read_bytes()),schema_path=schema_rel.as_posix(),schema_sha256=sha(sp.read_bytes()),metadata={k:v for k,v in d.items() if k!='text'},page_slots=len(d['text']),source_segments=sum(len(x) for x in d['text']),nonempty_segments=sum(bool(x) for p in d['text'] for x in p),empty_page_indices=[i for i,p in enumerate(d['text']) if not p],first_nonempty_ref=next((address(n['title'],i,j) for i,p in enumerate(d['text']) for j,s in enumerate(p) if s),None)))
    manifest=dict(schema_version='1.0.0',source_root_hint=str(root),source_toc_path='table_of_contents.json',source_toc_sha256=sha(toc.read_bytes()),source_release_note='Local export snapshot pinned by bytes; not claimed to be an upstream Git revision.',edition=VERSION,tractates=tractates)
    write(HERE/'source_manifest.json',manifest);return manifest
def extract(root,manifest):
    segments=[];context=[];windows=[]
    for m in manifest['tractates']:
        if m['title'] not in PILOTS:continue
        d=read(root/m['source_path']);lo,hi=PILOTS[m['title']]
        for i in range(max(0,lo-1),min(len(d['text']),hi+2)):
            for j,text in enumerate(d['text'][i]):
                ref=address(m['title'],i,j);r=dict(schema_version='1.0.0',id=stable('seg',m['title'],VERSION,str(i),str(j)),tractate=m['title'],ref=ref,source_index=[i,j],text=text,text_sha256=sha(text.encode()),source_sha256=m['source_sha256'],version_title=VERSION,scope='pilot' if lo<=i<=hi else 'context_only')
                (segments if r['scope']=='pilot' else context).append(r)
        ordered=sorted([r for r in segments+context if r['tractate']==m['title']],key=lambda r:r['source_index'])
        # Segment boundaries are not sugya boundaries. Context windows only guide reading.
        start=0
        while start<len(ordered):
            end=start;size=0
            while end<len(ordered) and end-start<10 and (size+len(ordered[end]['text'])<=8000 or end==start):size+=len(ordered[end]['text']);end+=1
            selected=ordered[start:end]
            windows.append(dict(id=stable('win',m['title'],selected[0]['id'],selected[-1]['id']),tractate=m['title'],segment_ids=[r['id'] for r in selected],start_ref=selected[0]['ref'],end_ref=selected[-1]['ref'],characters=size,oversized_atomic_segment=size>8000,role='reading_context_not_semantic_segmentation'))
            if end==len(ordered):break
            start=max(start+1,end-2)
    jsonl(HERE/'data/segments.jsonl',segments);jsonl(HERE/'context/segments.jsonl',context);jsonl(HERE/'context/windows.jsonl',windows)
    return segments
def build(root):
    m=inventory(root);ss=extract(root,m)
    print(json.dumps(dict(tractates=len(m['tractates']),inventory_segments=sum(x['source_segments'] for x in m['tractates']),pilot_segments=len(ss),context_segments=len(rows(HERE/'context/segments.jsonl')),windows=len(rows(HERE/'context/windows.jsonl')))))
def show(work,start,end):
    for r in sorted(rows(HERE/'data/segments.jsonl')+rows(HERE/'context/segments.jsonl'),key=lambda r:(r['tractate'],r['source_index'])):
        if r['tractate']==work and start<=r['source_index'][0]<=end:print(r['ref']+' '+plain(r['text']))
if __name__=='__main__':
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True);b=sub.add_parser('build');b.add_argument('--source-root',type=Path,default=DEFAULT);s=sub.add_parser('show');s.add_argument('tractate');s.add_argument('start',type=int);s.add_argument('end',type=int);a=p.parse_args()
    if a.cmd=='build':build(a.source_root)
    else:show(a.tractate,a.start,a.end)
