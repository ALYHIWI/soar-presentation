import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in presentation/index.html: {len(lines)}")

print("SLIDE_REFS keys:")
for i, line in enumerate(lines):
    m = re.match(r'^\s*(\d+):\s*\{', line)
    if m:
        title_line = ""
        for j in range(i+1, min(i+10, len(lines))):
            if 'titleEn:' in lines[j] or 'chapter:' in lines[j]:
                title_line += lines[j].strip() + " | "
        print(f"Key {m.group(1):>2s} at line {i+1}: {title_line[:100]}")
