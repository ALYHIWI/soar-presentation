import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m0 = re.search(r'<section\b[^>]*id=["\']s0["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m0:
    print('=== SLIDE 0 (TITLE) ===')
    for line in m0.group(1).splitlines():
        if 'h1' in line or 'title' in line or 'hero' in line or 'tag' in line:
            print(line.strip())

m20 = re.search(r'<section\b[^>]*id=["\']s20["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m20:
    print('\n=== CURRENT SLIDE 21 (s20) ===')
    print(m20.group(1))
