"""Frozen-snapshot excerpt review decisions, not full-sugya certification."""
import json
from pathlib import Path
P=Path(__file__).parent/'yochanan_lakish_results'
# Cross-topic pairs, transmissions/agreements or unclear attribution; never silently select.
EXCLUDE=set(map(int,'''17 24 30 55 58 62 77 78 114 118 131 134 141 157 161 163 167 169
185 192 194 196 244 248 274 278 298 313 330 333 374 381 427
475 483 487 491 492 514 531 538 561 591 607 613 618
635 641 652 665 679 682 690 698 723 740 756 762 776 779 786 796 804 808 811 821 826 828 829
884 898 920 924 961 980 984 1002 1003 1014 1031 1035 1040 1045 1050 1053
1055 1075 1087 1092 1099 1100 1102 1115 1120 1122 1127 1135 1137 1144 1149 1158 1159 1165
1187 1197 1199 1205 1207 1210 1215 1221 1228
1232 1244 1246 1248 1251 1252 1261 1275 1296 1309 1320 1337 1347 1358 1360 1362 1374 1376 1381 1382 1385 1396'''.split()))
UNCERTAIN={322,556,709,837,903,929,982,1177,1268,1312,1314}
ADD=set(map(int,'''56 145 212 213 250 312 347 348 368 387 394 431 432 439 500 501 558 559 563 564 572 609 630 648 649 670 676 691 715
781 803 859 880 900 916 925 963 965 981 1004 1043 1073 1103 1196 1218 1220 1239 1263 1265 1267 1270 1289 1300 1306 1311 1315
85 137 197 198 200 201 220 303 304 305 306 307 308 310 311 402 404 550 551 553 600 601 602 730 753 766 835 864 938 939 944 945 946 974 975 976 1018 1020 1021 1022 1033 1034 1044 1079 1080 1081 1105 1108 1145 1161 1163 1192 1194 1273 1274 1302 1303 1318 1329 1330 1331 1349 1350 1409'''.split()))
RECONCILED={208,379,1054}

def main():
 rows=json.loads((P/'candidates.json').read_text(encoding='utf-8'))
 assert len(rows)==1409,'Review applies to the frozen scan; remap stable keys before changing it'
 decisions=[]
 for r in rows:
  i=r['review_id'];a,b=r['anchors']
  strong=r['kind']=='declaration_pair' and b['forward'] and b['verb']!='בעי'
  selected=(strong and i not in EXCLUDE|UNCERTAIN) or i in ADD
  status='selected_excerpt_review' if selected else 'needs_review'
  reason='קריאה ראשונית של ציטוטים: דעות, תירוצים או דרשות שונות. לא נבדקה כל הסוגיה.' if selected else 'לא נבחר למפתח; אין זו קביעה שאין מחלוקת. נשמר להמשך בדיקה.'
  if i in EXCLUDE:status='excluded_pair';reason='הצימוד אינו מוכיח מחלוקת: מעבר בין דיונים, מסירה משותפת או אמירות משלימות. ייתכן שההקשר כולל מחלוקת אחרת.'
  if i in UNCERTAIN:reason='נדרש בירור הקשר/ייחוס; לא נכלל במפתח הראשי.'
  decisions.append({'key':r['key'],'review_id':i,'ref':r['ref'],'decision':status,'reason':reason,'reconciled':i in RECONCILED})
 (P/'review_decisions.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2),encoding='utf-8')
 print('Selected',sum(d['decision']=='selected_excerpt_review' for d in decisions))

if __name__=='__main__':main()
