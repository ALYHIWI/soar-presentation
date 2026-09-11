# -*- coding: utf-8 -*-
# This script updates ALL key slides in the presentation with verbatim text from the project file.

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Original HTML length: {len(html)}")

# ============================================================
# SLIDE S03 (s2): Modern SOC Context — from §1.1 
# UPDATE the lead paragraph to verbatim from file
# ============================================================
old = '''    <p class="lead en">Modern Security Operations Centers defend corporate infrastructures by aggregating logs across multi-vendor sensors, but encounter exponential data volume and severe operational friction.</p>'''
new = '''    <p class="lead en">A Security Operations Center (SOC) is a centralized operational function responsible for monitoring, detecting, investigating, and responding to organizational cyber threats. Modern SOCs deploy a diverse array of security sensors across network and host layers, implementing SIEM platforms for centralized log management, security-event collection, and basic correlation. However, security data is highly heterogeneous and complex to analyze due to distinct log schemas and vendor-specific data representations.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S03 lead paragraph updated")
else:
    print("✗ S03 lead paragraph NOT found")

# Update S03 card texts to match §1.1
old = '''        <h3 class="ct en">Data Influx &amp; SIEM Role</h3><h3 class="ct ar" style="display:none">طوفان البيانات ودور SIEM</h3>
        <p class="en">Gigabytes of security events collected daily from EDR, IDS/IPS, firewalls, and directory logs. SIEM aggregates logs and matches correlation signatures.</p>'''
new = '''        <h3 class="ct en">Data Influx &amp; SIEM Role</h3><h3 class="ct ar" style="display:none">طوفان البيانات ودور SIEM</h3>
        <p class="en">Organizations implement SIEM platforms for centralized log management, security-event collection, and basic correlation. Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion may consist of false positives and non-actionable noise.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S03 SIEM card updated")
else:
    print("✗ S03 SIEM card NOT found - trying partial match")
    idx = html.find('Gigabytes of security events collected')
    if idx >= 0:
        print(f"  Found at: {idx}")

old = '''        <h3 class="ct en">Heterogeneous Tool Stacks</h3><h3 class="ct ar" style="display:none">تشتت الأدوات الأمنية</h3>
        <p class="en">Security telemetry exists in vendor-specific schemas (Syslog, CEF, raw JSON). Lack of unified representations creates severe correlation barriers.</p>'''
new = '''        <h3 class="ct en">Heterogeneous Tool Stacks</h3><h3 class="ct ar" style="display:none">تشتت الأدوات الأمنية</h3>
        <p class="en">Security monitoring relies on diverse outputs from multi-vendor security stacks. Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous and complex to analyze.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S03 heterogeneous card updated")
else:
    print("✗ S03 heterogeneous card NOT found")

old = '''        <h3 class="ct en">Tiered Analyst Hierarchy</h3><h3 class="ct ar" style="display:none">هرمية المحللين المرهقة</h3>
        <p class="en">Tier-1 analysts manually sift through massive alert queues to verify threats before escalating to Tier-2/3 investigators, consuming critical response time.</p>'''
new = '''        <h3 class="ct en">Tiered Analyst Hierarchy</h3><h3 class="ct ar" style="display:none">هرمية المحللين المرهقة</h3>
        <p class="en">Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, following standard operating procedures to evaluate whether an incoming alert represents a legitimate threat or benign activity, manually gathering contextual evidence from multiple disparate security sources.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S03 tiered analyst card updated")
else:
    print("✗ S03 tiered analyst card NOT found")

# ============================================================
# SLIDE S04 (s3): Problem Statement — from §1.2
# ============================================================
old = '''        <p class="lead en" style="text-align:left;margin-bottom:14px">
          The unsustainable deluge of security data generates thousands of notifications per shift. A substantial percentage consists of benign activity, misconfigured scanners, and low-fidelity noise.
        </p>'''
new = '''        <p class="lead en" style="text-align:left;margin-bottom:14px">
          Modern Security Operations Centers (SOCs) face an unsustainable influx of security data, accumulating up to 100 gigabytes of log and alert data daily. A substantial portion of security alerts may consist of false positives and non-actionable noise. Processing this low-fidelity noise demands significant operational effort and detracts from proactive threat hunting.
        </p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S04 lead paragraph updated")
else:
    print("✗ S04 lead NOT found")

# Update S04 cards
old = '''            <h4 style="color:var(--acc);font-size:0.85rem;margin-bottom:4px" class="en">Cognitive Saturation</h4>
            <h4 style="display:none;color:var(--acc);font-size:0.85rem;margin-bottom:4px" class="ar">التشبع والإجهاد الإدراكي</h4>
            <p class="en">Continuous exposure to false alerts degrades analyst vigilance, leading to acute burnout and human error.</p>'''
new = '''            <h4 style="color:var(--acc);font-size:0.85rem;margin-bottom:4px" class="en">Alert Fatigue &amp; Context Switching</h4>
            <h4 style="display:none;color:var(--acc);font-size:0.85rem;margin-bottom:4px" class="ar">إرهاق التنبيهات وتبديل السياق</h4>
            <p class="en">This convergence of high alert volumes and excessive false positives causes high analyst workload and alert fatigue. Analysts manually investigate alerts through continuous context switching—repeatedly pivoting across disparate application windows to gather evidence, creating cognitive overload and analyst burnout.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S04 cognitive card updated")
