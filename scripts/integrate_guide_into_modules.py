from pathlib import Path
import re
import fitz

PDF = Path('/home/tofdan/.hermes/profiles/gerard/working/formation-guide-source/Astronomie.pdf')
ROOT = Path('/home/tofdan/Projets_Dev/wiki-oca')
MODULES = ROOT / 'docs/formation-guide-astro/modules'
RANGES = {
 '01-objectifs-du-module': (1,2), '02-introduction-a-l-astronomie': (3,3),
 '03-la-terre': (4,7), '04-la-lune-et-ses-effets': (8,11),
 '05-systeme-solaire': (12,18), '06-distances-dans-lespace': (19,20),
 '07-les-etoiles': (21,22), '08-constellations': (23,25),
 '09-voie-lactee': (26,27), '10-nombre-etoiles-univers': (28,29),
 '11-pratique-de-terrain': (30,41),
}
MARK='## Contenu complet du guide — reprise structurée'

def clean_page(text, page_no):
    lines=[]
    for raw in text.replace('\r','').splitlines():
        s=re.sub(r'[ \t]+',' ',raw).strip()
        if not s: 
            if lines and lines[-1] != '': lines.append('')
            continue
        if s in {'FORMATION GUIDE-NATURE®','FORMATION GUIDE-NATURE','Introduction à l’astronomie'}: continue
        if re.fullmatch(r'\d+',s): continue
        if s.startswith('Introduction à l’astronomie ') and re.search(r'\d+$',s): continue
        lines.append(s)
    while lines and lines[-1]=='': lines.pop()
    # Preserve readable paragraphs; source page headings remain visible.
    out=[]; para=[]
    for s in lines:
        if s=='':
            if para: out.append(' '.join(para)); para=[]
        else: para.append(s)
    if para: out.append(' '.join(para))
    return '\n\n'.join(out)

def page_text_reading_order(page):
    """Extract a two-column PDF page in human reading order."""
    blocks=[]
    mid=page.rect.width/2
    for b in page.get_text('blocks'):
        x0,y0,x1,y1,text,*_=b
        if y0 < 55 or y1 > page.rect.height-45:
            continue
        if not text.strip():
            continue
        blocks.append((x0,y0,x1,y1,text))
    left=[b for b in blocks if b[0] < mid]
    right=[b for b in blocks if b[0] >= mid]
    # A full-width block belongs in the column where its center falls;
    # retain the natural ordering for pages with no right column.
    if not right:
        ordered=sorted(blocks,key=lambda b:(b[1],b[0]))
    else:
        ordered=sorted(left,key=lambda b:(b[1],b[0]))+sorted(right,key=lambda b:(b[1],b[0]))
    return '\n'.join(b[4] for b in ordered)

doc=fitz.open(PDF)
for slug,(first,last) in RANGES.items():
    path=MODULES/f'{slug}.md'
    original=path.read_text(encoding='utf-8')
    if MARK in original:
        original=original.split(MARK,1)[0].rstrip()+'\n'
    sections=[original, MARK, '', '> Cette partie reprend l’intégralité du texte du guide pour les pages de ce module, réorganisée en paragraphes lisibles. Les ajouts de Gérard sont placés dans les autres sections de la fiche.', '']
    for n in range(first,last+1):
        text=clean_page(page_text_reading_order(doc[n+1]), n)
        sections += [f'### Contenu source — page {n}', '', text, '']
    path.write_text('\n'.join(sections).rstrip()+'\n',encoding='utf-8')
    print(path.name, first,last)
