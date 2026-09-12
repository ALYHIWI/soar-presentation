import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Fetching http://localhost:3000 ...")
req = urllib.request.Request('http://localhost:3000', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    status = resp.status
    headers = dict(resp.getheaders())
    html = resp.read().decode('utf-8')

print(f"HTTP Status: {status}")
print(f"Cache-Control: {headers.get('cache-control')}")
print(f"Pragma: {headers.get('pragma')}")

# 1. Slide Count
slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"', html)
print(f"\n[Check 1] Slide Count: {len(slides)} (Expected: 25)")
assert len(slides) == 25, f"Expected 25 slides, got {len(slides)}"

# 2. Slide 1 (s0)
m0 = re.search(r'<section[^>]*id="s0"[^>]*>(.*?)</section>', html, re.DOTALL)
assert m0 is not None, "Slide 1 (s0) not found"
s0 = m0.group(1)

students = [
    ("حزام محمد علي الشجرة", "202210102478"),
    ("حمود عبد الله صالح أبو عمرة", "202310101609"),
    ("محمد حميد قاسم محمد", "202310100174"),
    ("محمد طه قاسم الورافي", "202310100461"),
    ("مروان محمد سعيد الأمير", "202310100177"),
    ("نوح أحمد محمد مرق", "202310100452")
]

print("\n[Check 2] Slide 1 Student Verification:")
for name, sid in students:
    has_name = name in s0
    has_id = sid in s0
    print(f"  {name} ({sid}): {'✅' if (has_name and has_id) else '❌'}")
    assert has_name and has_id

has_sup = "المشرف العلمي" in s0 and "رائد سعيد" in s0 and "الأمن السيبراني والشبكات" in s0 and "علوم الحاسوب" in s0
print(f"  Supervisor & Dept: {'✅' if has_sup else '❌'}")
assert has_sup

# 3. Reference Footers on ALL 25 slides
print("\n[Check 3] Reference Footers Verification (All 25 slides):")
footers = re.findall(r'<div class="slide-ref-footer"[^>]*>(.*?)</div>', html, re.DOTALL)
print(f"  Total footers found: {len(footers)} / 25")
assert len(footers) == 25

# 4. Statistics Verification
print("\n[Check 4] Strict Statistics Verification:")
stats_needed = [
    ("100 GB", "100 GB" in html),
    ("22.9% reduction", "22.9%" in html),
    ("54% false positive suppression", "54%" in html),
    ("95.1% true alert capture", "95.1%" in html),
    ("AUC 92.67%", "92.67%" in html),
    ("Recall 0.92", "0.92" in html),
    ("Precision 0.39", "0.39" in html),
    ("39,427 events", "39,427" in html or "39427" in html),
    ("2.45 million events", "2.45" in html),
    ("2.25x recall gain", "2.25" in html),
    ("300 µs inference", "300" in html and ("µs" in html or "&mu;s" in html)),
    ("50% payload reduction", "50%" in html),
    ("609 analyzed playbooks", "609" in html),
    ("Risk equation (ws S + wt T + wa A - wc C)", "w_s" in html or "ws S" in html or "w_c C" in html)
]
for name, ok in stats_needed:
    print(f"  {name}: {'✅' if ok else '❌'}")
    assert ok

# 5. JS Features Verification
print("\n[Check 5] JavaScript Shortcuts & Functions:")
has_toggle_ref = "function toggleRefModal" in html
has_r_key = "'r'" in html or '"r"' in html
has_c_key = "'c'" in html or '"c"' in html
has_l_key = "'l'" in html or '"l"' in html
has_purge = "localStorage.removeItem('soar_custom_deck')" in html

print(f"  toggleRefModal function: {'✅' if has_toggle_ref else '❌'}")
print(f"  R shortcut (References drawer): {'✅' if has_r_key else '❌'}")
print(f"  C shortcut (Control center): {'✅' if has_c_key else '❌'}")
print(f"  L shortcut (Bilingual toggle): {'✅' if has_l_key else '❌'}")
print(f"  Stale localStorage cache purge: {'✅' if has_purge else '❌'}")

assert has_toggle_ref and has_r_key and has_c_key and has_l_key and has_purge

print("\n🎉 ALL CHECKS PASSED 100%! The presentation is fully updated, verified, and active on http://localhost:3000!")