else:
    print("✗ S04 cognitive card NOT found")

old = '''            <h4 style="color:var(--wa);font-size:0.85rem;margin-bottom:4px" class="en">Buried Critical Threats</h4>
            <h4 style="display:none;color:var(--wa);font-size:0.85rem;margin-bottom:4px" class="ar">دفن الحوادث الحرجة</h4>
            <p class="en">High-severity advanced persistent threats (APTs) remain hidden deep underneath routine noise queues.</p>'''
new = '''            <h4 style="color:var(--wa);font-size:0.85rem;margin-bottom:4px" class="en">Static Prioritization Limits</h4>
            <h4 style="display:none;color:var(--wa);font-size:0.85rem;margin-bottom:4px" class="ar">قيود الأولوية الثابتة</h4>
            <p class="en">When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried beneath lower-value noise. Dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues by 22.9%.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S04 buried card updated")
else:
    print("✗ S04 buried card NOT found")

# Update the impact on incident response section in S04
old = '''          <ul style="gap:8px">
            <li class="en"><strong>MTTD Inflation:</strong> Mean Time to Detect increases from minutes to weeks.</li>
            <li class="ar" style="display:none"><strong>تضخم زمن الاكتشاف:</strong> يتضاعف متوسط زمن اكتشاف التهديدات إلى أسابيع.</li>
            <li class="en"><strong>Analyst Churn:</strong> High turnover rates in SOC teams due to repetitive toil.</li>
            <li class="ar" style="display:none"><strong>استنزاف الكفاءات:</strong> تسرب المحللين الأمنيين بسبب الإرهاق والمهام الرتيبة.</li>
            <li class="en"><strong>SLA Violations:</strong> Delayed containment allows lateral movement across endpoints.</li>
            <li class="ar" style="display:none"><strong>فشل اتفاقيات الخدمة:</strong> تأخر العزل يمنح المهاجم فرصة التحرك العرضي في الشبكة.</li>
          </ul>'''
new = '''          <ul style="gap:8px">
            <li class="en"><strong>Automated Workflow Limits:</strong> Reliance on predefined rules and static playbooks may limit adaptability when alert context or risk conditions change dynamically.</li>
            <li class="ar" style="display:none"><strong>قيود الأتمتة التقليدية:</strong> الاعتماد على قواعد محددة مسبقاً ودفاتر عمل ثابتة يحد من التكيف عند تغير سياق التنبيه.</li>
            <li class="en"><strong>Rigid Logic Failures:</strong> Deterministic conditional logic can constrain effectiveness against novel or evasive threats that fall outside anticipated patterns.</li>
            <li class="ar" style="display:none"><strong>فشل المنطق الجامد:</strong> المنطق الحتمي يفقد فاعليته أمام التهديدات الجديدة التي تخرج عن الأنماط المتوقعة.</li>
            <li class="en"><strong>Prioritization Gap:</strong> Un-prioritized queues delay the handling of actionable threats; dynamic risk-aware ordering can reduce wait time for critical incidents by 22.9%.</li>
            <li class="ar" style="display:none"><strong>فجوة الأولوية:</strong> قوائم الانتظار غير المرتبة تؤخر التعامل مع التهديدات القابلة للتنفيذ؛ الترتيب الديناميكي يقلل وقت الانتظار بنسبة 22.9%.</li>
          </ul>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S04 impact list updated")
else:
    print("✗ S04 impact list NOT found")

# ============================================================
# SLIDE S05 (s4): Triage Bottleneck — from §1.2 (continued)
# ============================================================
old = '''        <p class="en">Static IF-THEN correlation rules fail against polymorphic malware, credential stuffing, and low-and-slow reconnaissance techniques.</p>'''
new = '''        <p class="en">Rigid conditional statements may become less effective against novel or evasive threats that fall outside anticipated patterns. While conventional automation efficiently executes repetitive steps, deterministic logic can constrain effectiveness when alert context or risk conditions change dynamically.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S05 rigid rules card updated")
else:
    print("✗ S05 rigid rules card NOT found")

old = '''        <p class="en">Analysts manually swivel between 5 to 10 disconnected consoles (SIEM, EDR, Threat Intel, Active Directory, Firewalls) to validate a single incident.</p>'''
new = '''        <p class="en">Analysts must manually gather contextual evidence from multiple disparate security sources. This manual investigation introduces context switching, where analysts repeatedly navigate across different application interfaces, hold investigative hypotheses in memory, and manually correlate heterogeneous data sources.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S05 context switching card updated")
else:
    print("✗ S05 context switching card NOT found")

