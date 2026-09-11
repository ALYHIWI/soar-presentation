# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Get line 50 content
obj = json.loads(lines[50])
content = obj.get('content', '')

# Find all chapter sections
sections = {
    '1.1': content.find('1.1\tOverview'),
    '1.2': content.find('1.2\tThe Problem'),
    '1.3': content.find('1.3\tMotivation'),
    '1.4': content.find('1.4\tProject Objectives'),
    '1.6': content.find('1.6\tProject Scope'),
    '2.2': content.find('2.2\tTechnical Background'),
    '2.3': content.find('2.3\tAI and ML'),
    '2.4': content.find('2.4\tReview of Existing'),
    '2.5': content.find('2.5\tGap Analysis'),
    '3.2': content.find('3.2\tHigh-Level Architecture'),
    '3.3': content.find('3.3\tIngestion'),
    '3.5': content.find('3.5 Machine Learning'),
    '3.7': content.find('3.7\tAutomated Response'),
    '3.8': content.find('3.8\tAnalyst Feedback'),
}

# Save each section to a file
output = []
for sec, idx in sorted(sections.items(), key=lambda x: x[1]):
    if idx >= 0:
        output.append(f'\n\n{"="*60}')
        output.append(f'SECTION {sec} (at {idx})')
        output.append('='*60)
        # Get next 3000 chars
        output.append(content[idx:idx+3000])

with open(r'c:\Users\Mo AL-Yahawy\SOAR\project_text.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("Done! Saved to project_text.txt")
print(f"Total content length: {len(content)}")
