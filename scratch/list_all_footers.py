import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the exact titles of all 25 slides
with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

for idx, (sid, content) in enumerate(slides):
    # footer text
    f = re.search(r'<div class="slide-ref-footer"[^>]*>(.*?)</div>', content, re.DOTALL)
    f_en = re.search(r'<span class="en"[^>]*>(.*?)</span>', f.group(1), re.DOTALL) if f else None
    footer_str = re.sub(r'<[^>]+>', ' ', f_en.group(1)).strip() if f_en else ""
    print(f"Slide {idx+1:02d} ({sid:3s}): {footer_str[:85]}")
