#!/usr/bin/env python3
from pathlib import Path
from weasyprint import HTML

OUT = Path('/home/tofdan/.hermes/profiles/gerard/working/fiche-reponse-aigle.pdf')
TMP = Path('/tmp/fiche-reponse-aigle')
TMP.mkdir(parents=True, exist_ok=True)

css = '''
@page { size: A4; margin: 9mm 10mm 13mm; @bottom-center { content: "Fiche réponse — Aigle | " counter(page) " / " counter(pages); font-size: 8pt; color: #667085; } }
* { box-sizing: border-box; }
body { margin:0; width:100%; font-family: DejaVu Sans, Arial, sans-serif; color:#17202a; font-size:10.5pt; line-height:1.38; }
h1 { color:#123b5d; font-size:23pt; border-bottom:2px solid #247ba0; padding-bottom:5pt; margin:0 0 10pt; }
h2 { color:#155e75; font-size:16pt; border-left:5px solid #e67e22; padding:5pt 9pt; margin:16pt 0 8pt; page-break-after:avoid; }
h3 { color:#155e75; font-size:12.5pt; margin:11pt 0 4pt; page-break-after:avoid; }
p { margin:4pt 0; }
ul,ol { margin-top:3pt; }
table { width:100%; border-collapse:collapse; margin:7pt 0 10pt; font-size:8.3pt; page-break-inside:avoid; }
td { border:1px solid #b8c6d1; padding:4pt 5pt; vertical-align:top; }
tr:first-child td { background:#eaf3f7; font-weight:bold; }
.answer-banner { background:#fdecec; border:1px solid #c83e3e; padding:7pt 9pt; margin-bottom:10pt; font-weight:bold; }
.source-note { background:#fff4e6; border-left:4px solid #e67e22; padding:7pt 9pt; margin:7pt 0; }
.link-box { background:#eaf3f7; border:1px solid #6b9caf; padding:7pt 9pt; margin:7pt 0; }
.figure { height:94mm; border:1.5px solid #64748b; background:repeating-linear-gradient(0deg, transparent, transparent 13mm, #dbe4ea 13.2mm), repeating-linear-gradient(90deg, transparent, transparent 13mm, #dbe4ea 13.2mm); position:relative; margin:7pt 0; }
.star { position:absolute; width:8px; height:8px; background:#111827; border-radius:50%; transform:translate(-50%,-50%); z-index:3; }
.star span { position:absolute; left:11px; top:-5px; z-index:4; background:rgba(255,255,255,.92); padding:0 2px; font-size:9pt; font-weight:bold; color:#123b5d; white-space:nowrap; }
.constellation-lines { position:absolute; inset:0; width:100%; height:100%; z-index:1; }
.legend { font-size:8.5pt; color:#536271; }
.small { font-size:8.8pt; }
''' 

figure = '''<div class="figure">
<div class="star" style="left:34%;top:48%"><span>1 Altaïr</span></div>
<div class="star" style="left:28%;top:39%"><span>2 Tarazed</span></div>
<div class="star" style="left:27%;top:57%"><span>3 Alshain</span></div>
<div class="star" style="left:53%;top:47%"><span>4 δ Aql</span></div>
<div class="star" style="left:61%;top:28%"><span>5 ζ Aql</span></div>
<div class="star" style="left:67%;top:66%"><span>6 η Aql</span></div>
<div class="star" style="left:59%;top:71%"><span>7 λ Aql</span></div>
<div class="star" style="left:78%;top:42%"><span>8 θ Aql</span></div>
<img class="constellation-lines" src="aigle-liaisons.svg" alt="Liaisons corrigées de la constellation de l’Aigle"></div>'''