old = '''        <p class="en">Alerts arrive sorted by generic vendor severity or arrival time (FIFO) without factoring in business asset criticality or active environmental risk.</p>'''
new = '''        <p class="en">When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried beneath lower-value noise. Un-prioritized queues delay the handling of actionable threats.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S05 prioritization card updated")
else:
    print("✗ S05 prioritization card NOT found")

old = '''      <p class="en"><strong>Key Takeaway:</strong> Conventional automation efficiently executes repetitive steps, but lacks the analytical adaptability to score situational context before triggering response actions.</p>'''
new = '''      <p class="en"><strong>Key Takeaway:</strong> These challenges motivate the ongoing need to investigate how intelligent alert analysis and prioritization can be integrated with operational workflows to support adaptive incident handling.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S05 key takeaway updated")
else:
    print("✗ S05 key takeaway NOT found")

# ============================================================
# SLIDE S06 (s5): Objectives — from §1.4
# ============================================================
old = '''        <p class="en" style="font-size:0.92rem">
          <strong>Primary Aim:</strong> Investigate, design, and architect an integrated <strong>AI-Based SOAR Tool</strong> that resolves alert fatigue and static triage through context-aware machine learning analysis, dynamic risk scoring, and automated orchestration.
        </p>'''
new = '''        <p class="en" style="font-size:0.92rem">
          <strong>Primary Objective:</strong> Investigate, design, and propose an integrated <strong>AI-Based Security Orchestration, Automation, and Response (SOAR) tool</strong> that addresses operational bottlenecks by integrating intelligent security alert analysis, risk-based scoring, dynamic prioritization, and automated incident response to support more adaptive and efficient security operations.
        </p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S06 primary objective updated")
else:
    print("✗ S06 primary objective NOT found")

# Update specific objectives
old = '''        <h3 class="ct en">1. Operational Analysis</h3><h3 class="ct ar" style="display:none">1. تحليل التحديات التشغيلية</h3>
        <p class="en">Examine modern SOC alert management challenges, identifying empirical points of alert fatigue and triage delay.</p>'''
new = '''        <h3 class="ct en">1. Analyze SOC Challenges</h3><h3 class="ct ar" style="display:none">1. تحليل تحديات SOC</h3>
        <p class="en">Analyze the operational challenges of current SOC alert management, specifically including alert fatigue and the limitations of static triage.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S06 obj 1 updated")
else:
    print("✗ S06 obj 1 NOT found")

old = '''        <h3 class="ct en">2. Literature &amp; Gap Synthesis</h3><h3 class="ct ar" style="display:none">2. مراجعة الأدبيات والفجوة البحثية</h3>
        <p class="en">Systematically review existing ML triage algorithms and conventional SOAR platforms to identify the integration gap.</p>'''
new = '''        <h3 class="ct en">2. Literature Review</h3><h3 class="ct ar" style="display:none">2. مراجعة الأدبيات</h3>
        <p class="en">Review existing AI/ML-based approaches and academic literature related to security alert analysis and prioritization.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S06 obj 2 updated")
else:
    print("✗ S06 obj 2 NOT found")

old = '''        <h3 class="ct en">3. Multi-Layer Architecture</h3><h3 class="ct ar" style="display:none">3. تصميم المعمارية متعددة الطبقات</h3>
        <p class="en">Formulate a comprehensive architectural design encompassing ingestion, context enrichment, ML engine, and response playbooks.</p>'''
new = '''        <h3 class="ct en">3. Design Architecture</h3><h3 class="ct ar" style="display:none">3. تصميم المعمارية</h3>
        <p class="en">Design the proposed AI-Based SOAR architecture and clearly identify its major functional components. Develop an AI/ML-based mechanism for context-aware alert analysis and risk assessment.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S06 obj 3 updated")
else:
    print("✗ S06 obj 3 NOT found")

old = '''        <h3 class="ct en">4. Controlled Automation &amp; Metrics</h3><h3 class="ct ar" style="display:none">4. الأتمتة المنضبطة والتقييم</h3>
        <p class="en">Connect dynamic prioritization with controlled SOAR response actions, incorporating human-in-the-loop oversight and rigorous evaluation.</p>'''
new = '''        <h3 class="ct en">4. Integration &amp; Evaluation</h3><h3 class="ct ar" style="display:none">4. التكامل والتقييم</h3>
        <p class="en">Integrate the outcomes of dynamic risk-based prioritization with SOAR response decision-making to guide automated workflows. Define a structured evaluation approach using appropriate machine-learning and operational metrics.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S06 obj 4 updated")
else:
    print("✗ S06 obj 4 NOT found")

# ============================================================
# SLIDE S07 (s6): Project Scope — from §1.6
# ============================================================
old = '''    <h2 class="st en">Project Scope &amp; Boundary Definition</h2>'''
new = '''    <h2 class="st en">Project Scope and Limitations</h2>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 title updated")
else:
    print("✗ S07 title NOT found")

