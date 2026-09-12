with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'slide-ref-footer', text)]
for m in matches:
    print(text[max(0, m-40):min(len(text), m+60)].replace('\n', ' '))
