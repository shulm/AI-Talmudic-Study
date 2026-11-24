"""Read-only inventory, conservative overlap grouping, and frozen 30-family draw."""
import collections, hashlib, html, json, random, re, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PAIRS = {'rav_shmuel':['Rav','Shmuel'], 'abaye_rava':['Abaye','Rava'], 'yochanan_lakish':['Rabbi Yohanan','Resh Lakish'], 'rabbah_yosef':['Rabbah','Rav Yosef']}
STRATA = {'civil_property':['Bava Batra','Bava Kamma','Bava Metzia'], 'shabbat_festival':['Shabbat','Eruvin','Pesachim','Sukkah','Beitzah','Yoma','Rosh Hashanah','Moed Katan','Chagigah'], 'prayer_blessing':['Berakhot']}
def dump(name, data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def lines(name, data):
    (HERE/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),encoding='utf8')
def clean(s):
    return re.sub(r'\s+',' ',re.sub('[\u0591-\u05bd\u05bf-\u05c7]','',html.unescape(re.sub('<[^>]*>','',s)))).strip()
def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    indexes={}; manifest=[]; nodes={}; refs=collections.defaultdict(list)
    for pair,people in PAIRS.items():
        path=ROOT/f'{pair}_results/{pair}_index.json'; data=json.loads(path.read_text(encoding='utf8')); indexes[pair]=data['entries']
        manifest.append({'pair':pair,'path':str(path.relative_to(ROOT)).replace('\\','/'),'sha256':sha(path.read_bytes()),'git_blob_sha1':subprocess.check_output(['git','hash-object',str(path)],cwd=ROOT,text=True).strip(),'occurrences':len(data['entries']),'branches':dict(collections.Counter(e['branch'] for e in data['entries']))})
        for e in data['entries']:
            key=f'{pair}:{e["id"]}'; nodes[key]={'occurrence_id':key,'pair':pair,'ref':e['ref'],'entry':e}
            for ref in set([e['ref']]+[u['ref'] for u in e.get('source_units',[])]): refs[ref].append(key)
    parent={k:k for k in nodes}
    def find(k):
        while parent[k]!=k: parent[k]=parent[parent[k]]; k=parent[k]
        return k
    edges=[]
    for ref,ks in sorted(refs.items()):
        for i,k in enumerate(sorted(ks)):
            for other in sorted(ks)[i+1:]:
                parent[find(other)]=find(k)
                edges.append({'left':k,'right':other,'shared_ref':ref,'relationship':'indexed_context_overlap','interpretation':'conservative grouping; overlap may be incidental, not proof of common question'})
    groups=collections.defaultdict(list)
    for k in nodes: groups[find(k)].append(k)
    family={k:'fam_'+sha('|'.join(sorted(ks)).encode())[:12] for ks in groups.values() for k in ks}
    mapping=[{'occurrence_id':k,'ref':v['ref'],'pair':v['pair'],'family_id':family[k],'grouping_status':'provisional_context_component'} for k,v in sorted(nodes.items())]
    lines('occurrence_family_map.jsonl',mapping); lines('family_relationships.jsonl',edges)
    lines('cross_inventory_overlap.jsonl',[e for e in edges if nodes[e['left']]['pair']!=nodes[e['right']]['pair']])
    graph={'scholars':list(sum(PAIRS.values(),[])), 'case_nodes':[{'family_id':family[ks[0]],'occurrences':len(ks),'observed_scholars':sorted(set(p for k in ks for p in PAIRS[nodes[k]['pair']]))} for ks in groups.values()], 'edges_are':'Inventory co-occurrence, not certified individual answers; no silence labels.', 'common_scale_identified':False}
    dump('person_case_overlap_graph.json',graph); dump('source_manifest.json',{'indexes':manifest,'seed':20261123,'grouping':'union of shared indexed context references, no semantic parallel certification'})
    rng=random.Random(20261123); selected=[]; pools={}; used=set(); reserves=[]
    for stratum,works in STRATA.items():
        eligible={}
        for e in indexes['rav_shmuel']:
            if e['branch']=='Bavli' and e['work'] in works:
                f=family[f'rav_shmuel:{e["id"]}']
                if f not in eligible or (e['work'],e['json_index'])<(eligible[f]['work'],eligible[f]['json_index']): eligible[f]=e
        ordered=sorted(eligible); pools[stratum]=ordered
        shuffled=ordered[:]; rng.shuffle(shuffled)
        if stratum in ['civil_property','shabbat_festival']:
            reserves.append((stratum,shuffled[10],eligible[shuffled[10]]))
        for f in [f for f in shuffled if f not in used][:10]:
            e=eligible[f]; used.add(f); selected.append({'attempt_id':f'RS{len(selected)+1:02}','family_id':f,'stratum':stratum,'occurrence_id':f'rav_shmuel:{e["id"]}','ref':e['ref'],'source_file':e['source_file'],'json_index':e['json_index']})
    for stratum,f,e in reserves:
        selected.append({'attempt_id':f'RS{len(selected)+1:02}','family_id':f,'stratum':stratum,'occurrence_id':f'rav_shmuel:{e["id"]}','ref':e['ref'],'source_file':e['source_file'],'json_index':e['json_index'],'replacement_reason':'Next shuffled family after manual answer-bearing linkage reduced initial 30 components to 28: RS09/RS10 and RS11/RS13.'})
    dump('pilot_selection.json',{'seed':20261123,'strata':STRATA,'procedure':'For each stratum in listed order, sort provisional family hashes; Python Random(seed).shuffle; first 10 unused. Focal occurrence minimum (work,json_index). Two recorded next-in-order replacements, preserving all original attempts.','eligible_family_pools':pools,'selected':selected})
    evidence=[]; readings=[]
    for s in selected:
        p=Path(s['source_file']); raw=p.read_bytes(); d=json.loads(raw); pi,si=s['json_index']; units=[]
        # Complete preceding, focal and following amud, preserving raw spans and normalized reading view.
        for a in range(max(0,pi-(2 if s['attempt_id']=='RS32' else 1)),min(len(d['text']),pi+(4 if s['attempt_id']=='RS17' else 2))):
            for j,t in enumerate(d['text'][a]):
                units.append({'ref':f'{d["title"]} {a//2+1}{"a" if a%2==0 else "b"}:{j+1}','json_index':[a,j],'raw_text':t,'text':clean(t)})
        e={**s,'source_sha256':sha(raw),'version_title':d.get('versionTitle'),'versions':d.get('versions'),'source_units':units,'review_level':'ai_single','context_extracted':f'{len(set(u["json_index"][0] for u in units))} complete amudim; extraction is not reading certification'}; evidence.append(e)
        focal=next(u for u in units if u['json_index']==[pi,si]); i=units.index(focal)
        readings.append(s['attempt_id']+' '+s['ref']+' '+s['stratum']+'\n'+'\n'.join(u['ref']+' '+u['text'] for u in units[max(0,i-4):i+13]))
    lines('evidence_context.jsonl',evidence); (HERE/'reading_windows.txt').write_text('\n\n'.join(readings),encoding='utf8')
    print(json.dumps({'counts':manifest,'selected':[(s['attempt_id'],s['ref']) for s in selected]},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
