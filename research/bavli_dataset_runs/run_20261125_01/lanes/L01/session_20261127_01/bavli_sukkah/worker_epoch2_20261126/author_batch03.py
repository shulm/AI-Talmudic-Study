import pathlib
exec(pathlib.Path(__file__).with_name('author_batch01.py').read_text(encoding='utf8').split("\ngroup('s1'")[0].replace('sk.e2.b01.','sk.e2.b03.'))
# Embedded diagrams were separately extracted and visually inspected. Preserve all
# raw bytes in primary structure; other evidence uses exact text on either side.
import re
original_add=add
def add(*args,**kwargs):
    rid=original_add(*args,**kwargs); record=records[-1]
    if record['layer']!='structure':
        out=[]
        for e in record['evidence']:
            t=e['quote']; cursor=0
            for match in re.finditer(r'<img[^>]+>',t):
                if cursor<match.start():out.append(dict(e,start_char=e['start_char']+cursor,end_char=e['start_char']+match.start(),quote=t[cursor:match.start()]))
                cursor=match.end()
            if cursor<len(t):out.append(dict(e,start_char=e['start_char']+cursor,end_char=e['end_char'],quote=t[cursor:]))
        record['evidence']=out
    return rid
group('s1','3b:13','4a:4','Reducing excess height with fillings and nullification')
group('s2','4a:5','4a:7','Descending branches at upper and lower height limits')
group('s3','4a:8','4b:3','Platforms, bent walls and excavating a low sukkah')
group('s4','4b:4','4b:5','Raised pillar and the demand for recognizable walls')
group('s5','4b:6','4b:13','Four poles: roof-edge dispute, refutation and corner-post criteria')

u('3b:13','anonymous Gemara','ineffective height reduction')
c('13','3b:13 4a:1','anonymous Gemara','Cushions and bolsters do not reduce a sukkah’s excessive height, even if designated to remain.','height repair by raising floor',['height >20 cubits; soft furnishings placed below'])
a('13','3b:13','anonymous Gemara','anonymous','cushions and bolsters rule');note('3b:13','Read continuation across daf: even express nullification does not make these furnishings effective.')
u('4a:1','anonymous Gemara','reason nullification fails')
c('1','4a:1','anonymous Gemara','His intention is disregarded against ordinary human practice.','ineffectiveness of nullifying cushions and bolsters')
a('1','4a:1','anonymous Gemara','anonymous','reason for failed floor reduction');edge('1','4a:1','c1','c13','support');note('4a:1','Source brackets [לכולהו] preserved in literal evidence; explanation limited to furnishings rather than all fillers.')
u('4a:2','anonymous Gemara','effective nullified fillings','composite')
c('2a','4a:2','anonymous Gemara','Straw explicitly nullified to the floor reduces the height.','height repair',['straw explicitly nullified'])
c('2b','4a:2','anonymous Gemara','All the more so, explicitly nullified earth reduces height.','height repair',['earth explicitly nullified'])
a('2','4a:2','anonymous Gemara','anonymous','straw and earth contrast');edge('2','4a:2','c2b','c2a','analogy');note('4a:2','A-fortiori comparison preserved without inventing dispute on express nullification of straw or earth.')
u('4a:3','anonymous Gemara citing Mishnah','disputed implicit nullification','composite')
c('3a','4a:3','anonymous Gemara','Straw not intended to be removed, and unspecified earth, depend on the dispute of R. Yose and sages.','nonexplicit nullification categories')
c('3b','4a:3','quoted Mishnah','A house filled with straw or pebbles and explicitly nullified has the filling nullified.','cited house-filling rule',['explicit nullification'])
a('3a','4a:3','ר\' יוסי ורבנן','collective','parties in nullification dispute',candidates=['רבי יוסי','רבנן']);a('3b','4a:3','דתנן','quoted_authority','house-filling Mishnah',candidates=['anonymous Mishnah']);note('4a:3','Cited house rule distinguished from sukkah application; next segment supplies inference and R. Yose’s categories.')
u('4a:4','anonymous inference and רבי יוסי','nullification conditions','composite')
c('4a','4a:4','anonymous Gemara reading Mishnah','Without explicit nullification the filling is not nullified.','inference assigned to sages’ side')
c('4b','4a:4','רבי יוסי','Straw not intended for removal is like unspecified earth and is nullified.','implicit nullification',['no planned straw removal; or unspecified earth'])
c('4c','4a:4','רבי יוסי','Earth intended for removal is like unspecified straw and is not nullified.','implicit nullification',['planned earth removal; or unspecified straw'])
a('4a','4a:4','ביטלו אין לא ביטלו לא','anonymous','inference from Mishnah wording',candidates=['anonymous Gemara']);a('4b','4a:4','רבי יוסי','quoted_authority','categories of nullification');edge('4','4a:4','c4b','c3a','support');note('4a:4','Four categories retained; not planning removal differs from explicit nullification and unspecified intention.')

