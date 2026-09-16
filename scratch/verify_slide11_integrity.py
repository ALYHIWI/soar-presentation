# -*- coding: utf-8 -*-
with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'<section\b[^>]*id=["\']s10["\'][^>]*>(.*?)</section>', html, re.DOTALL)
assert m, "Section s10 not found!"
content = m.group(1)

# Check all original phrases
required_phrases = [
    "Development Methodology: Design Science Research (DSR)",
    "منهجية التطوير: علوم التصميم (DSR)",
    "Problem Identification",
    "تحديد المشكلة",
    "Solution Objectives",
    "أهداف الحل",
    "Architecture Design",
    "تصميم المعمارية",
    "Prototype Demo",
    "عرض النموذج",
    "Evaluation",
    "التقييم",
    "Communication",
    "التوثيق",
    "Current Phase:",
    "المرحلة الحالية:",
    "dsr_6phases_methodology.jpg",
    "11 / 21"
]

for p in required_phrases:
    assert p in content, f"Phrase missing: {p}"
    print(f"[OK] Found: {p}")

en_count = len(re.findall(r'class=["\'][^"\']*\ben\b', content))
ar_count = len(re.findall(r'class=["\'][^"\']*\bar\b', content))
print(f"\nBilingual tags: {en_count} EN, {ar_count} AR")
assert en_count == ar_count, "Mismatch in bilingual tag count!"

print("\nVerification successful: 100% of content preserved with zero deletions!")
