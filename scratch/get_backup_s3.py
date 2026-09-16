import re

with open('presentation/index.html.pre_illustrations_backup', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<section\b[^>]*id=["\']s3["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m:
    with open('scratch/backup_s3.html', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print("Wrote scratch/backup_s3.html")
else:
    print("s3 not found in backup")
