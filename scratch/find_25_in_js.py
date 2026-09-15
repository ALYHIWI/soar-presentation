import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Scanning for '25' in lines after 4340:")
for i in range(4340, len(lines)):
    line = lines[i]
    if '25' in line and not ('2025' in line or 'rgba(' in line or '255' in line or 'p-25' in line):
        print(f"Line {i+1}: {line.strip()[:100]}")
