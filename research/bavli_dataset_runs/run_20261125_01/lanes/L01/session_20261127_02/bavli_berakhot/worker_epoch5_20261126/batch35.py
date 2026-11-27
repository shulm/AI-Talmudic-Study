from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.dead_guarding.20261127e5.'
assert r.sha(r.encoded(state))=='17c9dcdec07635019ddaf68eb5073e498ba50a0cebeda9e0b017fecc593ed469'
refs=['17b:'+str(i) for i in range(12,18)]+['18a:'+str(i) for i in range(1,13)]
for k,rr,title in [('m',refs[:4],'Mishnah: dead before him, bearers and consolation row'),('before',refs[4:9],'Meaning of before him and burial duty'),('guard',refs[9:15],'Guarding the dead and cemetery distance'),('bones',refs[15:17],'Transporting bones and Torah scroll in danger'),('escort',refs[17:],'Accompanying the dead')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Anonymous Mishnah','Anonymous Mishnah','Anonymous Mishnah','Anonymous Mishnah with parenthetical appended rule','Anonymous literal-scope inference','Baraita of eating and mourning','Baraita continuation and Rabban Shimon ben Gamliel','Rabbi Yohanan distinction','Rav Pappa and Rav Ashi alternative readings','Anonymous proposed exclusion','Baraita and anonymous synthesis','Anonymous inference and cemetery baraita objection','Anonymous distance distinction','Guarding baraita and Ben Azzai','Ravina explains difference','Transport baraita','Anonymous scope analysis','Rahava/Rav Yehuda and Rav Assi']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Conditional obligation, scope argument or reward teaching',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('12','17b:12','One whose dead lies before him is exempt from Shema, prayer, tefillin and all Torah commandments.',['Anonymous Mishnah'],cond=['Own dead lies before him'],unc=['18a3 offers literal-location versus burial-responsibility readings; do not assume only physical proximity.'])
claim('13shema','17b:13','The Mishnah discusses bier bearers and their successive replacements, those before and behind; its printed wording exempts needed persons before and obligates needed persons behind.',['Anonymous Mishnah'],status='Printed positional distinction',unc=['Pinned string repeats צורך בהם for before and behind. Preserve literal text rather than silently emending or assuming missing negation; fuller functional distinction needs review.'])
claim('13prayer','17b:13','Both groups are exempt from prayer.',['Anonymous Mishnah'],cond=['Bier-party groups described in same segment'])
claim('14','17b:14','After burial and return, they begin Shema if able to begin and finish before reaching the consolation row; otherwise they do not begin.',['Anonymous Mishnah'],cond=['Returning after burial','Enough time before row'])
claim('15row','17b:15','Those in the inner consolation row are exempt and those outside are obligated.',['Anonymous Mishnah'],cond=['Consolation row position'])
claim('15append','17b:15','A parenthetical clause exempts women, servants and minors from Shema and tefillin and obligates them in prayer, mezuzah and grace after meals.',['Parenthetical Mishnah text'],status='Appended parenthetical source clause, not silently relocated or omitted')
q('q16','17b:16','Does before him mean only physically before him, excluding a dead person not before him?')
claim('17place','17b:17','The baraita orders eating in another house, otherwise a friend’s house, otherwise behind a partition, otherwise turning one’s face.',['Anonymous baraita'],cond=['Dead lies before him','Each earlier alternative unavailable'])
claim('17meal','17b:17','He does not recline, eat meat, drink wine, bless or join zimmun.',['Anonymous baraita'],cond=['Weekday acute mourner case'])
claim('1weekday','18a:1','Others do not bless or count him for zimmun, and he is exempt from Shema, prayer, tefillin and all commandments.',['Anonymous baraita'],cond=['Weekday acute mourner case'])
claim('1shabbat','18a:1','On Shabbat he reclines, eats meat, drinks wine, blesses, joins zimmun and is included by others, and is obligated in commandments.',['Anonymous baraita'],cond=['Shabbat'])
claim('1rsg','18a:1','Rabban Shimon ben Gamliel says obligation in these entails obligation in all.',['Rabban Shimon ben Gamliel'],cond=['Shabbat'],status='Additional formulation whose practical difference is identified next')
claim('2','18a:2','Rabbi Yohanan says marital intercourse is the difference between the views.',['Rabbi Yohanan'],status='Identifies disputed subject',unc=['This short statement does not explicitly restate which view permits; do not assign by sequence alone.'])
claim('3pappa','18a:3','Rav Pappa interprets the exemption clause as the case of turning his face and eating.',['Rav Pappa'],status='Literal-proximity reconciliation')
claim('3ashi','18a:3','Rav Ashi treats a person obligated to bury the deceased as though the deceased lies before him, using Abraham’s before my dead language.',['Rav Ashi'],cond=['Burial responsibility remains'],status='Responsibility-based reconciliation')
q('q4','18a:4','Does own dead imply a mere guardian is not exempt?')
claim('5guard','18a:5','The cited baraita exempts one guarding a dead person even if not one’s own, from Shema, prayer, tefillin and all commandments.',['Anonymous baraita'],cond=['Guarding dead person'])
claim('5both','18a:5','The synthesis exempts a guardian even when it is not his dead, and one’s own dead even when not guarding.',['Anonymous Gemara'])
q('q6','18a:6','Does this exclude walking in a cemetery, despite the ban on visible tefillin and Torah reading there?')
claim('6','18a:6','The baraita forbids walking in a cemetery with tefillin on the head and a Torah scroll on the arm while reading, as mocking the poor and insulting his Maker.',['Anonymous baraita'],cond=['Cemetery conduct described'])
claim('7','18a:7','The cemetery ban concerns four cubits; beyond four one is obligated, whereas the guardian/own-dead exemption applies beyond four cubits too.',['Anonymous Gemara'],cond=['Four-cubit proximity versus guardian/burial responsibility'])
claim('8two','18a:8','When two guard a dead person, they alternate guarding and reciting.',['Anonymous baraita'],cond=['Two guardians'])
claim('8ben','18a:8','Ben Azzai says on a ship they place the dead in one corner and both pray in another.',['Ben Azzai'],cond=['Traveling on ship'])
claim('9','18a:9','Ravina identifies the difference as whether one fears mice.',['Ravina'],status='Explicit explanatory difference',unc=['מר סבר/מר סבר not explicitly named here; contextual mapping is not used to invent a direct named quote.'])
claim('10bones','18a:10','One transporting bones must not put them in a saddlebag on a donkey and ride over them, because this is degrading.',['Anonymous baraita'],cond=['Transporting bones'])
claim('10danger','18a:10','Fear of non-Jews or robbers permits that arrangement; the same teaching applies to a Torah scroll.',['Anonymous baraita'],cond=['Fear of attackers in source travel context'])
q('q11','18a:11','Does the Torah-scroll comparison concern the initial prohibition or the final permission?')
claim('11','18a:11','The comparison concerns danger permission; prohibition would be obvious, since a Torah scroll is not inferior to bones.',['Anonymous Gemara'])
claim('12duty','18a:12','Rav Yehuda through Rahava says one who sees the dead and does not accompany him violates mocking the poor and insulting his Maker.',['Rav Yehuda'],cond=['Sees dead','Does not accompany'])
q('q12','18a:12','What is the reward for accompanying?')
claim('12reward','18a:12','Rav Assi applies lending to God through kindness to the poor and honoring Him by favoring the needy.',['Rav Assi'],status='Exegetical reward description')
for k,ref,surface,name in [('1','18a:1','רשב"ג','רבן שמעון בן גמליאל'),('2','18a:2','ר יוחנן','רבי יוחנן'),('3p','18a:3','רב פפא','רב פפא'),('3a','18a:3','רב אשי','רב אשי'),('8','18a:8','בן עזאי','בן עזאי'),('9','18a:9','רבינא','רבינא'),('12a','18a:12','רב אסי','רב אסי')]:att('a'+k,ref,surface,'speaker',[name],'Local explicit ruling or explanation')
att('a12r','18a:12','רחבה אמר רב יהודה','transmitter',['רחבה'],'Escort duty transmission',chain=['רחבה','רב יהודה'])
for k,ref,a,b,rel in [('2','18a:2','c2','c1rsg','qualification'),('3p','18a:3','c3pappa','q16','answer'),('3a','18a:3','c3ashi','q16','answer'),('3d','18a:3','c3ashi','c3pappa','distinction'),('5','18a:5','c5both','q4','answer'),('5s','18a:5','c5guard','c5both','support'),('6','18a:6','c6','q6','support'),('7','18a:7','c7','q6','answer'),('8','18a:8','c8ben','c8two','qualification'),('9','18a:9','c9','c8ben','qualification'),('10','18a:10','c10danger','c10bones','qualification'),('11','18a:11','c11','q11','answer'),('12','18a:12','c12reward','q12','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local acute mourning, bier, guardian and cemetery rules. Preserve anomalous printed bearer wording, parenthetical appended clause, proximity versus burial responsibility, Shabbat and travel-danger qualifications.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read17b12–18b17; reread core17b12–18a12 for printed bier-party anomaly, row/timing conditions, parenthetical women clause, all meal-location alternatives, Shabbat difference without forced mapping, Pappa/Ashi alternatives, guardian scope, four cubits, ship/mice and danger-permitted transport. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch35_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch35_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch35_receipt.json',r.encoded(out));print(r.encoded(out).decode())
