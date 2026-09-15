import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section\b[^>]*id=["\']s18["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("s18 not found")
