with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('textEn: "Python 3.11+, FastAPI')
if pos != -1:
    # search backwards for const or let or var
    p_var = html.rfind('const ', 0, pos)
    print("Found const at:", p_var)
    print(html[p_var:pos+500])
