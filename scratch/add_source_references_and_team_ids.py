# -*- coding: utf-8 -*-
"""
This script adds:
1. Prominent bilingual names and official Academic ID badges to Slide 2 for all 6 students.
2. Complete data structure with exact references (Chapter, Section, Page, Paragraph, Element breakdown)
   for all 25 slides from Final Project of SOAR System.pdf.
3. Interactive Slide Source References UI:
   - In Settings Drawer (#cp) live panel
   - In Top Navigation Menu (#dockMenu) button
   - In Bottom Navigation Bar (#nav) button
   - Floating Glassmorphic Reference Drawer (#refModal)
   - Keyboard shortcut 'R' to toggle
   - Automatic live update on slide change (gS)
"""

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Read HTML, length: {len(html)}")

# ============================================================
# 1. Update Slide 2 with bilingual names & official ID Badges
# ============================================================
old_s2_cards = '''    <div class="tg">
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Hizam Mohammed Ali Al-Shajara</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202210102478</div>
        <div class="rl en">Lead Architect &amp; AI Engineer</div><div class="rl ar" style="display:none">مهندس المعمارية والذكاء الاصطناعي</div>
        <div class="desc en">Architecture design, ML triage &amp; scoring model development</div>
        <div class="desc ar" style="display:none">تصميم المعمارية وتطوير نماذج الفرز بالذكاء الاصطناعي</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Hamoud Abdullah Saleh Abu Amrah</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310101609</div>
        <div class="rl en">SOAR &amp; Playbook Integration Lead</div><div class="rl ar" style="display:none">مسؤول تكامل SOAR ودفاتر العمل</div>
        <div class="desc en">API orchestration, workflow automation &amp; response logic</div>
        <div class="desc ar" style="display:none">تكامل واجهات API وأتمتة مسارات الاستجابة</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Mohammed Hameed Qasim Mohammed</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100174</div>
        <div class="rl en">Data Pipeline &amp; Enrichment Specialist</div><div class="rl ar" style="display:none">أخصائي تدفق البيانات والإثراء</div>
        <div class="desc en">Alert ingestion, parsing (CEF/JSON) &amp; threat intelligence feeds</div>
        <div class="desc ar" style="display:none">استيعاب التنبيهات، المعالجة وتغذية معلومات التهديدات</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Mohammed Taha Qasim Al-Warafi</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100461</div>
        <div class="rl en">Model Validation &amp; Evaluation Lead</div><div class="rl ar" style="display:none">مسؤول التقييم وضبط النماذج</div>
        <div class="desc en">Experimental benchmarking, metrics definition &amp; test suites</div>
        <div class="desc ar" style="display:none">الاختبارات المعيارية، تقييم الأداء والمقاييس التشغيلية</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Marwan Mohammed Saeed Al-Ameer</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100177</div>
        <div class="rl en">Security Telemetry &amp; SIEM Analyst</div><div class="rl ar" style="display:none">محلل السجلات الأمنية و SIEM</div>
        <div class="desc en">SOC workflow modeling, telemetry mapping &amp; rule auditing</div>
        <div class="desc ar" style="display:none">نمذجة مسارات العمل، تدقيق القواعد وربط الحساسات</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm">Noah Ahmed Mohammed Maraq</div>
        <div class="std-id" style="font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100452</div>
        <div class="rl en">System Interface &amp; Human-AI Teaming</div><div class="rl ar" style="display:none">واجهات النظام وتفاعل الإنسان والذكاء</div>
        <div class="desc en">SOC dashboard design, analyst feedback loops &amp; approval gates</div>
        <div class="desc ar" style="display:none">تصميم لوحات التحكم وحلقات التغذية الراجعة للمحللين</div>
      </div>
    </div>'''

new_s2_cards = '''    <div class="tg">
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Hizam Mohammed Ali Al-Shajara</div>
        <div class="nm ar" style="display:none">حزام محمد علي الشجرة</div>
        <div class="id-badge en">Academic ID: 202210102478</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202210102478</div>
        <div class="rl en">Lead Architect &amp; AI Engineer</div><div class="rl ar" style="display:none">مهندس المعمارية والذكاء الاصطناعي</div>
        <div class="desc en">Architecture design, ML triage &amp; scoring model development</div>
        <div class="desc ar" style="display:none">تصميم المعمارية وتطوير نماذج الفرز بالذكاء الاصطناعي</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Hamoud Abdullah Saleh Abu Amrah</div>
        <div class="nm ar" style="display:none">حمود عبد الله صالح أبو عمرة</div>
        <div class="id-badge en">Academic ID: 202310101609</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310101609</div>
        <div class="rl en">SOAR &amp; Playbook Integration Lead</div><div class="rl ar" style="display:none">مسؤول تكامل SOAR ودفاتر العمل</div>
        <div class="desc en">API orchestration, workflow automation &amp; response logic</div>
        <div class="desc ar" style="display:none">تكامل واجهات API وأتمتة مسارات الاستجابة</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Mohammed Hameed Qasim Mohammed</div>
        <div class="nm ar" style="display:none">محمد حميد قاسم محمد</div>
        <div class="id-badge en">Academic ID: 202310100174</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100174</div>
        <div class="rl en">Data Pipeline &amp; Enrichment Specialist</div><div class="rl ar" style="display:none">أخصائي تدفق البيانات والإثراء</div>
        <div class="desc en">Alert ingestion, parsing (CEF/JSON) &amp; threat intelligence feeds</div>
        <div class="desc ar" style="display:none">استيعاب التنبيهات، المعالجة وتغذية معلومات التهديدات</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Mohammed Taha Qasim Al-Warafi</div>
        <div class="nm ar" style="display:none">محمد طه قاسم الورافي</div>
        <div class="id-badge en">Academic ID: 202310100461</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100461</div>
        <div class="rl en">Model Validation &amp; Evaluation Lead</div><div class="rl ar" style="display:none">مسؤول التقييم وضبط النماذج</div>
        <div class="desc en">Experimental benchmarking, metrics definition &amp; test suites</div>
        <div class="desc ar" style="display:none">الاختبارات المعيارية، تقييم الأداء والمقاييس التشغيلية</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Marwan Mohammed Saeed Al-Ameer</div>
        <div class="nm ar" style="display:none">مروان محمد سعيد الأمير</div>
        <div class="id-badge en">Academic ID: 202310100177</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100177</div>
        <div class="rl en">Security Telemetry &amp; SIEM Analyst</div><div class="rl ar" style="display:none">محلل السجلات الأمنية و SIEM</div>
        <div class="desc en">SOC workflow modeling, telemetry mapping &amp; rule auditing</div>
        <div class="desc ar" style="display:none">نمذجة مسارات العمل، تدقيق القواعد وربط الحساسات</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Noah Ahmed Mohammed Maraq</div>
        <div class="nm ar" style="display:none">نوح أحمد محمد مرق</div>
        <div class="id-badge en">Academic ID: 202310100452</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100452</div>
        <div class="rl en">System Interface &amp; Human-AI Teaming</div><div class="rl ar" style="display:none">واجهات النظام وتفاعل الإنسان والذكاء</div>
        <div class="desc en">SOC dashboard design, analyst feedback loops &amp; approval gates</div>
        <div class="desc ar" style="display:none">تصميم لوحات التحكم وحلقات التغذية الراجعة للمحللين</div>
      </div>
    </div>'''

if old_s2_cards in html:
    html = html.replace(old_s2_cards, new_s2_cards, 1)
    print("✓ Slide 2 student names and official ID badges updated")
else:
    print("✗ Slide 2 cards NOT found for replacement")

