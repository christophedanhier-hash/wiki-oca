# Fiches Structurées — Documents Sources T600
**Rédacteur :** Ethnographe (Bureau Gérard)  
**Date d'analyse :** 12 juin 2026  
**Source :** Google Drive — `01_SOURCES_BRUTES` (ID: 14D-4vFZiLvfiuCGOmhdMLFUItW6Nl95V)

---

## Fiche 1 — Domotisation Télescope T600.pdf

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Titre** | Domotisation du Télescope T600 |
| **Type** | Document PDF (13 pages, image-based) |
| **Auteur(s)** | Christian Wanlin & Jean-Paul Dumoulin |
| **Date** | 25 mai 2026 |
| **Langue** | Français |

### Concepts clés
- **Architecture système complète** : pilotage via automate **IPX800**, monitoring watchdog sur **Wemos D1 Mini (ESP8266)**
- **Transmission radio NRF24L01** pour l'ouverture sans fil des volets du dôme (cimiers)
- **Cartes Pléiades** : famille de cartes électroniques pour contrôle des moteurs CC (Alcyone-5, Electra-5, Maia-4)
- **Intégration logicielle** : ASCOM, NINA, supervision AnyDesk / Foscam
- **Infrastructure PC** : PC NUC intégré

### Composants matériels mentionnés
| Composant | Rôle / Description |
|-----------|-------------------|
| **IPX800** | Automate central de commande (Ethernet Control System) — 8 sorties relais, entrées analogiques et digitales |
| **Wemos D1 Mini (ESP8266)** | Watchdog alimentation + sonde température DS18B20 |
| **Relais Keyes** | Commande power switch pour IPX800 |
| **DS18B20** | Sonde température (OneWire) |
| **Arduino Uno** | Réception des ordres IPX800 pour cimiers (OG/FG/OD/FD) |
| **Module NRF24L01** | Liaison radio 2.4 GHz entre partie fixe et tournante |
| **Arduino Mega** | Réception côté dôme/batterie pour activation relais moteurs volets |
| **Alcyone-5 (Shield)** | Carte d'alimentation principale — reçoit 12V-24V, régule 12V (drivers) et 9V (Arduino Uno), ventilation requise si >19V |
| **Electra-5 (Motherboard)** | Supporte jusqu'à 2 cartes contrôleurs (MAIA, ATLAS), régulateurs 5V et 3.3V intégrés, port ST-4 autoguidage |
| **Maia-4** | Driver Toshiba TB67H303HC, boucle fermée via encodeur quadrature, tension jusqu'à 24V, courant sortie max 2.7A |
| **Variateur de fréquence** | Rotation dôme, réglé sur f=24.0 Hz |
| **Encodeur Gray Code** | Grayhill 654321 — encodeur de position pour rotation dôme |
| **Switch Home** | Recalage position zéro dôme |
| **Interface Velleman PVM110N** | Conversion des ordres USB du PC en signaux analogiques/logiques pour le variateur (Timer Interval: 60ms) |

