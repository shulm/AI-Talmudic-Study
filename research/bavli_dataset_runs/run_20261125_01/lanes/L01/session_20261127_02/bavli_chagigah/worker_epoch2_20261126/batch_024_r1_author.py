from authoring import *
import json
base=Path(__file__).parent
p=json.loads((base/'batch_024.json').read_text(encoding='utf8'))
for r in p['records']:
 if r['id']=='chg.e2.e24_7':r['content']['relation']='qualification'
runner.immutable(base/'batch_024_r1.json',runner.encoded(p))
