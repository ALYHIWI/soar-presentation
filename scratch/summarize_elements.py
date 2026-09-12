import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/all_slides_visual_elements.txt', 'r', encoding='utf-8') as f:
    text = f.read()

slides_data = text.split('='*80)
for s in slides_data:
    if not s.strip(): continue
    lines = [l.strip() for l in s.strip().splitlines() if l.strip()]
    if lines:
        header = lines[0]
        # find items
        items = [l for l in lines if l.startswith(('Title:', 'Lead:', 'Card ', 'Stat ', 'Stage ', 'Banner/HL:'))]
        print(f"{header}: {len(items)} items -> {', '.join([it.split(':')[0] for it in items])}")
