# -*- coding: utf-8 -*-
"""
Script to refine Slide 21 ONLY in presentation/index.html
"""
import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Refined Slide 21 HTML
refined_s20 = """<section class="slide" id="s20">
  <div class="orb o1" style="opacity:0.2;top:15%;left:10%"></div>
  <div class="orb o2" style="opacity:0.18;bottom:15%;right:10%"></div>

  <div class="content-box" style="text-align:center;max-width:1040px;margin:0 auto;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:75vh;padding:24px 20px">
    
    <!-- Top Defense Tag (Supporting Context) -->
    <div class="tag a1" style="display:inline-flex;margin-bottom:18px;border-color:rgba(0,212,255,0.3);background:rgba(0,212,255,0.06);padding:6px 14px">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <span class="en" style="color:var(--s);font-weight:700;letter-spacing:1px">GRADUATION DEFENSE &middot; CLOSING REMARKS</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:700">مناقشة مشروع التخرج &middot; الجلسة الختامية</span>
    </div>

    <!-- Exact Project Title (Supporting Context) -->
    <div style="margin-bottom:24px;max-width:860px">
      <h3 class="en" style="font-size:clamp(0.95rem, 1.35vw, 1.15rem);font-weight:600;color:var(--t2);letter-spacing:0.3px;margin:0;line-height:1.45">
        AI-Based Security Orchestration, Automation &amp; Response (SOAR) Tool
      </h3>
      <h3 class="ar" style="display:none;font-size:clamp(0.95rem, 1.35vw, 1.15rem);font-weight:600;color:var(--t2);margin:0;line-height:1.45">
        أداة أمنية ذكية للتنسيق والأتمتة والاستجابة للحوادث السيبرانية (SOAR)
      </h3>
    </div>

    <!-- Main Dominant Element: Thank You (Primary) -->
    <div style="margin-bottom:20px">
      <h1 class="en" style="font-size:clamp(2.8rem, 5.5vw, 4.2rem);font-weight:900;letter-spacing:-1px;color:#ffffff;margin:0;line-height:1.1">
        Thank You
      </h1>
      <h1 class="ar" style="display:none;font-size:clamp(2.6rem, 5vw, 4rem);font-weight:900;color:#ffffff;margin:0;line-height:1.2">
        شكراً لحسن استماعكم
      </h1>
      <div class="gl" style="margin:16px auto 0;width:90px;height:3px;background:linear-gradient(90deg, transparent, var(--s), var(--ok), transparent)"></div>
    </div>

    <!-- Questions & Discussion Prompt (Secondary) -->
    <div style="margin-bottom:28px">
      <div style="display:inline-flex;align-items:center;gap:10px;padding:8px 22px;border-radius:24px;background:rgba(255,255,255,0.04);border:1px solid rgba(0,212,255,0.25)">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        <span class="en" style="font-size:clamp(1rem, 1.3vw, 1.18rem);font-weight:700;color:#ffffff;letter-spacing:0.5px">Questions &amp; Discussion</span>
        <span class="ar" style="display:none;font-size:clamp(1rem, 1.3vw, 1.18rem);font-weight:700;color:#ffffff">الأسئلة والمناقشة</span>
      </div>
    </div>

    <!-- Appreciation Message (Appreciation for Supervisor & Committee) -->
    <div class="card" style="max-width:820px;width:100%;padding:18px 26px;border:1px solid rgba(255,255,255,0.08);background:linear-gradient(145deg, rgba(25,10,28,0.85), rgba(12,24,34,0.75));border-radius:12px;text-align:center">
      <p class="en" style="font-size:clamp(0.84rem, 1.05vw, 0.94rem);color:var(--t2);line-height:1.65;margin:0">
        With sincere appreciation to our project supervisor, <strong style="color:#ffffff">Dr. Raed Saeed</strong>, for his continuous guidance and support throughout this project, and to the honorable discussion committee for their valuable time, thoughtful evaluation, and constructive feedback.
      </p>
      <p class="ar" style="display:none;font-size:clamp(0.84rem, 1.05vw, 0.94rem);color:var(--t2);line-height:1.65;margin:0">
        مع خالص الشكر وعظيم الامتنان للمشرف الأكاديمي، <strong style="color:#ffffff">د. رائد سعيد</strong>، على دعمه وتوجيهه المتواصل طوال مسيرة هذا المشروع، ولأعضاء لجنة المناقشة الموقرة على وقتهم الثمين وتقييمهم وتوجيهاتهم القيمة البناءة.
      </p>
    </div>

  </div>
  <div class="sn">21 / 21</div>
</section>"""

# Replace section s20
pattern = re.compile(r'<section\b[^>]*id=["\']s20["\'][^>]*>.*?</section>', re.DOTALL)
if not pattern.search(html):
    raise ValueError("Section s20 not found in presentation/index.html!")

html = pattern.sub(refined_s20, html, count=1)
print("Replaced section s20 successfully.")

# Clean up SLIDE_REFS[20] as well to ensure no student names exist in drawer
slide20_clean_ref = """  20: {
    titleEn: "Slide 21: Conclusion & Questions — Defense Discussion",
    titleAr: "الشريحة 21: الختام والأسئلة — مناقشة مشروع التخرج",
    chapter: "Graduation Defense",
    section: "Supervision & Defense Committee Discussion",
    elements: [
      {
        elEn: "Academic Supervision",
        elAr: "الإشراف الأكاديمي",
        loc: "Project Defense Registry",
        textEn: "Supervised by Dr. Raed Saeed. Department of Computer Science & Engineering, University of Science and Technology.",
        textAr: "إشراف الدكتور رائد سعيد. قسم علوم الحاسوب وهندسة البرمجيات والشبكات، جامعة العلوم والتكنولوجيا."
      },
      {
        elEn: "Questions & Discussion",
        elAr: "الأسئلة والمناقشة",
        loc: "Defense Committee Evaluation",
        textEn: "Open for defense committee questions, operational review, and live architectural evaluation.",
        textAr: "جلسة الأسئلة والمناقشة والملاحظات التقييمية للجنة المناقشة الموقرة."
      }
    ]
  }"""

ref_pattern = re.compile(r'20:\s*\{.*?\n\s*\}\s*(?=\n\s*\};)', re.DOTALL)
if ref_pattern.search(html):
    html = ref_pattern.sub(slide20_clean_ref, html, count=1)
    print("Updated SLIDE_REFS[20] cleanly.")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved refined presentation/index.html successfully!")
