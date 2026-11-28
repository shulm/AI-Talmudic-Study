"""Preserve rejected attempt; fix only duplicate local attribution record ID."""
from pathlib import Path
text=Path(__file__).with_name('author_batch03.py').read_text(encoding='utf8')
exec(text.replace("a('13','3b:13'", "a('start','3b:13'").replace("'proposal03.json'", "'proposal03_fix01.json'"))
