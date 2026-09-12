import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract SLIDE_REFS
idx = text.find('const SLIDE_REFS =')
end_idx = text.find('function updateSlideReferences', idx)
refs_code = text[idx:end_idx]

import json

# Let's count elements per slide in SLIDE_REFS
slides_keys = re.findall(r'(\d+):\s*\{\s*titleEn:\s*"([^"]+)"', refs_code)
print(f"Total slides registered in SLIDE_REFS: {len(slides_keys)}")

for s_idx, title in slides_keys:
    # find elements block
    m = re.search(rf'{s_idx}:\s*\{{.*?elements:\s*\[(.*?)\]\s*\}}', refs_code, re.DOTALL)
    if m:
        elems = re.findall(r'elEn:\s*"([^"]+)"', m.group(1))
        print(f"Slide {int(s_idx)+1:02d}: {title[:40]} -> {len(elems)} elements: {elems}")
    else:
        print(f"Slide {int(s_idx)+1:02d}: {title[:40]} -> NO ELEMENTS BLOCK!")
