import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract the 20 slides between line 2028 and 2944
slide_pattern = re.compile(r'<section\b[^>]*id=["\']([^"\']+)["\'][^>]*>(.*?)</section>', re.DOTALL)
all_matches = list(slide_pattern.finditer(text))

print(f"Total matches: {len(all_matches)}")
new_20_slides = all_matches[:20]

for idx, m in enumerate(new_20_slides):
    s_id = m.group(1)
    s_html = m.group(2)
    # Get titles
    h1_en = re.findall(r'<h1[^>]*class=["\'][^"\']*en[^"\']*["\'][^>]*>(.*?)</h1>', s_html, re.DOTALL)
    if not h1_en:
        h1_en = re.findall(r'<h1[^>]*>(.*?)</h1>', s_html, re.DOTALL)
    h2_en = re.findall(r'<h2[^>]*class=["\'][^"\']*en[^"\']*["\'][^>]*>(.*?)</h2>', s_html, re.DOTALL)
    h2_ar = re.findall(r'<h2[^>]*class=["\'][^"\']*ar[^"\']*["\'][^>]*>(.*?)</h2>', s_html, re.DOTALL)
    cards = len(re.findall(r'class=["\'][^"\']*card[^"\']*["\']', s_html))
    stats = re.findall(r'class=["\']snum["\']>([^<]+)<', s_html)
    sn = re.findall(r'<div class="sn">([^<]+)</div>', s_html)
    
    title_en = (h2_en[0] if h2_en else (h1_en[0] if h1_en else "No Title"))
    title_en = re.sub(r'<[^>]+>', '', title_en).strip()
    title_ar = h2_ar[0] if h2_ar else ""
    title_ar = re.sub(r'<[^>]+>', '', title_ar).strip()
    
    print(f"\n--- Slide {idx+1:02d} ({s_id}) | SN: {sn[0] if sn else 'None'} ---")
    print(f"EN Title: {title_en}")
    print(f"AR Title: {title_ar}")
    print(f"Cards count: {cards}, Stats: {stats}")
