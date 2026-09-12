with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'toggleRefModal', text)]
print("Occurrences of toggleRefModal:", len(matches))
for m in matches:
    print(text[max(0, m-50):min(len(text), m+80)].replace('\n', ' '))
