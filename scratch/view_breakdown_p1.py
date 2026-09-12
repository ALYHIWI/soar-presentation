import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/detailed_slide_breakdown.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Print first 200 lines
lines = text.splitlines()
for l in lines[:150]:
    print(l)
