import io
import sys

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Checking lines 2030 to 2150 in new 20 slides:")
for i in range(2028, 2150):
    line = lines[i].rstrip()
    if 'class="ar"' in line or '<h' in line or 'sn' in line:
        print(f"{i+1}: {line}")

print("\n--- Checking lines 2945 to 3050 in old slides ---")
for i in range(2945, 3050):
    line = lines[i].rstrip()
    if 'class="ar"' in line or '<h' in line:
        print(f"{i+1}: {line}")
