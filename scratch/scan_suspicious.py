import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

suspicious_terms = [
    'Gartner', 'Cisco', 'Ponemon', 'IBM', '10K', '45 min', '42.0 min', '42 min', '2.5 sec',
    'FastAPI', 'Redis', 'Celery', 'Wazuh', 'Suricata', 'Atomic Red Team', 'Docker',
    'Stable-Baselines3', 'Scikit-Learn', 'PyTorch', 'OpenSearch', 'PostgreSQL',
    'T1059', 'T1078', 'T1486', '0.90', '0.70', '94.2'
]

print("=== Scanning 25 slides for unverified / suspicious terms ===")
for idx, (sid, content) in enumerate(slides):
    found = []
    for term in suspicious_terms:
        if term.lower() in content.lower():
            found.append(term)
    if found:
        print(f"Slide {idx+1} (id='{sid}'): FOUND {found}")
    else:
        # check if it has other numbers
        pass
