with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('textEn: "Python 3.11+, FastAPI')
print('Found at:', pos)
if pos != -1:
    print("--- CONTEXT AROUND MATCH ---")
    print(html[pos-300:pos+1200])
