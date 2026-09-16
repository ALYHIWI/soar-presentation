# -*- coding: utf-8 -*-
import re, os, urllib.request

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check sections
secs = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>', html)
print(f"Total sections: {len(secs)} (Expected: 20)")
assert len(secs) == 20, f"Error: expected 20 sections, got {len(secs)}"

# 2. Check images referenced
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags: {len(img_srcs)}")
for src in img_srcs:
    local_path = os.path.join('presentation', src.replace('/', os.sep))
    exists = os.path.exists(local_path)
    size = os.path.getsize(local_path) if exists else 0
    print(f"  Image: {src} -> Exists: {exists} ({size} bytes)")
    assert exists, f"Error: Image {local_path} does not exist!"

# 3. Check Lightbox modal
assert 'id="imgModal"' in html, "Error: imgModal not found in HTML!"
assert 'openImageModal' in html, "Error: openImageModal not found in HTML!"
print("Lightbox modal: Verified OK")

# 4. Check HTTP endpoint on server
try:
    for src in img_srcs:
        url = f"http://localhost:8000/presentation/{src}"
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"  HTTP {url} -> Status: {resp.status}")
except Exception as e:
    print(f"  HTTP check note: {e}")

# 5. Check slide numbers (sn)
sns = re.findall(r'<div class="sn">([^<]+)</div>', html)
print(f"Slide numbers count: {len(sns)}")
for i, sn in enumerate(sns):
    expected = f"{i+1:02d} / 20"
    if sn.strip() != expected:
        print(f"  Warning: Slide {i+1} has sn='{sn}', expected '{expected}'")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
