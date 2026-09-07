#!/usr/bin/env python3
from pathlib import Path
import html
import re
import subprocess
import sys
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/formation-guide-astro/constellations-et-objets.md'
OUT = Path('/home/tofdan/.hermes/profiles/gerard/working/constellations-dossier-pedagogique-v3.pdf')
TMP = Path('/tmp/constellations-dossier-pedagogique')
TMP.mkdir(parents=True, exist_ok=True)
MDHTML = TMP / 'source.html'
FINALHTML = TMP / 'final.html'
CSS = TMP / 'print.css'

css = r'''
@page { size: A4; margin: 10mm 10mm 14mm; @bottom-center { content: "Dossier pédagogique — Constellations | " counter(page) " / " counter(pages); font-size: 8pt; color: #667085; } }
* { box-sizing: border-box; }
body { width: 100%; max-width: none; margin: 0; padding: 0; font-family: "DejaVu Sans", Arial, sans-serif; color: #182230; font-size: 11pt; line-height: 1.5; }
h1 { color: #123b5d; font-size: 25pt; page-break-before: always; border-bottom: 2px solid #2b7a9b; padding-bottom: 7pt; margin: 0 0 16pt; }
h1:first-of-type { page-break-before: avoid; }
h2.constellation { color: #155e75; font-size: 20pt; margin-top: 0; padding-top: 0; page-break-before: always; page-break-after: avoid; border-bottom: 2px solid #2b7a9b; padding-bottom: 6pt; }
h2.constellation#grande-ourse-ursa-major-uma { page-break-before: avoid; }
h2 { color: #155e75; font-size: 17pt; margin-top: 20pt; page-break-after: avoid; border-bottom: 1px solid #a9c8d5; padding-bottom: 4pt; }
h3 { color: #234e70; font-size: 13pt; margin-top: 15pt; page-break-after: avoid; }
p, ul, ol { margin: 7pt 0 10pt; }
blockquote { background: #eef7fa; border-left: 4px solid #2b7a9b; padding: 7pt 10pt; margin: 9pt 0; page-break-inside: avoid; }
table { width: 100%; max-width: 100%; border-collapse: collapse; margin: 10pt 0 16pt; font-size: 9pt; page-break-inside: avoid; }
th { background: #155e75; color: white; font-weight: bold; }
th, td { border: 0.5pt solid #b8c7d1; padding: 5pt 6pt; vertical-align: top; }
tr:nth-child(even) td { background: #f3f7f9; }
img { display: block; width: auto; max-width: 100%; max-height: 205mm; height: auto; margin: 12pt auto 16pt; page-break-inside: avoid; }
hr { border: 0; border-top: 1px solid #b8c7d1; margin: 16pt 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt; background: #f1f3f5; padding: 1pt 3pt; }
a { color: #155e75; text-decoration: none; }
.cover { height: 235mm; page-break-after: always; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover h1 { font-size: 29pt; border-bottom: 3px solid #2b7a9b; padding-bottom: 12pt; }
.cover p { color: #52606d; font-size: 14pt; }
nav#TOC { page-break-after: always; font-size: 10pt; }
nav#TOC::before { content: "Sommaire"; display: block; color: #123b5d; font-size: 22pt; font-weight: bold; border-bottom: 2px solid #2b7a9b; padding-bottom: 6pt; margin-bottom: 14pt; }
.drawing-break { page-break-before: always; }
figure { page-break-inside: avoid; margin: 0; }
figure img { max-width: 100%; max-height: 195mm; }
figcaption { text-align: center; color: #52606d; font-size: 8.5pt; }
#sources-de-vérification + ul { columns: 2; column-gap: 14mm; font-size: 9pt; margin-bottom: 12pt; }
#sources-de-vérification + ul li { break-inside: avoid; margin-bottom: 3pt; }
#cartes-orientées-pour-la-belgique-7-septembre-2026 { margin-top: 10pt; }
'''
CSS.write_text(css, encoding='utf-8')

subprocess.run(['pandoc', str(SOURCE), '--from=markdown', '--standalone', '--toc', '--toc-depth=2', '-o', str(MDHTML)], check=True)
text = MDHTML.read_text(encoding='utf-8')
# Resolve Markdown image URLs to local absolute file URLs for WeasyPrint.
def resolve_image(m):
    alt, src = m.group(1), m.group(2)
    if src.startswith('http'):
        return m.group(0)
    path = (SOURCE.parent / src).resolve()
    return f'<img src="{path.as_uri()}" alt="{html.escape(alt)}">'
text = re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*>', lambda m: f'<img src="{(SOURCE.parent / m.group(1)).resolve().as_uri()}" alt="{html.escape(m.group(2))}">', text)
# Pandoc emits title metadata; add print stylesheet and document subtitle.
text = text.replace('</head>', '<link rel="stylesheet" href="print.css"></head>')
text = text.replace('<body>', '<body><div class="cover"><h1>Dossier pédagogique — Constellations</h1><p>Support de formation, d’impression et d’animation astronomique</p><p>Grande Ourse · Hercule · Céphée et neuf constellations supplémentaires</p></div>', 1)
constellation_ids = ['grande-ourse-ursa-major-uma','hercule-hercules-her','céphée-cepheus-cep','petite-ourse-ursa-minor-umi','aigle-aquila-aql','dragon-draco-dra','persée-perseus-per','cygne-cygnus-cyg','andromède-andromeda-and','cassiopée-cassiopeia-cas','pégase-pegasus-peg','bouvier-boötes-boo']
for cid in constellation_ids:
    text = text.replace(f'<h2 id="{cid}">', f'<h2 class="constellation" id="{cid}">')
# Do not force a page before each drawing: keep the constellation title, locating text and drawing together when it fits.
FINALHTML.write_text(text, encoding='utf-8')
OUT.parent.mkdir(parents=True, exist_ok=True)
HTML(filename=str(FINALHTML), base_url=str(TMP)).write_pdf(str(OUT), metadata={
    'title': 'Dossier pédagogique — Constellations — Version aérée',
    'author': 'Christophe Danhier / Gérard Astro',
    'subject': 'Constellations, étoiles principales, magnitudes et objets du ciel profond',
    'keywords': 'astronomie, constellations, formation, animation'
})
print(OUT)
print(OUT.stat().st_size)