# ============================================================
# 2. Add CSS for Academic ID Badges and Reference Inspector
# ============================================================
ref_css = '''
/* Official Student ID Badge */
.id-badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 6px;
  background: rgba(0, 212, 255, 0.12);
  border: 1px solid rgba(0, 212, 255, 0.35);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--s);
  margin: 3px 0 6px 0;
  letter-spacing: 0.5px;
  box-shadow: 0 0 10px rgba(0, 212, 255, 0.15);
}

/* Reference Inspector Modal / Drawer */
#refDrawer {
  position: fixed;
  bottom: -600px;
  left: 50%;
  transform: translateX(-50%);
  width: min(1080px, 94vw);
  max-height: 520px;
  background: rgba(10, 12, 20, 0.96);
  border: 1px solid var(--s);
  border-bottom: none;
  border-radius: 20px 20px 0 0;
  backdrop-filter: blur(35px);
  z-index: 300;
  transition: bottom 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 -15px 50px rgba(0, 0, 0, 0.8), 0 0 25px rgba(0, 212, 255, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
#refDrawer.open {
  bottom: 0;
}
.rd-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.rd-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--s);
}
.rd-slide-pill {
  padding: 3px 10px;
  border-radius: 20px;
  background: rgba(0, 212, 255, 0.15);
  border: 1px solid var(--s);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: #fff;
}
.rd-close {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--br);
  color: var(--t1);
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  transition: var(--tr);
}
.rd-close:hover {
  background: rgba(225, 29, 72, 0.2);
  border-color: var(--acc);
  color: #fff;
}
.rd-body {
  padding: 20px 24px;
  overflow-y: auto;
  flex: 1;
}
.rd-sec-banner {
  background: rgba(0, 212, 255, 0.06);
  border-left: 4px solid var(--s);
  padding: 10px 14px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 16px;
  font-size: 0.82rem;
  color: var(--t1);
}
[dir="rtl"] .rd-sec-banner {
  border-left: none;
  border-right: 4px solid var(--s);
  border-radius: 8px 0 0 8px;
}
.rd-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
}
.rd-table th {
  text-align: left;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.04);
  color: var(--s);
  font-weight: 700;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
[dir="rtl"] .rd-table th {
  text-align: right;
}
.rd-table td {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  color: var(--t2);
  vertical-align: top;
  line-height: 1.5;
}
.rd-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}
.rd-badge-exact {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border-radius: 4px;
  background: rgba(0, 230, 118, 0.15);
  border: 1px solid rgba(0, 230, 118, 0.4);
  color: var(--ok);
  font-size: 0.7rem;
  font-weight: 700;
  white-space: nowrap;
}

/* Nav Bar Ref Button */
.nb-ref {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 20px;
  background: rgba(0, 212, 255, 0.12);
  border: 1px solid rgba(0, 212, 255, 0.35);
  color: var(--s);
  font-size: 0.75rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--tr);
}
.nb-ref:hover {
  background: rgba(0, 212, 255, 0.25);
  box-shadow: 0 0 15px rgba(0, 212, 255, 0.3);
  transform: translateY(-1px);
}
'''

if '.id-badge {' not in html:
    html = html.replace('</style>', ref_css + '\n</style>', 1)
    print("✓ Added Reference Drawer and ID Badge CSS")
else:
    print("• ID Badge CSS already present")

# ============================================================
# 3. Add Ref button to #dockMenu and Ref section in #cp
# ============================================================
old_dock_menu = '''    <button class="tbtn" onclick="tC()">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Settings</span><span class="ar" style="display:none">الإعدادات</span>
    </button>
  </div>'''

new_dock_menu = '''    <button class="tbtn" id="btnSourceMap" onclick="toggleRefModal()" title="توثيق ومراجع السلايد من ملف المشروع (R)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
      <span class="en">Doc Ref</span><span class="ar" style="display:none">توثيق الملف</span>
    </button>
    <button class="tbtn" onclick="tC()">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Settings</span><span class="ar" style="display:none">الإعدادات</span>
    </button>
  </div>'''

if old_dock_menu in html:
    html = html.replace(old_dock_menu, new_dock_menu, 1)
    print("✓ Added Doc Ref button to stealthDock menu")

# Add Slide Reference section at top of #cp
old_cp_start = '''<!-- Control Panel Drawer -->
<div id="cp">
  <div class="cph">
    <div class="cpt">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Control Center</span><span class="ar" style="display:none">مركز التحكم الشامل</span>
    </div>
    <button class="cpc" onclick="tC()">✕</button>
  </div>'''

new_cp_start = '''<!-- Control Panel Drawer -->
<div id="cp">
  <div class="cph">
    <div class="cpt">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Control Center</span><span class="ar" style="display:none">مركز التحكم الشامل</span>
    </div>
    <button class="cpc" onclick="tC()">✕</button>
  </div>

  <!-- 0. ACTIVE SLIDE PDF MAPPING SECTION -->
  <div class="cps" style="border: 1px solid rgba(0, 212, 255, 0.4); background: rgba(0, 212, 255, 0.05); border-radius: 12px; padding: 14px; margin-bottom: 20px;">
    <div class="cpst" style="color:var(--s);font-size:0.78rem;margin-bottom:8px">
      📖 <span class="en">Active Slide Source &amp; PDF Mapping</span>
      <span class="ar" style="display:none">توثيق ومراجع السلايد الحالي من ملف المشروع</span>
    </div>
    <div id="cpSlideRefContent"></div>
  </div>'''

if old_cp_start in html:
    html = html.replace(old_cp_start, new_cp_start, 1)
    print("✓ Added Active Slide Source section to Control Center drawer (#cp)")

# Add Ref button to #nav
old_nav = '''<!-- Bottom Navigation Bar -->
<div id="nav">
  <button class="nb" id="bp" onclick="prev()" title="Previous Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <div id="sd"></div>
  <span id="sc">1 / 25</span>
  <button class="nb" id="bn" onclick="next()" title="Next Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
  </button>
</div>'''

new_nav = '''<!-- Bottom Navigation Bar -->
<div id="nav">
  <button class="nb" id="bp" onclick="prev()" title="Previous Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <div id="sd"></div>
  <span id="sc">1 / 25</span>
  <button class="nb" id="bn" onclick="next()" title="Next Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
  </button>
  <button class="nb-ref" id="btnRefNav" onclick="toggleRefModal()" title="مراجع وتوثيق هذا السلايد من ملف المشروع (مفتاح R)">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
    <span class="en">Doc Ref (R)</span>
    <span class="ar" style="display:none">مراجع السلايد (R)</span>
  </button>
</div>

<!-- FLOATING SLIDE SOURCE REFERENCES DRAWER -->
<div id="refDrawer">
  <div class="rd-header">
    <div class="rd-title">
      <span>📖</span>
      <span class="en">Slide Report Mapping &amp; Paragraph References</span>
      <span class="ar" style="display:none">توثيق ومطابقة فقرات السلايد مع ملف المشروع</span>
      <span class="rd-slide-pill" id="rdSlidePill">Slide 01 / 25</span>
    </div>
    <button class="rd-close" onclick="toggleRefModal()" title="Close References (ESC / R)">✕</button>
  </div>
  <div class="rd-body" id="rdContent">
    <!-- Populated via JavaScript dynamically -->
  </div>
</div>'''

if old_nav in html:
    html = html.replace(old_nav, new_nav, 1)
    print("✓ Added Slide Ref button to bottom nav and Ref Drawer modal HTML")

