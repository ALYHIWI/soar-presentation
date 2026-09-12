# -*- coding: utf-8 -*-

with open(r'presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_22 = html.find('\n  22: {')
pos_23 = html.find('\n  23: {')
pos_24 = html.find('\n  24: {')

print("pos_22:", pos_22)
print("pos_23:", pos_23)
print("pos_24:", pos_24)

new_refs_22 = '''\n  22: {
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

new_refs_23 = '''\n  23: {
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

# Replace from pos_22 to pos_24
html_updated = html[:pos_22] + new_refs_22 + new_refs_23 + html[pos_24:]

with open(r'presentation\index.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Cleanly replaced SLIDE_REFS 22 and 23!")
