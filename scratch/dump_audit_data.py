with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_start = html.find('const auditData =')
if pos_start == -1:
    pos_start = html.find('auditData')

print("auditData pos:", pos_start)
if pos_start != -1:
    pos_end = html.find('</script>', pos_start)
    with open('scratch/audit_data_js.txt', 'w', encoding='utf-8') as out:
        out.write(html[pos_start:pos_end])
    print("Saved scratch/audit_data_js.txt")
