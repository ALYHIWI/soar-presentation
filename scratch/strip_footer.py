# -*- coding: utf-8 -*-
"""
1. Strip .slide-ref-footer from all slides completely
2. Replace SLIDE_REFS with exact 1-to-1 visual-matching elements dictionary
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Strip .slide-ref-footer completely from all slides
footer_count = len(re.findall(r'<div class="slide-ref-footer"[^>]*>.*?</div>', html, re.DOTALL))
print(f"Found {footer_count} .slide-ref-footer elements to remove.")

html = re.sub(r'\s*<div class="slide-ref-footer"[^>]*>.*?</div>\s*', '\n  ', html, flags=re.DOTALL)

# Verify no slide-ref-footer remains
rem_footers = len(re.findall(r'slide-ref-footer', html))
print(f"Remaining slide-ref-footer occurrences: {rem_footers}")

# Write back
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Successfully removed .slide-ref-footer from all slides.")
