import re

with open('full_project_doc.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['Chapter 1', 'Chapter 2', 'Chapter 3', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '2.1', '2.2', '2.3', '2.4', '2.5', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8']):
        if len(line.strip()) < 80:
            print(f"Line {i+1}: {line.strip()}")
