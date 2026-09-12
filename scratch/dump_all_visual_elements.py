import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

with open('scratch/all_slides_visual_elements.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        out.write(f"\n{'='*80}\nSLIDE {idx+1:02d} (id='{sid}')\n{'='*80}\n")
        
        # 1. H1 / H2 Title
        title_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', content, re.DOTALL)
        if title_m:
            out.write("Title: " + re.sub(r'<[^>]+>', ' ', title_m.group(1)).strip() + "\n")
            
        # 2. Tag / Context
        tag_m = re.search(r'<div class="tag[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
        if tag_m:
            out.write("Tag: " + re.sub(r'<[^>]+>', ' ', tag_m.group(1)).strip() + "\n")
            
        # 3. Lead text
        lead_m = re.search(r'<p class="lead en"[^>]*>(.*?)</p>', content, re.DOTALL)
        if lead_m:
            out.write("Lead: " + re.sub(r'<[^>]+>', ' ', lead_m.group(1)).strip() + "\n")
            
        # 4. Any subtitles / highlighted banner
        hl_m = re.findall(r'<div class="hl"[^>]*>(.*?)</div>', content, re.DOTALL)
        for h in hl_m:
            out.write("Banner/HL: " + re.sub(r'<[^>]+>', ' ', h).strip() + "\n")
            
        # 5. Cards & Titles
        # Search for headings inside cards
        card_heads = re.findall(r'<div class="card[^"]*"[^>]*>.*?<h[345][^>]*>(.*?)</h[345]>(.*?)</div>', content, re.DOTALL)
        out.write(f"Cards found: {len(card_heads)}\n")
        for c_idx, (ch, cb) in enumerate(card_heads):
            ch_clean = re.sub(r'<[^>]+>', ' ', ch).strip()
            cb_clean = re.sub(r'<[^>]+>', ' ', cb).strip()
            out.write(f"  Card {c_idx+1}: {ch_clean}\n    Content: {cb_clean[:120]}...\n")
            
        # 6. Stat boxes (.sb)
        sb_boxes = re.findall(r'<div class="sb"[^>]*>.*?<div class="snum">(.*?)</div>.*?<div class="slbl en">(.*?)</div>', content, re.DOTALL)
        out.write(f"Stat boxes found: {len(sb_boxes)}\n")
        for s_idx, (num, lbl) in enumerate(sb_boxes):
            out.write(f"  Stat {s_idx+1}: {num.strip()} - {lbl.strip()}\n")
            
        # 7. Other structures: e.g. pipeline stages (.stage), table rows, or lists
        stages = re.findall(r'<div class="stage"[^>]*>(.*?)</div>', content, re.DOTALL)
        if stages:
            out.write(f"Stages found: {len(stages)}\n")
            for st_idx, st in enumerate(stages):
                out.write(f"  Stage {st_idx+1}: {re.sub(r'<[^>]+>', ' ', st).strip()[:80]}\n")
                
        table_rows = re.findall(r'<tr>(.*?)</tr>', content, re.DOTALL)
        if table_rows:
            out.write(f"Table rows found: {len(table_rows)}\n")

print("Saved scratch/all_slides_visual_elements.txt")
