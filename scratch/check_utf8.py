# -*- coding: utf-8 -*-
import re

html = open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', encoding='utf-8').read()
matches = re.findall(r'titleAr:\s*\"([^\"]+)\"', html)
print(f"Total titleAr matches: {len(matches)}")
with open(r'scratch/titles_out.txt', 'w', encoding='utf-8') as f:
    for i, m in enumerate(matches):
        f.write(f"Slide {i+1}: {m}\n")
print("Wrote titles to scratch/titles_out.txt")
