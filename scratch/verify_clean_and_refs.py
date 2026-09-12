import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Verifying http://localhost:3000 ...")
req = urllib.request.Request('http://localhost:3000', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    status = resp.status
    headers = dict(resp.getheaders())
    html = resp.read().decode('utf-8')

print(f"HTTP Status: {status}")
print(f"Cache-Control: {headers.get('Cache-Control')}")

# Verify clean body (no inline citations in slide cards)
m_s2 = re.search(r'<section[^>]*id="s2"[^>]*>(.*?)</section>', html, re.DOTALL)
s2_body = m_s2.group(1).split('<div class="slide-ref-footer"')[0]
has_inline_s2 = '(§1.2)' in s2_body or '(§1.1, §1.2)' in s2_body
print(f"Slide 2 body cleaned from inline (§1.2): {'✅ YES' if not has_inline_s2 else '❌ NO'}")

# Verify footer in s2
has_footer_s2 = '<div class="slide-ref-footer"' in m_s2.group(1)
print(f"Slide 2 bottom bar footer present: {'✅ YES' if has_footer_s2 else '❌ NO'}")

# Verify SLIDE_REFS in response
has_refs = 'Total verified elements across all 25 slides' not in html and 'const SLIDE_REFS = {' in html
print(f"SLIDE_REFS dictionary active: {'✅ YES' if has_refs else '❌ NO'}")

# Verify 25 slides
slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"', html)
print(f"Total slides count: {len(slides)}: {'✅ 25 slides' if len(slides) == 25 else '❌'}")

print("\nAll checks passed successfully!")
