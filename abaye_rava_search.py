"""Read-only corpus scan. Run explicitly; importing this module does not write files."""
from pathlib import Path
import argparse
import bisect
import collections
import hashlib
import html
import json
import re

OUT = Path(__file__).parent / 'abaye_rava_results'
DEFAULT_ROOT = Path('F:/Sefaria-Export-master/json/Talmud')


def plain(text):
    text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
    text = re.sub(r'[\u0591-\u05bd\u05bf-\u05c7]', '', text)
    return re.sub(r'\s+', ' ', text.replace('־', ' ').replace('״', '"').replace('׳', "'")).strip()


def leaves(value, index=()):
    if isinstance(value, str):
        if value.strip():
            yield index, value
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from leaves(child, index + (i,))


def load_works(root=DEFAULT_ROOT):
    works = []
    for branch in ['Bavli', 'Yerushalmi']:
        for path in sorted((root / branch).glob('Seder */*/Hebrew/merged.json')):
            source = path.read_bytes()
            data = json.loads(source)
            units, offsets, pos = [], [], 0
            for idx, raw in leaves(data['text']):
                if branch == 'Bavli':
                    addr = f'{idx[0] // 2 + 1}{"ab"[idx[0] % 2]}:' + ':'.join(str(i + 1) for i in idx[1:])
                else:
                    addr = ':'.join(str(i + 1) for i in idx)
                text = plain(raw)
                offsets.append(pos)
                units.append({'ref': data['title'] + ' ' + addr, 'index': idx, 'text': text})
                pos += len(text) + 1
            works.append({'work': data['title'], 'he_work': data['heTitle'], 'branch': branch,
                          'source_file': str(path), 'source_sha256': hashlib.sha256(source).hexdigest(),
                          'units': units, 'offsets': offsets, 'text': '\n'.join(u['text'] for u in units)})
    return works


NAME = re.compile(r'(?<![א-ת])(?:[ודלבכמש]?)(אביי|רבא)(?![א-ת])')
VERBS = r'(?:אמר|אומר|סבר|סובר|שרי|אסר|מתיר|אוסר|מחייב|פוטר|מכשיר|פוסל|פסיל|מחשר|מכשר|תני|מתני|מתרץ|מוקי|מוקים|מצלי|עביד|בעי|מפרש)'
DECL = re.compile(r'(?<![א-ת])(?:[וד]?(?P<front>אביי|רבא)\s+(?P<verb>' + VERBS + r')\b|(?:ו?אמר|דאמר|בשם|משמיה ד)\s*(?P<back>אביי|רבא)(?![א-ת]))')
JOINT = re.compile(r'(?<![א-ת])(?:אביי ורבא|רבא ואביי)(?![א-ת])')


def valid_name(text, start, end):
    # Rava bar ... and "Rav/Rabbi ... rava" are not silently identified as Rava.
    return not re.match(r'\s+(?:בר|בן|בריה)\b', text[end:]) and not re.search(r'(?:רבי|רב|ר\')\s*$', text[max(0, start-15):start])


def record(w, start, end, kind, anchors=None):
    i = bisect.bisect_right(w['offsets'], start)-1
    j = bisect.bisect_right(w['offsets'], end-1)-1
    # Retain complete source segments; never cut the second speaker's statement mid-unit.
    lo, hi = max(0, i-1), min(len(w['units']), j+3)
    evidence_end = w['offsets'][hi-1] + len(w['units'][hi-1]['text'])
    return {'key': hashlib.sha256(f"{w['work']}:{start}:{end}:{kind}".encode()).hexdigest()[:16],
            'work': w['work'], 'he_work': w['he_work'], 'branch': w['branch'],
            'ref': w['units'][i]['ref'], 'end_ref': w['units'][j]['ref'],
            'start': start, 'end': end, 'kind': kind, 'anchors': anchors or [],
            'evidence': w['text'][start:evidence_end], 'source_units': w['units'][lo:hi],
            'source_file': w['source_file'], 'source_sha256': w['source_sha256'],
            'json_index': w['units'][i]['index']}


def scan(root=DEFAULT_ROOT):
    works = load_works(root)
    candidates, broad, coverage = [], [], []
    for w in works:
        text = w['text']
        mentions = [m for m in NAME.finditer(text) if valid_name(text, m.start(), m.end())]
        pairs = {}
        for a, b in zip(mentions, mentions[1:]):
            if a[1] != b[1] and b.start()-a.end() <= 1400:
                i = bisect.bisect_right(w['offsets'], a.start())-1
                j = bisect.bisect_right(w['offsets'], b.start())-1
                pairs.setdefault((i,j), (a.start(), b.end()))
        for a,b in pairs.values():
            broad.append(record(w,a,b,'nearby_names'))
        events = []
        for m in DECL.finditer(text):
            who = m['front'] or m['back']
            name_start = m.start('front' if m['front'] else 'back')
            name_end = name_start+len(who)
            if valid_name(text,name_start,name_end):
                events.append((m.start(),m.end(),who,m['verb'],m[0]))
        for a,b in zip(events,events[1:]):
            if a[2] == b[2] or b[0]-a[1]>1100:
                continue
            between=text[a[1]:b[0]]
            if re.search(r"מתני'|משנה:",between):
                continue
            kind='direct_pair' if b[3] and a[3] not in {'בעי','מצלי','עביד'} and b[3] not in {'בעי','מצלי','עביד'} else 'declaration_pair'
            candidates.append(record(w,a[0],b[1],kind,[{'speaker':a[2],'offset':a[0],'form':a[4]}, {'speaker':b[2],'offset':b[0],'form':b[4]}]))
        for m in JOINT.finditer(text):
            after=text[m.end():m.end()+160]
            before=text[max(0,m.start()-100):m.start()]
            kind='joint_mention'
            if re.match(r'[\s,.:;—–-]*חד (?:אמר|תני)',after):
                kind='anonymous_pair'
            elif re.search(r'(?:פליגי|איפליגו|איתפלגון|מחלוקת)',before):
                kind='explicit_disagreement'
            elif re.search(r'(?:תרוייהו|תרווייהו|תרויהון|תריהון)',after[:60]):
                kind='agreement'
            candidates.append(record(w,m.start(),m.end(),kind))
        coverage.append({k:w[k] for k in ['work','he_work','branch','source_file','source_sha256']} | {
            'units':len(w['units']), 'abaye_mentions':sum(m[1]=='אביי' for m in mentions),
            'rava_mentions':sum(m[1]=='רבא' for m in mentions),
            'candidates':sum(r['work']==w['work'] for r in candidates)})
    OUT.mkdir(exist_ok=True)
    for name, data in [('candidates.json',candidates),('broad_candidates.json',broad),('coverage.json',coverage)]:
        (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'works':len(works),'segments':sum(c['units'] for c in coverage),'candidates':len(candidates),
                      'broad_windows':len(broad),'kinds':dict(collections.Counter(r['kind'] for r in candidates)),
                      'branches':dict(collections.Counter(r['branch'] for r in candidates))},ensure_ascii=False))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--corpus-root',type=Path,default=DEFAULT_ROOT)
    scan(parser.parse_args().corpus_root)
