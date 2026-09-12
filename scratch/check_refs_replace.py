with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pos_22 = html.find('22: {')
pos_23 = html.find('23: {')
pos_24 = html.find('24: {')

print("pos_22:", pos_22)
print("pos_23:", pos_23)
print("pos_24:", pos_24)

if pos_22 != -1:
    print("=== SLIDE 22 REF ===")
    print(html[pos_22:pos_23])
if pos_23 != -1:
    print("=== SLIDE 23 REF ===")
    print(html[pos_23:pos_24])
