import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

for idx, (sid, content) in enumerate(slides):
    parts = content.split('<div class="slide-ref-footer"')
    body = parts[0]
    
    # Print lines containing (§ or citations
    lines = body.splitlines()
    found = []
    for l in lines:
        if re.search(r'\(§|§\s*\d|\(20\d\d|et al\.|/ §', l):
            # Skip if it's purely an HTML tag or class name
            clean = l.strip()
            found.append(clean)
    if found:
        print(f"=== SLIDE {idx+1:02d} ({sid}) - {len(found)} lines with inline citations ===")
        for f in found[:8]:
            print("  ", f[:100])
