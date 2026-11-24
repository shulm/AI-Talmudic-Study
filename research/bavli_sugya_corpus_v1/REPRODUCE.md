# Reproduce and inspect the bounded pilot

Python3.12.4; jsonschema4.26.0, already available. Source handling/serialization otherwise uses the standard library. No new package installation, paid API, model training or corpus modification occurred. Reproduction replays recorded annotations; it does not claim a fresh model would independently produce identical judgments.

From this directory:

```powershell
python -X utf8 pipeline.py build --source-root 'F:\Sefaria-Export-master'
python make_schema.py
python -X utf8 compile_annotations.py
python -X utf8 validate.py --source-root 'F:\Sefaria-Export-master'
python -X utf8 test_pipeline.py
python -X utf8 test_reproduction.py
python -X utf8 examples.py sugya M04
python -X utf8 examples.py scholar 'רבא'
```

Build reads all37 named source files to construct the inventory; semantic extraction remains fixed to the two pilot intervals. It never falls back silently to merged.json or to another edition. An alternate source root is accepted, but hashes must match the delivered manifest for an exact reproduction. A different source snapshot is a new revision, not an equivalent rebuild. Save independent model or human review files separately; do not overwrite initial annotations.

`validate.py --public-only` checks the included pilot data, schemas, quotations and graph without accessing the original corpus; it does not verify external source hashes. Full validation also checks all37 original source/schema files, actual TOC order, exact source coverage and byte-exact text. `test_reproduction.py` builds in an isolated temporary directory and compares13 generated outputs byte-for-byte; it leaves the delivered data untouched.

`pipeline.py show Berakhot 2 4` displays zero-based page indices2–4, namely2a–3a, removing HTML only for reading. Do not treat this view as canonical text. context/windows.jsonl contains35 overlapping context windows, capped at10 segments/8,000 characters unless a single atomic segment exceeds that limit (explicitly flagged). Initial manual reading used the overlapping page-range batches documented in annotation_manifest.json; the window files support future provider use but are not claimed as35 separate model/API calls.

Live address checks can be repeated using the explicit Sefaria endpoint URLs and selected version in mapping_review.json. Those endpoints may change; historical response hashes and normalized match counts remain the recorded audit. Never regenerate the independently frozen initial review just to obtain agreement.

There is no Gemini adapter making hidden network calls. To change provider later, use a separately versioned annotated result bundle, record exact model/settings/prompt/input hashes and actual provider usage/cost, validate against the contract, and obtain a separate review before promotion. A paid provider requires an authorized budget.
