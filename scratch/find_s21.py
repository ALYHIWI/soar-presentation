import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section[^>]*id="s21"[^>]*>(.*?)</section>', text, re.DOTALL)
if m:
    for line in m.group(1).splitlines():
        if 'et al' in line:
            print(line.strip())
