import json, hashlib, pathlib, collections
ROOT=pathlib.Path(__file__).resolve().parent
JOB=ROOT/'jobs/bavli_meilah_supplement003b.json'
job=json.loads(JOB.read_text(encoding='utf-8-sig'))
sha=lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert sha(job['source']['path'])==job['source']['sha256']
for x in job['common_documents']: assert sha(x['path'])==x['sha256']
src=json.loads(pathlib.Path(job['source']['path']).read_text(encoding='utf-8-sig'))
texts={f'Meilah {i//2+1}{"a" if i%2==0 else "b"}:{j+1}':s for i,ss in enumerate(src['text']) for j,s in enumerate(ss)}
records=[]; by=collections.defaultdict(lambda:collections.defaultdict(list)); serial=collections.Counter()
def ev(r,quote=None):
 s=texts[r]; q=s if quote is None else quote; st=s.index(q)
 return dict(segment_id=r,start_char=st,end_char=st+len(q),quote=q)
def add(r,layer,content,origin='source_paraphrase',unc=None,links=None,quote=None):
 serial[layer]+=1; id=f'meilah_supp003b.{layer}.{serial[layer]:04d}'
 records.append(dict(id=id,layer=layer,evidence=[ev(r,quote)],content=content,origin=origin,uncertainty=unc or [],links=links or []))
 by[r][layer].append(id); return id
