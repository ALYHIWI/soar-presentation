import re

with open('scratch/test_updated_presentation.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total slides in updated HTML: {len(slides)}")

suspicious_terms = [
    'Gartner', 'Cisco', 'Ponemon', 'IBM', '10K', '45 min', '42.0 min', '42 min', '2.5 sec',
    'FastAPI', 'Redis', 'Celery', 'Wazuh', 'Suricata', 'Atomic Red Team', 'Docker',
    'Stable-Baselines3', 'Scikit-Learn', 'PyTorch', 'OpenSearch', 'PostgreSQL',
    'T1059', 'T1078', 'T1486', '0.90', '0.70', '94.2'
]

print("\n--- Scanning for suspicious terms in updated HTML ---")
total_found = 0
for idx, (sid, content) in enumerate(slides):
    for term in suspicious_terms:
        if term.lower() in content.lower():
            print(f"Slide {idx+1} ({sid}): STILL HAS {term}")
            total_found += 1

if total_found == 0:
    print("SUCCESS: 0 suspicious terms found! All 25 slides clean!")

print("\n--- Verifying slide numbers and IDs ---")
for idx, (sid, content) in enumerate(slides):
    sn = re.findall(r'<div\s+class="sn">\s*(\d{2}\s*/\s*25)\s*</div>', content)
    sn_val = sn[0] if sn else "MISSING"
    expected = f"{idx+1:02d} / 25"
    if sn_val != expected:
        print(f"WARNING: Slide {idx+1} ({sid}) sn is '{sn_val}', expected '{expected}'")
print("Slide number verification complete.")
