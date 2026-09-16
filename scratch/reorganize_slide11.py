# -*- coding: utf-8 -*-
"""
Script to reorganize Slide 11 (id="s10") with zero deletions and superior visual balance.
"""
import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_s10 = """<section class="slide" id="s10">
  <div class="orb o1" style="opacity:0.3"></div>
  <div class="orb o2" style="opacity:0.25"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
      <span class="en">Chapter 1 &ndash; Methodology</span><span class="ar" style="display:none">الفصل الأول &ndash; المنهجية</span>
    </div>
    <h2 class="st en">Development Methodology: Design Science Research (DSR)</h2>
    <h2 class="st ar" style="display:none">منهجية التطوير: علوم التصميم (DSR)</h2>
    <div class="gl"></div>
    <p class="lead en" style="margin-bottom:14px">DSR was selected as it provides a systematic, evidence-based framework for constructing and evaluating design artifacts &mdash; suited to AI-integrated system development where the goal is to build a justified solution to a real operational problem.</p>
    <p class="lead ar" style="display:none;margin-bottom:14px">تم اختيار DSR لأنها توفر إطاراً منهجياً قائماً على الأدلة لبناء وتقييم القطع المعمارية &mdash; مناسب لتطوير الأنظمة المدمجة بالذكاء الاصطناعي.</p>

    <!-- 6-Phase Full-Width Horizontal Stepper Grid -->
    <div style="display:grid;grid-template-columns:repeat(6, 1fr);gap:10px;margin-bottom:14px;width:100%">
      
      <!-- Phase 1: Completed -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.9), rgba(12,32,22,0.75));display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--ok);font-family:'JetBrains Mono',monospace">PHASE 01</span>
          <span style="width:16px;height:16px;border-radius:50%;background:rgba(16,185,129,0.2);color:var(--ok);display:inline-flex;align-items:center;justify-content:center;font-size:0.65rem">&check;</span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">Problem Identification</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">تحديد المشكلة</div>
        <span style="font-size:0.62rem;color:var(--ok);font-weight:600;margin-top:4px">Completed</span>
      </div>

      <!-- Phase 2: Completed -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.9), rgba(12,32,22,0.75));display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--ok);font-family:'JetBrains Mono',monospace">PHASE 02</span>
          <span style="width:16px;height:16px;border-radius:50%;background:rgba(16,185,129,0.2);color:var(--ok);display:inline-flex;align-items:center;justify-content:center;font-size:0.65rem">&check;</span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">Solution Objectives</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">أهداف الحل</div>
        <span style="font-size:0.62rem;color:var(--ok);font-weight:600;margin-top:4px">Completed</span>
      </div>

      <!-- Phase 3: Completed -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.9), rgba(12,32,22,0.75));display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--ok);font-family:'JetBrains Mono',monospace">PHASE 03</span>
          <span style="width:16px;height:16px;border-radius:50%;background:rgba(16,185,129,0.2);color:var(--ok);display:inline-flex;align-items:center;justify-content:center;font-size:0.65rem">&check;</span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">Architecture Design</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:700;color:#fff;line-height:1.25">تصميم المعمارية</div>
        <span style="font-size:0.62rem;color:var(--ok);font-weight:600;margin-top:4px">Completed</span>
      </div>

      <!-- Phase 4: Active Highlight -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid var(--s);background:linear-gradient(145deg, rgba(28,8,22,0.95), rgba(10,35,45,0.85));box-shadow:0 0 16px rgba(0,212,255,0.25);display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--s);font-family:'JetBrains Mono',monospace">PHASE 04</span>
          <span style="width:8px;height:8px;border-radius:50%;background:var(--s);box-shadow:0 0 8px var(--s);display:inline-block"></span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:800;color:#fff;line-height:1.25">Prototype Demo</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:800;color:#fff;line-height:1.25">عرض النموذج</div>
        <span style="font-size:0.62rem;color:var(--s);font-weight:800;text-transform:uppercase;letter-spacing:0.5px;margin-top:4px">Active &bull; قيد التقدم</span>
      </div>

      <!-- Phase 5: Planned -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid rgba(255,255,255,0.08);background:linear-gradient(145deg, rgba(28,8,22,0.8), rgba(20,12,22,0.7));display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--t3);font-family:'JetBrains Mono',monospace">PHASE 05</span>
          <span style="width:6px;height:6px;border-radius:50%;background:var(--t3);display:inline-block"></span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:700;color:var(--t2);line-height:1.25">Evaluation</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:700;color:var(--t2);line-height:1.25">التقييم</div>
        <span style="font-size:0.62rem;color:var(--t3);margin-top:4px">Planned</span>
      </div>

      <!-- Phase 6: Planned -->
      <div class="card" style="padding:10px 8px;text-align:center;border:1px solid rgba(255,255,255,0.08);background:linear-gradient(145deg, rgba(28,8,22,0.8), rgba(20,12,22,0.7));display:flex;flex-direction:column;align-items:center;justify-content:space-between;min-height:92px">
        <div style="display:flex;align-items:center;justify-content:space-between;width:100%;margin-bottom:4px">
          <span style="font-size:0.65rem;font-weight:800;color:var(--t3);font-family:'JetBrains Mono',monospace">PHASE 06</span>
          <span style="width:6px;height:6px;border-radius:50%;background:var(--t3);display:inline-block"></span>
        </div>
        <div class="fl en" style="font-size:0.82rem;font-weight:700;color:var(--t2);line-height:1.25">Communication</div>
        <div class="fl ar" style="display:none;font-size:0.82rem;font-weight:700;color:var(--t2);line-height:1.25">التوثيق</div>
        <span style="font-size:0.62rem;color:var(--t3);margin-top:4px">Planned</span>
      </div>

    </div>

    <!-- Bottom Split: Current Phase Status Card (Left) & DSR Blueprint Image Card (Right) -->
    <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:14px;align-items:stretch;width:100%">
      
      <!-- Current Phase Status Card -->
      <div class="card" style="padding:16px 20px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8));display:flex;flex-direction:column;justify-content:center;border-left:3px solid var(--s)">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <span style="font-size:0.75rem;font-weight:800;color:var(--s);text-transform:uppercase;letter-spacing:1px" class="en">DSR EXECUTION MILESTONE</span>
          <span style="font-size:0.75rem;font-weight:800;color:var(--s);letter-spacing:1px;display:none" class="ar">المحطة التنفيذية لمنهجية DSR</span>
        </div>
        <p class="en" style="font-size:0.88rem;color:var(--t1);line-height:1.6;margin:0">
          <strong>Current Phase:</strong> The project has completed Phases 1&ndash;3 (Problem Identification, Solution Objectives, Architecture Design) and is actively progressing through Phase 4 (Prototype Development).
        </p>
        <p class="ar" style="display:none;font-size:0.88rem;color:var(--t1);line-height:1.6;margin:0">
          <strong>المرحلة الحالية:</strong> المشروع أكمل المراحل 1&ndash;3 (تحديد المشكلة، الأهداف، التصميم) وهو يتقدم بنشاط في المرحلة 4 (تطوير النموذج الأولي).
        </p>
      </div>

      <!-- DSR Blueprint Illustration Card -->
      <div class="ill-card" style="margin:0;padding:6px;display:flex;flex-direction:column;justify-content:space-between">
        <div class="ill-frame" style="height:115px" onclick="openImageModal('images/dsr_6phases_methodology.jpg', 'Design Science Research (DSR) 6-Phase Engineering Framework')">
          <img src="images/dsr_6phases_methodology.jpg" alt="DSR 6 Phases Framework" class="ill-img" loading="lazy" style="object-fit:cover;height:115px;width:100%"/>
          <div class="ill-zoom-hint">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            <span>DSR BLUEPRINT ZOOM</span>
          </div>
        </div>
        <div class="ill-caption" style="padding:4px 8px">
          <div class="ill-title" style="font-size:0.75rem">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
            <span class="en">Rigorous 6-Phase Iterative Cycle (Peffers et al.)</span>
            <span class="ar" style="display:none">دورة مراحل DSR التكرارية المعتمدة</span>
          </div>
          <div class="ill-sub">CHAPTER 1 &sect;1.4 &middot; DSR FRAMEWORK</div>
        </div>
      </div>

    </div>

  </div>
  <div class="sn">11 / 21</div>
</section>"""

pattern = re.compile(r'<section\b[^>]*id=["\']s10["\'][^>]*>.*?</section>', re.DOTALL)
if not pattern.search(html):
    raise ValueError("Section s10 not found!")

html = pattern.sub(new_s10, html, count=1)

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Slide 11 (s10) reorganized successfully!")