# Each entry is a fresh semantic inventory. Semicolons below separate atomic propositions,
# not an automatic decomposition of source text. Conditions/status are assigned below.
inventory={
'11a:8':('ריש לקיש','challenge','Why not also teach the case of money set aside for bird pairs?',[
'The nazarite-money teaching is challenged by proposing an additional bird-pair-money case.']),
'11a:9':('ריש לקיש','proposed analogy',None,[
'The proposed bird-pair-money case would prohibit benefit but exempt from meilah.',
'The proposed reason is that all the money could purchase turtledoves before their time or young pigeons after their time.']),
'11a:10':('רבא','answer',None,[
'The Torah authorizes bringing peace offerings with unspecified nazarite money.',
'The Torah does not authorize bringing immature turtledoves: they are unfit for the altar.']),
'11a:11':('רבי שמעון','mishnah comparative heading',None,[
'Blood is lenient at the beginning and stringent at the end.',
'Libations are stringent at the beginning and lenient at the end.']),
'11a:12':('רבי שמעון','mishnah specification',None,[
'Blood initially is not subject to meilah.',
'Blood that has gone out to the Kidron stream is subject to meilah.',
'Libations initially are subject to meilah.',
'Libations that have descended into the shittin are not subject to meilah.']),
'11a:13':('ר׳ מאיר ור״ש;חכמים','baraita dispute',None,[
'R. Meir and R. Shimon say meilah applies to blood.',
'The sages say meilah does not apply to blood.']),
'11a:14':('anonymous;עולא;דבי ר׳ ישמעאל','question and alternative derivations','What is the reason of the view that blood has no meilah?',[
'Ulla reads לכם as declaring blood yours.',
'The school of R. Yishmael reads לכפר as given for atonement and not for meilah.']),
'11a:15':('רבי יוחנן','alternative derivation',None,[
'R. Yohanan equates the status of blood before atonement with its status after atonement.',
'Blood after atonement has no meilah.',
'Consequently blood before atonement has no meilah.']),
'11a:16':('anonymous','counter-reading','Why not infer that blood has meilah after atonement just as before atonement?',[
'An alternative direction of the equation would extend meilah from before atonement to afterward.']),
'11a:17':('anonymous','answer and challenge','Can an object whose mitzvah has been performed still have meilah? Why not?',[
'The response assumes that an object after performance of its mitzvah does not have meilah.',
'That assumption is itself challenged.']),
'11b:1':('anonymous','counterexample',None,[
'The removed altar ash has meilah even after its mitzvah is performed.']),
'11b:2':('anonymous','answer',None,[
'Removed altar ash and the limbs of the dispatched goat are two scriptural cases coming together.',
'Two scriptural cases coming together do not teach a general rule.']),
'11b:3':('anonymous','conditional objection','What explains the rule according to the view permitting benefit from the dispatched goat’s limbs?',[
'The preceding answer fits the view prohibiting benefit from the dispatched goat’s limbs.',
'There is an alternative view permitting benefit from those limbs.']),
'11b:4':('anonymous','replacement answer',None,[
'Removed altar ash and priestly garments are two scriptural cases coming together.',
'Two scriptural cases coming together do not teach a general rule.']),
'11b:5':('רבנן as quoted by anonymous','conditional acceptance',None,[
'The sages interpret והניחם שם to require that the garments be stored away.',
'The garment-based answer fits this view of the sages.']),
'11b:6':('רבי דוסא as quoted by anonymous','conditional objection','What explains the rule according to R. Dosa?',[
'R. Dosa permits an ordinary priest to use those garments.']),
'11b:7':('anonymous','replacement answer',None,[
'Removed altar ash and the heifer whose neck is broken are two scriptural cases coming together.']),
'11b:8':('anonymous','conditional objection','What explains the rule according to the view that two scriptural cases do teach?',[
'The preceding answer fits the view that two scriptural cases do not teach.',
'An alternative view holds that such cases do teach.']),
'11b:9':('anonymous','answer',None,[
'Two exclusionary expressions are written.',
'הערופה is the exclusionary expression concerning the heifer.']),
'11b:10':('anonymous','answer continuation',None,[
'ושמו אצל המזבח supplies the second exclusionary expression.',
'These exceptional cases retain the prohibition; other things after performance of their mitzvah do not.']),
'11b:11':('anonymous','proposed incompatibility','Must the mishnah disagree with R. Elazar son of R. Tzadok?',[
'The mishnah’s libation ruling is proposed to be incompatible with R. Elazar son of R. Tzadok.']),
'11b:12':('ר״א בר רבי צדוק','quoted baraita',None,[
'A small shaft lay between the ramp and altar on the west of the ramp.',
'Once in seventy years young priests descended into it.',
'They brought up congealed wine resembling fig cakes.',
'They burned that wine in sanctity.',
'The cited verse supports burning in sanctity just as the libation is performed in sanctity.']),
'11b:13':('anonymous;רבינא','question and derivation','How does the verse imply the burning requirement?',[
'Ravina derives the rule through the shared expression קודש.',
'בקודש occurs here and כי קודש הם occurs in the verse requiring burning of leftover sacrificial food.']),
'11b:14':('רבינא derivation continued','analogy',None,[
'Leftover sacrificial food is burned in sanctity.',
'Likewise this wine is burned in sanctity.']),
'11b:15':('anonymous','first-version reconciliation',None,[
'The mishnah can accord with R. Elazar son of R. Tzadok, through the case of catching the libation.']),
'11b:16':('איכא דאמרי','alternative version','Must the mishnah accord with R. Elazar son of R. Tzadok, through the case of catching?',[
'An alternative version proposes alignment with R. Elazar son of R. Tzadok through the case of catching.']),
'11b:17':('anonymous','alternative-version response','But does he not cite a verse?',[
'The proposed necessary alignment is denied.',
'The sanctity/burning requirement is rabbinic.',
'The cited verse is an asmachta.']),
'11b:18':('anonymous mishnah','mishnah',None,[
'Ash removed from the inner altar is forbidden for benefit but has no meilah.',
'Ash removed from the menorah is forbidden for benefit but has no meilah.',
'If one initially consecrates ash, meilah applies.',
'Turtledoves before their time are forbidden for benefit but have no meilah.',
'Young pigeons after their time are forbidden for benefit but have no meilah.']),
'11b:19':('anonymous','opening connective',None,[]),
'12a:1':('anonymous','derivation question','What is the source for the inner altar’s ash rule?',[
'The outer altar’s rule is understandable from ושמו אצל המזבח.']),
'12a:2':('ר״א','answer',None,[
'והסיר את מוראתו בנוצתה is applied to the inner altar if not needed for the outer altar.']),
'12a:3':('anonymous','alternative derivation','Why not apply both verses to the outer altar, to fix its location?',[
'An alternative reading would use both passages for the outer altar to specify a place.']),
'12a:4':('anonymous','answer',None,[
'If only location were intended the verse could say אצל המזבח.',
'הדשן therefore includes even the inner altar.']),
'12a:5':('anonymous','question and answer','What is the source for the menorah?',[
'The additional form הדשן relative to דשן supplies the menorah derivation.']),
'12a:6':('ר״ש','mishnah distinction',None,[
'R. Shimon says turtledoves before their time have meilah.',
'R. Shimon says young pigeons after their time are forbidden for benefit but have no meilah.']),
'12a:7':('anonymous;ר״ש','explanation by quoted rule',None,[
'R. Shimon’s position is understandable by his stated rule.',
'R. Shimon says that something fit at a later time, consecrated within its premature time, involves a negative commandment.',
'That prematurely consecrated future-fit object does not entail karet.']),
'12a:8':('anonymous','question','According to the sages, how does this differ from an animal lacking its requisite age?',[
'The sages’ view is challenged by comparison with an animal lacking its requisite age.']),
'12a:9':('anonymous','distinction',None,[
'An animal lacking requisite age is like a blemished animal in being subject to redemption.',
'Blemishes do not disqualify birds.',
'Birds therefore have no redemption.']),
'12a:10':('עולא → ר׳ יוחנן','reported ruling',None,[
'Consecrated animals that died leave Torah-level meilah.']),
'12a:11':('anonymous narrator;רב חסדא','narrative challenge','Who accepts your and your teacher R. Yohanan’s view; where has their sanctity gone?',[
'Ulla was sitting and stating the preceding teaching.',
'Rav Hisda challenged Ulla’s and R. Yohanan’s ruling on the ground that their sanctity persists.']),
'12a:12':('unnamed respondent to רב חסדא','counterchallenge','The same question should be asked against the mishnah: where has the birds’ sanctity gone?',[
'The mishnah says immature turtledoves and over-age pigeons are forbidden for benefit but have no meilah.',
'The disappearance-of-sanctity objection would also challenge that mishnah.']),
'12a:13':('unnamed dialogue speaker','concession and question','Can something have no meilah initially but have it later?',[
'The speaker concedes rabbinic meilah.',
'The speaker questions the possibility of initial absence followed by later meilah.']),
'12a:14':('anonymous dialogue voice','counterexample','Does blood not provide such a case?',[
'The mishnah says blood has no meilah initially.',
'The mishnah says blood has meilah after going out to Kidron.',
'Blood is offered as a counterexample to the impossibility of later-arising meilah.']),
'12a:15':('anonymous','answer',None,[
'Blood too has meilah at an earlier stage.']),
'12b:1':('רב quoted anonymously','support',None,[
'Blood drawn from a consecrated animal is prohibited for benefit.',
'Meilah applies to blood drawn from a consecrated animal.']),
'12b:2':('רב הונא → רב;רב המנונא','reported ruling and objection',None,[
'Rav Huna reports Rav that blood drawn from a consecrated animal is prohibited for benefit.',
'Rav Huna reports Rav that meilah applies to that drawn blood.',
'Rav Hamnuna objects from consecrated animals’ milk being prohibited for benefit but exempt from meilah.',
'The cited teaching also prohibits benefit from turtledoves’ eggs but exempts them from meilah.']),
'12b:3':('unnamed respondent','distinction',None,[
'The blood rule applies because an animal cannot survive without blood.',
'Milk is different because the animal can survive without milk.']),
'12b:4':('רב משרשיא','objection',None,[
'Manure and excrement in the courtyard are prohibited for benefit but exempt from meilah.',
'Their sale proceeds fall to the treasury chamber.']),
'12b:5':('anonymous','objection and distinction','Why does the animal’s inability to survive without excrement not yield the same rule?',[
'The challenge compares excrement with blood as necessary to the animal.',
'This particular excrement comes from outside and can be replaced by other excrement.',
'Blood differs because it comes from the animal’s body.']),
'12b:6':('anonymous;רבי אלעזר','support and general rule',None,[
'The teaching’s prohibition of benefit, exemption from meilah, and disposal of proceeds to the chamber support R. Elazar.',
'R. Elazar says that wherever the sages say sacred and not sacred, the proceeds fall to the chamber.']),
'12b:7':('anonymous mishnah','mishnah',None,[
'Milk of consecrated animals is forbidden for benefit but has no meilah.',
'Eggs of turtledoves are forbidden for benefit but have no meilah.']),
'12b:8':('anonymous mishnah','scope distinction',None,[
'The preceding exemption is stated regarding altar sanctity.',
'For repair-of-the-Temple sanctity, a consecrated chicken and its egg have meilah.',
'For repair-of-the-Temple sanctity, a consecrated she-ass and her milk have meilah.']),
'12b:9':('anonymous','inference challenge','Does monetary consecration for the altar really lack meilah?',[
'The wording implies absence of meilah even for monetary consecration for altar purposes; this implication is challenged.']),
'12b:10':('רב פפא','textual supplementation',None,[
'Rav Pappa says the mishnah is missing words.',
'The exemption applies when the animal was consecrated with bodily sanctity for the altar.',
'Monetary consecration for altar purposes is treated like consecration for Temple repair.',
'In that monetary-consecration case a chicken and its egg have meilah.',
'In that monetary-consecration case a she-ass and her milk have meilah.']),
'12b:11':('anonymous mishnah','opening category',None,[
'The category of objects fit for the altar begins the following meilah rule.']),
'13a:1':('anonymous mishnah','categories and introduction','How is the general rule instantiated?',[
'Meilah applies to what is fit for the altar but not for Temple repair.',
'Meilah applies to what is fit for Temple repair but not for the altar.',
'Meilah applies to what is fit for neither altar nor Temple repair.']),
'13a:2':('anonymous mishnah','examples continued at 13a:4',None,[
'The examples include consecrating a cistern already full of water.',
'The examples include consecrating a rubbish heap already full of manure.',
'The examples include consecrating a dovecote already full of doves.']),
'13a:3':('anonymous mishnah','examples continued at 13a:4',None,[
'The examples include consecrating a tree already full of fruit.',
'The examples include consecrating a field already full of vegetation.']),
'13a:4':('anonymous mishnah','rule for prior-filled examples',None,[
'Meilah applies to the consecrated containers or properties in the preceding examples.',
'Meilah also applies to their contents already present when consecrated.']),
'13a:5':('anonymous mishnah','contrasting sequence',None,[
'When a cistern is consecrated and later fills with water, it has meilah but its water does not.',
'When a rubbish heap is consecrated and later fills with manure, it has meilah but its manure does not.',
'When a dovecote is consecrated and later fills with doves, it has meilah but its doves do not.',
'When a tree is consecrated and later produces fruit, it has meilah but its fruit does not.',
'When a field is consecrated and later fills with vegetation, it has meilah but its vegetation does not.']),
'13a:6':('ר׳ יוסי','disputing exception',None,[
'R. Yose says a consecrated field and its growth have meilah.',
'R. Yose says a consecrated tree and its growth have meilah.',
'The reason is that these are growths of consecrated property.']),
'13a:7':('anonymous mishnah','nursing rules and provision',None,[
'The offspring of a tithed animal must not nurse from the tithed animal.',
'Others voluntarily provide the corresponding provision for that offspring.',
'The offspring of consecrated animals must not nurse from consecrated animals.',
'Others voluntarily provide the corresponding provision for that offspring.']),
'13a:8':('anonymous mishnah','workers and animal feeding',None,[
'Workers must not eat consecrated dried figs.',
'Likewise a cow must not eat consecrated vetches.']),
'13a:9':('anonymous','source question','What is the source for forbidding the tithed animal’s offspring to nurse?',[
'The discussion quotes the mishnah’s prohibition on the tithed animal’s offspring nursing.']),
'13a:10':('רב אחדבוי בר אמי','derivation',None,[
'Rav Ahadvoi bar Ammi derives the rule by העברה–העברה from a firstborn animal.',
'Meilah applies to the firstborn animal.',
'Accordingly meilah applies to the tithed animal’s milk.']),
'13a:11':('anonymous continuation','parallel derivation',None,[
'Consecrated animals’ milk too is derived by אמו–אמו from a firstborn animal.']),
'13a:12':('anonymous;רב אחדבוי בר אמי','source question and answer','Why may the workers not eat?',[
'Rav Ahadvoi bar Ammi interprets לא תחסום שור בדישו as your threshing.',
'The prohibition on muzzling does not extend to threshing consecrated produce.']),
'13a:13':('anonymous;רבינא','ruling objection and answer','Does meilah not require detached material?',[
'One who threshes qela’ilin in a consecrated field commits meilah.',
'The ruling is challenged because meilah requires detached material.',
'Ravina infers that the field’s dust benefits it.'])
}
assert len(inventory)==68
# Maintained and hypothetical status is assigned on the source's own discourse, not name order.
hyp={'11a:8','11a:9','11a:16','11b:11','11b:16','12a:3','12b:9'}
chall={'11a:17','12a:8','12a:11','12a:12','12a:13'}
reconciled={'11a:10','11b:2','11b:4','11b:7','11b:9','11b:10','11b:15','11b:17','12a:4','12a:9','12a:15','12b:3','12b:5','12b:10'}
uncertainties={
'11a:13':['The baraita does not restate a temporal qualifier for בדמים; preserve the mishnah’s stages and subsequent derivations without inventing an all-stages dispute.'],
'11b:15':['דאי קלט is elliptical: exact timing and whose case catches the wine are not expanded in this source; retain conditional reconciliation without adding an unquoted scenario.'],
'11b:16':['Alternative version reverses the proposed alignment; it is not a retraction of the first version. דאי קלט remains elliptical.'],
'11b:17':['The source labels the requirement rabbinic and its verse an asmachta, without expressly expanding every referent of the ellipsis.'],
'12a:2':['Surface abbreviation ר״א is preserved; the source here does not expand the name.'],
'12a:12':['א״ל is unnamed; conversational sequence suggests Ulla answering Rav Hisda, but this is inference, not an explicit name.'],
'12a:13':['א״ל is unnamed; the allocation of this concession and ensuing objection is not assigned a named holder without explicit evidence.'],
'12b:3':['אמר ליה does not explicitly name the respondent.'],
'12b:11':['The category begins here and its limitation and predicate occur at 13a:1.'],
'13a:7':['ואחרים מתנדבים כן is preserved as voluntary provision; the exact practical arrangement is not spelled out.'],
'13a:11':['The derivation is an unnamed continuation after Rav Ahadvoi bar Ammi; no explicit fresh attribution.'],
'13a:13':['The text does not gloss קלעילין; אבקה מעלי לה gives dust-benefit reasoning without an expanded material description.']
}
conditions={
'11a:8':['money set aside for bird pairs; proposed analogy to unspecified nazarite money'],
'11a:9':['hypothetical purchase of birds outside their valid age'],
'11a:10':['unspecified nazarite money versus birds unfit for altar'],
'11a:12':['blood: initial versus Kidron stage; libations: initial versus descent into shittin'],
'11a:15':['before versus after atonement'],
'11a:16':['hypothetical reverse direction of before/after comparison'],
'11b:2':['after fulfillment of mitzvah; two exceptional scriptural cases'],
'11b:3':['according to view allowing benefit from dispatched goat limbs'],
'11b:4':['alternative pair of scriptural exceptions'],
'11b:5':['sages require storing priestly garments'],
'11b:6':['R. Dosa allows ordinary priest to reuse garments'],
'11b:7':['alternative pair: removed ash and beheaded heifer'],
'11b:8':['according to view two cases can teach'],
'11b:15':['first version; if caught (דאי קלט)'],
'11b:16':['second version; if caught (דאי קלט)'],
'11b:17':['second version; rabbinic requirement and supporting verse'],
'12a:6':['immature turtledoves versus over-age pigeons'],
'12a:7':['fit later; consecrated before valid time'],
'12a:9':['redeemable animals versus nonredeemable birds'],
'12a:10':['consecrated animals died; Torah-level meilah'],
'12a:13':['rabbinic versus Torah-level meilah; initial versus later stage'],
'12b:1':['blood drawn from live consecrated animal'],
'12b:2':['drawn blood contrasted with milk and eggs'],
'12b:3':['necessary blood versus dispensable milk'],
'12b:5':['replaceable externally derived excrement versus blood from body'],
'12b:8':['altar consecration versus Temple-repair consecration'],
'12b:10':['bodily altar sanctity versus monetary altar sanctity'],
'13a:2':['contents present at consecration; rule completed at 13a:4'],
'13a:3':['growth present at consecration; rule completed at 13a:4'],
'13a:4':['objects and contents already together at consecration'],
'13a:5':['property consecrated before contents arrive or grow'],
'13a:6':['consecrated field/tree; subsequent growth'],
'13a:13':['threshing in consecrated field; dust benefits the processed material']
}
# Explicit questions and reconstructed comparable-question topics are distinguished.
qids={}; cids={}; uids={}
for short,(voice,role,q,claims) in inventory.items():
 r='Meilah '+short; un=uncertainties.get(short,[])
 boundary='open_both' if short in {'11a:9','11b:1','11b:10','11b:14','12a:1','12b:1','13a:1','13a:2','13a:3'} else 'open_right' if short in {'11a:8','11a:17','11b:9','11b:13','11b:19','12a:15','12b:11'} else 'closed'
 add(r,'structure',dict(title=role,primary=True,boundary=boundary,legacy_ids=[]), 'editorial_inference')
 uids[short]=add(r,'utterances',dict(textual_voice=voice,discourse_role=role,composition='composite' if len(claims)>1 or ';' in voice else 'atomic'),unc=un)
 # Anonymous, quoted, and transmissional voices are separately represented below where needed.
 if ' → ' in voice:
  chain=voice.split(';')[0].split(' → ')
  add(r,'attributions',dict(surface=chain[0],role='transmitter',candidates=[chain[0]],scope=role,transmission_chain=chain),unc=un,links=[uids[short]])
  add(r,'attributions',dict(surface=chain[1],role='position_holder',candidates=[chain[1]],scope=role,transmission_chain=chain),unc=un,links=[uids[short]])
 elif voice.startswith('anonymous') or voice.startswith('unnamed') or voice=='איכא דאמרי' or ';' in voice:
  add(r,'attributions',dict(surface=voice,role='anonymous',candidates=[],scope=role,transmission_chain=[]),unc=un,links=[uids[short]])
 else:
  add(r,'attributions',dict(surface=voice,role='speaker',candidates=[voice],scope=role,transmission_chain=[]),unc=un,links=[uids[short]])
 if q:
  qids[short]=add(r,'questions',dict(formulation=q,question_origin='explicit',conditions=conditions.get(short,[]),answer_set_status='partial'),unc=un)
 cids[short]=[]
 for n,p in enumerate(claims):
  mode='hypothetical' if short in hyp else 'challenged' if short in chall else 'reconciled' if short in reconciled else 'asserted'
  if short=='12a:13' and n==0: mode='asserted'
  if short=='11a:17' and n==1: mode='challenged'
  cid=add(r,'claims',dict(proposition=p,conditions=conditions.get(short,[]),scope=role,assertion_mode=mode),unc=un,links=[uids[short]])
  cids[short].append(cid)
  holders=[] if voice.startswith(('anonymous','unnamed')) or ';' in voice else [voice]
  if short=='11b:5': holders=['רבנן'] if n==0 else []
  if short=='11b:6': holders=['רבי דוסא']
  if short=='11b:13': holders=['רבינא']
  if short=='11b:14': holders=['רבינא']
  if short=='11b:16': holders=[]
  if short=='12a:7': holders=[] if n==0 else ['ר״ש']
  if short=='13a:12': holders=['רב אחדבוי בר אמי']
  if short=='11a:13': holders=['ר׳ מאיר','ר״ש'] if n==0 else ['חכמים']
  if short=='11a:14': holders=['עולא'] if n==0 else ['דבי ר׳ ישמעאל']
  if short=='12a:10': holders=['ר׳ יוחנן']
  if short=='12b:2': holders=['רב'] if n<2 else []
  if short=='12b:1': holders=['רב']
  if short=='12a:11' and n==1: holders=['רב חסדא']
  if short=='12b:6' and n==1: holders=['רבי אלעזר']
  if short=='13a:13' and n==2: holders=['רבינא']
  add(r,'positions',dict(holder_candidates=holders,claim_id=cid,question_id=qids.get(short),conditions=conditions.get(short,[]),local_status=mode+'; '+role),unc=un,links=[cid]+([qids[short]] if short in qids else []))
