import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check Slide 1 (s0)
m0 = re.search(r'(<section[^>]*id=["\']s0["\'][^>]*>.*?</section>)', text, re.DOTALL)
if m0:
    print("=== SLIDE 1 (s0) ===")
    print(m0.group(1)[:1200])
    print("\n--- s0 middle/end ---")
    print(m0.group(1)[1200:2500])
    if len(m0.group(1)) > 2500:
        print(m0.group(1)[2500:4000])

# 2. Check Slide 2 (s1)
m1 = re.search(r'(<section[^>]*id=["\']s1["\'][^>]*>.*?</section>)', text, re.DOTALL)
if m1:
    print("\n=== SLIDE 2 (s1) ===")
    print(m1.group(1)[:600])

# 3. Check slide ref footer count
footers = re.findall(r'class=["\'][^"\']*slide-ref-footer[^"\']*["\']', text)
print(f"\nTotal slide-ref-footers found: {len(footers)}")

# 4. Check if SLIDE_REFS exists in JS
js_refs = re.search(r'const\s+SLIDE_REFS\s*=\s*(\{.*?\});\s*(?:const|let|var|function|\n\n)', text, re.DOTALL)
if js_refs:
    print("SLIDE_REFS JS object found, length:", len(js_refs.group(1)))
else:
    print("SLIDE_REFS not matched directly with regex, searching...")
    idx = text.find('SLIDE_REFS')
    print("SLIDE_REFS found at index:", idx)
    if idx != -1:
        print(text[idx:idx+300])
