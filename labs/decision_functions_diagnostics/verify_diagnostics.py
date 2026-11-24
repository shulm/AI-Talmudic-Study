"""Post-run arithmetic and source checks only; no optimization or predictions."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse
import csv
from core import *
from synthetic import generate,expected_nll,contrast
from replay import compare,metrics

def main(private,local):
    result=read(OUT/'synthetic_results.json'); z,base,bias,u,v,split,ys,ps=generate()
    pfile=local/'synthetic_predictions.npz'; assert file_hash(pfile)==result['prediction_sha256']; arrays=dict(np.load(pfile))
    errors=[]; expected_keys=set()
    for row in result['results']:
        regime,lam,condition=row['regime'],row['lambda_'],row['condition']; prefix=f'{regime}_lambda{lam}_{condition}'
        pb,pm=arrays[prefix+'_B3'],arrays[prefix+'_M1']; expected_keys.update([prefix+'_B3',prefix+'_M1'])
        oracle=ps[regime][72:,split['test']]; labels=ys[regime][72:,split['test']]
        for name,p in [('B3',pb),('M1',pm)]:
            for key,value in metrics(p,labels).items(): errors.append(compare(value,row[name][key]))
            errors.append(compare(expected_nll(p,oracle),row['expected_nll_'+name]))
    assert set(arrays)==expected_keys
    # Materialize the declared two wording variants for engineering inspection only.
    # They were never an encoder input; no added observations and no extra fits.
    case_groups={str(case):case//3 for case in range(192)}; memberships={}
    for name in ['train','development','test']:
        for case in split[name]: memberships[str(case)]=name
    learner=[]; evaluator=[]
    for case,features in enumerate(z):
        for variant in range(2):
            text=(f'Condition vector: first={features[0]:.17g}; second={features[1]:.17g}.' if variant==0 else f'The first condition equals {features[0]:.17g}, and the second equals {features[1]:.17g}.')
            learner.append(dict(case=f'{case}-v{variant}',text=text,features=features.tolist()))
            evaluator.append(dict(case=f'{case}-v{variant}',semantic_case=case,group=case//3,split=memberships[str(case)]))
    atomic(local/'synthetic_learner_views.json',learner); atomic(local/'synthetic_evaluator_groups.json',evaluator)
    for group in range(64): assert len({r['split'] for r in evaluator if r['group']==group})==1
    # Independently reconstruct only the training matrix from the pinned raw CSV.
    raw=private/'source/350/diverse_safety_adversarial_dialog_350.csv'; source_hash=file_hash(raw)
    assert source_hash==pinned('source_manifest.json')['files'][-1]['sha256']
    splits=read(private/'splits.json'); people=splits['people']['train']; items=splits['items']['train']; pi={p:i for i,p in enumerate(people)}; qi={q:i for i,q in enumerate(items)}
    matrix=np.full((len(people),len(items)),-1,dtype=np.int64); mapping={'No':0,'Unsure':1,'Yes':2}
    with raw.open(encoding='utf-8',newline='') as stream:
        for row in csv.DictReader(stream):
            if row['rater_id'] in pi and row['item_id'] in qi:
                i,j=pi[row['rater_id']],qi[row['item_id']]
                assert matrix[i,j]==-1; matrix[i,j]=mapping[row['Q_overall']]
    assert (matrix>=0).all() and np.array_equal(matrix,np.load(private/'train_evaluator.npz')['y'])
    assert file_hash(raw)==source_hash
    receipt('diagnostic_verification.json',dict(status='PASS',synthetic_arrays=len(arrays),arithmetic_max_error=max(errors),wording_variants=len(learner),grouped_variants=True,wording_materialization='Post-fit engineering artifact only; numerical cases/labels/splits unchanged; no encoder used',fixture_hashes={name:file_hash(local/name) for name in ['synthetic_learner_views.json','synthetic_evaluator_groups.json']},training_matrix_matches_pinned_source=True,training_source_sha256=source_hash,training_matrix_shape=list(matrix.shape),no_fits=True))
    print('PASS',len(arrays),'arrays, grouped variants, training-source join')

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--private-root',required=True,type=Path); parser.add_argument('--output-private-root',required=True,type=Path); args=parser.parse_args(); main(args.private_root,args.output_private_root)