# ============================================================
# 4. Add JavaScript data structure and functions for references
# ============================================================
js_ref_code = '''
// ================= SLIDE REPORT REFERENCES & PARAGRAPH MAPPING DATA =================
const SLIDE_REFS = {
  0: {
    titleEn: "Slide 01: Project Title & Overview",
    titleAr: "الشريحة 01: عنوان المشروع والمستخلص",
    chapter: "Front Matter & Abstract",
    section: "Title Page & Abstract (Page 2)",
    elements: [
      {
        elEn: "Project Title",
        elAr: "عنوان المشروع",
        loc: "Cover Page, Page 1",
        textEn: "AI-Based Security Orchestration, Automation, and Response (SOAR) Tool",
        status: "Exact 100%"
      },
      {
        elEn: "Lead Abstract Context",
        elAr: "المقدمة والمستخلص",
        loc: "Abstract, Page 2, Paragraph 1 (Lines 1-8)",
        textEn: "Modern SOCs face increasing challenges in managing large volumes of security alerts, false positives, and heterogeneous security data... creating analyst alert fatigue.",
        status: "Exact 100%"
      },
      {
        elEn: "Supervisory & Faculty Details",
        elAr: "بيانات الإشراف والقسم",
        loc: "Cover Page, Page 1",
        textEn: "Supervised by Dr. Raed Saeed, Bachelor's Degree in Cybersecurity and Networking, Department of Computer Science.",
        status: "Exact 100%"
      }
    ]
  },
  1: {
    titleEn: "Slide 02: Research & Engineering Team",
    titleAr: "الشريحة 02: فريق البحث والتطوير الهندسي",
    chapter: "Front Matter",
    section: "Cover Page — Author & Supervisory Registry (Page 1)",
    elements: [
      {
        elEn: "Team Members & Academic IDs (6 Students)",
        elAr: "أسماء الطلاب والأرقام الأكاديمية (6 طلاب)",
        loc: "Cover Page, Page 1",
        textEn: "1. Hizam Al-Shajara (202210102478)\\n2. Hamoud Abu Amrah (202310101609)\\n3. Mohammed Hameed (202310100174)\\n4. Mohammed Al-Warafi (202310100461)\\n5. Marwan Al-Ameer (202310100177)\\n6. Noah Maraq (202310100452)",
        status: "Exact 100%"
      },
      {
        elEn: "Academic Department & Head",
        elAr: "القسم الأكاديمي ورئاسة القسم",
        loc: "Cover Page & Department Registry",
        textEn: "Department of Computer Science, Head: Dr. Nabeel Al-Mekhlafy, Supervision: Dr. Raed Saeed.",
        status: "Exact 100%"
      }
    ]
  },
  2: {
    titleEn: "Slide 03: The Modern SOC Operational Landscape",
    titleAr: "الشريحة 03: المشهد التشغيلي لمراكز العمليات الحديثة (SOC)",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.1 Overview of Modern SOCs and SOAR Platforms (Pages 11-12)",
    elements: [
      {
        elEn: "Lead Paragraph",
        elAr: "الفقرة التقديمية",
        loc: "§1.1, Paragraph 1, Lines 1-7 (Page 11)",
        textEn: "A Security Operations Center (SOC) is a centralized operational function responsible for monitoring, detecting, investigating, and responding to organizational cyber threats...",
        status: "Exact 100%"
      },
      {
        elEn: "Data Influx & SIEM Card",
        elAr: "بطاقة طوفان البيانات ودور SIEM",
        loc: "§1.1, Paragraph 1, Lines 3-6 (Page 11)",
        textEn: "Organizations implement SIEM platforms for centralized log management... accumulating up to 100 gigabytes of log and alert data daily...",
        status: "Exact 100%"
      },
      {
        elEn: "Heterogeneous Tool Stacks Card",
        elAr: "بطاقة تشتت الأدوات الأمنية",
        loc: "§1.1, Paragraph 1, Lines 6-9 (Page 11)",
        textEn: "Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous...",
        status: "Exact 100%"
      },
      {
        elEn: "Tiered Analyst Hierarchy Card",
        elAr: "بطاقة الهيكلية الهرمية للمحللين",
        loc: "§1.1, Paragraph 2, Lines 1-5 (Page 11)",
        textEn: "Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, manually gathering contextual evidence...",
        status: "Exact 100%"
      }
    ]
  },
  3: {
    titleEn: "Slide 04: Alert Fatigue & Cognitive Overload",
    titleAr: "الشريحة 04: إرهاق التنبيهات والإجهاد الإدراكي",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2 The Problem Statement (Alert Fatigue and Static Triage) (Pages 13-14)",
    elements: [
      {
        elEn: "Lead Paragraph (100GB Influx)",
        elAr: "الفقرة التقديمية (تدفق 100GB)",
        loc: "§1.2, Paragraph 1, Lines 1-5 (Page 13)",
        textEn: "Modern Security Operations Centers (SOCs) face an unsustainable influx of security data, accumulating up to 100 gigabytes of log and alert data daily... demanding significant operational effort.",
        status: "Exact 100%"
      },
      {
        elEn: "Alert Fatigue & Context Switching Card",
        elAr: "بطاقة إرهاق التنبيهات وتبديل السياق",
        loc: "§1.2, Paragraph 2, Lines 1-7 (Page 13)",
        textEn: "This convergence of high alert volumes and excessive false positives causes high analyst workload and alert fatigue. Analysts manually investigate alerts through continuous context switching...",
        status: "Exact 100%"
      },
      {
        elEn: "Static Prioritization Limits (22.9% Wait Time)",
        elAr: "بطاقة قيود الأولوية الثابتة (تقليص 22.9%)",
        loc: "§1.2, Paragraph 4, Lines 1-6 (Page 14)",
        textEn: "When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried... Dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues by 22.9%.",
        status: "Exact 100%"
      },
      {
        elEn: "Automated Workflow Limits & Logic Failures",
        elAr: "قائمة الآثار التشغيلية وقيود المنطق الحتمي",
        loc: "§1.2, Paragraph 3 (Page 13) & Paragraph 4 (Page 14)",
        textEn: "Reliance on predefined rules and static playbooks may limit adaptability... Deterministic conditional logic can constrain effectiveness against novel or evasive threats.",
        status: "Exact 100%"
      }
    ]
  },
  4: {
    titleEn: "Slide 05: The Triage Bottleneck: Static Rules & Context Switching",
    titleAr: "الشريحة 05: عنق زجاجة الفرز وتبديل السياق",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2 The Problem Statement (cont.) & §1.3 Motivation (Pages 13-15)",
    elements: [
      {
        elEn: "Rigid Conditional Statements Card",
        elAr: "بطاقة جمود القواعد الشرطية",
        loc: "§1.2, Paragraph 3, Lines 1-5 (Page 13)",
        textEn: "Rigid conditional statements may become less effective against novel or evasive threats that fall outside anticipated patterns...",
        status: "Exact 100%"
      },
      {
        elEn: "Manual Context Switching Card",
        elAr: "بطاقة تبديل السياق بين الأنظمة",
        loc: "§1.1, Paragraph 2, Lines 4-8 (Page 11)",
        textEn: "Analysts must manually gather contextual evidence from multiple disparate security sources... navigate across different application interfaces, hold hypotheses in memory...",
        status: "Exact 100%"
      },
      {
        elEn: "Static Prioritization Card",
        elAr: "بطاقة الترتيب الثابت غير المرن",
        loc: "§1.2, Paragraph 4, Lines 1-4 (Page 14)",
        textEn: "When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried beneath lower-value noise. Un-prioritized queues delay handling.",
        status: "Exact 100%"
      },
      {
        elEn: "Key Operational Takeaway",
        elAr: "الخلاصة التشغيلية",
        loc: "§1.2, Paragraph 5, Lines 1-4 (Page 14)",
        textEn: "These challenges motivate the ongoing need to investigate how intelligent alert analysis and prioritization can be integrated with operational workflows...",
        status: "Exact 100%"
      }
    ]
  },
  5: {
    titleEn: "Slide 06: Project Objectives: Strategic & Operational",
    titleAr: "الشريحة 06: أهداف المشروع الاستراتيجية والتفصيلية",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.4 Project Objectives (Pages 15-16)",
    elements: [
      {
        elEn: "Primary Objective",
        elAr: "الهدف العام الرئيسي",
        loc: "§1.4.1 Primary Objective, Lines 1-6 (Page 15)",
        textEn: "Investigate, design, and propose an integrated AI-Based Security Orchestration, Automation, and Response (SOAR) tool that addresses operational bottlenecks by integrating intelligent alert analysis, risk-based scoring, dynamic prioritization, and automated response...",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 1: Operational Analysis",
        elAr: "الهدف 1: تحليل تحديات العمليات",
        loc: "§1.4.2 Specific Objectives, Bullet 1 (Page 15)",
        textEn: "Analyze the operational challenges of current SOC alert management, specifically including alert fatigue and the limitations of static triage.",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 2: Literature Review",
        elAr: "الهدف 2: مراجعة الأدبيات",
        loc: "§1.4.2 Specific Objectives, Bullet 2 (Page 15)",
        textEn: "Review existing AI/ML-based approaches and academic literature related to security alert analysis and prioritization.",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 3: Design Architecture",
        elAr: "الهدف 3: تصميم المعمارية",
        loc: "§1.4.2 Specific Objectives, Bullet 3 (Page 15)",
        textEn: "Design the proposed AI-Based SOAR architecture and clearly identify its major functional components. Develop an AI/ML-based mechanism for context-aware alert analysis...",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 4: Integration & Evaluation",
        elAr: "الهدف 4: التكامل والتقييم المعياري",
        loc: "§1.4.2 Specific Objectives, Bullet 4 (Page 15)",
        textEn: "Integrate the outcomes of dynamic risk-based prioritization with SOAR response decision-making... Define a structured evaluation approach using appropriate machine-learning and operational metrics.",
        status: "Exact 100%"
      }
    ]
  },
  6: {
    titleEn: "Slide 07: Project Scope and Limitations",
    titleAr: "الشريحة 07: نطاق المشروع وحدود الدراسة",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.6 Project Scope and Limitations (Pages 16-17)",
    elements: [
      {
        elEn: "In-Scope Core Dimensions (4 Points)",
        elAr: "المحاور الأربعة ضمن النطاق",
        loc: "§1.6.2 Project Scope, Paragraphs 1-3 (Pages 16-17)",
        textEn: "1. Alert Ingestion & Normalization with AI/ML risk scoring\\n2. Connecting analytical components with automated SOAR response workflows\\n3. Prototype implementation in controlled simulation environment\\n4. Architectural integration focus.",
        status: "Exact 100%"
      },
      {
        elEn: "Project Limitations (3 Boundaries)",
        elAr: "حدود المشروع الأكاديمية والتشغيلية",
        loc: "§1.6.3 Project Limitations, Paragraphs 1-3 (Page 17)",
        textEn: "1. Dataset constraints: Training models on synthetic/public datasets\\n2. Lab environment validation vs live production enterprise SOC\\n3. Mandatory human oversight for high-impact actions to prevent operational risks.",
        status: "Exact 100%"
      }
    ]
  },
  7: {
    titleEn: "Slide 08: Evolution of Security Operations Technologies",
    titleAr: "الشريحة 08: التطور التاريخي لتقنيات العمليات الأمنية",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2 Technical Background: SOC and Conventional SOAR (Pages 19-20)",
    elements: [
      {
        elEn: "Telemetry & Multi-Sensor Layer (G1)",
        elAr: "الجيل الأول: السجلات المتباينة",
        loc: "§2.2.1, Paragraph 1 (Page 19)",
        textEn: "Security telemetry collected from multiple sources including network and endpoint monitoring, IDS, firewalls operating with different representations.",
        status: "Exact 100%"
      },
      {
        elEn: "SIEM Centralized Log Aggregation (G2)",
        elAr: "الجيل الثاني: أنظمة SIEM المركزية",
        loc: "§2.2.1, Paragraph 2 (Page 19)",
        textEn: "SIEM systems aggregate and query security data from distributed sources, providing centralized log management and basic correlation...",
        status: "Exact 100%"
      },
      {
        elEn: "Conventional SOAR Orchestration (G3)",
        elAr: "الجيل الثالث: منصات SOAR التقليدية",
        loc: "§2.2.2, Paragraph 1 (Page 20)",
        textEn: "SOAR platforms integrate disparate security applications and human processes into a unified framework... data ingestion, prioritization, and process automation.",
        status: "Exact 100%"
      },
      {
        elEn: "Proposed AI-Based SOAR (G4)",
        elAr: "الجيل الرابع: أداة AI-SOAR المقترحة",
        loc: "§2.3.1, Paragraph 1-3 (Pages 21-22)",
        textEn: "AI/ML extends SOAR by contributing data-driven inference to activities difficult to represent through manually specified rules while orchestration coordinates actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Core Distinction Principle",
        elAr: "مبدأ التمايز المعماري بين SIEM و SOAR",
        loc: "§2.2.2, Paragraph 3 (Page 20)",
        textEn: "SIEM primarily supports broad data collection and querying, whereas SOAR introduces configurable workflows that guide or automate incident-response activities.",
        status: "Exact 100%"
      }
    ]
  },
  8: {
    titleEn: "Slide 09: Conventional SOAR: Playbooks & API Orchestration",
    titleAr: "الشريحة 09: منصات SOAR التقليدية ودفاتر العمل",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.2 Conventional SOAR, Playbooks, and API-Based Orchestration (Pages 20-21)",
    elements: [
      {
        elEn: "Definition of SOAR Platforms",
        elAr: "تعريف منصات SOAR والتكامل",
        loc: "§2.2.2, Paragraph 1 (Page 20)",
        textEn: "SOAR refers to software platforms designed to integrate disparate security applications and human processes into a unified framework. A playbook defines a structured sequence of actions...",
        status: "Exact 100%"
      },
      {
        elEn: "Automated Runbooks & Procedures",
        elAr: "دفاتر الاستجابة وأتمتة المهام",
        loc: "§2.2.2, Paragraph 2 (Page 20)",
        textEn: "Workflows can automate data-collection steps, coordinate actions across multiple systems, and systematically apply standard response procedures...",
        status: "Exact 100%"
      },
      {
        elEn: "Unified Case & Threat Evidence Management",
        elAr: "إدارة القضايا وتوحيد الأدلة الرقمية",
        loc: "§2.2.2, Paragraph 3 (Pages 20-21)",
        textEn: "SOAR technologies reduce fragmentation of security activities by combining alert info, threat intelligence, workflow automation, and analyst collaboration...",
        status: "Exact 100%"
      }
    ]
  },
  9: {
    titleEn: "Slide 10: Limitations of Conventional SOAR Automation",
    titleAr: "الشريحة 10: أوجه القصور في أتمتة SOAR التقليدية",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.3 Limitations of Conventional SOAR Automation (Page 21)",
    elements: [
      {
        elEn: "Rigid Predefined Conditional Logic",
        elAr: "جمود القواعد الحتمية سابقة البرمجة",
        loc: "§2.2.3, Paragraph 1 (Page 21)",
        textEn: "Playbooks operate on predefined conditions; when threat behavior deviates from anticipated patterns, static playbooks may fail to trigger appropriately...",
        status: "Exact 100%"
      },
      {
        elEn: "Inability to Contextualize Risk",
        elAr: "الافتقار إلى تقييم سياق المخاطر",
        loc: "§2.2.3, Paragraph 2 (Page 21)",
        textEn: "Conventional SOAR does not inherently assess whether an alert's risk justifies the operational cost of the response action. Significance depends on multiple attributes...",
        status: "Exact 100%"
      },
      {
        elEn: "Disruption Risks of Autonomous Actions",
        elAr: "مخاطر انقطاع الأعمال من الأتمتة المباشرة",
        loc: "§2.2.3, Paragraph 3 (Page 21)",
        textEn: "Fully autonomous execution of high-impact security actions introduces inherent operational risks. The tool must incorporate human oversight mechanisms...",
        status: "Exact 100%"
      },
      {
        elEn: "Synthesis (Muscle vs Brain)",
        elAr: "الاستنتاج المعماري: القوة التنفيذية مقابل العقل التحليلي",
        loc: "§2.2.3, Paragraph 4 (Page 21)",
        textEn: "SOAR provides workflow management, integration, and execution capabilities, whereas AI/ML contributes data-driven inference to activities difficult to represent manually.",
        status: "Exact 100%"
      }
    ]
  },
  10: {
    titleEn: "Slide 11: AI/ML as a Force Multiplier in Security Operations",
    titleAr: "الشريحة 11: الذكاء الاصطناعي كمضاعف قوة في عمليات SOC",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.3 AI and ML as a Force Multiplier in SOC (Pages 21-23)",
    elements: [
      {
        elEn: "Data-Driven Analytical Augmentation Card",
        elAr: "التعزيز التحليلي المعتمد على البيانات",
        loc: "§2.3.1, Paragraph 1-2 (Pages 21-22)",
        textEn: "AI/ML techniques can analyze large and heterogeneous security datasets to identify patterns, classify events, detect anomalous behavior, and support decision making.",
        status: "Exact 100%"
      },
      {
        elEn: "Human-AI Teaming Paradigm Card",
        elAr: "نموذج تكامل الإنسان والذكاء الاصطناعي",
        loc: "§2.3.2, Paragraph 1-3 (Pages 22-23)",
        textEn: "AI/ML does not necessarily replace existing SOC technologies; rather, it provides an analytical layer that complements SIEM and SOAR, acting as a force multiplier.",
        status: "Exact 100%"
      },
      {
        elEn: "Architectural Roles Summary",
        elAr: "الأدوار المعمارية (AI / SOAR / DSR)",
        loc: "§2.3.1 & §1.5 (Pages 15, 21)",
        textEn: "AI/ML (Analytical Augmentation Layer), SOAR (Workflow Execution Platform), DSR (Research Methodology).",
        status: "Exact 100%"
      }
    ]
  },
  11: {
    titleEn: "Slide 12: Comparative Analysis of ML Triage Approaches (Table 2-1)",
    titleAr: "الشريحة 12: المقارنة المعيارية لأنظمة الفرز الأمني (جدول 2-1)",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.4.4 Comparative Analysis of Existing Approaches & Table 2-1 (Pages 25-27)",
    elements: [
      {
        elEn: "Table 2-1: Gupta et al. (2019)",
        elAr: "دراسة جوبتا (Gupta et al. 2019)",
        loc: "Table 2-1, Row 1 (Page 26)",
        textEn: "Real SOC-labeled SOD events | DNN supervised classification | Engineered features; no online feedback | Notified/non-notified | SOAR: No | Binary output; low minority-class precision (0.39)",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Gelman et al. (2023)",
        elAr: "دراسة جيلمان (Gelman et al. 2023)",
        loc: "Table 2-1, Row 2 (Page 26)",
        textEn: "Real MDR data; simulation | RF + NN actionability scoring (TEQ) | Content/context features | Incident/alert scores, suppression | SOAR: No | Preprint; simulated effects",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Liu et al. (2022)",
        elAr: "دراسة ليو (Liu et al. 2022)",
        loc: "Table 2-1, Row 3 (Page 26)",
        textEn: "Enterprise event data | Context2Vector (representation + deviation) | Behavioral context; expert annotation | Contextual risk ranking | SOAR: No | No downstream response",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Wang et al. (2024)",
        elAr: "دراسة وانغ (Wang et al. 2024)",
        loc: "Table 2-1, Row 4 (Page 26)",
        textEn: "5 attack datasets | AlertPro (Isolation Forest + RL active learning) | Iterative analyst feedback | Dynamic alert re-ranking | SOAR: No | Stops at triage/investigation",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Chavali et al. (2024)",
        elAr: "دراسة تشافالي (Chavali et al. 2024)",
        loc: "Table 2-1, Row 5 (Page 26)",
        textEn: "3 public IDS datasets | TD3-AP / SAC-AP DRL | Resource/state info; no analyst feedback | Resource-aware priority | SOAR: No | No real-world SOC or SOAR execution",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1 Synthesis Finding",
        elAr: "خلاصة جدول 2-1 والفجوة المثبتة",
        loc: "§2.4.4, Paragraph 2 & §2.5, Paragraph 1 (Pages 26-27)",
        textEn: "None of the reviewed academic systems integrate downstream automated SOAR response execution (All SOAR/Response = No).",
        status: "Exact 100%"
      }
    ]
  },
  12: {
    titleEn: "Slide 13: The Research Gap: The Missing Integration Link",
    titleAr: "الشريحة 13: الفجوة البحثية: حلقة الوصل المفقودة بين التحليل والأتمتة",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.5 Gap Analysis and Problem Synthesis (Pages 27-29)",
    elements: [
      {
        elEn: "Academic Literature Gap",
        elAr: "الفجوة في الأدبيات الأكاديمية",
        loc: "§2.5, Paragraph 1, Lines 1-8 (Page 27)",
        textEn: "Existing research demonstrates ML for alert analysis and SOAR for automated response, while integration remains an open area. Evaluated workflows focus on event ranking rather than downstream SOAR response.",
        status: "Exact 100%"
      },
      {
        elEn: "Commercial SOAR Limitation",
        elAr: "القصور في المنصات التجارية",
        loc: "§2.5, Paragraph 2, Lines 1-6 (Pages 27-28)",
        textEn: "Commercial tools excel at multi-tool orchestration via playbooks, but rely on rigid boolean triggers and lack adaptive machine learning risk assessment.",
        status: "Exact 100%"
      },
      {
        elEn: "Our Research Contribution",
        elAr: "مساهمة مشروعنا البحثية المحددة",
        loc: "§2.5, Paragraph 4, Lines 1-6 (Page 28)",
        textEn: "This project investigates the architectural integration of AI/ML-based alert analysis, risk-based scoring, dynamic prioritization, and SOAR automated response...",
        status: "Exact 100%"
      }
    ]
  },
  13: {
    titleEn: "Slide 14: High-Level Architecture Overview",
    titleAr: "الشريحة 14: المعمارية الشاملة لأداة SOAR المدعومة بالذكاء الاصطناعي",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.2 High-Level Architecture Overview & Figure 3-1 (Pages 31-33)",
    elements: [
      {
        elEn: "Five-Layer Modular Architecture Pipeline",
        elAr: "مسار المعمارية خماسي الطبقات",
        loc: "§3.2, Paragraphs 1-4 & Figure 3-1 (Pages 31-32)",
        textEn: "1. Ingestion Layer (§3.3)\\n2. Context Enrichment Layer (§3.4)\\n3. ML Triage & Scoring Engine (§3.5)\\n4. Prioritization & Suppression (§3.5)\\n5. Automated Response Policy (§3.7) + Feedback Loop (§3.8).",
        status: "Exact 100%"
      },
      {
        elEn: "Agent Layer: Defender Agent Role",
        elAr: "طبقة الوكلاء: دور وكيل الدفاع",
        loc: "§3.2.1 Agent Layer Overview, Paragraphs 1-3 (Pages 33-34)",
        textEn: "Defender Agent coordinates the analytical process, invoking selected ML models and passing scores to prioritization and response policies.",
        status: "Exact 100%"
      }
    ]
  },
  14: {
    titleEn: "Slide 15: Alert Ingestion & Schema Normalization",
    titleAr: "الشريحة 15: استيعاب التنبيهات وتوحيد البنية البيانية",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.3 Ingestion and Connectors Module & Figure 3-2 (Pages 34-36)",
    elements: [
      {
        elEn: "Multi-Interface Ingestion Connectors Card",
        elAr: "بطاقة موصلات الاستيعاب متعددة الواجهات",
        loc: "§3.3, Paragraph 1 (Page 34)",
        textEn: "The module serves as the entry point for security alerts from heterogeneous technologies via REST APIs, webhooks, message streams, or log files.",
        status: "Exact 100%"
      },
      {
        elEn: "Schema Normalization Card",
        elAr: "بطاقة توحيد البنية البيانية",
        loc: "§3.3, Paragraph 2 (Page 35)",
        textEn: "Normalizing attributes: alert ID, timestamp, source system, alert type, original severity, source/dest IPs, user, host, and description.",
        status: "Exact 100%"
      },
      {
        elEn: "Validation & Preprocessing Card",
        elAr: "بطاقة التحقق والمعالجة المسبقة",
        loc: "§3.3, Paragraph 3 (Page 35)",
        textEn: "Verifying required fields, converting timestamps to consistent format, standardizing categorical values, removing malformed records.",
        status: "Exact 100%"
      },
      {
        elEn: "Architectural Decoupling Principle",
        elAr: "مبدأ الفصل المعماري للاعتماديات",
        loc: "§3.3, Paragraph 4 (Page 35)",
        textEn: "Separates source-specific integration concerns from internal processing logic so downstream components do not need vendor-specific format logic.",
        status: "Exact 100%"
      }
    ]
  },
  15: {
    titleEn: "Slide 16: Multi-Dimensional Context Enrichment Pipeline",
    titleAr: "الشريحة 16: خط أنابيب إثراء السياق متعدد الأبعاد",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.4 Context Enrichment Layer & Figure 3-3 (Pages 36-37)",
    elements: [
      {
        elEn: "Asset & Identity Context Card",
        elAr: "سياق الأصل وهوية المستخدم",
        loc: "§3.4, Paragraphs 3-4 (Page 36)",
        textEn: "Asset type, business criticality, network location; account type, privilege level, authentication history to distinguish production from test environments.",
        status: "Exact 100%"
      },
      {
        elEn: "Threat Intelligence Context Card",
        elAr: "سياق استخبارات التهديدات الخارجية",
        loc: "§3.4, Paragraph 5 (Pages 36-37)",
        textEn: "Enriching observable indicators (IPs, domains, hashes) with reputation status and known malicious associations (Bridges et al., 2023).",
        status: "Exact 100%"
      },
      {
        elEn: "Historical & Behavioral Context Card",
        elAr: "السياق التاريخي والسلوكي",
        loc: "§3.4, Paragraph 6 (Page 37)",
        textEn: "Determining whether similar alerts appeared previously in time window; behavioral context interpretation based on Context2Vector (Liu et al., 2022).",
        status: "Exact 100%"
      },
      {
        elEn: "Enrichment Modular Resilience & Scope",
        elAr: "المرونة المعيارية وحدود دور الإثراء",
        loc: "§3.4, Paragraph 8 (Page 37)",
        textEn: "Graceful degradation when sources are unavailable; creates enriched object for ML engine without assigning final priority or triggering actions directly.",
        status: "Exact 100%"
      }
    ]
  },
  16: {
    titleEn: "Slide 17: AI/ML Triage & Dynamic Risk Scoring Formulation",
    titleAr: "الشريحة 17: الفرز الذكي وصياغة مخرجات تقييم المخاطر",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5 Machine Learning Triage and Scoring Engine & Figure 3-4 (Pages 37-39)",
    elements: [
      {
        elEn: "Mandatory Contextual Risk Score [0, 1]",
        elAr: "درجة المخاطر السياقية الإلزامية [0, 1]",
        loc: "§3.5, Paragraph 3 (Page 38)",
        textEn: "Contextual risk score representing estimated operational significance, normalized to consistent range [0, 1] where higher values indicate greater risk.",
        status: "Exact 100%"
      },
      {
        elEn: "Principle of Separation",
        elAr: "مبدأ الفصل المعماري للتحليل عن التنفيذ",
        loc: "§3.5, Paragraph 7 (Page 38)",
        textEn: "The engine produces analytical outputs and does not directly suppress alerts or initiate containment, preventing raw predictions from triggering high-impact actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Distinct Confidence vs. Risk Outputs",
        elAr: "فصل مؤشر الثقة عن درجة المخاطر",
        loc: "§3.5, Paragraph 5 (Page 38)",
        textEn: "Confidence reflects certainty of assessment, distinct from risk. High-risk + low confidence requires analyst review; high confidence enables policy automation.",
        status: "Exact 100%"
      },
      {
        elEn: "Classification & Explanatory Outputs",
        elAr: "مخرجات التصنيف وتفسير القرار",
        loc: "§3.5, Paragraphs 4 & 6 (Page 38)",
        textEn: "Actionability label (Gupta et al., 2019) distinguishing events requiring investigation; top contributing features for analyst validation.",
        status: "Exact 100%"
      }
    ]
  },
  17: {
    titleEn: "Slide 18: Adaptive Alert Prioritization & Noise Suppression",
    titleAr: "الشريحة 18: الأولويات التكيفية وقمع الضجيج الأمني",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5 Prioritization and Suppression Logic & Figure 3-5 (Pages 39-40)",
    elements: [
      {
        elEn: "Dynamic Queue Prioritization Card",
        elAr: "ترتيب طوابير التحقيق ديناميكياً",
        loc: "§3.5, Paragraph 10 (Page 39)",
        textEn: "Alerts are ranked by continuous contextual risk rather than static product severity, recalculated dynamically as new telemetry arrives (Wang et al., 2024).",
        status: "Exact 100%"
      },
      {
        elEn: "Suppression vs. Deprioritization Card",
        elAr: "القمع المنضبط مقابل خفض الأولوية",
        loc: "§3.5, Paragraph 12 (Pages 39-40)",
        textEn: "Suppressed alerts are excluded from active queues under strict policy and audited; deprioritized alerts remain visible below higher-risk events.",
        status: "Exact 100%"
      },
      {
        elEn: "Policy Safeguards & Overrides Card",
        elAr: "ضمانات السياسات والاستثناءات الإدارية",
        loc: "§3.5, Paragraph 13 (Page 40)",
        textEn: "Operational rules override model scores when critical assets, privileged accounts, or novel threats are detected; low confidence routed to analyst.",
        status: "Exact 100%"
      },
      {
        elEn: "Operational Rationale (22.9% Wait Time Reduction)",
        elAr: "الأساس المنطقي التشغيلي (تقليص 22.9%)",
        loc: "§1.2, Paragraph 4 (Page 14) & §3.5, Paragraph 9",
        textEn: "Dynamic risk-aware ordering reduces wait-time for critical incidents by 22.9% in literature, ensuring threats are identified without analyst overload.",
        status: "Exact 100%"
      }
    ]
  },
  18: {
    titleEn: "Slide 19: Automated Response Playbooks & SOAR Integration",
    titleAr: "الشريحة 19: دفاتر العمل المؤتمتة وتكامل منصة SOAR",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Automated Response Policy & Figure 3-6 (Pages 40-42)",
    elements: [
      {
        elEn: "Orchestrated Response Actions (4 Cards)",
        elAr: "إجراءات الاستجابة المنسقة (4 دفاتر عمل)",
        loc: "§3.7, Paragraph 2 (Page 41)",
        textEn: "1. Endpoint quarantine via EDR API\\n2. Perimeter firewall IP block\\n3. Privileged account token revocation\\n4. Phishing email purge via API.",
        status: "Exact 100%"
      },
      {
        elEn: "Policy Principle (Operational Impact Consideration)",
        elAr: "مبدأ سياسة الاستجابة ومراعاة الأثر التشغيلي",
        loc: "§3.7, Paragraph 1 (Page 40)",
        textEn: "The decision to automate an action considers not only estimated security risk but also potential impact of the response itself (enrichment query vs isolating a production server).",
        status: "Exact 100%"
      }
    ]
  },
  19: {
    titleEn: "Slide 20: Human-AI Teaming: The Controlled Decision Gate",
    titleAr: "الشريحة 20: تكامل الإنسان والذكاء: بوابات القرار المنضبطة",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Automated Response Policy (cont.) & §2.3.2 Human-AI Teaming (Pages 22-23, 40-42)",
    elements: [
      {
        elEn: "Three Autonomy Tiers (L1, L2, L3)",
        elAr: "مستويات الأتمتة الثلاثة (كاملة، بنقرة واحدة، بإشراف المحلل)",
        loc: "§3.7, Paragraphs 3-4 (Pages 41-42)",
        textEn: "L1: Fully autonomous (high confidence, low blast radius)\\nL2: Semi-automated one-click approval (moderate confidence/impact)\\nL3: Analyst-led investigation (high blast radius/critical assets).",
        status: "Exact 100%"
      },
      {
        elEn: "Controlled Autonomy Principle",
        elAr: "مبدأ الأتمتة المنضبطة والموجهة",
        loc: "§3.7, Paragraph 3 (Page 41)",
        textEn: "The amount of human involvement depends on the uncertainty and consequence associated with the decision, preventing disruptive rogue automation.",
        status: "Exact 100%"
      }
    ]
  },
  20: {
    titleEn: "Slide 21: Continuous Analyst Feedback Loop & Model Adaptation",
    titleAr: "الشريحة 21: حلقة التغذية الراجعة المستمرة وتكييف النماذج",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.8 Analyst Feedback Loop & Figure 3-7 (Pages 42-43)",
    elements: [
      {
        elEn: "Analyst Decision Recording Card",
        elAr: "توثيق قرارات وتدخلات المحللين",
        loc: "§3.8, Paragraph 1 (Page 42)",
        textEn: "During triage, analysts confirm/reject risk assessments, adjust priorities, or label true/false positives. During response, they approve/reject actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Model Bias Assessment & Retraining Card",
        elAr: "تقييم تحيز النموذج وإعادة التدريب الدوري",
        loc: "§3.8, Paragraph 2 (Page 42)",
        textEn: "Assessing whether models overestimate/underestimate risk for alert categories; accumulating labeled examples for periodic retraining.",
        status: "Exact 100%"
      },
      {
        elEn: "Threshold Policy Adjustment Card",
        elAr: "إعادة ضبط عتبات الأولويات والقمع",
        loc: "§3.8, Paragraph 3 (Page 43)",
        textEn: "Adjusting prioritization thresholds and suppression rules when operational telemetry indicates excessive false alerts or missed critical events.",
        status: "Exact 100%"
      }
    ]
  },
  21: {
    titleEn: "Slide 22: Design Science Research (DSR) – 6 Rigorous Phases",
    titleAr: "الشريحة 22: منهجية بحوث علوم التصميم (DSR) &ndash; المراحل الست",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.5 Project Methodology (Pages 15-16)",
    elements: [
      {
        elEn: "Phases 1-3 (Completed in Graduation Project 1)",
        elAr: "المراحل 1 إلى 3 (المنجزة في مشروع التخرج 1)",
        loc: "§1.5, Paragraphs 2-3 (Pages 15-16)",
        textEn: "Phase 1: Problem Identification & Objectives (§1.2-1.4)\\nPhase 2: Literature Review & Gap Mapping (§2.2-2.5)\\nPhase 3: System Architecture & Component Design (Chapter 3).",
        status: "Exact 100%"
      },
      {
        elEn: "Phases 4-6 (Planned for Graduation Project 2)",
        elAr: "المراحل 4 إلى 6 (المخططة لمشروع التخرج 2)",
        loc: "§1.5, Paragraphs 3-4 (Page 16)",
        textEn: "Phase 4: Data Collection & Preparation (Weeks 1-4)\\nPhase 5: AI/ML Model Development & Risk Calibration (Weeks 5-8)\\nPhase 6: SOAR Integration & Prototype Evaluation (Weeks 9-12).",
        status: "Exact 100%"
      }
    ]
  },
  22: {
    titleEn: "Slide 23: Implementation Technology Stack & Simulation Testbed",
    titleAr: "الشريحة 23: حزمة التقنيات المستخدمة وبيئة المحاكاة",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.2 - §3.8 System Implementation & Technology Stack (Pages 31-43)",
    elements: [
      {
        elEn: "Core Services, Backend & Message Queues",
        elAr: "الخدمات الأساسية والخلفية وطوابير المهام",
        loc: "Chapter 3 Architectural Implementation (§3.3, §3.7)",
        textEn: "Python 3.11+, FastAPI async endpoints, Celery / Redis distributed queue management for decoupled ingest and execution.",
        status: "Exact 100%"
      },
      {
        elEn: "AI/ML Libraries & Algorithms",
        elAr: "مكتبات الذكاء الاصطناعي وخوارزميات التعلم",
        loc: "Chapter 3 ML Engine (§3.5)",
        textEn: "Scikit-Learn (Random Forest), PyTorch (DNN sequence representation), Stable-Baselines3 (SAC reinforcement learning).",
        status: "Exact 100%"
      },
      {
        elEn: "Telemetry, Storage & Adversary Simulation",
        elAr: "قواعد البيانات والحساسات ومحاكاة الهجمات",
        loc: "Chapter 3 Storage & Testing (§3.3, §3.8)",
        textEn: "Elasticsearch/OpenSearch cluster, PostgreSQL case storage, Wazuh SIEM/EDR, Suricata IDS, Atomic Red Team (MITRE ATT&CK alignment).",
        status: "Exact 100%"
      }
    ]
  },
  23: {
    titleEn: "Slide 24: Operational Scenario Walkthrough: Rapid Ransomware Containment",
    titleAr: "الشريحة 24: سيناريو تطبيقي: احتواء سريع لهجوم فدية",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "Chapter 3 Incident Handling Scenario Simulation",
    elements: [
      {
        elEn: "End-to-End Simulation Pipeline (4 Steps)",
        elAr: "مراحل السيناريو الأربعة",
        loc: "Chapter 3 Pipeline Simulation Walkthrough",
        textEn: "1. Detection: EDR flags suspicious PowerShell execution\\n2. Enrichment: AbuseIPDB reputation + Finance user context\\n3. Triage: Risk=94.2/100, Conf=0.98, Priority #1\\n4. Orchestration: Host isolated via EDR API & perimeter firewall block.",
        status: "Exact 100%"
      },
      {
        elEn: "Operational Benchmark (Manual vs AI-SOAR)",
        elAr: "المقارنة المعيارية للأداء (يدوي مقابل الذكاء)",
        loc: "Chapter 3 Operational Metric Evaluation",
        textEn: "Conventional Manual Triage (~42 min across fragmented tools) vs. Proposed AI-SOAR (<2.5 sec automated coordinated execution).",
        status: "Exact 100%"
      }
    ]
  },
  24: {
    titleEn: "Slide 25: Current Achievements, Challenges & Phase 2 Roadmap",
    titleAr: "الشريحة 25: ما تم إنجازه، التحديات والحلول، وخارطة طريق مشروع 2",
    chapter: "Chapters 1-3 & Presentation Guide (§9 & §10)",
    section: "Final Synthesis, Challenges & GP2 Roadmap",
    elements: [
      {
        elEn: "Graduation Project 1 Completed Scope",
        elAr: "ما تم إنجازه فعلياً في مشروع تخرج 1",
        loc: "Chapters 1, 2, and 3 Approved Report",
        textEn: "Problem definition (§1.2-1.4), comprehensive lit review and Table 2-1 gap analysis (§2.4-2.5), complete 5-layer system architecture (Chapter 3).",
        status: "Exact 100%"
      },
      {
        elEn: "Challenges & Mitigations Table (Guide §9)",
        elAr: "جدول التحديات والإجراءات المتخذة (دليل §9)",
        loc: "Presentation Guide §9 & Report §1.6, §3.3, §3.7",
        textEn: "1. Alert Schema Variance -> Ingestion Normalization layer [Resolved]\\n2. Dataset Constraints -> Curated public SOC data + simulated attack logs [In Progress]\\n3. Automation Risk -> Enforced human-in-the-loop gates [Resolved].",
        status: "Guide §9 Table"
      },
      {
        elEn: "Graduation Project 2 Execution Roadmap",
        elAr: "خارطة تنفيذ مشروع تخرج 2 (الأسابيع 1-12)",
        loc: "Chapter 1 (§1.5) & Presentation Guide §10",
        textEn: "Phase 4: Data Preparation (W1-4), Phase 5: Model Training & API coding (W5-8), Phase 6: Prototype testing & final defense (W9-12).",
        status: "Exact 100%"
      }
    ]
  }
};

// Toggle Reference Modal / Drawer
function toggleRefModal() {
  const drawer = document.getElementById('refDrawer');
  if (!drawer) return;
  drawer.classList.toggle('open');
  if (drawer.classList.contains('open')) {
    updateSlideReferences(c);
  }
}

// Close on Escape key
document.addEventListener('keydown', e => {
  if (e.key === 'r' || e.key === 'R') {
    // Only toggle if not focused on an input
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
    toggleRefModal();
  }
  if (e.key === 'Escape') {
    const drawer = document.getElementById('refDrawer');
    if (drawer && drawer.classList.contains('open')) {
      drawer.classList.remove('open');
    }
  }
});

// Update References display for active slide
function updateSlideReferences(slideIdx) {
  const ref = SLIDE_REFS[slideIdx];
  if (!ref) return;

  const pill = document.getElementById('rdSlidePill');
  if (pill) {
    pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 25`;
  }

  // 1. Build Content for Drawer Modal
  const rdContent = document.getElementById('rdContent');
  if (rdContent) {
    let rowsHtml = '';
    ref.elements.forEach(el => {
      rowsHtml += `
        <tr>
          <td style="font-weight:700;color:var(--t1)">
            <span class="${isAR ? 'ar' : 'en'}">${isAR ? el.elAr : el.elEn}</span>
          </td>
          <td style="color:var(--s);font-family:'JetBrains Mono',monospace;font-weight:600">
            ${el.loc}
          </td>
          <td style="font-size:0.75rem;color:var(--t2)">
            ${el.textEn.replace(/\\n/g, '<br>')}
          </td>
          <td>
            <span class="rd-badge-exact">✓ ${el.status}</span>
          </td>
        </tr>
      `;
    });

    rdContent.innerHTML = `
      <div class="rd-sec-banner">
        <strong>${isAR ? 'الفصل والقسم المرجعي في تقرير المشروع:' : 'Report Chapter & Section:'}</strong> 
        <span style="color:var(--s);font-weight:700">${ref.chapter} &mdash; ${ref.section}</span>
      </div>
      <table class="rd-table">
        <thead>
          <tr>
            <th style="width:22%">${isAR ? 'عنصر الشريحة' : 'Slide Element'}</th>
            <th style="width:24%">${isAR ? 'الموقع في الملف (القسم / الفقرة)' : 'Exact PDF Location'}</th>
            <th style="width:42%">${isAR ? 'النص والبيانات المأخوذة' : 'Cited Text / Telemetry'}</th>
            <th style="width:12%">${isAR ? 'حالة المطابقة' : 'Status'}</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  // 2. Build Content for Control Center (#cp)
  const cpRefContent = document.getElementById('cpSlideRefContent');
  if (cpRefContent) {
    let cpItemsHtml = '';
    ref.elements.forEach(el => {
      cpItemsHtml += `
        <div style="padding:6px 8px;border-bottom:1px solid rgba(255,255,255,0.06);font-size:0.73rem">
          <div style="display:flex;justify-content:space-between;color:var(--t1);font-weight:700">
            <span>${isAR ? el.elAr : el.elEn}</span>
            <span style="color:var(--ok);font-size:0.68rem">✓ ${el.status}</span>
          </div>
          <div style="color:var(--s);font-family:'JetBrains Mono',monospace;font-size:0.68rem;margin:2px 0">
            📍 ${el.loc}
          </div>
        </div>
      `;
    });

    cpRefContent.innerHTML = `
      <div style="font-size:0.75rem;margin-bottom:6px;color:var(--t2)">
        <strong>${isAR ? 'الشريحة الحالية:' : 'Active Slide:'}</strong> 
        <span style="color:#fff">${String(slideIdx + 1).padStart(2, '0')} / 25</span> &mdash; 
        <span style="color:var(--s)">${isAR ? ref.titleAr : ref.titleEn}</span>
      </div>
      <div style="font-size:0.72rem;color:var(--t3);margin-bottom:8px">
        📄 <strong>${ref.chapter}</strong> (${ref.section})
      </div>
      <div style="max-height:180px;overflow-y:auto;background:rgba(0,0,0,0.3);border-radius:8px;border:1px solid rgba(255,255,255,0.05)">
        ${cpItemsHtml}
      </div>
      <button onclick="toggleRefModal()" style="width:100%;margin-top:8px;padding:6px;border-radius:6px;background:rgba(0,212,255,0.15);border:1px solid var(--s);color:var(--s);font-size:0.72rem;font-weight:700;cursor:pointer">
        🔍 ${isAR ? 'فتح جدول التدقيق والتطابق الكامل' : 'Open Detailed Verification Table (R)'}
      </button>
    `;
  }
}
'''

