# -*- coding: utf-8 -*-
import re

new_refs_2 = '''  2: {
    titleEn: "Slide 03: The Modern SOC Operational Landscape",
    titleAr: "الشريحة 03: المشهد التشغيلي لمراكز العمليات الأمنية الحديثة (SOC)",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.1 Overview of Modern SOCs & §1.2 Problem Statement (Pages 11-14)",
    elements: [
      {
        elEn: "Lead Paragraph",
        elAr: "الفقرة التمهيدية",
        loc: "§1.1, Paragraph 1, Lines 1-7 (Page 11)",
        textEn: "A Security Operations Center (SOC) is a centralized operational function responsible for monitoring, detecting, investigating, and responding to organizational cyber threats (Khayat et al., 2025)...",
        status: "Exact 100%"
      },
      {
        elEn: "Data Influx & SIEM Card",
        elAr: "طوفان البيانات ودور SIEM",
        loc: "§1.1 (Page 11) & §1.2 (Page 13)",
        textEn: "Organizations implement SIEM platforms for centralized log management... Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion consists of non-actionable noise.",
        status: "Exact 100%"
      },
      {
        elEn: "Heterogeneous Tool Stacks Card",
        elAr: "تشتت الأدوات الأمنية",
        loc: "§1.1, Paragraph 1, Lines 6-9 (Page 11)",
        textEn: "Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous (Kinyua & Awuah, 2021).",
        status: "Exact 100%"
      },
      {
        elEn: "Tiered Analyst Hierarchy Card",
        elAr: "هرمية المحللين المرهقة",
        loc: "§1.1, Paragraph 2, Lines 1-5 (Page 11)",
        textEn: "Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, manually gathering contextual evidence across disparate sources (Bridges et al., 2023; Khayat et al., 2025).",
        status: "Exact 100%"
      },
      {
        elEn: "Empirical Statistics Row (100 GB, 22.9%, 54%)",
        elAr: "شريط الإحصائيات المعتمدة",
        loc: "§1.2, Paragraph 1 & 4 (Pages 13-14) & §2.4.1 (Gelman et al., 2023)",
        textEn: "100 GB daily influx (§1.2); 22.9% critical incident queue dwell time reduction via dynamic triage (§1.2, Gelman et al., 2023); 54% false-positive incident suppression with 95.1% actionable capture (§2.4.1).",
        status: "Exact 100%"
      }
    ]
  },'''

new_refs_19 = '''  19: {
    titleEn: "Slide 20: Human-AI Teaming: Policy States & Controlled Decision Gates",
    titleAr: "الشريحة 20: تكامل الإنسان والذكاء: حالات السياسة وبوابات القرار المنضبطة",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Automated Response Policy & §2.3.2 Human-AI Teaming (Pages 22-23, 40-42)",
    elements: [
      {
        elEn: "Four Architectural Policy States (S1, S2, S3, S4)",
        elAr: "حالات السياسة الأربع المعتمدة",
        loc: "§3.7, Paragraphs 3-6 (Pages 41-42)",
        textEn: "S1: Automated Response (approved low-risk workflows, high confidence, low blast radius)\\nS2: Human Approval Required (containment actions with operational impact)\\nS3: Analyst Investigation (low confidence or critical production assets)\\nS4: Monitor / Record (retention without containment for auditability).",
        status: "Exact 100%"
      },
      {
        elEn: "Controlled Autonomy Principle",
        elAr: "مبدأ الأتمتة المنضبطة",
        loc: "§3.7, Paragraph 3 (Page 41) & Chhetri et al. (2024)",
        textEn: "The amount of human involvement depends on the uncertainty and consequence associated with the decision; strict safeguards prevent automatic suppression of critical assets.",
        status: "Exact 100%"
      }
    ]
  },'''

