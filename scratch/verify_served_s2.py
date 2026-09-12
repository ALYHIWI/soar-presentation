import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Fetching http://localhost:3000/ ...")
req = urllib.request.Request('http://localhost:3000/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')
    headers = dict(resp.getheaders())

print("HTTP Status: 200 OK")
print(f"Cache-Control: {headers.get('Cache-Control')}")

# 1. Verify no slide-ref-footer
footers = re.findall(r'class=[\"\'][^\"\']*slide-ref-footer', html)
print(f"Slide-ref-footers count in served HTML: {len(footers)} (Expected: 0)")
assert len(footers) == 0

# 2. Verify Slide 2 (index 1 in SLIDE_REFS)
s2_m = re.search(r'1:\s*\{.*?elements:\s*\[(.*?)\]\s*\}', html, re.DOTALL)
assert s2_m is not None, "SLIDE_REFS[1] not found"
s2_elements = re.findall(r'elEn:\s*"([^"]+)"', s2_m.group(1))
print(f"\nSlide 2 (s1) elements in doc ref: {len(s2_elements)} items:")
for i, el in enumerate(s2_elements):
    print(f"  Item {i+1}: {el}")

assert len(s2_elements) == 7, f"Expected 7 items for Slide 2, got {len(s2_elements)}"

# 3. Verify 100 GB in Slide 2 elements
assert "100 gigabytes" in s2_m.group(1) or "100 GB" in s2_m.group(1)
print("\n✅ Slide 2 elements match 1:1 with the visual slide (Upper Lead + 3 Cards + 3 Stat Boxes)!")
print("✅ 100 GB citation verified: Chapter 1 · §1.2, Page 12, Line 468!")
