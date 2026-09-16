import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'91%', text))
print(f"Total 91% matches: {len(matches)}")
with open('scratch/matches_91.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        pos = m.start()
        line = text[:pos].count('\n') + 1
        out.write(f"Line {line}: {text[max(0, pos-80):min(len(text), pos+80)]}\n")
print("Saved to scratch/matches_91.txt")
