import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original content length: {len(content)}")

# =========================================================================
# 1. DEFINE VECTOR SVG ICONS (TASTE-SKILL STANDARD: ULTRA-LIGHT, CRISP, NO EMOJIS)
# =========================================================================

svg_check = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="display:inline-block;vertical-align:middle"><polyline points="20 6 9 17 4 12"/></svg>'
svg_cross = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="display:inline-block;vertical-align:middle"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
svg_sync = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>'
svg_alert = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffd166" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
svg_ban = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>'
svg_shield = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
svg_book = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
svg_pin = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
svg_search = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
svg_file = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>'
svg_tasks = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="display:inline-block;vertical-align:middle"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
svg_gear = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:inline-block;vertical-align:middle"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>'

# Helper badge HTML
badge_done = f'<span style="display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:rgba(16,185,129,0.2);color:var(--ok);margin-right:6px;flex-shrink:0">{svg_check}</span>'
badge_prog = f'<span style="display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:rgba(255,180,0,0.2);color:var(--wa);margin-right:6px;flex-shrink:0">{svg_sync}</span>'
badge_plan = f'<span style="display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:rgba(0,212,255,0.2);color:var(--s);margin-right:6px;flex-shrink:0">{svg_tasks}</span>'

# =========================================================================
# 2. CLEAN UP EMOJIS IN DRAWER & CONTROL PANEL
# =========================================================================

# Drawer Header
content = content.replace('<span>📖</span>', f'<span style="color:var(--s);display:flex;align-items:center">{svg_book}</span>')
content = content.replace('<button class="rd-close" onclick="toggleRefModal()" title="Close References (ESC / R)">✕</button>',
                          f'<button class="rd-close" onclick="toggleRefModal()" title="Close References (ESC / R)">{svg_cross}</button>')

# Drawer JS population
content = content.replace('📍 ${el.loc}', f'{svg_pin} ${{el.loc}}')
content = content.replace('✓ ${isAR ? \'مطابقة تامة 100%\' : \'Exact 100% Match\'}', f'{svg_check} ${{isAR ? \'مطابقة تامة 100%\' : \'Exact 100% Match\'}}')
content = content.replace('✓ 100%', f'{svg_check} 100%')
content = content.replace('📄 <strong>${ref.chapter}</strong>', f'{svg_file} <strong>${{ref.chapter}}</strong>')
content = content.replace('🔍 ${isAR ? \'فتح جدول التدقيق والتطابق الكامل (R)\' : \'Open Detailed Verification Table (R)\'}',
                          f'{svg_search} ${{isAR ? \'فتح جدول التدقيق والتطابق الكامل (R)\' : \'Open Detailed Verification Table (R)\'}}')

# Control panel items
cp_replacements = [
    ('<span>✨</span> <span class="en">Golden Halo</span>', f'<span style="display:flex;align-items:center">{svg_gear}</span> <span class="en">Golden Halo</span>'),
    ('<span>🪞</span> <span class="en">Glass Lift</span>', f'<span style="display:flex;align-items:center">{svg_shield}</span> <span class="en">Glass Lift</span>'),
    ('<span>🔦</span> <span class="en">Spotlight Focus</span>', f'<span style="display:flex;align-items:center">{svg_search}</span> <span class="en">Spotlight Focus</span>'),
    ('<span>📐</span> <span class="en">Precision Line</span>', f'<span style="display:flex;align-items:center">{svg_tasks}</span> <span class="en">Precision Line</span>'),
    ('<div class="cpst">🌌 <span class="en">Dynamic Backgrounds', f'<div class="cpst">{svg_gear} <span class="en">Dynamic Backgrounds'),
    ('<span>🧠</span> <span class="en">Neural AI Mesh</span>', f'<span style="display:flex;align-items:center">{svg_gear}</span> <span class="en">Neural AI Mesh</span>'),
    ('<span>🌊</span> <span class="en">Quantum Waves</span>', f'<span style="display:flex;align-items:center">{svg_sync}</span> <span class="en">Quantum Waves</span>'),
    ('<span>🌌</span> <span class="en">Auroral Curtains</span>', f'<span style="display:flex;align-items:center">{svg_shield}</span> <span class="en">Auroral Curtains</span>'),
    ('<span>✨</span> <span class="en">Cosmic Stardust</span>', f'<span style="display:flex;align-items:center">{svg_gear}</span> <span class="en">Cosmic Stardust</span>'),
    ('<span>🌐</span> <span class="en">Hex Cyber Lattice</span>', f'<span style="display:flex;align-items:center">{svg_tasks}</span> <span class="en">Hex Cyber Lattice</span>'),
    ('<span>💚</span> <span class="en">Cyber Matrix</span>', f'<span style="display:flex;align-items:center">{svg_shield}</span> <span class="en">Cyber Matrix</span>'),
    ('<span>🚀</span> <span class="en">Space Warp</span>', f'<span style="display:flex;align-items:center">{svg_sync}</span> <span class="en">Space Warp</span>'),
    ('<span>🍃</span> <span class="en">Serene 0.5x</span>', f'<span style="display:flex;align-items:center">{svg_sync}</span> <span class="en">Serene 0.5x</span>'),
    ('<span>⚖️</span> <span class="en">Balanced 1x</span>', f'<span style="display:flex;align-items:center">{svg_gear}</span> <span class="en">Balanced 1x</span>'),
    ('<span>🕊️</span> <span class="en">Ultra Slow</span>', f'<span style="display:flex;align-items:center">{svg_shield}</span> <span class="en">Ultra Slow</span>'),
    ('<div class="cpst">👑 <span class="en">Prestige Color Gradients', f'<div class="cpst">{svg_shield} <span class="en">Prestige Color Gradients'),
    ('<div class="cpst">📑 <span class="en">Slide Directory', f'<div class="cpst">{svg_file} <span class="en">Slide Directory'),
    ('<div class="cpst">🔠 <span class="en">Font Scale', f'<div class="cpst">{svg_tasks} <span class="en">Font Scale')
]

