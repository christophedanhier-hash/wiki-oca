# Les 8 agents du Bureau Gérard

Le Bureau Gérard réunit **6 agents spécialistes** (dont 1 orchestrateur)
et **2 skills Support transverses** partagés avec les autres bureaux du cabinet
virtuel. Voici leur description détaillée.

---

## Orchestrateur

### `orchestrateur-gerard` — Gérard (alias Gérard)

> *Chef d'équipe du Bureau Gérard — coordination & livraison*

**Alias :** Gérard

**Rôle :** Gérard est l'orchestrateur principal du Bureau Gérard. Il combine
deux fonctions :

1. **Coordination des 5 agents spécialistes** (ethnographe, astro-optique,
   hardware, firmware, redacteur-technique) pour produire un corpus documentaire
   cohérent.
2. **Interface unique du pilote** : cadrage de la chaîne documentaire, arbitrage
   des divergences entre experts, contrôle qualité transverse, livraison finale.

**Principe fondamental :** Gérard ne décide jamais du fond technique et
n'implémente jamais. Il coordonne la production documentaire et garantit la
traçabilité de chaque donnée à sa source.

**Quand l'utiliser :** construction de documentation d'équipement technique,
assemblage d'un manuel utilisateur, production d'une fiche de maintenance,
lancement d'un cycle ethnographe → experts → rédacteur.

**Icône :** 📚

---

## Agents spécialistes (les 5 experts métier)

### `ethnographe` — The Interviewer

> *Extracteur de connaissance — traducteur du tacite vers le structuré*

**Alias :** The Interviewer

**Rôle :** Traduit les discussions informelles, notes manuscrites, schémas sur
un coin de table, photos de montages et souvenirs des spécialistes en données
brutes structurées, prêtes à être consommées par les autres agents. Posture
d'enquêteur systématique, neutre, factuelle : n'invente aucune donnée et marque
toute information manquante comme lacune.

**Position dans le cycle :** toujours en **amont** — sa sortie alimente
l'ensemble du Bureau Gérard.

**Quand l'utiliser :** extraction de connaissance tacite, structuration
d'entretien, nettoyage de transcription, décodage de schéma sur photo,
construction de fiche composants à partir d'échange oral.

!!! tip "Toujours mobiliser en premier"
    `ethnographe` est systématiquement mobilisé en entrée de cycle quand
    l'information est portée par un expert humain.

---

### `astro-optique` — The Astronomer-Physicist

> *Référent scientifique — optique, mécanique céleste, astronomie de position*

**Alias :** The Astronomer-Physicist

**Rôle :** Garantit que la documentation technique respecte les lois de
l'optique géométrique et physique ainsi que de l'astronomie de position : mise
en station, suivi sidéral, compensation de la rotation terrestre, backlash
mécanique, erreur périodique. Valide l'intégrité conceptuelle des solutions,
rédige les procédures d'alignement / collimation / calibrage et traduit la
physique pour un public technique non expert.

**Position dans le cycle :** validation **transverse** — à mobiliser dès
qu'une procédure touche à l'alignement, la collimation, le suivi sidéral ou
les tolérances.

**Quand l'utiliser :** validation d'une procédure de mise en station,
rédaction de procédure de collimation, vérification de cohérence optique,
explication du suivi sidéral, calcul de tolérance de pointage.

---

### `hardware` — The Hardware Specialist

> *Référent électronique-électricité — câblage, alimentation, BOM, protections*

**Alias :** The Hardware Specialist

**Rôle :** Documente l'architecture matérielle, la distribution d'énergie
(DC/AC), la protection des circuits, la connectique et les nomenclatures (BOM)
de l'équipement cible. Agit comme la référence unique du Bureau Gérard pour
toute question touchant au câblage, à l'alimentation, aux protections et aux
connecteurs physiques. Évalue l'obsolescence et propose des remplacements de
composants.

**Position dans le cycle :** **croisement** — en appui de la chaîne de
validation matérielle entre extraction (ethnographe) et assemblage
(redacteur-technique).

**Quand l'utiliser :** documentation d'un schéma de câblage, rédaction de
BOM, vérification de distribution d'alimentation, audit de protection de
circuit, identification de composants obsolètes, arbre de diagnostic
électrique.

---

### `firmware` — The Firmware Expert

> *Systèmes embarqués — analyse de code C/Arduino/ESP32, rétro-ingénierie*

**Alias :** The Firmware Expert

**Rôle :** Analyse le code des microcontrôleurs (Arduino, ESP32, AVR),
documente la logique algorithmique (pointage, suivi sidéral, contrôle moteur,
gestion des interruptions) et anticipe la maintenance logicielle. Cartographie
I/O, identification de la dette technique, propositions de refactorisation ou
de migration. Trace chaque assertion à sa source (ligne de code, datasheet,
entretien, comportement observé).