u('4a:5','anonymous Gemara','descending branch shade threshold','composite')
c('5a','4a:5','anonymous Gemara','A roof above twenty cubits is valid when branches descending below twenty provide more shade than sunlight.','upper height reduction',['descending branches below20; shade>sun'])
c('5b','4a:5','anonymous Gemara','If the descending branches lack that shade majority, the tall sukkah remains invalid.','upper height reduction',['shade not greater than sunlight'])
a('5','4a:5','anonymous Gemara','anonymous','branches at twenty-cubit threshold');note('4a:5','Both outcomes conditioned on shade of descending branches, not all roof shade.')
u('4a:6','אביי','proposed permission for sparse descending branches')
c('6','4a:6','אביי','At ten handbreadths, sparse branches descending into the ten may leave the sukkah valid when their sunlight exceeds shade.','lower height threshold',['height10; branches intrude below10; sun>shade'],mode='challenged',status='Rava rejects on uninhabitability grounds at 4a:7')
a('6','4a:6','אביי','speaker','tentative lower-height permission');note('4a:6','סבר למימר marked tentative and challenged; not Abaye’s final established ruling.')
u('4a:7','רבא','rejection of cramped dwelling')
c('7','4a:7','רבא','This is an unpleasant cramped dwelling in which people do not live.','rejection of branches intruding below ten handbreadths')
a('7','4a:7','רבא','speaker','response to Abaye');edge('7','4a:7','c7','c6','objection');note('4a:7','Sparse shade test does not answer lower-height habitability objection.')

