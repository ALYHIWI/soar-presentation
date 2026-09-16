import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Match section tags and their content
pattern = re.compile(r'<section\b([^>]*)>(.*?)</section>', re.DOTALL)
matches = pattern.findall(content)

print(f"Total sections found: {len(matches)}")
for idx, (attrs, body) in enumerate(matches):
    sid = re.search(r'id=["\']([^"\']+)["\']', attrs)
    sid_val = sid.group(1) if sid else 'N/A'
    sn = re.search(r'<div class=["\']sn["\']>([^<]+)</div>', body)
    sn_val = sn.group(1).strip() if sn else 'N/A'
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.DOTALL)
    h2_clean = re.sub(r'<[^>]+>', '', h2.group(1)).strip() if h2 else 'No H2'
    h2_clean = ' '.join(h2_clean.split())[:60]
    print(f"[{idx}] id={sid_val} | sn={sn_val} | h2={h2_clean}")
