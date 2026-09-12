import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find each slide
pattern = re.compile(r'<section\s+class="slide([^"]*)"\s+id="([^"]+)"(.*?)</section>', re.DOTALL)
matches = pattern.findall(content)

print(f"Total slides: {len(matches)}")
print("="*80)

for idx, (cls, sid, body) in enumerate(matches):
    # Strip tags for text
    text = re.sub(r'<[^>]+>', ' ', body)
    text = re.sub(r'\s+', ' ', text).strip()
    print(f"\n{'='*80}")
    print(f"SLIDE {idx+1} | ID: {sid}")
    print(f"{'='*80}")
    print(text[:3000])
    print()
