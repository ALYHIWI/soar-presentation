import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/slide_s0.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
cards = re.findall(r'<div class="team-title-card">.*?</div>\s*</div>', text, re.DOTALL)
print(f"Cards count in scratch/slide_s0.html: {len(cards)}")
for c in cards:
    print("---")
    print(c.strip())
