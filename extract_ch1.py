# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

obj = json.loads(lines[50])
content = obj.get('content', '')

# The actual Chapter 1 body text starts AFTER the table of contents
# Look for "Chapter 1:\r\r\nIntroduction and Problem Statement\r\r\n \r\r\n1.1"
ch1_real = content.find('Chapter 1:\r\r\nIntroduction and Problem Statement\r\r\n \r\r\n1.1')
print(f"Real Chapter 1 at: {ch1_real}")

if ch1_real >= 0:
    print(content[ch1_real:ch1_real+6000])
