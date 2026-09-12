import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Match all sections with class slide
slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Found {len(slides)} slides:\n")

with open('scratch/audit_report.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        sn = f"{idx+1:02d}"
        
        # Title
        h1_match = re.search(r'<h[12][^>]*>(.*?)</h[12]>', content, re.DOTALL)
        title = ""
        if h1_match:
            title = re.sub(r'<[^>]+>', ' ', h1_match.group(1)).strip()
            title = ' '.join(title.split())
            
        # Check slide number tag
        sn_tag = re.search(r'<div class="sn">([^<]+)</div>', content)
        sn_val = sn_tag.group(1) if sn_tag else "MISSING"
        
        # Check ref footer
        footer = re.search(r'<div class="slide-ref-footer"[^>]*>(.*?)</div>', content, re.DOTALL)
        if footer:
            f_text = re.sub(r'<[^>]+>', ' ', footer.group(1)).strip()
            f_text = ' '.join(f_text.split())
        else:
            f_text = "MISSING FOOTER"
            
        line = f"[{sn}] id={sid:4s} | sn={sn_val:7s} | Title={title[:50]:50s} | Footer={f_text[:70]}"
        print(line)
        out.write(line + "\n")

print("\nAudit written to scratch/audit_report.txt")
