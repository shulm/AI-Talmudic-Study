"""Save exact immutable partial receipts and bounded accepted proposals."""
import sys,hashlib,json,datetime
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('avodah_zarah','Avodah Zarah','unused')
out=Path(__file__).resolve().parent
state=r.current(a.job); snapshot=r.sha(r.encoded(state)); report=r.report(state,a.source)
count=report['completed_by_layer']['structure']
replay=r.replay(a.job);assert replay['replay_pass']
exportdir=a.job/'exports'/('checkpoint_'+str(count))
if not exportdir.exists():r.export(a.job,exportdir)
manifest=r.read(exportdir/'manifest.json')
for file,h in manifest['files'].items():assert r.sha((exportdir/file).read_bytes())==h,file
contract=Path('research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
cd=r.read(contract);assert r.sha(contract.read_bytes())=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for file,h in cd['production_files'].items():assert r.sha(Path(file).read_bytes())==h,file
for h in state['proposals']:
 raw=(a.job/'proposals'/(h+'.json')).read_bytes();assert r.sha(raw)==h
 r.immutable(out/'proposals'/(h+'.json'),raw)
receipt=dict(status='INCOMPLETE_PROVISIONAL_CORE',producer='/root/avodah_continuation_2',generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),run_id='run_20261125_01',job='bavli_avodah_zarah',lane='L04',owner=r.read(a.job/'OWNER.json'),snapshot_sha256=snapshot,contract_sha256=r.sha(contract.read_bytes()),production_git_commit=cd['production_git_commit'],production_files_verified=cd['production_files'],source_sha256=a.meta['source_sha256'],schema_sha256=cd['schema_sha256'],protocol_sha256=cd['annotation_protocol_sha256'],accepted_proposal_chain=state['proposals'],open_tails=state['open_tails'],replay_pass=True,export_directory=str(exportdir),export_manifest_sha256=r.sha((exportdir/'manifest.json').read_bytes()),export_files_verified=len(manifest['files']),external_job=str(a.job),paid_api_calls=0,source_and_tooling_modified=False,**report)
source_schema=Path('F:/Sefaria-Export-master/schemas/Avodah_Zarah.json')
assert r.sha(source_schema.read_bytes())=='10a04f596e570e6a75d101acac5e56165385955f8831577e541e236191ee9e74'
receipt['source_schema_sha256']=r.sha(source_schema.read_bytes())
receipt['remaining_segments']=2131-count
receipt['model_id']=None
receipt['independent_review_note']='No future source-only findings read; exact-version independent comparison remains outstanding for the added scope.'
r.immutable(out/f'CHECKPOINT_{count}_RECEIPT.json',r.encoded(receipt))
r.immutable(out/f'replay_{count}.json',r.encoded(replay))
nextref=report['next_unprocessed_by_layer']['structure']
notes=f'''# Avodah Zarah current partial source checkpoint

Owner `L04/avodah_zarah_resume_20261126`, epoch3. Snapshot `{snapshot}`.
External authoritative job: `{a.job}`.
All eight layers cover {count}/2131 original segments. {2131-count} remain. Typed records: {report['semantic_records']}.
Next source: **{nextref}**, with broad overlap and continuation. Current producer `/root/avodah_continuation_2`.

Read the immutable CHECKPOINT_{count}_RECEIPT.json and accepted proposal chain. Replay passed and {len(manifest['files'])} exported files match the immutable export manifest. Verify current OWNER/CURRENT and all nine frozen production file hashes before resuming. Source/schema hashes and source-only review boundary remain unchanged. No independent-review acceptance, tractate delivery, ML eligibility or human certification is claimed.

Preserve the four earlier structural tails `az.s03`, `az.s04`, `az.s05`, `az.s06` and their existing continuation links. They were not artificially closed. Consolidation requires explicit immutable supersession, complete dependency/scope/coverage updates and a full-span structural read. New local structures are smaller resolved arguments, not replacements for the old tails.

Recent distinctions: divine/Abraham/Adam quoted voices versus rabbinic expositors; alternative Amemar/Ravina attribution; retained איפוך and non-inversion answer at4b:12–13 linked to earlier schedule; silence and nonexecution do not imply assent/action; unexpanded ר״א at5a:5; corrected nonbirth reading of Resh Lakish and two tannaitic mortality positions; רבה at5b:2 is Rabbah. `partial` answer inventories mark only represented source-supported replies, not certified exhaustive alternatives. Earlier none metadata is not a source-absence claim.

Later distinctions: two alternative Yohanan/Resh Lakish objection directions at6b:3–4; three separate Abaye/Rava occurrences; debt versus dyeing scopes of the two rulings at6b:17; context-inferred Rav Huna attribution explicitly editorial; two Rabbi Yehuda readmission versions; four noncumulative explanations of repeated sages at7b:4–7; Nahum’s horse coordination and דגנוניתא remain qualified; Rav’s personal-prayer additions at8a:2–3 are compatible qualifications of Shmuel’s ruling, not an invented dispute. The source through8a:18 has been read for context, but no source after8a:4 is counted extracted at checkpoint195.

Author scripts are state-dependent records of manual annotation, not replay tools. Reproduce using immutable accepted proposals and the unchanged common runner. Rejected/unsubmitted staging attempts remain external. No commits/pushes were made by this producer. This checkpoint records completed work, not a promise of background continuation.
'''
(out/'NEXT_SOURCE_WORK.md').write_text(notes,encoding='utf8')
print(json.dumps({'snapshot':snapshot,'covered':count,'records':report['semantic_records'],'next':nextref,'verified_export_files':len(manifest['files'])}))
