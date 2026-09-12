import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_ids = ['s2', 's11', 's16', 's17', 's19', 's21', 's22', 's23']

for sid in target_ids:
    m = re.search(r'(<section\s+class="slide[^"]*"\s+id="' + sid + r'"[^>]*>.*?</section>)', html, re.DOTALL)
    if m:
        with open(f'scratch/slide_{sid}.html', 'w', encoding='utf-8') as out:
            out.write(m.group(1))
        print(f"Saved scratch/slide_{sid}.html ({len(m.group(1))} bytes)")
    else:
        print(f"NOT FOUND: {sid}")