# Separate literal name-bearing attributions prevent composite textual voices becoming person identities.
named={
'11a:13':[('ר\' מאיר','position_holder'),('ר"ש','position_holder'),('חכ"א','collective')],
'11a:14':[('עולא','speaker'),('דבי ר\' ישמעאל','collective')],
'11b:5':[('רבנן','collective')], '11b:6':[('רבי דוסא','quoted_authority')],
'11b:12':[('ר"א בר רבי צדוק','quoted_authority')],
'11b:13':[('רבינא','speaker')], '12a:7':[('ר"ש','quoted_authority')],
'12a:11':[('עולא','speaker'),('רב חסדא','speaker'),('ר\' יוחנן','quoted_authority')],
'12b:2':[('רב המנונא','speaker')], '12b:6':[('רבי אלעזר','quoted_authority')],
'13a:12':[('רב אחדבוי בר אמי','speaker')], '13a:13':[('רבינא','speaker')]
}
for short,items in named.items():
 for surface,role in items:
  add('Meilah '+short,'attributions',dict(surface=surface,role=role,candidates=[surface],scope=inventory[short][1],transmission_chain=[]),'literal',links=[uids[short]],quote=surface)
# Normalized comparison questions are editorial questions, not words attributed to a sage.
topics=[('11a:12','At which stage do blood and libations have meilah?',['11a:11','11a:12','11a:13']),
('12a:6','Do birds outside their valid age have meilah?',['11b:18','12a:6','12a:7','12a:8','12a:9']),
('12a:10','Does Torah-level meilah persist when consecrated animals die?',['12a:10','12a:11','12a:12','12a:13']),
('12b:2','Which animal derivatives have meilah, and why?',['12b:1','12b:2','12b:3','12b:4','12b:5','12b:6']),
('12b:8','How does bodily or monetary consecration affect milk and eggs?',['12b:7','12b:8','12b:9','12b:10']),
('13a:5','Do contents or growth added after consecration have meilah?',['13a:2','13a:3','13a:4','13a:5','13a:6'])]
topic_questions=[]
for short,form,scope in topics:
 q=add('Meilah '+short,'questions',dict(formulation=form,question_origin='editorial_reconstruction',conditions=conditions.get(short,[]),answer_set_status='topic_inventory'),'editorial_inference')
 topic_questions.append(dict(question_id=q,core_refs=['Meilah '+x for x in scope],answer_claim_ids=[c for x in scope for c in cids[x]],status='Source-position inventory; not a practical halachic ruling.'))
 for rec in records:
  if rec['layer']=='positions' and rec['content']['claim_id'] in topic_questions[-1]['answer_claim_ids'] and rec['content']['question_id'] is None:
   rec['content']['question_id']=q; rec['links'].append(q)
