import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', c, re.DOTALL)
print(f"Total slides: {len(slides)}")

for i, (sid, body) in enumerate(slides):
    hs = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body, re.DOTALL)
    clean_h = [' '.join(re.sub(r'<[^>]+>', ' ', h).split()) for h in hs]
    has_table = '<table' in body
    svg_count = len(re.findall(r'<svg', body))
    card_count = len(re.findall(r'class="[^"]*(?:card|box|panel|step)[^"]*"', body))
    print(f"Slide {i+1:02d} ({sid}): {clean_h[:2]} | Cards: {card_count} | Table: {has_table} | SVGs: {svg_count}")
