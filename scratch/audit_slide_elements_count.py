import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)

print(f"Total slides found: {len(slides)}")

for idx, (sid, content) in enumerate(slides):
    # Check if slide-ref-footer exists
    has_footer = '<div class="slide-ref-footer"' in content
    
    # Lead text
    lead = re.findall(r'<p class="lead en"[^>]*>(.*?)</p>', content, re.DOTALL)
    
    # Cards
    # Cards can be class="card..."
    cards = re.findall(r'<div class="card[^"]*"[^>]*>(.*?)</div>\s*(?=<div class="card|<div class="sb|<div class="stage|<div class="hl|<div class="grid|$)', content, re.DOTALL)
    
    # Stat boxes
    sbs = re.findall(r'<div class="sb"[^>]*>(.*?)</div>\s*</div>', content, re.DOTALL)
    
    # Team title cards (for slide 1)
    team_cards = re.findall(r'<div class="team-title-card"[^>]*>', content)
    
    print(f"Slide {idx+1:02d} ({sid:3s}): Footer={has_footer} | Leads={len(lead)} | Cards={len(cards)} | StatBoxes={len(sbs)} | TeamCards={len(team_cards)}")
