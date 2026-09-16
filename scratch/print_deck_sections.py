import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

secs = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', c, re.DOTALL)
print(f"Total sections: {len(secs)}")
for i, (sid, body) in enumerate(secs):
    m_en = re.search(r'<(?:h1|h2)[^>]*class="[^"]*(?:st|hero)[^"]*en"[^>]*>(.*?)</(?:h1|h2)>', body)
    m_ar = re.search(r'<(?:h1|h2)[^>]*class="[^"]*(?:st|hero)[^"]*ar"[^>]*>(.*?)</(?:h1|h2)>', body)
    t_en = re.sub(r'<[^>]+>', '', m_en.group(1)).strip() if m_en else ""
    t_ar = re.sub(r'<[^>]+>', '', m_ar.group(1)).strip() if m_ar else ""
    sn_m = re.search(r'<div class="sn">([^<]+)</div>', body)
    sn = sn_m.group(1).strip() if sn_m else ""
    print(f"Slide {i+1:02d} [{sid}] ({sn}): EN='{t_en}' | AR='{t_ar}'")
