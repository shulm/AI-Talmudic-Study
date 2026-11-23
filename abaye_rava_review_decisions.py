"""First-pass excerpt decisions for the 2026-11-23 scan; never full-sugya certification.

IDs refer to the frozen review_candidates.json. Exported decisions also carry stable keys.
Unselected records remain available for further review; omission is not a negative finding.
"""
import json
from pathlib import Path

P = Path(__file__).parent / 'abaye_rava_results'
EXCLUDE = set(map(int, '''31 84 98 185 186 232 250 264 265 270 296 307 309
366 368 370 395 426 435 467 483 493 500 547 553 554 557 590 604 613
626 629 673 708 712 716 726 740 746 763 768 785 789 799 806 835 881
893 901 905 924 956 957 963 969 973 1001 1003 1015 1019'''.split()))
UNCERTAIN = set(map(int, '198 260 326 387 463 659 739 751 886 1035'.split()))
ADD = set(map(int, '''2 4 7 10 12 13 14 21 26 41 46 50 68 72 78 96 97 113
124 130 131 133 134 142 146 152 157
181 184 192 193 214 215 239 242 249 251 252 253 254 258 266 267 273 278
280 281 289 290 305 315 318 329 333 340 345 359 360 361 377 382 383
384 386 398 402 431 455 459 480 484 485 488 489 496 504 507 511 516 518
525 530 532 533 540 549 556 559 570 576
596 599 600 602 612 616 622 630 633 634 636 639 640 642 644 651 653 656
661 665 667 679 682 683 710 722 723 724 725 728 737 738 752 754 756 759
762 764 766 783 784 788 793
796 814 815 821 831 849 855 862 869 887 894 900 909 911 913 920 962 980
995 1016 1017 928 930
122 123 223 224 227 453 884
230'''.split()))
# 230 added in the 2026-11-23 review: Megillah 8b, Abaye rejects Rava's derivation and gives his own.

SPECIFIC = {
 31:'שם אחר: בר רבא; אין לייחס לרבא.',
 185:'שם אחר: בר רבא; אין לייחס לרבא.',
 230:'אביי דוחה את לימוד רבא מן הפסוק ומביא לימוד אחר; מחלוקת במקור הדין, לא בהכרח בדין עצמו.',
 265:'מסירה מקבילה של אותה אמירה, ולא מחלוקת.',
 309:'שם אחר: בר רבא; אין לייחס לרבא.',
 483:'מחלוקת רבה ורבא; אביי מתאר את שיטת רבה.',
 463:'אביי מוסר דין ורבא מבאר את טעמו; אין כאן מחלוקת מוכחת.',
 198:'ייתכן שמדובר בדוגמאות משלימות, ולא בדעות חולקות.',
 260:'משלים שונים לאותה נקודה; לא הוכחה מחלוקת.',
 326:'משלים סמוכים; לא הוכחה מחלוקת.',
 387:'המשך הסוגיה מבחין בין שלושה, שבעה ושלושים יום; צריך בירור מלא.',
 739:'ייחוס עונש בידי כמה חכמים; לא הוכח שהם חולקים.',
 751:'תוספות בטעמים לפסילת המעשה; ייתכן שהן מצטרפות.',
 886:'בהמשך צריכא בין הפסוקים; לא הוכחה מחלוקת.',
 1035:'דוגמאות להלכה פסוקה; לא הוכחה מחלוקת.',
}

def main():
 rows=json.loads((P/'review_candidates.json').read_text(encoding='utf-8'))
 assert len(rows)==1052, 'Review IDs require the frozen 2026-11-23 snapshot'
 decisions=[]
 for r in rows:
  i=r['review_id']
  selected=(r['kind']=='direct_pair' and i not in EXCLUDE|UNCERTAIN) or i in ADD
  status='selected_excerpt_review' if selected else 'not_selected'
  reason='נמצאו דעות או פירושים שונים בקריאה ראשונית של ציטוטים. לא אומתה הסוגיה במלואה.' if selected else 'לא נבחר למפתח הראשי; אין להסיק מכך שאין כאן מחלוקת. נשמר להמשך בדיקה.'
  if i in EXCLUDE:status='excluded_from_index';reason='סמיכות שאינה מוכיחה מחלוקת בין אביי לרבא, או חיבור בין דיונים שונים; נשמר בפלט הגולמי.'
  if i in UNCERTAIN:status='needs_context_review'
  reason=SPECIFIC.get(i,reason)
  decisions.append({'key':r['key'],'review_id':i,'ref':r['ref'],'decision':status,'reason':reason})
 (P/'review_decisions.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Selected candidates:',sum(d['decision']=='selected_excerpt_review' for d in decisions))

if __name__=='__main__':main()
