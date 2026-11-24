"""Read-only reconstruction and evidence retrieval; never fabricate missing decisions."""
import argparse
import pipeline as p
def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['sugya','scholar']);ap.add_argument('value');a=ap.parse_args()
    seg={s['id']:s for s in p.rows(p.HERE/'data/segments.jsonl')}
    if a.mode=='sugya':
        gs=[g for g in p.rows(p.HERE/'data/sugyot.jsonl') if a.value in [g['id'],g['authoring_key']]]
        if not gs:raise SystemExit('Unknown sugya; no reconstruction invented')
        for g in gs:
            print(g['title_he'],g['boundary_status'])
            for sid in g['segment_ids']:print(seg[sid]['ref'],seg[sid]['text'])
    else:
        scholars={s['id']:s for s in p.rows(p.HERE/'data/scholars.jsonl') if s['name_he']==a.value}
        positions=[r for r in p.rows(p.HERE/'data/positions.jsonl') if r['scholar_id'] in scholars]
        statements={r['id']:r for r in p.rows(p.HERE/'data/statements.jsonl')}
        relations=p.rows(p.HERE/'data/relations.jsonl')
        print('Text-attested provisional positions; absent records mean missing evidence, never a negative answer.')
        for r in positions:
            print(r['id'],r['status'],r['proposition_he'])
            for e in statements[r['statement_id']]['evidence']:print(e['ref'],e['quote'])
            for rel in relations:
                if rel['target_id']==r['statement_id'] and rel['relation_type'] in ['rejects','qualifies','answers','reframes']:
                    print('Related reasoning:',rel['relation_type'])
                    for e in statements[rel['source_id']]['evidence']:print(e['ref'],e['quote'])
if __name__=='__main__':main()
