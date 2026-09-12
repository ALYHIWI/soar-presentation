import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function tL')
if idx != -1:
    print(text[idx:idx+1000])
else:
    print("tL not found!")
