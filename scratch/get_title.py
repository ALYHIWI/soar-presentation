import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<h1 class=["\']hero["\'][^>]*>(.*?)</h1>', text, re.DOTALL)
if m:
    print("Exact H1 content:")
    print(m.group(1).strip())
