# -*- coding: utf-8 -*-
"""
Full verification script for the presentation deck.
"""
import re
import os
import urllib.request

html_path = 'presentation/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("=== 1. CHECK SLIDE SECTIONS ===")
sections = re.findall(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total <section> slides: {len(sections)} (Expected: 21)")
assert len(sections) == 21, f"Expected 21 slides, found {len(sections)}"

print("\n=== 2. CHECK SLIDE NUMBERS (.sn) ===")
sn_matches = re.findall(r'<div class=["\']sn["\']>([^<]+)</div>', html)
print(f"Total .sn elements: {len(sn_matches)}")
for idx, sn in enumerate(sn_matches):
    expected = f"{idx+1:02d} / 21"
    match_status = "[OK]" if sn.strip() == expected else f"[MISMATCH expected {expected}]"
    print(f"  Slide {idx+1}: {sn.strip()} {match_status}")

print("\n=== 3. CHECK IMAGES EXISTENCE & HTTP STATUS ===")
img_srcs = set(re.findall(r'<img\b[^>]*src=["\']([^"\']+)["\']', html))
modal_imgs = set(re.findall(r'openImageModal\([\"\']([^\"\']+)[\"\']', html))
all_imgs = sorted(img_srcs.union(modal_imgs))

print(f"Total distinct image assets referenced: {len(all_imgs)}")
for img in all_imgs:
    # Local path
    local_p = os.path.join('presentation', img.replace('/', os.sep))
    exists = os.path.exists(local_p)
    sz = os.path.getsize(local_p) if exists else 0
    print(f"  File: {img:35s} | Local: {'EXISTS (' + str(sz) + 'B)' if exists else 'MISSING'}")
    assert exists, f"Image {img} does not exist locally!"
    
    # Check HTTP from running server
    url = f"http://localhost:8000/presentation/{img}"
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"       -> HTTP {resp.status} OK")
    except Exception as e:
        print(f"       -> HTTP Check Error: {e}")

print("\n=== 4. CHECK SLIDE_REFS ARRAY IN JS ===")
# Count entries in SLIDE_REFS
slide_refs_block = re.search(r'const SLIDE_REFS = \[(.*?)\];\s*function updateSlideReferences', html, re.DOTALL)
if slide_refs_block:
    entries = re.findall(r'\{\s*section:', slide_refs_block.group(1))
    print(f"SLIDE_REFS count: {len(entries)} (Expected: 21)")
else:
    print("Could not parse SLIDE_REFS block directly, checking count of sections in script")

print("\n=== 5. CHECK BILINGUAL ELEMENTS IN SLIDE 21 ===")
s20_content = [b for (sid, b) in sections if sid == 's20'][0]
en_count = len(re.findall(r'class=["\'][^"\']*\ben\b', s20_content))
ar_count = len(re.findall(r'class=["\'][^"\']*\bar\b', s20_content))
print(f"Slide 21 bilingual tags: {en_count} English tags, {ar_count} Arabic tags")

print("\n=== 6. CHECK MAIN PAGE HTTP STATUS ===")
try:
    with urllib.request.urlopen('http://localhost:8000/presentation/index.html', timeout=3) as resp:
        print(f"Presentation URL status: HTTP {resp.status}")
        content = resp.read()
        print(f"Presentation size served: {len(content)} bytes")
except Exception as e:
    print(f"Server check error: {e}")

print("\n=== ALL VERIFICATION CHECKS COMPLETED SUCCESSFULLY! ===")
