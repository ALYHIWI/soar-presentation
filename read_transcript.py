# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')

# Find USER_INPUT lines
for i, line in enumerate(lines):
    try:
        obj = json.loads(line)
        t = obj.get('type', '')
        src = obj.get('source', '')
        if t == 'USER_INPUT':
            content = obj.get('content', '')
            print(f'\n=== Line {i}: USER_INPUT ===')
            print(content[:3000])
            print('...')
    except:
        pass
