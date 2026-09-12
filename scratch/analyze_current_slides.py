import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all slides
slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total slides found: {len(slides)}")

with open('scratch/current_slides_overview.txt', 'w', encoding='utf-8') as out:
    for idx, (sid, content) in enumerate(slides):
        out.write(f"\n{'='*70}\n")
        out.write(f"SLIDE {idx+1} (id='{sid}')\n")
        out.write(f"{'='*70}\n")
        
        # Extract title / headers
        headers = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL)
        clean_headers = [re.sub(r'<[^>]+>', '', h).strip() for h in headers]
        out.write("Headers: " + " | ".join(clean_headers) + "\n")
        
        # Extract any numbers or statistics
        text_only = re.sub(r'<[^>]+>', ' ', content)
        # Find stats or numbers
        numbers = re.findall(r'(?:[\$€£]?\d+(?:\.\d+)?%?|\b(?:sec|min|hours?|GB|events?|alerts?)\b)', text_only)
        out.write(f"Numbers/Units: {numbers[:15]}\n")
        
        # Print snippet of slide text
        clean_text = ' '.join(text_only.split())
        out.write(f"Content preview: {clean_text[:300]}...\n")

print("Saved scratch/current_slides_overview.txt")
