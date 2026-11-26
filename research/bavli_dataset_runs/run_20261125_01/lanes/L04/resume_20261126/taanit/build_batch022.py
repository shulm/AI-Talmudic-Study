"""Manual 11a:14–11b:3: competing fasting evaluations and explicit qualifications."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','c5556c468e1892e5c71a0064aaf44fd076049e7b85a70f9c000033cf83f5c928').replace('ta.resume008.','ta.resume022.').replace('/root/taanit_continuation_2','/root/taanit_continuation_3')
exec(compile(helper,__file__,'exec'))
def v(k,r,t,p):
 x=c(k,r,t,p,voice='biblical quotation',comp='composite');next(z for z in P['records'] if z['id']==x+'.a')['content'].update(surface='scriptural quotation',role='quoted_authority',candidates=[]);return x
A=c('shmuel.sinner','11a:14','אמר שמואל כל היושב בתענית נקרא חוטא','Shmuel says one who fasts is called a sinner.',who='Shmuel',cond=['undertakes fasting'],status='evaluative teaching contrasted with alternatives below')
A1=c('shmuel.alignment','11a:14','סבר כי האי תנא','The discussion aligns Shmuel with the following tanna.',voice='anonymous explanatory alignment')
Bq=q('kappar.verse.q','11a:14',"דתניא ר' אלעזר הקפר ברבי אומר מה תלמוד לומר (במדבר ו, יא) וכפר עליו מאשר חטא על הנפש",'Rabbi Elazar HaKappar Berabbi asks what the verse means by atoning for sin against the soul.',who='Rabbi Elazar HaKappar Berabbi')
Bq2=q('kappar.sin.q','11a:14','וכי באיזה נפש חטא זה','Against what soul did this person sin?',who='Rabbi Elazar HaKappar Berabbi')
B=c('wine.affliction','11a:14','אלא שציער עצמו מן היין','HaKappar explains the sin as afflicting himself by abstaining from wine.',who='Rabbi Elazar HaKappar Berabbi',cond=['abstention from wine']);e('kappar.answer1','11a:14','אלא שציער עצמו מן היין',B,Bq,'answer');e('kappar.answer2','11a:14','אלא שציער עצמו מן היין',B,Bq2,'answer')
C=c('sinner.afortiori','11a:15',ix['11a:15']['text'],'If afflicting oneself only by abstaining from wine is called sin, abstaining from everything is all the more so.',who='Rabbi Elazar HaKappar Berabbi',comp='composite',status='a fortiori argument');e('sinner.support','11a:15',ix['11a:15']['text'],C,A);e('alignment.support','11a:15',ix['11a:15']['text'],C,A1)
D=c('elazar.holy','11a:16',"ר' אלעזר אומר נקרא קדוש",'Rabbi Elazar says the faster is called holy.',who='Rabbi Elazar',cond=['undertakes fasting'],status='competing evaluation, ability qualification follows')
Dv=v('holy.verse','11a:16','שנאמר (במדבר ו, ה) קדוש יהיה גדל פרע שער ראשו','The Nazirite verse calls him holy and mentions letting his hair grow.');e('holy.proof','11a:16','שנאמר (במדבר ו, ה) קדוש יהיה גדל פרע שער ראשו',Dv,D)
E=c('holy.afortiori','11a:16','ומה זה שלא ציער עצמו אלא מדבר אחד נקרא קדוש המצער עצמו מכל דבר על אחת כמה וכמה','If abstention from one thing merits holy, abstention from everything does all the more.',who='Rabbi Elazar',comp='composite',status='a fortiori argument');e('holy.support','11a:16','ומה זה שלא ציער עצמו אלא מדבר אחד נקרא קדוש המצער עצמו מכל דבר על אחת כמה וכמה',E,D);e('evaluations.distinction','11a:16',ix['11a:16']['text'],D,A,'distinction')
Fq=q('shmuel.holy.q','11a:17','ולשמואל הא איקרי קדוש','How does Shmuel account for the holy designation?')
F=c('hair.holy','11a:17','ההוא אגידול פרע קאי','For Shmuel, that designation concerns the growing hair.',voice='anonymous explanation of Shmuel');e('shmuel.holy.answer','11a:17','ההוא אגידול פרע קאי',F,Fq,'answer');e('hair.qualifies','11a:17','ההוא אגידול פרע קאי',F,Dv,'qualification')
Gq=q('elazar.sinner.q','11a:17',"ולר' אלעזר הא נקרא חוטא",'How does Rabbi Elazar account for the sinner designation?')
G=c('defilement.sin','11a:17','ההוא דסאיב נפשיה','For Elazar, that designation concerns his becoming impure.',voice='anonymous explanation of Rabbi Elazar');e('elazar.sin.answer','11a:17','ההוא דסאיב נפשיה',G,Gq,'answer')
Hq=q('elazar.contradiction.q','11a:18','ומי אמר רבי אלעזר הכי','Did Rabbi Elazar really say that?')
H=c('holy.within','11a:18',"והאמר ר' אלעזר לעולם ימוד אדם עצמו",'Rabbi Elazar also says one should always regard oneself as if a holy one dwells within one’s innards.',who='Rabbi Elazar',status='statement completed on next folio and used as objection')
for z in P['records']:
 if z['id'] in [H,H+'.u',H+'.a',H+'.p']:z['evidence'].append(ev('11b:1','כאילו קדוש שרוי בתוך מעיו'))
e('elazar.objection','11a:18',ix['11a:18']['text'],H,D,'objection')
Hv=v('within.verse','11b:1','שנאמר (הושע יא, ט) בקרבך קדוש ולא אבוא בעיר','Hosea says holy within you, and I will not enter the city.');e('within.proof','11b:1','שנאמר (הושע יא, ט) בקרבך קדוש ולא אבוא בעיר',Hv,H)
I=c('ability.distinction','11b:1','לא קשיא הא דמצי לצעורי נפשיה הא דלא מצי לצעורי נפשיה','The resolution distinguishes one able to bear self-affliction from one unable to bear it.',mode='reconciled',comp='composite',cond=['ability versus inability to bear self-affliction'],status='fasting praise is qualified by ability');e('ability.answer','11b:1','לא קשיא הא דמצי לצעורי נפשיה הא דלא מצי לצעורי נפשיה',I,Hq,'answer');e('ability.qualifies','11b:1','לא קשיא הא דמצי לצעורי נפשיה הא דלא מצי לצעורי נפשיה',I,D,'qualification');e('within.qualifies','11b:1','לא קשיא הא דמצי לצעורי נפשיה הא דלא מצי לצעורי נפשיה',I,H,'qualification')
J=c('lakish.pious','11b:2','ר"ל אמר נקרא חסיד','Resh Lakish gives the designation pious in this fasting discussion.',who='Resh Lakish',status='evaluative designation',unc=['The short נקרא חסיד has no repeated subject in this clause; local fasting context retained without supplementing a contrasting unprinted rule.'])
Jv=v('pious.verse','11b:2',"שנאמר (משלי יא, יז) גומל נפשו איש (חסיד) [צ\"ל חסד] ועוכר שארו וגו'",'Proverbs’s גומל נפשו איש is quoted with printed (חסיד) and corrective [צ"ל חסד], followed by ועוכר שארו.');e('pious.proof','11b:2',ix['11b:2']['text'].split('אמר רב ששת')[0],Jv,J)
K=c('sheshet.student','11b:2','אמר רב ששת האי בר בי רב דיתיב בתעניתא ליכול כלבא לשירותיה','Rav Sheshet disparages a student who fasts, saying a dog may eat his meal.',who='Rav Sheshet',cond=['Torah student fasting'],status='reported rhetorical criticism, not a feeding instruction')
L=c('babylon.public','11b:3','אמר רבי ירמיה בר אבא אין תענית צבור בבבל אלא תשעה באב בלבד','Rabbi Yirmeya bar Abba says there is no public fast in Babylonia except the Ninth of Av.',who='Rabbi Yirmeya bar Abba',cond=['Babylonia'],status='source-defined public-fast category; no expansion to every communal fasting practice')
M=c('scholar.prohibition','11b:3','(אמר) ר\' ירמיה בר אבא אמר ריש לקיש אין תלמיד חכם רשאי לישב בתענית','Resh Lakish, transmitted by Rabbi Yirmeya bar Abba, does not permit a Torah scholar to fast.',who='Resh Lakish',chain=['Rabbi Yirmeya bar Abba','Resh Lakish'],cond=['Torah scholar'])
N=c('heavens.work','11b:3','מפני שממעט במלאכת שמים:','The reason is that fasting diminishes the work of Heaven.',who='Resh Lakish',chain=['Rabbi Yirmeya bar Abba','Resh Lakish']);e('scholar.reason','11b:3','מפני שממעט במלאכת שמים:',N,M)
refs=list(ix);refs=refs[refs.index('11a:14'):refs.index('11b:3')+1]
add('structure.fasting','structure','11a:14',dict(title='Fasting as sin, holiness or piety, and scholar/public-fast restrictions',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs]
notes={'11a:14':'Shmuel evaluation, tanna alignment, two HaKappar questions and wine-affliction answer retained.','11a:15':'Full wine-to-total-abstention a fortiori argument retained.','11a:16':'Elazar alternative, Nazirite verse and opposing a fortiori argument retained.','11a:17':'Both objection questions and distinct hair/impurity responses retained.','11a:18':'Elazar self-contradiction question and exact cross-folio report retained.','11b:1':'Completion, Hosea proof and ability/inability reconciliation retained.','11b:2':'Lakish pious designation, printed corrective verse form and Sheshet rhetorical student criticism retained.','11b:3':'Yirmeya bar Abba public-fast statement kept distinct from his transmission of Lakish’s scholar prohibition and rationale.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory contains only the source-supported answer represented for this exact local question; no exhaustive choice set or task eligibility claimed.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch022.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
