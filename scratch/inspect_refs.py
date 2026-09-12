# -*- coding: utf-8 -*-
import json, re

html = open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', encoding='utf-8').read()
# Let's inspect elements from Slide 1, 2, 3, 12, 17, 22, 25
match = re.search(r'const SLIDE_REFS = (\{.*?\n\};)', html, re.DOTALL)
if match:
    # let's write to a text file for inspection
    with open('scratch/slide_refs_inspect.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(1)[:4000])
    print("Wrote inspect sample.")
