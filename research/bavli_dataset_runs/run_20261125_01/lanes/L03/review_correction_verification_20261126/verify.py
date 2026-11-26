import json,pathlib,hashlib,collections
ROOT=pathlib.Path(__file__).resolve().parents[5]
HERE=pathlib.Path(__file__).resolve().parent
INPUT=HERE.parent/"rosh_hashanah/review_correction_20261126"
JOB=pathlib.Path("F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah")
SHA="685478e47cbad58e38ac2a3436738429439adaa04b4e4d4f222905f883e93620"
def load(p):return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
sourcepath=pathlib.Path("F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Moed/Rosh Hashanah/Hebrew/Wikisource Talmud Bavli.json")
assert sha(sourcepath)=="9e7dafc69d032964e3004ba417a9020306b0bb6d94b098165d891066ec27942f"
source=load(sourcepath)["text"]; inv=load(JOB/"source_inventory.json");byid={x["id"]:x for x in inv};byref={x["ref"]:x for x in inv}
for x in inv:
 i,j=x["source_index"];assert x["text"]==source[i][j];assert hashlib.sha256(source[i][j].encode()).hexdigest()==x["text_sha256"]
sp=JOB/"snapshots"/(SHA+".json");assert sha(sp)==SHA
snap=load(sp);rs={x["id"]:x for x in snap["records"]};succ={x["supersedes"]:x["id"] for x in rs.values() if x.get("supersedes")}
def active(i):
 seen=set()
 while i in succ:
  assert i not in seen;seen.add(i);i=succ[i]
 return i
reader=load(INPUT/"reader_frozen.json");comp=load(INPUT/"comparison_frozen.json");response=load(INPUT/"RESPONSE_scope_fix.json")
assert sha(INPUT/"reader_frozen.json")==response["reader_sha256"]
assert sha(INPUT/"comparison_frozen.json")==response["comparison_sha256"]
assert sha(INPUT/"verdict_frozen.json")==response["verdict_sha256"]
assert sha(INPUT/"proposal.json")==response["proposal_sha256"]
assert sha(INPUT/"proposal_scope_fix.json")==response["scope_fix_proposal_sha256"]
new=load(INPUT/"proposal.json")["records"]+load(INPUT/"proposal_scope_fix.json")["records"]
assert len(new)==72 and len(response["findings"])==67
for r in new:
 assert r["id"] in rs
 for k,v in r.items():assert rs[r["id"]][k]==v
for r in rs.values():
 for i in r.get("links",[]):assert i in rs
counts=collections.Counter()
def evidence(e):
 x=byid[e["segment_id"]] if "segment_id" in e else byref[e["ref"]]
 i,j=x["source_index"];s=source[i][j];assert 0<=e["start_char"]<e["end_char"]<=len(s);assert s[e["start_char"]:e["end_char"]]==e["quote"]
 return dict(e,ref=x["ref"],source_index=x["source_index"])
for label,rows in [("snapshot",list(rs.values())),("new_rows",new),("reader",reader["records"])]:
 for r in rows:
  for e in r["evidence"]:evidence(e);counts[label]+=1
for r in new:
 for field in ["claim_id","question_id","source_id","target_id"]:
  i=r["content"].get(field)
  if i:assert i in rs and i==active(i)
base=load(JOB/"snapshots"/(response["base_snapshot"]+".json"))
basecells={(x["segment_id"],x["layer"]) for x in base["coverage"] if x["extraction_state"]=="completed"}
newcells={(x["segment_id"],x["layer"]) for x in snap["coverage"] if x["extraction_state"]=="completed"}
assert basecells==newcells
binding={n:dict(path=str(INPUT/n),sha256=sha(INPUT/n)) for n in ["reader_frozen.json","comparison_frozen.json","verdict_frozen.json","RESPONSE_scope_fix.json","proposal.json","proposal_scope_fix.json"]}
checks=dict(snapshot_sha256=SHA,source_sha256=sha(sourcepath),inventory_segments_checked=len(inv),new_rows=72,new_rows_active=sum(r["id"]==active(r["id"]) for r in new),new_rows_superseded_in_same_correction=sum(r["id"]!=active(r["id"]) for r in new),dispositions=67,evidence_counts=dict(counts),coverage_completed_per_layer=dict(collections.Counter(l for _,l in newcells)),coverage_added=0,all_new_row_content_matches_snapshot=True,all_new_typed_endpoints_active=True,all_snapshot_links_resolve=True,bindings=binding)
if __name__=="__main__":print(json.dumps(checks,ensure_ascii=False,indent=2))
