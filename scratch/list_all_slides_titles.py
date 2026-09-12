import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

print("=== Checking Slide Headers & Citations for All 25 Slides ===")
for idx, (sid, content) in enumerate(slides):
    headers = re.findall(r'<h2[^>]*class="st[^"]*en"[^>]*>(.*?)</h2>', content)
    tag = re.findall(r'<span\s+class="en"[^>]*>(.*?)</span>', content)
    tag_str = tag[0] if tag else "NO TAG"
    h2_str = headers[0] if headers else "NO H2"
    print(f"Slide {idx+1:02d} [{sid}]: Tag='{tag_str}' | Title='{h2_str}'")
