import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('full_project_doc.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(455, 490):
    print(f"Line {i+1}: {lines[i].strip()}")
