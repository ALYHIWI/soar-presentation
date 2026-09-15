import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for team title cards to be larger and more readable
old_team_css = """.team-title-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  max-width: 900px;
  margin-top: 12px;
  width: 100%;
}
.team-title-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.25s ease;
}
.team-title-card:hover {
  border-color: var(--s);
  background: rgba(0, 212, 255, 0.06);
  transform: translateY(-2px);
}
.team-title-av {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  background: rgba(0, 212, 255, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--s);
  flex-shrink: 0;
}
.team-title-name {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--t1);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.team-title-id {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  color: var(--s);
  letter-spacing: 0.5px;
}"""

new_team_css = """.team-title-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  max-width: 960px;
  margin-top: 14px;
  width: 100%;
}
.team-title-card {
  background: rgba(255, 255, 255, 0.045);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.25s ease;
  backdrop-filter: blur(12px);
}
.team-title-card:hover {
  border-color: var(--s);
  background: rgba(0, 212, 255, 0.08);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 212, 255, 0.15);
}
.team-title-av {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(0, 212, 255, 0.16);
  border: 1px solid rgba(0, 212, 255, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--s);
  flex-shrink: 0;
}
.team-title-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--t1);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.team-title-id {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: var(--s);
  letter-spacing: 0.5px;
  font-weight: 600;
}"""

if old_team_css in content:
    content = content.replace(old_team_css, new_team_css)
    print("Updated team CSS styles.")
else:
    print("Old team CSS not matched verbatim, checking...")

# 2. Build 6 Students Grid Markup
all_6_students_html = """    <div class="team-title-grid">
      <!-- Student 1 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Hizam Mohammed Ali Al-Shajara</div>
          <div class="team-title-name ar" style="display:none">حزام محمد علي الشجرة</div>
          <div class="team-title-id">ID: 202210102478</div>
        </div>
      </div>
      <!-- Student 2 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Hamoud Abdullah Saleh Abu Amrah</div>
          <div class="team-title-name ar" style="display:none">حمود عبد الله صالح أبو عمرة</div>
          <div class="team-title-id">ID: 202310101609</div>
        </div>
      </div>
      <!-- Student 3 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Mohammed Hameed Qasim Mohammed</div>
          <div class="team-title-name ar" style="display:none">محمد حميد قاسم محمد</div>
          <div class="team-title-id">ID: 202310100174</div>
        </div>
      </div>
      <!-- Student 4 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Mohammed Taha Qasim Al-Warafi</div>
          <div class="team-title-name ar" style="display:none">محمد طه قاسم الورافي</div>
          <div class="team-title-id">ID: 202310100461</div>
        </div>
      </div>
      <!-- Student 5 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Marwan Mohammed Saeed Al-Ameer</div>
          <div class="team-title-name ar" style="display:none">مروان محمد سعيد الأمير</div>
          <div class="team-title-id">ID: 202310100177</div>
        </div>
      </div>
      <!-- Student 6 -->
      <div class="team-title-card">
        <div class="team-title-av">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
        </div>
        <div class="team-title-info">
          <div class="team-title-name en">Noah Ahmed Mohammed Maraq</div>
          <div class="team-title-name ar" style="display:none">نوح أحمد محمد مرق</div>
          <div class="team-title-id">ID: 202310100452</div>
        </div>
      </div>
    </div>"""

# Replace old team-title-grid inside section s0
s0_match = re.search(r'(<section\b[^>]*id=["\']s0["\'][^>]*>.*?)(<div class=["\']team-title-grid["\']>.*?</div>\s*</div>)(.*?)(<div class=["\']hl["\'].*?</section>)', content, re.DOTALL)
if s0_match:
    print("Found s0 match with old team-title-grid.")
    content = content[:s0_match.start(2)] + all_6_students_html + content[s0_match.end(2):]
    print("Replaced team-title-grid with all 6 students.")
else:
    print("Direct s0 regex did not match, trying alternative search...")
    # Find start and end of team-title-grid in s0
    pos_grid = content.find('<div class="team-title-grid">')
    if pos_grid != -1:
        pos_grid_end = content.find('<div class="hl"', pos_grid)
        if pos_grid_end != -1:
            content = content[:pos_grid] + all_6_students_html + "\n\n " + content[pos_grid_end:]
            print("Successfully replaced team-title-grid via substring slice.")

# 3. Update SLIDE_REFS[0] to list all 6 students
old_ref_0 = """      {
        elEn: "Student Researchers & Academic Supervisor",
        elAr: "فريق الباحثين والمشرف الأكاديمي",
        loc: "Report Approval Sheet, Page 3",
        textEn: "Prepared by: Mohammed Al-Yahawy, Ahed Al-Huraibi, Moataz Al-Omari, Ammar Al-Awami, Al-Zubair Al-Dhabhani. Supervised by Dr. Raed Saeed.",
        textAr: "إعداد: محمد اليحيوي، عهد الحريبي، معتز العمري، عمار العوامي، الزبير الذبحاني. إشراف: د. رائد سعيد."
      }"""

new_ref_0 = """      {
        elEn: "Student Researchers & Academic Supervisor",
        elAr: "فريق الباحثين والمشرف الأكاديمي",
        loc: "Report Approval Sheet, Page 3",
        textEn: "Prepared by: Hizam Al-Shajara (202210102478), Hamoud Abu Amrah (202310101609), Mohammed Hameed (202310100174), Mohammed Al-Warafi (202310100461), Marwan Al-Ameer (202310100177), Noah Maraq (202310100452). Supervised by Dr. Raed Saeed.",
        textAr: "إعداد الطلاب: حزام الشجرة (202210102478)، حمود أبو عمرة (202310101609)، محمد حميد (202310100174)، محمد الورافي (202310100461)، مروان الأمير (202310100177)، نوح مرق (202310100452). إشراف: د. رائد سعيد."
      }"""

if old_ref_0 in content:
    content = content.replace(old_ref_0, new_ref_0)
    print("Updated SLIDE_REFS[0] with all 6 students.")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved presentation/index.html successfully!")
