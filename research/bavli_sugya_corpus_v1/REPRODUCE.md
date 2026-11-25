# Reproduce, Validate, and Inspect (`v1.1.0`)

Python 3.12+, `jsonschema`, and Node.js (built-in modules only for reader verification). No external network calls, paid API keys, or model training are used.

From `research/bavli_sugya_corpus_v1`:

```powershell
# 1. Validate cumulative dataset against local pinned Sefaria Wikisource export (all 37 tractates)
python -X utf8 continue_corpus.py validate --source-root "F:\Sefaria-Export-master"
python -X utf8 validate.py --source-root "F:\Sefaria-Export-master"

# 2. Public-only validation (no F:\Sefaria-Export-master required) + public artifact hash check
python -X utf8 continue_corpus.py validate --public-only
python -X utf8 verify_manifest.py

# 3. Run adversarial corruption tests, 7 continuation/rollback/replay tests, and isolated byte-for-byte rebuild
python -X utf8 test_pipeline.py
python -X utf8 test_continuation.py
python -X utf8 test_reproduction.py

# 4. Regenerate & verify Berakhot cumulative JSONL export, compact index, and self-contained Hebrew RTL reader
python -X utf8 continue_corpus.py export
node exports/verify_reader.cjs

# 5. Inspect reconstructed sugyot (including extended B24 and open-right B32) or scholar positions
python -X utf8 examples.py sugya B24
python -X utf8 examples.py sugya B32
python -X utf8 examples.py sugya M04
python -X utf8 examples.py scholar "רבא"
```

To open the interactive offline Hebrew RTL Berakhot reader, open `exports/berakhot_sugya_reader.html` directly in any browser. It supports full-text/title/summary/scholar search, daf and open-tail filtering, toggle between clean display text and raw Wikisource markup, and single-sugya export as `.json` or `.txt` with `CC-BY-SA` attribution.
