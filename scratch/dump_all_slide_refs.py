import re

with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_start = html.find('const SLIDE_REFS =')
pos_end = html.find('function updateSlideReferences', pos_start)

refs_code = html[pos_start:pos_end]

with open('scratch/all_slide_refs.js', 'w', encoding='utf-8') as out:
    out.write(refs_code)

print(f"Saved scratch/all_slide_refs.js ({len(refs_code)} bytes)")
