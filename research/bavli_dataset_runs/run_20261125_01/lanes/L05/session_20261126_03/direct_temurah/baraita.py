import opening as x
import json
x.records.clear()
add=x.add;cl=x.cl;q=x.q;at=x.at;edge=x.edge
add('b_s','structure',range(25,35),dict(title='Derivations and qualifications of the non-Jewish consecrations baraita',primary=True,boundary='closed',legacy_ids=[]))
roles={25:'Requotation and rabbinic/biblical distinction',26:'Question and sacrilege derivation',27:'Impurity exclusion',28:'Leftover meat derivation',29:'Piggul derivation',30:'Substitution exclusion',31:'Alternative-version substitution derivation',32:'Libation question and baraita derivation',33:'Rabbi Yose stringent view and reason',34:'Altar versus Temple-maintenance qualification and reason'}
for i,r in roles.items():
 add('b_u'+str(i),'utterances',[i],dict(textual_voice='Anonymous Gemara explaining quoted baraita',discourse_role=r,composition='composite'))
 at('b_a'+str(i),i,'Anonymous discussion','anonymous',r,cand=[])
cl('b_c25a',25,'Benefit from non-Jews’ consecrated offerings is prohibited by rabbinic law.',scope='Explaining Rabbi Shimon’s baraita; altar consecrations as restricted at 3a:12')
cl('b_c25b',25,'There is no biblical sacrilege liability for those offerings.',scope='Explaining Rabbi Shimon’s baraita; not Temple-maintenance consecrations')
q('b_q26',26,'Why is there no biblical sacrilege liability?')
cl('b_c26',26,'The חטא–חטא verbal analogy from terumah transfers the בני ישראל exclusion of non-Jews to sacrilege.',scope='Derivation supporting absence of biblical sacrilege liability')
cl('b_c27',27,'The impurity liability passage specifies offerings of בני ישראל and therefore excludes non-Jews’ offerings.',scope='First step in piggul/leftover/impurity exemption derivation')
cl('b_c28',28,'The חילול–חילול analogy transfers the impurity exclusion to leftover sacrificial meat.',scope='Second derivation step; distinct textual link')
cl('b_c29',29,'The עון–עון analogy transfers the leftover-meat exclusion to piggul; all three exclude non-Jews through בני ישראל.',scope='Third derivation step and shared exclusion')
cl('b_c30',30,'Substitution is excluded because the replacement/substitution passage is introduced as addressing בני ישראל.',scope='First version of derivation')
q('b_q31',31,'In the alternate version, why do non-Jews not effect substitution?')
cl('b_c31a',31,'The alternate version links animal substitution to animal tithe and animal tithe to grain tithe.',scope='Alternative-version chain, not an additional mandatory proof')
cl('b_c31b',31,'Grain tithe says בני ישראל, excluding non-Jews; the chain transmits that exclusion to substitution.',scope='End of alternate-version derivation')
q('b_q32a',32,'From where does Rabbi Shimon derive the libation rule?')
cl('b_c32a',32,'A citizen brings libations, while a non-Jew does not bring libations.',scope='Baraita expounding אזרח; distinguish actor from requirement on offering')
q('b_q32b',32,'Could this mean his burnt offering does not require libations?')
cl('b_c32b',32,'ככה teaches that the non-Jew’s burnt offering nevertheless requires libations.',scope='Rejection of removing the offering’s libation requirement')
at('b_a32s',32,'רבי שמעון','quoted_authority','Baraita view whose derivation is being explained')
cl('b_c33a',33,'Rabbi Yose rules stringently in all these cases.',scope='Disagreement with preceding exemptions',holder='Rabbi Yose')
q('b_q33',33,'What is Rabbi Yose’s reason?')
cl('b_c33b',33,'The consecration passage uses לה׳.',scope='Textual reason for Rabbi Yose’s stricter position')
at('b_a33y',33,'רבי יוסי','quoted_authority','Stringent position, distinct from anonymous explanation of reason')
cl('b_c34a',34,'The exemptions under discussion apply to altar consecrations; Temple-maintenance consecrations incur sacrilege liability.',scope='Explicit distinction by type of sanctity')
q('b_q34',34,'Why does the distinction depend on altar versus Temple-maintenance consecration?')
cl('b_c34b',34,'The sacrilege-to-terumah analogy is confined to intrinsic sanctity like terumah, and does not cover the monetary sanctity of Temple-maintenance offerings.',scope='Reason for limiting exclusion; preserve negative application')
for k,ii,a,b,r in [('1',[25],'b_c25a','c19a','qualification'),('2',[25],'b_c25b','c19a','qualification'),('3',[26],'b_c26','b_q26','answer'),('4',[27],'b_c27','c19b','support'),('5',[28],'b_c27','b_c28','support'),('6',[29],'b_c28','b_c29','support'),('7',[30],'b_c30','c19c','support'),('8',[31],'b_c31b','b_q31','answer'),('9',[31],'b_c31a','b_c31b','support'),('10',[32],'b_c32a','b_q32a','answer'),('11',[32],'b_c32b','b_q32b','answer'),('12',[33],'b_c33b','b_q33','answer'),('13',[33],'b_c33b','b_c33a','support'),('14',[34],'b_c34b','b_q34','answer'),('15',[34],'b_c34a','b_c25b','qualification')]:edge('b_e'+k,ii,a,b,r)
notes={25:'Rabbinic prohibition versus absence of biblical liability kept separate, qualified by altar/maintenance distinction.',26:'Question, both חטא anchors and בני ישראל exclusion preserved.',27:'Impurity step retained independently.',28:'חילול analogy and direction preserved.',29:'עון analogy and direction preserved; all three liability categories included.',30:'First substitution derivation retained independently.',31:'Explicit לישנא אחרינא retained; both intermediate links and grain-tithe exclusion preserved.',32:'Actor restriction not confused with offering requirement; hypothetical omission rejected by ככה.',33:'Rabbi Yose named disagreement distinguished from anonymous scriptural explanation.',34:'Intrinsic versus monetary sanctity restriction preserves the negation and limits prior exemption; next segment starts Rav’s separate general lashes rule.'}
coverage=[]
for i in range(25,35):
 for l in x.layers:
  rr=[r['id'] for r in x.records if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==x.inv[i]['id'] for e in r['evidence'])]
  coverage.append(dict(segment_id=x.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if rr else 'none_found_after_pass',record_ids=rr,rationale=('Source reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record found in this layer.' if not rr else '')))
p={k:x.meta[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/temurah',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=x.records,coverage=coverage,open_tails=[])
out=x.W/'baraita_3a3_3a12_v1.json';blob=(json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
if out.exists():assert out.read_bytes()==blob
else:out.write_bytes(blob)
print(len(x.records),'records')