old = '''          <li class="en"><strong>Multi-Source Telemetry Ingestion:</strong> Normalization of CEF, Syslog, and JSON alerts.</li>'''
new = '''          <li class="en"><strong>Alert Ingestion &amp; Normalization:</strong> Integration of AI/ML for security alert analysis, context-aware risk scoring, and dynamic alert prioritization.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 scope item 1 updated")
else:
    print("✗ S07 scope item 1 NOT found")

old = '''          <li class="en"><strong>Context Enrichment:</strong> Querying asset databases, threat intelligence, and user roles.</li>'''
new = '''          <li class="en"><strong>Analytical Components:</strong> Connecting analytical components with automated SOAR response workflows and decision-making mechanisms.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 scope item 2 updated")
else:
    print("✗ S07 scope item 2 NOT found")

old = '''          <li class="en"><strong>AI/ML Risk Scoring:</strong> Dynamic calculation of situational severity and certainty.</li>'''
new = '''          <li class="en"><strong>Prototype &amp; Evaluation:</strong> Implementation and testing conducted within a controlled prototype and simulation environment. Defining appropriate machine-learning and operational metrics to evaluate the tool.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 scope item 3 updated")
else:
    print("✗ S07 scope item 3 NOT found")

old = '''          <li class="en"><strong>Orchestration Gateways:</strong> Triggering automated containment with analyst oversight.</li>'''
new = '''          <li class="en"><strong>Architectural Focus:</strong> Emphasis on architectural integration rather than the invention of new foundational machine-learning algorithms or commercial platforms.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 scope item 4 updated")
else:
    print("✗ S07 scope item 4 NOT found")

# Update Out-of-Scope section
old = '''          <li class="en"><strong>Commercial SIEM Replacement:</strong> The tool supplements existing SIEMs rather than replacing enterprise storage.</li>'''
new = '''          <li class="en"><strong>Dataset Constraints:</strong> Model training may depend on synthetic, public, or otherwise limited security alert datasets, which may not fully replicate every enterprise environment.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 limitation 1 updated")
else:
    print("✗ S07 limitation 1 NOT found")

old = '''          <li class="en"><strong>Fully Autonomous Destructive Actions:</strong> Disabling critical domain controllers or production databases without approval.</li>'''
new = '''          <li class="en"><strong>Lab Environment Only:</strong> Validation is constrained to a laboratory or prototype environment rather than a live, large-scale enterprise SOC.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 limitation 2 updated")
else:
    print("✗ S07 limitation 2 NOT found")

old = '''          <li class="en"><strong>Deep Packet Hardware Inspection:</strong> Network capture is consumed via sensor logs, not raw silicon taps.</li>'''
new = '''          <li class="en"><strong>Human Oversight Required:</strong> Fully autonomous execution of high-impact actions introduces operational risks; therefore, the tool incorporates human oversight mechanisms for uncertain or potentially disruptive response actions.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S07 limitation 3 updated")
else:
    print("✗ S07 limitation 3 NOT found")

# ============================================================
# SLIDE S08 (s7): Lit Review SOC Evolution — from §2.2
# ============================================================
old = '''    <p class="lead en">Moving from static rule-based correlation to statistical machine learning allows SOC defenses to scale elastically with threat velocity.</p>''' 
# This is in the hl/highlight at bottom
old2 = '''      <p class="en"><strong>Theoretical Insight:</strong> Moving from static rule-based correlation to statistical machine learning allows SOC defenses to scale elastically with threat velocity.</p>'''
new2 = '''      <p class="en"><strong>Key Insight:</strong> SIEM primarily supports broad data collection and querying, whereas SOAR introduces configurable workflows that guide or automate investigation and incident-response activities. The output of a SIEM may serve as an input to subsequent triage, enrichment, investigation, and response processes.</p>'''

if old2 in html:
    html = html.replace(old2, new2)
    print("✓ S08 insight updated")
else:
    print("✗ S08 insight NOT found")

# G1 card
old = '''        <p class="en">Decentralized Syslog collection. Manual grep queries, reactive post-incident forensic searches.</p>'''
new = '''        <p class="en">Security telemetry collected from multiple sources including network and endpoint monitoring, intrusion detection technologies, firewalls, and threat-intelligence feeds operating with different data representations.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S08 G1 card updated")
else:
    print("✗ S08 G1 card NOT found")

# G2 card
old = '''        <p class="en">Centralized event correlation, compliance reporting, and rule-based threshold alerting.</p>'''
new = '''        <p class="en">SIEM systems aggregate and query security data from distributed sources, providing centralized log management, security-event collection, and basic correlation. However, SIEM differs from SOAR in that it primarily supports data collection rather than complete incident-response workflows.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S08 G2 card updated")
else:
    print("✗ S08 G2 card NOT found")

# G3 card
old = '''        <p class="en">API orchestration across tools, deterministic playbooks, automated ticketing and notifications.</p>'''
new = '''        <p class="en">SOAR platforms integrate disparate security applications and human processes into a unified framework. Data ingestion, correlation and prioritization, process automation, and analyst collaboration are defining SOAR capabilities, moving security information toward structured operational handling.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S08 G3 card updated")
else:
    print("✗ S08 G3 card NOT found")

