# -*- coding: utf-8 -*-
"""
Script to apply all approved upgrades to presentation/index.html
"""
import re
import shutil

# Make a dated backup first
shutil.copyfile('presentation/index.html', 'presentation/index.html.backup_before_21_slides')
print("Backed up presentation/index.html to presentation/index.html.backup_before_21_slides")

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS styles: Typography, subtlePulseLoop animation, haloGlow, etc.
css_additions = """
/* === LUXURY UPGRADE & SUBTLE ANIMATIONS === */
@keyframes subtlePulseLoop {
  0%, 100% { filter: drop-shadow(0 0 5px var(--ok)); opacity: 0.92; }
  50% { filter: drop-shadow(0 0 14px var(--ok)); opacity: 1; }
}
@keyframes haloGlow {
  0%, 100% { opacity: 0.35; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 0.7; transform: translate(-50%, -50%) scale(1.1); }
}
.ill-card {
  box-shadow: 0 0 0 1px rgba(255,255,255,0.08), 0 8px 30px rgba(0,0,0,0.6);
  border-radius: 12px;
}
.sb {
  min-width: 0;
  flex: 1 1 0;
  overflow: hidden;
}
"""

if 'subtlePulseLoop' not in html:
    html = html.replace('</style>', css_additions + '\n</style>', 1)
    print("Added subtle animations and CSS tweaks.")

# 2. Update JavaScript: const N = 21, totalSlides, and SLIDE_REFS
html = html.replace('const N = 20;', 'const N = 21;')
html = html.replace("pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 20`;",
                    "pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 21`;")
html = html.replace("<span style=\"color:#fff\">${String(slideIdx + 1).padStart(2, '0')} / 20</span>",
                    "<span style=\"color:#fff\">${String(slideIdx + 1).padStart(2, '0')} / 21</span>")

# Add SLIDE_REFS entry for Slide 21 (index 20) if not present
slide21_ref = """    {
      section: "Graduation Defense Conclusion & Acknowledgments",
      pages: "Conclusion & Defense Discussion",
      elements: [
        {
          elEn: "Supervision & Academic Attribution",
          elAr: "الإشراف العلمي وبيانات المشروع الأكاديمي",
          textEn: "Supervised by Dr. Raed Saeed. Department of Computer Science & Engineering, University of Science and Technology. Graduation Project Defense.",
          textAr: "إشراف الدكتور رائد سعيد. قسم علوم الحاسوب وهندسة البرمجيات والشبكات، جامعة العلوم والتكنولوجيا. مناقشة مشروع التخرج المعتمدة."
        },
        {
          elEn: "Defense Readiness",
          elAr: "جاهزية المناقشة",
          textEn: "Open for defense committee questions, operational review, and live architectural evaluation.",
          textAr: "مستعدون لأسئلة وملاحظات لجنة المناقشة الكريمة والمراجعة التشغيلية والتقييم المعماري."
        }
      ]
    }
  ];"""

# Replace the closing of SLIDE_REFS
if 'Graduation Defense Conclusion & Acknowledgments' not in html:
    # find where SLIDE_REFS array ends
    html = re.sub(r'(\s*\}\s*\];\s*(?=\/\/\s*Update References display|\/\/\s*Render slide references))',
                  r',\n' + slide21_ref, html, count=1)
    print("Appended Slide 21 reference to SLIDE_REFS.")

# 3. Update Slide Numbers across the document
for i in range(1, 21):
    old_sn = f"{i:02d} / 20"
    new_sn = f"{i:02d} / 21"
    html = html.replace(f'<div class="sn">{old_sn}</div>', f'<div class="sn">{new_sn}</div>')

print("Updated slide numbers from / 20 to / 21.")

# Save intermediate
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved intermediate updates.")
