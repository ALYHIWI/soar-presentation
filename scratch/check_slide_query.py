with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.slide', text)]
print("References to .slide in JS:")
for pos in matches:
    if pos > 140000: # in JS area
        line_no = text[:pos].count('\n') + 1
        start = max(0, pos - 100)
        end = min(len(text), pos + 100)
        print(f"Line {line_no}: {text[start:end].strip()}")
