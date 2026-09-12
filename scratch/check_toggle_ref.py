import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function toggleRefModal')
if idx != -1:
    print(text[idx:idx+800])
else:
    print("toggleRefModal not found!")
