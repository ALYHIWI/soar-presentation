import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(6460, len(lines)):
    print(f"{i+1}: {lines[i].rstrip()[:120]}")
