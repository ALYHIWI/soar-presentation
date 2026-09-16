import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m0 = re.search(r'<section\b[^>]*id=["\']s0["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m0:
    with open('scratch/s0_full.html', 'w', encoding='utf-8') as out:
        out.write(m0.group(1))