# G4 card
old = '''        <p class="en">Context-aware ML triage, dynamic risk assessment, adaptive prioritization, controlled human-AI oversight.</p>'''
new = '''        <p class="en">AI/ML can extend SOAR by improving analytical, threat-intelligence, detection, and response capabilities while orchestration technologies coordinate operational actions. SOAR provides workflow management and execution; AI/ML contributes data-driven inference to activities difficult to represent through manually specified rules.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S08 G4 card updated")
else:
    print("✗ S08 G4 card NOT found")

# ============================================================
# SLIDE S09 (s8): Conventional SOAR — from §2.2.2
# ============================================================
old = '''        <p class="en">Connecting heterogeneous security appliances through REST APIs. Enables bidirectional queries to firewalls, EDR, threat intel databases, and IAM platforms.</p>'''
new = '''        <p class="en">SOAR refers to software platforms designed to integrate disparate security applications and human processes into a unified framework. A playbook defines a structured sequence of steps and actions used to handle a particular incident type, with execution triggered when predefined conditions or events are satisfied.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S09 orchestration card updated")
else:
    print("✗ S09 orchestration card NOT found")

old = '''        <p class="en">Codified response runbooks. Standardized steps execute machine-speed tasks: querying virus databases, resetting user tokens, or archiving logs.</p>'''
new = '''        <p class="en">Workflows can automate data-collection steps, coordinate actions across multiple systems, and systematically apply standard response procedures, reducing the time and effort required for routine security tasks.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S09 playbooks card updated")
else:
    print("✗ S09 playbooks card NOT found")

old = '''        <p class="en">Centralized tracking of forensic artifacts, audit trails, and containment outcomes within a unified ticketing environment for analyst accountability.</p>'''
new = '''        <p class="en">SOAR technologies reduce fragmentation of security activities by combining alert information, threat intelligence, workflow automation, and analyst collaboration within a common operational environment, supporting structured operational handling.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S09 case management card updated")
else:
    print("✗ S09 case management card NOT found")

# ============================================================
# SLIDE S10 (s9): Limitations of Conventional SOAR — from §2.2.3
# ============================================================
old = '''        <p class="en">Playbooks rely on deterministic conditionals. When threat actors slightly modify an IOC or tactic, static playbooks fail to trigger or mishandle the incident.</p>'''
new = '''        <p class="en">Playbooks operate on predefined conditions; when threat behavior deviates from anticipated patterns, static playbooks may fail to trigger appropriately or handle the incident effectively. Deterministic logic can constrain effectiveness when alert context or risk conditions change dynamically.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S10 inability card updated")
else:
    print("✗ S10 inability card NOT found")

old = '''        <p class="en">A port scan on an isolated test machine triggers the same heavy playbook as a scan against a financial database, misallocating critical defensive bandwidth.</p>'''
new = '''        <p class="en">Conventional SOAR does not inherently assess whether an alert's risk justifies the operational cost of the response action. The significance of an event may depend on multiple attributes and surrounding contextual information rather than on a single static severity value.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S10 risk context card updated")
else:
    print("✗ S10 risk context card NOT found")

old = '''        <p class="en">Uncontrolled autonomous remediation risks catastrophic collateral damage: locking out executive accounts or terminating core operational network segments.</p>'''
new = '''        <p class="en">Fully autonomous execution of high-impact security actions introduces inherent operational risks. The tool must incorporate human oversight and approval mechanisms for uncertain or potentially disruptive response actions.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S10 disruption card updated")
else:
    print("✗ S10 disruption card NOT found")

old = '''      <p class="en"><strong>Synthesis:</strong> SOAR provides the <em>muscle</em> (orchestrated execution), but desperately lacks the <em>brain</em> (intelligent contextual analysis and adaptive prioritization).</p>'''
new = '''      <p class="en"><strong>Synthesis:</strong> SOAR provides workflow management, integration, and execution capabilities, whereas AI/ML can contribute data-driven inference to activities that are difficult to represent entirely through manually specified rules. This distinction is particularly relevant to alert handling, where event significance depends on multiple attributes and contextual information.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S10 synthesis updated")
else:
    print("✗ S10 synthesis NOT found")

