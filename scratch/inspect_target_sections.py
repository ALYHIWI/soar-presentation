import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_ids = ['s1', 's2', 's6', 's8', 's9', 's13']
for tid in target_ids:
    m = re.search(rf'(<section\s+class="slide[^"]*"\s+id="{tid}"[^>]*>.*?</section>)', html, re.DOTALL)
    if m:
        sec = m.group(1)
        first_line = sec.split('\n')[0]
        last_line = sec.split('\n')[-1]
        lines_count = len(sec.split('\n'))
        print(f"Found id='{tid}': {lines_count} lines. Start: {first_line[:40]} | End: {last_line}")
    else:
        print(f"NOT FOUND: id='{tid}'")
