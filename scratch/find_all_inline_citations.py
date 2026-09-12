import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

print(f"Auditing citations in slide body across {len(slides)} slides:\n")

for idx, (sid, content) in enumerate(slides):
    parts = content.split('<div class="slide-ref-footer"')
    body = parts[0]
    
    # Find any (§...) or §X.X or citations
    matches = re.findall(r'(\([^\)]*§[^\)]*\)|§\s*\d+(?:\.\d+)*|\([^\)]*20\d\d[^\)]*\)|et al\.)', body)
    if matches:
        print(f"Slide {idx+1:02d} ({sid}): {len(matches)} matches")
        for m in matches[:6]:
            print(f"   -> {m}")
