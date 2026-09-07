#!/usr/bin/env python3
from pathlib import Path
import html
import re
import subprocess
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/formation-guide-astro/videos/origines-conte-lumiere.md'
OUT = Path('/home/tofdan/.hermes/profiles/gerard/working/origines-conte-lumiere-document-participants-v3.pdf')
TMP = Path('/tmp/origines-conte-lumiere-pdf')
TMP.mkdir(parents=True, exist_ok=True)
source_html = TMP / 'source.html'
final_html = TMP / 'final.html'
css_file = TMP / 'participants.css'

css = r'''
@page { size: A4; margin: 9mm 10mm 13mm; @bottom-center { content: "Formation guide astro — Origines, un conte de la lumière | " counter(page) " / " counter(pages); font-size: 8pt; color: #667085; } }
* { box-sizing: border-box; }
body { width: 100%; max-width: none; margin: 0; padding: 0; font-family: "DejaVu Sans", Arial, sans-serif; color: #182230; font-size: 11pt; line-height: 1.48; }
h1 { color: #123b5d; font-size: 25pt; page-break-before: always; border-bottom: 2px solid #2b7a9b; padding-bottom: 6pt; margin: 0 0 14pt; }
h1:first-of-type { page-break-before: avoid; }
h2 { color: #155e75; font-size: 18pt; page-break-before: auto; page-break-after: avoid; border-left: 5px solid #e67e22; background: linear-gradient(90deg, rgba(230,126,34,.10), transparent); padding: 7pt 10pt 6pt; margin: 22pt 0 12pt; }
h2:first-of-type { page-break-before: avoid; }
h3 { color: #234e70; font-size: 13pt; page-break-after: avoid; margin-top: 15pt; }
p, ul, ol { margin: 6pt 0 9pt; }
blockquote { background: #eef7fa; border-left: 4px solid #2b7a9b; padding: 8pt 11pt; margin: 10pt 0; page-break-inside: avoid; }
table { width: 100%; max-width: 100%; border-collapse: collapse; margin: 10pt 0 14pt; font-size: 9.2pt; page-break-inside: avoid; }
th { background: #155e75; color: white; font-weight: bold; }
th, td { border: .5pt solid #b8c7d1; padding: 5pt 6pt; vertical-align: top; }
tr:nth-child(even) td { background: #f3f7f9; }
a { color: #155e75; text-decoration: none; }
.content-block { width: 100%; max-width: none; }
.compact-break { page-break-before: avoid; }
.cover { height: 235mm; page-break-after: always; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover h1 { font-size: 29pt; border-bottom: 3px solid #2b7a9b; padding-bottom: 12pt; }
.cover p { color: #52606d; font-size: 14pt; }
nav#TOC { page-break-after: always; font-size: 10pt; }
nav#TOC::before { content: "Sommaire"; display: block; color: #123b5d; font-size: 22pt; font-weight: bold; border-bottom: 2px solid #2b7a9b; padding-bottom: 6pt; margin-bottom: 14pt; }
.video-ref { background: #f3f7f9; border: 1px solid #b8c7d1; padding: 8pt 10pt; border-radius: 4pt; }
'''
css_file.write_text(css, encoding='utf-8')
subprocess.run(['pandoc', str(SOURCE), '--from=markdown', '--standalone', '--toc', '--toc-depth=2', '-o', str(source_html)], check=True)
text = source_html.read_text(encoding='utf-8')
text = re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*>', lambda m: f'<img src="{(SOURCE.parent / m.group(1)).resolve().as_uri()}" alt="{html.escape(m.group(2))}">', text)
text = text.replace('</head>', '<link rel="stylesheet" href="participants.css"></head>')
text = text.replace('<body>', '<body><div class="cover"><h1>Origines, un conte de la lumière</h1><p>Document explicatif pour les participants à la formation de guide astro</p><p>Documentaire ARTE — Big Bang, étoiles, galaxies, trous noirs et vie</p></div>', 1)
final_html.write_text(text, encoding='utf-8')
OUT.parent.mkdir(parents=True, exist_ok=True)
HTML(filename=str(final_html), base_url=str(TMP)).write_pdf(str(OUT), metadata={
    'title': 'Origines, un conte de la lumière — Document explicatif',
    'author': 'Christophe Danhier / Gérard Astro',
    'subject': 'Support participant pour la formation de guide astro',
    'keywords': 'lumière, Big Bang, étoiles, galaxies, trous noirs, formation astro'
})
print(OUT)
print(OUT.stat().st_size)