for old_str, new_str in cp_replacements:
    content = content.replace(old_str, new_str)

# Slide 16 bullets
content = content.replace('<li class="en">✅ ', f'<li class="en">{badge_done} ')
content = content.replace('<li class="ar" style="display:none">✅ ', f'<li class="ar" style="display:none">{badge_done} ')
content = content.replace('<li class="en">🔄 ', f'<li class="en">{badge_prog} ')
content = content.replace('<li class="ar" style="display:none">🔄 ', f'<li class="ar" style="display:none">{badge_prog} ')
content = content.replace('<li class="en">📋 ', f'<li class="en">{badge_plan} ')
content = content.replace('<li class="ar" style="display:none">📋 ', f'<li class="ar" style="display:none">{badge_plan} ')

# Slide 19 symbols
content = content.replace('<span>⚠️</span>', f'<span style="display:flex;align-items:center">{svg_alert}</span>')
content = content.replace('<span>🚫</span>', f'<span style="display:flex;align-items:center">{svg_ban}</span>')
content = content.replace('<span>🔄</span>', f'<span style="display:flex;align-items:center">{svg_sync}</span>')
content = content.replace('<div style="font-weight:700;color:#fff">🛡️ Human Gate</div>', f'<div style="font-weight:700;color:#fff;display:flex;align-items:center;justify-content:center;gap:4px">{svg_shield} Human Gate</div>')
content = content.replace('✓ <span class="en">', f'{svg_check} <span class="en">')

# Slide 20 headers
content = content.replace('<h3 class="ct en" style="color:var(--ok)">✅ Completed</h3>',
                          f'<h3 class="ct en" style="color:var(--ok);display:flex;align-items:center;gap:6px">{badge_done} Completed</h3>')
content = content.replace('<h3 class="ct ar" style="display:none;color:var(--ok)">✅ المنجز</h3>',
                          f'<h3 class="ct ar" style="display:none;color:var(--ok);align-items:center;gap:6px">{badge_done} المنجز</h3>')

content = content.replace('<h3 class="ct en" style="color:var(--wa)">🔄 In Progress</h3>',
                          f'<h3 class="ct en" style="color:var(--wa);display:flex;align-items:center;gap:6px">{badge_prog} In Progress</h3>')
content = content.replace('<h3 class="ct ar" style="display:none;color:var(--wa)">🔄 قيد التنفيذ</h3>',
                          f'<h3 class="ct ar" style="display:none;color:var(--wa);align-items:center;gap:6px">{badge_prog} قيد التنفيذ</h3>')

content = content.replace('<h3 class="ct en" style="color:var(--s)">📋 Remaining</h3>',
                          f'<h3 class="ct en" style="color:var(--s);display:flex;align-items:center;gap:6px">{badge_plan} Remaining</h3>')
content = content.replace('<h3 class="ct ar" style="display:none;color:var(--s)">📋 المتبقي</h3>',
                          f'<h3 class="ct ar" style="display:none;color:var(--s);align-items:center;gap:6px">{badge_plan} المتبقي</h3>')

# Slide 20 bullet points
content = content.replace('<li>✅ ', f'<li>{badge_done} ')
content = content.replace('<li>🔄 ', f'<li>{badge_prog} ')
content = content.replace('<li>📋 ', f'<li>{badge_plan} ')

print("Successfully replaced all emojis with vector SVG icons!")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved presentation/index.html successfully!")
