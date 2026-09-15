import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Verify where the old slides are and cut them out
# In lines:
lines = text.splitlines(keepends=True)
print(f"Original total lines: {len(lines)}")

# We know lines 0..2943 (line 1 to 2944 inclusive) contain wrap open and 20 slides and wrap close:
# Check line 2940-2944
print("Line 2941 (1-based):", repr(lines[2940])) # </section>
print("Line 2944 (1-based):", repr(lines[2943])) # </div>
print("Line 4339 (1-based):", repr(lines[4338])) # </div>
print("Line 4341 (1-based):", repr(lines[4340])) # <!-- Bottom Navigation Bar -->

# Cut:
trimmed_lines = lines[:2944] + lines[4339:]
print(f"Trimmed lines count: {len(trimmed_lines)}")

content = ''.join(trimmed_lines)

# 2. Verify slide count in content
slides_found = re.findall(r'<section\b[^>]*class=["\'][^"\']*slide[^"\']*["\']', content)
print(f"Slide sections after cut: {len(slides_found)}")

# 3. Replace all remaining / 25 in JS and HTML
# Update rdSlidePill
content = content.replace("pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 25`;",
                          "pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 20`;")

content = content.replace("<span style=\"color:#fff\">${String(slideIdx + 1).padStart(2, '0')} / 25</span> &mdash;",
                          "<span style=\"color:#fff\">${String(slideIdx + 1).padStart(2, '0')} / 20</span> &mdash;")

content = content.replace("restore the official 25 university slides and reset all changes?",
                          "restore the official 20 presentation slides and reset all changes?")
content = content.replace("Restore the official 25 university slides and reset all changes?",
                          "Restore the official 20 presentation slides and reset all changes?")
content = content.replace("استعادة جميع الشرائح الأصلية المعتمدة (25 شريحة)",
                          "استعادة جميع الشرائح الأصلية المعتمدة (20 شريحة)")

# Also check rdSlidePill in HTML:
content = content.replace('<span class="rd-slide-pill" id="rdSlidePill">Slide 01 / 25</span>',
                          '<span class="rd-slide-pill" id="rdSlidePill">Slide 01 / 20</span>')