**Position dans le cycle :** **croisement** — en appui de la chaîne de
validation logicielle entre extraction (ethnographe) et assemblage
(redacteur-technique).

**Quand l'utiliser :** analyse d'un fichier `.ino`, documentation d'un
firmware, explication d'une logique de suivi sidéral, cartographie I/O,
identification de bugs Arduino, audit de bibliothèque tierce, préparation de
migration ESP32.

---

### `redacteur-technique` — The Lead Technical Writer

> *Architecte documentaire — assemblage final, harmonisation, mise en page*

**Alias :** The Lead Technical Writer

**Rôle :** Assemble, harmonise et met en page la documentation technique finale
(fichiers Markdown `.md`, manuels utilisateur, fiches de maintenance, notes
techniques) à partir des contributions des autres agents du Bureau Gérard.
Architecte rédactionnel du corpus : normalise la syntaxe, homogénéise la
terminologie, fusionne les contributions hétérogènes en un récit cohérent et
navigable. Garantit la préservation des catégories (faits validés / sous réserve
/ lacunes) héritées des agents amont.

**Position dans le cycle :** **aval terminal** — reçoit les contributions de
tous les autres agents et produit le livrable final.

**Quand l'utiliser :** assemblage de documentation technique, production d'un
manuel utilisateur, rédaction d'une fiche de maintenance, harmonisation d'un
corpus Markdown, consolidation des contributions de plusieurs agents techniques.

!!! tip "Toujours mobiliser en fin de cycle"
    `redacteur-technique` est systématiquement mobilisé en sortie pour
    consolider les contributions des autres agents en un corpus cohérent.

---

## Skills Support transverses (partagés avec Bureau Robert et Bureau Sophie)

Ces skills ne sont **pas** des agents dédiés du Bureau Gérard. Ils sont
mobilisables par n'importe quel bureau du cabinet virtuel ou directement
par le pilote.

### `secretariat`

> *Assistant de secrétariat virtuel — plume administrative et lecture des flux*

**Rôle :** Prend en charge le geste rédactionnel quotidien et la lecture des
flux entrants : rédaction de mails, notes de service, comptes-rendus, rapports,
synthèses de messagerie et de conversations Teams. Adapte automatiquement le
ton, le format et le canal selon le destinataire. Couvre FR principalement,
NL et EN si demandé.

**Dans le cycle Bureau Gérard :** pour le mail d'accompagnement d'un manuel,
la note de service annonçant une nouvelle version, le CR de réunion de revue
documentaire, la relance d'un expert sollicité par `ethnographe`, la demande
d'accès à un document.

**Distinction clé :** `secretariat` couvre les **gestes courts**
(mails, notes, CR) ; `redacteur-technique` produit le **corpus documentaire
long** (manuels, fiches, notes techniques).

---

### `formateur`

> *Formateur virtuel — conception de parcours pédagogiques structurés*

**Rôle :** Conçoit et délivre des cours structurés progressifs sur tout sujet.
Construit un parcours pédagogique complet : objectifs d'apprentissage,
prérequis, théorie, exemples concrets, exercices pratiques, évaluation et
ressources pour aller plus loin. Adapte le format à la demande (réponse inline,
document Word, parcours multi-sessions).

**Dans le cycle Bureau Gérard :** pour transposer un livrable documentaire en
module pédagogique : formation des mainteneurs à partir d'une fiche de
maintenance, parcours d'apprentissage construit sur un manuel utilisateur,
montée en compétence des opérateurs d'équipement (T600).

**Distinction clé :** `formateur` s'appuie sur les livrables déjà produits
par `redacteur-technique` ; il ne réécrit jamais le manuel source.

---

## Tableau récapitulatif

| # | Agent | Alias | Périmètre | Phase du cycle |
|---|-------|-------|-----------|:--------------:|
| 1 | `orchestrateur-gerard` | Gérard | Coordination globale, cadrage, livraison | Pilotage |
| 2 | `ethnographe` | The Interviewer | Extraction de connaissance tacite | Amont |
| 3 | `astro-optique` | The Astronomer-Physicist | Validation scientifique optique/astronomique | Validation |
| 4 | `hardware` | The Hardware Specialist | Électronique, câblage, BOM, protections | Croisement |
| 5 | `firmware` | The Firmware Expert | Systèmes embarqués, code, I/O | Croisement |
| 6 | `redacteur-technique` | The Lead Technical Writer | Assemblage, harmonisation, livrable final | Aval |
| ⬜ | `secretariat` *(support)* | — | Geste secrétarial court | Transverse |
| ⬜ | `formateur` *(support)* | — | Transposition pédagogique | Transverse |

---

> *Documentation technique — production assistée par le Bureau Gérard*
