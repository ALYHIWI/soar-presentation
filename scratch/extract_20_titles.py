import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

slide_pattern = re.compile(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', re.DOTALL)
matches = list(slide_pattern.finditer(text))[:20]

for idx, m in enumerate(matches):
    s_id = m.group(1)
    s_html = m.group(2)
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', s_html, re.DOTALL)
    h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', s_html, re.DOTALL)
    tag = re.findall(r'<div class=["\']tag[^"\']*["\']>(.*?)</div>', s_html, re.DOTALL)
    
    def clean(txt):
        return ' '.join(re.sub(r'<[^>]+>', ' ', txt).split())
    
    print(f"Slide {idx} ({s_id}):")
    if tag:
        print(f"  Tag: {clean(tag[0])}")
    if h1:
        print(f"  H1: {clean(h1[0])}")
    if h2:
        for h in h2:
            print(f"  H2: {clean(h)}")
