"""Preserve rejected proposal; disambiguate challenge and answer edge IDs."""
from pathlib import Path
text=Path(__file__).with_name('author_batch04.py').read_text(encoding='utf8')
exec(text.replace("edge('cherub','5b:4'", "edge('cherub_answer','5b:4'").replace("'proposal04.json'", "'proposal04_fix01.json'"))
