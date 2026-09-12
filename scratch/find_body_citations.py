import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

for idx, (sid, content) in enumerate(slides):
    # Separate content into body and .slide-ref-footer
    parts = content.split('<div class="slide-ref-footer"')
    body = parts[0]
    footer = parts[1] if len(parts) > 1 else ""
    
    # Look for citations in body: §, Chapter, al., et al., (202, etc.
    citations = re.findall(r'(\([^\)]*§[^\)]*\)|§\s*\d+(?:\.\d+)*|\([^\)]*20\d\d[^\)]*\)|et al\.)', body, re.IGNORECASE)
    if citations:
        print(f"Slide {idx+1:02d} ({sid}) body citations found: {citations}")
