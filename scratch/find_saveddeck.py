import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'savedDeck' in line or 'soar_custom_deck' in line:
        print(f"Line {i+1}: {line}")
        # print surrounding lines
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"  {j+1}: {lines[j]}", end='')
        print("="*50)
