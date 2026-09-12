import re

with open('pdf_decoded.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

patterns = [
    r'100\s*gigabyte', r'22\.9%', r'54%', r'95\.1%', r'92\.67%', r'0\.92', r'0\.39',
    r'39,?427', r'2\.45\s*million', r'2\.25', r'96\.32%', r'98\.47%', r'50%', r'300\s*microsecond',
    r'609', r'Gelman', r'Gupta', r'Liu', r'Wang', r'Chavali', r'Karlz', r'Bridges', r'Khayat'
]

print(f"=== pdf_decoded.txt length: {len(text)} characters ===")
for p in patterns:
    matches = list(re.finditer(p, text, re.IGNORECASE))
    print(f"\n--- Pattern: {p} (matches: {len(matches)}) ---")
    for i, m in enumerate(matches[:3]):
        start = max(0, m.start() - 150)
        end = min(len(text), m.end() + 150)
        snippet = text[start:end].replace('\n', ' ')
        print(f"[{i+1}] ...{snippet}...")
