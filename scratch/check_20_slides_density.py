import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

slide_pattern = re.compile(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', re.DOTALL)
all_matches = list(slide_pattern.finditer(text))
new_20_slides = all_matches[:20]

for idx, m in enumerate(new_20_slides):
    s_html = m.group(2)
    # Check length
    words = len(re.sub(r'<[^>]+>', ' ', s_html).split())
    # Check grid classes
    grids = re.findall(r'class=["\'][^"\']*(?:g\d|grid|flex|bento)[^"\']*["\']', s_html)
    print(f"Slide {idx+1:02d}: words={words}, grids={grids}")
