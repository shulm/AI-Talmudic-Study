"""First-pass excerpt decisions for the frozen 207-candidate snapshot."""
import json
import hashlib
from pathlib import Path
P=Path(__file__).parent/'rabbah_yosef_results'
SELECT=set(map(int,'''1 3 5 6 9 11 12 13 14 15 17 19 20 24 25 26 28 29 30 32 33 34 35 36 44 45 46 47 49 51
59 61 62 63 64 65 68 70 74 77 79 82 83 84 86 88 91 94 95 96 98 101 102 103
117 119 120 121 122 124 125 126 129 132 133 138 139 140 141 142 143 144 148 150 151 153 155 156 157 163 164 165 166 168 169 170 178 179 180 181 182 183 185 186 188 189 190 191 192 193 201 203'''.split()))
NOTES={
20:'המשך סוגיית שתי הלחם. ההמשך מביא את רבא המסכים לאכילה ומבחין בינו לבין רבה בטעם הגזרה. אין להחליף את שמותיהם.',
9:'רבא דוחה את תירוץ רבה ומביא מסורת רב יוסף בשם רב יהודה בשם שמואל. הבדל תירוצים שהגמרא מציגה, ולא ויכוח ישיר בין רבה לרב יוסף.',
24:'חילוף מסורות על השאלה והתשובה; אין כאן בהכרח פסקי הלכה סותרים.',
125:'הגמרא מוסיפה ואיכא דאפיך להו: אין להציג את הייחוס הראשון כייחוס מוסכם.',
141:'שני פירושים באגדה. לא קשיא שבהמשך מיישב קושיה על רב יוסף מול מימרת רבי אילעאי; אין להסיק מכך שמחלוקת שני הפירושים עצמה בוטלה.',
164:'בנוסח ההקשר מופיעים גם רבה וגם רבא; נשמר נוסח המאגר ללא תיקון. יש לבדוק חילופי נוסח לפני קביעת הייחוס בכל שלבי המעשה.',
165:'בנוסח ההקשר מופיעים גם רבה וגם רבא; נשמר נוסח המאגר ללא תיקון.',
166:'בנוסח ההקשר מופיעים גם רבה וגם רבא; נשמר נוסח המאגר ללא תיקון.',
188:'חד אמר וחד אמר במסירה בשם רבה בר בר חנה בשם רבי מני; הדעות לא יוחסו לרבה ולרב יוסף לפי סדר השמות.',
189:'חד אמר וחד אמר במסירה בשם רבה בר בר חנה בשם רבי מני; הדעות לא יוחסו לרבה ולרב יוסף לפי סדר השמות.'}
def main():
 raw=(P/'candidates.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()=='9f13e361544d093da47833e05d571aa5edb3fcb48217c78b56334a5371af65a9', 'Candidate snapshot changed; remap decisions by stable keys'
 rows=json.loads(raw)
 assert len(rows)==207,'Remap stable keys if the scan changes'
 out=[]
 for r in rows:
  i=r['review_id'];selected=i in SELECT
  agreement=r['kind']=='joint_agreement_candidate' and i not in {57,129,148}
  decision='selected_excerpt_review' if selected else ('excluded_agreement' if agreement else 'needs_review')
  reason='נקרא ציטוט: דעות, תירוצים, מסורות או דרשות חלופיות. לא נבדקה כל הסוגיה.' if selected else ('אמירה משותפת; אינה מחלוקת ביניהם.' if agreement else 'הצימוד לא נבחר בקריאה ראשונית: מעבר נושא, הסכמה, שאלה או ספק הקשר. אין זו הוכחה להעדר מחלוקת בסוגיה.')
  out.append({'key':r['key'],'review_id':i,'ref':r['ref'],'decision':decision,'reason':reason,'note':NOTES.get(i,''),'reconciled':False})
 (P/'review_decisions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
 print('Selected',len(SELECT))
if __name__=='__main__':main()
