import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('full_project_doc.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'gigabyte' in line.lower() or '100' in line:
        print(f"Line {idx+1}: {line.strip()[:120]}")
        # print context
        for j in range(max(0, idx-3), min(len(lines), idx+4)):
            print(f"   [{j+1}] {lines[j].strip()[:100]}")
        print("="*60)
