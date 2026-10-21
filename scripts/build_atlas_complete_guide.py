#!/usr/bin/env python3
from pathlib import Path
import json, re, shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pypdf import PdfReader, PdfWriter
import fitz

ROOT=Path(__file__).resolve().parents[1]
WORK=Path('/home/tofdan/.hermes/profiles/gerard/working')
SOURCE_PDF=Path('/home/tofdan/.hermes/profiles/gerard/cache/documents/doc_665f09c14862_Atlas observation.pdf')
MANIFEST=WORK/'atlas-observation-source/manifest.json'
OUT=WORK/'guide-complet-constellations-P1-P2-Atlas-V1.pdf'
DRAFT=WORK/'guide-complet-constellations-P1-P2-Atlas-V1-draft.pdf'
manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
source=PdfReader(str(SOURCE_PDF))
source_doc=fitz.open(str(SOURCE_PDF))

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleFr', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=23, leading=28, textColor=colors.HexColor('#123b5d'), alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name='H1Fr', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor('#123b5d'), spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name='H2Fr', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#155e75'), spaceBefore=7, spaceAfter=5))
styles.add(ParagraphStyle(name='BodyFr', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.3, leading=12, spaceAfter=4))
styles.add(ParagraphStyle(name='SmallFr', parent=styles['BodyText'], fontName='Helvetica', fontSize=7.5, leading=9))
styles.add(ParagraphStyle(name='BoxFr', parent=styles['BodyText'], fontName='Helvetica', fontSize=9, leading=12, backColor=colors.HexColor('#fff4e6'), borderColor=colors.HexColor('#e67e22'), borderWidth=0.6, borderPadding=6, spaceAfter=7))


def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

def page_text(n):
    return clean(source.pages[n-1].extract_text() or '')

def objects(txt):
    return sorted(set(re.findall(r'\b(?:M\s*\d+|NGC\s*\d+|IC\s*\d+|B\d+/?\d*)\b', txt, flags=re.I)), key=lambda x:x.lower())

def footer(canvas, doc):
    canvas.saveState(); canvas.setFont('Helvetica',7); canvas.setFillColor(colors.HexColor('#667085'))
    canvas.drawCentredString(A4[0]/2, 7*mm, f'Guide constellations — Atlas observation | page {doc.page}')
    canvas.restoreState()

