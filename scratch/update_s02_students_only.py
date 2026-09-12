# -*- coding: utf-8 -*-
import re

file_path = r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the S02 section in index.html
old_s02_pattern = r'(<!-- ================= S02: TEAM & ROLES ================= -->\s*<section class="slide" id="s1">.*?)(<!-- ================= S03: MODERN SOC CONTEXT ================= -->)'

new_s02 = '''<!-- ================= S02: TEAM & ACADEMIC IDS ================= -->
<section class="slide" id="s1">
  <div class="orb o1" style="opacity:0.4"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
      <span class="en">Graduation Project Team</span><span class="ar" style="display:none">فريق مشروع التخرج</span>
    </div>
    <h2 class="st en">Project Team Members &amp; Academic Identifiers</h2>
    <h2 class="st ar" style="display:none">أعضاء فريق المشروع والأرقام الأكاديمية</h2>
    <div class="gl"></div>
    <div class="tg">
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Hizam Mohammed Ali Al-Shajara</div>
        <div class="nm ar" style="display:none">حزام محمد علي الشجرة</div>
        <div class="id-badge en">Academic ID: 202210102478</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202210102478</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Hamoud Abdullah Saleh Abu Amrah</div>
        <div class="nm ar" style="display:none">حمود عبد الله صالح أبو عمرة</div>
        <div class="id-badge en">Academic ID: 202310101609</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310101609</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Mohammed Hameed Qasim Mohammed</div>
        <div class="nm ar" style="display:none">محمد حميد قاسم محمد</div>
        <div class="id-badge en">Academic ID: 202310100174</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100174</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Mohammed Taha Qasim Al-Warafi</div>
        <div class="nm ar" style="display:none">محمد طه قاسم الورافي</div>
        <div class="id-badge en">Academic ID: 202310100461</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100461</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Marwan Mohammed Saeed Al-Ameer</div>
        <div class="nm ar" style="display:none">مروان محمد سعيد الأمير</div>
        <div class="id-badge en">Academic ID: 202310100177</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100177</div>
      </div>
      <div class="tcard">
        <div class="av"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <div class="nm en">Noah Ahmed Mohammed Maraq</div>
        <div class="nm ar" style="display:none">نوح أحمد محمد مرق</div>
        <div class="id-badge en">Academic ID: 202310100452</div>
        <div class="id-badge ar" style="display:none">الرقم الأكاديمي: 202310100452</div>
      </div>
    </div>
    <div class="hl" style="margin-top:18px;text-align:center">
      <p class="en"><strong>Academic Department:</strong> Department of Computer Science &nbsp;|&nbsp; <strong>Department Head:</strong> Dr. Nabeel Al-Mekhlafy &nbsp;|&nbsp; <strong>Supervision:</strong> Dr. Raed Saeed</p>
      <p class="ar" style="display:none"><strong>القسم الأكاديمي:</strong> قسم علوم الحاسوب &nbsp;|&nbsp; <strong>رئيس القسم:</strong> د. نبيل المخلافي &nbsp;|&nbsp; <strong>المشرف العلمي:</strong> د. رائد سعيد</p>
    </div>
  </div>
  <div class="sn">02 / 25</div>
</section>

<!-- ================= S03: MODERN SOC CONTEXT ================= -->'''

new_content, count = re.subn(old_s02_pattern, new_s02, content, flags=re.DOTALL)
print(f"Substituted S02: {count} matches")

# Also update CSS for tcard slightly for better vertical alignment and spacing
old_tcard_css = """.tcard {
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 12px;
  padding: 16px 12px;
  text-align: center;
  backdrop-filter: blur(16px);
}"""

new_tcard_css = """.tcard {
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 14px;
  padding: 22px 14px;
  text-align: center;
  backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 155px;
}"""

if old_tcard_css in new_content:
    new_content = new_content.replace(old_tcard_css, new_tcard_css)
    print("Updated tcard CSS")
else:
    print("tcard CSS pattern not found exact match, checking variation")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Saved updated index.html successfully!")