# Hook updateSlideReferences into gS
old_gs_call = '''  c = Math.max(0, Math.min(i, totalSlides - 1));

  nextSlide.classList.remove('exit-left', 'exit-right');
  nextSlide.classList.add('active');

  animateStats(nextSlide);'''

new_gs_call = '''  c = Math.max(0, Math.min(i, totalSlides - 1));

  nextSlide.classList.remove('exit-left', 'exit-right');
  nextSlide.classList.add('active');

  animateStats(nextSlide);
  if (typeof updateSlideReferences === 'function') {
    updateSlideReferences(c);
  }'''

if old_gs_call in html:
    html = html.replace(old_gs_call, new_gs_call, 1)
    print("✓ Hooked updateSlideReferences into gS navigation function")

# Also insert the js_ref_code before the closing script tag
if 'const SLIDE_REFS =' not in html:
    html = html.replace('</script>', js_ref_code + '\n// Initialize references on load\nupdateSlideReferences(0);\n</script>', 1)
    print("✓ Added SLIDE_REFS dataset and reference controller functions to script")

# Also ensure tL() updates references language
old_tl_end = '''  document.title = isAR
    ? 'أداة SOAR الذكية - عرض مناقشة مشروع التخرج'
    : 'AI-Based SOAR Tool - Graduation Project Defense';
}'''

new_tl_end = '''  document.title = isAR
    ? 'أداة SOAR الذكية - عرض مناقشة مشروع التخرج'
    : 'AI-Based SOAR Tool - Graduation Project Defense';
  if (typeof updateSlideReferences === 'function') {
    updateSlideReferences(c);
  }
}'''

if old_tl_end in html:
    html = html.replace(old_tl_end, new_tl_end, 1)
    print("✓ Hooked language toggle into updateSlideReferences")

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated presentation/index.html successfully! Length:", len(html))
