"""Read-only, pinned acquisition and canonicalization. Never print target responses.

Local participant artifacts are intentionally excluded from the public repository.
"""
from pathlib import Path
import ast
import hashlib
import html
import json
import re
import sys
import platform
import importlib.metadata
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
LOCAL = ROOT / 'local_data'
SRO = '4e6e837fb5aaca87ed5914fd9be251156f43eec9'
HF = '532794c51e046a0ddaf560e7972789688d46bf63'
SEED = 20261124

def digest(x):
    return hashlib.sha256(x if isinstance(x, bytes) else x.encode()).hexdigest()

def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def jsonl(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')

def clean(s):
    return html.unescape(re.sub('<[^>]+>', ' ', s)).strip()

def acquire():
    import truststore
    truststore.inject_into_ssl()
    import requests
    LOCAL.mkdir(exist_ok=True)
    sources = [
        ('sro_README.md', f'https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/{SRO}/README.md'),
        *[(f'sro_{t}.csv.gz', f'https://raw.githubusercontent.com/IanEisenberg/Self_Regulation_Ontology/{SRO}/Data/Complete_02-16-2019/Individual_Measures/{t}.csv.gz') for t in ['kirby','holt_laury_survey','columbia_card_task_cold']],
        ('kirby_experiment.js','https://raw.githubusercontent.com/expfactory/expfactory-experiments/49b8123f18b26d94dfc010bb8a6ec7458b265e2e/kirby/experiment.js'),
        ('holt_laury_survey_survey.tsv','https://raw.githubusercontent.com/expfactory/expfactory-surveys/7fee0ece12aa60497436990c6a7c5ca7349eb42a/holt_laury_survey/survey.tsv'),
        ('README.md',f'https://huggingface.co/datasets/HikaruAsano/cross-psych-101/resolve/{HF}/README.md'),
        *[(f'{split}-00000-of-00001.parquet',f'https://huggingface.co/datasets/HikaruAsano/cross-psych-101/resolve/{HF}/data/{split}-00000-of-00001.parquet') for split in ['train','test']]
    ]
    manifest=[]
    for name,url in sources:
        dest=LOCAL/name
        if not dest.exists():
            with requests.get(url,stream=True,timeout=120) as r:
                r.raise_for_status()
                with dest.open('wb') as f:
                    for chunk in r.iter_content(1024*1024):
                        f.write(chunk)
                        if sum(x.stat().st_size for x in LOCAL.iterdir() if x.is_file()) > 2*1024**3:
                            raise RuntimeError('download cap')
        b=dest.read_bytes()
        manifest.append(dict(file=name,url=url,bytes=len(b),sha256=digest(b)))
    dump(ROOT/'source_manifest.json',dict(sro_revision=SRO,cross_psych_revision=HF,files=manifest,
         downloaded_artifact_bytes=sum(x['bytes'] for x in manifest),license='SRO data CC-BY-4.0; Cross-Psych permission unresolved, not admitted'))

def audit_cross():
    import pyarrow.parquet as pq
    a=pq.read_table(LOCAL/'train-00000-of-00001.parquet').to_pandas()
    # Test content is never loaded for design: only linkage metadata.
    b=pq.read_table(LOCAL/'test-00000-of-00001.parquet',columns=['participant'])
    pa=set(a.participant);pb=set(b.column(0).to_pylist())
    histories=[]
    for r in a.itertuples():
        u=r.message[0]['content']
        s=u.split('--- PREVIOUS EXPERIMENT ---\n',1)[1].split('--- END PREVIOUS EXPERIMENT ---',1)[0]
        histories.append((r.participant,r.prev_task_name,digest(s)))
    audit=dict(train_rows=len(a),test_rows=len(b),train_people=len(pa),test_people=len(pb),
        union_people=len(pa|pb),overlap_people=len(pa&pb),train_unique_person_task_transcript_hashes=len(set(histories)),
        raw_decision_count=None,reason='Transcript hash cannot distinguish distinct identical sessions; release lacks original session/trial IDs and permission statement.',
        task_types=sorted(a.prev_task_name.unique().tolist()),test_content_inspected=False)
    dump(ROOT/'cross_psych_audit.json',audit)
    return audit

def build():
    a=pd.read_csv(LOCAL/'sro_kirby.csv.gz');b=pd.read_csv(LOCAL/'sro_holt_laury_survey.csv.gz')
    assert a['Unnamed: 0'].is_unique and b['Unnamed: 0'].is_unique
    a=a[a.exp_stage=='test'].copy()
    definition=(LOCAL/'kirby_experiment.js').read_text(encoding='utf-8')
    arrays=[json.loads('['+re.search(key+r':\s*\[([^]]+)\]',definition)[1]+']') for key in ['small_amt','large_amt','later_del']]
    expected_kirby=set(zip(*arrays))
    assert len(expected_kirby)==27
    assert set(zip(a.small_amount,a.large_amount,a.later_delay))==expected_kirby
    counts_a=a.groupby('worker_id').size();counts_b=b.groupby('worker_id').size()
    all_people=sorted(set(counts_a.index)|set(counts_b.index))
    eligible=[p for p in all_people if counts_a.get(p,0)==27 and counts_b.get(p,0)==10]
    order=sorted(eligible,key=lambda p:digest(f'{SEED}|person|{p}'))
    n=len(order); partition={p:('train' if i<int(.6*n) else 'validation' if i<int(.8*n) else 'test') for i,p in enumerate(order)}
    old=partition.get('s001');partition['s001']='train' # initial raw content audit: development permanently
    records=[]
    for task,df,filename in [('kirby',a,'sro_kirby.csv.gz'),('holt_laury',b,'sro_holt_laury_survey.csv.gz')]:
        sha=digest((LOCAL/filename).read_bytes())
        for pos,r in enumerate(df.to_dict('records')):
            p=r['worker_id']; rawid=r['Unnamed: 0']; did=digest(f'{SRO}|{task}|{rawid}')
            if task=='kirby':
                small,large,delay=[float(r[k]) for k in ['small_amount','large_amount','later_delay']]
                stimulus=clean(r['stimulus']);assert f'${int(small)}' in stimulus and f'${int(large)}' in stimulus and f'{int(delay)} days' in stimulus
                alternatives=[dict(id='sooner',text=f'${small:g} today',amount=small,delay_days=0),dict(id='later',text=f'${large:g} in {delay:g} days',amount=large,delay_days=delay)]
                choice={'smaller_sooner':'sooner','larger_later':'later'}.get(r['choice'])
                assert choice==({81:'sooner',80:'later'}.get(r['key_press']))
                family=f'kirby:{small:g}:{large:g}:{delay:g}'
                ordinal=int(rawid.rsplit('_',1)[1]); instructions='Choose the preferred amount now or later. A random trial determines a proportional bonus at the chosen time.'
                feature=[1, np.log(large/small),np.log1p(delay)/5,large/100,0,0,0,0]
                order_kind='original trial suffix; fixed list, after one practice item'
            else:
                options=ast.literal_eval(r['options']); assert len(options)==2
                alternatives=[dict(id='safe' if i==0 else 'risky',text=clean(o['text']),original_option_id=o['id']) for i,o in enumerate(options)]
                choice={1:'safe',2:'risky'}.get(r['response']); ordinal=int(r['question_num'])
                pr=int(re.search(r'(\d+)%',options[0]['text'])[1])/100
                for i,o in enumerate(options):
                    values=[float(v) for v in re.findall(r'(\d+(?:\.\d+)?)',clean(o['text']))]
                    assert values==[pr*100,100 if i==0 else 190,round((1-pr)*100),80 if i==0 else 5], values
                assert int(r['response']) in [int(o['value']) for o in options]
                assert clean(r['response_text'])==alternatives[int(r['response'])-1]['text']
                family='holt_laury:lottery_schedule' # all ten same-page items are one family
                stimulus=clean(r['text']); instructions='Indicate the preferred gamble for each of ten paired lottery choices, displayed on one page.'
                feature=[0,0,0,0,1,pr,pr*pr,(165*pr-75)/100]
                order_kind='display question number; within-page click chronology unavailable'
            records.append(dict(dataset_revision=SRO,person_id=p,task_id=task,family_id=family,session_id=f'{p}:{task}:{r["finishtime"]}',trial_id=rawid,
                decision_id=did,stable_original_decision_id=rawid,stimulus=stimulus,instructions=instructions,alternatives=alternatives,chosen_alternative=choice,
                missing_status=None if choice else 'unrecorded',original_order=ordinal,order_kind=order_kind,predecessor_dependencies=[],pre_choice_feedback=None,
                source_file=filename,source_span={'row_id':rawid},source_sha256=sha,extraction_version='1.0',observed=True,synthetic=False,
                partition=partition.get(p,'excluded_incomplete_coverage'),prediction_time_visibility={'scenario':'current_target_or_revealed_source','chosen_alternative':'source_only_if_budget_charged; target_evaluator_only'},
                feature_difference=feature))
    assert len({r['decision_id'] for r in records})==len(records)
    jsonl(LOCAL/'canonical_observations.jsonl',records)
    source_families=sorted({r['family_id'] for r in records if r['task_id']=='kirby'},key=lambda x:digest(f'{SEED}|support|{x}'))
    people=sorted(eligible); episodes=[]; scenarios=[]; labels=[]; supports=[]
    for p in people:
        sr=sorted([r for r in records if r['person_id']==p and r['task_id']=='kirby'],key=lambda r:source_families.index(r['family_id']))
        tr=sorted([r for r in records if r['person_id']==p and r['task_id']=='holt_laury'],key=lambda r:r['original_order'])
        assert len(sr)==27 and len(tr)==10 and all(r['chosen_alternative'] for r in sr+tr)
        assert {r['family_id'] for r in sr}==set(source_families) and len(source_families)==27
        assert [r['original_order'] for r in tr]==list(range(2,12))
        assert np.allclose([r['feature_difference'][5] for r in tr],np.arange(1,11)/10)
        for budget in [0,2,4,8]:
            episodes.append(dict(person_id=p,partition=partition[p],budget=budget,support=[r['decision_id'] for r in sr[:budget]],eligible_query_pool=[r['decision_id'] for r in sr],targets=[r['decision_id'] for r in tr]))
        for r in sr[:8]:
            supports.append({k:r[k] for k in ['person_id','decision_id','family_id','feature_difference','chosen_alternative','alternatives','partition']})
        for r in tr:
            scenarios.append({k:r[k] for k in ['person_id','decision_id','family_id','feature_difference','alternatives','partition']})
            labels.append({k:r[k] for k in ['person_id','decision_id','family_id','chosen_alternative','partition']})
    jsonl(LOCAL/'episode_membership.jsonl',episodes);jsonl(LOCAL/'source_observations.jsonl',supports)
    jsonl(LOCAL/'target_scenarios.jsonl',scenarios)
    for part in ['train','validation','test']:
        jsonl(LOCAL/f'evaluator_labels_{part}.jsonl',[r for r in labels if r['partition']==part])
    dump(LOCAL/'person_partitions.json',partition)
    dump(ROOT/'split_manifest.json',dict(seed=SEED,algorithm='SHA256(seed|person|worker_id); sorted; floor(.6N), floor(.8N) boundaries',
        original_audit_person_partition=old,audit_person_override='s001 assigned train after its first rows were inspected; not an official benchmark split',
        eligible_people=n,all_people=len(all_people),counts={s:sum(v==s for v in partition.values()) for s in ['train','validation','test']},
        exclusions={'incomplete_target_schedule':len(all_people)-n},source_support_order=source_families,
        source_decisions=len(a),target_decisions=len(b),eligible_source_decisions=n*27,eligible_target_decisions=n*10,
        target_families=1,source_item_families=27,independent_task_types=2,
        artifacts={f:digest((LOCAL/f).read_bytes()) for f in ['person_partitions.json','canonical_observations.jsonl','episode_membership.jsonl','source_observations.jsonl','target_scenarios.jsonl','evaluator_labels_train.jsonl','evaluator_labels_validation.jsonl','evaluator_labels_test.jsonl']}))
    dump(ROOT/'environment.json',dict(python=sys.version,platform=platform.platform(),packages={p:importlib.metadata.version(p) for p in ['numpy','scipy','pandas','pyarrow','torch','requests','truststore']}))

if __name__=='__main__':
    acquire();audit_cross();build()
    print('Pinned acquisition, structural audit, canonicalization, and participant split completed. No target responses printed.')
