from authoring import *
import json
base=Path(__file__).parent
p=json.loads((base/'batch_023.json').read_text(encoding='utf8'))
for r in p['records']:
 if r['id']=='chg.e2.colophon2':r['origin']='literal'
runner.immutable(base/'batch_023_r1.json',runner.encoded(p))
