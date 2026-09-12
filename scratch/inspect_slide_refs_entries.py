import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find SLIDE_REFS definition
idx = text.find('const SLIDE_REFS =')
end_idx = text.find('function updateSlideReferences', idx)
print(f"SLIDE_REFS slice length: {end_idx - idx}")

# Let's inspect slide 0, 1, 2
refs_block = text[idx:end_idx]
slides_match = re.split(r'\n\s*(\d+):\s*\{', refs_block)

print(f"Total split sections: {len(slides_match)}")
for i in range(1, min(8, len(slides_match)), 2):
    s_num = slides_match[i]
    s_body = slides_match[i+1]
    print(f"\n{'='*50}\nSLIDE KEY {s_num}:")
    print(s_body[:600] + "...")
