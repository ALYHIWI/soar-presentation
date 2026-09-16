with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('SLIDE_REFS =')
print("Position:", pos)
sub = text[pos:pos+15000]
lines = sub.splitlines()
keys = []
for idx, line in enumerate(lines):
    m = re.match(r'^\s*(\d+):\s*\{', line)
    if m:
        keys.append(m.group(1))
    if 'updateSlideReferences' in line or 'function ' in line:
        print(f"Function found at line {idx}: {line.strip()[:60]}")
        break

print("Found keys:", keys)
print("Count of keys:", len(keys))
