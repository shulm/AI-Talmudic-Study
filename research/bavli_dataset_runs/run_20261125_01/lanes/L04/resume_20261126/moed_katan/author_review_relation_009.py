"""Add missing relation F01 from independent frozen-version review."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r009')
a.e('majority_contrast','mk.r007.ashi_pool.c','mk.r007.pappa.c','distinction','4a:17')
a.rows[-1]['uncertainty']=['Direct contrast over the majority condition; neither opinion is marked retracted or finally adjudicated. Common schema distinction represents this contrast; no new relation vocabulary introduced.']
a.save_window(['4a:17'],'review_relation_009.json','Independent review F01 at comparison5fac8984, SHA523ce261690a1690a8defe25d5233bb181fd7e2374cc7b98eab86ef8d69665ab: add the explicit majority-condition contrast between Rav Pappa and Rav Ashi, preserving prior claims, edges and coverage.','475834408f788249ab0ea5760ce6e2e1e6a785e0c51a91d1f0daa29c1423f6f8')
