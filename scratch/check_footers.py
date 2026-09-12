import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

print(f"Total slides found: {len(slides)}\n")

for idx, (sid, content) in enumerate(slides):
    footer = re.search(r'<div class="slide-ref-footer"[^>]*>(.*?)</div>', content, re.DOTALL)
    if not footer:
        print(f"Slide {idx+1} ({sid}): ❌ MISSING FOOTER!")
        continue
    
    f_content = footer.group(1)
    en_part = re.search(r'<span class="en"[^>]*>(.*?)</span>', f_content, re.DOTALL)
    ar_part = re.search(r'<span class="ar"[^>]*>(.*?)</span>', f_content, re.DOTALL)
    pill = re.search(r'<span class="ref-pill"[^>]*>(.*?)</span>', f_content, re.DOTALL)
    
    en_txt = re.sub(r'<[^>]+>', '', en_part.group(1)).strip() if en_part else "NO EN"
    ar_txt = re.sub(r'<[^>]+>', '', ar_part.group(1)).strip() if ar_part else "NO AR"
    pill_txt = re.sub(r'<[^>]+>', '', pill.group(1)).strip() if pill else "NO PILL"
    
    print(f"Slide {idx+1:02d} ({sid:4s}):")
    print(f"   Pill: {pill_txt}")
    print(f"   EN:   {en_txt}")
    print(f"   AR:   {ar_txt}\n")