new_refs_22 = '''  22: {
    titleEn: "Slide 23: System Architecture & Prototype Integration Environment",
    titleAr: "الشريحة 23: معمارية النظام وبيئة التكامل والمحاكاة للنموذج الأولي",
    chapter: "Chapter 3: Proposed System Architecture & Chapter 1 Scope",
    section: "§3.2-3.3 Architecture & §1.6 Scope and Limitations (Pages 16, 31-35)",
    elements: [
      {
        elEn: "Multi-Agent Coordination Layer (§3.2.1)",
        elAr: "طبقة الوكلاء الأذكياء",
        loc: "§3.2.1 (Pages 33-34) & Agrawal et al. (2026)",
        textEn: "Attacker Agent generates adaptive attack activity in controlled testbed; Defender Agent coordinates intelligent defensive analysis, risk scoring, and decision support.",
        status: "Exact 100%"
      },
      {
        elEn: "Ingestion & Connector Module (§3.3)",
        elAr: "وحدة الاستيعاب والموصلات",
        loc: "§3.3 (Pages 34-35)",
        textEn: "Connectors interface with SIEM, EDR, IDS via REST APIs, webhooks, or log streams, standardizing alerts into normalized schemas while retaining source provenance.",
        status: "Exact 100%"
      },
      {
        elEn: "Analytical Scoring Engine & Logic (§3.4, §3.5, §3.6)",
        elAr: "محرك التحليل والتقييم الديناميكي",
        loc: "§3.4-3.6 (Pages 35-40)",
        textEn: "Processes multi-dimensional context to compute continuous normalized risk score [0, 1] and confidence indicators for dynamic queue prioritization.",
        status: "Exact 100%"
      },
      {
        elEn: "SOAR API Playbooks & Prototype Scope (§3.7, §1.6.1)",
        elAr: "دفاتر عمل SOAR ونطاق النموذج الأولي",
        loc: "§3.7 (Pages 40-42) & §1.6.1 (Page 16)",
        textEn: "Translates approved response decisions into automated API executions (Karlzén & Sommestad, 2023; Sworna et al., 2023); evaluated within controlled simulation environment.",
        status: "Exact 100%"
      }
    ]
  },'''

new_refs_23 = '''  23: {
    titleEn: "Slide 24: Operational Incident Handling Workflow & Empirical Benchmarks",
    titleAr: "الشريحة 24: مسار المعالجة التشغيلي للحوادث والمؤشرات المعيارية من الأدبيات",
    chapter: "Chapter 3: Proposed System Architecture & Chapter 2 Literature",
    section: "§3.2 Operational Pipeline & §1.2, §2.4 Empirical Benchmarks (Pages 13-14, 23-28, 31-33)",
    elements: [
      {
        elEn: "End-to-End Operational Pipeline (5 Steps)",
        elAr: "المسار التشغيلي المتكامل (5 خطوات)",
        loc: "§3.2-3.8 System Architecture (Pages 31-43)",
        textEn: "1. Ingestion & Normalization (§3.3)\\n2. Context Enrichment (§3.4)\\n3. AI Triage & Risk Scoring [0, 1] (§3.5)\\n4. Dynamic Prioritization & Policy Gate (§3.6, §3.7)\\n5. Controlled SOAR Execution & Feedback (§3.7, §3.8).",
        status: "Exact 100%"
      },
      {
        elEn: "Verified Empirical Benchmarks from Peer-Reviewed Literature",
        elAr: "المؤشرات المعيارية المعتمدة من الأدبيات",
        loc: "§1.2 (Page 14), §2.4.1 (Pages 24-25), §2.4.2 (Pages 25-26), §2.4.3 (Pages 26-27)",
        textEn: "Queue Dwell Time Reduction: 22.9% (Gelman et al., 2023)\\nFP Suppression: 54% with 95.1% Actionable Capture (Gelman et al., 2023)\\nInference Time: ~300 µs per sample (Chavali et al., 2024)\\nAttacker-IP Recall: up to 2.25x improvement (Liu et al., 2022).",
        status: "Exact 100%"
      }
    ]
  },'''

with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace entries in SLIDE_REFS using regex
def replace_ref_entry(html_code, idx, new_code):
    pattern = r'(\n\s*' + str(idx) + r':\s*\{.*?\n\s*\},\n)'
    m = re.search(pattern, html_code, re.DOTALL)
    assert m, f"Entry {idx} in SLIDE_REFS not found!"
    return html_code[:m.start()] + '\n' + new_code + '\n' + html_code[m.end():]

html = replace_ref_entry(html, 2, new_refs_2)
html = replace_ref_entry(html, 19, new_refs_19)
html = replace_ref_entry(html, 22, new_refs_22)
html = replace_ref_entry(html, 23, new_refs_23)

with open(r'presentation\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated SLIDE_REFS in presentation/index.html successfully!")
