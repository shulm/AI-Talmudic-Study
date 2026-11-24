"""Check packet coverage, exact inherited evidence, empty signoff and prior integrity."""
import json, re
from build_packet import HERE, SOURCE, ROOT, sha, read
def load(name): return json.loads((HERE/name).read_text(encoding='utf8'))
def main():
    packets=load('family_packets.json'); forms=load('human_review_forms.json'); pending=load('pending_families.json'); manifest=load('source_manifest.json')
    assert len(packets)==len(forms)==30
    assert len({p['family_id'] for p in packets})==30
    assert sum(len(p['attempt_ids']) for p in packets)==32
    assert sum(len(p['usable_focal_attempt_ids']) for p in packets)==24
    assert len(pending)==6
    original={r['attempt_id']:r for r in read('evidence_records.jsonl')}
    contexts={r['attempt_id']:r for r in read('evidence_context.jsonl')}
    assert {aid for p in packets for aid in p['attempt_ids']}==set(original)
    for p in packets:
        for aid in p['attempt_ids']: assert original[aid]['family_id']==p['family_id']
        for span in p['exact_excerpt_spans']:
            ctx=contexts[span['attempt_id']]; u=next(u for u in ctx['source_units'] if u['ref']==span['ref'])
            assert span['text']==u['text'] and span['json_index']==u['json_index']
            assert span['source_sha256']==ctx['source_sha256']
        assert p['human_review_status']=='not_performed'
        assert (HERE/p['source_card']).is_file() and (HERE/p['annotation_card']).is_file()
    for f in forms:
        assert f['human_review_status']=='not_performed'
        for role in ['independent_reader_1','independent_reader_2','adjudication']:
            assert all(v is None or v==[] for v in f[role].values()),'Human judgment/signoff must remain blank'
    for item in manifest['source_files']: assert sha(ROOT/item['path'])==item['local_sha256']
    checked=0
    for path in HERE.rglob('*.md'):
        for dest in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf8')):
            assert (path.parent/dest.split('#')[0]).resolve().exists(),(path,dest)
            checked+=1
    assert not manifest['human_review_performed']
    print(json.dumps({'status':'pass','families':30,'attempts':32,'usable_focal_cases':24,'pending_families':6,'source_excerpt_spans':sum(len(p['exact_excerpt_spans']) for p in packets),'valid_markdown_links':checked,'prior_files_hash_checked':len(manifest['source_files']),'human_reviews':0,'qualification':'Packet integrity only, not scholarly certification.'},indent=2))
if __name__=='__main__': main()
