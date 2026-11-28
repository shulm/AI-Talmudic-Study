import pathlib,json,importlib.util,sys
sys.dont_write_bytecode=True
B=pathlib.Path(__file__).resolve().parent.parent
read=lambda p:json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
a=read(B/'readings/meilah_supplement003b.json');r=a['proposal']['records']
J=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L06/bavli_meilah');H='376f00e4349914d3550a2c1673e749a1b752aa4d72169022f3267331fe365dbd';p=read(J/'snapshots'/f'{H}.json')
runner=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1/runner.py');sp=importlib.util.spec_from_file_location('r',runner);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()}
def refs(x):return [e.get('ref',e.get('source_ref',e.get('segment_id'))) if e.get('ref',e.get('source_ref',e.get('segment_id'))).startswith('Meilah ') else segs[e['segment_id']]['ref'] for e in x['evidence']]
if __name__=='__main__':
 for ref in a['core_refs']:
  if ref.split()[1].split(':')[0] not in sys.argv[1:]:continue
  print('\nSOURCE',ref,texts[ref])
  for label,rs in [('R',r),('P',p['records'])]:
   for x in rs:
    if x['layer'] not in ['claims','questions'] or x.get('release_state','valid')!='valid':continue
    if ref==refs(x)[0]:print(label,x['id'],json.dumps(x['content'],ensure_ascii=False))
