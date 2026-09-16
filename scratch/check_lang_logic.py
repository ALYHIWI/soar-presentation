import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find language toggle logic
for m in re.finditer(r'(?:lang|direction|dir=|\.ar\b|\.en\b)', c, re.IGNORECASE):
    snippet = c[max(0, m.start()-50):min(len(c), m.end()+100)]
    if 'display' in snippet or 'toggle' in snippet or 'addEventListener' in snippet:
        print("--- MATCH ---")
        print(snippet.strip())
        break
