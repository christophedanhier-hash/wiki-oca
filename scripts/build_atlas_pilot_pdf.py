#!/usr/bin/env python3
from pathlib import Path
import re
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/formation-guide-astro/fiches-atlas/aigle-fiche-pilote.md'
OUT = Path('/home/tofdan/.hermes/profiles/gerard/working/fiche-pilote-aigle-eleve-corrige.pdf')
TMP = Path('/tmp/fiche-pilote-aigle')
TMP.mkdir(parents=True, exist_ok=True)

text = SOURCE.read_text(encoding='utf-8')

def inline(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def markdown_to_html(src):
    out=[]; in_table=False; in_ul=False
    for raw in src.splitlines():
        line=raw.rstrip()
        if not line.strip():
            if in_ul: out.append('</ul>'); in_ul=False
            if in_table: out.append('</tbody></table>'); in_table=False
            continue
        if line.startswith('> '):
            out.append('<div class="note">%s</div>' % inline(line[2:])); continue
        if line.startswith('# '): out.append('<h1>%s</h1>' % inline(line[2:])); continue
        if line.startswith('## '): out.append('<h2>%s</h2>' % inline(line[3:])); continue
        if line.startswith('### '): out.append('<h3>%s</h3>' % inline(line[4:])); continue
        if line.startswith('- '):
            if not in_ul: out.append('<ul>'); in_ul=True
            out.append('<li>%s</li>' % inline(line[2:])); continue
        if re.match(r'^\d+\. ', line):
            if not in_ul: out.append('<ol>'); in_ul=True
            out.append('<li>%s</li>' % inline(re.sub(r'^\d+\. ', '', line))); continue
        if line.startswith('|'):
            cells=[x.strip() for x in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in cells): continue
            if not in_table:
                out.append('<table><tbody>'); in_table=True
            tag='th' if '<tbody>' in out[-1] else 'td'
            out.append('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in cells)); continue
        if line.startswith('<div class="drawing-box">'):
            out.append('<div class="drawing-box">Dessin de l’élève — placer, numéroter et relier les étoiles</div>'); continue
        if line.startswith('<br>'): out.append('<div class="drawing-space"></div>'); continue
        if line.startswith('---'):
            out.append('<div class="section-break"></div>'); continue
        out.append('<p>%s</p>' % inline(line))
    if in_ul: out.append('</ul>')
    if in_table: out.append('</tbody></table>')
    return '\n'.join(out)

body = markdown_to_html(text)
body = body.replace('<h1>Partie 1 — Fiche élève</h1>', '<div class="student-start"><h1>Partie 1 — Fiche élève</h1></div>')
body = body.replace('<h1>Partie 2 — Corrigé guide</h1>', '<div class="answer-start"><h1>Partie 2 — Corrigé guide</h1><p class="answer-warning">Corrigé réservé à l’animateur ou au formateur.</p></div>')

# Add source images only to the answer section, after the corrected representation heading.
img1 = ROOT / 'docs/assets/formation-guide-astro/atlas/page-001-image-1.png'
img2 = ROOT / 'docs/assets/formation-guide-astro/atlas/page-002-image-1.jpeg'
# The images are copied to a private working location beside the HTML for reliable rendering.
for src in [Path('/home/tofdan/.hermes/profiles/gerard/working/atlas-observation-source/page-001-image-1.png'), Path('/home/tofdan/.hermes/profiles/gerard/working/atlas-observation-source/page-002-image-1.jpeg')]:
    target=TMP/src.name; target.write_bytes(src.read_bytes())
insert = ('<div class="atlas-images"><h3>Illustrations de la source</h3>'
          '<figure><img src="page-001-image-1.png"><figcaption>Carte de l’Aigle — source Atlas, page 1. Crédit à compléter avant diffusion.</figcaption></figure>'
          '<figure><img src="page-002-image-1.jpeg"><figcaption>Illustration d’un objet de l’Aigle — source Atlas, page 2. Crédit à compléter avant diffusion.</figcaption></figure></div>')
body = body.replace('<h2>5. Photographies et illustrations de la source</h2>', insert + '<h2>5. Photographies et illustrations de la source</h2>')

css='''
@page { size: A4; margin: 9mm 10mm 13mm; @bottom-center { content: "Fiche pédagogique — Aigle | " counter(page) " / " counter(pages); font-size: 8pt; color: #667085; } }
* { box-sizing:border-box; }
body { margin:0; width:100%; font-family: DejaVu Sans, Arial, sans-serif; color:#17202a; font-size:10.5pt; line-height:1.4; }
h1 { color:#123b5d; font-size:23pt; border-bottom:2px solid #247ba0; padding-bottom:5pt; margin:0 0 12pt; }
h2 { color:#155e75; font-size:16pt; border-left:5px solid #e67e22; padding:5pt 9pt; margin:18pt 0 9pt; page-break-after:avoid; }
h3 { color:#155e75; font-size:12.5pt; margin:13pt 0 5pt; page-break-after:avoid; }
p { margin:5pt 0; }
ul,ol { margin-top:4pt; }
table { width:100%; border-collapse:collapse; margin:8pt 0 12pt; font-size:8.2pt; page-break-inside:avoid; }
td { border:1px solid #b8c6d1; padding:4pt 5pt; vertical-align:top; }
tr:first-child td { background:#eaf3f7; font-weight:bold; }
.note { background:#fff4e6; border-left:4px solid #e67e22; padding:7pt 9pt; margin:8pt 0; }
.drawing-space { height:15mm; border-bottom:1px solid #9aa7b2; margin:3pt 0; }
.drawing-box { height:105mm; border:1.5px solid #64748b; background:repeating-linear-gradient(0deg, transparent, transparent 13mm, #dbe4ea 13.2mm), repeating-linear-gradient(90deg, transparent, transparent 13mm, #dbe4ea 13.2mm); color:#64748b; padding:5pt; margin:8pt 0 12pt; font-size:8.5pt; }
.student-start { page-break-before:always; }
.student-start h1 { page-break-before:avoid; }
.answer-start { page-break-before:always; }
.answer-start h1 { page-break-before:avoid; }
.answer-warning { background:#fdecec; border:1px solid #d64545; padding:7pt; font-weight:bold; }
.section-break { border-top:1px solid #b8c6d1; margin:12pt 0; }
.atlas-images { page-break-before:always; }
.atlas-images figure { margin:8pt 0 16pt; text-align:center; page-break-inside:avoid; }
.atlas-images img { max-width:100%; max-height:105mm; object-fit:contain; }
figcaption { font-size:8.5pt; color:#536271; margin-top:4pt; }
code { background:#f1f3f5; padding:1pt 3pt; }
'''
html=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'''
html_path=TMP/'fiche.html'; html_path.write_text(html,encoding='utf-8')
HTML(string=html, base_url=str(TMP)).write_pdf(str(OUT))
print(OUT)
