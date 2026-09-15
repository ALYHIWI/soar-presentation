import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

corrupt_lines = []
for i, line in enumerate(lines):
    if '\ufffd' in line:
        corrupt_lines.append((i + 1, line.strip()[:100]))

print(f"Total lines with replacement char (U+FFFD): {len(corrupt_lines)}")
for l_no, text in corrupt_lines[:30]:
    print(f"Line {l_no}: {text}")