lines_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none">
<g fill="none" stroke="#123b5d" stroke-width="1.4" stroke-linecap="round">
<line x1="53" y1="47" x2="34" y2="48"/>
<line x1="53" y1="47" x2="61" y2="28"/>
<line x1="53" y1="47" x2="78" y2="42"/>
<line x1="53" y1="47" x2="59" y2="71"/>
<line x1="34" y1="48" x2="27" y2="57"/>
</g></svg>'''

html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{css}</style></head><body>
<h1>Partie 2 — Fiche réponse / corrigé guide</h1>
<div class="answer-banner">Document réservé à l’animateur ou au formateur — à utiliser avec le support papier élève « Aigle ».</div>
<div class="link-box"><strong>Lien avec la fiche élève :</strong> les numéros 1 à 8, les rubriques et les objets sont conservés dans le même ordre. Le guide peut corriger directement le travail de l’élève sans changer de codification.</div>
<h2>1. Identifier la constellation</h2>
<table><tbody>
<tr><td>Rubrique élève</td><td>Réponse attendue</td></tr>
<tr><td>Nom français</td><td><strong>Aigle</strong></td></tr>
<tr><td>Nom latin</td><td><em>Aquila</em></td></tr>
<tr><td>Génitif latin</td><td><em>Aquilae</em></td></tr>
<tr><td>Abréviation officielle</td><td><strong>Aql</strong></td></tr>
</tbody></table>
<p><strong>Date, heure, lieu et conditions du ciel :</strong> réponses propres à la séance d’observation.</p>
<h2>2. Se situer dans le ciel</h2>
<p>La fiche élève demande de retrouver les constellations voisines. Les réponses sont :</p>
<table><tbody><tr><td>Repère demandé</td><td>Réponse</td><td>Rôle pédagogique</td></tr>
<tr><td>La Flèche</td><td><em>Sagitta</em></td><td>Repère au nord de l’Aigle</td></tr>
<tr><td>Hercule</td><td><em>Hercules</em></td><td>Région du Triangle d’été</td></tr>
<tr><td>Le Serpent</td><td><em>Serpens</em></td><td>Limite de la zone nord-est</td></tr>
<tr><td>L’Écu</td><td><em>Scutum</em></td><td>Région riche de la Voie lactée</td></tr>
<tr><td>Le Sagittaire</td><td><em>Sagittarius</em></td><td>Repère vers le centre galactique</td></tr>
<tr><td>Le Capricorne</td><td><em>Capricornus</em></td><td>Repère méridional</td></tr>
<tr><td>Le Verseau</td><td><em>Aquarius</em></td><td>Repère à l’ouest/sud-ouest</td></tr>
<tr><td>Le Dauphin</td><td><em>Delphinus</em></td><td>Petit repère voisin facilement identifiable</td></tr>
</tbody></table>
<h2>3. Corriger le dessin et la numérotation</h2>
<p>Le dessin de référence ci-dessous correspond à la numérotation utilisée dans le tableau de la fiche élève. Il suit la convention de tracé observée sur la carte de l’Atlas : δ Aquilae est le nœud central ; Tarazed (γ) est repérée mais n’est pas reliée artificiellement dans cette convention.</p>
{figure}
<p class="legend">Représentation pédagogique non à l’échelle. Les traits servent à retrouver la figure de l’Aigle ; ils ne représentent pas des liens physiques entre les étoiles.</p>
<table><tbody><tr><td>N° élève</td><td>Désignation</td><td>Nom</td><td>Magnitude de référence</td><td>Correction</td></tr>
<tr><td>1</td><td>α Aql</td><td>Altaïr</td><td>≈ 0,8 — à vérifier selon catalogue</td><td>Étoile-repère principale</td></tr>
<tr><td>2</td><td>γ Aql</td><td>Tarazed</td><td>≈ 2,7 — à vérifier</td><td>Géante orangée apparente</td></tr>
<tr><td>3</td><td>β Aql</td><td>Alshain</td><td>≈ 3,7 — à vérifier</td><td>Compagne visuelle d’Altaïr</td></tr>
<tr><td>4</td><td>δ Aql</td><td>Deneb Okab</td><td>à vérifier</td><td>Centre de la figure</td></tr>
<tr><td>5</td><td>ζ Aql</td><td>Zeta Aql</td><td>à vérifier</td><td>Branche supérieure</td></tr>
<tr><td>6</td><td>η Aql</td><td>Eta Aquilae</td><td>variable</td><td>Céphéide ; ne pas corriger avec une valeur unique</td></tr>
<tr><td>7</td><td>λ Aql</td><td>Lambda Aql</td><td>à vérifier</td><td>Branche inférieure</td></tr>
<tr><td>8</td><td>θ Aql</td><td>Theta Aql</td><td>à vérifier</td><td>Prolongement de la figure</td></tr>
</tbody></table>
<div class="source-note">Les magnitudes ci-dessus sont des valeurs de repérage à vérifier dans une source astronomique actuelle avant validation définitive. La codification élève 1–5 est une échelle pédagogique et ne correspond pas directement à la magnitude apparente.</div>
<h2>4. Corriger la codification de luminosité</h2>
<table><tbody><tr><td>Code élève</td><td>Réponse guide</td><td>Interprétation</td></tr>
<tr><td>1</td><td>Très brillante</td><td>Altaïr est le meilleur exemple dans cette fiche</td></tr>
<tr><td>2</td><td>Brillante</td><td>Étoile immédiatement repérable dans le groupe</td></tr>
<tr><td>3</td><td>Moyenne</td><td>Visible dans un ciel favorable</td></tr>
<tr><td>4</td><td>Faible</td><td>Demande une attention ou un meilleur ciel</td></tr>
<tr><td>5</td><td>Limite</td><td>À rechercher avec un instrument ou sous ciel sombre</td></tr>
</tbody></table>
<h2>5. Corrigé des objets du ciel profond</h2>
<table><tbody><tr><td>Objet</td><td>Nature</td><td>Donnée de l’Atlas</td><td>Message pour l’activité</td></tr>
<tr><td>NGC 6709</td><td>Amas ouvert</td><td>Environ 40 étoiles ; magnitude Atlas 6,70</td><td>Cible d’initiation dans une région riche de la Voie lactée</td></tr>
<tr><td>NGC 6738</td><td>Amas ouvert</td><td>Modeste ; magnitude Atlas 8,30</td><td>Comparer un objet discret avec un amas plus riche</td></tr>
<tr><td>NGC 6755</td><td>Amas ouvert</td><td>Environ 100 étoiles au petit télescope ; magnitude Atlas 7,50</td><td>Montrer l’effet du diamètre de l’instrument</td></tr>
<tr><td>NGC 6756</td><td>Amas ouvert</td><td>Très concentré ; magnitude Atlas 10,60</td><td>Objet plus difficile</td></tr>
<tr><td>NGC 6760</td><td>Amas globulaire</td><td>Magnitude Atlas 9,55 ; diamètre apparent ≈ 2′</td><td>Comparer une structure sphérique dense aux amas ouverts</td></tr>
<tr><td>NGC 6751</td><td>Nébuleuse planétaire</td><td>Distance Atlas ≈ 6 500 a.l.</td><td>Introduire l’enveloppe gazeuse d’une étoile en fin d’évolution</td></tr>
</tbody></table>
<h2>6. Réponses aux questions d’observation</h2>
<ol>
<li><strong>Étoile la plus facile :</strong> Altaïr, repère brillant du secteur.</li>
<li><strong>Groupe reconnaissable :</strong> Altaïr–Tarazed–Alshain, puis les branches de la figure de l’Aigle.</li>
<li><strong>Différence de couleur :</strong> Tarazed apparaît plus orangée qu’Altaïr ; la couleur perçue dépend du contraste, du ciel et de la sensibilité de l’œil.</li>
<li><strong>Forme à l’œil nu :</strong> elle peut être partielle ; le dessin de l’Atlas est un support de repérage, pas une silhouette évidente pour tous les observateurs.</li>
<li><strong>Étoiles qui disparaissent :</strong> les plus faibles, surtout sous pollution lumineuse ou lorsque la transparence diminue.</li>
<li><strong>Instrument :</strong> les amas et nébuleuses faibles demandent généralement des jumelles ou un télescope ; la visibilité dépend du ciel et de l’instrument.</li>
</ol>
<h2>7. Message de conclusion pour le guide</h2>
<p>L’Aigle permet de partir d’un repère simple — Altaïr et ses étoiles voisines — puis d’ouvrir progressivement l’observation vers la Voie lactée et ses objets du ciel profond. Le dessin élève sert à apprendre à regarder ; le corrigé sert à nommer, comparer et expliquer.</p>
<h2>Sources et traçabilité</h2>
<p><strong>Source principale :</strong> <em>Atlas observation.pdf</em>, pages 1–2, fourni par Christophe.</p>
<p><strong>Statut des données :</strong> les mentions « Atlas » reprennent le document source ; les magnitudes et distances doivent être vérifiées avant validation définitive.</p>
</body></html>'''

(TMP/'aigle-liaisons.svg').write_text(lines_svg, encoding='utf-8')
(TMP/'fiche-reponse.html').write_text(html, encoding='utf-8')
HTML(string=html, base_url=str(TMP)).write_pdf(str(OUT))
print(OUT)
