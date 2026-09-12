with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'SLIDE_REFS', text)]
print(f"SLIDE_REFS referenced {len(matches)} times at: {matches}")
for m in matches:
    print("--- SNIPPET ---")
    print(text[max(0, m-100):min(len(text), m+200)])
