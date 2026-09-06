from pathlib import Path
import re

SOURCE = Path('/home/tofdan/.hermes/profiles/gerard/working/formation-guide-source/Astronomie.txt')
OUT = Path('/home/tofdan/Projets_Dev/wiki-oca/docs/formation-guide-astro/sources-integrales')
OUT.mkdir(parents=True, exist_ok=True)

# Pages PDF -> source module. Page numbering follows the printed syllabus pages.
groups = {
    '01-objectifs-du-module': (1, 2, 'Objectifs du module'),
    '02-introduction-a-l-astronomie': (3, 3, 'Introduction à l’astronomie'),
    '03-la-terre': (4, 7, 'La Terre'),
    '04-la-lune-et-ses-effets': (8, 11, 'La Lune et ses effets'),
    '05-systeme-solaire': (12, 18, 'Le Système solaire'),
    '06-distances-dans-lespace': (19, 20, 'Mesurer les distances dans l’espace'),
    '07-les-etoiles': (21, 22, 'Les étoiles'),
    '08-constellations': (23, 25, 'Les constellations'),
    '09-voie-lactee': (26, 27, 'La Voie lactée'),
    '10-nombre-etoiles-univers': (28, 29, 'Le nombre d’étoiles dans l’Univers'),
    '11-pratique-de-terrain': (30, 41, 'Pratique de terrain'),
}

raw_pages = SOURCE.read_text(encoding='utf-8', errors='replace').split('\f')
# The extracted file has cover/front matter before the printed page 1.
# The PDF text extraction creates one form-feed chunk per printed page.
# Chunk 2 is printed page 1; chunk 43 is printed page 42.
pages = {n: raw_pages[n + 1].strip() for n in range(1, 43) if n + 1 < len(raw_pages)}

for slug, (first, last, title) in groups.items():
    blocks = []
    missing = []
    for n in range(first, last + 1):
        if n not in pages:
            missing.append(n)
            continue
        blocks.append(f'## Reprise du document — page {n}\n\n```text\n{pages[n]}\n```')
    status = 'COMPLET' if not missing else 'INCOMPLET — pages manquantes : ' + ', '.join(map(str, missing))
    text = f'''# Source intégrale — {title}\n\n> **Statut de transcription : {status}**\n>\n> Cette page reprend le texte extrait du PDF source `Astronomie.pdf`, édition 2024, sans le remplacer par une synthèse. La mise en page, les illustrations et certains éléments typographiques peuvent différer du PDF original. Le PDF Google Drive reste la référence primaire.\n\n- **Source :** [Astronomie.pdf](https://drive.google.com/file/d/1VKdzcqjsHL7iiYPSFOkPYnqRRlyCM-Fq/view?usp=drivesdk)\n- **Pages reprises :** {first}–{last}\n- **Document éditeur :** Cercles des Naturalistes de Belgique asbl\n\n''' + '\n\n'.join(blocks) + '\n'
    (OUT / f'{slug}.md').write_text(text, encoding='utf-8')

index = '''# Reprises intégrales du guide\n\nCette section contient la transcription complète, module par module, du PDF `Astronomie.pdf`.\n\n## Principe\n\n- Les pages ci-dessous sont la **reprise du contenu source**.\n- Les pages `modules/` sont les **fiches pédagogiques et enrichies**.\n- Les deux niveaux sont volontairement séparés pour permettre la révision fidèle du guide et l’enrichissement documentaire.\n- La mise en page et les illustrations originales du PDF peuvent différer de la transcription textuelle ; le PDF Drive reste la source primaire.\n\n'''
for slug, (_, _, title) in groups.items():
    index += f'- [{title}]({slug}.md)\n'
(OUT / 'index.md').write_text(index, encoding='utf-8')
print(f'pages détectées: {len(pages)}; modules écrits: {len(groups)}')
