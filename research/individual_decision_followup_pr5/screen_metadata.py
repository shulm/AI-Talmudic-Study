"""Metadata-only GET helper; never follows file download links or reads responses.
Usage: python screen_metadata.py URL [URL ...]
Only OSF v2 metadata endpoints and GitHub repository metadata are accepted.
"""
import sys,json,hashlib,urllib.request
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent
LOG=ROOT/'admission_http_log.json'
log=json.loads(LOG.read_text()) if LOG.exists() else []
for url in sys.argv[1:]:
 p=urlparse(url)
 assert p.netloc in ('api.osf.io','api.github.com') and '/download' not in p.path
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'bounded-metadata-admission-screen'})
  with urllib.request.urlopen(req,timeout=30) as r:
   raw=r.read(4*1024*1024+1)
  assert len(raw)<=4*1024*1024
  obj=json.loads(raw)
  log.append(dict(url=url,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),kind='metadata',date='2026-11-24'))
  print(url,'BYTES',len(raw))
  if isinstance(obj,dict) and isinstance(obj.get('data'),list):
   for item in obj['data']:
    a=item.get('attributes',{});print(json.dumps({'id':item.get('id'),'attributes':{k:a.get(k) for k in ['name','title','kind','size','materialized_path','current_version','date_modified','extra']},'files':item.get('relationships',{}).get('files',{}).get('links'),'download':item.get('links',{}).get('download')},ensure_ascii=False))
   print('pagination',obj.get('links'))
  else:
   dat=obj.get('data',obj) if isinstance(obj,dict) else obj
   if isinstance(dat,dict) and dat.get('type')=='licenses':print({k:dat['attributes'].get(k) for k in ['name','url']})
   else:print(json.dumps(obj,ensure_ascii=False)[:6000])
 except Exception as e:
  log.append(dict(url=url,error=str(e),bytes=0,kind='metadata_attempt'));print(type(e).__name__,str(e))
 LOG.write_text(json.dumps(log,indent=2)+'\n')
