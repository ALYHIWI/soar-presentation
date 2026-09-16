import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', c, re.DOTALL)

for i, (sid, body) in enumerate(slides):
    m_en = re.search(r'<(?:h1|h2)[^>]*class="[^"]*(?:st|hero)[^"]*en"[^>]*>(.*?)</(?:h1|h2)>', body)
    t_en = re.sub(r'<[^>]+>', '', m_en.group(1)).strip() if m_en else sid
    # check for sub-structure
    has_table = '<table' in body
    has_grid = bool(re.search(r'class="[^"]*g[234][^"]*"', body))
    has_banner = 'hl-banner' in body or 'banner' in body
    text_length = len(re.sub(r'<[^>]+>', ' ', body).split())
    print(f"[{i+1:02d}] {sid} | Words: {text_length:3d} | Grid: {has_grid} | Table: {has_table} | Title: {t_en[:40]}")
