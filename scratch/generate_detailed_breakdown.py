import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

with open('scratch/detailed_slide_breakdown.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        out.write(f"\n{'='*80}\nSLIDE {idx+1:02d} ({sid})\n{'='*80}\n")
        
        # Heading
        title_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', content, re.DOTALL)
        title = re.sub(r'<[^>]+>', ' ', title_m.group(1)).strip() if title_m else ""
        out.write(f"Title: {title}\n")
        
        # Lead
        lead_m = re.search(r'<p class="lead en"[^>]*>(.*?)</p>', content, re.DOTALL)
        if lead_m:
            out.write(f"Lead text: {re.sub(r'<[^>]+>', ' ', lead_m.group(1)).strip()}\n")
            
        # Banner/hl
        hl_m = re.findall(r'<div class="hl"[^>]*>(.*?)</div>', content, re.DOTALL)
        for h in hl_m:
            out.write(f"Banner/HL: {re.sub(r'<[^>]+>', ' ', h).strip()}\n")
            
        # Cards
        cards = re.findall(r'<div class="card[^"]*"[^>]*>(.*?)</div>\s*(?=<div class="card|<div class="sb|<div class="stage|<div class="hl|<div class="grid|$)', content, re.DOTALL)
        for c_idx, c in enumerate(cards):
            c_title = re.search(r'<h[345][^>]*>(.*?)</h[345]>', c, re.DOTALL)
            t_str = re.sub(r'<[^>]+>', ' ', c_title.group(1)).strip() if c_title else f"Card {c_idx+1}"
            
            # extract text
            p_text = re.findall(r'<p class="en"[^>]*>(.*?)</p>', c, re.DOTALL)
            p_str = " ".join([re.sub(r'<[^>]+>', ' ', p).strip() for p in p_text])
            if not p_str:
                # check lis
                lis = re.findall(r'<li[^>]*>(.*?)</li>', c, re.DOTALL)
                p_str = " | ".join([re.sub(r'<[^>]+>', ' ', li).strip() for li in lis])
            out.write(f"  Card {c_idx+1}: [{t_str}] -> {p_str[:120]}\n")
            
        # Stats
        stats = re.findall(r'<div class="sb"[^>]*>.*?<div class="snum">(.*?)</div>.*?<div class="slbl en">(.*?)</div>', content, re.DOTALL)
        for s_idx, (num, lbl) in enumerate(stats):
            out.write(f"  Stat {s_idx+1}: {num.strip()} ({lbl.strip()})\n")
            
        # Stages
        stages = re.findall(r'<div class="stage"[^>]*>(.*?)</div>', content, re.DOTALL)
        for st_idx, st in enumerate(stages):
            out.write(f"  Stage {st_idx+1}: {re.sub(r'<[^>]+>', ' ', st).strip()[:100]}\n")

print("Saved scratch/detailed_slide_breakdown.txt")