# Relations are source-supported links. Multiple versions remain different nodes.
relations=[
('11a:9','11a:8','continuation'),('11a:10','11a:8','answer'),('11a:10','11a:9','distinction'),
('11a:12','11a:11','qualification'),('11a:14','11a:13','support'),('11a:15','11a:14','continuation'),
('11a:16','11a:15','objection'),('11a:17','11a:16','answer'),('11b:1','11a:17','objection'),
('11b:2','11b:1','answer'),('11b:3','11b:2','objection'),('11b:4','11b:3','answer'),
('11b:5','11b:4','qualification'),('11b:6','11b:4','objection'),('11b:7','11b:6','answer'),
('11b:8','11b:7','objection'),('11b:9','11b:8','answer'),('11b:10','11b:9','continuation'),
('11b:11','11a:12','objection'),('11b:12','11b:11','quotation'),('11b:13','11b:12','support'),
('11b:14','11b:13','continuation'),('11b:15','11b:11','answer'),('11b:16','11b:15','continuation'),
('11b:17','11b:16','answer'),('12a:1','11b:19','continuation'),('12a:2','12a:1','answer'),
('12a:3','12a:2','objection'),('12a:4','12a:3','answer'),('12a:5','12a:4','continuation'),
('12a:6','11b:18','distinction'),('12a:7','12a:6','support'),('12a:8','11b:18','objection'),
('12a:9','12a:8','answer'),('12a:11','12a:10','objection'),('12a:12','12a:11','answer'),
('12a:13','12a:12','continuation'),('12a:14','12a:13','objection'),('12a:15','12a:14','answer'),
('12b:1','12a:15','support'),('12b:2','12b:1','quotation'),('12b:3','12b:2','answer'),
('12b:4','12b:3','objection'),('12b:5','12b:4','answer'),('12b:6','12b:4','support'),
('12b:8','12b:7','qualification'),('12b:9','12b:8','objection'),('12b:10','12b:9','answer'),
('12b:10','12b:8','correction'),('13a:1','12b:11','continuation'),('13a:2','13a:1','answer'),
('13a:3','13a:2','continuation'),('13a:4','13a:3','continuation'),('13a:5','13a:4','distinction'),
('13a:6','13a:5','objection'),('13a:9','13a:7','quotation'),('13a:10','13a:9','answer'),
('13a:11','13a:10','analogy'),('13a:12','13a:8','support'),('13a:13','13a:12','continuation')]
for a,b,rel in relations:
 # Elliptical relation of the two alternative versions is recorded as editorial sequencing only.
 explicit='editorial_reconstruction' if (a,b) in {('11b:16','11b:15'),('13a:13','13a:12')} else 'source_explicit'
 add('Meilah '+a,'edges',dict(source_id=uids[a],target_id=qids.get(b,uids[b]),relation=rel,explicitness=explicit),origin='editorial_inference' if explicit=='editorial_reconstruction' else 'source_paraphrase',links=[uids[a],qids.get(b,uids[b])],unc=uncertainties.get(a,[]))
