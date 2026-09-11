import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class=["\']slide[^"\']*["\'][^>]*>(.*?)</section>', html, re.DOTALL)
print(f'Total slides count: {len(slides)}')
for i, s in enumerate(slides, 1):
    tag = re.search(r'<div class=["\']stag[^"\']*["\']>(.*?)</div>', s, re.DOTALL)
    tag_str = re.sub(r'<[^>]+>', ' ', tag.group(1)).strip() if tag else ''
    tag_str = ' '.join(tag_str.split())
    title = re.search(r'<h[12][^>]*>(.*?)</h[12]>', s, re.DOTALL)
    title_str = re.sub(r'<[^>]+>', ' ', title.group(1)).strip() if title else ''
    title_str = ' '.join(title_str.split())
    print(f'Slide {i:02d}: Tag=[{tag_str[:35]}] Title=[{title_str[:55]}]')
