# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

obj = json.loads(lines[50])
content = obj.get('content', '')

# Look for all occurrences of "1.1" to find the actual chapter body
positions = []
start = 0
while True:
    idx = content.find('A Security Operations Center (SOC)', start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

print(f"Found SOC definition at positions: {positions}")
if positions:
    for pos in positions:
        print(f"\n--- Position {pos} ---")
        print(content[pos:pos+2000])
        print()
