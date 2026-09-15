import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("CSS font-size lines in <style> block:")
in_style = False
current_selector = ""

for i, line in enumerate(lines[:1500]):
    if '<style' in line:
        in_style = True
    elif '</style>' in line:
        in_style = False
        break
    
    if in_style:
        stripped = line.strip()
        if '{' in stripped and not stripped.startswith('@'):
            current_selector = stripped.split('{')[0].strip()
        if 'font-size' in stripped:
            print(f"  Line {i+1}: {current_selector} -> {stripped}")
