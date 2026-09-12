import re

with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

suspicious = [
    'Gartner', 'Cisco', 'Ponemon', 'IBM', '10K', '45 min', '42.0 min', '42 min', '2.5 sec',
    'FastAPI', 'Redis', 'Celery', 'Wazuh', 'Suricata', 'Atomic Red Team', 'Docker',
    'Stable-Baselines3', 'Scikit-Learn', 'PyTorch', 'OpenSearch', 'PostgreSQL',
    'T1059', 'T1078', 'T1486', '0.90', '0.70', '94.2'
]

print('=== Comprehensive Whole-File Scan for Suspicious Terms ===')
total = 0
for s in suspicious:
    matches = list(re.finditer(r'\b' + re.escape(s) + r'\b', html, re.IGNORECASE))
    if matches:
        print(f'Term "{s}": {len(matches)} matches!')
        total += len(matches)
        for m in matches[:2]:
            start = max(0, m.start() - 50)
            end = min(len(html), m.end() + 50)
            print(f'   ...{html[start:end].replace("\n", " ")}...')

if total == 0:
    print('PERFECT! EXACT ZERO SUSPICIOUS TERMS IN THE ENTIRE HTML FILE!')
else:
    print(f'TOTAL FOUND: {total}')
