# Formation Opérateur — Télescope T600

!!! tip "Enrichissements issus de l'analyse Cowork"
    Cette formation a été enrichie avec les apports de l'analyse Cowork (Microsoft Copilot) :

    - ✅ **Objectifs SMART** détaillés par module
    - ✅ **QCM** 10 questions avec corrigé (annexe)
    - ✅ **Annexe formateur** avec pièges classiques
    - ✅ **Analyse des risques** avec coûts de résolution

    Voir [l'analyse comparative](../cowork/comparative.md) et [la présentation Cowork](../cowork/index.md).

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **Version** | 1.1 |
| **Date** | 12 juin 2026 |
| **Rédacteur** | Rédacteur Technique (Bureau Gérard) |
| **Audience** | Opérateurs débutants et intermédiaires |
| **Durée estimée** | 1 journée (théorie + pratique) |
| **Prérequis** | Notions de base en astronomie, utilisation d'un PC |

---

## Objectifs pédagogiques (SMART)

| Critère | Objectif |
|---------|----------|
| **S** — Spécifique | Exécuter la séquence complète de mise en route et d'extinction du T600, de la vérification météo au rebranchement de la batterie |
| **M** — Mesurable | Réaliser les 8 étapes clés (préparation physique, IPX800 .237, IPX800 .238, connexion télé, Foscam, diagnostic, cimiers, rotation) sans erreur d'ordre |
| **A** — Atteignable | Oui — après démonstration par le formateur et mise en situation encadrée |
| **R** — Réaliste | Adapté aux opérateurs OCA (tout niveau) sans prérequis technique avancé |
| **T** — Temporel | Validé en fin de session de 3h par une mise en situation complète notée |

**Objectif principal :** À l'issue de cette formation, l'opérateur sera capable de **mettre en route, utiliser et éteindre le T600 en autonomie**, en respectant les consignes de sécurité et l'ordre validé des opérations.

---

## Module 1 : Présentation du T600

### 1.1 Qu'est-ce que le T600 ?

Le **T600** est un télescope astronomique installé à l'**Observatoire Centre Ardennes (OCA)**. C'est un instrument de **600 mm d'ouverture** — ce qui signifie qu'il capte environ **7 300 fois plus de lumière** que l'œil humain.

**Caractéristiques principales :**
- **Ouverture :** 600 mm ✅
- **Monture :** Équatoriale allemande (GEM)
- **Dôme :** 4 500 mm de diamètre, motorisé
- **Domotisation :** Pilotage complet via automate IPX800
- **Supervision :** Caméra Foscam + AnyDesk (télétravail possible)

> ⚠️ **Information manquante :** Le type optique exact (Newton, Cassegrain, Ritchey-Chrétien...) et la focale du télescope ne sont pas connus à ce jour. Un relevé sur site est nécessaire avant d'utiliser l'instrument pour des travaux scientifiques. Consultez votre référent technique.

### 1.2 Que permet-il de faire ?

| Usage | Possible ? | Conditions |
|-------|:----------:|------------|
| Observation visuelle | ✅ Oui | Nécessite un oculaire adapté |
| Astrophotographie lunaire/planétaire | ⚠️ Partiel | Sans autoguideur, poses limitées |
| Imagerie ciel profond (nébuleuses, galaxies) | ❌ Limitée | Nécessite autoguideur + mise en station |
| Pilotage à distance | ✅ Oui | Via AnyDesk + Foscam |

### 1.3 Sécurité — Règles d'or

> **RÈGLE #1 : JAMAIS de rotation du dôme avec le câble de charge des cimiers branché.**
> **RÈGLE #2 : Toujours vérifier que les cimiers sont 100% ouverts avant de faire tourner le dôme.**
> **RÈGLE #3 : En cas d'orage, exécuter la procédure d'extinction complète immédiatement.**
> **RÈGLE #4 : Ne jamais forcer un mouvement mécanique — si ça coince, arrêter et diagnostiquer.**

---

## Module 2 : Architecture et composants

### 2.1 Vue d'ensemble simplifiée

```
┌─────────────────────────────────────────────────────────────────┐
│                        LE SYSTÈME T600                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    Commande     ┌──────────────┐               │
│  │ VOUS (ici)  │ ──────────────→│ 2 PCs NUC     │               │
│  │ (opérateur) │ ←──────────────│ (AnyDesk)     │               │
│  └─────────────┘                 └──────┬───────┘               │
│                                         │                        │
│         ┌───────────────────────────────┼───────────────┐        │
│         │                               │               │        │
│         v                               v               v        │
│  ┌────────────┐              ┌──────────────────┐               │
│  │  IPX800    │              │ Cartes Pléiades  │               │
│  │(Automate)  │              │ (Alcyone/Electra │               │
│  │  8 relais  │              │  /Maia)          │               │
│  └─────┬──────┘              └────────┬─────────┘               │
│        │                              │                          │
│        v                              v                          │
│  ┌────────────┐              ┌──────────────────┐               │
│  │  Cimiers   │              │  Monture GEM     │               │
│  │  (volets)  │              │  + Télescope     │               │
│  │  + Dôme    │              │  (AD/DEC)        │               │
│  └────────────┘              └──────────────────┘               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Les composants clés que vous devez connaître

| Composant | À quoi ça sert ? | Où ça se trouve ? |
|-----------|-----------------|-------------------|
| **IPX800** | Automate qui commande tous les relais (alimentation, cimiers, rotation) | Armoire électrique (adresses 192.168.0.237 et .238) |
| **PC T600-NUC** | PC du 1er étage — alimente l'IPX800 | 1er étage de l'observatoire |
| **PC T600-NUC-TELE** | PC qui pilote le télescope (NINA, LesveDomeNet) | Près de la monture ou accessible via AnyDesk |
| **Caméra Foscam** | Supervision visuelle du dôme | Fixée dans le dôme, vue sur l'ensemble |
| **Cimiers** | Volets du dôme — s'ouvrent et se ferment via commande radio | Sur le dôme (partie tournante) |
| **Variateur de fréquence** | Contrôle la vitesse de rotation du dôme | Armoire électrique (réglé à 24.0 Hz) |
| **Encodeur Grayhill** | Capteur de position du dôme (lecture par LesveDomeNet) | Sur l'axe de rotation du dôme |
| **Batterie cimiers** | Alimente la partie tournante (toujours en charge) | Sur le dôme, côté tournant |

### 2.3 Les logiciels que vous utiliserez

| Logiciel | Rôle | Où ça tourne |
|----------|------|:------------:|
| **NINA** | Acquisition d'images, pointage du télescope | T600-NUC-TELE |
| **LesveDomeNet** | Pilotage de la rotation du dôme | T600-NUC-TELE |
| **IPX800 (interface web)** | Commande des relais (alimentation, cimiers) | Navigateur vers 192.168.0.237/.238 |
| **Foscam** | Visualisation caméra de supervision | T600-NUC-TELE ou T600-NUC |
| **AnyDesk** | Connexion à distance aux PCs | Votre PC distant |

### 2.4 Comprendre la sémantique Output / Input de l'IPX800

L'interface web de l'IPX800 (192.168.0.238) distingue deux types de lignes essentielles à comprendre :

| Ligne | Signification | Exemple concret |
|-------|---------------|-----------------|
| **Output** (Sortie) | Ce que l'IPX800 **commande** — l'ordre envoyé à l'équipement | Vous cliquez ON sur S6 → Output S6 = ON (ordre d'ouverture des cimiers) |
| **Input** (Entrée) | Ce que l'IPX800 **reçoit** — le retour d'état des équipements | Si le moteur des cimiers est bien sous tension → Input S6 = ON (confirmation) |

**Règle fondamentale :** `Output` et `Input` doivent toujours correspondre.

| Situation | Interprétation | Action |
|-----------|----------------|--------|
| ✅ Output=ON **et** Input=ON | L'équipement est correctement alimenté | Continuer |
| ❌ Output=ON **mais** Input=OFF | Problème : fusible, câble, relais ou équipement défectueux | **Ne pas continuer** — diagnostiquer avant |
| ❌ Output=OFF **mais** Input=ON | Fuite de courant ou relais collé | **Intervention technique requise** |

**Exemple concret — Cimiers (S4, S5, S6) :**
```
S6 (Ouverture)      : Output=ON  →  Input doit passer ON  (moteur sous tension)
S5 (Urgence ferm.)  : Output=ON  →  Input doit passer ON
S4 (Fermeture)      : Output=ON  →  Input doit passer ON
```

> 💡 **Astuce diagnostic :** L'écart Output/Input est votre **premier indicateur de panne**. Avant d'appeler le support, vérifiez toujours ce couple sur l'interface .238. Un Output sans Input = un problème électrique entre l'automate et l'équipement.

---

## Module 3 : Démarrage pas-à-pas

### 3.1 Avant de commencer — Vérifications

- [ ] La météo est favorable (pas de pluie annoncée, vent modéré)
- [ ] L'observatoire est accessible
- [ ] Vous avez les mots de passe à portée de main (voir Aide-mémoire en annexe)

### 3.2 Procédure de démarrage

#### Étape 1 — Préparation physique
```
1. Débrancher le câble de charge des cimiers
   → La batterie des cimiers est toujours en charge.
   → ⚠️ NE SURTOUT PAS FAIRE TOURNER LE DÔME AVEC LE CÂBLE BRANCHÉ.
   → Risque : arrachement mécanique, dommages structurels.

2. Enlever la bâche du télescope

3. (Optionnel) Mettre tension sur coffret cimier via wifi si pilotage IPX800
   → Adresse : 192.168.0.236
```

#### Étape 2 — Connexion au PC T600-NUC (1er étage)
```
Option A — Sur place :
   Allumer le PC, mot de passe local : forets

Option B — À distance :
   AnyDesk → saisir 513 471 809 → mot de passe : T6002024$#@
```

#### Étape 3 — Alimentation IPX800
```
1. Ouvrir un navigateur Edge (ou autre)
2. Aller sur http://192.168.0.237 (CMD-Ipx800-237)
3. Cliquer sur le bouton ON de la ligne D0
   → Le statut passe de "IPX800 éteint" à ...
4. Actualiser la page
   → ✅ Vérifier que le module est bien allumé
```

#### Étape 4 — Activation des sorties IPX800
```
1. Nouvel onglet → http://192.168.0.238
2. Login : Admin  |  Mot de passe : Oc@2018
3. Cliquer sur "Out" → activer les 4 boutons (sorties S1 à S6)
   [A CONFIRMER : quels boutons exactement — à vérifier sur l'interface réelle]
4. Vérifier :
   → Ligne OUTPUT : affiche ce que vous avez demandé
   → Ligne INPUT : montre que les appareils sont alimentés
   (Si un input ne correspond pas, il y a un problème)
```

#### Étape 5 — Connexion au PC T600-NUC-TELE
```
Option A — Sur place (si à côté du télescope) : connexion directe
Option B — À distance : AnyDesk → 1 041 426 244 → mot de passe : T600NUC2024$#@
```

#### Étape 6 — Caméra Foscam
```
1. Démarrer le programme "Foscam T6002021"
2. Compte local : login = foscamt600 / mot de passe = T6002021
3. Sélectionner le device : FI9831P-T600
4. (Optionnel) Compte cloud : login = jean-paul.dumoulin@skynet.be
   mot de passe = T6002021$
```

#### Étape 7 — Diagnostic préalable (télémétrie)
```
Avant toute action sur les cimiers ou le dôme, vérifier :

☐ Tension batterie cimiers → NOMINALE
☐ Relais Keyes_SRly → NOMINAL (pas collé)
☐ Communication NRF24L01 TX/RX → NOMINALE (pas de perte de paquets)
☐ Détecteur de pluie → NOMINAL (signal inactif)
☐ Température dôme → pas d'anomalie thermique
  (Voir 192.168.4.201 pour la température DS18B20)
```

### 3.3 Procédure d'ouverture des cimiers

```
1. Commande : activer la sortie S6 de l'IPX800 (Ouverture Cimiers)
2. Pendant l'ouverture (~90 secondes) :
   - Surveiller le courant moteur (ACS712)
   - Vérifier les capteurs de fin de course (GH, GB, DY, DB)
   - Regarder la caméra Foscam (latence < 1 seconde)
3. ✅ Attendre que les cimiers soient physiquement 100% ouverts
```

**Si problème :**
- Activer S5 (Fermeture Cimiers URGENCE) pour un arrêt immédiat
- Vérifier le détecteur de pluie
- Inspecter visuellement via la caméra

### 3.4 Procédure de rotation du dôme

**Conditions STRICTES avant de lancer la rotation :**
- [ ] ✅ Cimiers 100% ouverts
- [ ] ✅ Câble chargeur débranché
- [ ] ✅ Aucun obstacle visible (vérifier via caméra)

**Lancement :**
1. Démarrer LesveDomeNet sur le T600-NUC-TELE
2. Activer la rotation
3. Surveiller en temps réel :
   - Encodeur Grayhill : transitions régulières
   - Position Home : cohérente (valeur = 310)
   - Vitesse : stable, pas de variation
   - Mécanique : pas de bruit anormal, pas de glissement

---

## Module 4 : Opérations courantes

### 4.1 Pointage du télescope

> ⚠️ **Information importante :** À ce jour, il n'existe **pas de procédure documentée** pour l'alignement stellaire et la mise en station du T600. Les étapes ci-dessous sont indicatives et devront être complétées par votre référent technique.

**Étapes générales (à adapter selon la procédure officielle en cours d'élaboration) :**

1. **Mise en station** (polar alignment) — aligner l'axe de la monture avec l'axe de rotation de la Terre
   - Méthode recommandée : SharpCap Polar Alignment ou caméra polaire
   - Fréquence : avant chaque session d'imagerie longue pose

2. **Alignement stellaire** — apprendre au télescope où sont les étoiles
   - Utiliser NINA → Plate Solving (ASTAP)
   - Aligner sur ≥ 6 étoiles réparties dans le ciel
   - Objectif : RMS de pointage < 30 arcsec

3. **Centrage** de l'objet cible
   - Utiliser la fonction Go-To de NINA
   - Affiner avec le plate solving

### 4.2 Suivi (Tracking)

Le T600 utilise les cartes **Pléiades** (Alcyone-5 + Electra-5 + Maia-4) pour le suivi des astres :
- **Boucle fermée** : l'encodeur quadrature vérifie en permanence que le moteur suit correctement
- **Port ST-4** présent pour l'autoguidage (mais l'autoguideur n'est pas documenté — [LACUNE])

**Sans autoguidage**, la durée de pose utile est limitée à environ 30–60 secondes maximum.

**Avec autoguidage** (à installer et documenter), des poses de plusieurs minutes deviennent possibles.

### 4.3 Acquisition d'images (NINA)

1. Lancer NINA sur le T600-NUC-TELE
2. Configurer la séquence d'acquisition :
   - Filtre (si roue à filtres disponible)
   - Temps de pose
   - Nombre de poses
   - Dossier de sauvegarde
3. Lancer l'acquisition
4. Surveiller via Foscam et les logs NINA

## Module 5 : Extinction et sécurisation

### 5.1 Procédure d'extinction en 4 niveaux

#### Niveau 1 — Mécanique (cimiers)
```
1. Commande FERMETURE CIMIERS via IPX800 (S4)
2. Vérifier les fins de course : GH, GB, DY, DB
3. Vérifier qu'il n'y a plus de tension sur les moteurs
4. REBRANCHER le câble de charge de la batterie des cimiers
```

#### Niveau 2 — Cerveau informatique (arrêt OS)
```
1. Sur le T600-NUC-TELE : clic Arrêter (ou fermer session)
   → La connexion AnyDesk sera perdue si vous êtes à distance
2. Attendre l'extinction complète du système
```

#### Niveau 3 — Relais (IPX800 .238)
```
1. Interface 192.168.0.238
2. Désactiver TOUTES les sorties
3. Vérifier que toutes les lignes Output sont OFF
```

#### Niveau 4 — Énergie (IPX800 .237)
```
1. Interface 192.168.0.237
2. Commande OFF sur la ligne D0
3. Actualiser → vérifier "IPX800 éteint"
```

> ⚠️ **Ordre v1.2 (correction JP Dumoulin) :** l'arrêt informatique précède la coupure des relais pour protéger l'intégrité des fichiers d'acquisition. Le rebranchement de la batterie fait partie intégrante du Niveau 1.

### 5.2 Procédure d'urgence

| Situation | Que faire ? |
|-----------|-------------|
| **Orage imminent** | Exécuter l'extinction complète (Niveaux 1→4) immédiatement |
| **Cimiers bloqués ouverts (risque pluie)** | Commande URGENCE S5 sur IPX800 — arrêt immédiat |
| **Rotation dôme avec câble branché** | STOP immédiat via LesveDomeNet, débrancher le câble |
| **Bruit anormal mécanique** | Arrêter immédiatement, ne pas forcer |
| **Perte réseau / IPX800 injoignable** | Vérifier T600-NUC allumé, redémarrer interface, couper alimentation manuelle si nécessaire |

### 5.3 Checklist de fin de session

- [ ] Cimiers fermés
- [ ] Télescope en position Park
- [ ] Alimentation IPX800 coupée
- [ ] PCs éteints
- [ ] Bâche du télescope remise (si applicable)
- [ ] Câble de charge des cimiers rebranché (pour recharger la batterie)
- [ ] Porte de l'observatoire fermée à clé

---

## Module 6 : Diagnostic et dépannage courant

### 6.1 Problèmes fréquents et solutions

| Problème | Cause probable | Solution |
|----------|---------------|----------|
| **L'IPX800 ne répond pas** | PC NUC éteint ou WiFi coupé | Vérifier T600-NUC, vérifier Switch WiFi dôme |
| **Les cimiers ne bougent pas** | Batterie déchargée, relais collé | Vérifier tension batterie, test relais Keyes |
| **La caméra Foscam ne s'affiche pas** | Foscam T6002021 non démarré, mauvais login | Vérifier programme, login foscamt600 / T6002021 |
| **Perte connexion AnyDesk** | PC distant éteint, réseau instable | Redémarrer AnyDesk, vérifier WiFi |
| **Rotation dôme irrégulière** | Encodeur Grayhill sale ou défaillant | Nettoyer roue encodeur, vérifier transitions dans LesveDomeNet |
| **Projection planétarium tronquée** | Perte EDID (mauvais ordre allumage) | Voir Module 4.4 — commande `sos` ou `rm monitors.xml` |
| **Température anormale** | Watchdog DS18B20, ventilation Alcyone-5 | Voir 192.168.4.201, vérifier ventilation |

### 6.2 Vérifications de première ligne (avant d'appeler le support)

```
Si quelque chose ne fonctionne pas :

1. VÉRIFIER l'alimentation
   → Le PC NUC est-il allumé ?
   → L'IPX800 est-il alimenté ?
   → Les sorties IPX800 sont-elles activées et confirmées par les inputs ?

2. VÉRIFIER le réseau
   → Le Switch WiFi dôme est-il allumé ?
   → Avez-vous la bonne adresse IP ?
   → Le WiFi est-il connecté ?

3. VÉRIFIER les câbles
   → Le câble de charge des cimiers est-il débranché ?
   → Les connexions USB (Velleman) sont-elles bien en place ?

4. VÉRIFIER les logs
   → LesveDomeNet a-t-il des erreurs ?
   → NINA a-t-il des messages d'erreur ?
```

### 6.3 Quand appeler le support technique

| Situation | Action |
|-----------|--------|
| **Bruit mécanique anormal** (grincement, claquement) | ⛔ Arrêter immédiatement, ne pas forcer |
| **Odeur de brûlé** | ⛔ Couper l'alimentation générale |
| **Fumée** | ⛔ Évacuer, appeler les pompiers, couper disjoncteur |
| **Fuite d'eau** | ⛔ Couper l'électricité, protéger les équipements |
| **Problème récurrent non résolu** | Contacter le support avec description détaillée |
| **Modification matérielle nécessaire** | Ne pas modifier sans accord du responsable technique |

---

## Module 7 : Maintenance 1er niveau

### 7.1 Avant chaque session (opérateur)

| Action | Détail |
|--------|--------|
| Diagnostic télémétrique cimiers | Tension batterie, relais, NRF24L01, détecteur pluie |
| Vérification visuelle | Câbles, connecteurs, absence obstacle |
| Test communication | Vérifier que tous les équipements répondent |
| Température dôme | Vérifier via 192.168.4.201 |

### 7.2 Hebdomadaire

| Action | Détail |
|--------|--------|
| Contrôle batterie cimiers | Vérifier tension, état du chargeur |
| Nettoyage optique (si autorisé) | Soufflette optique sur les poussières (NE PAS TOUCHER LES SURFACES) |

### 7.3 Mensuel

| Action | Détail |
|--------|--------|
| Inspection ventilation Alcyone-5 | Vérifier que le ventilateur tourne (si tension >19V) |
| Nettoyage connecteurs | RJ12, ST-4, USB Velleman |
| Test arrêts d'urgence | Vérifier que S5 fonctionne |
| Test détecteur de pluie | Simuler (avec accord technique) et vérifier la réaction |
| Mise à jour logiciels | NINA, ASCOM, LesveDomeNet, système d'exploitation |

### 7.4 Trimestriel

| Action | Détail |
|--------|--------|
| Vérification encodeur Grayhill | Nettoyer la roue, vérifier les transitions |
| Contrôle variateur de fréquence | Vérifier le réglage à 24.0 Hz |
| Vérification Switch WiFi dôme | Redémarrer, vérifier la couverture |

### 7.5 Annuel (avec support technique)

| Action | Détail |
|--------|--------|
| Relevé électrique complet | Mesure tensions, courants, serrage connecteurs |
| Inspection câbles | Vérifier isolation, connecteurs, chemins de câbles |
| Maintenance moteurs | Graissage si applicable, vérification fixation |
| Révision complète | Voir documentation maintenance avancée |

### 7.6 Ce qu'il ne faut JAMAIS faire

| ❌ Action interdite | Pourquoi ? |
|---------------------|------------|
| **Toucher les surfaces optiques** | Les doigts abîment les traitements — utiliser une soufflette uniquement |
| **Forcer un mouvement mécanique** | Risque de casse irréversible |
| **Modifier un paramètre inconnu** | Peut déstabiliser tout le système |
| **Débrancher/rebrancher sans couper** | Risque de court-circuit ou de décharge électrostatique |
| **Utiliser sans supervision** | La première fois, toujours avec un opérateur expérimenté |

---

## Annexe : Lexique, références, aide-mémoire

### A.1 Lexique rapide

| Terme | Explication simple |
|-------|-------------------|
| **Ouverture** | Diamètre du miroir ou de la lentille principale — plus c'est grand, plus on capte de lumière |
| **Focale** | Distance entre le miroir/lentille et le point où l'image se forme |
| **Monture équatoriale** | Monture qui suit la rotation de la Terre — un axe pointe vers l'étoile polaire |
| **AD / DEC** | Ascension Droite (est-ouest) / Déclinaison (nord-sud) — les coordonnées célestes |
| **Cimiers** | Les volets du dôme qui s'ouvrent pour observer |
| **IPX800** | Le boîtier qui commande tout : lumières, volets, rotation |
| **NINA** | Le logiciel qui pilote les observations et la caméra |
| **Autoguidage** | Technique qui corrige automatiquement le suivi pour des photos longues |
| **Plate Solving** | Technique qui identifie les étoiles sur une photo pour savoir où pointe le télescope |
| **Collimation** | Réglage de l'alignement des miroirs pour une image nette |

### A.2 Aide-mémoire : identifiants et mots de passe

> **À conserver en lieu sûr — ne pas diffuser largement.**

| Service | Identifiant | Mot de passe |
|---------|-------------|:------------:|
| IPX800 | Admin | Oc@2018 |
| AnyDesk T600-NUC-TELE | 1 041 426 244 | T600NUC2024$#@ |
| AnyDesk T600-NUC | 513 471 809 | T6002024$#@ |
| Foscam locale | foscamt600 | T6002021 |
| myfoscam.com | jean-paul.dumoulin@skynet.be | T6002021$ |
| WiFi dôme | wireless2.4G_A84620 | Admin2021$ |
| Local 1er étage | — | forets |
| Device Foscam | FI9831P-T600 | — |

### A.3 Aide-mémoire : adresses IP

| Adresse | Qu'est-ce que c'est ? |
|---------|----------------------|
| 192.168.0.236 | Commande cimiers (wifi) |
| 192.168.0.237 | IPX800 Alimentation (ON/OFF) |
| 192.168.0.238 | IPX800 Relais E/S (Admin / Oc@2018) |
| 192.168.4.201 | Température DS18B20 |

### A.4 Aide-mémoire : ordre des opérations

```
DÉMARRAGE :
1. Préparation physique (débrancher câble cimiers, enlever bâche)
2. Allumer T600-NUC (local ou AnyDesk)
3. Alimenter IPX800 (192.168.0.237 → ON)
4. Activer sorties IPX800 (192.168.0.238)
5. Allumer T600-NUC-TELE
6. Lancer Foscam
7. Diagnostic télémétrique
8. Ouvrir cimiers (S6)
9. Rotation dôme (LesveDomeNet)
10. Utilisation astronomique

EXTINCTION :
1. Fermer cimiers (S4) + rebrancher câble batterie
2. Éteindre T600-NUC-TELE
3. T600-NUC → désactiver sorties IPX800 (192.168.0.238)
4. Couper IPX800 (192.168.0.237 → OFF)
5. Éteindre T600-NUC
6. Remettre bâche si nécessaire
```

### A.5 Aide-mémoire : sécurité

```
⚠️ DANGER MÉCANIQUE :
  - JAMAIS de rotation dôme avec câble charge cimiers branché
  - JAMAIS de forcer un mouvement

⚠️ DANGER ÉLECTRIQUE :
  - Parafoudre Type 2 absent → éviter les orages
  - Protection différentielle à vérifier

⚠️ DANGER OPTIQUE :
  - NE JAMAIS TOUCHER les surfaces des miroirs/lentilles
  - NE JAMAIS regarder le Soleil directement
```

### A.6 Références utiles

| Ressource | Où trouver |
|-----------|------------|
| Documentation technique complète T600 | `DOCUMENTATION_TECHNIQUE_T600.md` (ce dossier) |
| Fiches sources (ethnographe) | `FICHES_SOURCES_T600.md` |
| NINA (logiciel) | https://nighttime-imaging.eu/ |
| LesveDomeNet | Site Lesve (rechercher "LesveDomeNet Observatoire") |
| ASCOM Platform | https://ascom-standards.org/ |
| Support technique OCA | Contacter Jean-Paul Dumoulin ou Christian Wanlin |

### A.7 Fiche réflexe — Démarrage rapide (1 minute)

```
1. 192.168.0.237 → ON
2. 192.168.0.238 → Admin/Oc@2018 → Out → 4 boutons
3. AnyDesk → T600-NUC-TELE → 1 041 426 244 / T600NUC2024$#@
4. Foscam → foscamt600 / T6002021
5. Vérifier télémétrie → ouvrir cimiers (S6)
6. LesveDomeNet → rotation dôme
7. NINA → observations
```

### A.8 Fiche réflexe — Extinction rapide (1 minute)

```
1. Fermer cimiers (S4) + rebrancher câble batterie
2. T600-NUC-TELE → Arrêter
3. T600-NUC → IPX800 (192.168.0.238) → tout éteindre
4. IPX800 (192.168.0.237) → OFF
```

---

> ⛔ **ANNEXE FORMATEUR — NE PAS DISTRIBUER À L'APPRENANT**
> Cette annexe contient des informations pédagogiques réservées au formateur.
> Version formateur — à conserver séparément du support apprenant.

## Annexe Formateur : Guide pédagogique

### B.1 Objectifs SMART — Cadre de la session

| Critère | Objectif |
|---------|----------|
| **Spécifique** | Exécuter la séquence complète de mise en route et d'extinction du T600 : de la vérification météo au rebranchement de la batterie |
| **Mesurable** | 8 étapes clés sans erreur d'ordre (cf. grille d'évaluation §B.4) |
| **Atteignable** | Oui — démonstration par le formateur + 2 mises en situation supervisées |
| **Réaliste** | Adapté aux opérateurs OCA (tout niveau) ; aucun prérequis technique avancé |
| **Temporel** | Validé en fin de session de 3h par mise en situation complète notée |

### B.2 Pièges classiques et parades

| Piège | Fréquence | Parade formateur |
|-------|-----------|------------------|
| **Confusion .237 vs .238** | ★★★ Très fréquent | Insister sur le rôle : .237 = alimentation (ON/OFF), .238 = relais (sorties/entrées). Faire répéter à l'apprenant avant de cliquer. |
| **Oubli débrancher câble batterie** | ★★☆ Fréquent | Ajouter un post-it physique sur le dôme. Vérifier avant chaque rotation. |
| **Ordre extinction erroné** | ★★★ Très fréquent | L'apprenant a tendance à commencer par l'énergie. Rappeler : Méca → Info → Relais → Énergie. Faire réciter à voix haute. |
| **Output/Input non vérifié** | ★★☆ Fréquent | L'apprenant active les sorties sans vérifier le retour Input. Insister sur le couple Output=Input. |
| **Cimiers pas 100 % ouverts avant rotation** | ★☆☆ Occasionnel | Rappeler que LesveDomeNet peut le refuser. Vérifier visuellement via Foscam. |
| **Rebrancher batterie oublié en fin de session** | ★★★ Très fréquent | Ajouter une vérification croisée dans la checklist de fin de session. |
| **Mot de passe AnyDesk non à jour** | ★☆☆ Occasionnel | Vérifier avant la session que les mots de passe sont toujours valides. |

### B.3 Notes d'animation par module

**Module 1 — Présentation (15 min)**
- Utiliser le schéma de l'architecture (§2.1) comme fil rouge
- Insister sur les Règles d'or — les faire répéter par l'apprenant
- Vérifier la compréhension du vocabulaire de base

**Module 2 — Architecture (20 min)**
- Montrer l'armoire électrique si formation sur site (ou photos)
- Insister sur la différence .237/.238 — c'est le point de blocage n°1
- Expliquer Output/Input avec l'analogie : "Output = ce que vous demandez, Input = ce que vous recevez"
- Faire un exercice : "Je clique sur S6, que vérifiez-vous ?"

**Module 3 — Démarrage (45 min, cœur de la formation)**
- Faire une démonstration complète sans interruption (15 min)
- Puis faire exécuter par l'apprenant en guidant (15 min)
- Enfin laisser l'apprenant seul (supervision à distance) (15 min)
- Être attentif aux erreurs d'ordre et aux oublis de vérification

**Module 4 — Opérations (30 min)**
- Pour le pointage, se limiter aux bases si pas de mise en station validée
- Montrer l'interface NINA sans lancer d'acquisition réelle
- Ne pas hésiter à reporter la partie pratique à une session dédiée

**Module 5 — Extinction (30 min)**
- Insister sur les 4 niveaux et leur ordre impératif
- Vérifier que l'apprenant rebranche bien la batterie
- Faire un exercice à blanc (simulation sans vrais équipements)

**Module 6 — Diagnostic (20 min)**
- Utiliser des cas concrets : "L'IPX800 ne répond pas, que faites-vous ?"
- Montrer l'écran de l'IPX800 .238 en situation normale et en panne simulée
- Insister sur le couple Output/Input comme premier réflexe de diagnostic

**Module 7 — Maintenance (10 min)**
- Lister ce qui relève de l'opérateur vs ce qui relève du support technique
- Rappeler les actions interdites (§7.6)

### B.4 Grille d'évaluation pratique

| Compétence | Critères de réussite | Note (0–3) | Commentaires |
|------------|---------------------|:----------:|--------------|
| **1. Vérifications préalables** | Météo, accès, mots de passe prêts | | |
| **2. Préparation physique** | Câble débranché, bâche enlevée | | |
| **3. Alimentation IPX800 .237** | Adresse correcte, ON sur D0, vérifié | | |
| **4. Activation sorties .238** | Login, activation S1–S6, vérification Output=Input | | |
| **5. Connexion PC distant** | AnyDesk, Foscam opérationnels | | |
| **6. Ouverture cimiers** | S6, vérification fin de course, attente 100 % | | |
| **7. Ordre des opérations (extinction)** | Respect de l'ordre Méca→Info→Relais→Énergie | | |
| **8. Rebranchement batterie** | Effectué en fin de session | | |

**Barème :** 0 = Non acquis / 1 = Partiel (avec aide) / 2 = Acquis (en autonomie) / 3 = Maîtrisé (rapide et sûr)

**Seuil de validation :** ≥ 16/24 — et aucune note à 0 sur les critères **3**, **6**, **7** ou **8**.

### B.5 Débriefing post-évaluation

Après la mise en situation, prendre 5 minutes pour :
1. ✅ Souligner ce qui a été bien fait
2. 🔄 Revenir sur les erreurs (sans jugement)
3. 📝 Noter les points de vigilance pour la prochaine session
4. 🎯 Fixer un objectif de progression (ex. : "La prochaine fois, on vise 22/24")

### B.6 QCM enrichi — Évaluation des connaissances

#### Questions

**Q1 — Quel est le rôle de l'IPX800 .237 ?**
- A) Piloter le télescope
- B) Alimenter / couper l'alimentation générale de l'IPX800
- C) Ouvrir les cimiers
- D) Activer la caméra Foscam

**Q2 — Que signifie un écart entre Output=ON et Input=OFF sur l'IPX800 .238 ?**
- A) L'équipement fonctionne normalement
- B) L'équipement est en veille
- C) Problème : fusible, câble ou relais défectueux
- D) L'IPX800 est éteint

**Q3 — Quelle est la première action à réaliser dans la procédure d'extinction ?**
- A) Couper l'IPX800 .237
- B) Éteindre le PC T600-NUC
- C) Fermer les cimiers (commande S4)
- D) Désactiver les sorties IPX800 .238

**Q4 — Pourquoi faut-il débrancher le câble de charge des cimiers avant la rotation du dôme ?**
- A) Pour économiser l'énergie de la batterie
- B) Pour éviter un arrachement mécanique et des dommages structurels
- C) Pour ne pas user la batterie
- D) Parce que le câble gêne l'ouverture des cimiers

**Q5 — Quelle adresse IP permet de consulter la température du dôme (DS18B20) ?**
- A) 192.168.0.236
- B) 192.168.0.237
- C) 192.168.0.238
- D) 192.168.4.201

**Q6 — Quel logiciel pilote la rotation du dôme ?**
- A) NINA
- B) AnyDesk
- C) LesveDomeNet
- D) Foscam

**Q7 — Que faire si Output=ON mais Input=OFF sur S6 (cimiers) ?**
- A) Continuer, ça va s'allumer tout seul
- B) Redémarrer l'IPX800
- C) Diagnostiquer avant de continuer (fusible, câble, relais)
- D) Actionner S5 en urgence immédiatement

**Q8 — Quel est l'ordre correct de la procédure d'extinction ?**
- A) Énergie → Relais → Info → Méca
- B) Méca → Info → Relais → Énergie
- C) Relais → Méca → Info → Énergie
- D) Info → Énergie → Méca → Relais

#### Corrigé

| Q | Réponse | Justification |
|---|---------|---------------|
| 1 | B | .237 = alimentation générale (bouton ON/OFF de l'IPX800) |
| 2 | C | Un écart Output/Input signale un défaut d'alimentation : fusible, câble ou relais |
| 3 | C | Niveau 1 d'extinction = Mécanique (fermeture des cimiers via S4) |
| 4 | B | Risque d'arrachement mécanique — c'est la RÈGLE n°1 de sécurité |
| 5 | D | 192.168.4.201 = sonde DS18B20 (température dôme) |
| 6 | C | LesveDomeNet gère la rotation du dôme |
| 7 | C | Toujours diagnostiquer avant de continuer — vérifier le couple Output/Input |
| 8 | B | Méca → Info → Relais → Énergie (ordre validé par Jean-Paul Dumoulin) |

---

*Annexe formateur — version 1.1 — 12 juin 2026*
*Réservé au formateur — ne pas distribuer aux apprenants*

---

*Document généré par le Rédacteur Technique (Bureau Gérard) — 12 juin 2026*
*À distribuer à tous les opérateurs du T600 — version 1.1 — enrichie du template formateur (SMART, sémantique IPX800, QCM, guide pédagogique)*