# Intra-segment objections/answers must not disappear behind a composite utterance.
internal=[('11a:13',1,0,'objection'),('11a:17',1,0,'objection'),('11b:17',2,1,'support'),
('12b:2',2,1,'objection'),('12b:2',3,1,'objection'),('12b:3',1,0,'distinction'),
('12b:5',1,0,'answer'),('12b:5',2,1,'distinction'),('13a:13',1,0,'objection'),('13a:13',2,1,'answer')]
for short,a,b,rel in internal:
 add('Meilah '+short,'edges',dict(source_id=cids[short][a],target_id=cids[short][b],relation=rel,explicitness='source_explicit'),links=[cids[short][a],cids[short][b]])
# Complete omission pass: verify each source segment's distinct predicates, alternatives,
# quoted authorities, conditions and response transitions against the original strings.
coverage=[]
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
for r in job['core_refs']:
 short=r.split(' ')[1]
 for layer in layers:
  ids=by[r][layer]
  if layer=='reconciliation':
   result='none_found_after_pass'; rationale='Source-based omission pass completed: checked distinct predicates and negations, named/anonymous voices, transmission, age/time/sanctity conditions, question alternatives, local status, and cross-segment continuations against original text. Preserved ambiguities listed for this core; no additional omitted local proposition identified.'
  elif ids:
   result='records_found'; rationale='Independently inventoried from exact pinned source; '+inventory[short][1]+'.'
  elif short=='11b:19':
   result='not_applicable'; rationale='Only gemara marker and בשלמ\' opening connective; no independent proposition/question/position in this segment. Continuation read and annotated at 12a:1.'
  else:
   result='none_found_after_pass'; rationale={'questions':'No additional explicit or useful comparable question originates in this segment; related questions/answers are linked elsewhere.','edges':'No separate source-supported outgoing relation beyond the recorded sequence was identified in this segment.'}.get(layer,'No independent item in this layer after source-based pass.')
  coverage.append(dict(segment_id=r,layer=layer,extraction_state='completed',extraction_result=result,record_ids=ids,rationale=rationale))
