import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for "doc ref" or "doc" or "ref" in buttons / toolbar / settings
for term in ['doc ref', 'Doc Ref', 'doc_ref', 'btnSourceMap', 'btnRefNav', 'refDrawer', 'cpSlideRefContent']:
    matches = [m.start() for m in re.finditer(re.escape(term), text, re.IGNORECASE)]
    print(f"Matches for '{term}': {len(matches)}")
    for m in matches[:3]:
        print("  " + text[max(0, m-60):min(len(text), m+120)].replace('\n', ' '))