def make_custom_pdf():
    doc=SimpleDocTemplate(str(DRAFT), pagesize=A4, rightMargin=10*mm, leftMargin=10*mm, topMargin=10*mm, bottomMargin=14*mm)
    story=[]
    story.append(Paragraph('Guide complet des constellations', styles['TitleFr']))
    story.append(Paragraph('Supports P1/P2 pour l’étude et l’observation — référentiel Atlas observation', styles['H1Fr']))
    story.append(Paragraph('Version V1 de travail — chaque constellation est organisée en fiche élève (P1), fiche réponse/corrigé guide (P2), puis pages originales du référentiel.', styles['BoxFr']))
    story.append(Paragraph(f"Le référentiel source contient {manifest['pages']} pages A4 et {len(manifest['constellations'])} constellations. Les pages originales sont conservées dans le PDF final après chaque corrigé afin de préserver les cartes, photos et notices.", styles['BodyFr']))
    story.append(Paragraph('Mode d’emploi', styles['H2Fr']))
    story.append(Paragraph('Distribuer uniquement les pages P1 aux participants. Conserver P2 et les pages Atlas pour le guide. La numérotation des étoiles doit être adaptée à la figure source de chaque constellation avant l’animation ; les pages Atlas servent de corrigé visuel de référence.', styles['BodyFr']))
    story.append(Spacer(1, 20*mm)); story.append(Paragraph('Sommaire des constellations', styles['H2Fr']))
    data=[[Paragraph('<b>N°</b>',styles['SmallFr']),Paragraph('<b>Constellation</b>',styles['SmallFr']),Paragraph('<b>Pages Atlas</b>',styles['SmallFr'])]]
    for i,e in enumerate(manifest['constellations'],1): data.append([str(i), e['name'], f"{e['start']}–{e['end']}"])
    t=Table(data,colWidths=[15*mm,90*mm,35*mm],repeatRows=1); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b8c6d1')),('VALIGN',(0,0),(-1,-1),'TOP'),('FONTSIZE',(0,0),(-1,-1),8),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)])); story.append(t)
    story.append(PageBreak())
    for idx,e in enumerate(manifest['constellations'],1):
        txt=' '.join(page_text(n) for n in e['pages'])
        obs=objects(txt)
        latin=e['latin']
        # P1 page 1
        story.append(Paragraph(f'P1 — Fiche élève : {e["name"]}', styles['TitleFr']))
        story.append(Paragraph(f'<b>Nom latin :</b> {latin} &nbsp;&nbsp; <b>Élève :</b> ______________________________', styles['BodyFr']))
        story.append(Paragraph('<b>Date :</b> __________________ &nbsp;&nbsp; <b>Heure :</b> __________ &nbsp;&nbsp; <b>Lieu :</b> __________________', styles['BodyFr']))
        story.append(Paragraph('1. Repérer la constellation', styles['H2Fr']))
        story.append(Paragraph('Observe le ciel et utilise les constellations voisines comme repères. Note les conditions du ciel et les premiers jalons que tu identifies.', styles['BodyFr']))
        qdata=[['Élément à noter','Réponse de l’élève'],['Constellation voisine 1','________________________________________'],['Constellation voisine 2','________________________________________'],['Étoile-repère','________________________________________'],['Conditions du ciel','________________________________________']]
        q=Table(qdata,colWidths=[55*mm,115*mm]); q.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b8c6d1')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('FONTSIZE',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),5)])); story.append(q)
        story.append(Paragraph('2. Dessiner et numéroter', styles['H2Fr']))
        story.append(Paragraph('Place les étoiles visibles, numérote-les dans ton ordre d’observation, puis relie uniquement les étoiles qui construisent la figure retenue.', styles['BodyFr']))
        story.append(Table([['Espace de dessin — placer, numéroter et relier les étoiles'],['\n\n\n\n\n\n\n\n\n\n\n\n']],colWidths=[170*mm],rowHeights=[7*mm,105*mm],style=TableStyle([('BOX',(0,0),(-1,-1),.8,colors.HexColor('#64748b')),('INNERGRID',(0,1),(-1,-1),.25,colors.HexColor('#dbe4ea')),('BACKGROUND',(0,1),(-1,1),colors.white),('TEXTCOLOR',(0,0),(-1,0),colors.HexColor('#64748b')),('FONTSIZE',(0,0),(-1,-1),8)])))
        story.append(PageBreak())
        # P1 page 2
        story.append(Paragraph(f'P1 — Fiche élève : {e["name"]} (suite)', styles['TitleFr']))
        story.append(Paragraph('3. Codification de la luminosité', styles['H2Fr']))
        cod=[['Code','Ce que j’observe'],['1 — très brillante','Visible immédiatement'],['2 — brillante','Facile à repérer'],['3 — moyenne','Visible dans un bon ciel'],['4 — faible','Demande une attention particulière'],['5 — limite','À rechercher avec un instrument ou sous ciel sombre']]
        t=Table(cod,colWidths=[45*mm,125*mm]); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b8c6d1')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('FONTSIZE',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),5)])); story.append(t)
        story.append(Paragraph('4. Tableau d’observation', styles['H2Fr']))
        rows=[['N°','Nom / désignation','Couleur','Code 1–5','Œil nu','Jumelles','Remarque']]
        for n in range(1,9): rows.append([str(n),'________________','________','___','oui/non','oui/non','________________'])
        t=Table(rows,colWidths=[10*mm,35*mm,25*mm,20*mm,22*mm,25*mm,33*mm],repeatRows=1); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.3,colors.HexColor('#b8c6d1')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('FONTSIZE',(0,0),(-1,-1),7),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),4)])); story.append(t)
        story.append(Paragraph('5. Objets du ciel profond à rechercher', styles['H2Fr']))
        objrows=[['Objet','Ce que j’observe','Instrument','Difficulté']]+[[o,'________________','________','________'] for o in (obs[:8] or ['Objet 1','Objet 2','Objet 3'])]
        t=Table(objrows,colWidths=[30*mm,75*mm,32*mm,33*mm],repeatRows=1); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.3,colors.HexColor('#b8c6d1')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('FONTSIZE',(0,0),(-1,-1),7),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),4)])); story.append(t)
        story.append(Paragraph('6. Questions pour l’observation', styles['H2Fr']))
        story.append(Paragraph('Quelle étoile est la plus facile à repérer ? Quelle différence de couleur observes-tu ? La figure est-elle évidente à l’œil nu ? Quels objets nécessitent des jumelles ou un télescope ?', styles['BodyFr']))
        story.append(Spacer(1,8*mm)); story.append(Paragraph('Réponses et notes :', styles['BodyFr'])); story.append(Table([['\n\n\n\n']],colWidths=[170*mm],rowHeights=[30*mm],style=TableStyle([('BOX',(0,0),(-1,-1),.6,colors.HexColor('#b8c6d1'))])))
        story.append(PageBreak())
        # P2 page 1
        story.append(Paragraph(f'P2 — Fiche réponse / corrigé guide : {e["name"]}', styles['TitleFr']))
        story.append(Paragraph('Document réservé au guide. Utiliser avec les deux pages P1 précédentes.', styles['BoxFr']))
        story.append(Paragraph('Lien de synchronisation', styles['H2Fr']))
        story.append(Paragraph('Les rubriques P1/P2 sont conservées dans le même ordre. Les numéros d’élèves sont des repères pédagogiques à faire correspondre à la figure originale de l’Atlas.', styles['BodyFr']))
        story.append(Paragraph('Identification et repérage', styles['H2Fr']))
        story.append(Paragraph(f'<b>Réponse :</b> {e["name"]} — {latin}. Pages Atlas : {e["start"]} à {e["end"]}.', styles['BodyFr']))
        story.append(Paragraph('Le guide fait nommer les constellations voisines, l’étoile-repère et les conditions d’observation avant de montrer la solution.', styles['BodyFr']))
        story.append(Paragraph('Étoiles et dessin corrigé', styles['H2Fr']))
        story.append(Paragraph(f'La représentation corrigée complète se trouve sur la page Atlas {e["start"]}, placée immédiatement après cette fiche P2. Elle doit être utilisée pour comparer le dessin de l’élève avec la carte du référentiel.', styles['BoxFr']))
        starrows=[['N°','Désignation / nom','Magnitude','Remarque guide']]
        for n in range(1,9): starrows.append([str(n),'À reporter depuis la carte Atlas','À vérifier','Correspondre au tracé de la source'])
        t=Table(starrows,colWidths=[15*mm,60*mm,35*mm,60*mm],repeatRows=1); t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b8c6d1')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf3f7')),('FONTSIZE',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),5)])); story.append(t)
        story.append(Paragraph('Objets signalés dans le référentiel', styles['H2Fr']))
        story.append(Paragraph(', '.join(obs) if obs else 'Voir directement les pages originales du référentiel.', styles['BodyFr']))
        story.append(Paragraph('Points d’animation', styles['H2Fr']))
        story.append(Paragraph('Faire partir le groupe d’un repère facilement visible, demander un dessin personnel, puis comparer avec la représentation de l’Atlas. Expliquer que la visibilité dépend du ciel, de la hauteur, de la pollution lumineuse et de l’instrument.', styles['BodyFr']))
        story.append(PageBreak())
        # P2 page 2
        story.append(Paragraph(f'P2 — Corrigé guide : {e["name"]} (suite)', styles['TitleFr']))
        preview_path=WORK / ('atlas-preview-%03d.png' % idx)
        pix=source_doc[e['start']-1].get_pixmap(matrix=fitz.Matrix(1.15,1.15), alpha=False)
        pix.save(str(preview_path))
        story.append(Paragraph('Représentation corrigée de référence', styles['H2Fr']))
        story.append(Image(str(preview_path), width=78*mm, height=110*mm))
        story.append(Paragraph(f'Carte Atlas page {e["start"]} — à comparer directement avec le dessin P1. Les liaisons, étoiles et objets sont ceux du référentiel ; la carte complète est reprise ensuite dans les pages originales.', styles['SmallFr']))
        story.append(Spacer(1,4*mm))
        story.append(Paragraph('Données à exploiter dans l’Atlas', styles['H2Fr']))
        excerpt=txt[:4200]
        # avoid too much; source pages follow in full
        story.append(Paragraph(clean(excerpt).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'), styles['SmallFr']))
        story.append(Spacer(1,6*mm))
        story.append(Paragraph(f'<b>Référence complète :</b> pages {e["start"]} à {e["end"]} du PDF original, reproduites immédiatement après cette fiche P2. La première page contient la carte corrigée ; les pages suivantes contiennent les notices et photographies.', styles['BoxFr']))
        story.append(Paragraph('Réponses et vigilance', styles['H2Fr']))
        story.append(Paragraph('Ne pas confondre magnitude intégrée et visibilité réelle d’un objet diffus. Indiquer les données anciennes de l’Atlas comme données à vérifier lorsqu’elles sont utilisées dans une fiche définitive. Les photographies montrent souvent davantage que l’œil à l’oculaire.', styles['BodyFr']))
        story.append(PageBreak())
    doc.build(story,onFirstPage=footer,onLaterPages=footer)

make_custom_pdf()
writer=PdfWriter(); custom=PdfReader(str(DRAFT))
# Interleave each constellation's P1/P2 block with its exact source pages.
# The P2 preview can change pagination, so detect each P1 boundary dynamically.
for p in custom.pages[:2]: writer.add_page(p)
starts=[]
for pos,p in enumerate(custom.pages):
    txt=' '.join((p.extract_text() or '').split())
    if 'P1 — Fiche élève :' in txt and '(suite)' not in txt:
        starts.append(pos)
if len(starts) != len(manifest['constellations']):
    raise RuntimeError(f'P1 boundary count {len(starts)} != constellation count {len(manifest["constellations"])}')
for idx,e in enumerate(manifest['constellations']):
    start=starts[idx]
    end=starts[idx+1] if idx+1 < len(starts) else len(custom.pages)
    for p in custom.pages[start:end]: writer.add_page(p)
    for n in e['pages']: writer.add_page(source.pages[n-1])
with OUT.open('wb') as f: writer.write(f)
print(OUT)
print('custom_pages',len(custom.pages),'source_pages',len(source.pages),'total_pages',len(writer.pages))