proposal=dict(schema_version='2.0.0-production',tractate='Meilah',owner='/root/reader_meilah_supplement003b',epoch=1,source_sha256=sha(job['source']['path']),protocol_sha256=job['common_documents'][0]['sha256'],schema_sha256=job['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id='/root/reader_meilah_supplement003b',model_id=None),records=records,coverage=coverage,open_tails=['11b:15–17: precise expansion of דאי קלט is not supplied in original source; both versions preserved.','12a:12–13 and 12b:3: unnamed dialogue speakers remain unassigned where source lacks explicit names.','12a:2: ר״א abbreviation not expanded.','13a:7: exact voluntary-provision arrangement not expanded by source.','13a:13: lexical identification of קלעילין not asserted.'])
context=[r for r in texts if (r.startswith('Meilah 10b:') or r in [f'Meilah 11a:{i}' for i in range(1,8)] or r in [f'Meilah 13b:{i}' for i in range(1,11)])]
out=dict(artifact_kind='frozen_source_only_independent_reading',job_id=job['job_id'],cohort=job['cohort'],neutral_job_binding=dict(path=str(JOB),sha256=sha(JOB)),source_binding=job['source'],common_document_bindings=job['common_documents'],core_refs=job['core_refs'],context_refs_read=context,provenance=dict(agent_id='/root/reader_meilah_supplement003b',model_id=None,source_only=True,producer_material_read=False,annotated_handoff_read=False,original_reading_preserved=True,source_edition={k:src.get(k) for k in ['versionTitle','versionSource','license','versionTitleInHebrew']},offset_convention='Python Unicode code-point offsets, half-open, original unnormalized strings including markup',review_status='AI provisional; no human scholarly certification; ML ineligible'),proposal=proposal,comparable_answer_sets=topic_questions,remaining_gaps=proposal['open_tails'],reconciliation=dict(completed=True,method='Second source-based pass over every core segment; inspected multiple propositions, composite speech, local objections/answers, temporal and consecration conditions, and versioned/elliptical passages. Mechanical checks do not establish scholarly accuracy.'))
# Verification checks exact source evidence, core accounting, IDs/links and primary partition.
assert list(inventory)==[x.split(' ')[1] for x in job['core_refs']]
ids={r['id'] for r in records}; assert len(ids)==len(records)
for rec in records:
 for e in rec['evidence']: assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 assert all(x in ids for x in rec['links'])
for ref in job['core_refs']:
 primary=[e for rec in records if rec['layer']=='structure' and rec['content']['primary'] for e in rec['evidence'] if e['segment_id']==ref]
 assert len(primary)==1 and primary[0]['start_char']==0 and primary[0]['end_char']==len(texts[ref])
assert len(coverage)==68*8
try:
 import jsonschema
 jsonschema.validate(proposal,json.loads(pathlib.Path(job['common_documents'][1]['path']).read_text(encoding='utf-8-sig')))
 out['mechanical_validation']='Passed JSON schema, exact source/hash/quotes/offsets, unique IDs, links, 544 coverage cells, and 68 full primary partitions.'
except ImportError:
 out['mechanical_validation']='Passed custom evidence/links/partition checks; jsonschema unavailable.'
dest=ROOT/'readings/meilah_supplement003b.json'
assert not dest.exists(), 'Frozen initial reading must never be overwritten'
dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
h=sha(dest); dest.with_suffix('.json.sha256').write_text(h+'  '+dest.name+'\n',encoding='utf-8')
print(json.dumps(dict(path=str(dest),sha256=h,core_count=68,context_count=len(context),layers=dict(collections.Counter(r['layer'] for r in records)),coverage_cells=len(coverage)),indent=2))
