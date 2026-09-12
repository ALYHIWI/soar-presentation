import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

obj = json.loads(lines[50])
content = obj.get('content', '')

for q in ['Risk =', 'w1', 'Formula', 'Figure 3-4', 'Figure 3-5']:
    idx = content.find(q)
    print(f'Search for "{q}": idx={idx}')
    if idx != -1:
        print(content[idx:idx+400])
