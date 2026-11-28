import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
job,segs=runner.load(Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir'));v=list(segs.values());S={x['ref'].removeprefix('Nazir '):x for x in v}
notes=[
('4a:2','Rava supplies replacement case: oath to drink followed by I am a nazir; nazir prohibition takes effect over the oath. Preserve sequence and distinguish from rejected kiddush/havdalah proposal.'),
('4a:3','Question to sages: verse also needed to prohibit mitzvah wine like optional wine.'),
('4a:3','Answer: wine alone would suffice for that; additional ושכר permits two derivations. Do not erase either use.'),
('4a:4','Shimon uses שכר/שכר comparison to Temple entry, rather than sages’ double derivation.'),
('4a:4','Nazir comparison premise: wine forbidden, other drinks not; keep separate scope from Temple law.'),
('4a:4','Derived Temple-entry view: wine forbidden, other intoxicating drinks not. These opposite drink classes require distinct conditions/outcomes.'),
('4a:5','Explicit contrast with Rabbi Yehudah: source lists eating Keilite fig and drinking honey and milk before Temple entry as liable. Preserve listed consumptions, do not invent dose or treat as contemporary ruling.'),
('4a:6','Alternative answer: Shimon does not accept a prohibition taking effect on an existing prohibition. Keep איבעית אימא as alternate explanation, not cumulative mandatory reason.'),
('4a:7','Evidence for Shimon alternative: one eating neveilah on Yom Kippur exempt in cited ruling. Scope exemption to additional prohibition argument, not blanket permitted eating.'),
('4a:8','Question to sages from מכל אשר יעשה מגפן היין.'),
('4a:8','Sages assign that wording to combination of nazir prohibitions with each other.'),
('4a:9','Shimon does not need combination in this account: any amount suffices for lashes.'),
('4a:9','Shimon retains olive-size minimum for an offering. Different sanction thresholds must not merge.'),
('4a:10','Mishnah Samson identification includes son of Manoah, husband of Delilah, uprooting Gaza gates, and Philistines blinding him; stated result is Samson nazir.'),
('4a:10','Following clarification warns plain Samson alone could mean another Samson; do not encode all identifiers as unconditionally sufficient standalone vows without qualification.'),
('4a:11','Explicit question why list all these identifiers.'),
('4a:11','If only Samson, might mean another Samson; son of Manoah added to identify intended figure.'),
('4a:12','Even son of Manoah might be another bearer of that name; Delilah and blinding identifiers remove this ambiguity. Keep actual source identifiers, no invented direct quote for Gaza explanation.'),
('4a:13','Mishnah asks distinction between perpetual nazir and Samson nazir.'),
('4a:13','Perpetual nazir may lighten hair with razor when hair becomes heavy.'),
('4a:13','Perpetual nazir brings three animals in connection with that haircut.'),
('4a:13','If perpetual nazir becomes impure, he brings impurity offering.'),
('4a:14','Samson nazir cannot lighten heavy hair.'),
('4a:14','If Samson nazir becomes impure, he does not bring impurity offering; subsequent4b5 removes inference of initial prohibition from if wording.'),
('4a:15','Gemara asks who introduced perpetual nazir; reconstructive חסורי מיחסרא adds explicit I am perpetual nazir declaration.'),
('4a:15','Reconstructed declaration I am perpetual nazir effects nazir status.'),
('4a:15','Reconstructed teaching repeats perpetual heavy-hair relief, three animals, and impurity offering. Keep parallel occurrence with initial Mishnah distinct.'),
('4a:15','Reconstructed Samson clause forbids razor lightening; continues across folio to4b1.'),
('4b:1','Crossfolio reconstructed Samson clause excludes impurity offering; do not shift page index.'),
('4b:2','Inference: only offering excluded, but nazir status does take effect.'),
('4b:3','Question proposes Mishnah fits neither Rabbi Yehudah nor Shimon.'),
('4b:3','Rabbi Yehudah permits Samson nazir to become impure through dead persons.'),
('4b:3','Yehudah cites Samson becoming impure as supporting precedent; later proofs questioned and finally tradition, not forced verse proof.'),
('4b:3','Shimon says I am Samson nazir has no effect.'),
('4b:3','Shimon reason: Samson’s nazir status was not expressed from his own mouth. Angel’s declaration later distinguished from self-vow.'),
('4b:4','Objection to Yehudah assignment: he allows impurity initially, whereas Mishnah says if he became impure.'),
('4b:4','Objection to Shimon assignment: he denies nazir status takes effect at all.'),
('4b:5','Final local assignment is Rabbi Yehudah; if became impure phrasing in Samson clause follows parallel perpetual-na-zir wording, not prohibition ab initio.'),
('4b:6','Proposed alignment with firstborn-vow dispute is an explicit question, not final identification.'),
('4b:6','For declaration upon me like a firstborn, Rabbi Yaakov prohibits.'),
('4b:6','For same declaration Rabbi Yose permits. Preserve question context and later rejection of proposed alignment.'),
('4b:7','CONTEXT proposed mapping: Yehudah like Yaakov no davar-hanadur requirement; Shimon like Yose requires it. This proposal is rejected next.'),
('4b:8','CONTEXT rejection: all require davar hanadur; firstborn case differs because לה׳ includes firstborn in this account.'),
('4b:9','CONTEXT Yose uses לה׳ to include sin offering and guilt offering; separate named categories.'),
('4b:10','CONTEXT why include those but exclude firstborn? They can be consecrated by vow, firstborn cannot in Yose account.'),
('4b:11','CONTEXT Yaakov counters firstborn too is consecrated; house of Rabbi teaches command to sanctify firstborn born in flock, citing הזכר תקדיש.'),
('4b:12','CONTEXT Yose concedes command to consecrate but asks whether it would not already be holy if not consecrated. Distinguish obligation from constitutive effect.'),
('4b:13','CONTEXT challenge: nazir verse also says לה׳.'),
('4b:14','CONTEXT שמעון הצדיק uses dedication verse through narrative: never ate impure nazir guilt offering except one man from south; his attractive hair prompts question.'),
('4b:15','CONTEXT young shepherd recounts seeing reflection, inclination threatening him and vow to shave for heaven; source self-address is not narrator diagnosis.'),
('4b:16','CONTEXT Shimon kisses head, praises such nazir vows, cites להזיר לה׳. Keep narrator and quoted shepherd voices separate.'),
('4b:17','CONTEXT question Samson not nazir despite prenatal divine-nazir verse; reply angel said it, preserving self-vow distinction.'),
('4b:18','CONTEXT impurity proof from jawbone killing thousand rejected as maybe incited/attacked without touching. Do not treat killing as automatic corpse contact.'),
('4b:19','CONTEXT alternative proof killing thirty and taking garments; counterproposal strip before killing answered by order struck then took.'),
('4b:20','CONTEXT further counterproposal victims only dying defeats conclusive corpse-contact proof; final conclusion tradition learned, not verse-established certainty.')]
findings=[]
for i,(ref,note) in enumerate(notes,1):
 s=S[ref];findings.append({'id':f'NAZ004-{i:03}','ref':s['ref'],'source_index':s['source_index'],'scope':'context' if note.startswith('CONTEXT') else 'core','finding':note,'evidence':[{'segment_id':s['id'],'start_char':0,'end_char':len(s['text']),'quote':s['text']}]})
cores=v[50:70];assert cores[0]['ref']=='Nazir 4a:2' and cores[-1]['ref']=='Nazir 4b:6'
r={'status':'FROZEN_BEFORE_NEW004_PRODUCER_LABELS','reader':'/root/rosh_hashanah','exposure':'Never Nazir producer. Previously independently compared Nazir001/002 and targeted corrections; earlier Nazir source/label exposure is disclosed. Current source window reread directly from pinned raw edition before any new004 labels. This is purposive contiguous continuation, not fresh random cohort. No claim of globally unexposed memory.','producer_labels_seen':False,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'source_sha256':job['source_sha256'],'schema_sha256':job['schema_sha256'],'protocol_sha256':job['protocol_sha256'],'scope':{'core_segments':20,'first':cores[0]['ref'],'last':cores[-1]['ref'],'inventory_indices':[50,69],'original_indices':[cores[0]['source_index'],cores[-1]['source_index']],'context_read':'3b9–4a1 preceding;4b7–4b20 following closes Samson source proof;4b21 begins perpetual-na-zir source discussion'},'findings':findings,'source_evidence':[{'ref':s['ref'],'source_index':s['source_index'],'text':s['text']} for s in v[44:85]],'layer_checks':{'structure':'Crossfolio4a15–4b1 and4b6 proposed alignment requires continuation;4b20 closes final tradition answer.','utterances':'Mishnah, reconstructed teaching, baraita and narrative voices distinct.','claims':'Wine/other-drink contrasts, sanction thresholds, haircut/offering outcomes and permitted/no-effect positions separate.','attributions':'Rava replacement, Shimon alternative, Yehudah/Yaakov/Yose proposals; Shimon the Righteous distinct.','questions':'Explicit why/how cases retained, competing assignments tested.','positions':'4b5 final Yehudah assignment;4b7 proposed mapping rejected4b8; no final source-proof claim from rejected verses.','edges':'Support, objection, qualification and correction direction anchored to continuation.','reconciliation':'All20 cores manually reread plus complete relevant Samson continuation; no context coverage credited.'},'resume':'Withhold findings from producer until initial exact snapshot frozen; then compare exact version.','ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0}
runner.immutable(OUT/'SOURCE_READING.json',runner.encoded(r));m={f.name:runner.sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'reading':m['SOURCE_READING.json'],'manifest':runner.sha((OUT/'MANIFEST.json').read_bytes()),'core_findings':sum(f['scope']=='core' for f in findings),'context_findings':sum(f['scope']=='context' for f in findings)}))