# ============================================================
# SLIDE S11 (s10): AI/ML Force Multiplier — from §2.3
# ============================================================
old = '''        <p class="en">Machine learning algorithms evaluate hundreds of contextual dimensions simultaneously (asset value, user deviation, threat reputation, time delta) that overwhelm human memory.</p>'''
new = '''        <p class="en">AI/ML techniques can analyze large and heterogeneous security datasets to identify patterns, classify events, detect anomalous behavior, and support security decision making. Supervised and unsupervised methods support event classification, anomaly detection, and risk assessment.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S11 analytical card updated")
else:
    print("✗ S11 analytical card NOT found")

old = '''        <p class="en">AI does not replace the security analyst; it operates as an intelligent co-pilot. Repetitive noise is filtered autonomously, while complex decisions are packaged with analytical rationale for human sign-off.</p>'''
new = '''        <p class="en">AI/ML does not necessarily replace existing SOC technologies; rather, it provides an analytical layer that complements the information collected by SIEM and the workflow execution capabilities provided by SOAR. This has been described as a force-multiplier effect for SOC analysts.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S11 human-AI card updated")
else:
    print("✗ S11 human-AI card NOT found")

# Remove unverified stats in S11
old = '''      <div class="sb"><div class="snum">70-85%</div><div class="slbl en">Noise Suppression Ratio</div><div class="slbl ar" style="display:none">نسبة قمع التنبيهات الكاذبة</div></div>
      <div class="sb"><div class="snum">&lt;2 sec</div><div class="slbl en">Inference &amp; Triage Latency</div><div class="slbl ar" style="display:none">زمن الاستنتاج والفرز</div></div>
      <div class="sb"><div class="snum">3.5x</div><div class="slbl en">Analyst Throughput Boost</div><div class="slbl ar" style="display:none">مضاعفة إنتاجية المحلل</div></div>'''
new = '''      <div class="sb"><div class="snum">AI/ML</div><div class="slbl en">Analytical Augmentation Layer</div><div class="slbl ar" style="display:none">طبقة التعزيز التحليلي</div></div>
      <div class="sb"><div class="snum">SOAR</div><div class="slbl en">Workflow Execution Platform</div><div class="slbl ar" style="display:none">منصة تنفيذ سير العمل</div></div>
      <div class="sb"><div class="snum">DSR</div><div class="slbl en">Research Methodology</div><div class="slbl ar" style="display:none">منهجية البحث العلمي</div></div>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S11 stats removed/updated")
else:
    print("✗ S11 stats NOT found")

# ============================================================
# SLIDE S13 (s12): Research Gap — from §2.5
# ============================================================
old = '''        <p class="en">Extensive literature exists evaluating ML classifiers on offline datasets (e.g. NSL-KDD, CIC-IDS). However, these studies stop at mathematical classification scores (Precision, Recall) without integrating into live incident containment pipelines.</p>'''
new = '''        <p class="en">Existing research demonstrates the use of ML for security alert analysis and SOAR workflows for automated incident response, while the integration between these capabilities remains an area worthy of further investigation. Evaluated workflows primarily focus on event ranking, alert selection, or analyst investigation rather than downstream SOAR-controlled response execution.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S13 academic gap updated")
else:
    print("✗ S13 academic gap NOT found")

old = '''        <p class="en">Commercial platforms (Splunk SOAR, Cortex XSOAR) excel at multi-tool orchestration via pre-built playbooks. However, they rely on rigid boolean triggers and lack adaptive machine learning risk assessment.</p>'''
new = '''        <p class="en">Research on automated incident response addresses a complementary portion of the incident-handling pipeline. However, existing approaches do not determine the required response directly from an alert's contextual risk, and automated execution remains identified as future work in the reviewed literature.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S13 commercial gap updated")
else:
    print("✗ S13 commercial gap NOT found")

old = '''        <p class="en" style="font-size:0.92rem">
          <strong>Our Contribution:</strong> Designing and implementing the cohesive pipeline that feeds <strong>Dynamic ML Risk Predictions</strong> directly into <strong>SOAR Orchestrated Containment Workflows</strong> with controlled human oversight gates.
        </p>'''
new = '''        <p class="en" style="font-size:0.92rem">
          <strong>Our Contribution:</strong> This project investigates the <strong>architectural integration</strong> of AI/ML-based alert analysis, risk-based scoring, dynamic prioritization, and SOAR automated response. The proposed tool examines how intelligent triage outputs can support more adaptive response decisions within operational SOAR workflows.
        </p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S13 contribution updated")
else:
    print("✗ S13 contribution NOT found")

# ============================================================
# SLIDE S14 (s13): Architecture Overview — from §3.2
# ============================================================
old = '''    <h2 class="st en">Proposed AI-Based SOAR System Architecture</h2>'''
new = '''    <h2 class="st en">High-Level Architecture Overview</h2>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S14 title updated")
else:
    print("✗ S14 title NOT found")

# ============================================================
# SLIDE S15 (s14): Ingestion — from §3.3
# ============================================================
old = '''        <p class="en">Listens to Kafka message queues, Webhooks, and Syslog sockets (UDP 514 / TCP 6514 TLS). Ingests raw alerts across diverse perimeter sensors.</p>'''
new = '''        <p class="en">The module serves as the entry point for security alerts from heterogeneous technologies. Sources may expose alerts through REST APIs, webhooks, message streams, log files, or other supported interfaces. Individual connectors communicate with corresponding sources and translate incoming data into a common internal alert structure.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S15 ingestion card updated")
else:
    print("✗ S15 ingestion card NOT found")

