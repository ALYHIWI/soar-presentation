import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total slides currently: {len(slides)}")

targets = [2, 4, 7, 8, 11, 12, 13, 15, 17, 18, 20]

with open('scratch/target_slides_inspection.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        s_num = idx + 1
        headers = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', content, re.DOTALL)
        clean_headers = [re.sub(r'<[^>]+>', ' ', h).strip() for h in headers]
        clean_headers = [' '.join(h.split()) for h in clean_headers]
        out.write(f"\n{'='*70}\n")
        out.write(f"SLIDE {s_num:02d} [id={sid}]\n")
        out.write(f"Headers: {' | '.join(clean_headers)}\n")
        
        # Check specific items
        if s_num == 2:
            mv_m = re.findall(r'.{0,40}Multi\s*Vendor.{0,40}', content, re.IGNORECASE)
            out.write(f"Multi-Vendor matches: {mv_m}\n")
        if s_num == 4:
            src_m = re.findall(r'.{0,40}Source.{0,40}', content, re.IGNORECASE)
            pct_m = re.findall(r'.{0,40}91%.{0,40}', content)
            out.write(f"Source matches: {src_m}\n")
            out.write(f"91% matches: {pct_m}\n")
        if s_num == 7:
            img_m = re.findall(r'<img[^>]+>', content)
            out.write(f"Images in Slide 7: {img_m}\n")
        if s_num in [8, 11, 12, 13, 15, 17, 18, 20]:
            out.write(f"Snippet: {content[:400]}...\n")

print("Saved scratch/target_slides_inspection.txt")
