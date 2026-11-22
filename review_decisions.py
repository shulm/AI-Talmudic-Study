import json
from pathlib import Path
p=Path('rav_shmuel_results')
strong=json.loads((p/'strong.json').read_text(encoding='utf-8'))
supp=json.loads((p/'supplements.json').read_text(encoding='utf-8'))
# Negative decisions: adjacent but unrelated statements, or crossing into a new topic.
remove={224,244,248,256,713,928,935,954,1139,1164,1205,1250,1257,1273,1283,1362,1364}
add=set(map(int,'''
19 39 41 53 56 72 80 82 89 91 98 105 109 110 130 138 143 152 158 166 168 170 173
198 203 206 216 223 227 233 235 252 255 266 268 278 283 285 337 338 347 349 354 363 373 375 377 381 384 386 388 394 397 407 409 413 415
420 423 429 431 439 441 444 455 457 466 471 472 476 478 480 482 486 498 503 505 515 523 524 525 528 541 550 556 309 310 314 325 327
561 564 577 578 589 591 604 610 617 620 623 627 640 645 673 675 677 688 694 716 722 731 732 735 738 741 743 747
766 768 771 778 780 781 787 823 824 825 830 838 840 841 846 847 851 856 857 858 868 881 887 909 910 915 916 922 927 930 931 932 934 940 946 970 971 973 977
979 980 984 986 989 990 991 992 993 995 997 1011 1015 1022 1029 1030 1033 1034 1036 1042 1044 1049 1053 1061 1064 1070 1072 1073 1085 1091 1108 1111 1116 1128 1130 1133 1152 1155 1157 1159 1161
1168 1199 1232 1234 1240 1254 1263 1275 1301 1302 1315 1316 1330 1338 1339 1341 1353 1356 1358 1374
'''.split()))
reconciled={1121,678,604,940,991,1311,1314,1111}
a=json.loads((p/'classified_candidates.json').read_text(encoding='utf-8'))
main=[r for r in a if (r['id'] in add or r['id'] in {v['id'] for v in strong}) and r['id'] not in remove]
for r in main:r['status']='reconciled' if r['id'] in reconciled else 'dispute'
(p/'selected.json').write_text(json.dumps(main,ensure_ascii=False,indent=2),encoding='utf-8')
reviewed={r['id'] for r in strong+supp}
other=[r for r in a if r['id'] not in reviewed]
print('SELECTED',len(main),'UNREVIEWED PAIRS',len(other))
(p/'remaining.json').write_text(json.dumps(other,ensure_ascii=False,indent=2),encoding='utf-8')
for r in other:
 if r['kind']!='paired' or len(r['evidence'])<1500:
  print(r['id'],r['ref'],r['evidence'].replace('\n',' ')[:140])