old = '''        <p class="en">Transforms disparate vendor schemas (ArcSight CEF, Snort Fast, Elastic JSON) into an Open Cybersecurity Schema (OCSF) internal model.</p>'''
new = '''        <p class="en">The normalization process preserves security-relevant information while standardizing fields required by the proposed tool. A normalized alert may contain attributes such as an alert identifier, timestamp, source system, alert type, original severity, source and destination information, affected user or asset, and event description.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S15 normalization card updated")
else:
    print("✗ S15 normalization card NOT found")

old = '''        <p class="en">Applies sliding window hash clustering to collapse storm alerts (e.g. 500 alerts from 1 port scan) into a single incident container.</p>'''
new = '''        <p class="en">Before forwarding an alert, the module performs basic validation and preprocessing: verifying required fields, converting timestamps into a consistent format, standardizing field names and categorical values, and removing malformed or incomplete records where appropriate.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S15 deduplication card updated")
else:
    print("✗ S15 deduplication card NOT found")

old = '''      <p class="en"><strong>Normalized Event Entity:</strong> <code>{ timestamp, source_ip, dest_ip, port, user_id, host_guid, event_type, raw_payload }</code> &mdash; establishing a clean contract for downstream enrichment.</p>'''
new = '''      <p class="en"><strong>Design Principle:</strong> The module separates source-specific integration concerns from the internal processing logic of the tool, ensuring that the remaining components do not require understanding of each vendor-specific format.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S15 footer note updated")
else:
    print("✗ S15 footer note NOT found")

# ============================================================
# SLIDE S17 (s16): AI/ML Triage — from §3.5 (remove unverified stats)
# ============================================================
old = '''      <div class="sb"><div class="snum">0 - 100</div><div class="slbl en">Dynamic Risk Range</div><div class="slbl ar" style="display:none">مدى تقييم الخطر</div></div>
      <div class="sb"><div class="snum">&plusmn;94.6%</div><div class="slbl en">Classification Accuracy</div><div class="slbl ar" style="display:none">دقة التصنيف المتوقعة</div></div>
      <div class="sb"><div class="snum">0.88</div><div class="slbl en">F1-Score Benchmark</div><div class="slbl ar" style="display:none">معيار التوازن F1</div></div>'''
new = '''      <div class="sb"><div class="snum">0–100</div><div class="slbl en">Contextual Risk Score Range</div><div class="slbl ar" style="display:none">مدى تقييم الخطر</div></div>
      <div class="sb"><div class="snum">AUC</div><div class="slbl en">Primary Evaluation Metric</div><div class="slbl ar" style="display:none">مقياس التقييم الأساسي</div></div>
      <div class="sb"><div class="snum">22.9%</div><div class="slbl en">Wait-Time Reduction (Literature)</div><div class="slbl ar" style="display:none">تحسين وقت الانتظار (الأدبيات)</div></div>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S17 stats updated")
else:
    print("✗ S17 stats NOT found")

# ============================================================
# SLIDE S18 (s17): Prioritization — update unverified stats
# ============================================================
old = '''      <p class="en"><strong>Operational Outcome:</strong> Reduces active analyst ticket backlog by <strong>65% to 80%</strong>, allowing investigators to focus on genuine advanced threats.</p>'''
new = '''      <p class="en"><strong>Operational Rationale:</strong> Dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues. The prioritization module ensures that genuine threats are identified rapidly without simultaneously increasing the manual investigative burden placed on human analysts.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S18 outcome updated")
else:
    print("✗ S18 outcome NOT found")

# ============================================================
# SLIDE S19 (s18): Playbooks — from §3.7
# ============================================================
old = '''      <p class="en"><strong>Immutable Action Log:</strong> Every playbook execution writes cryptographic audit logs capturing executing timestamp, API target, parameters, and outcome.</p>'''
new = '''      <p class="en"><strong>Policy Principle:</strong> The decision to automate an action considers not only the estimated security risk but also the potential impact of the response itself. Performing an enrichment query carries less operational risk than disabling a privileged account, isolating a production endpoint, or modifying a firewall policy.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S19 footer updated")
else:
    print("✗ S19 footer NOT found")

# ============================================================
# SLIDE S20 (s19): Human-AI Teaming — from §3.7
# ============================================================
old = '''      <p class="en"><strong>Safety Architecture:</strong> Adopts the <a href="#" style="color:var(--s)">A<sup>2</sup>C Framework</a> (Advisory &amp; Controlled Autonomy), preventing rogue automation while ensuring maximum operational speed.</p>'''
new = '''      <p class="en"><strong>Controlled Autonomy Principle:</strong> The amount of human involvement depends on the uncertainty and consequence associated with the decision. This supports a risk-aware level of autonomy, ensuring human oversight and approval mechanisms for uncertain or potentially disruptive response actions.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S20 safety architecture updated")
else:
    print("✗ S20 safety architecture NOT found")

# ============================================================
# SLIDE S21 (s20): Feedback Loop — from §3.8
# ============================================================
old = '''        <p class="en">Whenever an analyst overrides a classification, re-labels an alert, or modifies risk scores, the decision and rationale are recorded as golden training samples.</p>'''
new = '''        <p class="en">During alert investigation, an analyst may confirm or reject the model's risk assessment, adjust the assigned priority, identify whether the alert represents a true or false positive, or provide a final incident disposition. During response handling, the analyst may approve or reject a recommended action or record whether an executed workflow achieved the intended result.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S21 feedback card 1 updated")
else:
    print("✗ S21 feedback card 1 NOT found")