### Firmware / Logiciel
- **NINA** (logiciel d'acquisition) — paramètres de géométrie de la monture
- **LesveDomeNet** — pilotage du dôme
- **ASCOM** — plateforme d'intégration
- **AnyDesk** — supervision à distance
- **Foscam** — caméra de supervision

### Spécifications techniques
| Paramètre | Valeur |
|-----------|--------|
| Diamètre coupole | 4500 mm |
| Roue capteur Azimut | 241 mm |
| Nombre de trous (encodeur) | 16 |
| Temps Shutter (cimiers) | 90 s |
| Tolérance position dôme | 10 |
| Position Park | 10 |
| Position Home | 310 |
| Variateur fréquence | 24.0 Hz |
| Timer interval Velleman | 60 ms |
| Dimensions monture (GEM) | Scope N/S: 50mm, E/W: 230mm, U/D: 2250mm |
| Dome Radius (NINA) | 750 mm |
| GEM Axis Length | 44.3 mm |

### Lacunes identifiées
- Aucune information sur les schémas de câblage détaillés (seulement une vue d'architecture)
- Pas de spécifications électriques précises pour les câbles et connecteurs
- Le document est entièrement composé d'images (schémas, diagrammes) — le texte a été obtenu par OCR, quelques détails fins peuvent manquer

### Citations textuelles importantes
> *"Sortie 1 : Rotation Coupole / Sortie 2 : Pilier 20V & Télescope 12V / Sortie 3 : PC NUC T600 / Sortie 4 : Fermeture Cimiers / Sortie 5 : Fermeture Cimiers URGENCE / Sortie 6 : Ouverture Cimiers"*

> *"Alcyone-5 (Shield) : Carte d'alimentation principale. Reçoit entre 12V et 24V. 12V (Drivers) et 9V (Arduino Uno). Ventilation requise si tension > 19V."*

> *"Maia-4 : Driver Toshiba TB67H303HC. Boucle fermée via encodeur quadrature. Tension de service : Jusqu'à 24V. Courant de sortie max : 2.7 A"*

---

## Fiche 2 — Améliorations (Google Doc)

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Titre** | Améliorations |
| **Type** | Document Google Doc (exporté en .docx) |
| **Auteur** | Jean-Paul Dumoulin (JP) |
| **Date** | Non précisée (document de travail) |
| **Langue** | Français |

### Concepts clés
- Document très concis listant les **lacunes critiques** du système actuel
- Met en évidence des **risques matériels** importants

### Procédures décrites
- Aucune procédure — il s'agit d'une **liste de problèmes** (todo/risk register)

### Composants matériels mentionnés
| Composant | Contexte |
|-----------|----------|
| **PC NUC-T600** | Au premier étage, permet l'alimentation de l'IPX800 |
| **PC NUC-T600-TELE** | Alimenté par l'IPX800, pilote le télescope |
| **IPX800** | Alimentation depuis le NUC du 1er étage |

### Lacunes identifiées (ce document en est la source)
1. **Absence de capteurs de fin de course** sur les axes AD/DEC du télescope → risque de collision destructrice
2. **Autoguideur non documenté** → risque pour l'imagerie longue pose sur un télescope de 600mm
3. **Absence de parafoudre type 2** → risque pour l'électronique sensible en cas d'orage

### Spécifications techniques
- Télescope de **600mm** d'ouverture (mentionné dans le contexte)

### Citations textuelles importantes
> *"Correction par rapport à la mémoire le PC NUC-T600 est au premier étage et permet l'alimentation du de l'IPX800, Le PC NUC-T600-TELE est alimenté par l'IPX800 et pilote le télescope."*

> *"Absence de capteurs de fin de course sur les axes AD/DEC du télescope — risque de collision destructrice"*

> *"Autoguideur non documenté — risque pour l'imagerie longue pose sur un télescope de 600mm"*

> *"Absence de parafoudre type 2 — risque pour l'électronique sensible en cas d'orage"*

---

## Fiche 3 — Opérations_T600.pptx

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Titre** | Opérations et Télémétrie Experte du Télescope T600 |
| **Sous-titre** | Édition Harmonisée 2026 — Optimisée pour opérateurs confirmés |
| **Type** | Présentation PowerPoint (11 slides, image-based) |
| **Auteur(s)** | Jean-Paul Dumoulin & Christian Wanlin |
| **Date** | 2026 (Édition Harmonisée) |
| **Langue** | Français |
| **Note** | Document généré/annoté avec NotebookLM |

### Concepts clés
- **Safety first** : approche structurée par niveaux de criticité (Nominal / Alerte / Séquentiel / Criticité Maximale)
- **Matrice diagnostique des niveaux d'intervention matérielle** : classification des risques par type d'action
- **Cartographie réseau complète** : architecture IP des équipements
- **Interverrouillage mécanique absolu** : règle stricte interdisant la rotation avec le chargeur des cimiers branché
- **Sanctuarisation de l'intégrité du matériel** : principe de non-violation des sécurités

### Procédures décrites

#### Séquence d'initialisation et validation d'intégrité
1. Connexion au **T600-NUC-TELE** → Vérifier allumage système, stabilité, température CPU OK
2. Accès IP **192.168.0.237** → Commande ON → Actualiser → Vérifier cohérence timestamp d'allumage
3. Accès IP **192.168.0.238** → Login Admin → Vérifier cohérence Output/Input (aucun relais bloqué, absence de retour fantôme)
4. Vérifier température dôme (DS18B20) pour anomalies thermiques

#### Interverrouillage mécanique absolu avant mouvement
- **Risque majeur** d'arrachement mécanique et de dommages structurels immédiats
- **Câble de charge des cimiers impérativement débranché**
- L'état [CÂBLE BRANCHÉ] interdit catégoriquement toute initialisation de rotation du dôme

#### Diagnostic télémétrique préalable des cimiers
- Tension batterie module (NOMINAL)
- État relais Keyes_SRly (NOMINAL) — pas de collage physique
- Communication NRF24L01 TX/RX (NOMINAL) — absence stricte de perte de paquets
- Détecteur de pluie (NOMINAL) — signal inactif

#### Cinématique des cimiers et boucle de rétroaction active
- Commande OUVERTURE/FERMETURE CIMIERS
- Vérification courant moteur via **capteur ACS712**
- Cohérence fins de course (capteurs GH, GB, DY, DB)
- Surveillance caméra Foscam (latence vidéo < 1s)
- URGENCE : FERMETURE CIMIERS URGENCE → SYSTEM HALT / SAFETY PROTOCOL

#### Autorisation conditionnelle pour la rotation du dôme
- Cimiers physiquement 100% ouverts
- Câble chargeur formellement débranché
- Absence totale d'obstacle interne
- **Télémétrie post-lancement** via LesveDomeNet :
  - Encodeur Grayhill : transitions régulières
  - Position Home : cohérence capteur (310)
  - Vitesse de rotation : stable, sans variation
  - Mécanique : aucun glissement, aucun bruit anormal

#### Anatomie électronique du pilotage de la monture
- Activation : **Pilier 20V & Télescope 12V** (vérifier tension réelle)
- **Alcyone-5** : régulateurs 12V / 9V, contrôle température OK, port ST-4 ordre couleurs conforme
- **Electra-5** : alimentation 5V / 3.3V, contrôle tension stable
- **Maia-4** : driver TB67H303HG, contrôle pas de surchauffe, quadrature correcte, cohérence vitesse/commande, port RJ12 absence faux contacts

#### Procédure de mise en sécurité et extinction logicielle
- **Niveau 1 (Mécanique)** : Fermer les cimiers + rebrancher câble batterie → Vérifier fins de course, absence tension résiduelle sur moteurs
- **Niveau 2 (Cerveau informatique)** : Arrêter T600-NUC-TELE → Extinction complète du système
- **Niveau 3 (Relais)** : IP 192.168.0.238 → Désactiver toutes les sorties → Vérifier cohérence stricte Output/Input
- **Niveau 4 (Énergie)** : IP 192.168.0.237 → Commande OFF → Actualiser → Vérifier D0 (module IPX800 physiquement éteint)

### Composants matériels mentionnés
| Composant | Rôle |
|-----------|------|
| **Capteur ACS712** | Mesure courant moteur cimiers |
| **Capteurs GH, GB, DY, DB** | Fins de course cimiers |
| **Encodeur Grayhill** | Transitions régulières pour position dôme |
| **Caméra Foscam** | Surveillance visuelle (latence < 1s) |
| **NRF24L01** | Liaison radio TX/RX pour cimiers |

### Firmware / Logiciel
- **LesveDomeNet** : lancement et télémétrie post-lancement du dôme
- **NINA** : logiciel d'acquisition (référencé)
- **NotebookLM** : utilisé pour la génération/annotation du document
- **AnyDesk** : connexion distante (mentionné dans la cartographie)

### Réseau (IP)
| Adresse | Équipement |
|---------|------------|
| 192.168.4.201 | Énergie & Environnement (température DS18B20) |
| 192.168.0.237 | Gestion alimentation IPX800 (commande ON/OFF) |
| 192.168.0.238 | Gestion relais E/S (Login Admin requis) |
| (adresse variable) | T600-NUC-TELE (connexion locale ou AnyDesk) |

### Codes / Diagnostics
- **SYS_IP** : identifiant système apparent dans les slides
- **DIAG PORT : 5492** : port de diagnostic mentionné
- **TELEMETRY CODE** : code de télémétrie spécifique (non documenté)

### Spécifications techniques
- **Latence vidéo caméra Foscam** : < 1s
- **Position Home dôme** : 310

### Lacunes identifiées
- **Niveau 4 de l'extinction** (Cerveau informatique) non détaillé
- Codes télémétriques (TELEMETRY CODE) non définis
- Pas de schémas de connexion réseau détaillés
- Absence de mention des spécifications du capteur ACS712 (modèle, calibre)

### Citations textuelles importantes
> *"Risque majeur d'arrachement mécanique et de dommages structurels immédiats."*

> *"L'état [CÂBLE BRANCHÉ] interdit catégoriquement toute initialisation de la rotation du dôme."*

> *"JAMAIS DE ROTATION AVEC LE CHARGEUR DES CIMIERS BRANCHÉ. STOP IMMÉDIAT EN CAS DE VIOLATION."*

> *"Niveau 1 : Mécanique / Niveau 2 : Relais / Niveau 3 : Énergie / Niveau 4 : Cerveau informatique"*

---

## Fiche 4 — T600-Mise-en-route-20260525.pptx

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Titre** | T600 — Mise en route au 26/05/2026 |
| **Type** | Présentation PowerPoint (17 slides) |
| **Auteur(s)** | Jean-Paul Dumoulin & Christian Wanlin |
| **Date** | 26 mai 2026 |
| **Langue** | Français |

### Concepts clés
- **Architecture à deux PC** : T600-NUC (1er étage, alimentation IPX800) et T600-NUC-TELE (pilote le télescope)
- **Batterie cimiers** : toujours en charge → nécessite débranchement avant rotation
- **Double accès** : local (1er étage) ou distant (AnyDesk)
- **Procédure complète** de démarrage et d'extinction, slide par slide

### Procédures décrites

#### A. Mise en route (démarrage)

**Étape 1 — Préparation physique**
1. Enlever le câble de charge des cimiers (batterie toujours en charge)
2. Enlever la bâche du télescope
3. Si pilotage cimiers via IPX800 : mettre tension sur coffret cimier via wifi (192.168.0.236)

**Étape 2 — Connexion au PC T600-NUC**
- Local (1er étage) : connexion directe (psw: `forets`)
- Distant : AnyDesk sur T600-NUC
  - T600-NUC-TELE : AnyDesk 1 041 426 244, psw: `T600NUC2024$#@`
  - T600-NUC : AnyDesk 513 471 809, psw: `T6002024$#@`

**Étape 3 — Alimentation IPX800**
1. Navigateur Edge → CMD-Ipx800-237
2. Cliquer ON sur ligne D0: "IPX800 éteint"
3. Actualiser → confirmation IPX800 allumé

**Étape 4 — Connexion IPX800**
1. Nouvel onglet → Ipx800-238
2. Login: `Admin`, psw: `Oc@2018`
3. Cliquer Out → cliquer les 4 boutons sélectionnés
4. Vérifier : Output = demandes, Input = retour tension (appareil alimenté)

**Étape 5 — Connexion au PC T600-NUC-TELE**
- Direct ou AnyDesk (T600-NUC-TELE : 1 041 426 244, psw: `T600NUC2024$#@`)

**Étape 6 — Caméra Foscam**
1. Démarrer programme **Foscam T6002021**
2. Compte local : login `foscamt600`, psw: `T6002021`
3. Device: FI9831P-T600
4. Compte myfoscam.com : login `jean-paul.dumoulin@skynet.be`, psw: `T6002021$`

**Étape 7 — Vérification réseau**
- Switch wifi dôme T600 distribue :
  - Caméra dôme (Ethernet filaire)
  - Commande IPX800 (wifi)
- Réseau wifi : SSID `wireless2.4G_A84620`, psw: `Admin2021$`

**Étape 8 — Utilisation**
1. Démarrer les applications nécessaires
2. Faire les photos/observations
3. Arrêter les applications avant fermeture

#### B. Extinction

**Étape 1 — Arrêt PC T600-NUC-TELE**
1. Sur l'écran du T600-NUC-TELE : clic Arrêter
2. Perte connexion AnyDesk si travail à distance

**Étape 2 — Connexion sur PC T600-NUC**
1. AnyDesk sur T600-NUC (513 471 809, psw: `T6002024$#@`)
2. Edge → 192.168.0.238 → Décocher les boutons allumés

**Étape 3 — Extinction IPX800**
1. Edge → 192.168.0.237 → Clic OFF → Actualiser
2. Confirmation : "Tout est éteint"

### Composants matériels mentionnés
| Composant | Rôle |
|-----------|------|
| **PC T600-NUC** | 1er étage, alimente l'IPX800, entrée principale OCA |
| **PC T600-NUC-TELE** | Pilote le télescope, alimenté par IPX800 |
| **IPX800** | Automate central (adresses 237 et 238) |
| **Caméra Foscam FI9831P-T600** | Supervision visuelle |
| **Batterie cimiers** | Alimentation des cimiers, toujours en charge |
| **Switch wifi dôme** | Distribution réseau (SSID: wireless2.4G_A84620) |

### Firmware / Logiciel
- **AnyDesk** : connexion à distance
- **Edge** : navigateur pour interface IPX800
- **Foscam T6002021** : visionnage caméra
- **CMD-Ipx800** : page web de contrôle IPX800

### Spécifications techniques / Identifiants
| Élément | Valeur |
|---------|--------|
| AnyDesk T600-NUC-TELE | 1 041 426 244 |
| Mot de passe T600-NUC-TELE | T600NUC2024$#@ |
| AnyDesk T600-NUC | 513 471 809 |
| Mot de passe T600-NUC | T6002024$#@ |
| Login IPX800 | Admin |
| Mot de passe IPX800 | Oc@2018 |
| Login Foscam local | foscamt600 |
| Mot de passe Foscam local | T6002021 |
| Device Foscam | FI9831P-T600 |
| Login myfoscam.com | jean-paul.dumoulin@skynet.be |
| Mot de passe myfoscam.com | T6002021$ |
| SSID wifi dôme | wireless2.4G_A84620 |
| Mot de passe wifi | Admin2021$ |
| Adresse IP IPX800 commande | 192.168.0.237 |
| Adresse IP IPX800 relais | 192.168.0.238 |
| Adresse IP cimiers (wifi) | 192.168.0.236 |
| Mot de passe local 1er étage | forets |

### Lacunes identifiées
- **Absence de capture des 4 boutons à cliquer** (slide 7) — pas de détail sur quels boutons exactement
- Procédure d'arrêt des applications avant fermeture non listée
- Pas de mention de que faire si l'IPX800 ne répond pas
- Quelques slides sans texte (slides 9, 18, 20) — informations visuelles uniquement
- Mot de passe du 1er étage (`forets`) mentionné sans contexte de sécurité

### Citations textuelles importantes
> *"Il y a un PC T600-NUC-TELE pour piloter le T600. Tous les boitiers électriques sont pilotés par l'IPX800."*

> *"Les cimiers sont alimentés par une batterie qui est toujours en charge, Il faut donc enlever le câble de charge avant de faire tourner la coupole."*

> *"La ligne Output reprend les demandes de mise sous tension. La ligne Input renseigne le retour de tension, signifiant que l'appareil est alimenté."*

> *"Le switch wifi du dôme T600 distribue : - La caméra du Dôme du T600 par liaison filaire Ethernet. - La commande de l'IPX800 par wifi"*

---

## Fiche 5 — Domotisation-T600-20260525.pptx

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Titre** | Domotisation T600 : 25 mai 2026 |
| **Type** | Présentation PowerPoint (39 slides) |
| **Auteur(s)** | Jean-Paul Dumoulin & Christian Wanlin |
| **Date** | 25 mai 2026 |
| **Langue** | Français |

### Concepts clés
- **Vue d'ensemble architecturale** de la domotisation complète du T600
- **Plan** : Matériel → Cimiers → Télescope → Rotation Dôme → Logiciel
- **Sécurités** : arrêts d'urgence visualisés par diodes, détecteur de pluie
- **Supervision** : AnyDesk + caméra Foscam

### Procédures décrites
- Aucune procédure pas-à-pas — il s'agit d'une **présentation descriptive** de l'architecture et des composants
- Mention de la supervision du PC NUC à l'aide d'AnyDesk et contrôle visuel via caméra Foscam

### Composants matériels mentionnés (par catégorie)

#### Matériel central
| Composant | Description |
|-----------|-------------|
| **IPX800** | Automate de commande des relais |
| **Boîtier principal** | Avec sonde température |
| **Wemos D1 Mini** | ESP8266 (non nommé explicitement mais implicite) |

#### Cimiers
| Composant | Description |
|-----------|-------------|
| **Carte émettrice commandes cimiers** | Transmission depuis IPX800 |
| **Boîtier commande cimiers** | Sur batterie |
| **Carte réception cimiers** | Ouverture/fermeture |
| **Limiteur de courant + détecteur de pluie** | Protection |

#### Télescope / Monture
| Composant | Description |
|-----------|-------------|
| **Boîtier pilier** | Avec PC NUC dans la porte + chauffage |
| **Contrôle température PC NUC** | Surveillance thermique |
| **Alcyone-5** | Carte d'alimentation/drivers |
| **MAIA-4** | Carte contrôleur moteur |
| **ELECTRA-5** | Carte mère support |
| **Diodes arrêts d'urgence** | Visualisation lors déplacement télescope |
| **Contrôle moteurs** | Système de commande |

#### Rotation Dôme
| Composant | Description |
|-----------|-------------|
| **Moteur réducteur** | Avec switch home |
| **Encodeur Gray Code** | Capteur de position |
| **Variateur de fréquence** | Contrôle vitesse rotation |

### Firmware / Logiciel
- **NINA** : paramètres de géométrie de la monture
- **AnyDesk** : supervision à distance
- **Caméra Foscam** : contrôle visuel

### Spécifications techniques
- PC NUC dans le boîtier pilier avec **chauffage intégré**
- Limiteur de courant + détecteur de pluie (pas de spécifications détaillées)

### Lacunes identifiées
- Très peu de texte sur la majorité des slides (1-2 mots par slide)
- L'essentiel du contenu est **visuel** (photos, schémas, captures d'écran)
- Pas de spécifications électriques précises dans le texte
- Slides 18, 20, 23, 24, 26, 27, 29, 30, 31 : **aucun texte**
- Pas de mention des modèles exacts des moteurs

### Citations textuelles importantes
> *"Commande des relais avec un Ipx800"*

> *"Contrôle de la température du pc Nuc pilotant le T600"*

> *"Visualisation grâce à des diodes, des arrêts d'urgences lors du déplacement du télescope"*

> *"Carte Alcyone-5" / "Carte MAIA-4" / "Carte ELECTRA-5"*

> *"Moteur réducteur, switch home, Encodeur gray code et Variateur de fréquence"*

> *"Logiciel NINA — Géométrie de la monture"*

> *"Réalisation : Christian Wanlin et Jean-Paul Dumoulin. vendredi 25 mai 2026"*



---

## Annexe : Synthèse transversale

### Cartographie réseau complète du T600
| Adresse IP | Équipement | Fonction |
|------------|------------|----------|
| 192.168.0.236 | Cimiers (wifi) | Commande ouverture/fermeture |
| 192.168.0.237 | IPX800 — Alimentation | Commande ON/OFF globale |
| 192.168.0.238 | IPX800 — Relais E/S | Gestion des sorties (login: Admin / Oc@2018) |
| 192.168.4.201 | Énergie & Environnement | Capteur température DS18B20 |
| (variable) | T600-NUC-TELE | PC de pilotage télescope (AnyDesk: 1 041 426 244) |
| (variable) | T600-NUC | PC 1er étage (AnyDesk: 513 471 809) |
| SSID: wireless2.4G_A84620 | Switch wifi dôme | Distribution réseau caméra + IPX800 |

### Niveaux de criticité (matrice Opérations_T600)
| Niveau | Risque | Action |
|--------|--------|--------|
| **Nominal** | Aucune interaction dangereuse | Actions de routine |
| **Alerte** | Risque potentiel si mauvaise séquence | Validation stricte ordre opérations |
| **Séquentiel** | — | Nécessite validation stricte |
| **Criticité Maximale** | Risque mécanique ou électrique immédiat | Arrêt immédiat ou vérification prérequis |

### Checklist des risques identifiés
1. ✅ **Présent et documenté** : rotation dôme, cimiers, IPX800, cartes Pléiades, NINA
2. ⚠️ **Partiellement documenté** : autoguideur (mentionné comme absent/manquant)
3. ❌ **Absent / non traité** : capteurs fin de course AD/DEC, parafoudre type 2
4. ❓ **Non documenté** : modèle projecteur planétarium, version Ubuntu

### Identifiants et mots de passe consolidés
| Service | Identifiant | Mot de passe |
|---------|-------------|-------------|
| IPX800 | Admin | Oc@2018 |
| AnyDesk T600-NUC-TELE | 1 041 426 244 | T600NUC2024$#@ |
| AnyDesk T600-NUC | 513 471 809 | T6002024$#@ |
| Foscam locale | foscamt600 | T6002021 |
| myfoscam.com | jean-paul.dumoulin@skynet.be | T6002021$ |
| WiFi dôme | wireless2.4G_A84620 | Admin2021$ |
| Local 1er étage | — | forets |
| Foscam Device | FI9831P-T600 | — |
