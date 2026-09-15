import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in [1723, 1727, 1790, 3358, 3382]:
    if idx < len(lines):
        print(f"Line {idx+1}: {lines[idx].strip()}")