old = '''        <p class="en">Statistical tracking (Kolmogorov-Smirnov tests) monitors input feature drift against production baselines, detecting shifting attacker tradecraft.</p>'''
new = '''        <p class="en">Feedback can be used to assess whether the machine-learning model consistently overestimates or underestimates risk for particular types of alerts. Accumulated analyst decisions can provide additional labeled examples for periodic model retraining or validation.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S21 feedback card 2 updated")
else:
    print("✗ S21 feedback card 2 NOT found")

old = '''        <p class="en">Validated feedback samples are batched into automated model retraining pipelines. Shadow testing verifies performance before live promotion.</p>'''
new = '''        <p class="en">Feedback can support adjustment of prioritization thresholds and suppression policies when operational results indicate that the current configuration produces excessive false positives, unnecessary escalations, or missed high-priority events.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S21 feedback card 3 updated")
else:
    print("✗ S21 feedback card 3 NOT found")

# ============================================================
# SLIDE S22 (s21): DSR Methodology — fix label from §1.5
# ============================================================
old = '''      <span class="en">Chapter 2 &ndash; Research Methodology</span>'''
new = '''      <span class="en">Research Methodology &ndash; Design Science Research (DSR)</span>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S22 chapter label fixed")
else:
    print("✗ S22 chapter label NOT found")

old = '''          <p class="en">Quantified SOC operational bottlenecks, alert fatigue crisis, and established academic &amp; practical significance.</p>'''
new = '''          <p class="en">Defines the operational challenges associated with SOC alert management, including alert fatigue and static triage, and establishes the objectives of the project. Undertaken primarily within Graduation Project 1.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S22 P1 description updated")
else:
    print("✗ S22 P1 description NOT found")

old = '''          <p class="en">Systematic literature review, technical background analysis, and formalization of research gap and deliverables.</p>'''
new = '''          <p class="en">Examines existing research on SOC alert management, conventional SOAR, AI/ML-based alert analysis, risk scoring, dynamic prioritization, and automated incident response. Provides the academic foundation for identifying and validating the research gap. Undertaken primarily within Graduation Project 1.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S22 P2 description updated")
else:
    print("✗ S22 P2 description NOT found")

old = '''          <p class="en">Formulation of multi-tier architecture, module specifications, data flows, and playbook orchestrations.</p>'''
new = '''          <p class="en">Develops the system architecture, module specifications, data flows, and integration mechanisms. Formulates the major functional components of the proposed tool. The current scope of Graduation Project 1.</p>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S22 P3 description updated")
else:
    print("✗ S22 P3 description NOT found")

# ============================================================
# SLIDE S25 (s24): Progress & Roadmap — update completion items
# ============================================================
old = '''          <li class="en"><strong style="color:var(--ok)">&#10003; Problem Definition:</strong> Rigorous analysis of SOC alert fatigue &amp; triage bottlenecks.</li>'''
new = '''          <li class="en"><strong style="color:var(--ok)">&#10003; Problem Definition:</strong> Analysis of SOC alert fatigue, context switching, static triage limitations, and prioritization gaps.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S25 achievement 1 updated")
else:
    print("✗ S25 achievement 1 NOT found")

old = '''          <li class="en"><strong style="color:var(--ok)">&#10003; Literature &amp; Gap Synthesis:</strong> Benchmarked ML algorithms against SOAR frameworks.</li>'''
new = '''          <li class="en"><strong style="color:var(--ok)">&#10003; Literature Review &amp; Gap Analysis:</strong> Reviewed AI/ML approaches, SOAR frameworks, and identified the integration gap between intelligent triage and automated response.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S25 achievement 2 updated")
else:
    print("✗ S25 achievement 2 NOT found")

old = '''          <li class="en"><strong style="color:var(--ok)">&#10003; System Architecture:</strong> Fully articulated 5-layer design, data schema &amp; risk formula.</li>'''
new = '''          <li class="en"><strong style="color:var(--ok)">&#10003; System Architecture (Chapter 3):</strong> Modular pipeline design covering Ingestion, Context Enrichment, AI/ML Engine, Response Policy, and Feedback Loop.</li>'''

if old in html:
    html = html.replace(old, new)
    print("✓ S25 achievement 3 updated")
else:
    print("✗ S25 achievement 3 NOT found")

# Save the updated file
with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nDone! Updated HTML length: {len(html)}")
