with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'soar_custom_deck', text)]
for pos in matches:
    line_no = text[:pos].count('\n') + 1
    # print context
    start = max(0, pos - 200)
    end = min(len(text), pos + 200)
    print(f"\n--- At line {line_no} ---")
    print(text[start:end])
