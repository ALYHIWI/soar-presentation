import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all slides
slide_pattern = re.compile(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', re.DOTALL)
matches = list(slide_pattern.finditer(content))

print(f"Total slide matches: {len(matches)}")

for i, m in enumerate(matches):
    s_id = m.group(1)
    slide_html = m.group(2)
    # Extract title
    h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', slide_html, re.DOTALL)
    h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', slide_html, re.DOTALL)
    h3 = re.findall(r'<h3[^>]*>(.*?)</h3>', slide_html, re.DOTALL)
    sn = re.findall(r'<div class="sn">(.*?)</div>', slide_html)
    
    clean_h = []
    for h in h1 + h2:
        txt = re.sub(r'<[^>]+>', ' ', h).strip()
        txt = ' '.join(txt.split())
        clean_h.append(txt[:60])
    
    sn_val = sn[0] if sn else "N/A"
    print(f"Slide {i+1:2d}: id='{s_id}', sn='{sn_val}', titles={clean_h[:2]}")
