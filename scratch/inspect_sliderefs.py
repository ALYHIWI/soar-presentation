import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+slideRefs\s*=\s*\{', text)
if m:
    start_pos = m.start()
    line_no = text[:start_pos].count('\n') + 1
    print(f"slideRefs found at line {line_no}")
    # print the next 50 lines
    lines = text[start_pos:].splitlines()[:60]
    for idx, l in enumerate(lines):
        print(f"{line_no+idx}: {l[:100]}")
else:
    print("slideRefs not found!")
