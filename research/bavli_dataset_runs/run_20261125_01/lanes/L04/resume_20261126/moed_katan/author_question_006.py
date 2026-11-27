"""Source-reread addition: explicit internal baraita question at3a:8."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r006')
question=a.question('analogy','3a:8','זריעה בכלל היתה ולמה יצתה','Why was sowing singled out when it was already included?')
a.e('analogy_answer','mk.r004.analogy.c',question,'answer','3a:8')
a.save_window(['3a:8'],'question_006.json','Targeted source reread restores the explicit internal question separately from the already retained derivation claim; preserves all prior active coverage records and adds no new covered segment.','8b868e951311f175f748bb7a9a7b42d3fe741e814264fc071f6c72a16728636b')
