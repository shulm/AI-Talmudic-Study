from authoring import *
import json
base=Path(__file__).parent
p=json.loads((base/'batch_026.json').read_text(encoding='utf8'))
for r in p['records']:
 if r['id'] in ['chg.e2.q310','chg.e2.q311']:
  r['content']['answer_set_status']='none'
  r['uncertainty'].append('שאלה ללא תשובה מפורשת בהמשך המקומי')
runner.immutable(base/'batch_026_r1.json',runner.encoded(p))
