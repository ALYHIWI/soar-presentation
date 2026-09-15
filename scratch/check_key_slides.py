import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

slide_pattern = re.compile(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', re.DOTALL)
matches = list(slide_pattern.finditer(text))

target_ids = ['s7', 's9', 's10', 's12', 's13', 's16', 's17', 's18']

for m in matches:
    s_id = m.group(1)
    if s_id in target_ids:
        html = m.group(2)
        h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
        sn = re.findall(r'<div class="sn">([^<]+)</div>', html)
        tables = len(re.findall(r'<table', html))
        svds = len(re.findall(r'<svg', html))
        cards = len(re.findall(r'class=["\'][^"\']*card[^"\']*["\']', html))
        print(f"Slide id={s_id:<4s} | SN={sn[0] if sn else 'None'} | tables={tables} | svgs={svds} | cards={cards} | title={h2[0] if h2 else 'None'}")
