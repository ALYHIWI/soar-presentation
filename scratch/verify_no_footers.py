import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<div[^>]*class=[\"\'][^\"\']*slide-ref-footer', text)
print(f"Total slide-ref-footer elements in HTML: {len(matches)}")
assert len(matches) == 0, "slide-ref-footer should be completely gone!"
print("✅ All slide-ref-footers successfully eliminated from HTML!")
