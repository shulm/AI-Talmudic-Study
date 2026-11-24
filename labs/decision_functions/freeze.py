"""Resolve the supplied template, hash exact inputs, and validate freeze readiness."""
import importlib.metadata
import platform
import numpy as np
from common import *

def resources():
    logs=read(OUT/'command_log.json'); dev=read(OUT/'development_results.json')
    sources=read(OUT/'source_manifest.json'); enc=read(OUT/'encoder_manifest.json')
    evals=[read(OUT/name) for name in ['development_controls.json','test_results.json'] if (OUT/name).exists()]
    result=dict(hardware=dict(system=platform.platform(),processor=platform.processor(),logical_cpus=os.cpu_count()),downloaded_dataset_and_weight_payload_bytes=sum(f['bytes'] for f in sources['files'])+sum(f['bytes'] for f in enc['files']),download_accounting='Unique acquired payload bytes, includes failed encoder attempt reuse; HTTP metadata/transport overhead not measured',dependency_installs=0,dependency_install_bytes=0,measured_commands=logs,measured_cpu_seconds=sum(x['cpu_seconds_sampled'] for x in logs),measured_wall_seconds=sum(x['wall_seconds'] for x in logs),sampled_peak_rss_bytes=max(x['peak_rss_bytes_sampled'] for x in logs),human_shared_fits=dev['shared_fits'],synthetic_shared_fits_total=4,adaptation_person_solves=dev['adaptation_person_solves']+sum(x['adaptation_person_solves'] for x in evals),limits=dict(download_bytes=2147483648,cpu_core_hours=6,memory_bytes=8589934592,shared_fits=40),unmeasured='Initial acquire/prepare and small documentation/inspection commands not process-profiled; measured child-process CPU/RSS sampled every 0.1 seconds, final fraction of second may be missed. HTTP metadata/transport overhead not captured.',failed_attempts=['Initial encoding: removed prepare_for_model API; no model fit or query scoring occurred.','Read-only diagnostic numpy.linalg.norm with 3-axis argument failed; no artifacts changed.'])
    assert result['human_shared_fits']+result['synthetic_shared_fits_total']<=40
    assert result['measured_cpu_seconds']<6*3600 and result['sampled_peak_rss_bytes']<8589934592
    write(OUT/'RESOURCE_USAGE.json',result)
    return result

def main():
    p=read(OUT.parents[1]/'protocol_template.json')
    audit=read(OUT/'audit.json'); source=read(OUT/'source_manifest.json'); enc=read(OUT/'encoder_manifest.json'); grid=read(Path(__file__).with_name('grid.json')); dev=read(OUT/'development_results.json')
    assert read(OUT/'validation_results.json')['status']=='PASS'
    assert all(o['success'] for o in dev['optimizations'])
    p.update(status='PROTOCOL_FROZEN',source_base_commit='2c6d3466328752c220a9b1fc05c3c308553dab47')
    p['dataset'].update(upstream_revision=REV,artifact_sha256=source['files'][-1]['sha256'],downloaded_bytes=sum(x['bytes'] for x in source['files']),actual_class_mapping=CLASSES,quality_policy=audit['policy'],source_terms='Google LLC CC-BY-4.0; attribution in source_manifest.json',counts_before=audit['before'],counts_after=audit['after'],grouping_policy=read(OUT/'split_manifest.json')['grouping'],eligible_cohort=read(OUT/'split_manifest.json')['counts'])
    p['encoder'].update(revision=enc['revision'],tokenizer_revision=enc['revision'],embedding_dimension=384,max_sequence_length=enc['max_sequence_length'],pooling=enc['pooling'],libraries=enc['libraries'],artifact_manifest='encoder_manifest.json')
    p['partitions'].update(item_grouping_rule=read(OUT/'split_manifest.json')['grouping'],split_manifest_path='split_manifest.json',split_manifest_sha256=manifest(OUT/'split_manifest.json')['sha256'])
    p['support'].update(support_manifest_path='support_manifest.json',support_manifest_sha256=manifest(OUT/'support_manifest.json')['sha256'])
    p['models'].update(optimizer_and_convergence=grid,selected_baseline=dev['primary_baseline'],selected_M1_configuration=dev['selected']['M1'],selected_all=dev['selected'])
    p['evaluation'].update(final_evaluation_list=grid['final_batch'],freeze_commit='External pushed SHA supplied to scorer and issue before evaluation (cannot self-embed)',final_run_id='pilot_v1_test_once',results='Not yet scored at freeze')
    p['resources']['actual_usage']=resources()
    p['private_files']={name:manifest(PRIVATE/name) for name in ['splits.json','supports.json','learner.json','embeddings.npy','selected_models.npz','test_evaluator.npz','test_support.npz']}
    files=list((ROOT/'labs/decision_functions').glob('*.py'))+[ROOT/'labs/decision_functions/grid.json']+[OUT/name for name in ['source_manifest.json','dataset_schema.json','split_manifest.json','support_manifest.json','encoder_manifest.json','model_artifact_manifest.json','validation_results.json','development_results.json']]
    p['integrity_files']={str(f.relative_to(ROOT)).replace('\\','/'):sha(f.read_bytes()) for f in files}
    for field in p['required_before_development']+p['required_before_final_scoring']:
        val=p
        for part in field.split('.'): val=val[part]
        assert val is not None,field
    write(OUT/'experiment_protocol.json',p)
    versions={name:importlib.metadata.version(name) for name in ['numpy','scipy','pandas','requests','psutil','torch','transformers','huggingface-hub','safetensors']}
    (ROOT/'labs/decision_functions/requirements.txt').write_text('\n'.join(f'{k}=={v}' for k,v in versions.items())+'\n',encoding='utf-8')
    (OUT/'EXPERIMENT_PROTOCOL.md').write_text('# Resolved freeze\n\nMachine-readable contract: experiment_protocol.json; grid: ../../../../labs/decision_functions/grid.json. Source and encoder are immutable. Primary baseline '+dev['primary_baseline']+'; M1 '+json.dumps(dev['selected']['M1'])+'. No development refitting. All declared support curves, seeds, and ten fixed history derangements at k=16 will be evaluated in one batch. Probabilities and paired cell losses remain local with public hashes. Scorer requires HEAD and remote branch to equal the supplied freeze SHA and checks code, protocol-linked manifests, and private artifact hashes. The freeze SHA is recorded externally before any test scoring.\n\nDevelopment M1 basis norms are near zero; expect effective equality with B3. Preserve this result and do not expand the grid. Numerical-scale differences are not evidence of substantive interaction. No post hoc practical-significance threshold is introduced.\n',encoding='utf-8')
    print('FREEZE_READY')

if __name__=='__main__': main()
