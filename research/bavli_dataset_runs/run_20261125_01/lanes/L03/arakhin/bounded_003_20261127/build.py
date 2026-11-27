import json,pathlib,hashlib,copy
D=pathlib.Path(__file__).parent;J=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');ROOT=pathlib.Path.cwd();C=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x):
 p=D/n;assert not p.exists();p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
active=read(C/'research/bavli_dataset_runs/ACTIVE_RUN.json');contract=read(C/active['contract_path']);assert h(C/active['contract_path'])==active['contract_sha256']
for f,digest in contract['production_files'].items():assert h(ROOT/f)==digest
job=read(J/'JOB.json');owner=read(J/'OWNER.json');assert owner=={'owner':'/root/lead_l01_l03','epoch':1};base='18bb932d660d694686e98f376d9aa8e2feeedb8e1e328affb1cd3ab0cee49cf5';assert read(J/'CURRENT.json')['snapshot_sha256']==base;assert h(J/f'snapshots/{base}.json')==base
src=pathlib.Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Kodashim/Arakhin/Hebrew/Wikisource Talmud Bavli.json');assert h(src)==job['source_sha256'];raw=read(src)['text'];inv=read(J/'source_inventory.json');seg={x['ref'].replace('Arakhin ',''):x for x in inv};cores=[x['ref'].replace('Arakhin ','') for x in inv[30:50]];old=read(J/f'snapshots/{base}.json');existing={x['id']:x for x in old['records'] if x['release_state']=='valid'};rows=[];P='ar.e1.b003.';rev={}
for x in inv:
 a,b=x['source_index'];assert raw[a][b]==x['text']
def ev(ref):
 x=seg[ref];return dict(segment_id=x['id'],start_char=0,end_char=len(x['text']),quote=x['text'])
def refs(x):return x.split('|') if isinstance(x,str) else x
def ID(x):return x[1:] if x.startswith('@') else P+x
def add(k,layer,rr,content,links=(),origin='source_paraphrase',sup=None,unc=()):
 x=dict(id=P+k,layer=layer,evidence=[ev(z) for z in refs(rr)],content=content,origin=origin,links=[ID(z) for z in links],uncertainty=list(unc))
 if sup:x['supersedes']=sup;rev[sup]=x['id']
 rows.append(x);return x
scope='Local inclusive-formula discussion; exact conditions and argument stages retained, not a claim of later practical ruling'
def c(k,rr,t,holder='anonymous Gemara',cond=(),mode='asserted',status='asserted locally',sup=None):
 add(k,'claims',rr,dict(proposition=t,conditions=list(cond),scope=scope,assertion_mode=mode),sup=sup)
 add(k+'.p','positions',rr,dict(holder_candidates=[holder],claim_id=P+k,question_id=None,conditions=list(cond),local_status=status),[k],sup=(sup+'.pos') if sup else None)
