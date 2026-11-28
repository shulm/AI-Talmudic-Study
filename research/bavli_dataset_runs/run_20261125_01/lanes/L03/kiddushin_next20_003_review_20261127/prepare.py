import sys,json
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;j,s=runner.load(Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin'));seg=list(s.values())
notes=[
(30,'Two source questions: money effects betrothal, and father owns daughter’s betrothal money. Distinguish listed money/document/intercourse rights from proofs sought here.'),
(31,'Rav Yehuda reports Rav: Exodus21:11 no money for this master implies money for another master, identified as father.'),
(32,'Challenge proposes daughter receives money; response father receives her betrothal from את בתי נתתי so she cannot simply take money instead.'),
(33,'Challenge distinguishes minor without receiving capacity from naara who can receive; hypothesis she betroths herself and takes money.'),
(33,'Provisional בנעוריה בית אביה response generalizes youth benefits to father; argument is rejected/narrowed below, not final unrestricted monetary principle.'),
(34,'Rav Huna reports Rav’s separate daughter-earnings derivation from sale as maidservant, analogizing earnings to master/father.'),
(34,'Redundancy objection: why derive earnings if youth-benefits verse sufficed?'),
(35,'בנעוריה is about vow annulment; money cannot be learned from prohibition-domain rule. Apply restriction to prior proposed money proof.'),
(36,'Proposed fine analogy rejected: ordinary money cannot be derived from penal payment.'),
(37,'Proposed shame/damage analogy distinguished because father has his own involvement in those payments.'),
(38,'Corrected comparable-exit derivation begins and crosses folio into4a1; preserve originalindices and linked sentence.'),
(39,'Exclusion concerns comparable exit; father’s money right no longer relies on rejected all-benefits principle.'),
(40,'Objection contrasts complete departure from master versus daughter still requiring entry to chuppah.'),
(40,'Response: she has at least left father’s sole annulment domain; father and husband jointly annul betrothed naara’s vows, cited Mishnah. Do not assert complete paternal release.'),
(41,'Challenge that verse already supplies maturity/adolescence emancipation.'),
(41,'Quoted baraita maps ויצאה חנם to bogrut and אין כסף to naarut; separate phrases/outcomes.'),
(42,'Ravina uses extra yod אין versus אן to retain no money for this master but money for another, father.'),
(43,'Question seeks warrant for spelling-based derivation; priestly-woman seed verse begins.'),
(44,'Baraita initially derives descendants of descendants from זרע אין לה/עיין לה.'),
(44,'Baraita also derives invalid offspring; preserve separate queried class and answer.'),
(45,'Objection asks how same phrase supplies both uses.'),
(45,'Correction: descendants’ descendants need no special verse since grandchildren count as children; extra expression needed for invalid offspring. Earlier derivation superseded as necessity, not outcome.'),
(46,'Why may tanna read this spelling? מאן בלעם and ומאן יבמי lack yod but אין here has it, warranting exposition.'),
(47,'Both betrothal and earnings verses needed: betrothal alone might favor father because daughter did not labor for it; earnings could be hers.'),
(48,'Converse: earnings alone might favor father because he feeds her; externally arriving betrothal money could be hers. Preserve both hypotheses and צריכא outcome.'),
(49,'Gufa repeats bogrut/naarut mapping; retain repeated occurrence, not duplicate unique-topic claim.'),
(49,'Why write bogrut if naarut already releases her? Core question open until contextual answers.'),
(50,'Rabbah says one expression teaches about other; רבה distinct from רבא.'),
(51,'Toshav acquired permanently and sakhir for years are separate classifications.'),
(52,'Proposed redundancy inference: permanent servant barred from eating, term servant all the more.'),
(53,'Without second term first could be misread as term servant; second clarifies first includes permanent servant’s exclusion.'),
(54,'Abaye objects two-person analogy differs; Scripture can state conclusion already available by qal-vahomer.'),
(55,'Here same person already leaves at adolescence, so maturity clause unnecessary; objection to Rabbah analogy.'),
(56,'Abaye proposes bogrut of ailonit as needed case.'),
(57,'Hypothesis release at adolescence but not bogrut is rejected by verse.'),
(58,'Mar bar Rav Ashi objects a fortiori: signs not releasing from father release from master; maturity releasing from father should release from master.'),
(59,'Mar bar Rav Ashi instead applies verse to initial validity of ailonit sale; hypothesis sale of one never attaining signs invalid.'),
(60,'Verse rejects invalid-sale hypothesis; crossfolio continuation retained.'),
(61,'Distinguish explicit qal-vahomer repetition with no alternative reading from available alternative exposition. Do not flatten answers into consensus.')
]
findings=[dict(id=f'kid003.source.{n:03}',scope='core' if i<50 else 'context',ref=seg[i]['ref'],source_index=seg[i]['source_index'],segment_id=seg[i]['id'],quote=seg[i]['text'],finding=t) for n,(i,t) in enumerate(notes,1)]
r=dict(reader='/root',source_sha256=j['source_sha256'],source_inventory=len(seg),core_refs=[seg[30]['ref'],seg[49]['ref']],core_indices=[seg[30]['source_index'],seg[49]['source_index']],new_cores=20,next_ref=seg[50]['ref'],passes=runner.LAYERS,findings=findings,continuation_read_through='Kiddushin4b6; core question continuation closes4b2, new money-proof unit4b3–6 inspected',context_refs=[x['ref'] for x in seg[27:30]+seg[50:66]],exposure='Root never produced Kiddushin; prepared previous002 source reading and saw bounded comparison summaries, not003 labels. Freeze before003dispatch. Purposive sequential reading, no random/fresh-cohort claim.',qualification=False)
runner.immutable(out/'SOURCE_READING.json',runner.encoded(r));runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={p.name:runner.sha(p.read_bytes()) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'})))
print(json.dumps(dict(reading_sha256=runner.sha((out/'SOURCE_READING.json').read_bytes()),findings=len(findings),core_findings=sum(x['scope']=='core' for x in findings))))
