import pathlib,json,importlib.util,sys
sys.dont_write_bytecode=True
B=pathlib.Path(__file__).resolve().parent.parent
read=lambda p:json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
a=read(B/'readings/meilah_supplement002.json');c=read(B/'readings/meilah_supplement002_completion001.json');allr={x['id']:x for x in a['records']+c['records']};r=[allr[i] for i in c['effective_record_ids']]
J=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L06/bavli_meilah');H='a172bef8f41d754c30d756f69e09c34c46aa95d3171610dd605f9742359c4810';p=read(J/'snapshots'/f'{H}.json')
runner=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1/runner.py');sp=importlib.util.spec_from_file_location('r',runner);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()}
def refs(x):return [e['segment_id'] if e['segment_id'].startswith('Meilah ') else segs[e['segment_id']]['ref'] for e in x['evidence']]
if __name__=='__main__':
 layers=sys.argv[1].split(',');pages=sys.argv[2:]
 for ref in a['core_refs_read']:
  if ref.split()[1].split(':')[0] not in pages:continue
  print('\nSOURCE',ref,texts[ref])
  for label,rs in [('R',r),('P',p['records'])]:
   for x in rs:
    if x['layer'] not in layers or x.get('release_state','valid')!='valid':continue
    if ref==refs(x)[0]:print(label,x['id'].replace('meilah_supplement002_completion001.','C.').replace('meilah_supplement002.','B.'),json.dumps(x['content'],ensure_ascii=False))