# 4. Now let's build the complete 20 SLIDE_REFS
# We will create an accurate SLIDE_REFS dictionary for keys 0..19
new_slide_refs_js = """// ================= EXACT 1-TO-1 SLIDE REPORT REFERENCES FOR MANUAL AUDIT (ALL 20 SLIDES) =================
// Generated to ensure 100% telemetry, paragraph and page traceability for university graduation defense
const SLIDE_REFS = {
  0: {
    titleEn: "Slide 01: AI-Based SOAR Tool — Title & Graduation Defense",
    titleAr: "الشريحة 01: أداة SOAR المدعومة بالذكاء الاصطناعي — العنوان وسجل المناقشة",
    chapter: "Title Page & Authorization Registry",
    section: "Cover & Sign-off Registry (Pages 1-3)",
    elements: [
      {
        elEn: "Project Title & Acronym",
        elAr: "عنوان المشروع والاختصار الأكاديمي",
        loc: "Report Cover & Approval Page, Page 1-3",
        textEn: "AI-Based Security Orchestration, Automation, and Response (SOAR) Tool: Advanced Security Incident Handling through Intelligent Machine Learning Triage and Adaptive Incident Response Pipelines.",
        textAr: "أداة التنسيق والأتمتة والاستجابة الأمنية القائمة على الذكاء الاصطناعي لمراكز العمليات الأمنية الحديثة."
      },
      {
        elEn: "Student Researchers & Academic Supervisor",
        elAr: "فريق الباحثين والمشرف الأكاديمي",
        loc: "Report Approval Sheet, Page 3",
        textEn: "Prepared by: Mohammed Al-Yahawy, Ahed Al-Huraibi, Moataz Al-Omari, Ammar Al-Awami, Al-Zubair Al-Dhabhani. Supervised by Dr. Raed Saeed.",
        textAr: "إعداد: محمد اليحيوي، عهد الحريبي، معتز العمري، عمار العوامي، الزبير الذبحاني. إشراف: د. رائد سعيد."
      },
      {
        elEn: "Academic Institution & Scope",
        elAr: "المؤسسة الأكاديمية والاعتماد",
        loc: "Report Cover, Page 1",
        textEn: "Department of Computer Science, Faculty of Engineering & Information Technology, University of Science and Technology, Sana'a.",
        textAr: "قسم علوم الحاسوب، كلية الهندسة وتكنولوجيا المعلومات، جامعة العلوم والتكنولوجيا، صنعاء."
      }
    ]
  },
  1: {
    titleEn: "Slide 02: Background — The Modern SOC Operational Landscape",
    titleAr: "الشريحة 02: الخلفية — المشهد التشغيلي لمراكز العمليات الأمنية الحديثة",
    chapter: "Chapter 1",
    section: "§1.1-1.2 Overview of Modern SOCs & Operational Influx (Pages 11-12)",
    elements: [
      {
        elEn: "100 GB Daily Log Volume",
        elAr: "حجم السجلات اليومية (100 غيغابايت)",
        loc: "Chapter 1 · §1.2, Page 12, Line 2-4",
        textEn: "Organizations regularly collect up to 100 GB of log data per day across heterogeneous network telemetry, endpoints, and firewall appliances.",
        textAr: "تجمع المنظمات ما يصل إلى 100 غيغابايت من السجلات يومياً عبر بيئات شبكية متباينة."
      },
      {
        elEn: "Heterogeneous Multi-Vendor Architecture",
        elAr: "بنية الأدوات المتعددة الموردين",
        loc: "Chapter 1 · §1.2, Page 12",
        textEn: "SIEM engines ingest syslog, firewall logs, NetFlow, and EDR events in divergent data schemas, preventing unified analysis.",
        textAr: "تنوع صيغ السجلات القادمة من جدران الحماية والشبكات والأجهزة الطرفية دون هيكل موحد."
      },
      {
        elEn: "Tiered Analyst Hierarchy (Tier-1/2/3)",
        elAr: "الهيكل الهرمي للمحللين (المستويات 1 و2 و3)",
        loc: "Chapter 1 · §1.1-1.2, Page 11-12",
        textEn: "Tier-1 junior analysts handle initial alert inspection manually, spending valuable time on repetitive false alarms before escalating to Tier-2/3.",
        textAr: "محللو المستوى الأول يستنزفون جهودهم في الفرز اليدوي للتنبيهات المتكررة قبل التصعيد."
      }
    ]
  },
  2: {
    titleEn: "Slide 03: The Core Problem — Alert Fatigue & Static Triage",
    titleAr: "الشريحة 03: المشكلة الجوهرية — إرهاق التنبيهات والفرز الثابت",
    chapter: "Chapter 1",
    section: "§1.2 Problem Statement & Alert Fatigue (Pages 12-14)",
    elements: [
      {
        elEn: "Alert Fatigue Crisis",
        elAr: "أزمة إرهاق التنبيهات (Alert Fatigue)",
        loc: "Chapter 1 · §1.2, Page 13",
        textEn: "Security Operations Centers (SOCs) are overwhelmed by thousands of alerts daily, creating severe cognitive overload where critical threats are missed.",
        textAr: "إغراق مراكز العمليات بآلاف التنبيهات اليومية مما يتسبب في إجهاد ذهني وإغفال التهديدات الحقيقية."
      },
      {
        elEn: "High False Positive Ratio",
        elAr: "النسبة المرتفعة للإيجابيات الكاذبة",
        loc: "Chapter 1 · §1.2, Page 13",
        textEn: "A massive percentage of daily alerts are benign anomalies or routine operations, leading analysts to distrust monitoring signals.",
        textAr: "نسبة هائلة من التنبيهات عبارة عن إنذارات خاطئة تؤدي لتشتيت المحللين وإضعاف موثوقية الأنظمة."
      },
      {
        elEn: "Static Rigid Correlation Rules",
        elAr: "قواعد الارتباط الثابتة والهشة",
        loc: "Chapter 1 · §1.2, Page 13",
        textEn: "Legacy detection systems rely on rigid threshold-based rules that fail to understand behavioral context and cannot adapt to evolving attacks.",
        textAr: "الاعتماد على قواعد ثابتة عاجزة عن فهم السياق السلوكي والتكيف مع الهجمات المتطورة."
      },
      {
        elEn: "Manual Context Switching Bottleneck",
        elAr: "عنق زجاجة التبديل اليدوي بين الأدوات",
        loc: "Chapter 1 · §1.2-1.3, Page 13-14",
        textEn: "Analysts must pivot across 5 to 10 disparate consoles (SIEM, EDR, Threat Intel, Firewall) to verify a single incident, slowing MTTR.",
        textAr: "تبديل المحلل بين واجهات متعددة للتحقق من تنبيه واحد يرفع زمن الاستجابة ويزيد الأخطاء البشرية."
      }
    ]
  },
  3: {
    titleEn: "Slide 04: Motivation & Significance — Empirical Industry Benchmarks",
    titleAr: "الشريحة 04: الأهمية والدافع البحثي — مؤشرات معيارية مثبتة",
    chapter: "Chapter 1 & 2",
    section: "§1.3 Motivation & §2.4.1 Empirical Triage Benchmarks (Pages 14-15, 29-30)",
    elements: [
      {
        elEn: "22.9% Critical Alerts Handled (Gelman et al. 2023)",
        elAr: "معالجة 22.9% فقط من التنبيهات الحرجة",
        loc: "Chapter 1 · §1.2 & Chapter 2 · §2.4.1, Page 13, 29",
        textEn: "Empirical study by Gelman et al. (2023) shows human analysts only inspect ~22.9% of critical alerts during peak operational volume.",
        textAr: "دراسة جيلمان (2023) أثبتت أن المحللين يفحصون 22.9% فقط من التنبيهات أثناء ذروة العمليات."
      },
      {
        elEn: "54% FP Suppression with 95.1% True Capture",
        elAr: "قمع 54% من الإيجابيات الكاذبة مع التقاط 95.1%",
        loc: "Chapter 2 · §2.4.1, Page 29",
        textEn: "Machine learning triage demonstrates up to 54% reduction in false-positive workload while preserving a 95.1% true-positive capture rate.",
        textAr: "الفرز الذكي أثبت قدرته على قمع 54% من الإنذارات الكاذبة مع الحفاظ على 95.1% من التهديدات الفعلية."
      },
      {
        elEn: "Strategic SOC Modernization",
        elAr: "التحول الاستراتيجي في عمليات الأمن",
        loc: "Chapter 1 · §1.3, Page 14-15",
        textEn: "Transforming reactive manual SOC workflows into an intelligent, data-driven security response engine that scales with enterprise telemetry.",
        textAr: "تحويل عمليات الأمن من دفاع يدوي بطيء إلى استجابة ذكية مؤتمتة تواكب نمو التهديدات السيبرانية."
      }
    ]
  },
  4: {
    titleEn: "Slide 05: Project Objectives — Strategic & Operational Goals",
    titleAr: "الشريحة 05: أهداف المشروع — الأهداف الاستراتيجية والتشغيلية",
    chapter: "Chapter 1",
    section: "§1.4 Research Objectives (1 General + 4 Specific Goals) (Pages 15-16)",
    elements: [
      {
        elEn: "General Objective (Main Goal)",
        elAr: "الهدف العام للمشروع",
        loc: "Chapter 1 · §1.4, Page 15",
        textEn: "Develop an AI-based SOAR tool that automates alert ingestion, contextual enrichment, and intelligent triage to reduce analyst fatigue and accelerate incident response.",
        textAr: "تطوير أداة SOAR مدعومة بالذكاء الاصطناعي لأتمتة استيعاب وإثراء وفرز التنبيهات لتقليل الإجهاد وتسريع الاستجابة."
      },
      {
        elEn: "Objective 1: Ingestion & Normalization",
        elAr: "الهدف الأول: الاستيعاب وتوحيد البنية البيانية",
        loc: "Chapter 1 · §1.4, Page 15",
        textEn: "Design and implement ingestion connectors that normalize multi-vendor security telemetry into an open standardized schema.",
        textAr: "تصميم وتنفيذ موصلات استيعاب توحد سجلات الموردين المتعددين في بنية بيانات قياسية."
      },
      {
        elEn: "Objective 2: ML Triage & Dynamic Scoring",
        elAr: "الهدف الثاني: الفرز الذكي وتقييم المخاطر الديناميكي",
        loc: "Chapter 1 · §1.4, Page 15",
        textEn: "Formulate and train machine learning models to calculate dynamic risk scores and filter benign noise.",
        textAr: "بناء وتدريب نماذج تعلم آلي لحساب درجات المخاطر بدقة وتصفية الضجيج الأمني."
      },
      {
        elEn: "Objective 3: Automated Playbooks & Containment",
        elAr: "الهدف الثالث: دفاتر العمل المؤتمتة وإجراءات الاحتواء",
        loc: "Chapter 1 · §1.4, Page 15",
        textEn: "Construct adaptive response playbooks with controlled decision gates for rapid, auditable containment actions.",
        textAr: "بناء دفاتر استجابة مؤتمتة خاضعة لسياسات تحكم دقيقة لتنفيذ إجراءات الاحتواء السريع."
      },
      {
        elEn: "Objective 4: DSR Prototype Evaluation",
        elAr: "الهدف الرابع: تقييم النموذج الأولي وفق منهجية DSR",
        loc: "Chapter 1 · §1.4, Page 16",
        textEn: "Validate the prototype against benchmark cybersecurity datasets and evaluate performance using precision, recall, and MTTR metrics.",
        textAr: "التحقق من كفاءة النموذج الأولي عبر مجموعات بيانات قياسية وقياس الدقة وزمن الاستجابة."
      }
    ]
  },
  5: {
    titleEn: "Slide 06: Project Scope & Limitations — Technical Boundaries",
    titleAr: "الشريحة 06: نطاق المشروع وحدوده — المحددات الفنية والأكاديمية",
    chapter: "Chapter 1",
    section: "§1.6 Scope & Limitations of the Investigation (Pages 17-18)",
    elements: [
      {
        elEn: "In-Scope Core Capabilities",
        elAr: "القدرات الواقعة ضمن النطاق",
        loc: "Chapter 1 · §1.6, Page 17",
        textEn: "Ingestion of SIEM/network telemetry, multi-dimensional enrichment (asset, threat intel), ML-based classification, risk scoring, and rule-based playbook execution.",
        textAr: "استيعاب السجلات، إثراء السياق، التصنيف بالتعلم الآلي، حساب المخاطر، وتنفيذ دفاتر العمل."
      },
      {
        elEn: "Academic & Simulated Environment Constraints",
        elAr: "حدود البيئة الأكاديمية والمحاكاة",
        loc: "Chapter 1 · §1.6, Page 17-18",
        textEn: "Evaluated using public benchmark security datasets and simulated enterprise testbeds due to privacy and NDA restrictions on live corporate SOC data.",
        textAr: "التقييم يعتمد على بيانات معيارية وبيئات محاكاة لتعذر الوصول إلى شبكات تجارية حية لقيود الخصوصية."
      },
      {
        elEn: "Supervised & Explainable Autonomy",
        elAr: "الأتمتة الخاضعة للرقابة والتفسير",
        loc: "Chapter 1 · §1.6, Page 18",
        textEn: "High-impact response actions (host isolation, account revocation) require human-in-the-loop analyst confirmation to prevent operational disruption.",
        textAr: "الإجراءات عالية التأثير تتطلب مصادقة المحلل البشري لتفادي تعطيل الأعمال التشغيلية الحيوية."
      }
    ]
  },
  6: {
    titleEn: "Slide 07: Existing Systems — SOC Technology Evolution & SOAR Limits",
    titleAr: "الشريحة 07: الأنظمة الحالية — تطور تقنيات SOC ومحدودية SOAR التقليدي",
    chapter: "Chapter 2",
    section: "§2.1-2.3 Evolution of Security Tech & SOAR Limitations (Pages 20-25)",
    elements: [
      {
        elEn: "SIEM Platforms (G1/G2 Foundation)",
        elAr: "منصات SIEM وتجميع السجلات",
        loc: "Chapter 2 · §2.1-2.2, Page 20-22",
        textEn: "SIEM centralized logging and rule correlation, but produced overwhelming alert volumes without contextual prioritization or automated execution.",
        textAr: "قدمت SIEM المركزية لكنها أغرقت الفرق بتنبيهات تفتقر إلى السياق وقدرات التنفيذ المؤتمت."
      },
      {
        elEn: "Conventional SOAR Playbooks",
        elAr: "منصات SOAR التقليدية ودفاتر العمل",
        loc: "Chapter 2 · §2.2.2, Page 22-24",
        textEn: "Conventional SOAR systems introduced automated playbooks and API orchestration across tools, standardizing basic response workflows.",
        textAr: "أدخلت SOAR دفاتر العمل وأتمتة الواجهات لتوحيد إجراءات الاستجابة الروتينية."
      },
      {
        elEn: "Critical Limitations of Legacy SOAR",
        elAr: "أوجه القصور الحرجة في SOAR التقليدي",
        loc: "Chapter 2 · §2.2.3, Page 24-25",
        textEn: "Legacy SOAR relies on rigid boolean rules, suffers from high playbook maintenance overhead, lacks machine learning triage, and executes blindly without confidence gating.",
        textAr: "الاعتماد على قواعد شرطية هشة، صعوبة الصيانة، وانعدام الفرز الذكي مما يؤدي لقرارات خاطئة."
      }
    ]
  },
  7: {
    titleEn: "Slide 08: Comparative Analysis of Prior Work (Table 2-1)",
    titleAr: "الشريحة 08: المقارنة المعيارية للأعمال السابقة (جدول 2-1)",
    chapter: "Chapter 2",
    section: "§2.4.4 Comparative Synthesis of ML SOC Literature & Table 2-1 (Pages 31-33)",
    elements: [
      {
        elEn: "Gupta et al. (2019) — 39,427 Events, 92.67% AUC",
        elAr: "دراسة جوبتا (2019) — 39,427 حدث، AUC 92.67%",
        loc: "Chapter 2 · §2.4.1 & Table 2-1, Page 29, 32",
        textEn: "Applied Random Forest on 39,427 firewall/proxy events achieving 92.67% AUC, but lacked continuous feedback and automated playbook dispatch.",
        textAr: "نموذج الغابات العشوائية على 39,427 حدث بدقة 92.67% لكنه افتقر للتغذية الراجعة وأتمتة الاستجابة."
      },
      {
        elEn: "Liu et al. (2022) — Context2Vector (2.45M Events)",
        elAr: "دراسة ليو Context2Vector (2.45 مليون حدث)",
        loc: "Chapter 2 · §2.4.2 & Table 2-1, Page 30, 32",
        textEn: "Graph embedding on 2.45M security events improved attacker IP recall, yet focused purely on offline detection without operational SOAR containment.",
        textAr: "تضمين بياني لـ 2.45 مليون حدث لتحسين التعرف، لكنه ركز على الكشف المنفصل دون استجابة SOAR."
      },
      {
        elEn: "Wang et al. (2024) — AlertPro (96.3% Prec, 98.5% Rec)",
        elAr: "دراسة وانغ AlertPro (دقة 96.3%، استدعاء 98.5%)",
        loc: "Chapter 2 · §2.4.2 & Table 2-1, Page 30, 32",
        textEn: "Deep learning alert aggregation achieved 96.32% precision and 98.47% recall, but lacked adaptive risk formula and human policy gates.",
        textAr: "تجميع التنبيهات بالتعلم العميق بدقة استثنائية، دون معادلة مخاطر تكيفية أو بوابات تحكم بشرية."
      },
      {
        elEn: "Chavali et al. (2024) — TD3-AP (50% Improvement)",
        elAr: "دراسة تشافالي TD3-AP (تحسن بنسبة 50%)",
        loc: "Chapter 2 · §2.4.3 & Table 2-1, Page 31, 32",
        textEn: "Deep Reinforcement Learning (TD3) optimized alert prioritization by 50%, but did not address schema normalization or end-to-end containment.",
        textAr: "تعلم تعزيزي عميق حسّن ترتيب الأولويات بنسبة 50%، دون توحيد البيانات أو خط أنابيب استجابة كامل."
      },
      {
        elEn: "Our Proposed Solution: Integrated 5-Layer AI-SOAR",
        elAr: "حلنا المقترح: نظام AI-SOAR المتكامل خماسي الطبقات",
        loc: "Chapter 2 · §2.5 & Table 2-1, Page 32-34",
        textEn: "Bridges ML triage, multi-source enrichment, dynamic risk scoring, adaptive playbooks, and feedback loops into a unified, open architecture.",
        textAr: "يدمج الفرز الذكي، الإثراء الشامل، تقييم المخاطر، دفاتر العمل المؤتمتة، وحلقة التعلم في نظام موحد."
      }
    ]
  },
  8: {
    titleEn: "Slide 09: Proposed Solution — AI Augments SOAR Architecture",
    titleAr: "الشريحة 09: الحل المقترح — الذكاء الاصطناعي يعزز منصة SOAR",
    chapter: "Chapter 2 & 3",
    section: "§2.5 The Research Gap & §3.1-3.2 Proposed AI-SOAR Paradigm (Pages 33-35, 37-39)",
    elements: [
      {
        elEn: "The Research Gap Addressed",
        elAr: "الفجوة البحثية التي يعالجها المشروع",
        loc: "Chapter 2 · §2.5, Page 33-35",
        textEn: "Prior research isolated machine learning triage as an offline experimental exercise, leaving a critical disconnect with real-time SOAR playbook automation.",
        textAr: "الأبحاث السابقة فصلت نماذج التعلم الآلي عن منصات الأتمتة الحية، مما أوجد فجوة بين التنبؤ والتنفيذ."
      },
      {
        elEn: "AI as an Operational Force Multiplier",
        elAr: "الذكاء الاصطناعي كمضاعف قوة تشغيلي",
        loc: "Chapter 2 · §2.3 & Chapter 3 · §3.1, Page 25-27, 37",
        textEn: "Embedding ML directly into the decision pipeline to filter benign noise, compute probabilistic threat scores, and trigger context-aware playbooks.",
        textAr: "دمج الذكاء الاصطناعي مباشرة في مسار اتخاذ القرار لتصفية الضجيج وتفعيل دفاتر العمل بذكاء."
      },
      {
        elEn: "Human-in-the-Loop Controlled Autonomy",
        elAr: "الأتمتة المنضبطة بمشاركة المحلل البشري",
        loc: "Chapter 2 · §2.3.2 & Chapter 3 · §3.7, Page 26, 48",
        textEn: "Balancing speed and safety via policy tiers: autonomous for low-risk routine tasks, supervised confirmation for high-criticality assets.",
        textAr: "الموازنة بين السرعة والأمان عبر بوابات قرار: تنفيذ تلقائي للمهام الآمنة وتأكيد يدوي للأصول الحساسة."
      }
    ]
  },
  9: {
    titleEn: "Slide 10: System Architecture Overview — 5-Layer Pipeline",
    titleAr: "الشريحة 10: نظرة عامة على معمارية النظام — خط الأنابيب خماسي الطبقات",
    chapter: "Chapter 3",
    section: "§3.1-3.2 Proposed 5-Layer AI-SOAR System Architecture Overview (Pages 37-39)",
    elements: [
      {
        elEn: "Layer 1: Telemetry Ingestion & Normalization",
        elAr: "الطبقة 1: استيعاب وتوحيد السجلات",
        loc: "Chapter 3 · §3.2-3.3, Page 38-41",
        textEn: "Connectors pull raw logs via REST APIs, syslog, and file streams, converting them into standard ECS/CEF schema.",
        textAr: "موصلات تسحب السجلات وتحولها إلى بنية بيانات معيارية موحدة."
      },
      {
        elEn: "Layer 2: Multi-Dimensional Context Enrichment",
        elAr: "الطبقة 2: إثراء السياق متعدد الأبعاد",
        loc: "Chapter 3 · §3.2, §3.4, Page 38, 41-43",
        textEn: "Correlates alert telemetry with Asset Criticality DB, Threat Intelligence feeds (IP reputation, CVEs), and historical analyst patterns.",
        textAr: "ربط التنبيه بحساسية الأصل وقواعد بيانات استخبارات التهديدات والأنماط السابقة."
      },
      {
        elEn: "Layer 3: AI/ML Triage & Dynamic Risk Scoring",
        elAr: "الطبقة 3: محرك الفرز الذكي وتقييم المخاطر",
        loc: "Chapter 3 · §3.2, §3.5, Page 38, 43-45",
        textEn: "ML models evaluate enriched features to output incident probability P(Threat) and formulate total dynamic risk R_total.",
        textAr: "نماذج الذكاء الاصطناعي تحسب احتمالية التهديد وصياغة درجة المخاطر الإجمالية."
      },
      {
        elEn: "Layer 4: Adaptive Prioritization & Policy Routing",
        elAr: "الطبقة 4: الأولويات التكيفية وتوجيه السياسات",
        loc: "Chapter 3 · §3.2, §3.6, Page 38, 45-47",
        textEn: "Suppresses benign alerts, re-ranks urgent queues dynamically, and routes incidents based on autonomy policies.",
        textAr: "قمع التنبيهات الروتينية، إعادة ترتيب قوائم الفحص، وتوجيه الحوادث وفق سياسات الأتمتة."
      },
      {
        elEn: "Layer 5: Automated Response Playbooks & Feedback",
        elAr: "الطبقة 5: دفاتر الاستجابة المؤتمتة وحلقة التعلم",
        loc: "Chapter 3 · §3.2, §3.7-3.8, Page 39, 47-51",
        textEn: "Dispatches API actions (block IP, isolate host) and captures analyst verdicts for continuous active model retraining.",
        textAr: "تنفيذ أوامر الاحتواء عبر الواجهات البرمجية وتغذية قرارات المحللين للنموذج لإعادة التدريب."
      }
    ]
  },
  10: {
    titleEn: "Slide 11: Development Methodology — Design Science Research (DSR)",
    titleAr: "الشريحة 11: منهجية التطوير — علوم التصميم (DSR) بالمراحل الست",
    chapter: "Chapter 1",
    section: "§1.5 Research Methodology & Design Science Research (DSR) 6 Phases (Pages 16-17)",
    elements: [
      {
        elEn: "Phase 1: Problem Identification & Motivation",
        elAr: "المرحلة 1: تحديد المشكلة والدافع البحثي",
        loc: "Chapter 1 · §1.5, Page 16",
        textEn: "Documenting alert fatigue, static triage bottlenecks, and empirical SOC operational gaps through rigorous literature review.",
        textAr: "توثيق مشكلة إرهاق التنبيهات وقصور الفرز التقليدي عبر مراجعة الأدبيات الأكاديمية."
      },
      {
        elEn: "Phase 2: Objectives of a Solution",
        elAr: "المرحلة 2: تعريف أهداف الحل",
        loc: "Chapter 1 · §1.5, Page 16",
        textEn: "Defining functional requirements for multi-source ingestion, contextual enrichment, ML classification, and automated containment.",
        textAr: "تحديد المتطلبات الوظيفية للاستيعاب، الإثراء، التصنيف الذكي، والأتمتة."
      },
      {
        elEn: "Phase 3: Design & Development",
        elAr: "المرحلة 3: التصميم والتطوير (التركيز الحالي)",
        loc: "Chapter 1 · §1.5, Page 16-17",
        textEn: "Architecting the 5-layer pipeline, schema normalizers, dynamic risk formulas, and integration connectors (Chapters 2 & 3).",
        textAr: "بناء المعمارية خماسية الطبقات وصياغة معادلات تقييم المخاطر ودفاتر العمل."
      },
      {
        elEn: "Phases 4-6: Demonstration, Evaluation & Communication",
        elAr: "المراحل 4-6: التطبيق، التقييم، ونشر النتائج (مشروع 2)",
        loc: "Chapter 1 · §1.5, Page 17",
        textEn: "Prototyping alert pipeline, validating against benchmark datasets, empirical metrics evaluation, and graduation project dissertation.",
        textAr: "تشغيل خط الأنابيب، القياس على بيانات معيارية، إعداد أطروحة التخرج والمناقشة النهائية."
      }
    ]
  },
  11: {
    titleEn: "Slide 12: Analysis Progress — Ingestion Connectors & Context Enrichment",
    titleAr: "الشريحة 12: تقدم التحليل — موصلات الاستيعاب وإثراء السياق",
    chapter: "Chapter 3",
    section: "§3.3 Ingestion Pipeline & §3.4 Context Enrichment Pipeline (Pages 39-43)",
    elements: [
      {
        elEn: "Schema Normalization Pipeline",
        elAr: "مسار توحيد البنية البيانية",
        loc: "Chapter 3 · §3.3, Page 40-41",
        textEn: "Converts divergent raw alerts into standardized JSON containing timestamp, source/dest IP, port, protocol, event type, and severity tag.",
        textAr: "تحويل التنبيهات المتباينة إلى بنية JSON قياسية تضم المعرفات الشبكية والبروتوكول ونوع الحدث."
      },
      {
        elEn: "Internal Asset Context Enrichment",
        elAr: "إثراء السياق الداخلي وحساسية الأصل",
        loc: "Chapter 3 · §3.4, Page 41-42",
        textEn: "Queries Asset DB for host role, business criticality weight C_asset in [1, 5], OS version, and assigned business unit.",
        textAr: "الاستعلام عن قاعدة الأصول لتحديد حساسية الهدف ونظام التشغيل والأهمية التشغيلية."
      },
      {
        elEn: "External Threat Intelligence Enrichment",
        elAr: "إثراء استخبارات التهديدات الخارجية",
        loc: "Chapter 3 · §3.4, Page 42-43",
        textEn: "Queries reputation APIs (VirusTotal, AbuseIPDB, AlienVault OTX) to attach malicious reputation scores, CVE IDs, and threat actor tags.",
        textAr: "الاستعلام التلقائي من منصات السمعة الأمنية لإرفاق تقييم الخبث ومعرفات الثغرات."
      }
    ]
  },
  12: {
    titleEn: "Slide 13: Design Progress — AI/ML Triage & Risk Scoring Engine",
    titleAr: "الشريحة 13: تقدم التصميم — محرك الفرز الذكي ومعادلة تقييم المخاطر",
    chapter: "Chapter 3",
    section: "§3.5 Layer 3: AI/ML Triage Engine & Dynamic Risk Scoring Formulation (Pages 43-45)",
    elements: [
      {
        elEn: "Supervised ML Classification Model",
        elAr: "نموذج التصنيف بالتعلم الخاضع للإشراف",
        loc: "Chapter 3 · §3.5, Page 43-44",
        textEn: "Random Forest / Gradient Boosted ensemble evaluates normalized and enriched feature vector to compute threat probability P(Threat) in [0, 1].",
        textAr: "نماذج الغابات العشوائية وخوارزميات التعزيز لحساب احتمالية التهديد الحقيقي بين 0 و1."
      },
      {
        elEn: "Dynamic Risk Score Formulation (R_total)",
        elAr: "صياغة معادلة درجة المخاطر الإجمالية (R_total)",
        loc: "Chapter 3 · §3.5, Page 44-45",
        textEn: "R_total = alpha * P(Threat) + beta * S_base + gamma * C_asset, where alpha + beta + gamma = 1.0, dynamically balancing probability, severity, and asset impact.",
        textAr: "معادلة رياضية تدمج احتمالية الذكاء الاصطناعي مع خطورة التنبيه وحساسية الأصل بأوزان محددة."
      },
      {
        elEn: "Explainability & Feature Attributions",
        elAr: "تفسير القرارات وتحليل أهمية الخصائص",
        loc: "Chapter 3 · §3.5, Page 45",
        textEn: "Extracts SHAP/feature importance rankings so human analysts understand why the ML model scored an alert as high risk.",
        textAr: "تقديم تفسير معلل لقرارات النموذج للمحلل البشري لتعزيز الشفافية وبناء الثقة في التوصيات."
      }
    ]
  },
  13: {
    titleEn: "Slide 14: Design Progress — Adaptive Prioritization & Noise Suppression",
    titleAr: "الشريحة 14: تقدم التصميم — الأولويات التكيفية وقمع الضجيج الأمني",
    chapter: "Chapter 3",
    section: "§3.5-3.6 Layer 3/4: Adaptive Prioritization Queues & Noise Suppression (Pages 45-47)",
    elements: [
      {
        elEn: "Intelligent Noise Suppression Gate",
        elAr: "بوابة قمع الضجيج الأمني الذكي",
        loc: "Chapter 3 · §3.6, Page 45-46",
        textEn: "Alerts with P(Threat) below 0.20 and low asset impact are automatically marked as benign noise and suppressed from the active queue.",
        textAr: "التنبيهات ذات الاحتمالية الأقل من 0.20 والأصول غير الحساسة تُقمع تلقائياً دون إزعاج المحلل."
      },
      {
        elEn: "Dynamic Priority Queuing (P1-P4)",
        elAr: "قوائم الفحص ذات الأولويات الديناميكية",
        loc: "Chapter 3 · §3.6, Page 46-47",
        textEn: "Incidents are dynamically slotted into Critical (P1), High (P2), Medium (P3), and Low (P4) queues based on R_total rather than static vendor tags.",
        textAr: "إعادة ترتيب التنبيهات في 4 مستويات أولوية وفق درجة المخاطر الفعلية بدلاً من تصنيف المورد الثابت."
      },
      {
        elEn: "Alert Aggregation & Deduplication",
        elAr: "تجميع التنبيهات وإلغاء التكرار",
        loc: "Chapter 3 · §3.6, Page 47",
        textEn: "Correlates identical attack patterns within sliding time windows into a single incident dossier to prevent duplicate triage.",
        textAr: "دمج التنبيهات المتطابقة زمنياً في ملف حادثة موحد لمنع التكرار وازدواجية الفحص."
      }
    ]
  },
  14: {
    titleEn: "Slide 15: Design Progress — Response Policy & Automated Playbooks",
    titleAr: "الشريحة 15: تقدم التصميم — سياسة الاستجابة ودفاتر العمل المؤتمتة",
    chapter: "Chapter 3",
    section: "§3.7 Layer 4: Automated Response Playbooks & SOAR API Orchestration (Pages 47-49)",
    elements: [
      {
        elEn: "Automated Incident Containment Playbooks",
        elAr: "دفاتر عمل احتواء الحوادث المؤتمتة",
        loc: "Chapter 3 · §3.7, Page 47-48",
        textEn: "Modular playbooks execute containment actions: dynamic firewall IP blocking, endpoint host isolation, credential revocation, and email quarantine.",
        textAr: "دفاتر عمل مرنة لتنفيذ إجراءات الاحتواء: حظر العناوين، عزل الأجهزة، وإلغاء صلاحيات الحسابات."
      },
      {
        elEn: "Controlled Autonomy Policy States",
        elAr: "حالات سياسة التحكم الثلاث (المستقل، شبه المستقل، اليدوي)",
        loc: "Chapter 2 · §2.3.2 & Chapter 3 · §3.7, Page 26, 48-49",
        textEn: "Autonomous Execution for low-risk confirmed threats; Semi-Autonomous (Analyst Approval Gate) for production servers; Manual Review for edge cases.",
        textAr: "تنفيذ مستقل للتهديدات الروتينية المؤكدة، مصادقة المحلل للأصول الحساسة، ومراجعة يدوية للحالات المعقدة."
      },
      {
        elEn: "Audit Logging & Rollback Safety",
        elAr: "سجل التدقيق والتراجع الآمن عن الإجراءات",
        loc: "Chapter 3 · §3.7, Page 49",
        textEn: "Every playbook step logs timestamped API requests, parameter payloads, and response codes, providing full traceability and one-click rollback.",
        textAr: "توثيق كل خطوة استجابة بسجل تدقيق كامل مع توفير إمكانية التراجع الفوري لتفادي الأضرار العرضية."
      }
    ]
  },
  15: {
    titleEn: "Slide 16: Implementation Progress — Architecture Stack & Technologies",
    titleAr: "الشريحة 16: تقدم التنفيذ — بيئة التطوير والتقنيات المستخدمة",
    chapter: "Chapter 3",
    section: "§3.2-3.3, §1.6 Prototype Simulation Stack & Technical Specifications (Pages 17-18, 38-41)",
    elements: [
      {
        elEn: "Core Backend & API Framework",
        elAr: "الواجهة الخلفية والبنية البرمجية",
        loc: "Chapter 3 · §3.2, §3.3, Page 38-41",
        textEn: "Built with Python 3.11, FastAPI for asynchronous high-throughput ingestion, and Pydantic for strict schema validation.",
        textAr: "تطوير الواجهة الخلفية باستخدام Python وFastAPI للاستيعاب السريع والتحقق من البيانات."
      },
      {
        elEn: "Machine Learning Pipeline Stack",
        elAr: "حزمة أدوات التعلم الآلي والبيانات",
        loc: "Chapter 3 · §3.5, Page 43-45",
        textEn: "Scikit-learn, XGBoost, and Pandas for feature preprocessing, training classification models, and calculating risk weights.",
        textAr: "استخدام مكتبات Scikit-learn وXGBoost لتدريب نماذج التصنيف واستخراج الخصائص وحساب المخاطر."
      },
      {
        elEn: "Message Queuing & Enrichment Cache",
        elAr: "طوابير الرسائل والتخزين المؤقت للإثراء",
        loc: "Chapter 3 · §3.3-3.4, Page 40-42",
        textEn: "Redis in-memory queue for decoupled ingestion buffering, rate limiting, and caching threat intelligence lookups.",
        textAr: "استخدام Redis لتنظيم تدفق التنبيهات في طوابير مؤقتة وتسريع الاستعلام عن معلومات التهديدات."
      },
      {
        elEn: "Integration Simulation Testbed",
        elAr: "بيئة المحاكاة والاختبار المعملية",
        loc: "Chapter 1 · §1.6 & Chapter 3 · §3.2, Page 17-18, 38",
        textEn: "Containerized Docker environment simulating firewall logs, SIEM forwarders, and mock security API endpoints.",
        textAr: "بيئة حاويات Docker تحاكي تدفق سجلات الجدران النارية وخدمات الاستجابة البرمجية."
      }
    ]
  },
  16: {
    titleEn: "Slide 17: Working Prototype — Alert Processing Pipeline Flow",
    titleAr: "الشريحة 17: النموذج الأولي العامل — مسار معالجة التنبيه في خط الأنابيب",
    chapter: "Chapter 3",
    section: "§3.2, §3.7 Incident Handling Lifecycle & Working Pipeline Prototype (Pages 37-39, 47-49)",
    elements: [
      {
        elEn: "Step 1 & 2: Alert Ingestion & Normalization",
        elAr: "الخطوة 1 و2: استلام التنبيه وتوحيد هيكل البيانات",
        loc: "Chapter 3 · §3.2-3.3, Page 38-40",
        textEn: "Raw multi-vendor log ingested, parsed, and mapped to standardized JSON schema with extracted IP/port entities.",
        textAr: "استلام السجل وتفكيكه وتحويله إلى بنية بيانات موحدة واستخراج الكيانات الشبكية."
      },
      {
        elEn: "Step 3: Context Enrichment Query",
        elAr: "الخطوة 3: الاستعلام وإثراء السياق التلقائي",
        loc: "Chapter 3 · §3.4, Page 41-43",
        textEn: "Asset database confirms Tier-1 database server; Threat Intel attaches malicious reputation score (AbuseIPDB 88%).",
        textAr: "تحديد الأصل كخادم قواعد بيانات حساس، وإرفاق درجة خبث العنوان الخارجي بنسبة 88%."
      },
      {
        elEn: "Step 4: AI Triage & R_total Scoring",
        elAr: "الخطوة 4: الفرز الذكي وحساب درجة المخاطر الإجمالية",
        loc: "Chapter 3 · §3.5, Page 43-45",
        textEn: "ML model classifies threat probability P(Threat) = 0.94; dynamic risk score evaluates to R_total = 0.91 (Critical P1).",
        textAr: "النموذج يصنف احتمال التهديد بـ 0.94؛ وترتفع درجة المخاطر الإجمالية إلى 0.91 (حرجة P1)."
      },
      {
        elEn: "Step 5: Policy Gating & Playbook Containment",
        elAr: "الخطوة 5: بوابات السياسة وتنفيذ دفاتر الاحتواء",
        loc: "Chapter 3 · §3.7, Page 47-49",
        textEn: "Triggers Semi-Autonomous gate; analyst approves one-click firewall IP block and host isolation in under 15 seconds.",
        textAr: "تفعيل بوابة القرار؛ مصادقة المحلل بنقرة واحدة لتطبيق حظر العنوان وعزل الجهاز خلال 15 ثانية."
      }
    ]
  },
  17: {
    titleEn: "Slide 18: Testing & Evaluation Framework — Benchmarks & Validation Metrics",
    titleAr: "الشريحة 18: إطار الاختبار والتقييم — مجموعات البيانات المعيارية ومقاييس التحقق",
    chapter: "Chapter 2 & 3",
    section: "§2.4, §3.5 Benchmark Datasets & Quantitative Evaluation Metrics (Pages 28-31, 43-45)",
    elements: [
      {
        elEn: "Benchmark Evaluation Datasets",
        elAr: "مجموعات البيانات المعيارية للاختبار",
        loc: "Chapter 2 · §2.4, Page 28-31",
        textEn: "Validation planned using established public cybersecurity datasets: CIC-IDS2017 / CSE-CIC-IDS2018 and UNSW-NB15 containing realistic attack traffic.",
        textAr: "التدريب والاختبار على مجموعات بيانات قياسية معتمدة مثل CIC-IDS2017 وUNSW-NB15."
      },
      {
        elEn: "Classification Performance Metrics",
        elAr: "مقاييس كفاءة التصنيف والفرز",
        loc: "Chapter 2 · §2.4 & Chapter 3 · §3.5, Page 31, 44",
        textEn: "Evaluated using Precision, Recall, F1-Score, and Area Under the ROC Curve (AUC-ROC) targeting false-positive suppression above 50%.",
        textAr: "قياس الدقة والاستدعاء ودرجة F1 ومساحة منحنى ROC لاستهداف قمع إيجابيات كاذبة يتجاوز 50%."
      },
      {
        elEn: "Operational SOC Efficiency Metrics",
        elAr: "مقاييس الكفاءة التشغيلية في مركز العمليات",
        loc: "Chapter 1 · §1.3 & Chapter 3 · §3.2, Page 14, 38",
        textEn: "Mean Time to Detect (MTTD), Mean Time to Respond (MTTR), and analyst alert reduction percentage to measure real-world productivity gains.",
        textAr: "قياس زمن الكشف (MTTD) وزمن الاستجابة (MTTR) ونسبة تقليص حجم التنبيهات اليدوية."
      }
    ]
  },
  18: {
    titleEn: "Slide 19: Challenges, Risks & Mitigations — Operational Controls",
    titleAr: "الشريحة 19: التحديات والمخاطر والإجراءات المتخذة — ضوابط الحماية التشغيلية",
    chapter: "Graduation Guide & Chapters 1-3",
    section: "Graduation Defense Guide §9 & Report §1.2, §2.4, §3.7, §3.8 Operational Risk Controls",
    elements: [
      {
        elEn: "Data Quality & Heterogeneity Challenge",
        elAr: "تحدي جودة البيانات وتباين الصيغ",
        loc: "Chapter 1 · §1.2 & Chapter 3 · §3.3, Page 12, 39-41",
        textEn: "Risk: Inconsistent log schemas degrade ML accuracy. Mitigation: Robust schema normalization layer with fallback default mappers and strict validation.",
        textAr: "الخطر: تباين سجلات الموردين يربك النماذج. الإجراء: طبقة توحيد بياني صارمة ومعالجة مرنة للحقول المفقودة."
      },
      {
        elEn: "Model Drift & Evolving Attack Vectors",
        elAr: "انحراف النماذج وتغير أساليب الهجمات",
        loc: "Chapter 3 · §3.8, Page 50-51",
        textEn: "Risk: Static ML models degrade as adversaries modify attack patterns. Mitigation: Continuous active feedback loop capturing analyst overrides for periodic retraining.",
        textAr: "الخطر: تراجع دقة النموذج مع ابتكار أساليب جديدة. الإجراء: حلقة تغذية راجعة تلتقط تصويبات المحلل لإعادة التدريب."
      },
      {
        elEn: "Automated Action Disruption (False Positive Containment)",
        elAr: "خطر انقطاع الخدمة بسبب إجراءات خاطئة",
        loc: "Chapter 2 · §2.3.2 & Chapter 3 · §3.7, Page 26, 48-49",
        textEn: "Risk: Automated isolation of critical production assets due to false alarms. Mitigation: Human-in-the-loop decision gates and automated instant rollback mechanisms.",
        textAr: "الخطر: عزل خوادم إنتاجية حساسة بالخطأ. الإجراء: بوابات موافقة بشرية للأصول الهامة وخاصية التراجع الفوري."
      }
    ]
  },
  19: {
    titleEn: "Slide 20: Conclusion, Remaining Work & Next Steps — Phase 2 Roadmap",
    titleAr: "الشريحة 20: الخلاصة والأعمال المتبقية والخطوات التالية — خارطة طريق المرحلة الثانية",
    chapter: "Chapters 1-3 & Guide §8",
    section: "DSR Milestones Achieved (Project 1) & Phase 2 Execution Plan (Pages 16-17, 50-51)",
    elements: [
      {
        elEn: "Current Project 1 Achievements",
        elAr: "ما تم إنجازه بنجاح في مشروع 1",
        loc: "Chapter 1-3 Summary & Guide §8",
        textEn: "Completed foundational theoretical framework (Ch. 1-2), comprehensive architectural design (Ch. 3), schema normalizers, dynamic risk formulas, and initial prototype pipeline.",
        textAr: "إنجاز الإطار النظري، التصميم المعماري الشامل، صياغة معادلات تقييم المخاطر، وبناء مسار النموذج الأولي."
      },
      {
        elEn: "Phase 2 Execution Roadmap (Project 2)",
        elAr: "خارطة طريق تنفيذ المرحلة الثانية (مشروع 2)",
        loc: "Chapter 1 · §1.5 (DSR Phases 4-5), Page 16-17",
        textEn: "Complete machine learning training on CIC-IDS datasets, build production-grade response playbooks, integrate web dashboard UI, and perform empirical benchmark evaluations.",
        textAr: "استكمال تدريب النماذج على بيانات CIC-IDS، بناء دفاتر العمل الإنتاجية، تطوير الواجهة، والتقييم التجريبي."
      },
      {
        elEn: "Deliverables & Expected Defense Outcome",
        elAr: "مخرجات المشروع والهدف النهائي",
        loc: "Chapter 1 · §1.4 & Graduation Guide §8",
        textEn: "A functional, evaluated AI-based SOAR tool ready for graduation defense that concretely solves alert fatigue and accelerates incident handling.",
        textAr: "تقديم أداة SOAR ذكية متكاملة ومختبرة تعالج إرهاق التنبيهات وتسرع الاستجابة في مراكز العمليات الأمنية."
      }
    ]
  }
};
"""

# Replace the old SLIDE_REFS block in content
# Find start of SLIDE_REFS and end of SLIDE_REFS
m_start = content.find("const SLIDE_REFS = {")
if m_start != -1:
    # Find matching closing bracket or where toggleRefModal / updateSlideReferences starts
    m_end = content.find("// Update References display for active slide", m_start)
    if m_end == -1:
        m_end = content.find("function toggleRefModal()", m_start)
    
    if m_end != -1:
        # Check if there is something before m_end that ends the object
        print(f"Replacing SLIDE_REFS from char {m_start} to {m_end}")
        content = content[:m_start] + new_slide_refs_js.strip() + "\n\n" + content[m_end:]
    else:
        print("Could not find end of SLIDE_REFS block!")
else:
    print("Could not find start of SLIDE_REFS block!")

# 5. Write the final cleaned content
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated presentation/index.html!")