def q(k,rr,t):add(k,'questions',rr,dict(formulation=t,question_origin='explicit',conditions=[],answer_set_status='partial'))
def e(k,rr,a,b,relation):add(k,'edges',rr,dict(source_id=ID(a),target_id=ID(b),relation=relation,explicitness='source_explicit'),[a,b])
def attr(k,rr,surface,who,role='quoted_authority',scope0='',chain=()):add(k,'attributions',rr,dict(surface=surface,candidates=who,role=role,scope=scope0,transmission_chain=list(chain)))
# Immutable successor closes the previous appearance structure; prior source ownership retained.
s=copy.deepcopy(existing['ar.e1.b002.s3']);s={k:v for k,v in s.items() if k in ['id','layer','evidence','content','origin','links','uncertainty']};s['id']=P+'appearance';s['supersedes']='ar.e1.b002.s3';rev[s['supersedes']]=s['id'];s['evidence'] += [ev(z) for z in cores[:3]];s['content']['boundary']='closed';s['content']['title']='Festival appearance alternatives and cited half-slave Mishnah through Beit Hillel retraction';rows.append(s)
for k,rr,title in [('mitzvot',cores[3:8],'Shofar, Megillah and zimmun inclusions and capacities'),('impurity',cores[8:16],'Infant/minor impurity, verse allocations and male/female afflicted-person duties'),('inspection',cores[16:18],'Inspection expertise and Ravina understanding qualification'),('sanctify',cores[18:19],'Purification-water preparation eligibility: Rabbi Judah and sages'),('sprinkle',cores[19:20],'Uncircumcised sprinkler: Rabbi Elazar validation')]:add(k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
roles=['Quoted initial Beit Hillel alternating service','Beit Shammai marriage and creation-purpose objection','Compelled freeing,half-value debt,and Beit Hillel retraction','Shofar educational-age inclusion','Megillah inclusive formulas,question continues','Women inclusion and Yehoshua ben Levi miracle reason','Separate women/slave zimmun groups','Knowing whom one blesses minor, Rav Nahman report','One-day infant zivah, Rabbi Judah duplication proof','Yishmael son of Yohanan ben Beroka alternative proof and ordinary-language reading','Minor corpse impurity; rejected exclusion and נפשות proof','איש excludes minor from karet','Minor lesion impurity; tentative exclusion','Challenge answered by אדם inclusive wording','Woman inclusion from והצרוע','Male-only hair/garment duties','Nonexpert lesion examiner inclusion','Conflicting teaching; Ravina understanding distinction','Sanctification eligibility: Judah/sages inclusions and exceptions','Uncircumcised sprinkling inclusion; Rabbi Elazar']
for n,(ref,role) in enumerate(zip(cores,roles)):
 add('u'+str(n),'utterances',ref,dict(textual_voice='anonymous Gemara with explicitly quoted voices where marked',discourse_role=role,composition='composite'))
 add('frame'+str(n),'attributions',ref,dict(surface='anonymous framing',role='anonymous',candidates=[],scope='Question/report framing only; named speakers separately retained: '+role,transmission_chain=[]))
# Reuse initial schedule and retraction. Split prior compound context claims now entering core coverage.
attr('bh','2b:14','דברי ב״ה',['Beit Hillel'],scope0='Initial alternating-service view, retracted at2b16')
attr('bs','2b:15|2b:16','אמרו להם ב״ש',['Beit Shammai'],scope0='Objection and corrective freeing solution')
c('no_slave_marriage','2b:15','The half-slave half-free person cannot marry a slave woman.','Beit Shammai', ['Half slave and half free'],sup='ar.e1.r002.objection')
c('no_free_marriage','2b:15','The half-slave half-free person cannot marry a free woman.','Beit Shammai',['Half slave and half free'])
c('master_only','2b:15','The initial arrangement repairs the master’s situation but does not repair the person’s own situation.','Beit Shammai',['Initial alternating-service arrangement'])
q('idle','2b:15','Should the person remain without procreation?')
c('creation','2b:15','The world was created for procreation/inhabitation, as לא תוהו בראה לשבת יצרה is cited.','Beit Shammai')
e('purpose_answer','2b:15','creation','idle','answer');e('free_objection','2b:15','no_free_marriage','@ar.e1.r002.initial','objection');e('master_objection','2b:15','master_only','@ar.e1.r002.initial','objection')
c('compel_free','2b:16','For תיקון העולם the master is compelled to free the person.','Beit Shammai; subsequently accepted by Beit Hillel',['Half slave and half free'],sup='ar.e1.r002.freeing')
c('debt','2b:16','The freed person writes a debt instrument for half his value.','Beit Shammai; subsequently accepted by Beit Hillel',['Compelled freeing of the half-slave half-free person'])
e('debt_scope','2b:16','debt','compel_free','qualification');e('free_answer','2b:15|2b:16','compel_free','idle','answer')
q('shofar_q','2b:17','What does the inclusive shofar obligation add?');c('shofar_minor','2b:17','It includes a minor who has reached education age.',cond=['Minor reached education age']);c('shofar_allow','2b:17','The quoted Mishnah says not to prevent a minor from sounding on Yom Tov.','quoted Mishnah');e('shofar_a','2b:17','shofar_minor','shofar_q','answer');e('shofar_proof','2b:17','shofar_allow','shofar_minor','support')
q('megillah_q','2b:18|3a:1','Whom do the inclusive Megillah obligation and reading-eligibility formulas add?');c('women_obligated','2b:18|3a:1','Women are obligated in Megillah reading.','Rabbi Yehoshua ben Levi');c('women_eligible','2b:18|3a:1','The inclusive Megillah reading-eligibility formula includes women.',cond=['Local הכל כשרין לקרות formula; no broader audience-discharge ruling supplied']);c('miracle','3a:1','Women too were in that miracle.','Rabbi Yehoshua ben Levi');attr('rybl','3a:1','דאמר ר׳ יהושע בן לוי',['Rabbi Yehoshua ben Levi'],scope0='Women Megillah obligation and miracle reason');e('meg_a1','2b:18|3a:1','women_obligated','megillah_q','answer');e('meg_a2','2b:18|3a:1','women_eligible','megillah_q','answer');e('miracle_reason','3a:1','miracle','women_obligated','support')
q('zim_q','3a:2','Whom does the inclusive zimmun obligation add?');c('women_zim','3a:2','Women make zimmun for themselves.','quoted baraita', ['Women group separately']);c('slaves_zim','3a:2','Slaves make zimmun for themselves.','quoted baraita',['Slave group separately']);e('zim_w','3a:2','women_zim','zim_q','answer');e('zim_s','3a:2','slaves_zim','zim_q','answer')
q('join_q','3a:3','Whom does the inclusive joining-zimmun formula add?');c('minor_join','3a:3','A minor who knows to whom the blessing is addressed may be counted for zimmun.','Rav Nahman',['Minor knows whom one blesses']);attr('nahman','3a:3','דאמר רב נחמן',['Rav Nahman'],scope0='Knowing whom one blesses condition');e('join_a','3a:3','minor_join','join_q','answer')
q('zivah_q','3a:4','Whom does the inclusive zivah-impurity formula add?');c('infant_zivah','3a:4','An infant one day old can become impure through zivah.','Rabbi Judah',['One-day-old infant']);c('ish_double','3a:4','Rabbi Judah derives the infant inclusion from איש איש.','Rabbi Judah');attr('judah_zivah','3a:4','דברי רבי יהודה',['Rabbi Judah'],scope0='Infant zivah inclusion via duplicated איש');e('zivah_a','3a:4','infant_zivah','zivah_q','answer');e('zivah_proof','3a:4','ish_double','infant_zivah','support')
c('male_all','3a:5','לזכר includes every male, whether minor or adult.','Rabbi Yishmael son of Rabbi Yohanan ben Beroka');c('female_all','3a:5','לנקבה includes every female, whether minor or adult.','Rabbi Yishmael son of Rabbi Yohanan ben Beroka');c('proof_unneeded','3a:5','The duplicated איש proof is unnecessary because male/female wording already includes young and old.','Rabbi Yishmael son of Rabbi Yohanan ben Beroka');q('double_use','3a:5','What then does איש איש teach?');c('human_language','3a:5','The Torah speaks in ordinary human language here.','Rabbi Yishmael son of Rabbi Yohanan ben Beroka');attr('yishmael','3a:5','רבי ישמעאל בנו של רבי יוחנן בן ברוקה',['Rabbi Yishmael son of Rabbi Yohanan ben Beroka'],scope0='Alternative inclusive proof and ordinary-language account; full patronymic retained');e('male_ground','3a:5','male_all','proof_unneeded','support');e('female_ground','3a:5','female_all','proof_unneeded','support');e('proof_alternative','3a:4|3a:5','proof_unneeded','ish_double','distinction');e('language_a','3a:5','human_language','double_use','answer')
q('corpse_q','3a:6','Whom does inclusive corpse impurity add?');c('minor_corpse','3a:6','A minor is susceptible to corpse impurity.');c('corpse_exclude','3a:6','One might infer from איש אשר יטמא that only an adult and not a minor becomes impure.',mode='rejected',status='Tentative exclusion rejected by inclusive נפשות');c('nefashot','3a:6','ועל הנפשות אשר היו שם supports inclusion of minors.');e('corpse_a','3a:6','minor_corpse','corpse_q','answer');e('corpse_proof','3a:6','nefashot','minor_corpse','support');e('corpse_correct','3a:6','minor_corpse','corpse_exclude','correction');q('ish_exclude','3a:7','What does איש exclude instead?');c('minor_karet','3a:7','The minor is excluded from karet.');e('karet_a','3a:7','minor_karet','ish_exclude','answer')
q('lesion_q','3a:8','Whom does inclusive lesion impurity add?');c('minor_lesion','3a:8','A minor is susceptible to lesion impurity.');c('lesion_exclude','3a:8','One might read איש צרוע as including an adult but excluding a minor.',mode='rejected',status='Rejected tentative exclusion; source answer follows3a9');e('lesion_a','3a:8','minor_lesion','lesion_q','answer');q('perhaps_exclude','3a:9','Why not indeed exclude the minor?');c('adam','3a:9','אדם כי יהיה בעור בשרו includes the person without that age exclusion.');e('adam_a','3a:9','adam','perhaps_exclude','answer');e('adam_proof','3a:8|3a:9','adam','minor_lesion','support')
q('ish_need','3a:10','Why is איש needed in the lesion passage?');q('woman_source','3a:10','From איש only a man is stated; what includes a woman?');c('woman_lesion','3a:10','והצרוע includes a woman along with the man.','quoted baraita');e('woman_a','3a:10','woman_lesion','woman_source','answer')
c('man_hair','3a:11','The afflicted man leaves his hair unbound.','quoted baraita');c('man_tear','3a:11','The afflicted man rends his garments.','quoted baraita');c('woman_nohair','3a:11','The afflicted woman does not leave her hair unbound under this rule.','quoted baraita');c('woman_notear','3a:11','The afflicted woman does not rend her garments under this rule.','quoted baraita');
for n,k in enumerate(['man_hair','man_tear','woman_nohair','woman_notear']):e('ish_duty'+str(n),'3a:10|3a:11',k,'ish_need','answer')
q('inspect_q','3a:12','Whom do the inclusive lesion-inspection eligibility formulas add?');c('nonexpert','3a:12|3a:13','The inclusion allows one not expert in the lesions and their names, provided explanation enables understanding.',cond=['Not expert in lesions and their names','Can understand when explained'],status='Initial inclusion qualified by Ravina at3a13');c('noexpert_quote','3a:13','The cited teaching says one not expert in lesions and their names does not inspect.','quoted authority',status='Objection qualified by Ravina distinction');q('inspect_conflict','3a:13','How can nonexpert inclusion stand against the teaching excluding nonexperts?');c('understands','3a:13','Ravina distinguishes the case where explanation makes him understand.','Ravina',['Explanation given','He understands'],status='Permitting branch of distinction');c('no_understand','3a:13','Where explanation does not make him understand, the exclusion applies.','Ravina',['Explanation given','He does not understand']);attr('ravina','3a:13','אמר רבינא',['Ravina'],role='speaker',scope0='Understanding after explanation distinction');e('inspect_a','3a:12|3a:13','nonexpert','inspect_q','answer');e('inspect_obj','3a:13','noexpert_quote','nonexpert','objection');e('understand_a','3a:13','understands','inspect_conflict','answer');e('notunderstand_a','3a:13','no_understand','inspect_conflict','answer');e('understand_scope','3a:13','understands','nonexpert','qualification');e('no_understand_scope','3a:13','no_understand','noexpert_quote','qualification')
q('sanctify_q','3a:14','Whom does הכל כשרין לקדש include?');c('judah_minor','3a:14','Rabbi Judah includes a minor as eligible to sanctify the purification water.','Rabbi Judah');c('sages_woman','3a:14','For the sages the inclusive formula includes a woman as eligible to sanctify the purification water.','sages');e('sanctify_j','3a:14','judah_minor','sanctify_q','answer');e('sanctify_s','3a:14','sages_woman','sanctify_q','answer')
for k,t in [('deaf','חרש'),('incompetent','שוטה'),('minor','קטן')]:c('sages_no_'+k,'3a:14','The first Mishnah view excludes '+t+' from sanctifying the purification water.','first Mishnah view / sages')
c('judah_nowoman','3a:14','Rabbi Judah disqualifies a woman from sanctifying the purification water.','Rabbi Judah');c('judah_noandrogynos','3a:14','Rabbi Judah disqualifies an androgynos from sanctifying the purification water.','Rabbi Judah');attr('judah_water','3a:14','רבי יהודה מכשיר',['Rabbi Judah'],scope0='Minor validation, woman and androgynos disqualification');e('minor_difference','3a:14','judah_minor','sages_no_minor','distinction');e('woman_difference','3a:14','judah_nowoman','sages_woman','distinction')
q('sprinkle_q','3a:15','Whom does inclusive sprinkling eligibility add?');c('uncircumcised','3a:15','Sprinkling performed by an uncircumcised person is valid.','Rabbi Elazar',['Uncircumcised sprinkler']);attr('elazar','3a:15','דא״ר אלעזר',['Rabbi Elazar'],scope0='Valid sprinkling by uncircumcised person; full name anchors abbreviation');e('sprinkle_a','3a:15','uncircumcised','sprinkle_q','answer')
# Rewrite dependent prior records immutably until references are all live.
def replace(x):
 if isinstance(x,str):return rev.get(x,x)
 if isinstance(x,list):return [replace(z) for z in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
again=True
while again:
 again=False
 for oid,rec in existing.items():
  if oid in rev:continue
  clean={k:copy.deepcopy(v) for k,v in rec.items() if k in ['id','layer','evidence','content','origin','links','uncertainty']}
  test=replace(clean)
  if test!=clean:
   nid=P+'revised.'+oid;rev[oid]=nid;test['id']=nid;test['supersedes']=oid;rows.append(test);again=True
# Apply complete map to dependencies while retaining each supersedes original.
for rec in rows:
 rec['content']=replace(rec['content']);rec['links']=replace(rec['links'])
coverage=[]
for oldc in old['coverage']:
 newc=replace(oldc)
 if newc!=oldc:
  newc.pop('proposal_execution',None);coverage.append(newc)
active_rows={k:v for k,v in existing.items() if k not in rev};active_rows.update({x['id']:x for x in rows})
for ref in cores:
 sid=seg[ref]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[x['id'] for x in active_rows.values() if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  why='Source reread: BH retraction preserved; compound prior context split; distinct marriage exclusions/freeing/debt; educational capacities; women/slaves separate zimmun; male/female infant proof alternatives; minor impurity versus karet; male/female lesion duties; Ravina understanding qualification; Judah/sages water preparation and Elazar sprinkling. Continuation3a16–3b3 inspected as next distinct inclusive topics. No independent reader labels seen.' if layer=='reconciliation' else ('Evidence-linked records including reused prior context; source indices preserved.' if ids else 'Read original segment: no additional explicit question/attribution/edge in this layer; no invented content.')
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version='2.0.0-production',tractate='Arakhin',owner=owner['owner'],epoch=1,source_sha256=job['source_sha256'],protocol_sha256=job['protocol_sha256'],schema_sha256=job['schema_sha256'],execution=dict(route='interactive_agent',agent_id='/root/blind_review',model_id=None),records=rows,coverage=coverage,open_tails=[])
assert len(cores)==20 and len({x['id'] for x in rows})==len(rows)
for rec in rows:
 for z in rec['links']:assert z in active_rows,z
write('PINS.json',dict(base_snapshot_sha256=base,owner=owner,active_run=active,contract_sha256=h(C/active['contract_path']),production_files_verified=True,source_sha256=h(src),source_manifest_sha256=h(J/'source_manifest.json'),core_refs=[seg[z]['ref'] for z in cores],core_indices=[seg[z]['source_index'] for z in cores],context_read=['Arakhin2b11–13','Arakhin3a16–3b3'],revision_map=rev,independent_reading_seen=False))
write('INITIAL_PROPOSAL.json',p);print(len(rows),len(rev),h(D/'INITIAL_PROPOSAL.json'))
