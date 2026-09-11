import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class=["\']slide[^"\']*["\'][^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total slides: {len(slides)}")

with open(r'c:\Users\Mo AL-Yahawy\SOAR\scratch\slides_summary.txt', 'w', encoding='utf-8') as out:
    for i, s in enumerate(slides, 1):
        titles = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', s, re.DOTALL)
        title_str = " | ".join([re.sub(r'<[^>]+>', '', t).strip() for t in titles])
        title_str = ' '.join(title_str.split())
        
        # get all p and li texts
        paragraphs = re.findall(r'<p[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</p>', s, re.DOTALL)
        lis = re.findall(r'<li[^>]*class=["\']([^"\']*)["\'][^>]*>(.*?)</li>', s, re.DOTALL)
        
        out.write(f"=== SLIDE {i:02d}: {title_str} ===\n")
        for cls, p in paragraphs:
            clean = re.sub(r'<[^>]+>', '', p).strip()
            clean = ' '.join(clean.split())
            if clean:
                out.write(f"  [P:{cls}] {clean}\n")
        for cls, li in lis:
            clean = re.sub(r'<[^>]+>', '', li).strip()
            clean = ' '.join(clean.split())
            if clean:
                out.write(f"  [LI:{cls}] {clean}\n")
        out.write("\n")

print("Wrote slides summary to scratch/slides_summary.txt")
