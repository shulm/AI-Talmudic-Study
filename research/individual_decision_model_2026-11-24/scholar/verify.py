"""Mechanical provenance and boundary checks, not scholarly certification."""
import collections, json, re
from pathlib import Path
from prepare import HERE, ROOT, sha, clean
def read(name): return [json.loads(l) for l in (HERE/name).read_text(encoding='utf8').splitlines()]
def main():
    contexts=read('evidence_context.jsonl'); records=read('evidence_records.jsonl'); inputs=read('prediction_inputs.jsonl')
    assert len(contexts)==len(records)==32
    assert len({r['attempt_id'] for r in records})==32
    assert len({r['family_id'] for r in records})==30
    assert sha((HERE/'second_review.jsonl').read_bytes())=='df45928a843dfe445d469eac184ae1569bfd02047467fa482affbc803e3de7cf'
    second={r['attempt_id']:r for r in read('second_review.jsonl')}
    assert len(second)==32
    for r in records: assert r['review_level']=='ai_independent_double'
    def eligibility_agreement(first, limit=32):
        selected=[r for r in first if int(r['attempt_id'][2:])<=limit]
        return sum((r['initial_eligibility']=='provisional_usable')==second[r['attempt_id']]['status'].startswith('eligible') for r in selected),len(selected)
    assert eligibility_agreement(read('initial_reviews_round1.jsonl'),30)==(28,30)
    assert eligibility_agreement(read('initial_reviews_round1.jsonl'))==(29,32)
    assert eligibility_agreement(read('initial_reviews.jsonl'))==(30,32)
    raw={}
    for d in contexts:
        p=Path(d['source_file'])
        if str(p) not in raw:
            b=p.read_bytes(); raw[str(p)]=(sha(b),json.loads(b))
        h,source=raw[str(p)]; assert h==d['source_sha256']
        for u in d['source_units']:
            a,b=u['json_index']; assert source['text'][a][b]==u['raw_text']; assert clean(u['raw_text'])==u['text']
            assert u['ref']==f'{source["title"]} {a//2+1}{"a" if a%2==0 else "b"}:{b+1}'
    usable=[r for r in records if r['eligibility']=='provisional_usable']
    assert len(usable)==len(inputs)==24
    assert len({r['family_id'] for r in usable})==24
    for r in usable:
        assert set(r['attribution'])=={'Rav','Shmuel'}
        assert set(r['attribution'].values())=={c['candidate_id'] for c in r['candidates']}
        ctx=next(c for c in contexts if c['attempt_id']==r['attempt_id']); spans={s['ref']:s for s in ctx['source_units']}
        for s in r['evidence_spans']: assert spans[s['ref']]['raw_text']==s['raw_text']
    for v in inputs:
        assert set(v)=={'case_id','question_he','conditions_he','candidates'}
        assert len(v['candidates'])==2
        text=v['question_he']+' '+v['conditions_he']+' '+' '.join(c['text_he'] for c in v['candidates'])
        assert not re.search(r'\b(?:רב|שמואל|אביי|רבא)\b|https?://|\d+[ab]:\d+',text),text
        assert v['candidates']==sorted(v['candidates'],key=lambda c:c['candidate_id'])
    m=json.loads((HERE/'source_manifest.json').read_text(encoding='utf8'))
    for item in m['indexes']: assert sha((ROOT/item['path']).read_bytes())==item['sha256']
    print(json.dumps({'status':'pass','source_files':len(raw),'extracted_units':sum(len(c['source_units']) for c in contexts),'inputs':len(inputs),'attempts':len(records),'types':dict(collections.Counter(r['decision_type'] for r in usable)),'qualification':'Mechanical checks only; no independent expert validation'},indent=2))
if __name__=='__main__': main()
