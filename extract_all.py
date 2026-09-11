# -*- coding: utf-8 -*-
import json

path = r'C:\Users\Mo AL-Yahawy\.gemini\antigravity-ide\brain\027b33b7-01fc-40d8-b890-5eff14eda53c\.system_generated\logs\transcript_full.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

obj = json.loads(lines[50])
content = obj.get('content', '')

# Extract from position 9783 (start of Chapter 1 body) onwards
ch1_body_start = 9783
text = content[ch1_body_start:]

# Find key sections
sections = {}
markers = [
    ('1.1_SOC_Overview', 'A Security Operations Center (SOC) is a centralized'),
    ('1.2_Problem_Statement', '1.2\tThe Problem Statement'),
    ('1.3_Motivation', '1.3\tMotivation'),
    ('1.4_Objectives', '1.4\tProject Objectives'),
    ('1.6_Scope', '1.6\tProject Scope'),
    ('ch2_start', '2.1\tIntroduction'),
    ('2.2_SOAR', '2.2\tTechnical Background'),
    ('2.3_AI', '2.3\tAI and ML as a Force Multiplier'),
    ('2.4_ML_Review', '2.4\tReview of Existing ML'),
    ('2.5_Gap', '2.5\tGap Analysis'),
    ('ch3_arch', '3.2\tHigh-Level Architecture Overview'),
    ('3.3_ingestion', '3.3\tIngestion'),
    ('3.5_ML_engine', '3.5 Machine Learning Triage'),
    ('3.7_response', '3.7\tAutomated Response Policy'),
    ('3.8_feedback', '3.8\tAnalyst Feedback Loop'),
]

section_positions = []
for name, marker in markers:
    pos = text.find(marker)
    if pos >= 0:
        section_positions.append((pos, name, marker))

section_positions.sort()

output = []
for i, (pos, name, marker) in enumerate(section_positions):
    # Get next 1500 chars or until next section
    if i + 1 < len(section_positions):
        end = section_positions[i+1][0]
    else:
        end = pos + 3000
    output.append(f'\n\n{"="*60}')
    output.append(f'SECTION: {name}')
    output.append('='*60)
    output.append(text[pos:min(end, pos+2500)])

with open(r'c:\Users\Mo AL-Yahawy\SOAR\chapters_text.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("Saved to chapters_text.txt")
for pos, name, _ in section_positions:
    print(f"  {name}: at {pos}")
