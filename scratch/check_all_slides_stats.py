import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

for idx, (sid, content) in enumerate(slides):
    # strip tags
    clean = re.sub(r'<[^>]+>', ' ', content)
    # find percentages, numbers, stats
    nums = re.findall(r'(?:\b\d+(?:\.\d+)?%|\b\d+(?:\.\d+)?\s*(?:GB|events?|alerts?|incidents?|min|sec|microseconds?|times?|playbooks?)\b|AUC|recall|precision)', clean, re.IGNORECASE)
    # find citations
    cites = re.findall(r'\b(?:[A-Z][a-zA-Z]+ et al\., \d{4}|[A-Z][a-zA-Z]+ & [A-Z][a-zA-Z]+, \d{4})\b', clean)
    print(f"Slide {idx+1} ({sid}):")
    if nums:
        print(f"   Stats: {nums}")
    if cites:
        print(f"   Cites: {list(set(cites))}")
