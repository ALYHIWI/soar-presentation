import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'updateSlideReferences', text)]
print("Occurrences of updateSlideReferences:", len(matches))
for m in matches:
    print(text[max(0, m-80):min(len(text), m+120)].replace('\n', ' '))
