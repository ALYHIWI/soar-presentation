# -*- coding: utf-8 -*-
with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx1 = html.find('id="s1"')
idx2 = html.find('id="s2"')
print("=== Slide 2 in index.html ===")
print(html[idx1:idx2])
