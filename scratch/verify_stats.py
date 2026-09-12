import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ("100 GB", "100 GB" in text or "100GB" in text),
    ("22.9%", "22.9%" in text or "22.9" in text),
    ("54%", "54%" in text),
    ("95.1%", "95.1%" in text),
    ("AUC 92.67%", "92.67%" in text),
    ("Recall 0.92", "0.92" in text),
    ("Precision 0.39", "0.39" in text),
    ("39,427", "39,427" in text or "39427" in text),
    ("2.45", "2.45" in text),
    ("2.25x", "2.25" in text),
    ("300 µs", "300" in text and ("µs" in text or "μs" in text or "us" in text or "microsec" in text)),
    ("50% (Chavali)", "50%" in text),
    ("609 playbooks", "609" in text),
    ("Risk equation (ws S + wt T + wa A - wc C)", "w_s" in text or "ws" in text or "w_c C" in text or "w_c" in text)
]

for name, found in checks:
    status = "✅ PASS" if found else "❌ FAIL"
    print(f"{status}: {name}")
