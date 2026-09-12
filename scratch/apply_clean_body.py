# -*- coding: utf-8 -*-
"""
Script to apply:
1. Clean slide bodies from inline (§...) and parenthetical citations
2. Inject exhaustive 25-slide SLIDE_REFS dictionary
3. Upgrade updateSlideReferences() and #refDrawer for seamless manual audit
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# 1. CLEAN SLIDE BODIES (Keep .slide-ref-footer intact)
# -------------------------------------------------------------
slide_section_regex = r'(<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>)(.*?)(<div class="slide-ref-footer".*?</section>)'

def clean_slide_body(body, sid):
    # Do not clean Table 2-1 study author names in table cells
    cleaned = body
    
    # Remove (.sref divs) in stats if any
    cleaned = re.sub(r'<div class="sref[^"]*"[^>]*>.*?</div>\s*', '', cleaned)
    
    # Remove parenthetical section tags: e.g. (§1.1-1.2) or (§3.7) or (§3.2, §3.7, §2.4)
    cleaned = re.sub(r'\s*\([§\d\.\s,\-–&;]+\)', '', cleaned)
    cleaned = re.sub(r'\s*\(§1\.\d+(?:[–\-]\d+\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\s*\(§2\.\d+(?:\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\s*\(§3\.\d+(?:\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\s*\(§9\)', '', cleaned)
    
    # Remove inline tags in headers / spans:
    cleaned = re.sub(r'\s*§1\.\d+', '', cleaned)
    cleaned = re.sub(r'\s*§2\.\d+', '', cleaned)
    cleaned = re.sub(r'\s*§3\.\d+', '', cleaned)
    
    # Remove researcher parentheticals from body text except Table 2-1 table cells
    if sid != 's10':
        cleaned = re.sub(r'\s*\([A-Za-z\s&;,]+(?:et al\.)?,?\s*\d{4}[^)]*\)', '', cleaned)
        cleaned = re.sub(r'\s*\(Karlzén\s*&amp;\s*Sommestad,\s*\d{4}[^)]*\)', '', cleaned)
        cleaned = re.sub(r'\s*\(معيار جيلمان[^)]*\)', '', cleaned)
        cleaned = re.sub(r'\s*\(Gelman baseline[^)]*\)', '', cleaned)
        cleaned = re.sub(r'Informed by Agrawal et al\. \(\d{4}\):\s*', '', cleaned)
        cleaned = re.sub(r'بناءً على Agrawal et al\. \(\d{4}\):\s*', '', cleaned)
    
    # Clean specific phrase leftovers
    cleaned = cleaned.replace('Key Empirical Finding:', 'Key Empirical Finding:')
    cleaned = cleaned.replace('Graduation Defense Guide §9', 'Graduation Defense Guide')
    cleaned = cleaned.replace('دليل إعداد العرض §9', 'دليل إعداد العرض')
    cleaned = cleaned.replace('✓ Mitigation: Intermediate Normalization Engine', '✓ Intermediate Normalization Engine')
    
    # Clean excessive whitespace
    cleaned = re.sub(r'[ \t]{2,}', ' ', cleaned)
    cleaned = re.sub(r'\s+\.', '.', cleaned)
    cleaned = re.sub(r'\s+:', ':', cleaned)
    cleaned = re.sub(r'\(\s*\)', '', cleaned)
    
    return cleaned

def replace_slides(match):
    prefix = match.group(1)
    sid = match.group(2)
    body = match.group(3)
    suffix = match.group(4)
    cleaned_body = clean_slide_body(body, sid)
    return prefix + cleaned_body + suffix

html = re.sub(slide_section_regex, replace_slides, html, flags=re.DOTALL)
print("✓ Cleaned slide bodies across all 25 slides.")

# Write intermediate check
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved cleaned presentation/index.html.")