u('4a:8','anonymous Gemara','full-width platform against middle wall')
c('8','4a:8','anonymous Gemara','A tall sukkah is valid with a platform spanning the middle wall if the platform has the minimum sukkah area.','platform height repair',['height >20; full span along middle wall; platform adequate area'])
a('8','4a:8','anonymous Gemara','anonymous','middle-wall platform');note('4a:8','Embedded diagram visually inspected: platform spans back wall between side walls. Literal primary interval includes image markup; legal condition derives from text.')
u('4a:9','anonymous Gemara','side platform and bent-wall distances','composite')
c('9a','4a:9','anonymous Gemara','For a side platform, a gap of four cubits from platform edge to wall leaves the sukkah invalid.','side-platform repair',['gap≥4 cubits'])
c('9b','4a:9','anonymous Gemara','A gap of less than four cubits leaves it valid.','side-platform repair',['gap<4 cubits'])
a('9','4a:9','anonymous Gemara','anonymous','side-platform distance rule');note('4a:9','Diagram visually inspected for side placement; four cubits is invalid boundary, unlike the later three-handbreadth wall-creation rule.')
u('4a:10','anonymous Gemara quoting Mishnah','novelty objection','composite')
q('10','4a:10','Does the platform case merely teach bent-wall doctrine already taught for a breached house roof?')
c('10a','4a:10','quoted Mishnah','A house with roof breached and sukkah covering added is invalid if wall-to-cover distance is four cubits, but valid below that.','prior bent-wall example',['wall-to-cover gap threshold4 cubits'])
a('10','4a:10','תנינא','quoted_authority','breached-roof Mishnah',candidates=['anonymous Mishnah']);edge('10','4a:10','q10','c9b','objection');note('4a:10','Question targets novelty, not truth of platform ruling; quoted roof-repair example retained separately.')
u('4a:11','anonymous Gemara','rejected limitation of bent-wall application')
c('11a','4a:11','hypothetical interpreter','Perhaps bent-wall doctrine works only where the existing wall is fit, not for an overheight wall.','possible limitation',mode='rejected',status='rejected by teaching platform case')
c('11b','4a:11','anonymous Gemara','The platform case teaches application even where the original wall was not suitable because of excess height.','novelty of side-platform ruling')
a('11','4a:11','מהו דתימא','anonymous','hypothetical limit and rejection',candidates=['anonymous Gemara']);edge('11','4a:11','c11b','q10','answer');note('4a:11','Hypothetical limitation not installed as actual accepted wall rule.')
u('4a:12','anonymous Gemara','central platform gap rule','composite')
c('12a','4a:12','anonymous Gemara','A central platform in a tall sukkah is invalid where four-cubit gaps to walls prevent the required bent-wall connection.','central platform',['four cubits from edge to walls'])
c('12b','4a:12','anonymous Gemara','With the relevant gaps below four cubits the central platform arrangement is valid.','central platform',['relevant gaps<4 cubits'])
a('12','4a:12','anonymous Gemara','anonymous','central platform');note('4a:12','Retained לכל רוח ורוח wording; no unprinted geometry or extra wall count supplied.')
u('4a:13','anonymous Gemara','repeated-novelty question');q('13','4a:13','Is this again simply the same bent-wall rule?');a('13','4a:13','anonymous Gemara','anonymous','central-platform novelty question');edge('13','4a:13','q13','c12b','objection');note('4a:13','Not a second objection to doctrinal validity, but request for added teaching.')
u('4a:14','anonymous Gemara','multiple-direction application')
c('14a','4a:14','hypothetical interpreter','Perhaps bent-wall applies in one direction but not in every direction.','possible restriction',mode='rejected')
c('14b','4a:14','anonymous Gemara','The central-platform case teaches bent-wall application in multiple directions.','novelty of central platform')
a('14','4a:14','מהו דתימא','anonymous','hypothesis and rejection',candidates=['anonymous Gemara']);edge('14','4a:14','c14b','q13','answer');note('4a:14','Rejected one-direction limitation separated from positive multi-direction teaching.')
u('4a:15','anonymous Gemara','excavation invalidity condition')
c('15','4a:15','anonymous Gemara','Excavating a low sukkah to ten handbreadths fails if the trench edge is three handbreadths from the wall.','creating required wall height',['original height<10; trench reaches10; gap≥3 handbreadths'])
a('15','4a:15','anonymous Gemara','anonymous','low sukkah excavation');note('4a:15','Three handbreadths, not four cubits; contrasting valid limb continues at 4b:1.')
u('4b:1','anonymous Gemara','excavation validity condition')
c('b1','4a:15 4b:1','anonymous Gemara','The excavation is valid when the trench edge lies less than three handbreadths from the wall.','creating required wall height',['original height<10; trench reaches10; gap<3 handbreadths'])
a('b1','4b:1','anonymous Gemara','anonymous','valid excavation limb');note('4b:1','Paired with prior-page case; no freestanding three-handbreadth rule detached from excavation.')
u('4b:2','anonymous Gemara','question comparing thresholds');q('b2','4b:2','Why did the tall platform case allow below four cubits, but excavation requires below three handbreadths?');a('b2','4b:2','anonymous Gemara','anonymous','threshold comparison');note('4b:2','Compares existing tall walls and creation of low walls, not inconsistent units.')
u('4b:3','anonymous Gemara','distinction between existing and newly constituted wall')
c('b3','4b:3','anonymous Gemara','An existing wall suffices with a below-four-cubit bent connection; to constitute a wall one needs a gap below three handbreadths.','resolution of platform/excavation thresholds')
a('b3','4b:3','anonymous Gemara','anonymous','existing vs created wall distinction');edge('b3','4b:3','cb3','qb2','distinction');note('4b:3','Preserved distinct legal operations: bent existing wall versus joining height to create wall.')

