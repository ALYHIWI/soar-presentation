import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function toggleLang[^{]*\{.*?\}', c, re.DOTALL)
if not m:
    # search for 'ar' and 'en' toggling
    m = re.search(r'function\s+\w+\([^)]*\)\s*\{[^}]*\.classList\.toggle[^}]*\}', c, re.DOTALL)
if not m:
    for m2 in re.finditer(r'(?:lang|arabic|english)', c, re.IGNORECASE):
        start = max(0, m2.start() - 100)
        end = min(len(c), m2.end() + 200)
        snippet = c[start:end]
        if 'display' in snippet and 'none' in snippet and '<script' in c[:start]:
            print("FOUND IN SCRIPT:")
            print(snippet)
            break
