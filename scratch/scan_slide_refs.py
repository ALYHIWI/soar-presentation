import re

with open('scratch/all_slide_refs.js', 'r', encoding='utf-8') as f:
    text = f.read()

suspicious = [
    'Gartner', 'Cisco', 'Ponemon', 'IBM', '10K', '45 min', '42.0 min', '42 min', '2.5 sec',
    'FastAPI', 'Redis', 'Celery', 'Wazuh', 'Suricata', 'Atomic Red Team', 'Docker',
    'Stable-Baselines3', 'Scikit-Learn', 'PyTorch', 'OpenSearch', 'PostgreSQL',
    'T1059', 'T1078', 'T1486', '0.90', '0.70', '94.2'
]

print("=== Scanning all_slide_refs.js for suspicious terms ===")
for term in suspicious:
    matches = list(re.finditer(term, text, re.IGNORECASE))
    if matches:
        print(f"Found '{term}': {len(matches)} times")
        for m in matches[:2]:
            start = max(0, m.start() - 60)
            end = min(len(text), m.end() + 60)
            print(f"   Snippet: ...{text[start:end].replace('\n', ' ')}...")