u('4b:4','אביי','proposed virtual extension of pillar walls')
c('b4','4b:4','אביי','A ten-handbreadth pillar with adequate sukkah area could use upward extension of its sides as walls.','pillar inside tall sukkah',['pillar height10; sufficient area; original sukkah >20'],mode='challenged',status='rejected by Rava’s recognizable-walls requirement')
a('b4','4b:4','אביי','speaker','tentative gud-asik application');note('4b:4','Tentative סבר למימר, not unconditional permission for any raised platform.')
u('4b:5','רבא','recognizable walls objection')
c('b5','4b:5','רבא','Sukkah requires recognizable walls, absent in this pillar arrangement.','rejection of pillar gud-asik')
a('b5','4b:5','רבא','speaker','recognizable walls reply');edge('b5','4b:5','cb5','cb4','objection');note('4b:5','Objection scoped to pillar configuration; following roof-edge sugya has independently disputed details.')

u('4b:6','baraita: רבי יעקב and חכמים','four-pole dispute','composite')
c('b6a','4b:6','רבי יעקב','Roofing over four planted poles is valid.','baraita four-pole case',status='placement and pole dimensions clarified in following discussion')
c('b6b','4b:6','חכמים','Roofing over those four poles is invalid.','baraita four-pole case')
a('b6a','4b:6','ר\' יעקב','quoted_authority','four-pole permission',candidates=['רבי יעקב']);a('b6b','4b:6','חכמים','collective','four-pole invalidation');note('4b:6','No location or thickness inferred prematurely; later baraita supplies corner-post conditions.')
u('4b:7','רב הונא and רב נחמן','scope dispute and gud-asik rationale','composite')
c('b7a','4b:7','רב הונא','The tannaitic dispute is at the roof edge; R. Jacob applies upward extension, sages do not.','roof-edge interpretation',status='roof-edge dispute not refuted by second challenge; roof-middle consensus is refuted')
c('b7b','4b:7','רב הונא','At the middle of the roof all invalidate.','roof-middle interpretation',mode='rejected',status='explicitly refuted at 4b:9–10')
c('b7c','4b:7','רב נחמן','The dispute concerns the middle of the roof.','alternative location interpretation',status='whether roof edge also disputed remains unresolved at 4b:8')
a('b7a','4b:7','רב הונא','speaker','roof-edge-only interpretation');a('b7b','4b:7','רב נחמן','speaker','roof-middle interpretation');note('4b:7','Two components of Rav Huna separated: only middle consensus explicitly refuted; Rav Nahman’s edge position remains open.')
u('4b:8','anonymous academy','unresolved scope inquiry','composite')
q('b8','4b:8','Does Rav Nahman mean all validate at the roof edge, or both locations are disputed?',status='unreviewed_alternatives')
c('b8a','4b:8','anonymous academy','Perhaps roof-middle alone is disputed and roof edge is valid for all.','first interpretation of Rav Nahman',mode='unresolved',status='תיקו')
c('b8b','4b:8','anonymous academy','Perhaps both roof-middle and roof-edge cases are disputed.','second interpretation of Rav Nahman',mode='unresolved',status='תיקו')
a('b8','4b:8','איבעיא להו','anonymous','unresolved scope inquiry',candidates=['anonymous academy']);edge('b8','4b:8','cb8b','qb8','unresolved_outcome');note('4b:8','תיקו retained; no binary target or resolved attribution to Rav Nahman manufactured.')
u('4b:9','anonymous Gemara quoting baraita','ground-pole counterexample','composite')
c('b9a','4b:9','רבי יעקב','Four poles planted in the ground and roofed over are valid.','explicit ground baraita')
c('b9b','4b:9','חכמים','Those ground poles roofed over are invalid.','explicit ground baraita')
a('b9a','4b:9','ר\' יעקב','quoted_authority','ground-pole validity',candidates=['רבי יעקב']);a('b9b','4b:9','חכמים','collective','ground-pole invalidity');edge('b9','4b:9','cb9a','cb7b','objection');note('4b:9','Separate occurrence of baraita retained because explicit בארץ changes force of objection.')
u('4b:10','anonymous Gemara','explicit refutation of Rav Huna')
c('b10','4b:10','anonymous Gemara','Ground resembles roof-middle, yet R. Jacob permits; Rav Huna’s assertion of consensus invalidity is refuted.','scope of תיובתא')
a('b10','4b:10','anonymous Gemara','anonymous','formal refutation');edge('b10','4b:10','cb10','cb7b','correction');note('4b:10','Explicit תיובתא applies to roof-middle consensus, not automatically every element of Rav Huna’s report.')
u('4b:11','anonymous Gemara','suggested second refutation');q('b11','4b:11','Does restricting dispute to the middle imply roof-edge consensus validity and thus refute Rav Huna twice?');a('b11','4b:11','anonymous Gemara','anonymous','second refutation proposal');edge('b11','4b:11','qb11','cb7a','objection');note('4b:11','Second refutation is proposed, then answered; must not count as sustained תיובתא.')
u('4b:12','anonymous Gemara defending רב הונא','possible response to second refutation')
c('b12','4b:12','רב הונא as defended anonymously','The baraita may dispute both locations and select the middle to show R. Jacob’s stronger permission.','answer to second challenge',status='blocks second refutation; does not undo first')
a('b12','4b:12','אמר לך רב הונא','position_holder','anonymous defense',candidates=['רב הונא']);edge('b12','4b:12','cb12','qb11','answer');note('4b:12','אמר לך marks constructed defense; retained original first refutation and open Rav Nahman scope rather than claiming retraction of both.')
u('4b:13','baraita: רבי יעקב and חכמים','corner-post size criteria','composite')
c('b13a','4b:13','רבי יעקב','Poles count as corner posts if hypothetical carving and division would leave a handbreadth in each direction.','four-pole validity',['potential corner legs each1 handbreadth'])
c('b13b','4b:13','רבי יעקב','Without that capacity the poles do not count as corner posts.','four-pole invalidity',['insufficient corner-leg capacity'])
c('b13c','4b:13','רבי יעקב','Sukkah corner posts require one handbreadth.','general corner-post measure')
c('b13d','4b:13','חכמים','Two walls must meet their full requirements and the third may be one handbreadth.','sages’ wall requirement')
a('b13a','4b:13','ר\' יעקב','quoted_authority','corner-post criterion',candidates=['רבי יעקב']);a('b13b','4b:13','חכמים','collective','two full walls and third handbreadth');edge('b13','4b:13','cb13a','cb9a','qualification');note('4b:13','Hypothetical carving is a dimensional test, not command actually to carve. Two tannaitic wall systems kept distinct; next unit begins minimum height derivation.')

refs=list(ss);core=refs[refs.index('3b:13'):refs.index('4b:13')+1]
assert len(core)==29 and set(core)==set(notes)
coverage=[]
for ref in core:
    sid=ss[ref]['id']
    for layer in r.LAYERS:
        ids=[v['id'] for v in records if (layer=='reconciliation' or v['layer']==layer) and any(e['segment_id']==sid for e in v['evidence'])]
        rationale=notes[ref] if layer=='reconciliation' else 'Source-read '+layer+' pass. '+notes[ref]
        if not ids:rationale+=' No separate '+layer+' record after complete local continuation.'
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p={k:j[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
p.update(owner='/root/sukkah_production',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/sukkah_production',model_id=None),records=records,coverage=coverage,open_tails=[])
r.immutable(BASE/'proposal03.json',r.encoded(p))
print(json.dumps(dict(proposal_sha256=r.sha(r.encoded(p)),records=len(records),segments=len(core))))
