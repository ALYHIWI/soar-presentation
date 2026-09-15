import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")
print("\n--- Lines 4335-4375 ---")
for i in range(4334, min(4375, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()[:100]}")

print("\n--- Searching for slideRefs and navigation scripts ---")
for i, line in enumerate(lines):
    if 'const N' in line or 'let cur' in line or 'const slideRefs' in line or 'function showSlide' in line or 'function updateRefDrawer' in line or 'localStorage' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
