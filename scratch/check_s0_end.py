import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2120, min(2160, len(lines))):
    print(f"{i+1}: {lines[i].rstrip()[:100]}")
