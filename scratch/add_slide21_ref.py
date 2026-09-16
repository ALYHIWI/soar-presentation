# -*- coding: utf-8 -*-
with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos19 = html.find('19: {')
end_obj = html.find('};', pos19)
if pos19 != -1 and end_obj != -1:
    key20 = """,
  20: {
    titleEn: "Slide 21: Graduation Defense & Academic Attribution — Open for Discussion",
    titleAr: "الشريحة 21: مناقشة مشروع التخرج والبيانات الأكاديمية — مستعدون لأسئلة اللجنة",
    chapter: "Graduation Defense & Academic Registry",
    section: "Supervision, Candidate Attribution & Defense Committee Discussion",
    elements: [
      {
        elEn: "Academic Supervision & Attribution",
        elAr: "الإشراف الأكاديمي والتوثيق العلمي",
        loc: "Project Defense Registry & Academic Guide",
        textEn: "Supervised by Dr. Raed Saeed. Department of Computer Science & Engineering, University of Science and Technology.",
        textAr: "إشراف الدكتور رائد سعيد. قسم علوم الحاسوب وهندسة البرمجيات والشبكات، جامعة العلوم والتكنولوجيا."
      },
      {
        elEn: "Candidate & Research Team",
        elAr: "فريق إعداد وبحث المشروع",
        loc: "Bachelor Degree Candidate Registry",
        textEn: "Mo AL-Yahawy and the Engineering Research Team. Bachelor in Cybersecurity & Networking.",
        textAr: "محمد اليحوي وفريق البحث الهندسي. بكالوريوس الأمن السيبراني والشبكات."
      },
      {
        elEn: "Defense Readiness & Live Demonstration",
        elAr: "جاهزية المناقشة والعرض التطبيقي",
        loc: "Graduation Defense Committee Q&A",
        textEn: "Fully prepared for defense committee questions, operational review, live prototype demonstration, and architectural evaluation.",
        textAr: "جاهزون بالكامل لأسئلة وملاحظات لجنة المناقشة الموقرة والمراجعة التشغيلية والعرض الحي للنموذج الأولي والتقييم المعماري."
      }
    ]
  }"""
    html = html[:end_obj] + key20 + "\n" + html[end_obj:]
    with open('presentation/index.html', 'w', encoding='utf-8') as out:
        out.write(html)
    print("Successfully added key 20 to SLIDE_REFS!")
else:
    print("Could not find pos19 or end_obj")
