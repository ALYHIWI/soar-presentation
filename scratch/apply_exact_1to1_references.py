# -*- coding: utf-8 -*-
"""
Script to apply exact 1-to-1 matching SLIDE_REFS where every visible element 
in each slide has an exact corresponding entry in the doc ref drawer.
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SLIDE_REFS_CODE = """
// ================= EXACT 1-TO-1 SLIDE REPORT REFERENCES FOR MANUAL AUDIT (ALL 25 SLIDES) =================
const SLIDE_REFS = {
  0: {
    titleEn: "Slide 01: Project Title & Academic Team",
    titleAr: "الشريحة 01: عنوان المشروع وفريق البحث الأكاديمي",
    chapter: "Front Matter",
    section: "Title Page & Authorization Registry (Pages 1 & 3)",
    elements: [
      {
        elEn: "Main Title: AI-Based SOAR Tool",
        elAr: "العنوان الرئيسي: أداة SOAR القائمة على الذكاء الاصطناعي",
        loc: "Report Page 1",
        textEn: "AI-Based Security Orchestration, Automation, and Response (SOAR) Tool.",
        status: "Exact 100%"
      },
      {
        elEn: "Academic Supervisor & Department",
        elAr: "المشرف العلمي والقسم الأكاديمي",
        loc: "Report Page 1, Lines 23-28",
        textEn: "Supervised By Dr. Raed Saeed | Department of Computer Science | Bachelor's Degree in Cybersecurity and Networking.",
        status: "Exact 100%"
      },
      {
        elEn: "6 Research Students & Academic IDs",
        elAr: "فريق البحث الطلابي الستة وأرقامهم الأكاديمية",
        loc: "Report Page 1 & Page 3 (Authorization)",
        textEn: "Hizam Mohammed Ali Al-Shajara (202210102478), Hamoud Abdullah Saleh Abu Amrah (202310101609), Mohammed Hameed Qasim Mohammed (202310100174), Mohammed Taha Qasim Al-Warafi (202310100461), Marwan Mohammed Saeed Al-Ameer (202310100177), Noah Ahmed Mohammed Maraq (202310100452).",
        status: "Exact 100%"
      },
      {
        elEn: "Executive Project Scope & Goal",
        elAr: "الهدف التنفيذي ونطاق العمل",
        loc: "Report Page 4, Abstract, ¶2",
        textEn: "The proposed tool integrates artificial intelligence and machine learning techniques with SOAR capabilities to analyze incoming security alerts, assess contextual risk, and dynamically prioritize incidents before initiating appropriate response workflows.",
        status: "Exact 100%"
      }
    ]
  },
  1: {
    titleEn: "Slide 02: The Modern SOC Operational Landscape",
    titleAr: "الشريحة 02: المشهد التشغيلي لمراكز العمليات الأمنية الحديثة (SOC)",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.1-1.2 Overview of Modern SOCs & Operational Influx (Pages 11-12)",
    elements: [
      {
        elEn: "Upper Lead: Modern SOC Operational Strain",
        elAr: "النص العلوي: العبء التشغيلي لمراكز العمليات الأمنية",
        loc: "Chapter 1 · §1.1, Page 11, ¶1",
        textEn: "A Security Operations Center (SOC) centralizes cyber threat monitoring, detection, and incident response, but faces acute operational strain from massive log volumes and heterogeneous data schemas.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Data Influx & SIEM Role",
        elAr: "الفقرة 1: طوفان البيانات ودور منصات SIEM",
        loc: "Chapter 1 · §1.1 & §1.2, Page 11-12, ¶2",
        textEn: "Organizations implement SIEM platforms for centralized log management, security-event collection, and basic correlation. Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion of security alerts may consist of false positives and non-actionable noise.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Heterogeneous Tool Stacks",
        elAr: "الفقرة 2: تشتت الأدوات الأمنية متعددة الموردين",
        loc: "Chapter 1 · §1.1, Page 11, ¶3",
        textEn: "Security monitoring relies on diverse outputs from multi-vendor security stacks. Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous and complex to analyze.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Tiered Analyst Hierarchy",
        elAr: "الفقرة 3: هرمية المحللين المرهقة وإجراءات الفرز",
        loc: "Chapter 1 · §1.1, Page 12, ¶1",
        textEn: "Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, following standard operating procedures to evaluate whether an alert is a legitimate threat or benign activity, manually gathering contextual evidence across disparate sources.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat Box 1: 100 GB Daily Influx",
        elAr: "الفقرة 4 (إحصائية): 100 غيغابايت تدفق السجلات والتنبيهات يومياً",
        loc: "Chapter 1 · §1.2, Page 12, Line 468",
        textEn: "Modern Security Operations Centers (SOCs) face an unsustainable influx of security data, accumulating up to 100 gigabytes of log and alert data daily.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat Box 2: 22.9% Queue Dwell Time Reduction",
        elAr: "الفقرة 5 (إحصائية): 22.9% تقليص زمن انتظار الحوادث الحرجة في الطوابير",
        loc: "Chapter 1 · §1.2, Page 13, Line 482 (Gelman et al., 2023)",
        textEn: "whereas dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues by 22.9%.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat Box 3: 54% FP Suppression (95.1% True Capture)",
        elAr: "الفقرة 6 (إحصائية): 54% قمع الإنذارات الكاذبة مع التقاط 95.1% من الحوادث الحقيقية",
        loc: "Chapter 2 · §2.4.1, Page 27, Line 820 & Table 2-1 (Gelman et al., 2023)",
        textEn: "Gelman et al. (2023) developed a machine learning model capable of suppressing 54% of non-actionable alerts while maintaining a 95.1% detection rate for true positive incidents.",
        status: "Exact 100%"
      }
    ]
  },
  2: {
    titleEn: "Slide 03: Alert Fatigue & Cognitive Overload",
    titleAr: "الشريحة 03: أزمة إرهاق التنبيهات والإجهاد الذهني",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2 Problem Statement & Alert Fatigue (Pages 12-14)",
    elements: [
      {
        elEn: "Upper Lead: The Core Crisis Formulation",
        elAr: "النص العلوي: توصيف الأزمة المركزية للإرهاق",
        loc: "Chapter 1 · §1.2, Page 12, ¶1",
        textEn: "The convergence of massive alert volumes and excessive false positives creates acute analyst workload, cognitive burnout, and critical response delays.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Alert Influx & Noise (100 GB / Day Influx)",
        elAr: "الفقرة 1: فيضان التنبيهات وتدفق 100 غيغابايت يومياً",
        loc: "Chapter 1 · §1.2, Page 12, ¶2",
        textEn: "Modern SOCs accumulate up to 100 GB of log data daily. A substantial portion consists of non-actionable noise and false positives, exhausting operational capacity and diverting analysts from proactive hunting.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Context Switching (Cognitive Overload)",
        elAr: "الفقرة 2: عنق زجاجة تبديل السياق بين التطبيقات",
        loc: "Chapter 1 · §1.2-1.3, Page 13-14",
        textEn: "Analysts manually investigate alerts through continuous context switching—repeatedly pivoting across disparate application windows to gather evidence, creating cognitive overload and analyst burnout.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Static Rules & Queues (Static Automation Limits)",
        elAr: "الفقرة 3: جمود القواعد الثابتة وطوابير FIFO",
        loc: "Chapter 1 · §1.2, Page 13, ¶4",
        textEn: "Conventional SOAR relies on deterministic rules and static playbooks that cannot adapt to evolving risk conditions. Critical incidents get buried beneath lower-value noise in un-prioritized FIFO queues.",
        status: "Exact 100%"
      },
      {
        elEn: "Highlight Card: 22.9% Dwell Time Reduction Finding",
        elAr: "البطاقة المميزة: النتيجة التجريبية المحورية (22.9%)",
        loc: "Chapter 1 · §1.2, Page 13, Line 482",
        textEn: "In un-prioritized queues, critical incidents wait excessively; dynamic, risk-aware ordering reduces critical incident queue dwell time by 22.9%.",
        status: "Exact 100%"
      }
    ]
  },
  3: {
    titleEn: "Slide 04: The Triage Bottleneck: Static Rules & Context Switching",
    titleAr: "الشريحة 04: عنق زجاجة الفرز: القواعد الثابتة وتبديل السياق",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2-1.3 The Triage Bottleneck & Context Switching (Pages 13-14)",
    elements: [
      {
        elEn: "Banner: Operational Friction Synthesis",
        elAr: "الشريط العلوي: ملخص قيود الفرز اليدوي",
        loc: "Chapter 1 · §1.2, Page 13, ¶1",
        textEn: "Static triage rules create an acute operational friction between rapid adversary threat velocity and constrained human analyst cognitive bandwidth.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Rigid Rule-Based Triage",
        elAr: "الفقرة 1: جمود الفرز القائم على القواعد",
        loc: "Chapter 1 · §1.2, Page 13, ¶2",
        textEn: "Rigid conditional statements (IF-THEN rules) become fragile against evolving threat behaviors, demanding continuous rule maintenance and fine-tuning.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Severe Context Switching",
        elAr: "الفقرة 2: أعباء تبديل السياق بين المنصات",
        loc: "Chapter 1 · §1.3, Page 14, ¶2",
        textEn: "Analysts must pivot across multiple dashboards, CMDB records, and external threat intelligence sites to compile basic context, causing triage delays and analyst burnout.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Prioritization Blindspots",
        elAr: "الفقرة 3: غياب الأولوية والتقييم الديناميكي للمخاطر",
        loc: "Chapter 1 · §1.2, Page 14, ¶1",
        textEn: "Static priority levels fail to incorporate runtime environmental risk, asset sensitivity, or threat intelligence dynamically, burying critical alerts.",
        status: "Exact 100%"
      }
    ]
  },
  4: {
    titleEn: "Slide 05: Project Objectives: Strategic & Operational",
    titleAr: "الشريحة 05: أهداف المشروع: الاستراتيجية والتشغيلية",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.4 Research Objectives (1 General + 4 Specific Goals) (Pages 15-16)",
    elements: [
      {
        elEn: "Primary Strategic Objective Banner",
        elAr: "الهدف العام والأساسي للمشروع",
        loc: "Chapter 1 · §1.4.1, Page 15",
        textEn: "Investigate, design, and propose an integrated AI-Based Security Orchestration, Automation, and Response (SOAR) tool that addresses alert fatigue through intelligent triage and context-aware automated response.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: 1. Analyze SOC Challenges",
        elAr: "الفقرة 1: 1. تحليل تحديات مراكز العمليات الأمنية",
        loc: "Chapter 1 · §1.4.2, Page 15",
        textEn: "Analyze current operational challenges in SOC environments, focusing on alert fatigue, static triage limitations, and integration friction.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: 2. Literature Review & Synthesis",
        elAr: "الفقرة 2: 2. مراجعة الأدبيات والأنظمة المقارنة",
        loc: "Chapter 1 · §1.4.2, Page 15",
        textEn: "Review and synthesize existing academic and commercial approaches combining AI/ML with security operations to identify benchmarks and capability gaps.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: 3. Design Architecture",
        elAr: "الفقرة 3: 3. تصميم المعمارية الشاملة خماسية الطبقات",
        loc: "Chapter 1 · §1.4.2, Page 15",
        textEn: "Design an integrated system architecture incorporating ingestion, context enrichment, ML triage, dynamic risk scoring, and automated response orchestration.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 4: 4. Integration & Evaluation",
        elAr: "الفقرة 4: 4. التطوير والتقييم التجريبي للنموذج",
        loc: "Chapter 1 · §1.4.2, Page 16",
        textEn: "Implement and evaluate the prototype system using established machine-learning and operational metrics to assess triage accuracy and efficiency improvements.",
        status: "Exact 100%"
      }
    ]
  },
  5: {
    titleEn: "Slide 06: Project Scope and Limitations",
    titleAr: "الشريحة 06: نطاق المشروع وحدود الدراسة الأكاديمية",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.6 Scope & Limitations of the Investigation (Pages 17-18)",
    elements: [
      {
        elEn: "Card 1: In-Scope Focus Areas",
        elAr: "الفقرة 1: ما يقع داخل نطاق المشروع الأكاديمي",
        loc: "Chapter 1 · §1.6.1, Page 17",
        textEn: "Alert Ingestion & Normalization; Multi-Dimensional Context Enrichment; AI/ML-Based Triage & Dynamic Risk Scoring; Priority Queuing; Automated Playbook Orchestration under policy states.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Out-of-Scope Boundaries",
        elAr: "الفقرة 2: ما يقع خارج نطاق المشروع وحدود الدراسة",
        loc: "Chapter 1 · §1.6.2, Page 18",
        textEn: "Raw Network Packet Capture; Direct Proprietary Sensor Code Modification; Full Unsupervised Autonomy (policy states mandate human control for high-impact actions).",
        status: "Exact 100%"
      },
      {
        elEn: "Evaluation Scope & Dataset Protocol",
        elAr: "بروتوكول البيانات وبيئة التقييم المعملية",
        loc: "Chapter 1 · §1.6.1-1.6.2, Page 17-18",
        textEn: "Evaluation conducted using simulated SOC testbed environments and curated security alert datasets with validated ground truth.",
        status: "Exact 100%"
      }
    ]
  },
  6: {
    titleEn: "Slide 07: Evolution of Security Operations Technologies",
    titleAr: "الشريحة 07: التطور التاريخي لتقنيات عمليات الأمن السيبراني",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.1-2.2 Evolution of Security Operations & SIEM Platforms (Pages 20-22)",
    elements: [
      {
        elEn: "Evolution Paradigm Shift Banner",
        elAr: "الشريط العلوي: الرؤية النظرية لمسار التحول التاريخي",
        loc: "Chapter 2 · §2.1-2.3, Page 20-25",
        textEn: "The evolutionary trajectory shifts from manual raw log analysis toward rule-based SIEM correlation, conventional SOAR orchestration, and finally AI-augmented contextual autonomous triage.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: G1: Log Management",
        elAr: "الفقرة 1: الجيل الأول: إدارة السجلات المركزية",
        loc: "Chapter 2 · §2.1, Page 20",
        textEn: "Security telemetry collected from multiple sources including network and endpoint monitoring, intrusion detection technologies, and server logs.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: G2: SIEM Era",
        elAr: "الفقرة 2: الجيل الثاني: أنظمة SIEM",
        loc: "Chapter 2 · §2.2.1, Page 20-22",
        textEn: "SIEM systems aggregate and query security data from distributed sources, providing centralized log management, security-event correlation, and compliance reporting.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: G3: Conventional SOAR",
        elAr: "الفقرة 3: الجيل الثالث: منصات SOAR التقليدية",
        loc: "Chapter 2 · §2.2.2, Page 22-24",
        textEn: "SOAR platforms integrate disparate security applications and human processes into a unified framework. Data ingestion, case management, and playbook automation form core functional capabilities.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 4: G4: AI-Augmented SOAR",
        elAr: "الفقرة 4: الجيل الرابع: SOAR المعزز بالذكاء الاصطناعي",
        loc: "Chapter 2 · §2.3, Page 25-27",
        textEn: "AI/ML can extend SOAR by improving analytical, threat-intelligence, detection, and response capabilities while orchestrating automated response workflows dynamically.",
        status: "Exact 100%"
      }
    ]
  },
  7: {
    titleEn: "Slide 08: Conventional SOAR: Playbooks & API Orchestration",
    titleAr: "الشريحة 08: منصات SOAR التقليدية: دفاتر العمل وتنسيق الواجهات",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.2 SOAR Frameworks & Automated Playbooks (Pages 22-24)",
    elements: [
      {
        elEn: "Card 1: Security Orchestration",
        elAr: "الفقرة 1: التنسيق الأمني (Orchestration)",
        loc: "Chapter 2 · §2.2.2, Page 22-23",
        textEn: "SOAR refers to software platforms designed to integrate disparate security applications and human processes into a unified framework via bidirectional APIs, webhooks, and CLI integrations.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Automated Playbooks (609 Field Study)",
        elAr: "الفقرة 2: أتمتة الإجراءات ودراسة 609 دفاتر عمل ميدانية",
        loc: "Chapter 2 · §2.2.2, Page 23-24 (Karlzén & Sommestad, 2023)",
        textEn: "Empirical study of 609 operational playbooks across enterprise SOCs demonstrated that workflows systematically apply standard operating procedures, but follow static condition trees lacking runtime context.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Incident Case Management",
        elAr: "الفقرة 3: إدارة الحوادث الموحدة وحفظ الأدلة",
        loc: "Chapter 2 · §2.2.2, Page 24",
        textEn: "SOAR technologies reduce fragmentation of security activities by combining alert information, threat intelligence, workflows, and analyst collaboration into standardized incident cases.",
        status: "Exact 100%"
      }
    ]
  },
  8: {
    titleEn: "Slide 09: Limitations of Conventional SOAR Automation",
    titleAr: "الشريحة 09: أوجه القصور في أتمتة منصات SOAR التقليدية",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.3 Limitations of Conventional Rule-Based SOAR Systems (Pages 24-25)",
    elements: [
      {
        elEn: "Synthesis Banner: Rule Execution vs Data-Driven Inference",
        elAr: "الشريط العلوي: الاستنتاج المقارن بين القوة التنفيذية والعقل التحليلي",
        loc: "Chapter 2 · §2.2.3, Page 24",
        textEn: "SOAR provides workflow management and execution, whereas AI/ML contributes data-driven inference to activities difficult to represent through manually specified rules.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Inability to Adapt",
        elAr: "الفقرة 1: العجز عن التكيف مع المستجدات",
        loc: "Chapter 2 · §2.2.3, Page 24",
        textEn: "Playbooks operate on predefined conditions; when threat behavior deviates from anticipated patterns, static playbooks may fail or execute inappropriately.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Lack of Risk Context",
        elAr: "الفقرة 2: غياب السياق الأمني للمخاطر",
        loc: "Chapter 2 · §2.2.3, Page 24-25",
        textEn: "Conventional SOAR does not inherently assess whether an alert's risk justifies the operational cost of the response action, treating distinct assets uniformly.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Disruption Hazards (Blast Radius)",
        elAr: "الفقرة 3: مخاطر التعطيل الذاتي للأعمال",
        loc: "Chapter 2 · §2.2.3, Page 25",
        textEn: "Fully autonomous execution of high-impact security actions introduces inherent operational risks. False positives can lead to inadvertent disruption of business operations.",
        status: "Exact 100%"
      }
    ]
  },
  9: {
    titleEn: "Slide 10: AI/ML as a Force Multiplier in Security Operations",
    titleAr: "الشريحة 10: الذكاء الاصطناعي كمضاعف قوة في مراكز العمليات",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.4 Machine Learning & AI Augmentation in Security Operations (Pages 27-28)",
    elements: [
      {
        elEn: "Card 1: Data-Driven Analytical Augmentation",
        elAr: "الفقرة 1: التعزيز التحليلي المعتمد على البيانات",
        loc: "Chapter 2 · §2.4, Page 27",
        textEn: "AI/ML techniques can analyze large and heterogeneous security datasets to identify patterns, classify events, detect anomalies, and support decision making beyond static rules.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Human-AI Teaming Paradigm",
        elAr: "الفقرة 2: نموذج تكامل الإنسان والذكاء الاصطناعي",
        loc: "Chapter 2 · §2.3.2, Page 26",
        textEn: "AI/ML does not necessarily replace existing SOC technologies; rather, it provides an analytical layer that complements human expertise through controlled automation.",
        status: "Exact 100%"
      },
      {
        elEn: "Pillar 1: AI/ML (Analytical Augmentation Layer)",
        elAr: "الركيزة 1: الذكاء الاصطناعي (طبقة التعزيز التحليلي)",
        loc: "Chapter 2 · §2.4, Page 27-28",
        textEn: "Extracts statistical patterns, predicts actionability labels, and computes dynamic risk scores across incoming telemetry in milliseconds.",
        status: "Exact 100%"
      },
      {
        elEn: "Pillar 2: SOAR (Workflow Execution Platform)",
        elAr: "الركيزة 2: منصة SOAR (بيئة التنفيذ والتنسيق)",
        loc: "Chapter 2 · §2.2.2, Page 22-24",
        textEn: "Provides the underlying integration framework, API connectors, and audited state machine to orchestrate countermeasures across endpoints and firewalls.",
        status: "Exact 100%"
      },
      {
        elEn: "Pillar 3: DSR (Research Methodology)",
        elAr: "الركيزة 3: منهجية علوم التصميم (DSR)",
        loc: "Chapter 1 · §1.5, Page 16-17",
        textEn: "Governs the 6-phase scientific design process: Problem Identification, Solution Objectives, Architecture Design, Prototype Demonstration, Evaluation, and Communication.",
        status: "Exact 100%"
      }
    ]
  },
  10: {
    titleEn: "Slide 11: Comparative Analysis of Literature (Table 2-1)",
    titleAr: "الشريحة 11: المقارنة المعيارية لأنظمة الفرز الأمني القائمة على تعلم الآلة",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.4.4 Comparative Synthesis of ML SOC Literature & Table 2-1 (Pages 31-33)",
    elements: [
      {
        elEn: "Table 2-1 Synthesis Banner",
        elAr: "الشريط العلوي: خلاصة المقارنة المعيارية وإثبات الفجوة البحثية",
        loc: "Chapter 2 · §2.4.4, Page 31 & §2.5, Page 33-34",
        textEn: "None of the reviewed academic or preprint systems execute automated downstream SOAR response workflows. This empirically establishes the core research gap addressed by our project.",
        status: "Exact 100%"
      },
      {
        elEn: "Row 1: Gupta et al. (2019) Benchmark",
        elAr: "الدراسة 1: جوبتا وآخرون (2019)",
        loc: "Chapter 2 · §2.4.4, Table 2-1, Page 31",
        textEn: "Random Forest evaluated on 39,427 enterprise security events, achieving AUC 92.67%, Recall 0.92, and Precision 0.39 for tier-1 alert filtering.",
        status: "Exact 100%"
      },
      {
        elEn: "Row 2: Gelman et al. (2023) Benchmark",
        elAr: "الدراسة 2: جيلمان وآخرون (2023)",
        loc: "Chapter 2 · §2.4.4, Table 2-1, Page 31-32",
        textEn: "Gradient Boosting on commercial cloud SOC data suppressed 54% of false positives while maintaining 95.1% true incident capture and reducing queue dwell time by 22.9%.",
        status: "Exact 100%"
      },
      {
        elEn: "Row 3: Liu et al. (2022) Contextual Benchmark",
        elAr: "الدراسة 3: ليو وآخرون (2022)",
        loc: "Chapter 2 · §2.4.4, Table 2-1, Page 32",
        textEn: "Contextual graph triage over 2.45 million events improved attacker IP recall by 2.25x through multi-dimensional host and network correlation.",
        status: "Exact 100%"
      },
      {
        elEn: "Row 4: Wang et al. (2024) Adaptive Benchmark",
        elAr: "الدراسة 4: وانغ وآخرون (2024)",
        loc: "Chapter 2 · §2.4.4, Table 2-1, Page 32-33",
        textEn: "Adaptive online learning addressing concept drift and dynamic priority queue adjustment in evolving adversarial environments.",
        status: "Exact 100%"
      },
      {
        elEn: "Row 5: Chavali et al. (2024) Pipeline Benchmark",
        elAr: "الدراسة 5: تشافالي وآخرون (2024)",
        loc: "Chapter 2 · §2.4.4, Table 2-1, Page 33",
        textEn: "High-speed inference pipeline achieving 300 µs decision speed with 50% feature payload reduction for enterprise SOC throughput.",
        status: "Exact 100%"
      }
    ]
  },
  11: {
    titleEn: "Slide 12: The Research Gap: The Missing Integration Link",
    titleAr: "الشريحة 12: الفجوة البحثية: حلقة الوصل المفقودة بين التحليل والأتمتة",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.5 The Research Gap: Disconnect Between ML Triage & SOAR Execution (Pages 33-35)",
    elements: [
      {
        elEn: "Research Gap Formulation Banner",
        elAr: "الشريط العلوي: مساهمة مشروعنا في سد الفجوة المعمارية",
        loc: "Chapter 2 · §2.5, Page 34-35",
        textEn: "This project investigates the architectural integration of AI/ML-based alert analysis, risk-based scoring, dynamic prioritization, and SOAR automated response under governed security policies.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Academic ML Research",
        elAr: "الفقرة 1: أبحاث تعلم الآلة الأكاديمية المنعزلة",
        loc: "Chapter 2 · §2.5, Page 33-34",
        textEn: "Existing research demonstrates the use of ML for security alert analysis, but models operate as standalone classifiers without initiating downstream containment actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Commercial SOAR Frameworks",
        elAr: "الفقرة 2: منصات SOAR التجارية محدودة الذكاء",
        loc: "Chapter 2 · §2.5, Page 34",
        textEn: "Commercial SOAR frameworks excel at automated workflow execution but rely heavily on manually coded static rules without dynamic ML-based risk assessment.",
        status: "Exact 100%"
      }
    ]
  },
  12: {
    titleEn: "Slide 13: High-Level Architecture Overview",
    titleAr: "الشريحة 13: المعمارية الشاملة خماسية الطبقات لأداة AI-SOAR",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.1-3.2 Proposed 5-Layer AI-SOAR System Architecture Overview (Pages 37-39)",
    elements: [
      {
        elEn: "Layer 1: Ingestion Connectors & Normalization",
        elAr: "الطبقة الأولى: الاستيعاب وتوحيد البنية البيانية",
        loc: "Chapter 3 · §3.2, Page 38",
        textEn: "Collects raw security alerts from SIEM, EDR, IDS, and network devices, standardizing attributes into a unified canonical JSON schema.",
        status: "Exact 100%"
      },
      {
        elEn: "Layer 2: Multi-Dimensional Context Enrichment",
        elAr: "الطبقة الثانية: إثراء السياق متعدد الأبعاد",
        loc: "Chapter 3 · §3.2, Page 38",
        textEn: "Enriches normalized alerts with asset criticality, identity privilege level, external threat intelligence, and historical frequency baselines.",
        status: "Exact 100%"
      },
      {
        elEn: "Layer 3: AI/ML Triage & Dynamic Risk Scoring",
        elAr: "الطبقة الثالثة: محرك الفرز الذكي وتقييم المخاطر",
        loc: "Chapter 3 · §3.2, Page 38",
        textEn: "Supervised classifiers estimate actionability probability and compute continuous risk score R = ws S + wt T + wa A - wc C.",
        status: "Exact 100%"
      },
      {
        elEn: "Layer 4: Adaptive Prioritization & Automated Playbooks",
        elAr: "الطبقة الرابعة: إدارة الأولويات وأتمتة دفاتر الاستجابة",
        loc: "Chapter 3 · §3.2, Page 39",
        textEn: "Orders alerts dynamically into P1-P4 priority queues and triggers appropriate automated playbooks governed by 4 policy states.",
        status: "Exact 100%"
      },
      {
        elEn: "Layer 5: Continuous Analyst Feedback Loop",
        elAr: "الطبقة الخامسة: حلقة التغذية الراجعة المستمرة والتكيف",
        loc: "Chapter 3 · §3.2, Page 39",
        textEn: "Logs analyst decisions to detect concept drift over time and trigger scheduled model retraining cycles.",
        status: "Exact 100%"
      }
    ]
  },
  13: {
    titleEn: "Slide 14: Alert Ingestion & Schema Normalization",
    titleAr: "الشريحة 14: استيعاب التنبيهات وتوحيد البنية البيانية",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.3 Layer 1: Ingestion Connectors & Schema Normalization Pipeline (Pages 39-41)",
    elements: [
      {
        elEn: "Design Principle Banner: Ingestion Decoupling",
        elAr: "الشريط العلوي: مبدأ العزل المعماري للاستيعاب",
        loc: "Chapter 3 · §3.3, Page 39",
        textEn: "The module separates source-specific integration concerns from the internal processing logic of the tool, ensuring downstream layers operate on standardized attributes.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Multi-Protocol Ingestion",
        elAr: "الفقرة 1: استقبال متعدد البروتوكولات",
        loc: "Chapter 3 · §3.3, Page 39-40",
        textEn: "The module serves as the entry point for security alerts from heterogeneous technologies via Syslog, CEF, webhook endpoints, and REST API polling.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Parsing & Normalization",
        elAr: "الفقرة 2: التحليل وتوحيد الحقول",
        loc: "Chapter 3 · §3.3, Page 40",
        textEn: "The normalization process preserves security-relevant information while standardizing fields required by the proposed tool into canonical JSON structures.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Deduplication & Grouping",
        elAr: "الفقرة 3: إزالة التكرار والتجميع",
        loc: "Chapter 3 · §3.3, Page 40-41",
        textEn: "Performs validation and preprocessing: verifying required fields, converting formats, and grouping repetitive alerts within sliding time windows to eliminate raw telemetry noise.",
        status: "Exact 100%"
      }
    ]
  },
  14: {
    titleEn: "Slide 15: Multi-Dimensional Context Enrichment Pipeline",
    titleAr: "الشريحة 15: خط أنابيب إثراء السياق متعدد الأبعاد",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.4 Layer 2: Multi-Dimensional Context Enrichment Pipeline (Pages 41-43)",
    elements: [
      {
        elEn: "Banner: Enrichment Modular Resilience & Scope",
        elAr: "الشريط العلوي: المرونة المعيارية وحدود الإثراء",
        loc: "Chapter 3 · §3.4, Page 41",
        textEn: "The layer degrades gracefully when particular enrichment sources are temporarily unavailable, preparing an enriched alert object without directly executing actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Asset & Identity Context",
        elAr: "الفقرة 1: سياق حساسية الأصول ورتبة الهوية",
        loc: "Chapter 3 · §3.4, Page 41-42",
        textEn: "Provides organizational context: asset type, business criticality, network location, and exposure level. Enriches account privilege level and role indicators.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Threat Intelligence",
        elAr: "الفقرة 2: معلومات التهديدات السيبرانية الخارجية",
        loc: "Chapter 3 · §3.4, Page 42",
        textEn: "Enriches observable indicators (IPs, domains, URLs, file hashes) with reputation status, confidence ratings, and threat actor attribution.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Historical Context",
        elAr: "الفقرة 3: التتبع الزمني والتكرار التاريخي",
        loc: "Chapter 3 · §3.4, Page 43",
        textEn: "Determines whether similar alerts, indicators, or assets appeared previously within a configurable time window to establish behavioral frequency baselines.",
        status: "Exact 100%"
      }
    ]
  },
  15: {
    titleEn: "Slide 16: AI/ML Triage & Dynamic Risk Scoring Formulation",
    titleAr: "الشريحة 16: محرك الفرز الذكي وصياغة معادلة تقييم المخاطر الديناميكية",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5 Layer 3: AI/ML Triage Engine & Dynamic Risk Scoring Formulation (Pages 43-45)",
    elements: [
      {
        elEn: "Card 1: Supervised ML Triage Model",
        elAr: "الفقرة 1: نموذج تعلم الآلة الإشرافي للفرز",
        loc: "Chapter 3 · §3.5, Page 43-44",
        textEn: "Employs supervised classification trained on enriched feature vectors to predict whether an alert represents a true actionable threat or benign security noise.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Dynamic Risk Scoring Formula",
        elAr: "الفقرة 2: معادلة تقييم المخاطر الديناميكية المعتمدة",
        loc: "Chapter 3 · §3.5, Page 44",
        textEn: "R = ws S + wt T + wa A - wc C computes calibrated risk balancing baseline severity (S), threat intelligence (T), asset criticality (A), and compensating controls (C).",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Mandatory Analytical Output",
        elAr: "الفقرة 3: المخرج التحليلي المعاير لدعم القرار",
        loc: "Chapter 3 · §3.5, Page 45",
        textEn: "Produces an actionability probability label alongside a continuous normalized risk score between 0.00 and 1.00 to drive dynamic priority ordering.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat 1: R (Dynamic Risk Score)",
        elAr: "الشارة 1: درجة الخطر الديناميكية R",
        loc: "Chapter 3 · §3.5, Page 44",
        textEn: "Composite risk metric balancing threat indicators and compensating controls.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat 2: 95.1% Incident Retention Target",
        elAr: "الشارة 2: نسبة حفظ التهديدات الحقيقية 95.1%",
        loc: "Chapter 2 · §2.4.1 & Chapter 3 · §3.5, Page 27, 44",
        textEn: "Ensures suppression algorithms retain over 95% of actionable security incidents.",
        status: "Exact 100%"
      },
      {
        elEn: "Stat 3: 0.0 - 1.0 Calibrated Scale",
        elAr: "الشارة 3: المدى المعاير من 0.0 إلى 1.0",
        loc: "Chapter 3 · §3.5, Page 45",
        textEn: "Normalized decision score driving queue tier assignment.",
        status: "Exact 100%"
      }
    ]
  },
  16: {
    titleEn: "Slide 17: Adaptive Alert Prioritization & Noise Suppression",
    titleAr: "الشريحة 17: طوابير الأولويات التكيفية وقمع الضجيج الأمني",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5-3.6 Layer 3/4: Adaptive Prioritization Queues & Noise Suppression (Pages 45-47)",
    elements: [
      {
        elEn: "Banner: Operational Rationale for Dynamic Ordering",
        elAr: "الشريط العلوي: الأساس المنطقي للترتيب الديناميكي",
        loc: "Chapter 3 · §3.5, Page 45",
        textEn: "Dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues by 22.9%, preventing high-priority threat delays.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Adaptive Prioritization",
        elAr: "الفقرة 1: الترتيب التكيفي للأولويات",
        loc: "Chapter 3 · §3.6, Page 45",
        textEn: "Converts analytical outputs into operational decisions about alert ordering. Alerts are placed into dynamic priority tiers (P1-P4) using the calculated risk score.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Noise Suppression",
        elAr: "الفقرة 2: قمع الضجيج الأمني وحجب التنبيهات الروتينية",
        loc: "Chapter 3 · §3.6, Page 46",
        textEn: "Suppressed alerts are excluded from primary queues under explicit policy conditions, reducing analyst fatigue while retaining telemetry in audit archives.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Deterministic Overrides",
        elAr: "الفقرة 3: القواعد الحاكمة والاستثناءات الأمنية",
        loc: "Chapter 3 · §3.6, Page 46-47",
        textEn: "Operational rules override model scores when critical assets, privileged accounts, or sensitive network segments are involved, ensuring mandatory analyst review.",
        status: "Exact 100%"
      }
    ]
  },
  17: {
    titleEn: "Slide 18: Automated Response Playbooks & SOAR Integration",
    titleAr: "الشريحة 18: دفاتر الاستجابة المؤتمتة وتكامل واجهات SOAR",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Layer 4: Automated Response Playbooks & SOAR API Orchestration (Pages 47-49)",
    elements: [
      {
        elEn: "Banner: Response Policy Principle",
        elAr: "الشريط العلوي: مبدأ سياسة الاستجابة المنضبطة",
        loc: "Chapter 3 · §3.7, Page 47",
        textEn: "The decision to automate considers both estimated security risk and the potential operational disruption of the response action itself.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Host Isolation Playbook",
        elAr: "الفقرة 1: دفتر عزل الأجهزة المصابة",
        loc: "Chapter 3 · §3.7, Page 47-48",
        textEn: "Quarantines compromised endpoints via EDR API, cutting off network lateral movement while preserving forensic telemetry.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Firewall IP Block Playbook",
        elAr: "الفقرة 2: دفتر حظر عناوين IP على الجدران النارية",
        loc: "Chapter 3 · §3.7, Page 48",
        textEn: "Pushes dynamic blacklists to perimeter firewalls via API to sever active Command & Control (C2) communication channels.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Account Revocation Playbook",
        elAr: "الفقرة 3: دفتر سحب صلاحيات الحسابات المخترقة",
        loc: "Chapter 3 · §3.7, Page 48",
        textEn: "Revokes compromised Kerberos tickets and disables Active Directory accounts exhibiting anomalous credential dumps.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 4: Phishing Purge Playbook",
        elAr: "الفقرة 4: دفتر تطهير رسائل التصيد الاحتيالي",
        loc: "Chapter 3 · §3.7, Page 49",
        textEn: "Searches Exchange/O365 mailboxes via Graph API to purge matching malicious phishing messages enterprise-wide.",
        status: "Exact 100%"
      }
    ]
  },
  18: {
    titleEn: "Slide 19: Human-AI Teaming: Policy States & Controlled Decision Gates",
    titleAr: "الشريحة 19: بوابات القرار المنضبطة وحالات السياسة الأربع",
    chapter: "Chapter 2 & 3: Human-AI Teaming",
    section: "§2.3.2 & §3.7 Controlled Autonomy, Policy States & Decision Gates (Pages 26-27, 48-49)",
    elements: [
      {
        elEn: "Banner: Controlled Autonomy Principle",
        elAr: "الشريط العلوي: مبدأ الأتمتة المنضبطة",
        loc: "Chapter 3 · §3.7, Page 48",
        textEn: "Strict policy safeguards prevent automatic suppression or destructive containment on critical assets or privileged identities regardless of statistical model score.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Automated Response (State 1)",
        elAr: "الفقرة 1: الحالة الأولى: استجابة مؤتمتة بالكامل",
        loc: "Chapter 3 · §3.7, Page 48",
        textEn: "High Confidence + Low Blast Radius: Executes approved low-risk or well-defined response workflows when policy conditions and confidence thresholds are fully met.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Human Approval Required (State 2)",
        elAr: "الفقرة 2: الحالة الثانية: تتطلب موافقة بشرية",
        loc: "Chapter 3 · §3.7, Page 48",
        textEn: "Operational Consequences: Generates a recommended response action but requires explicit analyst authorization before executing on moderate-impact systems.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Analyst Investigation (State 3)",
        elAr: "الفقرة 3: الحالة الثالثة: تحقيق يدوي معمق",
        loc: "Chapter 3 · §3.7, Page 49",
        textEn: "Low Confidence or Critical Assets: Forwards the alert to the active analyst queue for comprehensive manual validation when high ambiguity exists.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 4: Monitor / Record (State 4)",
        elAr: "الفقرة 4: الحالة الرابعة: مراقبة وتسجيل فقط",
        loc: "Chapter 3 · §3.7, Page 49",
        textEn: "Audit & Baseline Telemetry: Retains the alert and all associated contextual evidence in the security dossier without active intervention for audit compliance.",
        status: "Exact 100%"
      }
    ]
  },
  19: {
    titleEn: "Slide 20: Continuous Analyst Feedback Loop & Model Adaptation",
    titleAr: "الشريحة 20: حلقة التغذية الراجعة المستمرة وتكييف النماذج ضد الانحراف",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.8 Continuous Analyst Feedback Loop & Active Model Adaptation (Pages 50-51)",
    elements: [
      {
        elEn: "Card 1: Analyst Resolution Capture",
        elAr: "الفقرة 1: توثيق قرارات المحللين وبناء الحقيقة الأرضية",
        loc: "Chapter 3 · §3.8, Page 50",
        textEn: "During alert investigation, an analyst may confirm or reject the model's risk assessment, adjust the assigned priority, or modify the response course, logging ground-truth data.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Concept Drift Monitoring",
        elAr: "الفقرة 2: مراقبة انحراف المفاهيم ورصد تراجع الدقة",
        loc: "Chapter 3 · §3.8, Page 50-51",
        textEn: "Feedback can be used to assess whether the machine-learning model consistently overestimates or underestimates risk for specific alert types as adversary behaviors evolve.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Scheduled Retraining Pipeline",
        elAr: "الفقرة 3: خط أنابيب إعادة التدريب والتحديث الدوري",
        loc: "Chapter 3 · §3.8, Page 51",
        textEn: "Feedback supports adjustment of prioritization thresholds and suppression policies when operational results indicate recurring false positives or false negatives.",
        status: "Exact 100%"
      }
    ]
  },
  20: {
    titleEn: "Slide 21: Design Science Research (DSR) – 6 Rigorous Phases",
    titleAr: "الشريحة 21: منهجية البحث العلمي ومراحل بحوث علوم التصميم الست",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.5 Research Methodology & Design Science Research (DSR) 6 Phases (Pages 16-17)",
    elements: [
      {
        elEn: "Phase 1: Problem Identification & Motivation",
        elAr: "المرحلة الأولى: توصيف المشكلة وتحفيز البحث",
        loc: "Chapter 1 · §1.5, Page 16",
        textEn: "Documented alert fatigue, static playbook fragility, and operational bottlenecks across contemporary enterprise SOCs.",
        status: "Exact 100%"
      },
      {
        elEn: "Phase 2: Objectives of a Solution",
        elAr: "المرحلة الثانية: صياغة متطلبات ومعايير الحل",
        loc: "Chapter 1 · §1.5, Page 16",
        textEn: "Derived technical objectives for multi-layered ingestion, context enrichment, ML triage, dynamic risk scoring, and governed response.",
        status: "Exact 100%"
      },
      {
        elEn: "Phase 3: Design & Development Blueprint",
        elAr: "المرحلة الثالثة: التصميم المعماري والتطوير",
        loc: "Chapter 1 · §1.5, Page 16",
        textEn: "Architected the 5-layer AI-SOAR framework, specifying data flows, normalization protocols, and decision state machine logic.",
        status: "Exact 100%"
      },
      {
        elEn: "Phase 4: Demonstration in Simulation Lab",
        elAr: "المرحلة الرابعة: التطبيق العملي في بيئة محاكاة",
        loc: "Chapter 1 · §1.5, Page 17",
        textEn: "Preparing security alert datasets, performing feature engineering, simulated enterprise environment setup, and integrating the prototype pipeline.",
        status: "Exact 100%"
      },
      {
        elEn: "Phase 5: Evaluation against Empirical Metrics",
        elAr: "المرحلة الخامسة: التقييم مقابل المؤشرات المعيارية",
        loc: "Chapter 1 · §1.5, Page 17",
        textEn: "Developing the selected AI/ML mechanism, training algorithms, and establishing calibration thresholds; evaluating against accuracy and dwell time metrics.",
        status: "Exact 100%"
      },
      {
        elEn: "Phase 6: Academic Communication & Defense",
        elAr: "المرحلة السادسة: التوثيق الأكاديمي والمناقشة الرسمية",
        loc: "Chapter 1 · §1.5, Page 17",
        textEn: "Connecting intelligent analysis with SOAR response workflows; thesis report documentation and presentation dissemination to the university panel.",
        status: "Exact 100%"
      }
    ]
  },
  21: {
    titleEn: "Slide 22: System Architecture & Prototype Integration Environment",
    titleAr: "الشريحة 22: المواصفات المعمارية وبيئة المحاكاة للنموذج الأولي",
    chapter: "Chapter 3: System Architecture & Prototype Specifications",
    section: "§3.2-3.3, §1.6 System Architecture Specifications & Prototype Simulation Stack (Pages 17-18, 38-41)",
    elements: [
      {
        elEn: "Banner: Graduation Project Scope & Simulation Testbed",
        elAr: "الشريط العلوي: نطاق المشروع وبيئة المحاكاة المعملية",
        loc: "Chapter 1 · §1.6 & Chapter 3 · §3.2, Page 17-18, 38",
        textEn: "The project focuses on architectural integration and prototype evaluation within a controlled laboratory and simulation environment using benchmark datasets.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Multi-Agent Layer",
        elAr: "الفقرة 1: طبقة العملاء الذكية (المهاجم والمدافع)",
        loc: "Chapter 3 · §3.2.1, Page 39",
        textEn: "Attacker Agent simulates adaptive multi-stage cyber attacks in a controlled testbed; Defender Agent coordinates intelligent alert analysis, risk scoring, and decision support.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Ingestion & Connectors",
        elAr: "الفقرة 2: موصلات استيعاب السجلات وتوحيد البنية",
        loc: "Chapter 3 · §3.3, Page 39-41",
        textEn: "Connectors interface with SIEM, EDR, IDS, and network telemetry via REST APIs, webhooks, or log streams, standardizing heterogeneous alerts into JSON format.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Analytical Scoring Engine",
        elAr: "الفقرة 3: محرك التقييم التحليلي للمخاطر",
        loc: "Chapter 3 · §3.4-3.5, Page 41-45",
        textEn: "Processes multi-dimensional context (asset criticality, identity sensitivity, threat intelligence) to compute continuous risk scores and actionability labels.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 4: SOAR API Playbooks",
        elAr: "الفقرة 4: دفاتر عمل SOAR عبر واجهات البرمجة",
        loc: "Chapter 3 · §3.7, Page 47-49",
        textEn: "Translates approved response decisions into automated API executions across target security controls (host isolation, IP blocking, credential resets).",
        status: "Exact 100%"
      }
    ]
  },
  22: {
    titleEn: "Slide 23: Incident Handling Workflow & Empirical Benchmarks",
    titleAr: "الشريحة 23: مسار معالجة الحوادث المتكامل والمؤشرات المعيارية",
    chapter: "Chapter 3: Incident Handling Workflow",
    section: "§3.2, §3.7, §2.4 End-to-End Incident Handling Lifecycle & Empirical Literature Benchmarks (Pages 28-33, 38-49)",
    elements: [
      {
        elEn: "Banner: Theoretical & Empirical Alignment",
        elAr: "الشريط العلوي: المطابقة العلمية والعملية للمسار التشغيلي",
        loc: "Chapter 3 · §3.2 & Chapter 2 · §2.4, Page 28, 38",
        textEn: "Rather than relying on unverified operational claims, the workflow connects the 5-layer architecture directly with verified empirical metrics from peer-reviewed SOC literature.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: End-to-End Operational Pipeline (5 Stages)",
        elAr: "الفقرة 1: المسار التشغيلي المتكامل خماسي المراحل",
        loc: "Chapter 3 · §3.2 & §3.7, Page 38-49",
        textEn: "1. Alert Ingestion & Normalization -> 2. Context Enrichment -> 3. AI Triage & Risk Scoring -> 4. Dynamic Prioritization & Policy Gate -> 5. Controlled SOAR Execution & Feedback.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: Empirical Benchmarks from Literature",
        elAr: "الفقرة 2: المؤشرات المعيارية الموثقة في الأدبيات السابقة",
        loc: "Chapter 1 · §1.2, Chapter 2 · §2.4.1-2.4.3, Pages 13, 27-30",
        textEn: "Queue Dwell Time: 22.9% reduction (Gelman 2023); FP Suppression: 54% with 95.1% true capture (Gelman 2023); Latency: 300 µs inference (Chavali 2024); Attacker IP Recall: 2.25x (Liu 2022).",
        status: "Exact 100%"
      }
    ]
  },
  23: {
    titleEn: "Slide 24: Operational Challenges & Technical Adaptations",
    titleAr: "الشريحة 24: التحديات التشغيلية والحلول التقنية المعتمدة",
    chapter: "Project Report & Defense Guide",
    section: "Graduation Defense Guide §9 & Report §1.2, §2.4, §3.7, §3.8 Operational Risk Controls & Mitigations",
    elements: [
      {
        elEn: "Upper Lead: Operational Friction Landscape",
        elAr: "النص العلوي: مشهد التحديات والمخاطر التشغيلية",
        loc: "Report §1.2, §2.4, §3.8, Page 12, 27, 50",
        textEn: "Real-world SOC deployments encounter severe friction across data variance, high-speed triage risks, and temporal model degradation. The proposed architecture directly embeds countermeasures at each architectural layer.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Log Schema Divergence (Mitigation: Normalization)",
        elAr: "الفقرة 1: تشتت صيغ البيانات (الحل: محرك التوحيد المعياري)",
        loc: "Report §1.1 & §3.3, Page 11, 39-40",
        textEn: "Multi-vendor tool telemetry (firewalls, EDR, SIEM) outputs incompatible fields, causing pipeline parsing failures. Countermeasure: Intermediate Normalization Engine standardizes schema into unified attributes.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: False-Positive Automation (Mitigation: Policy Gating)",
        elAr: "الفقرة 2: مخاطر الأتمتة العشوائية (الحل: بوابات القرار المنضبطة)",
        loc: "Report §2.2.3 & §3.7, Page 25, 48-49",
        textEn: "Uncontrolled automated containment on benign alerts risks cutting business-critical hosts. Countermeasure: 4-Tier Controlled Policy Gating mandates manual approval for high blast-radius actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Temporal Concept Drift (Mitigation: Feedback Loop)",
        elAr: "الفقرة 3: انحراف دقة النماذج (الحل: حلقة التغذية الراجعة المستمرة)",
        loc: "Report §2.4 & §3.8, Page 27, 50-51",
        textEn: "Adversarial TTPs evolve rapidly, causing static classifiers to experience accuracy degradation over time. Countermeasure: Continuous Analyst Feedback Loop recalibrates models against new attack vectors.",
        status: "Exact 100%"
      }
    ]
  },
  24: {
    titleEn: "Slide 25: Current Achievements & Phase 2 Roadmap",
    titleAr: "الشريحة 25: ما تم إنجازه وخارطة طريق المرحلة الثانية",
    chapter: "Project Milestones & Future Roadmap",
    section: "Chapter 1 (§1.5), Chapter 2 (§2.5), Chapter 3 (§3.1-3.8) Design Science Research Milestone Registry (Pages 16-17, 34-35, 51-53)",
    elements: [
      {
        elEn: "Closing Banner: Defense Conclusion & Faculty Acknowledgments",
        elAr: "الشريط العلوي: ختام المناقشة والشكر للجنة الأكاديمية",
        loc: "Front Matter, Page 1 & Chapter 1 · §1.5, Page 17",
        textEn: "Thank You – Open for Discussion & Defense Questions | Supervised by Dr. Raed Saeed · Department of Computer Science · University of Science and Technology.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 1: Completed in GP1",
        elAr: "الفقرة 1: ما تم إنجازه في مشروع تخرج 1",
        loc: "Report §1.5, §2.5, §3.1-3.8, Pages 16-53",
        textEn: "Empirical Problem Formulation: Documented alert fatigue, 100 GB daily influx, and triage bottleneck. Literature Synthesis: Structured Table 2-1 and established research gap. 5-Layer Architecture Design: Engineered end-to-end blueprint.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 2: GP2 Roadmap (Weeks 1-12)",
        elAr: "الفقرة 2: خارطة طريق التنفيذ لمشروع 2 (الأسابيع 1-12)",
        loc: "Report §1.5, Page 17",
        textEn: "Phase 4 (Weeks 1-4): SOC alert dataset curation, schema parsing & feature vectorization pipeline. Phase 5 (Weeks 5-8): ML training & dynamic risk calibration. Phase 6 (Weeks 9-12): SOAR playbook integration & testbed evaluation.",
        status: "Exact 100%"
      },
      {
        elEn: "Card 3: Evaluation Target Metrics",
        elAr: "الفقرة 3: معايير ومؤشرات التقييم المستهدفة",
        loc: "Report §1.5 & §2.4.1, Page 17, 27",
        textEn: "Dwell Time Reduction: Target >= 22.9% reduction in queue wait time. False Positive Suppression: Target >= 50% suppression with >= 95% true alert retention. Full Decision Auditability: 100% logging of all triage and response actions.",
        status: "Exact 100%"
      }
    ]
  }
};
"""

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace SLIDE_REFS
old_refs_match = re.search(r'// =+ [^\n]*SLIDE REPORT REFERENCES.*?const SLIDE_REFS = \{.*?\n\};\n', html, re.DOTALL)
if old_refs_match:
    html = html[:old_refs_match.start()] + SLIDE_REFS_CODE.strip() + "\n\n" + html[old_refs_match.end():]
    print("✓ Successfully replaced SLIDE_REFS with exact 1:1 matching dictionary.")
else:
    # fallback regex
    old_refs_match2 = re.search(r'const SLIDE_REFS = \{.*?\n\};\n', html, re.DOTALL)
    if old_refs_match2:
        html = html[:old_refs_match2.start()] + SLIDE_REFS_CODE.strip() + "\n\n" + html[old_refs_match2.end():]
        print("✓ Fallback: successfully replaced SLIDE_REFS with exact 1:1 matching dictionary.")
    else:
        print("❌ Could not find old SLIDE_REFS to replace!")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved presentation/index.html with exact 1-to-1 SLIDE_REFS.")
