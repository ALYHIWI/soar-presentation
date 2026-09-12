with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('textEn: "Python 3.11+, FastAPI')
p_start = html.rfind('<script', 0, pos)
print("Script tag before at:", p_start)
p_obj = html.rfind('const ', p_start, pos)
print("const before at:", p_obj)
print(html[p_obj:p_obj+100])
