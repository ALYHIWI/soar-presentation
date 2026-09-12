import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract SLIDE_REFS
idx = text.find('const SLIDE_REFS =')
end_idx = text.find('function updateSlideReferences', idx)
refs_block = text[idx:end_idx]

# Check each slide 0 to 24
total_elements = 0
for i in range(25):
    pattern = rf'\n\s*{i}:\s*\{{.*?titleEn:\s*"([^"]+)".*?chapter:\s*"([^"]+)".*?section:\s*"([^"]+)".*?elements:\s*\[(.*?)\]\s*\}}'
    m = re.search(pattern, refs_block, re.DOTALL)
    if not m:
        print(f"❌ Slide {i+1:02d} NOT FOUND in SLIDE_REFS!")
    else:
        title = m.group(1)
        chap = m.group(2)
        sec = m.group(3)
        elems = re.findall(r'elEn:\s*"([^"]+)"', m.group(4))
        locs = re.findall(r'loc:\s*"([^"]+)"', m.group(4))
        total_elements += len(elems)
        print(f"Slide {i+1:02d}: {len(elems)} elements | {title[:40]:40s} | {chap[:30]} ({sec[:25]})")
        for e, l in zip(elems, locs):
            print(f"     • {e:45s} -> {l}")

print(f"\n🎉 Total verified elements across all 25 slides: {total_elements}")
