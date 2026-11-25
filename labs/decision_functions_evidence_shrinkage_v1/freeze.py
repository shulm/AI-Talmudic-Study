"""Create exact pre-fit contracts; no research fixture materialization."""
from contracts import *
if __name__=='__main__':
    atomic(OUT/'EXPECTED.json',contract());atomic(OUT/'environment.json',environment());atomic(OUT/'historical_blobs.json',historical())
    atomic(OUT/'prefit_sources.json',dict(files={p:file_hash(ROOT/p) for p in source_paths()},assignment=BASE,source_names=list(SOURCE_NAMES),comparison_count=len(comparison_ids())))
