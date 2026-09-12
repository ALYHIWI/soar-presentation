import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

with open('scratch/slide_elements_summary.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        body = content.split('<div class="slide-ref-footer"')[0]
        out.write(f"\n{'='*70}\n")
        out.write(f"SLIDE {idx+1:02d} ({sid})\n")
        out.write(f"{'='*70}\n")
        
        # Heading
        h1_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', body, re.DOTALL)
        if h1_m:
            out.write("Heading: " + re.sub(r'<[^>]+>', ' ', h1_m.group(1)).strip() + "\n")
            
        # Lead
        lead_m = re.search(r'<p class="lead en"[^>]*>(.*?)</p>', body, re.DOTALL)
        if lead_m:
            out.write("Lead: " + re.sub(r'<[^>]+>', ' ', lead_m.group(1)).strip() + "\n")
            
        # Cards
        cards = re.findall(r'<div class="card[^"]*"[^>]*>(.*?)</div>\s*(?=<div class="card|<div class="sb|<div class="stage|$)', body, re.DOTALL)
        out.write(f"Cards count: {len(cards)}\n")
        for c_idx, c in enumerate(cards):
            c_title = re.search(r'<h[345][^>]*>(.*?)</h[345]>', c, re.DOTALL)
            t_str = re.sub(r'<[^>]+>', ' ', c_title.group(1)).strip() if c_title else "No Title"
            out.write(f"  Card {c_idx+1}: {t_str}\n")
            
        # Stats / Stat boxes
        sbs = re.findall(r'<div class="sb"[^>]*>(.*?)</div>\s*</div>', body, re.DOTALL)
        if sbs:
            out.write(f"  Stat boxes found: {len(sbs)}\n")

print("Generated scratch/slide_elements_summary.txt")
