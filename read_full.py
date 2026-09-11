# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')

# Find the big USER_INPUT at line 50
for i, line in enumerate(lines):
    try:
        obj = json.loads(line)
        t = obj.get('type', '')
        if t == 'USER_INPUT' and i == 50:
            content = obj.get('content', '')
            print(f'Line 50 length: {len(content)}')
            # Print from beginning looking for chapter 1
            ch1_idx = content.find('Chapter 1')
            if ch1_idx == -1:
                ch1_idx = content.find('1 Introduction')
            print(f'Chapter 1 at: {ch1_idx}')
            if ch1_idx >= 0:
                print(content[ch1_idx:ch1_idx+5000])
            break
    except Exception as e:
        print(f'Error on line {i}: {e}')
