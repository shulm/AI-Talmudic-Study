"""Independent narrow recall probe; does not establish exhaustive coverage."""
import json
import re
from pathlib import Path
from abaye_rava_search import load_works

P = Path(__file__).parent / 'rabbah_yosef_results'

def main():
    selected = {e['ref'] for e in json.loads((P / 'rabbah_yosef_index.json').read_text(encoding='utf8'))['entries']}
    hits = []
    for work in load_works():
        for unit in work['units']:
            text = unit['text']
            if re.search(r'(?<![א-ת])רבה (?:אמר|אומר)(?![א-ת])', text) and re.search(r'רב יוסף (?:אמר|אומר)(?![א-ת])', text):
                hit = {'ref': unit['ref'], 'selected': unit['ref'] in selected}
                if unit['ref'] == 'Eruvin 88a:9':
                    hit['review'] = 'Same ruling, attributed to different teachers; not a dispute between Rabbah and Rav Yosef.'
                hits.append(hit)
    result = {'method': 'Independent within-segment literal רבה אמר/אומר and רב יוסף אמר/אומר; not an exhaustive recall test.', 'hits': hits}
    (P / 'recall_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf8')
    print(f'Recall probe: {len(hits)} hits; {sum(not h["selected"] for h in hits)} not main entries.')

if __name__ == '__main__':
    main()
