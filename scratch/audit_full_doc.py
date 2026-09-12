import re

with open('full_project_doc.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print(f"Total characters: {len(text)}")

patterns = [
    r'100\s*gigabyte', r'22\.9%', r'54%', r'95\.1%', r'92\.67%', r'0\.92', r'0\.39',
    r'39,?427', r'2\.45\s*million', r'2\.25', r'96\.32%', r'98\.47%', r'50%', r'300\s*microsecond',
    r'609', r'Gelman', r'Gupta', r'Liu', r'Wang', r'Chavali', r'Karlz', r'Bridges', r'Khayat'
]

print("=== Pattern Matches in full_project_doc.txt ===")
for p in patterns:
    matches = list(re.finditer(p, text, re.IGNORECASE))
    print(f"Pattern {p}: {len(matches)} matches")
    for i, m in enumerate(matches[:2]):
        start = max(0, m.start() - 100)
        end = min(len(text), m.end() + 100)
        snippet = text[start:end].replace('\n', ' ')
        print(f"   [{i+1}] ...{snippet}...")

# Let's also find all numbers with % or units or metrics in the text
print("\n=== All percentages in document ===")
pcts = set(re.findall(r'\b\d+(?:\.\d+)?%', text))
print("Percentages found:", sorted(list(pcts)))

print("\n=== All decimal numbers / metrics ===")
metrics = set(re.findall(r'\b\d+\.\d+\b', text))
# Filter out section numbers like 1.1, 2.3, etc.
actual_metrics = [m for m in metrics if not re.match(r'^[1-5]\.\d+$', m)]
print("Decimal metrics:", sorted(actual_metrics))

print("\n=== Numbers with units or counts ===")
counts = re.findall(r'\b\d+(?:,\d+)?\s*(?:gigabytes?|GB|events?|alerts?|incidents?|seconds?|sec|minutes?|min|hours?|playbooks?|microseconds?|times?|percent)\b', text, re.IGNORECASE)
print("Counts/Units found:", sorted(list(set(counts))))
