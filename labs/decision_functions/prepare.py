"""Acquire immutable DICES files, audit, and isolate evaluator labels."""
import argparse
import re
import unicodedata
import numpy as np
import pandas as pd
import requests
from common import *

def acquire():
    entries = []
    for file in ['README.md', '350/README.md', '350/diverse_safety_adversarial_dialog_350.csv']:
        url = f'https://raw.githubusercontent.com/google-research-datasets/dices-dataset/{REV}/{file}'
        p = PRIVATE / 'source' / file
        if not p.exists():
            r = requests.get(url, timeout=120); r.raise_for_status()
            p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(r.content)
        entries.append(dict(url=url, **manifest(p)))
    write(OUT/'source_manifest.json', dict(revision=REV, attribution='Google LLC, DICES, Aroyo et al. 2023', license='CC-BY-4.0', files=entries))

def norm(x):
    return ' '.join(unicodedata.normalize('NFKC', str(x)).split())

def prepare():
    df = pd.read_csv(PRIVATE/'source/350/diverse_safety_adversarial_dialog_350.csv', dtype=str, keep_default_na=False)
    docs = (PRIVATE/'source/350/README.md').read_text(encoding='utf-8', errors='replace')
    removed = re.findall(r"'([0-9]+)'", docs.split('removed_raters_350 =')[1])
    assert len(removed)==19
    assert set(df.Q_overall)==set(CLASSES), 'Unknown or missing target; do not silently drop'
    assert not df.duplicated(['rater_id','item_id']).any()
    before = dict(rows=len(df), people=df.rater_id.nunique(), items=df.item_id.nunique())
    missing = {c:int((df[c]=='').sum()) for c in df.columns}
    duplicates = int(df.duplicated().sum())
    df = df[~df.rater_id.isin(removed)].copy()
    people = sorted(df.rater_id.unique()); items = sorted(df.item_id.unique())
    assert len(df)==len(people)*len(items)
    for col in ['context','response']:
        assert df.groupby('item_id')[col].nunique().max()==1
    texts = df.drop_duplicates('item_id').set_index('item_id').loc[items]
    # Join identical normalized input, or identical nonempty conversation context.
    # This conservative input-only origin proxy groups different responses to one context.
    parent = list(range(len(items)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    seen = {}
    for i, row in enumerate(texts.itertuples()):
        keys = [('input', norm(row.context), norm(row.response))]
        if norm(row.context): keys.append(('context', norm(row.context)))
        for key in keys:
            if key in seen: parent[root(i)] = root(seen[key])
            else: seen[key]=i
    groups = {items[i]:min(items[j] for j in range(len(items)) if root(j)==root(i)) for i in range(len(items))}
    splits = dict(people=partition(people,'people_v1'), groups=partition(set(groups.values()),'question_groups_v1'), item_to_group=groups)
    splits['items']={s:[q for q in items if groups[q] in gs] for s,gs in splits['groups'].items()}
    supports={str(seed):sorted(splits['items']['train'], key=lambda q:(sha(f'{seed}|supports_v1|{q}'.encode()),q))[:64] for seed in [101,211,307]}
    assert all(len(v)==64 for v in supports.values())
    write(PRIVATE/'splits.json',splits); write(PRIVATE/'supports.json',supports)
    learner=[dict(item_id=q, text=f'Context:\n{texts.loc[q,"context"]}\n\nAssessed response:\n{texts.loc[q,"response"]}') for q in items]
    write(PRIVATE/'learner.json',learner)
    matrix=df.pivot(index='rater_id',columns='item_id',values='Q_overall').loc[people,items].replace(CLASSES).to_numpy(dtype=np.int64)
    # Separate files enforce that develop does not open test-query outcomes.
    for split in ['train','development','test']:
        ps=splits['people'][split]; qi=splits['items']['train' if split=='train' else split]
        pi=[people.index(p) for p in ps]
        np.savez(PRIVATE/f'{split}_evaluator.npz', y=matrix[np.ix_(pi,[items.index(q) for q in qi])])
        np.savez(PRIVATE/f'{split}_support.npz', y=matrix[np.ix_(pi,[items.index(q) for q in splits['items']['train']])])
    write(OUT/'split_manifest.json',dict(algorithm='SHA256(seed|namespace|canonical_id), lexical digest then ID; floor 60/20/rest', seed=20261124, private_manifest=manifest(PRIVATE/'splits.json'), counts={k:{s:len(v) for s,v in splits[k].items()} for k in ['people','groups','items']}, grouping='NFKC whitespace-normalized full-input duplicates OR same nonempty normalized context; connected components; no outcome access'))
    write(OUT/'support_manifest.json',dict(budgets=[0,4,16,64],primary=16,seeds=[101,211,307],algorithm='SHA256(draw_seed|supports_v1|item_id); nested prefixes, same items for every person',private_manifest=manifest(PRIVATE/'supports.json'),eligible='All 104 retained people; dense matrix'))
    audit=dict(before=before,after=dict(rows=len(df),people=len(people),items=len(items),groups=len(set(groups.values()))),excluded_people=len(removed),policy='Exclude exactly the 19 author-listed failed-quality raters before splitting; no outcome-based exclusions',missing_fields_before=missing,duplicate_rows=duplicates,duplicate_person_item_pairs=0,normalized_duplicate_inputs=len(items)-len({(norm(r.context),norm(r.response)) for r in texts.itertuples()}),observations_per_person=len(items),raters_per_item=len(people),assignment_components=1,group_sizes=sorted(pd.Series(list(groups.values())).value_counts().tolist(),reverse=True))
    write(OUT/'audit.json',audit)
    write(OUT/'dataset_schema.json',dict(person='rater_id',item='item_id',input=['context','response'],target='Q_overall',classes=CLASSES,class_meaning='Yes denotes perceived unsafe; No denotes not unsafe; Unsure retained as a distinct decision. Raw CSV is strings; integers are this adapter mapping, not guessed TFDS codes.',learner_fields=['item_id','text'],source_columns=list(df.columns),missing='Empty target rejected, never mapped to Unsure',quality_policy=audit['policy']))
    (OUT/'DATA_AUDIT.md').write_text('# DICES350 measured audit\n\n'+json.dumps(audit,indent=2)+'\n\nSource: https://github.com/google-research-datasets/dices-dataset/tree/'+REV+'\n\nQ_overall is a per-rater derived overall unsafe judgment from that rater’s Q2–Q6 responses; it is not a population majority. Response is assessed chatbot text. Mapping: No=0, Unsure=1, Yes=2. Demographics, expert fields, timings and other ratings are excluded. The author removal list is used as published; underlying quality criteria were not independently revalidated. Full-input duplicates and identical contexts are grouped without labels. Other near-duplicate/semantic links are not certified, so claims concern held-out input groups, not wholly new semantic topics. Raw text and histories are local only.\n',encoding='utf-8')
    print(json.dumps(dict(audit=audit['after'],splits=read(OUT/'split_manifest.json')['counts'])))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('command',choices=['acquire','prepare']); args=parser.parse_args()
    globals()[args.command]()
