with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'const SLIDE_REFS = (\[.*?\]);\s*function updateSlideReferences', text, re.DOTALL)
if m:
    raw_js = m.group(1)
    # Count sections
    entries = re.findall(r'section:\s*["\']', raw_js)
    print(f"SLIDE_REFS has {len(entries)} section entries.")
else:
    print("Could not locate SLIDE_REFS")
