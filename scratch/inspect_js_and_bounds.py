import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check where the old slides are
m = re.search(r'<!--\s*=================\s*S01:\s*HERO\s*&\s*GRADUATION\s*TEAM\s*=================\s*-->', text)
if m:
    pos = m.start()
    line_no = text[:pos].count('\n') + 1
    print(f"Old slides start marker found at char {pos}, line {line_no}")
else:
    print("Old slides start marker not found by regex")

# Also check where #wrap ends
wrap_matches = [m.start() for m in re.finditer(r'</div>\s*<!--\s*Bottom Navigation Bar\s*-->', text)]
print(f"Wrap end before nav bar at chars: {wrap_matches}")

# Check slideRefs object keys
ref_keys = re.findall(r'(\d+):\s*\{', text)
print(f"Slide ref keys found: {len(ref_keys)}")
