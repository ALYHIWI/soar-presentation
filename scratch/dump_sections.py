import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>.*?</section>)', re.DOTALL)
sections = {m.group(2): m.group(1) for m in pattern.finditer(content)}

target_ids = ['s1', 's3', 's6', 's7', 's10', 's11', 's12', 's14', 's16', 's17', 's19']

for sid in target_ids:
    if sid in sections:
        with open(f'scratch/{sid}.html', 'w', encoding='utf-8') as out:
            out.write(sections[sid])
        print(f"Wrote scratch/{sid}.html (length: {len(sections[sid])})")
    else:
        print(f"Warning: {sid} not found!")
