import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# check font sizes in CSS
rules = re.findall(r'([^{]+)\{([^}]+font-size:[^}]+)\}', text)
print(f"Found {len(rules)} rules with font-size. Printing key selectors:")
for sel, body in rules:
    sel = sel.strip()
    if any(k in sel for k in ['body', '.st', '.hero', '.card', '.ctbl', 'p', 'table', '.sn', '.tag', '.lead']):
        fs = re.findall(r'font-size:\s*([^;]+);', body)
        print(f"  {sel[:40]:<40} -> font-size: {fs}")
