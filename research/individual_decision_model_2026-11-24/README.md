# Individual decision pilot — 2026-11-24

A bounded, local-CPU experiment: predict a new person's Holt–Laury choices from eight observed Kirby choices. See [RESULTS.md](RESULTS.md) for the human result, [DATA_ADMISSION.md](DATA_ADMISSION.md) for the rejected first dataset and admitted fallback, and [SCHOLAR_AUDIT.md](SCHOLAR_AUDIT.md) for the separate source-feasibility track. Synthetic controls are engineering evidence only.

## Reproduce

Use Python/package versions in `environment.json`. From this directory, in a **fresh copy** (do not overwrite the completed frozen run):

```powershell
python data_pipeline.py
python run_lab.py validate
python test_models.py > synthetic_controls.json
python run_lab.py smoke
```

`resource_smoke_refined.json` records a subsequent timing check on all 304 training people at dimension eight/ten epochs after importing torch. Its reproducible measurement is:

```powershell
python -c "import torch,time; from run_lab import *; d=load('train',True); t=time.process_time(); m=ProfileModel(dim=8,reg=.1,seed=17,epochs=10,population_reg=.1).fit(*fit_args(d)); print(time.process_time()-t)"
```

Update resource measurements honestly in a new run; never reuse an earlier runtime as a newly measured value. The fixed configuration lives in `model_config.json` and `run_lab.py`. Continue:

```powershell
python run_lab.py develop
python run_lab.py freeze
python run_lab.py predict
python run_lab.py score
```

`freeze` requires a signed independent review of exact current file hashes. The checked-in signoff describes this execution; a materially changed experiment needs a new review. Commit the frozen manifest before prediction. `predict` saves all declared probability vectors without loading target labels. `score` reads test labels once, refuses to replace an existing result, and never loads fitted models. Fresh reproduction of this already exposed test is a reproduction, not a new confirmation experiment. Model serialization hashes can vary across environments; regenerate and review a new freeze rather than bypassing hash checks.

Acquisition uses pinned HTTPS URLs, system certificate trust, and a size guard. It downloads about 161 MB of data/artifacts; no model weights or paid API. The SRO data are CC-BY-4.0, credited in DATA_ADMISSION. Cross-Psych is retained locally only for the failed admission audit. Downloads and all participant-level artifacts are ignored by Git. Missing local artifacts can be regenerated; their SHA256 values are in source/split/prediction manifests. Full probability JSONL contains both safe/risky probabilities for each person, decision, budget and method. The compressed NPZ additionally preserves profile-seed and donor-assignment predictions. Seeds/donors are not independent people.

`DATA_CONTRACT.json` specifies canonical observed records. `data_pipeline.py` performs raw mapping and mechanical assertions, creates physical train/validation/test label files, source observations, label-free target scenarios, canonical records and episode memberships. `run_lab.py validate` checks isolation and accounting. `test_models.py` checks synthetic recovery, no-transfer, option-order invariance and probability behavior. Original source reports are not changed; their UI verifier is not a test of this experiment or of scholarly accuracy.

See [scholar/README.md](scholar/README.md) for the read-only source preparation and verification commands. Do not run historical index builders, train a scholar simulator, or score the earlier confirmation set.
