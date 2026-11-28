import json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;j,src=runner.load(Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin'));seg=list(src.values())
items=[
(30,'Beit Hillel initial arrangement alternates a half-slave’s labor for master and self; keep each recipient/day condition.'),
(31,'Beit Shammai objections: master accommodated but person not accommodated; cannot marry slave woman or free woman, separate impediments.'),
(31,'Procreation/world-purpose argument and Isaiah45:18 are grounds against remaining unmarried; do not turn rhetorical question into approved abstention.'),
(32,'Social repair requires coercing master to free him; writing a debt document for half-value separate obligation.'),
(32,'Beit Hillel retracts to teach like Beit Shammai; link to former alternating-day arrangement and2b13 first/later-Mishnah reconciliation without unsupported Ravina allocation.'),
(33,'Universal shofar obligation’s inclusion question answered by child reaching educational age.'),
(33,'Quoted Mishnah allows child to blow on festival without being stopped; preserve distinction between cited permission and educational-obligation interpretation.'),
(34,'Two Megillah universal statements (obligation and eligibility to read) span folio boundary into3a1; do not drop either scope.'),
(35,'Women included; Rabbi Yehoshua ben Levi says women obligated in Megillah reading.'),
(35,'They too were in the miracle is an explicit reason; do not infer additional historical identification.'),
(36,'Zimmun universal obligation inclusion question answered by women and slaves.'),
(36,'Quoted baraita: women form their own zimmun, slaves their own; preserve separate groups, no mixed-group permission inference.'),
(37,'Joining zimmun inclusion: minor who knows to whom blessings are addressed.'),
(37,'Rav Nahman’s cited statement supports counting such a minor; distinct from Rav himself.'),
(38,'Universal zav-impurity inclusion: infant one day old.'),
(38,'Rabbi Yehuda derives infant inclusion from doubled איש איש; preserve text and derivation separate from outcome.'),
(39,'Rabbi Yishmael son of Rabbi Yohanan ben Beroka says doubled phrase is unnecessary; disagreement over derivation, not exclusion of infant.'),
(39,'His male-word derivation includes males young and old; female-word includes females young and old.'),
(39,'Alternative reading of איש איש: Torah speaks in human language; link as alternative rationale, no invented halakhic dispute.'),
(40,'Corpse-impurity inclusion includes minor.'),
(40,'Rejected hypothesis from איש would exclude minor; resolved by ועל הנפשות אשר היו שם.'),
(41,'Follow-up question asks remaining function of איש; answer excludes minor from karet, not impurity itself.'),
(42,'Lesion impurity includes minor; rejected איש צרוע hypothesis would exclude minor.'),
(43,'Challenge asks why not retain that exclusion; אדם כי יהיה בעור בשרו supports broad inclusion.'),
(44,'Question asks remaining function of איש; cited baraita’s והצרוע includes woman.'),
(45,'איש applies to following rule: man performs פריעה and פרימה, woman does neither; separate gender/act conditions, no exclusion from lesion impurity.'),
(46,'Universal lesion-inspection qualifications include a person initially not proficient in lesions and their names.'),
(47,'Contrary teaching excludes the unproficient; retain tension before reconciliation.'),
(47,'Ravina distinguishes one who understands explanation from one who does not; connect conditions to permitted/forbidden inspection, not unconditional incompetence permission.'),
(48,'Universal eligibility לקדש: Rabbi Yehuda inclusion is minor; rabbis inclusion is woman.'),
(48,'Quoted majority rule excludes deaf-mute, person without legal competence, minor; do not silently conflate exclusion list with Rabbi Yehuda’s amendment.'),
(48,'Rabbi Yehuda qualifies minor, disqualifies woman, disqualifies androgynos; separate outcomes and holder.'),
(49,'Universal sprinkling eligibility includes uncircumcised man.'),
(49,'Rabbi Elazar explicitly named after abbreviation ר״א; his stated outcome is validity of performed sprinkling. Preserve source basis and avoid unsupported expanded ruling.'),
]
findings=[]
for ix,(i,note) in enumerate(items,1):
 s=seg[i];findings.append(dict(id=f'ar003.source.{ix:03}',scope='core',ref=s['ref'],source_index=s['source_index'],segment_id=s['id'],quote=s['text'],finding=note))
reading=dict(reader='/root',source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],source_inventory_count=len(seg),core_scope=dict(start=seg[30]['ref'],end=seg[49]['ref'],indices=[seg[30]['source_index'],seg[49]['source_index']],count=20),next_ref=seg[50]['ref'],context_read=[dict(ref=s['ref'],source_index=s['source_index'],text_sha256=s['text_sha256']) for s in seg[27:30]+seg[50:61]],passes=runner.LAYERS,findings=findings,exposure='Independent of Arakhin production; root previously reviewed Arakhin002 and its contextual2b14–16 labels. Those three readings are reuse with disclosed exposure, not fresh blindness. No Arakhin003 labels seen; freeze precedes dispatch.',limitations=['Purposive sequential source-first review, not random or fresh blind cohort.','No external interpretive expansion of local terms needed for these source-backed findings.','Continued next unit through3b9 read to establish boundaries; no additional covered cores.'],ml_eligible=False)
runner.immutable(out/'SOURCE_READING.json',runner.encoded(reading));runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:runner.sha(p.read_bytes()) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(reading_sha256=runner.sha((out/'SOURCE_READING.json').read_bytes()),findings=len(findings),manifest_sha256=runner.sha((out/'MANIFEST.json').read_bytes()))))
