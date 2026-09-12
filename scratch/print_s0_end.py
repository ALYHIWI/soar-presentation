import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="s0"')
if idx != -1:
    end_s0 = text.find('</section>', idx)
    print(text[idx+2000:end_s0+10])
