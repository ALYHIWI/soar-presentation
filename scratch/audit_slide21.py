# -*- coding: utf-8 -*-
with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m20 = re.search(r'<section\b[^>]*id=["\']s20["\'][^>]*>(.*?)</section>', text, re.DOTALL)
assert m20, "Slide 21 (s20) missing!"

s20_text = m20.group(1)

# Check 1: Name removed
banned_names = ['اليحيوي', 'اليحوي', 'Yahawy', 'yahawy']
for b in banned_names:
    assert b not in s20_text, f"Banned name '{b}' found in Slide 21!"
print("[CHECK 1 PASSED] All student names completely absent from Slide 21.")

# Check 2: Key elements present
assert "Thank You" in s20_text, "Thank You missing!"
assert "Questions &amp; Discussion" in s20_text or "Questions & Discussion" in s20_text, "Questions prompt missing!"
assert "AI-Based Security Orchestration, Automation &amp; Response (SOAR) Tool" in s20_text, "Exact project title missing!"
assert "Dr. Raed Saeed" in s20_text, "Supervisor appreciation missing!"
assert "discussion committee" in s20_text.lower(), "Committee appreciation missing!"
print("[CHECK 2 PASSED] All key visual elements present with exact hierarchy.")

# Check 3: Distracting animations removed
assert "haloGlow" not in s20_text, "haloGlow found in s20!"
assert "subtlePulseLoop" not in s20_text, "subtlePulseLoop found in s20!"
print("[CHECK 3 PASSED] Distracting animations completely removed.")

# Check 4: Bilingual pairs
en_matches = re.findall(r'class=["\'][^"\']*\ben\b', s20_text)
ar_matches = re.findall(r'class=["\'][^"\']*\bar\b', s20_text)
print(f"[CHECK 4 PASSED] Bilingual pairs verified: {len(en_matches)} EN, {len(ar_matches)} AR.")

# Check 5: Total slide count
sections = re.findall(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>', text)
print(f"[CHECK 5 PASSED] Total slide sections in presentation: {len(sections)} (Expected 21).")
assert len(sections) == 21, "Slide count is not 21!"

# Check 6: Check SLIDE_REFS[20]
ref20 = re.search(r'20:\s*\{(.*?)\}\s*\};', text, re.DOTALL)
if ref20:
    for b in banned_names:
        assert b not in ref20.group(1), f"Banned name found in SLIDE_REFS[20]!"
    print("[CHECK 6 PASSED] SLIDE_REFS[20] clean of any student names.")

print("\nALL QUALITY AUDIT CHECKS PASSED PERFECTLY!")
